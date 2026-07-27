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

from app.services.geometry import (
    Side,
    angle_at_joint,
    horizontal_outward_offset,
    opposite_side,
    shoulder_width,
    side_landmark_name,
    vertical_offset,
)
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

    width = shoulder_width(left_shoulder, right_shoulder)
    if width <= 0:
        return MovementResult(
            movement="raise_both_arms",
            completed=False,
            confidence=0.0,
            feedback_code="full_body_missing",
        )

    margin = vertical_margin_ratio * width
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


DEFAULT_REACH_RATIO = 0.85
"""Fraction of shoulder width the requested wrist must clear outward.

Matches the acceptance matrix's "wrist is outward by >= 0.85 *
shoulder_width" progress measurement (docs/movement_specification.md
section 12).
"""

DEFAULT_REACH_VERTICAL_RATIO = 0.50
"""Fraction of shoulder width the wrist may drift vertically from its
shoulder while still counting as a side reach rather than a raised or
dropped arm. Matches the acceptance matrix's "vertical offset is <= 0.50
* shoulder_width" progress measurement.
"""

SIDE_REACH_COMMON_REQUIRED_LANDMARKS: tuple[str, ...] = (
    "left_shoulder",
    "right_shoulder",
    "left_hip",
    "right_hip",
)
"""Landmarks every side-reach evaluation needs regardless of requested side.

The requested side's own wrist is required in addition to these (see
:func:`evaluate_side_reach`). The opposite wrist and both elbows are read
by neither this rule nor the acceptance-matrix formula, mirroring the
raise-both-arms elbow exclusion recorded above and in the "MP-014
decisions" note in movement_specification.md: requiring them would fail
the checked-in side_reach_fixtures.json positive/wrong-side cases, which
omit them, for the wrong reason (missing landmark instead of insufficient
reach).
"""


