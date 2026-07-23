"""Unit tests for the MP-018 session-state service.

The service is exercised with a plain ``dict`` as storage, so no Flask
request context is required and the behavior is fully deterministic.
"""

from __future__ import annotations

from app.services.movement_rules import MovementResult
from app.services.scoring import ScoringSession
from app.services.session_state import STORAGE_KEY, SessionStateService
from app.services.session_summary import SessionSummary


def _success(movement: str) -> MovementResult:
    return MovementResult(
        movement=movement, completed=True, confidence=1.0, feedback_code="great"
    )


def test_initialization_produces_empty_summary():
    service = SessionStateService({})
    summary = service.build_summary()

    assert summary == SessionSummary(
        attempted_movements=0, completed_movements=0, stars=0
    )
    assert service.is_finished() is False


def test_record_attempt_counts_distinct_movements():
    service = SessionStateService({})

    service.record_attempt("raise_both_arms")
    service.record_attempt("raise_both_arms")  # duplicate ignored
    service.record_attempt("side_reach")
    service.record_attempt("knee_lift_or_step")

    assert service.build_summary().attempted_movements == 3


def test_record_completion_counts_distinct_movements():
    service = SessionStateService({})

    service.record_completion("raise_both_arms")
    service.record_completion("raise_both_arms")  # duplicate ignored
    service.record_completion("side_reach")

    assert service.build_summary().completed_movements == 2


def test_records_all_three_activities():
    """Acceptance: a session records all three activities."""
    service = SessionStateService({})
    for movement in ("raise_both_arms", "side_reach", "knee_lift_or_step"):
        service.record_result(_success(movement), completed=True)

    summary = service.build_summary()
    assert summary.attempted_movements == 3
    assert summary.completed_movements == 3


def test_scoring_session_round_trip_persists_stars():
    storage: dict = {}
    service = SessionStateService(storage)

    scoring = service.load_scoring_session()
    scoring.process_result(_success("raise_both_arms"))
    service.save_scoring_session(scoring)

    # A fresh service over the same storage sees the persisted total.
    reloaded = SessionStateService(storage).load_scoring_session()
    assert isinstance(reloaded, ScoringSession)
    assert reloaded.total_stars == 1
    assert reloaded.current_movement == "raise_both_arms"


def test_record_result_updates_attempt_and_completion():
    service = SessionStateService({})

    service.record_result(_success("raise_both_arms"), completed=True)
    incomplete = MovementResult(
        movement="side_reach",
        completed=False,
        confidence=0.4,
        feedback_code="reach_left",
    )
    service.record_result(incomplete, completed=False)

    summary = service.build_summary()
    assert summary.attempted_movements == 2
    assert summary.completed_movements == 1


def test_reset_clears_all_state():
    storage: dict = {}
    service = SessionStateService(storage)

    scoring = service.load_scoring_session()
    scoring.process_result(_success("raise_both_arms"))
    service.save_scoring_session(scoring)
    service.record_result(_success("raise_both_arms"), completed=True)
    service.finish()

    service.reset()

    summary = service.build_summary()
    assert summary == SessionSummary(
        attempted_movements=0, completed_movements=0, stars=0
    )
    assert service.is_finished() is False
    assert service.load_scoring_session().total_stars == 0


def test_finish_marks_finished_and_returns_summary():
    service = SessionStateService({})
    service.record_result(_success("raise_both_arms"), completed=True)

    summary = service.finish()

    assert service.is_finished() is True
    assert summary.attempted_movements == 1
    assert summary.completed_movements == 1


def test_finish_is_idempotent_and_awards_no_stars():
    storage: dict = {}
    service = SessionStateService(storage)

    scoring = service.load_scoring_session()
    scoring.process_result(_success("raise_both_arms"))
    service.save_scoring_session(scoring)
    service.record_result(_success("raise_both_arms"), completed=True)

    first = service.finish()
    second = service.finish()

    assert first == second
    assert first.stars == 1  # unchanged by finishing


def test_summary_reflects_persisted_star_total():
    storage: dict = {}
    service = SessionStateService(storage)

    scoring = service.load_scoring_session()
    scoring.process_result(_success("raise_both_arms"))
    service.save_scoring_session(scoring)

    assert service.build_summary().stars == 1


def test_state_lives_under_single_namespaced_key():
    storage: dict = {}
    SessionStateService(storage).record_attempt("raise_both_arms")

    assert set(storage.keys()) == {STORAGE_KEY}
