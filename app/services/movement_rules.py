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
    opposite_side,
    shoulder_width,
    side_landmark_name,
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
)
"""Landmarks the raise-both-arms rule needs to evaluate a frame.

Elbows and hips are deliberately excluded because the executable rule uses
only shoulder width and each wrist's height relative to its matching shoulder.
The checked-in negative/borderline/low-visibility fixtures in
data/landmarks/raise_both_arms_fixtures.json omit elbow landmarks entirely
while still expecting a non-``full_body_missing`` result. Requiring
unread lower-body landmarks also prevents a valid upper-body camera frame
from being evaluated. See the ``MP-014 decisions`` note in
docs/movement_specification.md.
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


DEFAULT_SIDE_BEND_RATIO = 0.18
"""Minimum lateral torso displacement as a fraction of shoulder width."""

DEFAULT_OVERHEAD_HEIGHT_RATIO = 0.35
"""Minimum height the active wrist must clear above its shoulder."""

DEFAULT_OVERHEAD_CROSS_RATIO = 0.20
"""Minimum distance the active wrist reaches toward the requested side."""

SIDE_REACH_COMMON_REQUIRED_LANDMARKS: tuple[str, ...] = (
    "left_shoulder",
    "right_shoulder",
    "left_hip",
    "right_hip",
)
"""Torso landmarks required to detect the pictured lateral body bend."""


def evaluate_side_reach(
    landmarks: dict[str, Landmark],
    requested_side: Side,
    *,
    consecutive_samples: int | None = None,
    minimum_visibility: float = DEFAULT_MINIMUM_VISIBILITY,
    bend_ratio: float = DEFAULT_SIDE_BEND_RATIO,
    overhead_height_ratio: float = DEFAULT_OVERHEAD_HEIGHT_RATIO,
    overhead_cross_ratio: float = DEFAULT_OVERHEAD_CROSS_RATIO,
    required_consecutive_samples: int = DEFAULT_REQUIRED_CONSECUTIVE_SAMPLES,
    lenient: bool = False,
) -> MovementResult:
    """Evaluate the pictured standing side bend in either anatomical direction.

    ``requested_side`` is the direction the user's torso should bend. A
    left bend uses the right arm overhead; a right bend uses the left arm.
    The direction is derived from the observed anatomical shoulders, so
    horizontally mirrored camera frames produce the same result.

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
    active_arm_side = opposite_side(requested_side)
    active_shoulder_name = side_landmark_name(active_arm_side, "shoulder")
    active_elbow_name = side_landmark_name(active_arm_side, "elbow")
    active_wrist_name = side_landmark_name(active_arm_side, "wrist")
    requested_shoulder_name = side_landmark_name(requested_side, "shoulder")
    required = SIDE_REACH_COMMON_REQUIRED_LANDMARKS + (
        active_elbow_name,
        active_wrist_name,
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

    requested_shoulder = landmarks[requested_shoulder_name]
    active_shoulder = landmarks[active_shoulder_name]
    elbow = landmarks[active_elbow_name]
    wrist = landmarks[active_wrist_name]
    left_hip = landmarks["left_hip"]
    right_hip = landmarks["right_hip"]

    # `side_direction` points toward the requested anatomical side in the
    # observed frame. It flips automatically if the input is mirrored.
    side_direction = -1.0 if requested_shoulder.x < active_shoulder.x else 1.0
    shoulder_mid_x = (left_shoulder.x + right_shoulder.x) / 2
    hip_mid_x = (left_hip.x + right_hip.x) / 2
    lateral_bend = (shoulder_mid_x - hip_mid_x) * side_direction
    overhead_height = active_shoulder.y - wrist.y
    overhead_cross = (wrist.x - active_shoulder.x) * side_direction
    elbow_angle = angle_at_joint(active_shoulder, elbow, wrist)

    effective_bend_ratio = min(bend_ratio, 0.12) if lenient else bend_ratio
    effective_height_ratio = (
        min(overhead_height_ratio, 0.25) if lenient else overhead_height_ratio
    )
    effective_cross_ratio = (
        min(overhead_cross_ratio, 0.10) if lenient else overhead_cross_ratio
    )
    elbow_angle_threshold = 110.0 if lenient else 125.0

    bend_progress = lateral_bend / (effective_bend_ratio * width)
    height_progress = overhead_height / (effective_height_ratio * width)
    cross_progress = overhead_cross / (effective_cross_ratio * width)
    confidence = min(
        1.0,
        max(
            0.0,
            min(bend_progress, height_progress, cross_progress),
        ),
    )

    reached = (
        lateral_bend >= effective_bend_ratio * width
        and overhead_height >= effective_height_ratio * width
        and overhead_cross >= effective_cross_ratio * width
        and elbow_angle >= elbow_angle_threshold
    )

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
