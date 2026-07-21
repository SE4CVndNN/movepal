"""Application configuration using portable paths."""

from __future__ import annotations

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


class BaseConfig:
    """Shared safe defaults."""

    SECRET_KEY = os.getenv("SECRET_KEY", "development-only-change-me")
    MAX_CONTENT_LENGTH = int(os.getenv("MAX_CONTENT_LENGTH_MB", "5")) * 1024 * 1024
    SAMPLE_DATA_DIR = BASE_DIR / "data" / "samples"
    LANDMARK_DATA_DIR = BASE_DIR / "data" / "landmarks"
    ALLOWED_IMAGE_EXTENSIONS = {"jpg", "jpeg", "png"}
    ALLOWED_VIDEO_EXTENSIONS = {"mp4", "webm"}
    POSE_MODEL_PATH = Path(
        os.getenv("POSE_MODEL_PATH", BASE_DIR / "pose_landmarker_lite.task")
    )


class DevelopmentConfig(BaseConfig):
    """Local development configuration."""

    DEBUG = False


class TestingConfig(BaseConfig):
    """Deterministic configuration for automated tests."""

    TESTING = True
    SECRET_KEY = "testing-secret"
