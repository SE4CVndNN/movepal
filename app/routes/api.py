"""JSON API routes."""

from flask import Blueprint, jsonify

from app.services.health import get_health_status

api_bp = Blueprint("api", __name__)


@api_bp.get("/health")
def health():
    data = get_health_status()

    return jsonify(data), 200
