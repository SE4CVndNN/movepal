"""Rule-based movement validation contracts.

Contains the pure raise-both-arms movement rule described in
docs/movement_specification.md sections 6 and 12. Rules here accept the
project-level ``Landmark`` representation and configuration values only;
they never import Flask or MediaPipe, so they can be unit-tested with
plain dictionaries or the checked-in synthetic fixtures.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from app.services.pose_tracking import Landmark, landmark_distance

DEFAULT_MINIMUM_VISIBILITY = 0.5
"""Per-landmark visibility cutoff for required raise-both-arms landmarks.

Matches docs/movement_specification.md section 12's acceptance-matrix
prerequisite (``visibility >= 0.50``). A Sprint-1 game heuristic, not a
validated final value; see MP-021.
"""

DEFAULT_VERTICAL_MARGIN_RATIO = 0.40
"""Fraction of shoulder width a wrist must clear above its shoulder.

Matches the acceptance matrix's "Each wrist is at least 0.40 *
shoulder_width above its matching shoulder" progress measurement.
"""

DEFAULT_REQUIRED_CONSECUTIVE_SAMPLES = 2
"""Number of consecutive satisfying samples required before ``great``.

Matches the acceptance matrix's "true for 2 consecutive evaluated
samples" success/hold rule.
"""

RAISE_BOTH_ARMS_REQUIRED_LANDMARKS: tuple[str, ...] = (
    "left_shoulder",
    "right_shoulder",
    "left_wrist",
    "right_wrist",
    "left_hip",
    "right_hip",
)
"""Landmarks the raise-both-arms rule needs to evaluate a frame.

Elbows are deliberately excluded here even though earlier prose in
docs/movement_specification.md section 6 lists them as a "minimum
required landmark". The executable acceptance matrix's progress
measurement never reads elbow coordinates, and the checked-in negative/
borderline/low-visibility fixtures in
data/landmarks/raise_both_arms_fixtures.json omit elbow landmarks entirely
while still expecting a non-``full_body_missing`` result. Requiring
elbows here would make those fixtures fail for the wrong reason (missing
landmark) instead of the intended one (arms not raised). This is a
recorded MP-014 contract-mismatch fix; see the "MP-014 decisions" note at
the end of movement_specification.md.
"""


@dataclass(frozen=True)
class MovementResult:
    """Outcome returned by a movement rule."""

    movement: str
    completed: bool
    confidence: float
    feedback_code: str


def _raise_progress(wrist: Landmark, shoulder: Landmark, margin: float) -> float:
    """Return how far *wrist* has cleared *shoulder* relative to *margin*.

    ``1.0`` means the wrist exactly reached the required margin above the
    shoulder; more is higher, less (down to ``0.0``) is short of it.
    """
    if margin <= 0:
        return 0.0
    return max(0.0, (shoulder.y - wrist.y) / margin)


def evaluate_raise_both_arms(
    landmarks: dict[str, Landmark],
    *,
    consecutive_samples: int | None = None,
    minimum_visibility: float = DEFAULT_MINIMUM_VISIBILITY,
    vertical_margin_ratio: float = DEFAULT_VERTICAL_MARGIN_RATIO,
    required_consecutive_samples: int = DEFAULT_REQUIRED_CONSECUTIVE_SAMPLES,
) -> MovementResult:
    """Evaluate the raise-both-arms movement for a single normalized pose.

    ``consecutive_samples`` is the number of consecutive samples,
    including this one, for which the caller has observed the raised
    condition holding true (see ``observed_consecutive_samples`` in the
    checked-in fixtures). MP-014 does not implement cross-request session
    tracking, so callers that omit it get ``required_consecutive_samples``
    by default, meaning a single satisfying sample succeeds immediately.
    A future session-tracking task (MP-016) can pass a real running count
    to exercise the ``hold`` outcome across requests.

    Follows docs/movement_specification.md section 3's evaluation order:
    required landmarks, then visibility, then framing/scale, then the
    movement condition, then hold, then the final result.
    """
    if consecutive_samples is None:
        consecutive_samples = required_consecutive_samples

    for name in RAISE_BOTH_ARMS_REQUIRED_LANDMARKS:
        landmark = landmarks.get(name)
        if landmark is None or landmark.visibility < minimum_visibility:
            return MovementResult(
                movement="raise_both_arms",
                completed=False,
                confidence=0.0,
                feedback_code="full_body_missing",
            )

    left_shoulder = landmarks["left_shoulder"]
    right_shoulder = landmarks["right_shoulder"]
    left_wrist = landmarks["left_wrist"]
    right_wrist = landmarks["right_wrist"]

    shoulder_width = landmark_distance(left_shoulder, right_shoulder)
    if shoulder_width <= 0:
        return MovementResult(
            movement="raise_both_arms",
            completed=False,
            confidence=0.0,
            feedback_code="full_body_missing",
        )

    margin = vertical_margin_ratio * shoulder_width
    left_progress = _raise_progress(left_wrist, left_shoulder, margin)
    right_progress = _raise_progress(right_wrist, right_shoulder, margin)
    confidence = min(1.0, (left_progress + right_progress) / 2)
    both_raised = left_progress >= 1.0 and right_progress >= 1.0

    if not both_raised:
        return MovementResult(
            movement="raise_both_arms",
            completed=False,
            confidence=confidence,
            feedback_code="raise_arms",
        )

    if consecutive_samples < required_consecutive_samples:
        return MovementResult(
            movement="raise_both_arms",
            completed=False,
            confidence=confidence,
            feedback_code="hold",
        )

    return MovementResult(
        movement="raise_both_arms",
        completed=True,
        confidence=confidence,
        feedback_code="great",
    )


def landmarks_from_fixture(fixture: dict[str, Any]) -> dict[str, Landmark]:
    """Convert a movement fixture's name-keyed landmark dict to Landmarks."""
    raw_landmarks = fixture.get("landmarks") or {}
    return {
        name: Landmark(
            name=name,
            x=float(values["x"]),
            y=float(values["y"]),
            z=float(values.get("z", 0.0)),
            visibility=float(values["visibility"]),
        )
        for name, values in raw_landmarks.items()
    }


def load_movement_fixtures(filename: str) -> list[dict[str, Any]]:
    """Load a raw movement fixture list from data/landmarks/<filename>."""
    path = (
        Path(__file__).resolve().parent.parent.parent / "data" / "landmarks" / filename
    )
    with open(path, encoding="utf-8") as handle:
        return json.load(handle)


def load_raise_both_arms_fixture(fixture_id: str) -> dict[str, Any]:
    """Load one named fixture from raise_both_arms_fixtures.json.

    Raises KeyError if no fixture with that id exists.
    """
    for fixture in load_movement_fixtures("raise_both_arms_fixtures.json"):
        if fixture["fixture_id"] == fixture_id:
            return fixture
    raise KeyError(f"No raise_both_arms fixture named {fixture_id!r}")
