from app.services.scoring import stars_for_confidence


def test_star_thresholds():
    assert stars_for_confidence(0.90) == 3
    assert stars_for_confidence(0.70) == 2
    assert stars_for_confidence(0.50) == 1
    assert stars_for_confidence(0.20) == 0


def test_confidence_is_bounded():
    assert stars_for_confidence(5.0) == 3
    assert stars_for_confidence(-5.0) == 0
