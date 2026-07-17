#!/usr/bin/env python3
"""Manual MP-005 demo: exercise the pose adapter contract two ways.

This script is a local investigation aid, not part of CI. It shows:

1. an offline synthetic fixture from data/landmarks/pose_fixtures.json
   turned into a PoseResult (no camera, image, or model needed);
2. optionally, a real image run through MediaPipePoseAdapter, so a real
   permitted sample and a fixture both produce a result through the same
   project-owned contract.

The real-image path requires a downloaded MediaPipe Pose Landmarker
``.task`` model bundle (network access, one-time). Get one with:

    python -c "import urllib.request; urllib.request.urlretrieve(
        'https://storage.googleapis.com/mediapipe-models/pose_landmarker/'
        'pose_landmarker_lite/float16/latest/pose_landmarker_lite.task',
        'pose_landmarker_lite.task')"

Usage:

    python scripts/pose_adapter_demo.py
    python scripts/pose_adapter_demo.py --model pose_landmarker_lite.task --image sample.jpg
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app.services.pose_tracking import (  # noqa: E402
    MediaPipePoseAdapter,
    load_pose_fixture,
)


def _print_result(label: str, result) -> None:
    print(f"\n[{label}] status={result.status.value}")
    if result.error:
        print(f"  error: {result.error}")
    for name, landmark in result.landmarks.items():
        print(
            f"  {name:15s} x={landmark.x:.3f} y={landmark.y:.3f} "
            f"z={landmark.z:.3f} visibility={landmark.visibility:.3f}"
        )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--fixture-id",
        default="synthetic_full_visibility_arms_raised_001",
        help="Fixture id from data/landmarks/pose_fixtures.json",
    )
    parser.add_argument(
        "--model", help="Path to a downloaded pose_landmarker*.task file"
    )
    parser.add_argument("--image", help="Path to a permitted sample image")
    args = parser.parse_args()

    fixture_result = load_pose_fixture(args.fixture_id)
    _print_result(f"fixture:{args.fixture_id}", fixture_result)

    if args.model and args.image:
        adapter = MediaPipePoseAdapter(model_path=args.model)
        real_result = adapter.estimate(args.image)
        _print_result(f"real-sample:{args.image}", real_result)
    else:
        print(
            "\n(skipping real-sample path: pass --model and --image to also "
            "run a real permitted sample through the same contract)"
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
