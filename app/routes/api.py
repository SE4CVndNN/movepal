"""JSON API routes."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from flask import Blueprint, current_app, jsonify, request

from app.services.feedback import FEEDBACK_MESSAGES, format_feedback
from app.services.frame_processing import process_frame
from app.services.health import get_health_status
from app.services.movement_rules import (
    MovementResult,
    evaluate_raise_both_arms,
    landmarks_from_fixture,
    load_raise_both_arms_fixture,
)
from app.services.pose_tracking import MediaPipePoseAdapter, PoseResult, PoseStatus
from app.services.scoring import stars_for_completion

api_bp = Blueprint("api", __name__)

ALLOWED_MIME_TYPES = {"image/jpeg", "image/png", "image/jpg"}
SUPPORTED_MOVEMENTS = {"raise_both_arms"}


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


def _movement_request_payload() -> dict[str, Any]:
    """Merge form fields and a JSON body into a single lookup dict.

    Supports both a browser fallback path (form-encoded) and a JSON
    request body (used by contract tests), so callers do not need to know
    which encoding the client chose.
    """
    payload: dict[str, Any] = dict(request.form)
    if request.is_json:
        payload.update(request.get_json(silent=True) or {})
    return payload


@api_bp.post("/movement")
def movement():
    """Evaluate a deterministic movement fixture through the movement rule.

    MP-014's vertical slice: request -> fixture landmarks -> movement rule
    -> feedback/stars -> JSON response, with no camera or MediaPipe model
    involved. See docs/architecture.md section "Suggested API contract"
    for the response shape and docs/movement_specification.md for the
    rule this wraps.
    """
    payload = _movement_request_payload()
    movement_code = payload.get("movement")
    fixture_id = payload.get("fixture_id")

    if movement_code not in SUPPORTED_MOVEMENTS:
        return (
            jsonify({"status": "error", "message": "Unsupported or missing movement."}),
            400,
        )
    if not fixture_id:
        return jsonify({"status": "error", "message": "fixture_id is required."}), 400

    try:
        fixture = load_raise_both_arms_fixture(str(fixture_id))
    except KeyError:
        return jsonify({"status": "error", "message": "Unknown fixture_id."}), 400

    consecutive_samples_raw = payload.get("consecutive_samples")
    if consecutive_samples_raw is None:
        consecutive_samples = fixture.get("observed_consecutive_samples")
    else:
        try:
            consecutive_samples = int(consecutive_samples_raw)
        except (TypeError, ValueError):
            return (
                jsonify(
                    {
                        "status": "error",
                        "message": "consecutive_samples must be an integer.",
                    }
                ),
                400,
            )

    landmarks = landmarks_from_fixture(fixture)
    result = evaluate_raise_both_arms(
        landmarks, consecutive_samples=consecutive_samples
    )

    return jsonify(_movement_response(result)), 200


def _movement_response(result: MovementResult) -> dict[str, Any]:
    feedback_result = format_feedback(result)
    return {
        "movement": result.movement,
        "completed": feedback_result.completed,
        "confidence": result.confidence,
        "feedback_code": feedback_result.feedback_code,
        "feedback": feedback_result.message,
        "stars": feedback_result.stars_awarded,
        "visibility_ok": feedback_result.visibility_ok,
        "retryable": feedback_result.retryable,
    }


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
