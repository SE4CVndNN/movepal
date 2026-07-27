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
    assert 'id="capture-processing"' in body
    assert "<span>Checking your pose…</span>" in body
    assert 'class="loading-spinner"' in body


def test_avatar_uses_unique_gradient_ids(client):
    response = client.get("/")
    assert response.status_code == 200
    body = response.get_data(as_text=True)
    assert "robotBody-start" in body
    assert "robotBody-activity" in body
    assert "robotBody-summary" in body
    assert "robotBody-default" not in body