def evaluate_side_reach(
    landmarks: dict[str, Landmark],
    requested_side: Side,
    *,
    consecutive_samples: int | None = None,
    minimum_visibility: float = DEFAULT_MINIMUM_VISIBILITY,
    reach_ratio: float = DEFAULT_REACH_RATIO,
    vertical_ratio: float = DEFAULT_REACH_VERTICAL_RATIO,
    required_consecutive_samples: int = DEFAULT_REQUIRED_CONSECUTIVE_SAMPLES,
    lenient: bool = False,
) -> MovementResult:
    """Evaluate a side-reach movement for one requested anatomical side.

    ``requested_side`` is the user's own side, never the mirrored
    preview's screen side (docs/movement_specification.md section 2).
    Only the requested side's own shoulder/wrist pair is read, so an
    opposite-arm reach can never satisfy the request regardless of how
    far it extends.

    ``consecutive_samples`` follows the same per-request hold contract as
    :func:`evaluate_raise_both_arms`: omitting it assumes the hold
    requirement is already satisfied, so a single satisfying sample
    succeeds immediately; a caller exercising ``hold`` must pass a lower
    count explicitly.

    Follows docs/movement_specification.md section 3's evaluation order:
    required landmarks, then visibility, then framing/scale, then the
    movement condition, then hold, then the final result.
    """
    if consecutive_samples is None:
        consecutive_samples = required_consecutive_samples

    feedback_code = f"reach_{requested_side}"
    requested_wrist_name = side_landmark_name(requested_side, "wrist")
    requested_elbow_name = side_landmark_name(requested_side, "elbow")
    opposite_side_name = opposite_side(requested_side)
    opposite_wrist_name = side_landmark_name(opposite_side_name, "wrist")
    opposite_elbow_name = side_landmark_name(opposite_side_name, "elbow")
    if lenient:
        # Live camera and uploaded-image evaluation only needs the torso scale
        # and the requested arm. Requiring the opposite arm and both hips made
        # an otherwise clear side reach fail when those unrelated landmarks
        # were cropped or briefly low visibility.
        required = (
            "left_shoulder",
            "right_shoulder",
            requested_elbow_name,
            requested_wrist_name,
        )
    else:
        required = SIDE_REACH_COMMON_REQUIRED_LANDMARKS + (
            requested_elbow_name,
            requested_wrist_name,
            opposite_elbow_name,
            opposite_wrist_name,
        )

    for name in required:
        landmark = landmarks.get(name)
        if landmark is None or landmark.visibility < minimum_visibility:
            return MovementResult(
                movement="side_reach",
                completed=False,
                confidence=0.0,
                feedback_code="full_body_missing",
            )

    left_shoulder = landmarks["left_shoulder"]
    right_shoulder = landmarks["right_shoulder"]
    width = shoulder_width(left_shoulder, right_shoulder)
    if width <= 0:
        return MovementResult(
            movement="side_reach",
            completed=False,
            confidence=0.0,
            feedback_code="full_body_missing",
        )

    requested_shoulder = left_shoulder if requested_side == "left" else right_shoulder
    wrist = landmarks[requested_wrist_name]
    elbow = landmarks[requested_elbow_name]
    opposite_shoulder = right_shoulder if requested_side == "left" else left_shoulder

    # Allow a more forgiving set of thresholds for live/uploaded frames
    # when callers explicitly request lenient mode (helps users get
    # immediate feedback in imperfect home setups). Fixtures and the
    # deterministic `/api/movement` path remain strict.
    effective_reach_ratio = reach_ratio
    effective_vertical_ratio = vertical_ratio
    elbow_angle_threshold = 170.0
    if lenient:
        # More aggressive leniency for live uploads: reduce required
        # outward reach, allow more vertical drift, and accept more
        # elbow bend. Also skip strict shoulder-level enforcement to
        # accommodate casual phone framing.
        effective_reach_ratio = min(reach_ratio, 0.74)
        effective_vertical_ratio = max(vertical_ratio, 0.9)
        elbow_angle_threshold = 125.0

    outward = horizontal_outward_offset(
        wrist,
        requested_shoulder,
        requested_side,
        opposite_shoulder,
    )
    elbow_outward = horizontal_outward_offset(
        elbow,
        requested_shoulder,
        requested_side,
        opposite_shoulder,
    )
    wrist_height_ok = (
        vertical_offset(wrist, requested_shoulder) <= effective_vertical_ratio * width
    )
    elbow_height_ok = (
        vertical_offset(elbow, requested_shoulder) <= effective_vertical_ratio * width
    )
    elbow_angle = angle_at_joint(requested_shoulder, elbow, wrist)
    # In lenient mode, allow looser shoulder alignment by skipping the
    # strict shoulder-level check; hip alignment still helps detect
    # gross framing issues.
    if lenient:
        shoulder_level_ok = True
    else:
        shoulder_level_ok = abs(left_shoulder.y - right_shoulder.y) <= (
            effective_vertical_ratio * width
        )

    # In lenient mode, skip hip-level enforcement as well to tolerate
    # casual framing and minor stance shifts in uploaded photos.
    if lenient:
        hip_level_ok = True
        opposite_arm_relaxed = True
    else:
        left_hip = landmarks["left_hip"]
        right_hip = landmarks["right_hip"]
        hip_level_ok = abs(left_hip.y - right_hip.y) <= (
            effective_vertical_ratio * width
        )
        opposite_elbow = landmarks[opposite_elbow_name]
        opposite_wrist = landmarks[opposite_wrist_name]
        opposite_arm_relaxed = (
            opposite_wrist.y >= opposite_elbow.y
            and opposite_elbow.y >= opposite_shoulder.y
        )
    elbow_in_line = elbow_outward >= 0 and outward >= elbow_outward
    confidence = (
        min(1.0, max(0.0, outward) / (effective_reach_ratio * width))
        if effective_reach_ratio > 0
        else 0.0
    )

    if not elbow_in_line or not elbow_height_ok or elbow_angle < elbow_angle_threshold:
        return MovementResult(
            movement="side_reach",
            completed=False,
            confidence=confidence,
            feedback_code=feedback_code,
        )

    if not opposite_arm_relaxed:
        return MovementResult(
            movement="side_reach",
            completed=False,
            confidence=confidence,
            feedback_code=feedback_code,
        )

    if not shoulder_level_ok or not hip_level_ok:
        return MovementResult(
            movement="side_reach",
            completed=False,
            confidence=confidence,
            feedback_code=feedback_code,
        )

    reached = wrist_height_ok and outward >= effective_reach_ratio * width

    if not reached:
        return MovementResult(
            movement="side_reach",
            completed=False,
            confidence=confidence,
            feedback_code=feedback_code,
        )

    if consecutive_samples < required_consecutive_samples:
        return MovementResult(
            movement="side_reach",
            completed=False,
            confidence=confidence,
            feedback_code="hold",
        )

    return MovementResult(
        movement="side_reach",
        completed=True,
        confidence=confidence,
        feedback_code="great",
    )


