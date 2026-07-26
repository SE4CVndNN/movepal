import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.services.pose_tracking import MediaPipePoseAdapter
from app.services.movement_rules import evaluate_side_reach
from app.services.geometry import (
    side_landmark_name,
    horizontal_outward_offset,
    vertical_offset,
    angle_at_joint,
    shoulder_width,
    opposite_side,
)

img = Path('app/static/images/avatars/reach-to-the-right.png')
adapter = MediaPipePoseAdapter(model_path=Path('pose_landmarker_lite.task'))
pose = adapter.estimate(img)
landmarks = pose.landmarks

requested_side = 'right'
left_shoulder = landmarks['left_shoulder']
right_shoulder = landmarks['right_shoulder']
left_hip = landmarks['left_hip']
right_hip = landmarks['right_hip']
width = shoulder_width(left_shoulder, right_shoulder)

wrist_name = side_landmark_name(requested_side, 'wrist')
elbow_name = side_landmark_name(requested_side, 'elbow')
opp_side = opposite_side(requested_side)
opp_elbow = side_landmark_name(opp_side, 'elbow')
opp_wrist = side_landmark_name(opp_side, 'wrist')

wrist = landmarks[wrist_name]
elbow = landmarks[elbow_name]
opp_el = landmarks[opp_elbow]
opp_wr = landmarks[opp_wrist]

reach_ratio = 0.85
vertical_ratio = 0.5
lenient = True
effective_reach_ratio = min(reach_ratio, 0.74) if lenient else reach_ratio
effective_vertical_ratio = max(vertical_ratio, 0.8) if lenient else vertical_ratio
elbow_angle_threshold = 125.0 if lenient else 170.0

outward = horizontal_outward_offset(wrist, right_shoulder, requested_side)
elbow_outward = horizontal_outward_offset(elbow, right_shoulder, requested_side)
wrist_v = vertical_offset(wrist, right_shoulder)
elbow_v = vertical_offset(elbow, right_shoulder)
elbow_angle = angle_at_joint(right_shoulder, elbow, wrist)
shoulder_diff = abs(left_shoulder.y - right_shoulder.y)
hip_diff = abs(left_hip.y - right_hip.y)

print('shoulder_width:', width)
print('outward:', outward)
print('required_outward (effective):', effective_reach_ratio * width)
print('wrist_vertical:', wrist_v)
print('allowed_wrist_vertical (effective):', effective_vertical_ratio * width)
print('elbow_angle:', elbow_angle)
print('elbow_angle_threshold:', elbow_angle_threshold)
print('shoulder_diff:', shoulder_diff)
print('allowed_shoulder_diff:', effective_vertical_ratio * width)

res = evaluate_side_reach(landmarks, 'right', consecutive_samples=1, lenient=True)
print('evaluate result:', res)
