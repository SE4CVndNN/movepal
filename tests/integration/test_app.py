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
