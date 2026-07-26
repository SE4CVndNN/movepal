from __future__ import annotations

from app.services.movement_rules import MovementResult
from app.services.scoring import (
    ScoringSession,
    stars_for_completion,
    stars_for_confidence,
)


def test_star_thresholds():
    assert stars_for_confidence(0.90) == 3
    assert stars_for_confidence(0.70) == 2
    assert stars_for_confidence(0.50) == 1
    assert stars_for_confidence(0.20) == 0


def test_confidence_is_bounded():
    assert stars_for_confidence(5.0) == 3
    assert stars_for_confidence(-5.0) == 0


def test_stars_for_completion_matches_approved_wording():
    """The "great" feedback text is a fixed "1 Star", so a completed
    attempt must award exactly 1 star, not a confidence-scaled count."""
    assert stars_for_completion(True) == 1
    assert stars_for_completion(False) == 0


def test_scoring_session_rewards_each_completed_attempt():
    """Repeated successful attempts should earn a new star each time."""
    session = ScoringSession(current_movement="raise_both_arms")
    success_result = MovementResult(
        movement="raise_both_arms",
        completed=True,
        confidence=1.0,
        feedback_code="great",
    )

    awarded, total = session.process_result(success_result)
    assert awarded == 1
    assert total == 1
    assert session.attempt_completed is True

    for _ in range(5):
        awarded_repeat, total_repeat = session.process_result(success_result)
        assert awarded_repeat == 1
        assert total_repeat == total_repeat


def test_scoring_session_start_new_attempt_resets_completion():
    """Starting a new attempt resets the completion state so a new star can be earned."""
    session = ScoringSession(current_movement="raise_both_arms")
    success_result = MovementResult(
        movement="raise_both_arms",
        completed=True,
        confidence=1.0,
        feedback_code="great",
    )

    # Attempt 1
    session.process_result(success_result)
    assert session.total_stars == 1

    # Start new attempt
    session.start_new_attempt()
    assert session.attempt_completed is False
    assert session.attempt_count == 2

    # Attempt 2 success awards another star
    awarded, total = session.process_result(success_result)
    assert awarded == 1
    assert total == 2


def test_scoring_session_non_success_frames_award_zero_stars():
    """Retry, hold, and missing frames award zero stars."""
    session = ScoringSession(current_movement="raise_both_arms")

    retry_result = MovementResult(
        movement="raise_both_arms",
        completed=False,
        confidence=0.5,
        feedback_code="raise_arms",
    )
    awarded, total = session.process_result(retry_result)
    assert awarded == 0
    assert total == 0
    assert session.attempt_completed is False

    hold_result = MovementResult(
        movement="raise_both_arms",
        completed=False,
        confidence=0.9,
        feedback_code="hold",
    )
    awarded, total = session.process_result(hold_result)
    assert awarded == 0
    assert total == 0

    missing_result = MovementResult(
        movement="raise_both_arms",
        completed=False,
        confidence=0.0,
        feedback_code="full_body_missing",
    )
    awarded, total = session.process_result(missing_result)
    assert awarded == 0
    assert total == 0


def test_scoring_session_reset_session_clears_all_stars_and_state():
    """Resetting the session clears total stars, attempt count, and completion state."""
    session = ScoringSession(current_movement="raise_both_arms")
    success_result = MovementResult(
        movement="raise_both_arms",
        completed=True,
        confidence=1.0,
        feedback_code="great",
    )

    session.process_result(success_result)
    assert session.total_stars == 1

    session.reset_session()
    assert session.total_stars == 0
    assert session.attempt_completed is False
    assert session.current_movement is None
    assert session.attempt_count == 0


def test_scoring_session_movement_transition_triggers_new_attempt():
    """Switching to a different movement automatically starts a new attempt."""
    session = ScoringSession(current_movement="raise_both_arms")
    arms_success = MovementResult(
        movement="raise_both_arms",
        completed=True,
        confidence=1.0,
        feedback_code="great",
    )
    reach_success = MovementResult(
        movement="side_reach",
        completed=True,
        confidence=1.0,
        feedback_code="great",
    )

    session.process_result(arms_success)
    assert session.total_stars == 1

    # Transitioning to side_reach automatically starts a new attempt
    awarded, total = session.process_result(reach_success)
    assert awarded == 1
    assert total == 2
    assert session.current_movement == "side_reach"
