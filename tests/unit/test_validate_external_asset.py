import json

import pytest

from scripts.validate_external_asset import (
    ExternalAssetError,
    validate_external_asset,
    validate_landmark_shape,
)

VALID_LANDMARKS = {
    "left_shoulder": {"x": 0.42, "y": 0.30, "z": -0.02, "visibility": 0.9},
    "right_shoulder": {"x": 0.58, "y": 0.30, "z": -0.02, "visibility": 0.9},
    "left_elbow": {"x": 0.40, "y": 0.45, "z": -0.01, "visibility": 0.9},
    "right_elbow": {"x": 0.60, "y": 0.45, "z": -0.01, "visibility": 0.9},
    "left_wrist": {"x": 0.39, "y": 0.58, "z": 0.0, "visibility": 0.9},
    "right_wrist": {"x": 0.61, "y": 0.58, "z": 0.0, "visibility": 0.9},
    "left_hip": {"x": 0.45, "y": 0.60, "z": 0.0, "visibility": 0.9},
    "right_hip": {"x": 0.55, "y": 0.60, "z": 0.0, "visibility": 0.9},
    "left_knee": {"x": 0.45, "y": 0.78, "z": 0.0, "visibility": 0.9},
    "right_knee": {"x": 0.55, "y": 0.78, "z": 0.0, "visibility": 0.9},
    "left_ankle": {"x": 0.45, "y": 0.95, "z": 0.0, "visibility": 0.9},
    "right_ankle": {"x": 0.55, "y": 0.95, "z": 0.0, "visibility": 0.9},
}


def test_validate_landmark_shape_accepts_valid_landmarks():
    assert validate_landmark_shape(VALID_LANDMARKS) == []


def test_validate_landmark_shape_flags_unknown_name():
    bad = {
        **VALID_LANDMARKS,
        "left_pinky": {"x": 0.1, "y": 0.1, "z": 0.0, "visibility": 0.9},
    }
    problems = validate_landmark_shape(bad)
    assert any("left_pinky" in p for p in problems)


def test_validate_landmark_shape_flags_out_of_range_value():
    bad = {
        **VALID_LANDMARKS,
        "left_wrist": {"x": 1.5, "y": 0.1, "z": 0.0, "visibility": 0.9},
    }
    problems = validate_landmark_shape(bad)
    assert any("left_wrist" in p and "x=" in p for p in problems)

def test_validate_landmark_shape_flags_non_numeric_values():
    """Regression: malformed JSON with string instead of number should be caught."""
    bad = {
        **VALID_LANDMARKS,
        "left_shoulder": {"x": "oops", "y": 0.1, "z": 0.0, "visibility": 0.9},
    }
    problems = validate_landmark_shape(bad)
    assert any("x must be numeric" in p for p in problems)

def test_validate_external_asset_from_fixture_json(tmp_path):
    fixture_path = tmp_path / "sample.json"
    fixture_path.write_text(
        json.dumps({"landmarks": VALID_LANDMARKS}), encoding="utf-8"
    )

    report = validate_external_asset(fixture_json=fixture_path)

    assert report["status"] == "success"
    assert report["is_compatible"] is True
    assert report["missing_tracked_landmarks"] == []
    assert report["shape_problems"] == []


def test_validate_external_asset_flags_low_coverage(tmp_path):
    partial = {"left_shoulder": VALID_LANDMARKS["left_shoulder"]}
    fixture_path = tmp_path / "partial.json"
    fixture_path.write_text(json.dumps({"landmarks": partial}), encoding="utf-8")

    report = validate_external_asset(fixture_json=fixture_path)

    assert report["status"] == "low_visibility"
    assert report["is_compatible"] is False
    assert "right_shoulder" in report["missing_tracked_landmarks"]


def test_validate_external_asset_missing_file_raises_clear_error(tmp_path):
    with pytest.raises(ExternalAssetError, match="No such fixture JSON file"):
        validate_external_asset(fixture_json=tmp_path / "does_not_exist.json")


def test_validate_external_asset_requires_input():
    with pytest.raises(ExternalAssetError, match="Provide either"):
        validate_external_asset()


def test_validate_external_asset_bad_json_raises_clear_error(tmp_path):
    fixture_path = tmp_path / "bad.json"
    fixture_path.write_text("{not valid json", encoding="utf-8")

    with pytest.raises(ExternalAssetError, match="not valid JSON"):
        validate_external_asset(fixture_json=fixture_path)
