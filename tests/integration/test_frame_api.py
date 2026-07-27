"""Integration tests for POST /api/frame endpoint."""

from __future__ import annotations

import io
from pathlib import Path

import pytest

from app.services.pose_tracking import PoseResult, PoseStatus


class MockPoseAdapter:
    """Mock adapter for deterministic API tests."""

    def __init__(self, result: PoseResult) -> None:
        self.result = result
        self.last_estimated_path: Path | None = None

    def estimate(self, image_path: str | Path) -> PoseResult:
        self.last_estimated_path = Path(image_path)
        return self.result


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
