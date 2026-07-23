"""Friendly, non-medical feedback messages.

Wording for ``great``, ``raise_arms``, ``reach_left``, ``reach_right``,
``hold``, and ``full_body_missing`` must match the approved wording table
in docs/movement_specification.md section 12 ("Result and
friendly-feedback mapping"). MP-015 added the ``reach_left``/
``reach_right`` entries required by ``evaluate_side_reach``; a future
knee-lift task still owes the ``lift_knee`` mapping.
"""

_MOVEMENT_CORRECTION_TEXT = "Please adjust your pose slightly."
"""Shared wording for every movement-specific correction code.

Section 12's table intentionally gives ``raise_arms``, ``reach_left``,
``reach_right``, and ``lift_knee`` the identical approved sentence -- the
distinction between movements and sides is carried by ``feedback_code``,
not by different wording, so it is defined once here rather than repeated
per key (and risking the two sides drifting apart).
"""

FEEDBACK_MESSAGES = {
    "great": "Awesome job! You've earned ⭐ 1 Star!",
    "raise_arms": _MOVEMENT_CORRECTION_TEXT,
    "reach_left": _MOVEMENT_CORRECTION_TEXT,
    "reach_right": _MOVEMENT_CORRECTION_TEXT,
    "move_back": "Move slightly farther from the camera.",
    "hold": "Please hold a bit longer for better validation.",
    "full_body_missing": (
        "We lost track of you! Please step back so your full body is "
        "visible in the frame."
    ),
    "try_again": "Try again.",
}
