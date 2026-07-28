"""Integration tests for POST /api/frame endpoint."""

from __future__ import annotations

import io
from pathlib import Path

import pytest

from app import create_app
from app.routes.api import get_pose_adapter
from app.services.pose_tracking import PoseResult, PoseStatus


class MockPoseAdapter:
    """Mock adapter for deterministic API tests."""

    def __init__(self, result: PoseResult) -> None:
        self.result = result
        self.last_estimated_path: Path | None = None

    def estimate(self, image_path: str | Path) -> PoseResult:
        self.last_estimated_path = Path(image_path)
        return self.result


def test_pose_adapter_is_reused_within_one_flask_app(app):
    with app.app_context():
        first = get_pose_adapter()
        second = get_pose_adapter()

    assert first is second


def test_pose_adapter_cache_is_isolated_between_flask_apps():
    first_app = create_app({"TESTING": True, "SECRET_KEY": "first"})
    second_app = create_app({"TESTING": True, "SECRET_KEY": "second"})

    with first_app.app_context():
        first = get_pose_adapter()
    with second_app.app_context():
        second = get_pose_adapter()

    assert first is not second


def test_pose_adapter_is_replaced_when_model_path_changes(app, tmp_path):
    with app.app_context():
        first = get_pose_adapter()
        app.config["POSE_MODEL_PATH"] = tmp_path / "different-model.task"
        second = get_pose_adapter()

    assert first is not second


def test_pose_readiness_warms_reused_adapter_without_exposing_path(client, monkeypatch):
    class ReadyAdapter:
        def __init__(self):
            self.warm_count = 0

        def warm_up(self):
            self.warm_count += 1

    adapter = ReadyAdapter()
    monkeypatch.setattr("app.routes.api.get_pose_adapter", lambda: adapter)

    first = client.get("/api/pose/readiness")
    second = client.get("/api/pose/readiness")

    assert first.status_code == second.status_code == 200
    assert first.get_json() == {"status": "ready"}
    assert "path" not in first.get_data(as_text=True).lower()
    assert adapter.warm_count == 2


def test_pose_preview_is_transient_and_has_no_scoring_side_effect(client, monkeypatch):
    from app.services.movement_rules import (
        landmarks_from_fixture,
        load_raise_both_arms_fixture,
    )

    fixture = load_raise_both_arms_fixture("synthetic_raise_arms_positive_001")
    landmarks = landmarks_from_fixture(fixture)
    captured_paths = []

    class PreviewAdapter:
        def estimate(self, image_path):
            path = Path(image_path)
            captured_paths.append(path)
            assert path.exists()
            return PoseResult(status=PoseStatus.SUCCESS, landmarks=landmarks)

    monkeypatch.setattr("app.routes.api.get_pose_adapter", lambda: PreviewAdapter())
    before = client.get("/api/session/summary").get_json()
    response = client.post(
        "/api/pose/preview",
        data={
            "image": (io.BytesIO(b"synthetic bytes"), "preview.jpg"),
            "movement": "raise_both_arms",
        },
        content_type="multipart/form-data",
    )
    after = client.get("/api/session/summary").get_json()

    payload = response.get_json()
    assert response.status_code == 200
    assert payload["ready_for_capture"] is True
    assert payload["guidance"] == "Great pose! Hold still!"
    assert set(payload) == {
        "pose_status",
        "ready_for_capture",
        "guidance",
        "display_landmarks",
    }
    assert set(payload["display_landmarks"]) <= {
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
    }
    assert before == after
    assert captured_paths and not captured_paths[0].exists()


