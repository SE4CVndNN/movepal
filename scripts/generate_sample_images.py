from pathlib import Path

from PIL import Image, ImageDraw

BG = (254, 246, 230)
LIMB = (58, 155, 168)
JOINT = (245, 130, 174)
HEAD = (245, 130, 174)
FACE = (23, 32, 51)
LABEL = (23, 32, 51)

SCALE = 4
WIDTH = 320
HEIGHT = 360
JOINT_R = 8 * SCALE
LIMB_W = 10 * SCALE

POSES = {
    "sample_raise_both_arms.png": {
        "label": "Raise Both Arms",
        "head": (160, 55),
        "shoulders": [(120, 110), (200, 110)],
        "elbows": [(95, 60), (225, 60)],
        "wrists": [(80, 15), (240, 15)],
        "hips": [(135, 200), (185, 200)],
        "knees": [(130, 255), (190, 255)],
        "ankles": [(125, 305), (195, 305)],
    },
    "sample_side_reach.png": {
        "label": "Side Reach",
        "head": (160, 55),
        "shoulders": [(120, 110), (200, 110)],
        "elbows": [(60, 110), (207, 150)],
        "wrists": [(10, 110), (212, 190)],
        "hips": [(135, 200), (185, 200)],
        "knees": [(130, 255), (190, 255)],
        "ankles": [(125, 305), (195, 305)],
    },
    "sample_knee_lift.png": {
        "label": "Knee Lift",
        "head": (160, 55),
        "shoulders": [(120, 110), (200, 110)],
        "elbows": [(95, 150), (215, 150)],
        "wrists": [(85, 185), (225, 185)],
        "hips": [(135, 200), (185, 200)],
        "knees": [(150, 220), (190, 255)],
        "ankles": [(165, 260), (195, 305)],
    },
}


def scaled(point):
    return (point[0] * SCALE, point[1] * SCALE)


def draw_limb(draw, a, b):
    draw.line([scaled(a), scaled(b)], fill=LIMB, width=LIMB_W)


def draw_joint(draw, point):
    x, y = scaled(point)
    draw.ellipse((x - JOINT_R, y - JOINT_R, x + JOINT_R, y + JOINT_R), fill=JOINT)


def draw_pose(pose):
    img = Image.new("RGB", (WIDTH * SCALE, HEIGHT * SCALE), BG)
    draw = ImageDraw.Draw(img)

    left_shoulder, right_shoulder = pose["shoulders"]
    neck_bottom = ((left_shoulder[0] + right_shoulder[0]) / 2, left_shoulder[1])
    draw_limb(draw, left_shoulder, right_shoulder)
    draw_limb(draw, pose["head"], neck_bottom)

    for shoulder, elbow, wrist in zip(
        pose["shoulders"], pose["elbows"], pose["wrists"], strict=True
    ):
        draw_limb(draw, shoulder, elbow)
        draw_limb(draw, elbow, wrist)
        draw_joint(draw, elbow)
        draw_joint(draw, wrist)
        draw_joint(draw, shoulder)

    left_hip, right_hip = pose["hips"]
    hip_center = ((left_hip[0] + right_hip[0]) / 2, left_hip[1])
    draw_limb(draw, left_hip, right_hip)
    draw_limb(draw, neck_bottom, hip_center)

    for hip, knee, ankle in zip(
        pose["hips"], pose["knees"], pose["ankles"], strict=True
    ):
        draw_limb(draw, hip, knee)
        draw_limb(draw, knee, ankle)
        draw_joint(draw, hip)
        draw_joint(draw, knee)
        draw_joint(draw, ankle)

    head_x, head_y = scaled(pose["head"])
    head_r = 26 * SCALE
    draw.ellipse(
        (head_x - head_r, head_y - head_r, head_x + head_r, head_y + head_r),
        fill=HEAD,
    )
    eye_r = 4 * SCALE
    draw.ellipse(
        (
            head_x - 12 * SCALE - eye_r,
            head_y - eye_r,
            head_x - 12 * SCALE + eye_r,
            head_y + eye_r,
        ),
        fill=FACE,
    )
    draw.ellipse(
        (
            head_x + 12 * SCALE - eye_r,
            head_y - eye_r,
            head_x + 12 * SCALE + eye_r,
            head_y + eye_r,
        ),
        fill=FACE,
    )
    draw.arc(
        (
            head_x - 14 * SCALE,
            head_y - 4 * SCALE,
            head_x + 14 * SCALE,
            head_y + 18 * SCALE,
        ),
        start=20,
        end=160,
        fill=FACE,
        width=int(3 * SCALE),
    )

    img = img.resize((WIDTH, HEIGHT), Image.LANCZOS)
    return img


if __name__ == "__main__":
    out_dir = Path(__file__).resolve().parent.parent / "data" / "samples"
    out_dir.mkdir(parents=True, exist_ok=True)
    for filename, pose in POSES.items():
        draw_pose(pose).save(out_dir / filename)
        print(f"wrote {filename}")
