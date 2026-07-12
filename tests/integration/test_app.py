def test_index_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"MovePal" in response.data


def test_health_endpoint(client):
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.get_json() == {"service": "movepal", "status": "ok"}
