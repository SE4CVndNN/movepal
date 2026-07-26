"""Unit tests for the pure raise-both-arms movement rule."""

from __future__ import annotations

import pytest

from app.services.feedback import FEEDBACK_MESSAGES
from app.services.movement_rules import (
    evaluate_knee_lift,
    evaluate_raise_both_arms,
    evaluate_side_reach,
    landmarks_from_fixture,
    load_knee_lift_fixture,
    load_raise_both_arms_fixture,
    load_side_reach_fixture,
)
from app.services.pose_tracking import Landmark

FIXTURE_CASES = [
    ("synthetic_raise_arms_positive_001", True, "great"),
    ("synthetic_raise_arms_negative_001", False, "raise_arms"),
    ("synthetic_raise_arms_borderline_001", False, "raise_arms"),
    ("synthetic_raise_arms_low_visibility_001", False, "full_body_missing"),
]


@pytest.mark.parametrize("fixture_id, expected_completed, expected_code", FIXTURE_CASES)
def test_committed_fixtures_match_expected_outcome(
    fixture_id, expected_completed, expected_code
):
    fixture = load_raise_both_arms_fixture(fixture_id)
    landmarks = landmarks_from_fixture(fixture)

    result = evaluate_raise_both_arms(
        landmarks,
        consecutive_samples=fixture["observed_consecutive_samples"],
    )

    assert result.movement == "raise_both_arms"
    assert result.completed is expected_completed
    assert result.feedback_code == expected_code
    assert fixture["expected_completed"] == expected_completed
    assert fixture["expected_feedback_code"] == expected_code


def test_unknown_fixture_id_raises_key_error():
    with pytest.raises(KeyError):
        load_raise_both_arms_fixture("does_not_exist")


def _base_landmarks() -> dict[str, Landmark]:
    """Both shoulders/hips at a neutral stance; wrists start down."""
    return {
        "left_shoulder": Landmark("left_shoulder", 0.3, 0.4, 0.0, 0.9),
        "right_shoulder": Landmark("right_shoulder", 0.7, 0.4, 0.0, 0.9),
        "left_wrist": Landmark("left_wrist", 0.3, 0.65, 0.0, 0.9),
        "right_wrist": Landmark("right_wrist", 0.7, 0.65, 0.0, 0.9),
        "left_hip": Landmark("left_hip", 0.35, 0.65, 0.0, 0.9),
        "right_hip": Landmark("right_hip", 0.65, 0.65, 0.0, 0.9),
    }


def test_only_left_arm_raised_does_not_complete():
    landmarks = _base_landmarks()
    landmarks["left_wrist"] = Landmark("left_wrist", 0.3, 0.1, 0.0, 0.9)

    result = evaluate_raise_both_arms(landmarks, consecutive_samples=2)

    assert result.completed is False
    assert result.feedback_code == "raise_arms"


def test_only_right_arm_raised_does_not_complete():
    landmarks = _base_landmarks()
    landmarks["right_wrist"] = Landmark("right_wrist", 0.7, 0.1, 0.0, 0.9)

    result = evaluate_raise_both_arms(landmarks, consecutive_samples=2)

    assert result.completed is False
    assert result.feedback_code == "raise_arms"


def test_both_arms_down_returns_raise_arms():
    landmarks = _base_landmarks()

    result = evaluate_raise_both_arms(landmarks, consecutive_samples=2)

    assert result.completed is False
    assert result.feedback_code == "raise_arms"


def test_missing_required_landmark_returns_full_body_missing():
    landmarks = _base_landmarks()
    del landmarks["right_wrist"]

    result = evaluate_raise_both_arms(landmarks, consecutive_samples=2)

    assert result.completed is False
    assert result.feedback_code == "full_body_missing"
    assert result.confidence == 0.0


def test_condition_met_but_insufficient_consecutive_samples_holds():
    fixture = load_raise_both_arms_fixture("synthetic_raise_arms_positive_001")
    landmarks = landmarks_from_fixture(fixture)

    result = evaluate_raise_both_arms(landmarks, consecutive_samples=1)

    assert result.completed is False
    assert result.feedback_code == "hold"


def test_default_consecutive_samples_assumes_hold_already_satisfied():
    fixture = load_raise_both_arms_fixture("synthetic_raise_arms_positive_001")
    landmarks = landmarks_from_fixture(fixture)

    result = evaluate_raise_both_arms(landmarks)

    assert result.completed is True
    assert result.feedback_code == "great"


