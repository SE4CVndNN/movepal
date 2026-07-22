"""Shared side-selection and relative-position helpers for movement rules.

Movements that ask the player to use one anatomical side (side reach, knee
lift, ...) all need the same three primitives: picking the requested
side's own landmark name, measuring how far a joint has moved outward
from the body's midline, and measuring how far it has drifted vertically.
Keeping them here means each movement rule only states its own
thresholds instead of re-deriving the same left/right arithmetic. See
docs/movement_specification.md section 2 for the anatomical-side
convention assumed throughout: ``left``/``right`` always name the user's
own side, never the mirrored preview's screen side.
"""

from __future__ import annotations

from typing import Literal

from app.services.pose_tracking import Landmark, landmark_distance

Side = Literal["left", "right"]


def opposite_side(side: Side) -> Side:
    """Return the anatomical side other than *side*."""
    return "right" if side == "left" else "left"


def side_landmark_name(side: Side, joint: str) -> str:
    """Build the name-keyed landmark key for *joint* on *side*.

    ``side_landmark_name("left", "wrist") == "left_wrist"``.
    """
    return f"{side}_{joint}"


def shoulder_width(left_shoulder: Landmark, right_shoulder: Landmark) -> float:
    """Euclidean distance between the two shoulders.

    The shared body-scale reference every relative measurement
    (reach ratio, vertical offset, ...) is expressed against.
    """
    return landmark_distance(left_shoulder, right_shoulder)


def horizontal_outward_offset(wrist: Landmark, shoulder: Landmark, side: Side) -> float:
    """Signed horizontal distance *wrist* has moved outward from *shoulder*.

    Positive means the wrist is farther from the torso midline than the
    shoulder on *side*; negative means it has crossed inward, toward or
    past the midline. Normalized image ``x`` grows toward the viewer's
    right (docs/movement_specification.md section 12), so "outward" is a
    decreasing ``x`` on the left side and an increasing ``x`` on the
    right side -- this is the one place the left/right mirroring needs an
    explicit sign; every other helper here treats both sides identically.
    """
    if side == "left":
        return shoulder.x - wrist.x
    return wrist.x - shoulder.x


def vertical_offset(wrist: Landmark, shoulder: Landmark) -> float:
    """Absolute vertical distance between *wrist* and *shoulder*."""
    return abs(wrist.y - shoulder.y)
