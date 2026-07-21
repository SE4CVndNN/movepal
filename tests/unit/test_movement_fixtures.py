"""Structural regression checks for MP-005-compatible movement fixtures."""

from __future__ import annotations

import json
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).parents[2]
SCHEMA_PATH = REPOSITORY_ROOT / "data" / "schemas" / "movement_fixture.schema.json"
FIXTURES_DIRECTORY = REPOSITORY_ROOT / "data" / "landmarks"

MOVEMENT_FILE_CONTRACTS = {
    "raise_both_arms_fixtures.json": "raise_both_arms",
    "side_reach_fixtures.json": "side_reach",
    "knee_lift_or_step_fixtures.json": "knee_lift_or_step",
}

APPROVED_FEEDBACK_CODES = {
    "great",
    "raise_arms",
    "reach_left",
    "reach_right",
    "lift_knee",
    "full_body_missing",
}


def _validate_fixture(
    fixture: dict,
    fixture_ids: set[str],
    sides_by_movement: dict[str, set[str]],
    categories_by_movement: dict[str, set[str]],
) -> None:
    """Validate individual fixture structure, unique IDs, and field enums."""
    fixture_id = fixture["id"]
    assert fixture_id not in fixture_ids, f"Duplicate fixture ID found: {fixture_id}"
    fixture_ids.add(fixture_id)

    # Validate feedback code against approved enum values
    feedback_code = fixture.get("expected_feedback_code")
    assert feedback_code in APPROVED_FEEDBACK_CODES, (
        f"Invalid expected_feedback_code '{feedback_code}' in fixture '{fixture_id}'. "
        f"Must be one of {sorted(APPROVED_FEEDBACK_CODES)}"
    )

    movement = fixture["movement"]
    sides_by_movement.setdefault(movement, set()).add(fixture["requested_side"])
    categories_by_movement.setdefault(movement, set()).add(fixture["category"])


def test_movement_fixtures_follow_mp005_structure_and_keep_sides_explicit():
    """Validate all fixture files without a camera or optional schema package."""
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    fixture_paths = [
        FIXTURES_DIRECTORY / filename for filename in MOVEMENT_FILE_CONTRACTS
    ]
    assert all(path.is_file() for path in fixture_paths)
    fixtures_by_path = {
        path.name: json.loads(path.read_text(encoding="utf-8"))
        for path in fixture_paths
    }

    assert schema["type"] == "array"
    assert set(fixtures_by_path) == set(MOVEMENT_FILE_CONTRACTS)
    assert all(isinstance(group, list) and group for group in fixtures_by_path.values())

    fixture_ids: set[str] = set()
    sides_by_movement: dict[str, set[str]] = {}
    categories_by_movement: dict[str, set[str]] = {}
    for filename, group in fixtures_by_path.items():
        for fixture in group:
            assert fixture["movement"] == MOVEMENT_FILE_CONTRACTS[filename]
            _validate_fixture(
                fixture, fixture_ids, sides_by_movement, categories_by_movement
            )

    assert sides_by_movement["side_reach"] == {"left", "right"}
    assert sides_by_movement["knee_lift_or_step"] == {"left", "right"}
