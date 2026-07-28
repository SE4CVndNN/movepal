"""Template rendering checks for the MP-011 base game interface."""


def test_index_page_renders_all_regions(client):
    response = client.get("/")
    assert response.status_code == 200
    body = response.get_data(as_text=True)
    assert 'id="score-region"' in body
    assert 'data-screen="activity"' in body
    assert 'data-screen="camera-choice"' in body
    assert 'data-screen="feedback"' in body
    assert 'data-screen="summary"' in body
    assert "avatar" in body


def test_ui_includes_initial_state_and_feedback_modes(client):
    response = client.get("/")
    assert response.status_code == 200
    body = response.get_data(as_text=True)
    assert '<body data-app-state="idle">' in body
    assert 'data-feedback="success"' in body
    assert 'data-feedback="retry"' in body
    assert 'id="feedback-status"' in body
    assert 'aria-hidden="true"' in body
    assert '<canvas id="capture-canvas" hidden></canvas>' in body
    assert '<canvas id="skeleton-overlay" aria-hidden="true"></canvas>' in body
    assert 'id="capture-processing"' in body
    assert "<span>Checking your pose…</span>" in body
    assert 'class="loading-spinner"' in body
    assert 'class="camera-guidance"' in body
    assert "Stand in the middle so I can see you!" in body
    assert 'accept="image/jpeg,image/png"' in body
    assert 'id="camera-upload-preview"' in body
    assert 'id="camera-upload-overlay"' in body
    assert 'id="fallback-upload-preview"' in body
    assert 'id="fallback-upload-overlay"' in body
    assert body.count("JPEG or PNG, up to 5 MB.") == 2
    assert body.count("Check my move") == 2
    assert 'class="camera-privacy-note"' in body
    assert 'class="camera-auto-off-note"' in body
    assert 'class="camera-actions"' in body


def test_avatar_uses_unique_gradient_ids(client):
    response = client.get("/")
    assert response.status_code == 200
    body = response.get_data(as_text=True)
    assert "robotBody-start" in body
    assert "robotBody-activity" in body
    assert "robotBody-summary" in body
    assert "robotBody-default" not in body


def test_server_error_page_template_is_friendly_and_actionable(app):
    from flask import render_template

    with app.test_request_context():
        body = render_template("errors/500.html")

    assert "Something went wrong" in body
    assert "Return to MovePal" in body
