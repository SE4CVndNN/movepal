"""Static asset presence checks, OS-portable via pathlib."""

from pathlib import Path


def test_static_assets_exist():
    static_dir = Path(__file__).parents[2] / "app" / "static"
    assert (static_dir / "css" / "app.css").is_file()
    assert (static_dir / "js" / "app.js").is_file()


def test_camera_preparation_state_machine_and_skeleton_are_present():
    root = Path(__file__).parents[2]
    app_js = (root / "app" / "static" / "js" / "app.js").read_text(encoding="utf-8")
    app_css = (root / "app" / "static" / "css" / "app.css").read_text(encoding="utf-8")

    for state in (
        "loading-model",
        "opening-camera",
        "finding-pose",
        "pose-ready",
        "countdown",
        "captured",
        "processing",
        "feedback",
    ):
        assert f'"{state}"' in app_js
    assert 'fetch("/api/pose/readiness",' in app_js
    assert 'fetch("/api/pose/preview"' in app_js
    assert "previewRequestInFlight" in app_js
    assert "drawSkeleton" in app_js
    assert "clearSkeletonOverlay" in app_js
    assert "REQUIRED_STABLE_POSE_CHECKS = 2" in app_js
    assert "Readiness is latched" in app_js
    assert 'cameraState !== "countdown"' in app_js
    assert "captureCountdownValue = 3" in app_js
    assert "Running fallback demo" not in app_js
    assert "pointer-events: none" in app_css
    assert ".capture-countdown[hidden]" in app_css
    assert ".camera-guidance" in app_css
    assert "font-size: clamp(1.25rem, 3vw, 1.55rem)" in app_css
    assert ".upload-photo-wrapper" in app_css
    assert ".camera-actions" in app_css
    assert ".camera-privacy-note" in app_css
    assert ".camera-auto-off-note" in app_css
    assert "MAX_UPLOAD_FILE_BYTES = 5 * 1024 * 1024" in app_js
    assert 'new Set(["image/jpeg", "image/png"])' in app_js
    assert 'fetch("/api/pose/preview"' in app_js
    assert "inspectSelectedPhoto" in app_js
    assert "drawSkeletonOnCanvas" in app_js
    assert "I can’t find a person." in app_js


def test_camera_lifecycle_stops_streams_and_cancels_background_work():
    app_js = (Path(__file__).parents[2] / "app" / "static" / "js" / "app.js").read_text(
        encoding="utf-8"
    )

    assert 'if (name !== "camera-live")' in app_js
    assert "readinessRequestController?.abort()" in app_js
    assert "previewRequestController?.abort()" in app_js
    assert "activeStream?.getTracks().forEach((track) => track.stop())" in app_js
    assert "preview.pause()" in app_js
    assert "preview.srcObject = null" in app_js
    assert 'window.addEventListener("beforeunload", stopCamera)' in app_js
    assert 'window.addEventListener("pagehide", stopCamera)' in app_js
    assert 'document.addEventListener("visibilitychange"' in app_js
    assert "requestedStream.getTracks().forEach((track) => track.stop())" in app_js


def test_screen_changes_manage_keyboard_focus_and_keep_mobile_controls_usable():
    root = Path(__file__).parents[2]
    app_js = (root / "app" / "static" / "js" / "app.js").read_text(encoding="utf-8")
    app_css = (root / "app" / "static" / "css" / "app.css").read_text(encoding="utf-8")

    assert "function focusScreenHeading" in app_js
    assert 'heading.setAttribute("tabindex", "-1")' in app_js
    assert "heading.focus({ preventScroll: true })" in app_js
    assert "focusScreenHeading(activeScreen)" in app_js
    assert ":focus-visible" in app_css
    assert "@media (max-width: 22.5rem)" in app_css
