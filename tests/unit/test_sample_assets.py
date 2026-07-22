from pathlib import Path

EXPECTED_SAMPLES = {
    "sample_raise_both_arms.png",
    "sample_side_reach.png",
    "sample_knee_lift.png",
}


def test_fallback_sample_images_exist():
    samples_dir = Path(__file__).parents[2] / "data" / "samples"
    existing = {path.name for path in samples_dir.glob("*.png")}
    assert EXPECTED_SAMPLES <= existing
