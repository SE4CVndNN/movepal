"""Video sign recognition using the verified landmark classifier."""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from importlib import import_module
from pathlib import Path
from typing import Any

LANDMARK_COUNT = 21
MAX_HANDS = 2


@dataclass(frozen=True)
class SignRecognitionResult:
    """Safe result contract for one uploaded sign video."""

    status: str
    label: str | None = None
    confidence: float | None = None
    frames_processed: int = 0
    detected_frames: int = 0
    error: str | None = None


def frame_features(frame: Any) -> list[float] | None:
    """Build the same wrist-relative feature vector used during training."""
    hands = frame.hand_landmarks
    if not hands:
        return None
    points = hands[0]
    if len(points) != LANDMARK_COUNT:
        return None
    wrist = points[0]
    relative = [
        (point.x - wrist.x, point.y - wrist.y, point.z - wrist.z)
        for point in points
    ]
    scale = max(
        max(abs(x) for x, _, _ in relative),
        max(abs(y) for _, y, _ in relative),
        1e-6,
    )
    return [coordinate / scale for point in relative for coordinate in point]


class SignRecognizer:
    """Reusable MediaPipe Tasks and scikit-learn video recognizer."""

    def __init__(self, model_path: str | Path, classifier_path: str | Path) -> None:
        self._model_path = Path(model_path)
        self._classifier_path = Path(classifier_path)
        self._classifier: Any | None = None

    def _load_classifier(self) -> Any:
        if self._classifier is None:
            if not self._classifier_path.is_file():
                raise FileNotFoundError("Sign classifier model is not configured.")
            joblib = import_module("joblib")
            self._classifier = joblib.load(self._classifier_path)
        return self._classifier

    def recognize(self, video_path: str | Path, max_frames: int = 120) -> SignRecognitionResult:
        try:
            if not self._model_path.is_file():
                return SignRecognitionResult(status="unavailable", error="Hand landmark model is unavailable.")
            classifier = self._load_classifier()
            cv2 = import_module("cv2")
            mediapipe = import_module("mediapipe")
            capture = cv2.VideoCapture(str(video_path))
            if not capture.isOpened():
                return SignRecognitionResult(status="error", error="Video could not be opened.")
            fps = float(capture.get(cv2.CAP_PROP_FPS) or 0) or 30.0
            predictions: list[str] = []
            confidences: list[float] = []
            processed = 0
            try:
                options = mediapipe.tasks.vision.HandLandmarkerOptions(
                    base_options=mediapipe.tasks.BaseOptions(
                        model_asset_path=str(self._model_path)
                    ),
                    running_mode=mediapipe.tasks.vision.RunningMode.VIDEO,
                    num_hands=MAX_HANDS,
                )
                with mediapipe.tasks.vision.HandLandmarker.create_from_options(options) as detector:
                    while processed < max_frames:
                        ok, frame = capture.read()
                        if not ok:
                            break
                        image = mediapipe.Image(
                            image_format=mediapipe.ImageFormat.SRGB,
                            data=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB),
                        )
                        timestamp_ms = max(processed, round(processed * 1000 / fps))
                        result = detector.detect_for_video(image, timestamp_ms)
                        vector = frame_features(result)
                        processed += 1
                        if vector is None:
                            continue
                        prediction = classifier.predict([vector])[0]
                        predictions.append(str(prediction))
                        if hasattr(classifier, "predict_proba"):
                            probabilities = classifier.predict_proba([vector])[0]
                            classes = list(classifier.classes_)
                            confidences.append(float(probabilities[classes.index(prediction)]))
            finally:
                capture.release()
        except (ImportError, FileNotFoundError) as error:
            return SignRecognitionResult(status="unavailable", error=str(error))
        except Exception as error:  # noqa: BLE001 - controlled upload failure
            return SignRecognitionResult(status="error", error=str(error))

        if not predictions:
            return SignRecognitionResult(
                status="no_hand_detected",
                frames_processed=processed,
            )
        label = Counter(predictions).most_common(1)[0][0]
        confidence = sum(confidences) / len(confidences) if confidences else None
        return SignRecognitionResult(
            status="success",
            label=label,
            confidence=confidence,
            frames_processed=processed,
            detected_frames=len(predictions),
        )
