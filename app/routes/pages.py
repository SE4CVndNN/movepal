"""HTML page routes."""

from flask import Blueprint, render_template

pages_bp = Blueprint("pages", __name__)


@pages_bp.get("/")
def index() -> str:
    """Render the initial MovePal landing page."""
    return render_template("index.html")
