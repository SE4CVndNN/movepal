"""Game scoring helpers."""

from __future__ import annotations


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