def test_zero_shoulder_width_is_treated_as_framing_failure():
    landmarks = _base_landmarks()
    landmarks["right_shoulder"] = Landmark(
        "right_shoulder",
        landmarks["left_shoulder"].x,
        landmarks["left_shoulder"].y,
        0.0,
        0.9,
    )

    result = evaluate_raise_both_arms(landmarks, consecutive_samples=2)

    assert result.completed is False
    assert result.feedback_code == "full_body_missing"


# --- Side reach ------------------------------------------------------------
#
# The requested side always refers to the user's own anatomical side, never
# the mirrored preview's screen side (docs/movement_specification.md section
# 2). Tests below are parametrized over ("left", "right") wherever the
# scenario should behave identically once mirrored, so a left/right
# asymmetry bug shows up as one parametrized case failing rather than a
# hand-duplicated pair silently drifting apart.

SIDE_REACH_FIXTURE_CASES = [
    ("synthetic_side_reach_left_positive_001", "left", True, "great"),
    ("synthetic_side_reach_right_negative_001", "right", False, "reach_right"),
    ("synthetic_side_reach_left_borderline_001", "left", False, "reach_left"),
    (
        "synthetic_side_reach_right_low_visibility_001",
        "right",
        False,
        "full_body_missing",
    ),
]


@pytest.mark.parametrize(
    "fixture_id, side, expected_completed, expected_code", SIDE_REACH_FIXTURE_CASES
)
def test_side_reach_committed_fixtures_match_expected_outcome(
    fixture_id, side, expected_completed, expected_code
):
    fixture = load_side_reach_fixture(fixture_id)
    landmarks = landmarks_from_fixture(fixture)

    result = evaluate_side_reach(
        landmarks,
        side,
        consecutive_samples=fixture["observed_consecutive_samples"],
    )

    assert result.movement == "side_reach"
    assert result.completed is expected_completed
    assert result.feedback_code == expected_code
    assert fixture["requested_side"] == side
    assert fixture["expected_completed"] == expected_completed
    assert fixture["expected_feedback_code"] == expected_code


def test_unknown_side_reach_fixture_id_raises_key_error():
    with pytest.raises(KeyError):
        load_side_reach_fixture("does_not_exist")


def _side_reach_landmarks(
    side: str, outward_ratio: float, vertical_ratio: float = 0.0
) -> dict[str, Landmark]:
    """Build a minimal side-reach pose for *side*.

    The requested wrist is placed ``outward_ratio * shoulder_width``
    beyond its shoulder (and ``vertical_ratio * shoulder_width`` above or
    below it). Calling this with "left" and "right" for the same ratios
    produces literal mirror images across the body midline, so the same
    assertions can be parametrized over both sides to prove symmetry by
    construction rather than by hand-authoring two matching fixtures.
    """
    shoulder_width_value = 0.3
    left_shoulder_x, right_shoulder_x = 0.35, 0.65
    shoulder_y = 0.4
    shoulder_x = left_shoulder_x if side == "left" else right_shoulder_x
    sign = -1 if side == "left" else 1
    wrist_x = shoulder_x + sign * outward_ratio * shoulder_width_value
    wrist_y = shoulder_y + vertical_ratio * shoulder_width_value
    opposite_side_name = "right" if side == "left" else "left"
    opposite_shoulder_x = right_shoulder_x if side == "left" else left_shoulder_x
    opposite_elbow_x = 0.55 if side == "left" else 0.45
    opposite_wrist_x = 0.6 if side == "left" else 0.4
    return {
        "left_shoulder": Landmark(
            "left_shoulder", left_shoulder_x, shoulder_y, 0.0, 0.9
        ),
        "right_shoulder": Landmark(
            "right_shoulder", right_shoulder_x, shoulder_y, 0.0, 0.9
        ),
        f"{side}_elbow": Landmark(
            f"{side}_elbow",
            shoulder_x + sign * 0.35 * shoulder_width_value,
            shoulder_y,
            0.0,
            0.9,
        ),
        f"{side}_wrist": Landmark(f"{side}_wrist", wrist_x, wrist_y, 0.0, 0.9),
        f"{opposite_side_name}_elbow": Landmark(
            f"{opposite_side_name}_elbow",
            opposite_elbow_x,
            shoulder_y + 0.05,
            0.0,
            0.9,
        ),
        f"{opposite_side_name}_wrist": Landmark(
            f"{opposite_side_name}_wrist",
            opposite_wrist_x,
            shoulder_y + 0.1,
            0.0,
            0.9,
        ),
        "left_hip": Landmark("left_hip", 0.4, 0.65, 0.0, 0.9),
        "right_hip": Landmark("right_hip", 0.6, 0.65, 0.0, 0.9),
    }


