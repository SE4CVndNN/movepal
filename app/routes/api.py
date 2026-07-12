"""JSON API routes."""

from flask import Blueprint, jsonify

api_bp = Blueprint("api", __name__)


@api_bp.get("/health")
def health() -> tuple[dict[str, str], int]:
    """Return a small smoke-test response without loading a pose model."""
    return jsonify(status="ok", service="movepal"), 200
