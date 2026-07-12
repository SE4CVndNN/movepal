"""Session summary data structures."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class SessionSummary:
    """Small MVP session summary without personal identifiers."""

    attempted_movements: int
    completed_movements: int
    stars: int
