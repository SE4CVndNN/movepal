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

_MOVEMENT_CORRECTION_TEXT = "Please adjust your pose slightly."
"""Shared wording for every movement-specific correction code.

Section 12's table intentionally gives ``raise_arms``, ``reach_left``,
``reach_right``, and ``lift_knee`` the identical approved sentence -- the
distinction between movements and sides is carried by ``feedback_code``,
not by different wording, so it is defined once here rather than repeated
per key (and risking the two sides drifting apart).
"""

FEEDBACK_MESSAGES: dict[str, str] = {
    "great": "Awesome job! You've earned ⭐ 1 Star!",
    "raise_arms": _MOVEMENT_CORRECTION_TEXT,
    "reach_left": _MOVEMENT_CORRECTION_TEXT,
    "reach_right": _MOVEMENT_CORRECTION_TEXT,
    "lift_knee": _MOVEMENT_CORRECTION_TEXT,
    "move_back": "Move slightly farther from the camera.",
    "hold": "Please hold a bit longer for better validation.",
    "full_body_missing": (
        "We lost track of you! Please step back so your full body is "
        "visible in the frame."
    ),
    "try_again": "Try again.",
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
        stars_awarded, total_stars = session.process_result(result)
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
