"""Contract and smoke tests for POST /api/movement.

MP-014's vertical slice: a deterministic fixture travels through the
Flask API, the raise-both-arms rule, and the friendly feedback mapping
without touching a camera or MediaPipe. See docs/architecture.md's
"Suggested API contract" for the response shape this asserts.
"""

from __future__ import annotations


def test_movement_success_fixture_returns_documented_schema(client):
    response = client.post(
        "/api/movement",
        json={
            "movement": "raise_both_arms",
            "fixture_id": "synthetic_raise_arms_positive_001",
        },
    )

    assert response.status_code == 200
    assert response.get_json() == {
        "movement": "raise_both_arms",
        "completed": True,
        "confidence": 1.0,
        "feedback_code": "great",
        "feedback": "Awesome job! You've earned ⭐ 1 Star!",
        "stars": 1,
        "visibility_ok": True,
        "retryable": True,
    }


def test_movement_negative_fixture_asks_to_raise_arms(client):
    response = client.post(
        "/api/movement",
        json={
            "movement": "raise_both_arms",
            "fixture_id": "synthetic_raise_arms_negative_001",
        },
    )

    payload = response.get_json()
    assert response.status_code == 200
    assert payload["completed"] is False
    assert payload["feedback_code"] == "raise_arms"
    assert (
        payload["feedback"]
        == "You need both arms up. Try a picture with your hands above your shoulders."
    )
    assert payload["visibility_ok"] is True


def test_movement_borderline_fixture_does_not_complete(client):
    response = client.post(
        "/api/movement",
        json={
            "movement": "raise_both_arms",
            "fixture_id": "synthetic_raise_arms_borderline_001",
        },
    )

    payload = response.get_json()
    assert response.status_code == 200
    assert payload["completed"] is False
    assert payload["feedback_code"] == "raise_arms"


def test_movement_low_visibility_fixture_reports_full_body_missing(client):
    response = client.post(
        "/api/movement",
        json={
            "movement": "raise_both_arms",
            "fixture_id": "synthetic_raise_arms_low_visibility_001",
        },
    )

    payload = response.get_json()
    assert response.status_code == 200
    assert payload["completed"] is False
    assert payload["feedback_code"] == "full_body_missing"
    assert payload["visibility_ok"] is False


def test_movement_consecutive_samples_override_produces_hold(client):
    response = client.post(
        "/api/movement",
        json={
            "movement": "raise_both_arms",
            "fixture_id": "synthetic_raise_arms_positive_001",
            "consecutive_samples": 1,
        },
    )

    payload = response.get_json()
    assert response.status_code == 200
    assert payload["completed"] is False
    assert payload["feedback_code"] == "hold"
    assert "Hold your pose a little longer" in payload["feedback"]


def test_movement_form_encoded_request_is_also_supported(client):
    response = client.post(
        "/api/movement",
        data={
            "movement": "raise_both_arms",
            "fixture_id": "synthetic_raise_arms_positive_001",
        },
    )

    assert response.status_code == 200
    assert response.get_json()["feedback_code"] == "great"


def test_movement_unsupported_movement_code(client):
    response = client.post(
        "/api/movement",
        json={
            "movement": "cartwheel",
            "fixture_id": "synthetic_raise_arms_positive_001",
        },
    )

    assert response.status_code == 400
    assert response.get_json() == {
        "status": "error",
        "message": "Unsupported or missing movement.",
    }


def test_movement_missing_fixture_id(client):
    response = client.post("/api/movement", json={"movement": "raise_both_arms"})

    assert response.status_code == 400
    assert response.get_json() == {
        "status": "error",
        "message": "fixture_id is required.",
    }


def test_movement_unknown_fixture_id(client):
    response = client.post(
        "/api/movement",
        json={"movement": "raise_both_arms", "fixture_id": "does_not_exist"},
    )

    assert response.status_code == 400
    assert response.get_json() == {
        "status": "error",
        "message": "Unknown fixture_id.",
    }


def test_movement_invalid_consecutive_samples(client):
    response = client.post(
        "/api/movement",
        json={
            "movement": "raise_both_arms",
            "fixture_id": "synthetic_raise_arms_positive_001",
            "consecutive_samples": "not-a-number",
        },
    )

    assert response.status_code == 400
    assert response.get_json() == {
        "status": "error",
        "message": "consecutive_samples must be an integer.",
    }


def test_movement_supports_side_reach_left(client):
    response = client.post(
        "/api/movement",
        json={
            "movement": "side_reach",
            "side": "left",
            "fixture_id": "synthetic_side_reach_left_positive_001",
        },
    )
    assert response.status_code == 200
    assert response.get_json()["completed"] is True


def test_movement_supports_knee_lift_left(client):
    response = client.post(
        "/api/movement",
        json={
            "movement": "knee_lift_or_step",
            "side": "left",
            "fixture_id": "synthetic_knee_lift_left_positive_001",
        },
    )
    assert response.status_code == 200
    assert response.get_json()["completed"] is True


def test_movement_side_reach_missing_side_returns_error(client):
    response = client.post(
        "/api/movement",
        json={
            "movement": "side_reach",
            "fixture_id": "synthetic_side_reach_left_positive_001",
        },
    )

    assert response.status_code == 400
    assert response.get_json() == {
        "status": "error",
        "message": "A valid side is required for this movement.",
    }


def test_movement_side_reach_invalid_side_returns_error(client):
    response = client.post(
        "/api/movement",
        json={
            "movement": "side_reach",
            "side": "center",
            "fixture_id": "synthetic_side_reach_left_positive_001",
        },
    )

    assert response.status_code == 400
    assert response.get_json() == {
        "status": "error",
        "message": "A valid side is required for this movement.",
    }