@pytest.mark.parametrize("side", ["left", "right"])
def test_full_reach_succeeds_symmetrically(side):
    landmarks = _side_reach_landmarks(side, outward_ratio=1.0)

    result = evaluate_side_reach(landmarks, side, consecutive_samples=2)

    assert result.movement == "side_reach"
    assert result.completed is True
    assert result.feedback_code == "great"


@pytest.mark.parametrize("side", ["left", "right"])
def test_arm_down_returns_reach_code_symmetrically(side):
    landmarks = _side_reach_landmarks(side, outward_ratio=0.0)

    result = evaluate_side_reach(landmarks, side, consecutive_samples=2)

    assert result.completed is False
    assert result.feedback_code == f"reach_{side}"


@pytest.mark.parametrize("side", ["left", "right"])
def test_boundary_just_below_reach_ratio_fails_symmetrically(side):
    landmarks = _side_reach_landmarks(side, outward_ratio=0.84)

    result = evaluate_side_reach(landmarks, side, consecutive_samples=2)

    assert result.completed is False
    assert result.feedback_code == f"reach_{side}"


@pytest.mark.parametrize("side", ["left", "right"])
def test_boundary_exactly_at_reach_ratio_succeeds_symmetrically(side):
    landmarks = _side_reach_landmarks(side, outward_ratio=0.85)

    result = evaluate_side_reach(landmarks, side, consecutive_samples=2)

    assert result.completed is True
    assert result.feedback_code == "great"


@pytest.mark.parametrize("side", ["left", "right"])
def test_vertical_offset_too_large_fails_despite_full_reach_symmetrically(side):
    landmarks = _side_reach_landmarks(side, outward_ratio=1.0, vertical_ratio=-0.6)

    result = evaluate_side_reach(landmarks, side, consecutive_samples=2)

    assert result.completed is False
    assert result.feedback_code == f"reach_{side}"


@pytest.mark.parametrize("side", ["left", "right"])
def test_missing_requested_wrist_returns_full_body_missing_symmetrically(side):
    landmarks = _side_reach_landmarks(side, outward_ratio=1.0)
    del landmarks[f"{side}_wrist"]

    result = evaluate_side_reach(landmarks, side, consecutive_samples=2)

    assert result.completed is False
    assert result.feedback_code == "full_body_missing"
    assert result.confidence == 0.0


@pytest.mark.parametrize("side", ["left", "right"])
def test_low_visibility_requested_wrist_returns_full_body_missing_symmetrically(side):
    landmarks = _side_reach_landmarks(side, outward_ratio=1.0)
    wrist = landmarks[f"{side}_wrist"]
    landmarks[f"{side}_wrist"] = Landmark(wrist.name, wrist.x, wrist.y, wrist.z, 0.2)

    result = evaluate_side_reach(landmarks, side, consecutive_samples=2)

    assert result.completed is False
    assert result.feedback_code == "full_body_missing"


@pytest.mark.parametrize("side", ["left", "right"])
def test_zero_shoulder_width_is_framing_failure_symmetrically(side):
    landmarks = _side_reach_landmarks(side, outward_ratio=1.0)
    landmarks["right_shoulder"] = Landmark(
        "right_shoulder",
        landmarks["left_shoulder"].x,
        landmarks["left_shoulder"].y,
        0.0,
        0.9,
    )

    result = evaluate_side_reach(landmarks, side, consecutive_samples=2)

    assert result.completed is False
    assert result.feedback_code == "full_body_missing"


@pytest.mark.parametrize("side", ["left", "right"])
def test_condition_met_but_insufficient_consecutive_samples_holds_symmetrically(side):
    landmarks = _side_reach_landmarks(side, outward_ratio=1.0)

    result = evaluate_side_reach(landmarks, side, consecutive_samples=1)

    assert result.completed is False
    assert result.feedback_code == "hold"


@pytest.mark.parametrize("side", ["left", "right"])
def test_default_consecutive_samples_assumes_hold_already_satisfied_symmetrically(side):
    landmarks = _side_reach_landmarks(side, outward_ratio=1.0)

    result = evaluate_side_reach(landmarks, side)

    assert result.completed is True
    assert result.feedback_code == "great"