DEFAULT_KNEE_LIFT_RATIO = 0.35
"""Maximum selected hip-to-knee vertical offset as a fraction of leg scale."""


def evaluate_knee_lift(
    landmarks: dict[str, Landmark],
    requested_side: Side,
    *,
    consecutive_samples: int | None = None,
    minimum_visibility: float = DEFAULT_MINIMUM_VISIBILITY,
    lift_ratio: float = DEFAULT_KNEE_LIFT_RATIO,
    required_consecutive_samples: int = DEFAULT_REQUIRED_CONSECUTIVE_SAMPLES,
) -> MovementResult:
    """Evaluate a knee lift for one requested anatomical side.

    ``requested_side`` names the user's anatomical side; preview mirroring
    does not change it. As with the existing movement rules, omitting
    ``consecutive_samples`` assumes the required hold count is satisfied.

    Confidence is the allowed hip-to-knee vertical offset divided by the
    observed downward offset, capped to ``[0.0, 1.0]``. A satisfying
    position therefore has confidence ``1.0``; unusable input has ``0.0``.
    This is deterministic game-rule progress, not a clinical measure.
    """
    if consecutive_samples is None:
        consecutive_samples = required_consecutive_samples

    selected_hip_name = side_landmark_name(requested_side, "hip")
    selected_knee_name = side_landmark_name(requested_side, "knee")
    selected_ankle_name = side_landmark_name(requested_side, "ankle")
    other_side = opposite_side(requested_side)
    opposite_hip_name = side_landmark_name(other_side, "hip")
    opposite_ankle_name = side_landmark_name(other_side, "ankle")
    required = (
        selected_hip_name,
        selected_knee_name,
        selected_ankle_name,
        opposite_hip_name,
        opposite_ankle_name,
    )

    for name in required:
        landmark = landmarks.get(name)
        if landmark is None or landmark.visibility < minimum_visibility:
            return MovementResult(
                movement="knee_lift_or_step",
                completed=False,
                confidence=0.0,
                feedback_code="full_body_missing",
            )

    selected_hip = landmarks[selected_hip_name]
    selected_knee = landmarks[selected_knee_name]
    selected_ankle = landmarks[selected_ankle_name]
    leg_scale = landmark_distance(selected_hip, selected_ankle)
    if leg_scale <= 0:
        return MovementResult(
            movement="knee_lift_or_step",
            completed=False,
            confidence=0.0,
            feedback_code="full_body_missing",
        )

    allowed_offset = lift_ratio * leg_scale
    observed_offset = selected_knee.y - selected_hip.y
    knee_lifted = selected_knee.y <= selected_hip.y + allowed_offset
    if knee_lifted:
        confidence = 1.0
    elif allowed_offset > 0 and observed_offset > 0:
        confidence = min(1.0, allowed_offset / observed_offset)
    else:
        confidence = 0.0

    if not knee_lifted:
        return MovementResult(
            movement="knee_lift_or_step",
            completed=False,
            confidence=confidence,
            feedback_code="lift_knee",
        )

    if consecutive_samples < required_consecutive_samples:
        return MovementResult(
            movement="knee_lift_or_step",
            completed=False,
            confidence=confidence,
            feedback_code="hold",
        )

    return MovementResult(
        movement="knee_lift_or_step",
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


def load_side_reach_fixture(fixture_id: str) -> dict[str, Any]:
    """Load one named fixture from side_reach_fixtures.json.

    Raises KeyError if no fixture with that id exists.
    """
    for fixture in load_movement_fixtures("side_reach_fixtures.json"):
        if fixture["fixture_id"] == fixture_id:
            return fixture
    raise KeyError(f"No side_reach fixture named {fixture_id!r}")


def load_knee_lift_fixture(fixture_id: str) -> dict[str, Any]:
    """Load one named fixture from knee_lift_fixtures.json.

    Raises KeyError if no fixture with that id exists.
    """
    for fixture in load_movement_fixtures("knee_lift_fixtures.json"):
        if fixture["fixture_id"] == fixture_id:
            return fixture
    raise KeyError(f"No knee_lift fixture named {fixture_id!r}")
