"""Unit tests for the pure raise-both-arms movement rule."""

from __future__ import annotations

import pytest

from app.services.movement_rules import (
    evaluate_raise_both_arms,
    landmarks_from_fixture,
    load_raise_both_arms_fixture,
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
