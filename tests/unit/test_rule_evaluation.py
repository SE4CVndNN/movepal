"""Automated rule evaluation and regression tests for MP-021.

Verifies schema compliance, deterministic evaluation across calibration and
held-out landmark fixture sets, and edge-case framing/visibility handling.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from app.services.movement_rules import (
    evaluate_knee_lift,
    evaluate_raise_both_arms,
    evaluate_side_reach,
    landmarks_from_fixture,
    load_movement_fixtures,
)

REPO_ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = REPO_ROOT / "data" / "schemas" / "movement_fixture.schema.json"
LANDMARKS_DIR = REPO_ROOT / "data" / "landmarks"

FIXTURE_FILES = [
    "raise_both_arms_fixtures.json",
    "side_reach_fixtures.json",
    "knee_lift_fixtures.json",
]


def test_schema_file_exists_and_is_valid_json():
    assert SCHEMA_PATH.is_file()
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    assert schema.get("$schema")
    assert schema.get("title")


@pytest.mark.parametrize("filename", FIXTURE_FILES)
def test_fixture_files_exist_and_contain_fixtures(filename: str):
    path = LANDMARKS_DIR / filename
    assert path.is_file()
    fixtures = load_movement_fixtures(filename)
    assert len(fixtures) >= 10


def _all_fixtures():
    fixtures = []
    for filename in FIXTURE_FILES:
        for f in load_movement_fixtures(filename):
            fixtures.append((f["fixture_id"], filename, f))
    return fixtures


@pytest.mark.parametrize("fixture_id, filename, fixture", _all_fixtures())
def test_all_fixtures_evaluate_to_expected_outcomes(
    fixture_id: str, filename: str, fixture: dict
):
    movement = fixture["movement"]
    landmarks = landmarks_from_fixture(fixture)
    consecutive = fixture.get("observed_consecutive_samples", 2)
    requested_side = fixture.get("requested_side", "both")

    if movement == "raise_both_arms":
        result = evaluate_raise_both_arms(landmarks, consecutive_samples=consecutive)
    elif movement == "side_reach":
        result = evaluate_side_reach(
            landmarks, requested_side, consecutive_samples=consecutive
        )
    elif movement == "knee_lift_or_step":
        result = evaluate_knee_lift(
            landmarks, requested_side, consecutive_samples=consecutive
        )
    else:
        pytest.fail(f"Unknown movement {movement} in {fixture_id}")

    assert result.completed is fixture["expected_completed"], (
        f"Fixture {fixture_id}: expected completed={fixture['expected_completed']}, "
        f"got {result.completed}"
    )
    assert result.feedback_code == fixture["expected_feedback_code"], (
        f"Fixture {fixture_id}: expected feedback_code={fixture['expected_feedback_code']}, "
        f"got {result.feedback_code}"
    )


def test_evaluation_script_runs_successfully():
    from scripts.evaluate_rules import run_evaluation

    assert run_evaluation() is True