@pytest.mark.parametrize("requested_side", ["left", "right"])
def test_opposite_arm_reaching_does_not_satisfy_requested_side(requested_side):
    """A full reach on the *other* arm must never satisfy the requested side.

    Matches the acceptance matrix's "a right-arm reach does not satisfy
    the [left] request" rule (docs/movement_specification.md section 12),
    checked here in both directions.
    """
    other_side = "right" if requested_side == "left" else "left"
    landmarks = _side_reach_landmarks(other_side, outward_ratio=1.0)
    # The requested side's own wrist stays down at its shoulder, not reaching.
    requested_shoulder_x = 0.35 if requested_side == "left" else 0.65
    landmarks[f"{requested_side}_wrist"] = Landmark(
        f"{requested_side}_wrist", requested_shoulder_x, 0.4, 0.0, 0.9
    )

    result = evaluate_side_reach(landmarks, requested_side, consecutive_samples=2)

    assert result.completed is False
    assert result.feedback_code == f"reach_{requested_side}"


def test_reach_left_and_reach_right_give_side_specific_feedback():
    assert "left-side reach" in FEEDBACK_MESSAGES["reach_left"]
    assert "right-side reach" in FEEDBACK_MESSAGES["reach_right"]
    assert FEEDBACK_MESSAGES["reach_left"] != FEEDBACK_MESSAGES["reach_right"]


# --- Knee lift -------------------------------------------------------------

KNEE_LIFT_FIXTURE_CASES = [
    ("synthetic_knee_lift_left_positive_001", "left", True, "great"),
    ("synthetic_knee_lift_right_negative_001", "right", False, "lift_knee"),
    ("synthetic_knee_lift_right_borderline_001", "right", False, "lift_knee"),
    (
        "synthetic_knee_lift_left_low_visibility_001",
        "left",
        False,
        "full_body_missing",
    ),
]


@pytest.mark.parametrize(
    "fixture_id, side, expected_completed, expected_code", KNEE_LIFT_FIXTURE_CASES
)
def test_knee_lift_committed_fixtures_match_expected_outcome(
    fixture_id, side, expected_completed, expected_code
):
    fixture = load_knee_lift_fixture(fixture_id)
    result = evaluate_knee_lift(
        landmarks_from_fixture(fixture),
        side,
        consecutive_samples=fixture["observed_consecutive_samples"],
    )

    assert result.movement == "knee_lift_or_step"
    assert result.completed is expected_completed
    assert result.feedback_code == expected_code
    assert fixture["requested_side"] == side
    assert fixture["expected_completed"] == expected_completed
    assert fixture["expected_feedback_code"] == expected_code


def test_unknown_knee_lift_fixture_id_raises_key_error():
    with pytest.raises(KeyError):
        load_knee_lift_fixture("does_not_exist")


def _knee_lift_landmarks(
    selected_side: str, selected_knee_y: float, opposite_knee_y: float = 0.7
) -> dict[str, Landmark]:
    """Build symmetric lower-body landmarks with a vertical 0.4 leg scale."""
    other_side = "right" if selected_side == "left" else "left"
    x_by_side = {"left": 0.4, "right": 0.6}
    landmarks = {}
    for side in ("left", "right"):
        x = x_by_side[side]
        landmarks[f"{side}_hip"] = Landmark(f"{side}_hip", x, 0.5, 0.0, 0.9)
        landmarks[f"{side}_ankle"] = Landmark(f"{side}_ankle", x, 0.9, 0.0, 0.9)
    landmarks[f"{selected_side}_knee"] = Landmark(
        f"{selected_side}_knee",
        x_by_side[selected_side],
        selected_knee_y,
        0.0,
        0.9,
    )
    landmarks[f"{other_side}_knee"] = Landmark(
        f"{other_side}_knee",
        x_by_side[other_side],
        opposite_knee_y,
        0.0,
        0.9,
    )
    return landmarks


@pytest.mark.parametrize("side", ["left", "right"])
def test_knee_lift_succeeds_symmetrically_for_anatomical_side(side):
    result = evaluate_knee_lift(
        _knee_lift_landmarks(side, selected_knee_y=0.6),
        side,
        consecutive_samples=2,
    )

    assert result.completed is True
    assert result.feedback_code == "great"


@pytest.mark.parametrize("side", ["left", "right"])
def test_neutral_knee_returns_lift_knee_symmetrically(side):
    result = evaluate_knee_lift(
        _knee_lift_landmarks(side, selected_knee_y=0.7),
        side,
        consecutive_samples=2,
    )

    assert result.completed is False
    assert result.feedback_code == "lift_knee"


