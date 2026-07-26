import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.services.pose_tracking import MediaPipePoseAdapter, PoseStatus
from app.services.movement_rules import evaluate_side_reach
from app.services.geometry import (
    side_landmark_name,
    horizontal_outward_offset,
    vertical_offset,
    angle_at_joint,
    shoulder_width,
    opposite_side,
)

img = Path('app/static/images/avatars/reach-to-the-left.png')
adapter = MediaPipePoseAdapter(model_path=Path('pose_landmarker_lite.task'))
pose = adapter.estimate(img)
print('pose status:', pose.status)
landmarks = pose.landmarks

requested_side = 'left'
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

outward = horizontal_outward_offset(wrist, left_shoulder, requested_side)
elbow_outward = horizontal_outward_offset(elbow, left_shoulder, requested_side)
wrist_height_ok = vertical_offset(wrist, left_shoulder) <= 0.5 * width
elbow_height_ok = vertical_offset(elbow, left_shoulder) <= 0.5 * width
elbow_angle = angle_at_joint(left_shoulder, elbow, wrist)
shoulder_level_ok = abs(left_shoulder.y - right_shoulder.y) <= 0.5 * width
hip_level_ok = abs(left_hip.y - right_hip.y) <= 0.5 * width
elbow_in_line = elbow_outward >= 0 and outward >= elbow_outward
opposite_arm_relaxed = (opp_wr.y >= opp_el.y) and (opp_el.y >= right_shoulder.y)

print('shoulder_width:', width)
print('outward:', outward)
print('elbow_outward:', elbow_outward)
print('wrist_height_ok:', wrist_height_ok)
print('elbow_height_ok:', elbow_height_ok)
print('elbow_angle:', elbow_angle)
print('elbow_in_line:', elbow_in_line)
print('opposite_arm_relaxed:', opposite_arm_relaxed)
print('shoulder_level_ok:', shoulder_level_ok)
print('hip_level_ok:', hip_level_ok)

res = evaluate_side_reach(landmarks, 'left', consecutive_samples=1)
print('evaluate result:', res)
