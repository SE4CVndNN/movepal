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
