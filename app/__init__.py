"""MovePal Flask application factory."""

from __future__ import annotations

from flask import Flask, jsonify, render_template, request

from app.config import DevelopmentConfig
from app.routes.api import api_bp
from app.routes.pages import pages_bp


def create_app(test_config: dict[str, object] | None = None) -> Flask:
    """Create and configure a MovePal Flask application instance."""
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)

    if test_config is not None:
        app.config.from_mapping(test_config)

    app.register_blueprint(pages_bp)
    app.register_blueprint(api_bp, url_prefix="/api")

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template("errors/404.html"), 404

    @app.errorhandler(413)
    def request_entity_too_large(error):
        if request.path.startswith("/api/"):
            return jsonify({"status": "error", "message": "File too large."}), 413
        return render_template("errors/413.html"), 413

    return app
