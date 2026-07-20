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
    "knee_lift_fixtures.json": "knee_lift_or_step",
}
MP005_FIELDS = {
    "fixture_id",
    "schema_version",
    "source_type",
    "provenance_reference",
    "description",
    "expected_status",
    "annotator",
    "landmarks",
}
MOVEMENT_FIELDS = {
    "movement",
    "requested_side",
    "expected_completed",
    "expected_feedback_code",
    "category",
    "observed_consecutive_samples",
}
LANDMARK_FIELDS = {"x", "y", "z", "visibility"}
LANDMARK_NAMES = {
    f"{side}_{joint}"
    for side in ("left", "right")
    for joint in (
        "shoulder",
        "elbow",
        "wrist",
        "hip",
        "knee",
        "ankle",
    )
}
MOVEMENT_VALUES = set(MOVEMENT_FILE_CONTRACTS.values())
CATEGORY_VALUES = {"positive", "negative", "borderline", "low_visibility"}
REQUESTED_SIDE_VALUES = {"left", "right", "both"}
EXPECTED_STATUS_VALUES = {"success", "retry", "low_visibility"}


def test_movement_fixtures_follow_mp005_structure_and_keep_sides_explicit():
    """Validate all fixture files without a camera or optional schema package."""
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    fixture_paths = sorted(FIXTURES_DIRECTORY.glob("*_fixtures.json"))
    fixtures_by_path = {
        path.name: json.loads(path.read_text(encoding="utf-8"))
        for path in fixture_paths
    }

    assert schema["type"] == "array"
    assert set(schema["items"]["required"]) == MP005_FIELDS | MOVEMENT_FIELDS
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
    for movement in MOVEMENT_VALUES:
        assert categories_by_movement[movement] == CATEGORY_VALUES


def _validate_fixture(
    fixture: dict,
    fixture_ids: set[str],
    sides_by_movement: dict[str, set[str]],
    categories_by_movement: dict[str, set[str]],
) -> None:
    """Validate MP-005 metadata and MP-007 movement requirements."""
    assert set(fixture) == MP005_FIELDS | MOVEMENT_FIELDS
    assert fixture["fixture_id"] not in fixture_ids
    fixture_ids.add(fixture["fixture_id"])
    assert fixture["schema_version"] == "1.0"
    assert fixture["source_type"] == "synthetic"
    assert fixture["description"]
    assert fixture["provenance_reference"]
    assert fixture["annotator"]
    assert fixture["movement"] in MOVEMENT_VALUES
    assert fixture["category"] in CATEGORY_VALUES
    assert fixture["requested_side"] in REQUESTED_SIDE_VALUES
    assert fixture["expected_status"] in EXPECTED_STATUS_VALUES
    assert isinstance(fixture["expected_completed"], bool)
    assert isinstance(fixture["observed_consecutive_samples"], int)
    assert fixture["observed_consecutive_samples"] >= 0
    assert isinstance(fixture["landmarks"], dict)
    assert fixture["landmarks"]
    for name, landmark in fixture["landmarks"].items():
        assert name in LANDMARK_NAMES
        assert set(landmark) == LANDMARK_FIELDS
        assert 0 <= landmark["x"] <= 1
        assert 0 <= landmark["y"] <= 1
        assert -1 <= landmark["z"] <= 1
        assert 0 <= landmark["visibility"] <= 1
    sides_by_movement.setdefault(fixture["movement"], set()).add(
        fixture["requested_side"]
    )
    categories_by_movement.setdefault(fixture["movement"], set()).add(
        fixture["category"]
    )
