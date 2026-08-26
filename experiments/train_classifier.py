"""Train a lightweight sign classifier from captured landmark clips.

The input is JSONL produced by capture_landmarks.py. Each detected frame becomes
one training row after translation to the wrist and scale normalization, which
makes the first experiment less sensitive to camera distance and hand position.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any

LANDMARK_COUNT = 21


def frame_features(frame: dict[str, Any]) -> list[float] | None:
    """Return a translation/scale-normalized feature vector for the first hand."""
    hands = frame.get("hands", [])
    if not hands:
        return None
    points = sorted(hands[0].get("landmarks", []), key=lambda point: point.get("index", -1))
    if len(points) != LANDMARK_COUNT:
        return None
    wrist = points[0]
    relative = [
        (point["x"] - wrist["x"], point["y"] - wrist["y"], point["z"] - wrist["z"])
        for point in points
    ]
    scale = max(
        max(abs(x) for x, _, _ in relative),
        max(abs(y) for _, y, _ in relative),
        1e-6,
    )
    return [coordinate / scale for point in relative for coordinate in point]


def load_dataset(path: Path) -> tuple[list[list[float]], list[str]]:
    features: list[list[float]] = []
    labels: list[str] = []
    with path.open(encoding="utf-8") as source:
        for line_number, line in enumerate(source, 1):
            if not line.strip():
                continue
            record = json.loads(line)
            label = record.get("label")
            if not isinstance(label, str) or not label.strip():
                raise ValueError(f"Line {line_number} has no non-empty label.")
            for frame in record.get("frames", []):
                vector = frame_features(frame)
                if vector is not None:
                    features.append(vector)
                    labels.append(label)
    return features, labels


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=Path("data/experiments/landmarks.jsonl"))
    parser.add_argument("--output", type=Path, default=Path("data/experiments/sign_classifier.joblib"))
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    try:
        from joblib import dump
        from sklearn.pipeline import make_pipeline
        from sklearn.preprocessing import StandardScaler
        from sklearn.svm import SVC
    except ImportError as error:
        raise SystemExit("Install the experiment dependencies first: pip install -r requirements.txt") from error

    features, labels = load_dataset(args.input)
    label_counts = Counter(labels)
    if len(label_counts) < 2:
        raise SystemExit("Capture at least two different labels before training.")
    if min(label_counts.values()) < 2:
        raise SystemExit("Capture at least two detected frames for every label.")

    classifier = make_pipeline(StandardScaler(), SVC(kernel="rbf", probability=True))
    classifier.fit(features, labels)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    dump(classifier, args.output)
    print(f"Saved {args.output} ({len(features)} frames, labels: {dict(label_counts)}).")


if __name__ == "__main__":
    main()
