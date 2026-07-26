"""Pose tracking adapter.

Converts third-party pose-estimation output into a small, project-owned
result contract (:class:`PoseResult`) so that routes and movement rules
never import or depend on MediaPipe objects directly.

Two ways to obtain a :class:`PoseResult` are supported:

- :class:`MediaPipePoseAdapter`, which wraps the MediaPipe Tasks
  ``PoseLandmarker`` for a real image. This path requires the
  ``mediapipe`` package and a downloaded ``.task`` model bundle, so it is
  never exercised in CI tests.
- :func:`load_pose_fixture`, which reads a tiny synthetic landmark JSON
  fixture from ``data/landmarks/pose_fixtures.json``. This path needs no
  camera, image, model download, or personal data and is what CI/unit
  tests use.

Landmark coordinate convention (see docs/adr/002-pose-estimator.md and
docs/movement_specification.md for the full compatibility write-up):

- ``x``, ``y`` are normalized image coordinates in ``[0, 1]`` from the
  top-left corner of the *raw, unmirrored* input frame: larger ``x`` is
  further right, larger ``y`` is further down (so a raised wrist has a
  *smaller* ``y`` than the shoulder).
- ``z`` is roughly hip-relative depth on a similar scale to ``x``;
  smaller (more negative) is closer to the camera. Sprint 1 movement
  rules do not depend on ``z``.
- ``left_*`` / ``right_*`` names refer to the subject's anatomical
  side in that raw frame, matching MediaPipe's own convention. If the
  browser shows the user a mirrored ("selfie") preview for comfort, that
  mirroring must stay a display-only concern: the frame sent for pose
  processing must not be flipped, or the anatomical labels would be
  swapped.
- A missing landmark is simply absent from :attr:`PoseResult.landmarks`;
  callers must not assume every name is present.
"""

from __future__ import annotations

import json
from collections.abc import Sequence
from dataclasses import dataclass, field
from enum import StrEnum
from pathlib import Path
from typing import Any

DEFAULT_VISIBILITY_THRESHOLD = 0.5
"""Starting per-landmark visibility cutoff.

This is a game heuristic used during the spike, not a validated final
value. See docs/movement_specification.md section 4; MP-021 must record
the justified final threshold(s).
"""

DEFAULT_MINIMUM_COVERAGE = 0.35
"""Fraction of TRACKED_LANDMARK_NAMES that must clear the visibility
threshold before a detected pose counts as PoseStatus.SUCCESS rather than
PoseStatus.LOW_VISIBILITY. The Sprint-1 game experience is intentionally
more forgiving so children can play without needing a perfect full-body
frame."""

# When validating external evidence (conservative mode) require a higher
# fraction of visible tracked landmarks so incomplete samples are flagged
# as LOW_VISIBILITY.
CONSERVATIVE_MINIMUM_COVERAGE = 0.75


TRACKED_LANDMARK_NAMES: tuple[str, ...] = (
    "left_shoulder",
    "right_shoulder",
    "left_elbow",
    "right_elbow",
    "left_wrist",
    "right_wrist",
    "left_hip",
    "right_hip",
    "left_knee",
    "right_knee",
    "left_ankle",
    "right_ankle",
)
"""Landmark names the pose adapter extracts and movement rules may use.

Covers the shoulder/elbow/wrist/hip/knee landmarks named in MP-005, plus
ankle, which docs/movement_specification.md's knee-lift/step movement
also requires.
"""

_MEDIAPIPE_LANDMARK_INDEX: dict[str, int] = {
    "left_shoulder": 11,
    "right_shoulder": 12,
    "left_elbow": 13,
    "right_elbow": 14,
    "left_wrist": 15,
    "right_wrist": 16,
    "left_hip": 23,
    "right_hip": 24,
    "left_knee": 25,
    "right_knee": 26,
    "left_ankle": 27,
    "right_ankle": 28,
}
"""MediaPipe Pose Landmarker index for each name in TRACKED_LANDMARK_NAMES.

See https://ai.google.dev/edge/mediapipe/solutions/vision/pose_landmarker
for the full 33-point topology; only the subset MovePal's movements need
is mapped here.
"""


