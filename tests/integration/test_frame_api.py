"""Integration tests for POST /api/frame endpoint."""

from __future__ import annotations

import io
from pathlib import Path

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


def test_sample_asset_route_serves_existing_file(client):
    response = client.get("/api/samples/sample_raise_both_arms.png")
    assert response.status_code == 200
    assert response.content_type == "image/png"


def test_sample_asset_route_404s_for_unknown_file(client):
    response = client.get("/api/samples/does_not_exist.png")
    assert response.status_code == 404


def test_process_frame_with_sample_asset(client, monkeypatch):
    from pathlib import Path

    from app.services.pose_tracking import PoseResult, PoseStatus

    class MockPoseAdapter:
        def estimate(self, image_path):
            return PoseResult(status=PoseStatus.SUCCESS)

    monkeypatch.setattr("app.routes.api.get_pose_adapter", lambda: MockPoseAdapter())

    sample_path = (
        Path(__file__).parents[2] / "data" / "samples" / "sample_raise_both_arms.png"
    )
    with open(sample_path, "rb") as handle:
        data = {"image": (handle, "sample_raise_both_arms.png")}
        response = client.post(
            "/api/frame", data=data, content_type="multipart/form-data"
        )

    assert response.status_code == 200
    assert response.get_json()["pose_status"] == "success"
