"""Friendly, non-medical feedback messages and orchestration service.

Wording for ``great``, movement corrections, ``hold``, and
``full_body_missing`` must match the approved wording table
in docs/movement_specification.md section 12 ("Result and
friendly-feedback mapping") and docs/content_baseline.md.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.services.movement_rules import MovementResult
    from app.services.scoring import ScoringSession

_MOVEMENT_CORRECTION_TEXT = (
    "This picture doesn't show the move we asked for. Try again with the right pose."
)
"""Shared wording for every movement-specific correction code.

Section 12's table intentionally gives ``raise_arms``, ``reach_left``,
``reach_right``, and ``lift_knee`` the identical approved sentence -- the
distinction between movements and sides is carried by ``feedback_code``,
not by different wording, so it is defined once here rather than repeated
per key (and risking the two sides drifting apart).
"""

FEEDBACK_MESSAGES: dict[str, str] = {
    "great": "Awesome job! You've earned ⭐ 1 Star!",
    "raise_arms": "You need both arms up. Try a picture with your hands above your shoulders.",
    "reach_left": "I asked for a left-side reach. Use your left arm to stretch out to the side.",
    "reach_right": "I asked for a right-side reach. Use your right arm to stretch out to the side.",
    "lift_knee": "I asked for a knee lift. Try lifting your knee up in front like a marching move.",
    "move_back": "Move slightly farther from the camera.",
    "hold": "Hold your pose a little longer so I can see the whole move.",
    "full_body_missing": (
        "We lost track of you! Please step back so your full body is "
        "visible in the frame."
    ),
    "try_again": "Looks like that one missed the move. Try again with the right pose.",
}

VISIBILITY_FRAMING_CODES: set[str] = {"full_body_missing", "move_back"}
"""Feedback codes representing visibility or framing issues."""


@dataclass(frozen=True)
class FeedbackResult:
    """Orchestrated user-facing feedback and reward result."""

    feedback_code: str
    message: str
    completed: bool
    stars_awarded: int
    total_stars: int
    visibility_ok: bool
    retryable: bool


def get_feedback_message(feedback_code: str) -> str:
    """Return the user-facing friendly message for *feedback_code*.

    Guarantees every observation code maps to a non-medical friendly
    message from the catalog, falling back to a default encouraging
    correction if an unknown code is provided.
    """
    return FEEDBACK_MESSAGES.get(feedback_code, _MOVEMENT_CORRECTION_TEXT)


def format_feedback(
    result: MovementResult, session: ScoringSession | None = None
) -> FeedbackResult:
    """Turn a raw MovementResult into a user-facing FeedbackResult.

    Parameters
    ----------
    result:
        The MovementResult returned by a movement rule evaluation.
    session:
        Optional ScoringSession tracking cumulative stars and attempt status.
        If omitted, star awards are calculated statelessly (1 if completed else 0).

    Returns
    -------
    FeedbackResult
        The orchestrated feedback outcome, prioritizing visibility/framing
        messages over technique feedback and providing idempotent star counts.
    """
    visibility_ok = result.feedback_code not in VISIBILITY_FRAMING_CODES

    if session is not None:
        # Call into the session to update stars. However, format_feedback
        # must be idempotent for repeated frames within the same active
        # attempt: if the session already reported the previous attempt as
        # completed, do not allow this call to award additional stars or
        # mutate the session state.
        before_total = session.total_stars
        before_attempt_count = session.attempt_count
        before_attempt_completed = session.attempt_completed
        before_current_movement = session.current_movement

        stars_awarded, total_stars = session.process_result(result)

        if before_attempt_completed and result.completed:
            # Revert any session-side mutation performed by process_result
            # and report zero newly-awarded stars for idempotence.
            session.total_stars = before_total
            session.attempt_completed = before_attempt_completed
            session.attempt_count = before_attempt_count
            session.current_movement = before_current_movement
            stars_awarded = 0
            total_stars = before_total
    else:
        stars_awarded = 1 if result.completed else 0
        total_stars = stars_awarded

    message = get_feedback_message(result.feedback_code)

    return FeedbackResult(
        feedback_code=result.feedback_code,
        message=message,
        completed=result.completed,
        stars_awarded=stars_awarded,
        total_stars=total_stars,
        visibility_ok=visibility_ok,
        retryable=True,
    )
