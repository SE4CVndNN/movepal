import json
import sys
from pathlib import Path

# Ensure the project package `app` is importable when running this script
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.services.pose_tracking import MediaPipePoseAdapter, PoseStatus

img = Path("app/static/images/avatars/reach-to-the-left.png")
model = Path("pose_landmarker_lite.task")

out = {"image": str(img), "model": str(model)}

try:
    adapter = MediaPipePoseAdapter(model_path=model)
    pose = adapter.estimate(img)
    out["pose_status"] = pose.status.value
    out["error"] = pose.error
    out["landmarks"] = {
        k: {"x": float(v.x), "y": float(v.y), "visibility": float(v.visibility)}
        for k, v in pose.landmarks.items()
    }
    if pose.status == PoseStatus.SUCCESS:
        try:
            from app.services.movement_rules import evaluate_side_reach

            result = evaluate_side_reach(pose.landmarks, "left", consecutive_samples=1)
            out["movement_result"] = {
                "movement": result.movement,
                "completed": result.completed,
                "feedback_code": result.feedback_code,
                "confidence": result.confidence,
            }
        except Exception as exc:
            out["movement_error"] = str(exc)
except Exception as exc:
    out["exception"] = str(exc)

print(json.dumps(out, indent=2))
