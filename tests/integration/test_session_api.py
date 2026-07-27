"""Integration tests for the MP-018 session API.

Uses the Flask test client only. No cameras, real images, or network calls;
the movement endpoint is driven by the deterministic checked-in fixtures.
Each test client carries its own signed-cookie session, which is how state is
isolated between clients.
"""

from __future__ import annotations

SUCCESS_REQUEST = {
    "movement": "raise_both_arms",
    "fixture_id": "synthetic_raise_arms_positive_001",
}


def _summary(client):
    return client.get("/api/session/summary").get_json()


def test_reset_returns_success_message(client):
    response = client.post("/api/session/reset")

    assert response.status_code == 200
    assert response.get_json() == {
        "status": "success",
        "message": "Session reset successfully.",
    }


def test_initial_summary_is_empty(client):
    response = client.get("/api/session/summary")

    assert response.status_code == 200
    assert response.get_json() == {
        "attempted_movements": 0,
        "completed_movements": 0,
        "stars": 0,
    }


def test_movement_request_updates_and_persists_summary(client):
    star_response = client.post("/api/movement", json=SUCCESS_REQUEST)
    assert star_response.status_code == 200
    assert star_response.get_json()["stars"] == 1

    # State persists across a separate request via the session cookie.
    assert _summary(client) == {
        "attempted_movements": 1,
        "completed_movements": 1,
        "stars": 1,
    }


def test_repeated_success_frames_do_not_double_count(client):
    client.post("/api/movement", json=SUCCESS_REQUEST)
    second = client.post("/api/movement", json=SUCCESS_REQUEST)

    # The star was already awarded for this attempt (MP-017 idempotency).
    assert second.get_json()["stars"] == 0
    assert _summary(client) == {
        "attempted_movements": 1,
        "completed_movements": 1,
        "stars": 1,
    }


def test_start_attempt_allows_another_star_for_same_movement(client):
    client.post("/api/movement", json=SUCCESS_REQUEST)
    assert _summary(client)["stars"] == 1

    reset_attempt = client.post(
        "/api/session/start-attempt",
        json={"movement": "raise_both_arms"},
    )
    assert reset_attempt.status_code == 200

    second = client.post("/api/movement", json=SUCCESS_REQUEST)
    assert second.get_json()["stars"] == 1
    assert _summary(client) == {
        "attempted_movements": 1,
        "completed_movements": 2,
        "stars": 2,
    }


def test_reset_clears_state(client):
    client.post("/api/movement", json=SUCCESS_REQUEST)
    assert _summary(client)["stars"] == 1

    client.post("/api/session/reset")

    assert _summary(client) == {
        "attempted_movements": 0,
        "completed_movements": 0,
        "stars": 0,
    }


def test_finish_returns_final_summary_with_friendly_message(client):
    client.post("/api/movement", json=SUCCESS_REQUEST)

    response = client.post("/api/session/finish")
    payload = response.get_json()

    assert response.status_code == 200
    assert payload["attempted_movements"] == 1
    assert payload["completed_movements"] == 1
    assert payload["stars"] == 1
    assert payload["finished"] is True
    assert "1 movement(s)" in payload["message"]
    assert "1 star(s)" in payload["message"]


def test_repeated_finish_calls_are_idempotent(client):
    client.post("/api/movement", json=SUCCESS_REQUEST)

    first = client.post("/api/session/finish").get_json()
    second = client.post("/api/session/finish").get_json()

    assert first == second
    assert first["stars"] == 1  # finishing awards no extra stars


def test_two_clients_do_not_share_session_state(app):
    client_a = app.test_client()
    client_b = app.test_client()

    client_a.post("/api/movement", json=SUCCESS_REQUEST)

    assert _summary(client_a) == {
        "attempted_movements": 1,
        "completed_movements": 1,
        "stars": 1,
    }
    # Client B never touched the movement endpoint; its session is clean.
    assert _summary(client_b) == {
        "attempted_movements": 0,
        "completed_movements": 0,
        "stars": 0,
    }


def test_invalid_movement_id_still_returns_400(client):
    response = client.post(
        "/api/movement",
        json={
            "movement": "cartwheel",
            "fixture_id": "synthetic_raise_arms_positive_001",
        },
    )

    assert response.status_code == 400
    assert response.get_json()["message"] == "Unsupported or missing movement."
