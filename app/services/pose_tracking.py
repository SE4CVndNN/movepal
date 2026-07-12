"""Pose tracking interface.

The real MediaPipe implementation is intentionally deferred to a Sprint 1 task.
CI tests should use small deterministic landmark fixtures rather than a camera.
"""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass


@dataclass(frozen=True)
class Landmark:
    """Normalized pose landmark used by movement rules."""

    name: str
    x: float
    y: float
    z: float
    visibility: float


def visible_landmarks(
    landmarks: Sequence[Landmark], minimum_visibility: float = 0.5
) -> list[Landmark]:
    """Return landmarks that satisfy the selected visibility threshold."""
    return [item for item in landmarks if item.visibility >= minimum_visibility]
