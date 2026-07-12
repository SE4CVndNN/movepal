"""Game scoring helpers."""

from __future__ import annotations


def stars_for_confidence(confidence: float) -> int:
    """Map a normalized confidence score to zero through three stars."""
    bounded = max(0.0, min(1.0, confidence))
    if bounded >= 0.85:
        return 3
    if bounded >= 0.65:
        return 2
    if bounded >= 0.45:
        return 1
    return 0
