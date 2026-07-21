import pytest

from app.services.pose_tracking import (
    TRACKED_LANDMARK_NAMES,
    Landmark,
    MediaPipePoseAdapter,
    PoseStatus,
    landmark_distance,
    load_pose_fixture,
    load_pose_fixtures,
    visible_landmarks,
)

REQUIRED_FIXTURE_FIELDS = {
    "fixture_id",
    "schema_version",
    "source_type",
    "provenance_reference",
    "description",
    "expected_status",
    "landmarks",
}

REQUIRED_FIXTURE_IDS = {
    "synthetic_full_visibility_standing_001",
    "synthetic_full_visibility_arms_raised_001",
    "synthetic_no_pose_001",
    "synthetic_low_visibility_dark_room_001",
    "synthetic_partial_upper_body_only_001",
}


def test_fixtures_are_schema_valid():
    fixtures = load_pose_fixtures()
    seen_ids = set()
    for fixture in fixtures:
        assert REQUIRED_FIXTURE_FIELDS.issubset(fixture.keys())
        assert fixture["fixture_id"] not in seen_ids
        seen_ids.add(fixture["fixture_id"])
        assert fixture["expected_status"] in {status.value for status in PoseStatus}
        for values in fixture["landmarks"].values():
            assert "x" in values and "y" in values and "visibility" in values
            assert 0.0 <= values["x"] <= 1.0
            assert 0.0 <= values["y"] <= 1.0
            assert 0.0 <= values["visibility"] <= 1.0

    # Guards against accidentally dropping one of the five scenarios MP-005
    # introduced (success, arms-raised, no-pose, low-visibility, partial-body).
    assert REQUIRED_FIXTURE_IDS.issubset(seen_ids)


@pytest.mark.parametrize("fixture_id", sorted(REQUIRED_FIXTURE_IDS))
def test_fixture_status_matches_expected(fixture_id):
    fixtures = {item["fixture_id"]: item for item in load_pose_fixtures()}
    fixture = fixtures[fixture_id]

    result = load_pose_fixture(fixture_id)

    assert result.status.value == fixture["expected_status"]


def test_no_pose_fixture_has_no_landmarks():
    result = load_pose_fixture("synthetic_no_pose_001")

    assert result.status == PoseStatus.NO_POSE
    assert result.landmarks == {}


def test_partial_upper_body_fixture_omits_lower_body_landmarks():
    result = load_pose_fixture("synthetic_partial_upper_body_only_001")

    assert result.status == PoseStatus.SUCCESS
    assert "left_shoulder" in result.landmarks
    assert "left_hip" not in result.landmarks
    assert "left_knee" not in result.landmarks


def test_unknown_fixture_id_raises_key_error():
    with pytest.raises(KeyError):
        load_pose_fixture("does_not_exist")


def test_visible_landmarks_filters_by_threshold():
    landmarks = [
        Landmark(name="left_wrist", x=0.1, y=0.1, z=0.0, visibility=0.9),
        Landmark(name="right_wrist", x=0.2, y=0.2, z=0.0, visibility=0.2),
    ]

    result = visible_landmarks(landmarks, minimum_visibility=0.5)

    assert [item.name for item in result] == ["left_wrist"]


def test_tracked_landmark_names_cover_movement_spec_joints():
    for side in ("left", "right"):
        for joint in ("shoulder", "elbow", "wrist", "hip", "knee"):
            assert f"{side}_{joint}" in TRACKED_LANDMARK_NAMES


def test_adapter_returns_error_result_without_raising(tmp_path):
    adapter = MediaPipePoseAdapter(model_path=tmp_path / "missing_model.task")

    result = adapter.estimate(tmp_path / "missing_image.jpg")

    assert result.status == PoseStatus.ERROR
    assert result.error
    assert result.landmarks == {}


def test_landmark_distance_is_translation_invariant():
    a = Landmark(name="left_shoulder", x=0.4, y=0.3, z=0.0, visibility=1.0)
    b = Landmark(name="right_shoulder", x=0.6, y=0.3, z=0.0, visibility=1.0)
    shift_x, shift_y = 0.1, -0.2
    a_shifted = Landmark(
        name=a.name, x=a.x + shift_x, y=a.y + shift_y, z=0.0, visibility=1.0
    )
    b_shifted = Landmark(
        name=b.name, x=b.x + shift_x, y=b.y + shift_y, z=0.0, visibility=1.0
    )

    assert landmark_distance(a, b) == pytest.approx(0.2)
    assert landmark_distance(a_shifted, b_shifted) == pytest.approx(
        landmark_distance(a, b)
    )


def test_landmark_distance_matches_fixture_shoulder_width():
    result = load_pose_fixture("synthetic_full_visibility_standing_001")

    width = landmark_distance(
        result.landmarks["left_shoulder"], result.landmarks["right_shoulder"]
    )

    assert width > 0
