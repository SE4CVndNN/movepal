"""Regression tests for the MP-024 deterministic QA self-check."""

from scripts.qa_selfcheck import _matches_fixture_outcome


def test_framing_retry_matches_api_contract_without_becoming_low_visibility():
    fixture = {
        "expected_completed": False,
        "expected_feedback_code": "full_body_missing",
        "expected_status": "retry",
        "category": "framing",
    }
    payload = {
        "completed": False,
        "feedback_code": "full_body_missing",
        "visibility_ok": False,
    }

    assert _matches_fixture_outcome(payload, fixture)


def test_wrong_feedback_code_fails_even_when_completion_matches():
    fixture = {
        "expected_completed": False,
        "expected_feedback_code": "full_body_missing",
        "expected_status": "low_visibility",
        "category": "low_visibility",
    }
    payload = {
        "completed": False,
        "feedback_code": "raise_arms",
        "visibility_ok": True,
    }

    assert not _matches_fixture_outcome(payload, fixture)
