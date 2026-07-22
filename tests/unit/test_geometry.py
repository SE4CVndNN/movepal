"""Unit tests for the shared side-selection and relative-position helpers."""

from __future__ import annotations

import pytest

from app.services.geometry import (
    horizontal_outward_offset,
    opposite_side,
    shoulder_width,
    side_landmark_name,
    vertical_offset,
)
from app.services.pose_tracking import Landmark


def test_opposite_side_is_its_own_inverse():
    assert opposite_side("left") == "right"
    assert opposite_side("right") == "left"


@pytest.mark.parametrize("side", ["left", "right"])
def test_side_landmark_name_builds_name_keyed_key(side):
    assert side_landmark_name(side, "wrist") == f"{side}_wrist"
    assert side_landmark_name(side, "shoulder") == f"{side}_shoulder"


def test_shoulder_width_matches_landmark_distance():
    left = Landmark("left_shoulder", 0.35, 0.4, 0.0, 0.9)
    right = Landmark("right_shoulder", 0.65, 0.4, 0.0, 0.9)

    assert shoulder_width(left, right) == pytest.approx(0.3)


def test_horizontal_outward_offset_is_symmetric_for_mirrored_reaches():
    left_shoulder = Landmark("left_shoulder", 0.35, 0.4, 0.0, 0.9)
    right_shoulder = Landmark("right_shoulder", 0.65, 0.4, 0.0, 0.9)
    left_wrist = Landmark("left_wrist", 0.05, 0.4, 0.0, 0.9)
    right_wrist = Landmark("right_wrist", 0.95, 0.4, 0.0, 0.9)

    left_offset = horizontal_outward_offset(left_wrist, left_shoulder, "left")
    right_offset = horizontal_outward_offset(right_wrist, right_shoulder, "right")

    assert left_offset == pytest.approx(0.3)
    assert right_offset == pytest.approx(0.3)


def test_horizontal_outward_offset_is_negative_when_wrist_crosses_midline():
    left_shoulder = Landmark("left_shoulder", 0.35, 0.4, 0.0, 0.9)
    inward_wrist = Landmark("left_wrist", 0.6, 0.4, 0.0, 0.9)

    assert horizontal_outward_offset(inward_wrist, left_shoulder, "left") < 0


def test_vertical_offset_is_symmetric_above_and_below():
    shoulder = Landmark("left_shoulder", 0.35, 0.4, 0.0, 0.9)
    above = Landmark("left_wrist", 0.35, 0.3, 0.0, 0.9)
    below = Landmark("left_wrist", 0.35, 0.5, 0.0, 0.9)

    assert vertical_offset(above, shoulder) == pytest.approx(0.1)
    assert vertical_offset(below, shoulder) == pytest.approx(0.1)
