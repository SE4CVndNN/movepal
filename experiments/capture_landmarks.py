"""Capture labeled hand-landmark clips from a webcam.

Usage:
    python experiments/capture_landmarks.py --label hello --clips 10

Press SPACE to record one clip and Q to quit. The webcam preview is display-only;
only normalized landmarks and timestamps are written to JSON.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

MAX_HANDS = 2


def _landmark(hand: Any, index: int) -> dict[str, float | int]:
    point = hand.landmark[index]
    return {"index": index, "x": point.x, "y": point.y, "z": point.z}


def _frame_payload(result: Any, frame_index: int) -> dict[str, Any]:
    hands = []
    for hand_index, hand in enumerate(result.multi_hand_landmarks[:MAX_HANDS]):
        handedness = "unknown"
        if result.multi_handedness and hand_index < len(result.multi_handedness):
            handedness = result.multi_handedness[hand_index].classification[0].label.lower()
        hands.append(
            {
                "handedness": handedness,
                "landmarks": [_landmark(hand, index) for index in range(21)],
            }
        )
    return {
        "frame_index": frame_index,
        "timestamp_ms": frame_index * 33,
        "hands": hands,
        "pose": [],
    }


def capture_clip(cap: Any, hands: Any, cv2: Any) -> list[dict[str, Any]]:
    frames: list[dict[str, Any]] = []
    while True:
        ok, image = cap.read()
        if not ok:
            raise RuntimeError("The webcam stopped returning frames.")
        result = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        if result.multi_hand_landmarks:
            frames.append(_frame_payload(result, len(frames)))
        cv2.imshow("MovePal landmark capture - SPACE saves, Q quits", image)
        key = cv2.waitKey(1) & 0xFF
        if key in (ord(" "), 13) or len(frames) >= 60:
            return frames
        if key == ord("q"):
            return []


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--label", required=True, help="Label for the sign being recorded")
    parser.add_argument("--clips", type=int, default=10, help="Number of clips to capture")
    parser.add_argument("--output", type=Path, default=Path("data/experiments/landmarks.jsonl"))
    parser.add_argument("--camera", type=int, default=0)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.clips < 1:
        raise SystemExit("--clips must be at least 1")

    try:
        import cv2
        import mediapipe as mp
    except ImportError as error:
        raise SystemExit("Install the experiment dependencies first: pip install -r requirements.txt") from error

    args.output.parent.mkdir(parents=True, exist_ok=True)
    cap = cv2.VideoCapture(args.camera)
    if not cap.isOpened():
        raise SystemExit(f"Could not open camera {args.camera}.")

    try:
        with mp.solutions.hands.Hands(
            static_image_mode=False,
            max_num_hands=MAX_HANDS,
            min_detection_confidence=0.6,
            min_tracking_confidence=0.6,
        ) as hands, args.output.open("a", encoding="utf-8") as output:
            print("Show the sign, then press SPACE to save each clip. Press Q to quit.")
            for clip_number in range(args.clips):
                input(f"Ready for clip {clip_number + 1}/{args.clips}; press Enter...")
                frames = capture_clip(cap, hands, cv2)
                if not frames:
                    break
                output.write(json.dumps({"label": args.label, "frames": frames}) + "\n")
                output.flush()
                print(f"Saved clip with {len(frames)} detected frames.")
    finally:
        cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
