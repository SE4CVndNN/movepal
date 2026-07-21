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
