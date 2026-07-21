"""Friendly, non-medical feedback messages.

Wording for ``great``, ``raise_arms``, ``hold``, and ``full_body_missing``
must match the approved wording table in docs/movement_specification.md
section 12 ("Result and friendly-feedback mapping"). MP-017 should add the
new side/knee code mappings (``reach_left``, ``reach_right``,
``lift_knee``) without changing the meaning of the codes already here.
"""

FEEDBACK_MESSAGES = {
    "great": "Awesome job! You've earned ⭐ 1 Star!",
    "raise_arms": "Please adjust your pose slightly.",
    "move_back": "Move slightly farther from the camera.",
    "hold": "Please hold a bit longer for better validation.",
    "full_body_missing": (
        "We lost track of you! Please step back so your full body is "
        "visible in the frame."
    ),
    "try_again": "Try again.",
}
