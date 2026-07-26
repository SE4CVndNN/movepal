import json
from app.services.movement_rules import load_side_reach_fixture
from app.services.pose_tracking import pose_result_from_fixture_data

fixture_ids = [
    "synthetic_side_reach_left_positive_001",
    "synthetic_side_reach_right_negative_001",
    "synthetic_side_reach_left_borderline_001",
    "synthetic_side_reach_right_low_visibility_001",
]

out = []
for fid in fixture_ids:
    fixture = load_side_reach_fixture(fid)
    pose = pose_result_from_fixture_data(fixture)
    raw = fixture.get('landmarks', {})
    landmarks = {k: { 'x': float(v['x']), 'y': float(v['y']), 'visibility': float(v['visibility']) } for k,v in raw.items()}
    out.append({'fixture_id': fid, 'pose_status': pose.status.value, 'landmarks': landmarks})
print(json.dumps(out, indent=2))
