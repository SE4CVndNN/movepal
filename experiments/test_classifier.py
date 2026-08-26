"""Evaluate a saved sign classifier on held-out landmark clips.

Use a separate JSONL file for this command so training and test clips do not
silently overlap.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any

from train_classifier import frame_features


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True, help="Held-out JSONL clips")
    parser.add_argument("--model", type=Path, default=Path("data/experiments/sign_classifier.joblib"))
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    try:
        from joblib import load
    except ImportError as error:
        raise SystemExit("Install the experiment dependencies first: pip install -r requirements.txt") from error

    classifier = load(args.model)
    clip_predictions: list[tuple[str, str]] = []
    with args.input.open(encoding="utf-8") as source:
        for line_number, line in enumerate(source, 1):
            if not line.strip():
                continue
            record: dict[str, Any] = json.loads(line)
            expected = record.get("label")
            if not isinstance(expected, str) or not expected.strip():
                raise ValueError(f"Line {line_number} has no non-empty label.")
            features = [
                vector
                for frame in record.get("frames", [])
                if (vector := frame_features(frame)) is not None
            ]
            if not features:
                print(f"Clip {line_number}: skipped (no usable hand landmarks).")
                continue
            predictions = classifier.predict(features)
            predicted = Counter(predictions).most_common(1)[0][0]
            clip_predictions.append((expected, predicted))
            print(f"Clip {line_number}: expected={expected} predicted={predicted}")

    if not clip_predictions:
        raise SystemExit("No usable clips found in the held-out input.")
    correct = sum(expected == predicted for expected, predicted in clip_predictions)
    accuracy = correct / len(clip_predictions)
    print(f"Clip accuracy: {correct}/{len(clip_predictions)} ({accuracy:.1%})")


if __name__ == "__main__":
    main()
