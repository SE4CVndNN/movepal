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


def test_unhandled_page_error_is_friendly_and_does_not_expose_traceback(app):
    app.config.update(TESTING=False, PROPAGATE_EXCEPTIONS=False)

    @app.get("/test-server-error")
    def test_server_error():
        raise RuntimeError("test-only internal detail")

    response = app.test_client().get("/test-server-error")
    body = response.get_data(as_text=True)

    assert response.status_code == 500
    assert "Something went wrong" in body
    assert "test-only internal detail" not in body
    assert "Traceback" not in body


def test_unhandled_api_error_is_safe_json(app):
    app.config.update(TESTING=False, PROPAGATE_EXCEPTIONS=False)

    @app.get("/api/test-server-error")
    def test_api_server_error():
        raise RuntimeError("test-only internal detail")

    response = app.test_client().get("/api/test-server-error")

    assert response.status_code == 500
    assert response.get_json() == {
        "status": "error",
        "message": "Something went wrong. Please try again.",
    }
    assert "test-only internal detail" not in response.get_data(as_text=True)
