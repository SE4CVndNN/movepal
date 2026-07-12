"""Rule-based movement validation contracts."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class MovementResult:
    """Outcome returned by a movement rule."""

    movement: str
    completed: bool
    confidence: float
    feedback_code: str
