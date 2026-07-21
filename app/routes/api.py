"""JSON API routes."""

from __future__ import annotations

from pathlib import Path

from flask import Blueprint, current_app, jsonify, request

from app.services.frame_processing import process_frame
from app.services.health import get_health_status
from app.services.pose_tracking import MediaPipePoseAdapter, PoseResult, PoseStatus

api_bp = Blueprint("api", __name__)

ALLOWED_MIME_TYPES = {"image/jpeg", "image/png", "image/jpg"}


def get_pose_adapter() -> MediaPipePoseAdapter:
    """Instantiate the pose adapter with current application config."""
    model_path = current_app.config.get(
        "POSE_MODEL_PATH",
        current_app.config.get("BASE_DIR", Path(".")) / "pose_landmarker_lite.task",
    )
    return MediaPipePoseAdapter(model_path=model_path)


@api_bp.get("/health")
def health():
    data = get_health_status()

    return jsonify(data), 200


@api_bp.post("/frame")
def frame():
    if "image" not in request.files:
        return jsonify({"status": "error", "message": "No image file provided."}), 400

    file = request.files["image"]
    if not file or not file.filename:
        return jsonify({"status": "error", "message": "No image file provided."}), 400

    original_filename = file.filename or ""
    extension = (
        original_filename.rsplit(".", 1)[-1].lower() if "." in original_filename else ""
    )
    allowed_extensions = current_app.config.get(
        "ALLOWED_IMAGE_EXTENSIONS", {"jpg", "jpeg", "png"}
    )

    raw_mimetype = file.mimetype or ""
    mimetype = raw_mimetype.split(";")[0].strip().lower()

    if extension not in allowed_extensions or mimetype not in ALLOWED_MIME_TYPES:
        return jsonify({"status": "error", "message": "Unsupported image format."}), 415

    adapter = get_pose_adapter()
    result: PoseResult = process_frame(file, adapter)

    return _map_pose_result(result)


def _map_pose_result(result: PoseResult):
    match result.status:
        case PoseStatus.SUCCESS:
            return (
                jsonify(
                    {
                        "status": "success",
                        "message": "Frame processed successfully.",
                        "pose_status": "success",
                    }
                ),
                200,
            )
        case PoseStatus.NO_POSE:
            return (
                jsonify(
                    {
                        "status": "success",
                        "message": "No pose detected.",
                        "pose_status": "no_pose",
                    }
                ),
                200,
            )
        case PoseStatus.LOW_VISIBILITY:
            return (
                jsonify(
                    {
                        "status": "success",
                        "message": "Pose visibility is too low.",
                        "pose_status": "low_visibility",
                    }
                ),
                200,
            )
        case PoseStatus.ERROR | _:
            return (
                jsonify(
                    {
                        "status": "error",
                        "message": "Unable to process frame.",
                        "pose_status": "error",
                    }
                ),
                500,
            )
