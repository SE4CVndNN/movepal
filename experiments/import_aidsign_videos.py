"""Convert existing AidSign MP4 uploads into MovePal landmark JSONL clips.

This creates a temporal holdout: the first part of every video is training data
and the final part is held out for evaluation. It is useful for a pipeline smoke
test, but it is not a substitute for recordings from separate performers.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

MAX_HANDS = 2


def frame_payload(result: Any, frame_index: int, timestamp_ms: int) -> dict[str, Any]:
    hands = []
    for hand_index, hand in enumerate(result.hand_landmarks[:MAX_HANDS]):
        handedness = "unknown"
        if result.handedness and hand_index < len(result.handedness):
            handedness = result.handedness[hand_index][0].category_name.lower()
        hands.append(
            {
                "handedness": handedness,
                "landmarks": [
                    {
                        "index": index,
                        "x": point.x,
                        "y": point.y,
                        "z": point.z,
                    }
                    for index, point in enumerate(hand)
                ],
            }
        )
    return {
        "frame_index": frame_index,
        "timestamp_ms": timestamp_ms,
        "hands": hands,
        "pose": [],
    }


def extract_video(video_path: Path, model_path: Path, split: float, cv2: Any, mp: Any) -> tuple[dict[str, Any], dict[str, Any]]:
    cap = cv2.VideoCapture(str(video_path))
    if not cap.isOpened():
        raise RuntimeError(f"Could not open {video_path.name}.")
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = float(cap.get(cv2.CAP_PROP_FPS) or 0) or 30.0
    boundary = max(1, int(frame_count * split))
    train_frames: list[dict[str, Any]] = []
    held_out_frames: list[dict[str, Any]] = []
    options = mp.tasks.vision.HandLandmarkerOptions(
        base_options=mp.tasks.BaseOptions(model_asset_path=str(model_path)),
        running_mode=mp.tasks.vision.RunningMode.VIDEO,
        num_hands=MAX_HANDS,
    )
    try:
        with mp.tasks.vision.HandLandmarker.create_from_options(options) as detector:
            index = 0
            while True:
                ok, frame = cap.read()
                if not ok:
                    break
                rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb)
                timestamp_ms = max(index, round(index * 1000 / fps))
                result = detector.detect_for_video(image, timestamp_ms)
                payload = frame_payload(result, index, timestamp_ms)
                (train_frames if index < boundary else held_out_frames).append(payload)
                index += 1
    finally:
        cap.release()
    return (
        {"label": video_path.stem, "frames": train_frames},
        {"label": video_path.stem, "frames": held_out_frames},
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-dir", type=Path, default=Path("../aidsign/app/static/signs"))
    parser.add_argument("--model", type=Path, default=Path("data/experiments/hand_landmarker.task"))
    parser.add_argument("--train-output", type=Path, default=Path("data/experiments/aidsign_train.jsonl"))
    parser.add_argument("--test-output", type=Path, default=Path("data/experiments/aidsign_held_out.jsonl"))
    parser.add_argument("--train-fraction", type=float, default=0.7)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if not args.model.is_file():
        raise SystemExit(f"Missing model: {args.model}")
    if not 0.5 <= args.train_fraction < 1:
        raise SystemExit("--train-fraction must be at least 0.5 and below 1")
    try:
        import cv2
        import mediapipe as mp
    except ImportError as error:
        raise SystemExit("Install the experiment dependencies first: pip install -r requirements.txt") from error

    videos = sorted(args.input_dir.glob("*.mp4"))
    if not videos:
        raise SystemExit(f"No MP4 files found in {args.input_dir}")
    args.train_output.parent.mkdir(parents=True, exist_ok=True)
    train_count = test_count = 0
    with args.train_output.open("w", encoding="utf-8") as train_file, args.test_output.open("w", encoding="utf-8") as test_file:
        for video in videos:
            train, held_out = extract_video(video, args.model, args.train_fraction, cv2, mp)
            if train["frames"] and held_out["frames"]:
                train_file.write(json.dumps(train) + "\n")
                test_file.write(json.dumps(held_out) + "\n")
                train_count += len(train["frames"])
                test_count += len(held_out["frames"])
                print(f"{video.name}: {len(train['frames'])} train, {len(held_out['frames'])} held-out frames")
    print(f"Wrote {train_count} training and {test_count} held-out frames from {len(videos)} videos.")


if __name__ == "__main__":
    main()
