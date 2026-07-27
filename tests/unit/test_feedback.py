"""Unit tests for feedback orchestration service and message catalog.

Guarantees every rule observation maps to a friendly, non-medical user-facing message,
and enforces visibility/framing message precedence.
"""

from __future__ import annotations

import pytest

from app.services.feedback import (
    FEEDBACK_MESSAGES,
    FeedbackResult,
    format_feedback,
    get_feedback_message,
)
from app.services.movement_rules import MovementResult
from app.services.scoring import ScoringSession


def test_message_catalog_covers_all_observation_codes():
    """Verify that all standard movement rule feedback codes exist in catalog."""
    expected_codes = {
        "great",
        "raise_arms",
        "reach_left",
        "reach_right",
        "lift_knee",
        "hold",
        "full_body_missing",
        "move_back",
        "try_again",
    }
    for code in expected_codes:
        assert code in FEEDBACK_MESSAGES
        assert isinstance(FEEDBACK_MESSAGES[code], str)
        assert len(FEEDBACK_MESSAGES[code]) > 0


@pytest.mark.parametrize(
    "code,expected_substring",
    [
        ("great", "Awesome job! You've earned ⭐ 1 Star!"),
        ("raise_arms", "both arms up"),
        ("reach_left", "bend gently to your left"),
        ("reach_right", "bend gently to your right"),
        ("lift_knee", "knee lift"),
        ("hold", "Hold your pose a little longer"),
        ("full_body_missing", "visible in the frame"),
        ("move_back", "Move slightly farther from the camera."),
    ],
)
def test_get_feedback_message_returns_friendly_text(code: str, expected_substring: str):
    message = get_feedback_message(code)
    assert expected_substring in message


def test_get_feedback_message_unknown_code_fallback():
    """Unknown codes must gracefully fall back to friendly default non-medical wording."""
    message = get_feedback_message("unknown_custom_observation")
    assert (
        message
        == "This picture doesn't show the move we asked for. Try again with the right pose."
    )


def test_format_feedback_success_result():
    result = MovementResult(
        movement="raise_both_arms",
        completed=True,
        confidence=1.0,
        feedback_code="great",
    )
    formatted = format_feedback(result)

    assert isinstance(formatted, FeedbackResult)
    assert formatted.feedback_code == "great"
    assert formatted.completed is True
    assert formatted.stars_awarded == 1
    assert formatted.total_stars == 1
    assert formatted.visibility_ok is True
    assert formatted.retryable is True
    assert formatted.message == "Awesome job! You've earned ⭐ 1 Star!"


def test_format_feedback_visibility_precedence():
    """Visibility/framing failures take precedence over technique feedback."""
    result = MovementResult(
        movement="raise_both_arms",
        completed=False,
        confidence=0.0,
        feedback_code="full_body_missing",
    )
    formatted = format_feedback(result)

    assert formatted.feedback_code == "full_body_missing"
    assert formatted.completed is False
    assert formatted.visibility_ok is False
    assert formatted.stars_awarded == 0
    assert "visible in the frame" in formatted.message


def test_format_feedback_with_scoring_session():
    """Passing a ScoringSession to format_feedback delegates scoring idempotently."""
    session = ScoringSession(current_movement="raise_both_arms")
    success = MovementResult(
        movement="raise_both_arms",
        completed=True,
        confidence=1.0,
        feedback_code="great",
    )

    first = format_feedback(success, session=session)
    assert first.stars_awarded == 1
    assert first.total_stars == 1

    # Second success frame in same attempt awards 0 additional stars
    second = format_feedback(success, session=session)
    assert second.stars_awarded == 0
    assert second.total_stars == 1
    assert second.completed is True