@dataclass(frozen=True)
class Landmark:
    """Normalized pose landmark used by movement rules."""

    name: str
    x: float
    y: float
    z: float
    visibility: float


class PoseStatus(StrEnum):
    """Outcome of a single pose-estimation attempt."""

    SUCCESS = "success"
    NO_POSE = "no_pose"
    LOW_VISIBILITY = "low_visibility"
    ERROR = "error"


@dataclass(frozen=True)
class PoseResult:
    """Project-owned result of a pose-estimation attempt.

    ``landmarks`` is keyed by name so routes and movement rules never
    need to know a provider-specific index or object type.
    """

    status: PoseStatus
    landmarks: dict[str, Landmark] = field(default_factory=dict)
    error: str | None = None


def visible_landmarks(
    landmarks: Sequence[Landmark],
    minimum_visibility: float = DEFAULT_VISIBILITY_THRESHOLD,
) -> list[Landmark]:
    """Return landmarks that satisfy the selected visibility threshold."""
    return [item for item in landmarks if item.visibility >= minimum_visibility]


def landmark_distance(first: Landmark, second: Landmark) -> float:
    """Euclidean distance between two landmarks in normalized x/y space.

    ``z`` is excluded because docs/movement_specification.md's relative
    measurements (``shoulder_width``, ``leg_scale``, reach ratios, ...) are
    all defined in the normalized image plane. Movement rules use this to
    turn raw coordinates into body-scale-relative ratios, which stay
    meaningful across different camera distances and framing -- unlike a
    raw pixel/coordinate distance on its own.
    """
    return ((first.x - second.x) ** 2 + (first.y - second.y) ** 2) ** 0.5


def _status_for_landmarks(
    landmarks: dict[str, Landmark],
    minimum_visibility: float,
    minimum_coverage: float,
    coverage_denominator: int | None = None,
) -> PoseStatus:
    if not landmarks:
        return PoseStatus.NO_POSE

    tracked = [landmarks[name] for name in TRACKED_LANDMARK_NAMES if name in landmarks]
    if not tracked:
        return PoseStatus.LOW_VISIBILITY

    visible_count = len(visible_landmarks(tracked, minimum_visibility))
    # Coverage denominator may be provided by the caller. When validating
    # external assets we default to the full set of tracked landmark names
    # (conservative). When converting a checked-in fixture to a PoseResult
    # we pass the number of present tracked landmarks so existing fixture
    # semantics are preserved.
    denom = (
        coverage_denominator
        if coverage_denominator is not None
        else len(TRACKED_LANDMARK_NAMES)
    )
    coverage = visible_count / denom
    if coverage < minimum_coverage:
        return PoseStatus.LOW_VISIBILITY
    return PoseStatus.SUCCESS


class MediaPipePoseAdapter:
    """Adapts the MediaPipe Tasks PoseLandmarker to :class:`PoseResult`.

    ``mediapipe`` is imported lazily inside :meth:`estimate` rather than
    at module load time, so importing ``app.services.pose_tracking`` (and
    running fixture-based tests) never requires MediaPipe's native
    libraries or a downloaded model to be present.
    """

    def __init__(
        self,
        model_path: str | Path,
        minimum_visibility: float = DEFAULT_VISIBILITY_THRESHOLD,
        minimum_coverage: float = DEFAULT_MINIMUM_COVERAGE,
    ) -> None:
        self._model_path = str(model_path)
        self._minimum_visibility = minimum_visibility
        self._minimum_coverage = minimum_coverage
        self._landmarker: Any | None = None

    def _get_landmarker(self) -> Any:
        if self._landmarker is None:
            from mediapipe.tasks.python import BaseOptions, vision

            options = vision.PoseLandmarkerOptions(
                base_options=BaseOptions(model_asset_path=self._model_path),
                running_mode=vision.RunningMode.IMAGE,
            )
            self._landmarker = vision.PoseLandmarker.create_from_options(options)
        return self._landmarker

    def estimate(self, image_path: str | Path) -> PoseResult:
        """Run pose estimation on an image file and return a PoseResult.

        Any decode/model/inference failure is caught and returned as
        PoseStatus.ERROR rather than raised, per the architecture's
        "controlled unable-to-process result rather than crashing" rule.
        """
        try:
            import mediapipe as mp

            landmarker = self._get_landmarker()
            mp_image = mp.Image.create_from_file(str(image_path))
            result = landmarker.detect(mp_image)
        except Exception as exc:  # noqa: BLE001 - convert any provider failure
            return PoseResult(status=PoseStatus.ERROR, error=str(exc))

        if not result.pose_landmarks:
            return PoseResult(status=PoseStatus.NO_POSE)

        raw = result.pose_landmarks[0]
        landmarks = {
            name: Landmark(
                name=name,
                x=raw[index].x,
                y=raw[index].y,
                z=raw[index].z,
                visibility=raw[index].visibility,
            )
            for name, index in _MEDIAPIPE_LANDMARK_INDEX.items()
        }
        status = _status_for_landmarks(
            landmarks, self._minimum_visibility, self._minimum_coverage
        )
        return PoseResult(status=status, landmarks=landmarks)


