"""MovePal Flask application factory."""

from __future__ import annotations

from flask import Flask

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
    return app
