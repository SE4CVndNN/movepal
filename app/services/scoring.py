"""Game scoring helpers and session state machine."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.services.movement_rules import MovementResult


def stars_for_confidence(confidence: float) -> int:
    """Map a normalized confidence score to zero through three stars.

    Reserved for a future graduated scoring feature; not used by the
    MP-014 movement endpoint, whose approved "great" wording is a flat
    "1 Star" regardless of confidence (see stars_for_completion).
    """
    bounded = max(0.0, min(1.0, confidence))
    if bounded >= 0.85:
        return 3
    if bounded >= 0.65:
        return 2
    if bounded >= 0.45:
        return 1
    return 0


def stars_for_completion(completed: bool) -> int:
    """Award the single star promised by the approved "great" wording.

    See docs/movement_specification.md section 12 and
    app/services/feedback.py: a completed attempt's feedback text always
    says "1 Star", so the stars field must match that fixed value rather
    than a variable confidence-scaled count.
    """
    return 1 if completed else 0


class ScoringSession:
    """Finite-state machine for tracking session score and attempt idempotency.

    Prevents repeated success frames from awarding unlimited points by awarding
    stars exactly once per successful attempt. Starting a new attempt or resetting
    the session resets the attempt completion state.
    """

    def __init__(self, current_movement: str | None = None) -> None:
        self.total_stars: int = 0
        self.attempt_completed: bool = False
        self.current_movement: str | None = current_movement
        self.attempt_count: int = 0 if current_movement is None else 1

    def process_result(self, result: MovementResult) -> tuple[int, int]:
        """Evaluate a MovementResult and update total stars idempotently.

        Parameters
        ----------
        result:
            The MovementResult from evaluating a movement frame.

        Returns
        -------
        tuple[int, int]
            A tuple of ``(stars_awarded_this_frame, total_stars_in_session)``.
        """
        movement_name = getattr(result, "movement", None)
        if (
            self.current_movement is not None
            and movement_name is not None
            and movement_name != self.current_movement
        ):
            self.start_new_attempt(movement_name)

        if self.current_movement is None and movement_name is not None:
            self.current_movement = movement_name
            if self.attempt_count == 0:
                self.attempt_count = 1

        if result.completed:
            if not self.attempt_completed:
                self.attempt_completed = True
                stars_awarded = stars_for_completion(True)
                self.total_stars += stars_awarded
                return stars_awarded, self.total_stars
            return 0, self.total_stars

        return 0, self.total_stars

    def start_new_attempt(self, movement: str | None = None) -> None:
        """Reset the attempt completion flag to allow scoring a new attempt.

        Optionally updates ``current_movement``.
        """
        self.attempt_completed = False
        if movement is not None:
            self.current_movement = movement
        self.attempt_count += 1

    def reset_session(self) -> None:
        """Reset the entire session score, attempt count, and completion state."""
        self.total_stars = 0
        self.attempt_completed = False
        self.current_movement = None
        self.attempt_count = 0
