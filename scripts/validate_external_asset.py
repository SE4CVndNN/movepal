#!/usr/bin/env python3
"""MP-020 compatibility spike: validate an external/permitted sample against
MovePal's project-owned pose contract and fixture shape.

This is a local, manual reproducibility aid (same spirit as
scripts/pose_adapter_demo.py), not part of CI. It supports two inputs so it
can be exercised without any network access, model file, or personal image:

1. --fixture-json: a local JSON file already containing a "landmarks" dict
   (e.g. docs/evidence/mp-020-external-sample-landmarks.json, or a tiny
   synthetic/mocked file used by pytest). This path needs no network access,
   model file, or image and is what CI/unit tests use.
2. --model and --image: run a real permitted sample through
   MediaPipePoseAdapter, exactly like scripts/pose_adapter_demo.py, then
   validate the result. Requires a locally downloaded .task model and a
   permitted local image; never used in CI.

Known limitation (see docs/external_asset_evaluation.md section 5): this
script checks landmark names and x/y/z/visibility ranges against the same
rules data/schemas/movement_fixture.schema.json expresses, but it does not
claim "source_type": "synthetic", so its output is not meant to be dropped
into the three schema-enforced fixture files under data/landmarks/ — it is
evidence for this task's spike, not a new MP-007 fixture.

Never prints image bytes, file contents beyond landmark numbers, or any
path other than what the caller passed in.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app.services.pose_tracking import (  # noqa: E402
    TRACKED_LANDMARK_NAMES,
    MediaPipePoseAdapter,
    PoseStatus,
    pose_result_from_fixture_data,
)

LANDMARK_NAMES = {
    f"{side}_{joint}"
    for side in ("left", "right")
    for joint in ("shoulder", "elbow", "wrist", "hip", "knee", "ankle")
}


class ExternalAssetError(ValueError):
    """Raised when the external asset/input cannot be validated."""


def load_landmarks_from_json(path: Path) -> dict[str, Any]:
    """Load a {"landmarks": {...}} JSON file. Never downloads anything."""
    if not path.is_file():
        raise ExternalAssetError(f"No such fixture JSON file: {path}")
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ExternalAssetError(f"{path} is not valid JSON: {exc}") from exc
    landmarks = data.get("landmarks")
    if not isinstance(landmarks, dict) or not landmarks:
        raise ExternalAssetError(f"{path} has no non-empty 'landmarks' object")
    return landmarks


def validate_landmark_shape(landmarks: dict[str, Any]) -> list[str]:
    """Check landmark names/ranges against the fixture schema's per-landmark
    rules. Returns a list of human-readable problems (empty = compatible).
    """
    problems: list[str] = []
    for name, values in landmarks.items():
        if name not in LANDMARK_NAMES:
            problems.append(f"'{name}' is not a recognized MovePal landmark name")
            continue
        if not isinstance(values, dict):
            problems.append(f"'{name}' value is not an object")
            continue
        for field in ("x", "y", "z", "visibility"):
            if field not in values:
                problems.append(f"'{name}' is missing '{field}'")
            if "x" in values:
                if not isinstance(values["x"], (int, float)):
                    problems.append(f"'{name}'.x must be numeric, got {type(values['x']).__name__}")
                elif not (0.0 <= values["x"] <= 1.0):
                    problems.append(f"'{name}'.x={values['x']} outside [0, 1]")
          
            if "y" in values:
                if not isinstance(values["y"], (int, float)):
                    problems.append(f"'{name}'.y must be numeric, got {type(values['y']).__name__}")
                elif not (0.0 <= values["y"] <= 1.0):
                    problems.append(f"'{name}'.y={values['y']} outside [0, 1]")
          
            if "z" in values:
                if not isinstance(values["z"], (int, float)):
                    problems.append(f"'{name}'.z must be numeric, got {type(values['z']).__name__}")
                elif not (-1.0 <= values["z"] <= 1.0):
                    problems.append(f"'{name}'.z={values['z']} outside [-1, 1]")
            
            if "visibility" in values:
                if not isinstance(values["visibility"], (int, float)):
                    problems.append(f"'{name}'.visibility must be numeric, got {type(values['visibility']).__name__}")
                elif not (0.0 <= values["visibility"] <= 1.0):
                    problems.append(f"'{name}'.visibility={values['visibility']} outside [0, 1]")

    return problems





def validate_external_asset(
    *,
    fixture_json: Path | None = None,
    model_path: Path | None = None,
    image_path: Path | None = None,
) -> dict[str, Any]:
    """Validate one external/permitted sample against the MovePal contract.

    Exactly one of (fixture_json) or (model_path AND image_path) must be
    given. Raises ExternalAssetError on missing/unsupported input rather
    than letting an unrelated exception escape.
    """
    if fixture_json is not None:
        landmarks_raw = load_landmarks_from_json(fixture_json)
        # Treat local fixture JSON as external evidence: validate
        # conservatively against the full tracked landmark set.
        pose_result = pose_result_from_fixture_data(
            {"landmarks": landmarks_raw}, conservative=True
        )
    elif model_path is not None and image_path is not None:
        if not model_path.is_file():
            raise ExternalAssetError(f"Model file not found: {model_path}")
        if not image_path.is_file():
            raise ExternalAssetError(f"Image file not found: {image_path}")
        adapter = MediaPipePoseAdapter(model_path=model_path)
        pose_result = adapter.estimate(image_path)
        landmarks_raw = {
            name: {"x": lm.x, "y": lm.y, "z": lm.z, "visibility": lm.visibility}
            for name, lm in pose_result.landmarks.items()
        }
    else:
        raise ExternalAssetError(
            "Provide either --fixture-json, or both --model and --image."
        )

    shape_problems = validate_landmark_shape(landmarks_raw)
    missing_tracked = [
        name for name in TRACKED_LANDMARK_NAMES if name not in landmarks_raw
    ]

    return {
        "status": pose_result.status.value,
        "landmark_count": len(landmarks_raw),
        "missing_tracked_landmarks": missing_tracked,
        "shape_problems": shape_problems,
        "is_compatible": (
            pose_result.status == PoseStatus.SUCCESS and not shape_problems
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--fixture-json",
        type=Path,
        help="Local JSON file with a 'landmarks' object (no network/model needed)",
    )
    parser.add_argument(
        "--model", type=Path, help="Path to a downloaded pose_landmarker*.task file"
    )
    parser.add_argument(
        "--image",
        type=Path,
        help="Path to a permitted local sample image (never committed)",
    )
    args = parser.parse_args()

    try:
        report = validate_external_asset(
            fixture_json=args.fixture_json,
            model_path=args.model,
            image_path=args.image,
        )
    except ExternalAssetError as exc:
        print(f"ERROR: {exc}")
        return 1

    print(json.dumps(report, indent=2))
    return 0 if report["is_compatible"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