def test_pose_preview_reports_no_person_with_child_friendly_guidance(
    client, monkeypatch
):
    class NoPoseAdapter:
        def estimate(self, image_path):
            return PoseResult(status=PoseStatus.NO_POSE)

    monkeypatch.setattr("app.routes.api.get_pose_adapter", lambda: NoPoseAdapter())
    response = client.post(
        "/api/pose/preview",
        data={
            "image": (io.BytesIO(b"safe synthetic bytes"), "preview.jpg"),
            "movement": "raise_both_arms",
        },
        content_type="multipart/form-data",
    )

    payload = response.get_json()
    assert response.status_code == 200
    assert payload["pose_status"] == "no_pose"
    assert payload["ready_for_capture"] is False
    assert payload["display_landmarks"] == {}
    assert payload["guidance"] == "Stand in the middle so I can see you!"


def test_process_frame_success(client, monkeypatch):
    mock_adapter = MockPoseAdapter(PoseResult(status=PoseStatus.SUCCESS))
    monkeypatch.setattr("app.routes.api.get_pose_adapter", lambda: mock_adapter)

    data = {"image": (io.BytesIO(b"dummy image bytes"), "frame.jpg")}
    response = client.post("/api/frame", data=data, content_type="multipart/form-data")

    assert response.status_code == 200
    assert response.get_json() == {
        "status": "success",
        "message": "Frame processed successfully.",
        "pose_status": "success",
    }


def test_process_frame_no_pose(client, monkeypatch):
    mock_adapter = MockPoseAdapter(PoseResult(status=PoseStatus.NO_POSE))
    monkeypatch.setattr("app.routes.api.get_pose_adapter", lambda: mock_adapter)

    data = {"image": (io.BytesIO(b"dummy image bytes"), "frame.png")}
    response = client.post("/api/frame", data=data, content_type="multipart/form-data")

    assert response.status_code == 200
    assert response.get_json() == {
        "status": "success",
        "message": "No pose detected.",
        "pose_status": "no_pose",
    }


def test_process_frame_low_visibility(client, monkeypatch):
    mock_adapter = MockPoseAdapter(PoseResult(status=PoseStatus.LOW_VISIBILITY))
    monkeypatch.setattr("app.routes.api.get_pose_adapter", lambda: mock_adapter)

    data = {"image": (io.BytesIO(b"dummy image bytes"), "frame.jpeg")}
    response = client.post("/api/frame", data=data, content_type="multipart/form-data")

    assert response.status_code == 200
    assert response.get_json() == {
        "status": "success",
        "message": "Pose visibility is too low.",
        "pose_status": "low_visibility",
    }


def test_process_frame_mocked_service_error(client, monkeypatch):
    mock_adapter = MockPoseAdapter(
        PoseResult(status=PoseStatus.ERROR, error="Model error")
    )
    monkeypatch.setattr("app.routes.api.get_pose_adapter", lambda: mock_adapter)

    data = {"image": (io.BytesIO(b"dummy image bytes"), "frame.png")}
    response = client.post("/api/frame", data=data, content_type="multipart/form-data")

    assert response.status_code == 500
    assert response.get_json() == {
        "status": "error",
        "message": "Unable to process frame.",
        "pose_status": "error",
    }


def test_process_frame_missing_image(client):
    response = client.post("/api/frame", data={}, content_type="multipart/form-data")

    assert response.status_code == 400
    assert response.get_json() == {
        "status": "error",
        "message": "No image file provided.",
    }


def test_process_frame_empty_filename(client):
    data = {"image": (io.BytesIO(b""), "")}
    response = client.post("/api/frame", data=data, content_type="multipart/form-data")

    assert response.status_code == 400
    assert response.get_json() == {
        "status": "error",
        "message": "No image file provided.",
    }


def test_process_frame_unsupported_extension(client):
    data = {"image": (io.BytesIO(b"text file content"), "document.txt")}
    response = client.post("/api/frame", data=data, content_type="multipart/form-data")

    assert response.status_code == 415
    assert response.get_json() == {
        "status": "error",
        "message": "Unsupported image format.",
    }


def test_process_frame_unsupported_mimetype(client):
    response = client.post(
        "/api/frame",
        data={"image": (io.BytesIO(b"fake data"), "image.png", "text/plain")},
        content_type="multipart/form-data",
    )

    assert response.status_code == 415
    assert response.get_json() == {
        "status": "error",
        "message": "Unsupported image format.",
    }


