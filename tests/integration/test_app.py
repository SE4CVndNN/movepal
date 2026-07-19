def test_index_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"MovePal" in response.data


def test_health_endpoint(client):
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.get_json() == {"service": "movepal", "status": "ok"}


def test_not_found_page(client):
    response = client.get("/missing-page")

    assert response.status_code == 404
    assert b"Page not found" in response.data


def test_request_too_large_page(app):
    app.config.update(MAX_CONTENT_LENGTH=10)

    @app.post("/test-upload")
    def test_upload():
        from flask import request

        request.files.get("file")
        return "ok"

    client = app.test_client()

    response = client.post(
        "/test-upload",
        data={"file": (b"x" * 20, "test.txt")},
        content_type="multipart/form-data",
    )

    assert response.status_code == 413
    assert b"File too large" in response.data