def _landmark_from_fixture(name: str, data: dict[str, float]) -> Landmark:
    return Landmark(
        name=name,
        x=float(data["x"]),
        y=float(data["y"]),
        z=float(data.get("z", 0.0)),
        visibility=float(data["visibility"]),
    )


def pose_result_from_fixture_data(
    fixture: dict[str, Any],
    minimum_visibility: float = DEFAULT_VISIBILITY_THRESHOLD,
    minimum_coverage: float = DEFAULT_MINIMUM_COVERAGE,
    *,
    conservative: bool = False,
) -> PoseResult:
    """Build a PoseResult from an already-loaded fixture dict.

    Exercises the same status logic as MediaPipePoseAdapter.estimate so
    that a real sample and an offline fixture produce results through the
    identical contract.
    """
    raw_landmarks = fixture.get("landmarks") or {}
    landmarks = {
        name: _landmark_from_fixture(name, values)
        for name, values in raw_landmarks.items()
    }
    # Determine coverage denominator:
    # - If `conservative` is True (external evidence), validate against the
    #   full set of tracked landmark names so incomplete fixtures are
    #   flagged as LOW_VISIBILITY.
    # - Otherwise (checked-in fixtures), use the number of present tracked
    #   landmarks so existing fixture semantics remain unchanged.
    if conservative:
        # Conservative mode uses the full tracked-landmark denominator and
        # a stricter minimum coverage threshold so incomplete fixtures are
        # flagged as LOW_VISIBILITY.
        coverage_denominator = None
        minimum_coverage = max(minimum_coverage, CONSERVATIVE_MINIMUM_COVERAGE)
    else:
        tracked_present = [name for name in TRACKED_LANDMARK_NAMES if name in landmarks]
        coverage_denominator = len(tracked_present) if tracked_present else None

    status = _status_for_landmarks(
        landmarks,
        minimum_visibility,
        minimum_coverage,
        coverage_denominator=coverage_denominator,
    )
    return PoseResult(status=status, landmarks=landmarks)


def load_pose_fixtures(fixture_path: str | Path | None = None) -> list[dict[str, Any]]:
    """Load the raw fixture records from data/landmarks/pose_fixtures.json."""
    if fixture_path is None:
        fixture_path = (
            Path(__file__).resolve().parent.parent.parent
            / "data"
            / "landmarks"
            / "pose_fixtures.json"
        )
    with open(fixture_path, encoding="utf-8") as handle:
        return json.load(handle)


def load_pose_fixture(
    fixture_id: str, fixture_path: str | Path | None = None
) -> PoseResult:
    """Load one named fixture and convert it to a PoseResult.

    Raises KeyError if no fixture with that id exists.
    """
    fixtures = load_pose_fixtures(fixture_path)
    for fixture in fixtures:
        if fixture["fixture_id"] == fixture_id:
            return pose_result_from_fixture_data(fixture)
    raise KeyError(f"No pose fixture named {fixture_id!r}")