def test_process_frame_oversized_upload(app):
    app.config.update(MAX_CONTENT_LENGTH=50)
    client = app.test_client()

    large_data = b"x" * 200
    data = {"image": (io.BytesIO(large_data), "large_frame.png")}
    response = client.post("/api/frame", data=data, content_type="multipart/form-data")

    assert response.status_code == 413
    assert response.get_json() == {
        "status": "error",
        "message": "File too large.",
    }


def test_process_frame_deletes_temp_file(client, monkeypatch):
    temp_path_captured: list[Path] = []

    def mock_estimate(self, path):
        captured = Path(path)
        temp_path_captured.append(captured)
        assert captured.exists()
        return PoseResult(status=PoseStatus.SUCCESS)

    monkeypatch.setattr(
        "app.services.pose_tracking.MediaPipePoseAdapter.estimate", mock_estimate
    )

    data = {"image": (io.BytesIO(b"dummy image bytes"), "frame.png")}
    response = client.post("/api/frame", data=data, content_type="multipart/form-data")

    assert response.status_code == 200
    assert len(temp_path_captured) == 1
    # Verify the temp file was unlinked after request processing completes
    assert not temp_path_captured[0].exists()


def test_frame_with_movement_evaluates_when_pose_succeeds(client, monkeypatch):
    import io

    from app.services.movement_rules import (
        landmarks_from_fixture,
        load_raise_both_arms_fixture,
    )
    from app.services.pose_tracking import PoseResult, PoseStatus

    fixture = load_raise_both_arms_fixture("synthetic_raise_arms_positive_001")
    landmarks = landmarks_from_fixture(fixture)

    class MockPoseAdapter:
        def estimate(self, image_path):
            return PoseResult(status=PoseStatus.SUCCESS, landmarks=landmarks)

    monkeypatch.setattr("app.routes.api.get_pose_adapter", lambda: MockPoseAdapter())

    tiny_png = bytes.fromhex(
        "89504e470d0a1a0a0000000d49484452000000010000000108020000009077"
        "53de0000000c4944415408d763f8ffff3f0005fe02fea739663a0000000049"
        "454e44ae426082"
    )
    data = {
        "image": (io.BytesIO(tiny_png), "sample.png"),
        "movement": "raise_both_arms",
    }
    response = client.post("/api/frame", data=data, content_type="multipart/form-data")

    payload = response.get_json()
    assert response.status_code == 200
    assert "completed" in payload


@pytest.mark.parametrize(
    "side, fixture_id",
    [
        ("left", "synthetic_side_reach_left_positive_001"),
        ("right", "synthetic_side_reach_right_positive_001"),
    ],
)
def test_live_frame_side_reach_evaluates_both_anatomical_sides(
    client, monkeypatch, side, fixture_id
):
    from app.services.movement_rules import (
        landmarks_from_fixture,
        load_side_reach_fixture,
    )

    fixture = load_side_reach_fixture(fixture_id)
    landmarks = landmarks_from_fixture(fixture)

    class SideReachPoseAdapter:
        def estimate(self, image_path):
            return PoseResult(status=PoseStatus.SUCCESS, landmarks=landmarks)

    monkeypatch.setattr(
        "app.routes.api.get_pose_adapter",
        lambda: SideReachPoseAdapter(),
    )

    data = {
        "image": (io.BytesIO(b"safe synthetic bytes"), "frame.png"),
        "movement": "side_reach",
        "side": side,
    }
    response = client.post(
        "/api/frame",
        data=data,
        content_type="multipart/form-data",
    )

    payload = response.get_json()
    assert response.status_code == 200
    assert payload["movement"] == "side_reach"
    assert payload["completed"] is True
    assert payload["feedback_code"] == "great"
    assert payload["stars"] == 1