@pytest.mark.parametrize("side", ["left", "right"])
def test_exact_knee_lift_threshold_succeeds(side):
    result = evaluate_knee_lift(
        _knee_lift_landmarks(side, selected_knee_y=0.64),
        side,
        consecutive_samples=2,
    )

    assert result.completed is True
    assert result.confidence == 1.0


@pytest.mark.parametrize("side", ["left", "right"])
def test_just_outside_knee_lift_threshold_retries(side):
    result = evaluate_knee_lift(
        _knee_lift_landmarks(side, selected_knee_y=0.640001),
        side,
        consecutive_samples=2,
    )

    assert result.completed is False
    assert result.feedback_code == "lift_knee"
    assert 0.0 < result.confidence < 1.0


@pytest.mark.parametrize("requested_side", ["left", "right"])
def test_opposite_knee_alone_does_not_satisfy_selected_side(requested_side):
    result = evaluate_knee_lift(
        _knee_lift_landmarks(requested_side, selected_knee_y=0.7, opposite_knee_y=0.6),
        requested_side,
        consecutive_samples=2,
    )

    assert result.completed is False
    assert result.feedback_code == "lift_knee"


@pytest.mark.parametrize("requested_side", ["left", "right"])
def test_both_knees_lifted_evaluates_selected_side_consistently(requested_side):
    result = evaluate_knee_lift(
        _knee_lift_landmarks(requested_side, selected_knee_y=0.6, opposite_knee_y=0.6),
        requested_side,
        consecutive_samples=2,
    )

    assert result.completed is True
    assert result.feedback_code == "great"


@pytest.mark.parametrize(
    "missing_name",
    ["left_hip", "left_knee", "left_ankle", "right_hip", "right_ankle"],
)
def test_missing_each_required_knee_lift_landmark_returns_framing(missing_name):
    landmarks = _knee_lift_landmarks("left", selected_knee_y=0.6)
    del landmarks[missing_name]

    result = evaluate_knee_lift(landmarks, "left", consecutive_samples=2)

    assert result.completed is False
    assert result.feedback_code == "full_body_missing"
    assert result.confidence == 0.0


@pytest.mark.parametrize(
    "low_visibility_name",
    ["left_hip", "left_knee", "left_ankle", "right_hip", "right_ankle"],
)
def test_low_visibility_on_each_required_knee_lift_landmark_returns_framing(
    low_visibility_name,
):
    landmarks = _knee_lift_landmarks("left", selected_knee_y=0.6)
    landmark = landmarks[low_visibility_name]
    landmarks[low_visibility_name] = Landmark(
        landmark.name, landmark.x, landmark.y, landmark.z, 0.2
    )

    result = evaluate_knee_lift(landmarks, "left", consecutive_samples=2)

    assert result.completed is False
    assert result.feedback_code == "full_body_missing"
    assert result.confidence == 0.0


def test_zero_knee_lift_leg_scale_is_framing_failure():
    landmarks = _knee_lift_landmarks("left", selected_knee_y=0.5)
    landmarks["left_ankle"] = Landmark("left_ankle", 0.4, 0.5, 0.0, 0.9)

    result = evaluate_knee_lift(landmarks, "left", consecutive_samples=2)

    assert result.completed is False
    assert result.feedback_code == "full_body_missing"
    assert result.confidence == 0.0


def test_knee_lift_condition_with_one_sample_holds():
    result = evaluate_knee_lift(
        _knee_lift_landmarks("left", selected_knee_y=0.6),
        "left",
        consecutive_samples=1,
    )

    assert result.completed is False
    assert result.feedback_code == "hold"


def test_knee_lift_condition_with_two_samples_succeeds():
    result = evaluate_knee_lift(
        _knee_lift_landmarks("left", selected_knee_y=0.6),
        "left",
        consecutive_samples=2,
    )

    assert result.completed is True
    assert result.feedback_code == "great"


def test_knee_lift_omitted_samples_assumes_hold_satisfied():
    result = evaluate_knee_lift(
        _knee_lift_landmarks("left", selected_knee_y=0.6), "left"
    )

    assert result.completed is True
    assert result.feedback_code == "great"


def test_lift_knee_gives_knee_lift_specific_feedback():
    assert "knee lift" in FEEDBACK_MESSAGES["lift_knee"]
    assert FEEDBACK_MESSAGES["lift_knee"] != FEEDBACK_MESSAGES["raise_arms"]
