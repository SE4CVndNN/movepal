"""Executable rule evaluation script for MovePal landmark fixtures (MP-021).

Evaluates the three pure heuristic movement rules (raise_both_arms,
side_reach, knee_lift_or_step) against all committed synthetic landmark
fixtures in data/landmarks/. Validates fixtures against the schema,
separates calibration/tuning cases from held-out sanity cases, and computes
confusion-style counts and performance summaries.

Usage:
    python scripts/evaluate_rules.py
"""

from __future__ import annotations

import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

# Ensure repository root is on Python path
REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from app.services.movement_rules import (
    evaluate_knee_lift,
    evaluate_raise_both_arms,
    evaluate_side_reach,
    landmarks_from_fixture,
    load_movement_fixtures,
)

SCHEMA_PATH = REPO_ROOT / "data" / "schemas" / "movement_fixture.schema.json"
FIXTURE_FILES = {
    "raise_both_arms": "raise_both_arms_fixtures.json",
    "side_reach": "side_reach_fixtures.json",
    "knee_lift_or_step": "knee_lift_fixtures.json",
}


@dataclass
class EvaluationMetrics:
    """Metrics tracking expected vs actual outcomes for a set of fixtures."""

    total: int = 0
    true_positives: int = 0
    true_negatives: int = 0
    false_positives: int = 0
    false_negatives: int = 0
    feedback_code_matches: int = 0
    low_visibility_correct: int = 0
    framing_failure_correct: int = 0

    @property
    def accuracy(self) -> float:
        if self.total == 0:
            return 0.0
        return (self.true_positives + self.true_negatives) / self.total * 100.0


def is_held_out(fixture: dict[str, Any]) -> bool:
    """Determine if a fixture belongs to the held-out sanity set."""
    fixture_id = fixture.get("fixture_id", "")
    prov = fixture.get("provenance_reference", "")
    return "heldout" in fixture_id or "held-out" in prov.lower()


def evaluate_fixture(fixture: dict[str, Any]) -> tuple[bool, str, str]:
    """Run the appropriate rule for a fixture and return (completed, feedback_code, status)."""
    movement = fixture["movement"]
    landmarks = landmarks_from_fixture(fixture)
    consecutive = fixture.get("observed_consecutive_samples", 2)
    requested_side = fixture.get("requested_side", "both")

    if movement == "raise_both_arms":
        res = evaluate_raise_both_arms(landmarks, consecutive_samples=consecutive)
    elif movement == "side_reach":
        res = evaluate_side_reach(
            landmarks, requested_side, consecutive_samples=consecutive
        )
    elif movement == "knee_lift_or_step":
        res = evaluate_knee_lift(
            landmarks, requested_side, consecutive_samples=consecutive
        )
    else:
        raise ValueError(f"Unknown movement in fixture: {movement}")

    return res.completed, res.feedback_code, res.movement


def run_evaluation() -> bool:
    """Run full evaluation across all fixture files and print structured results."""
    print("=" * 80)
    print(" MovePal MP-021 Prototype Heuristic Rule Evaluation Report")
    print(" Note: Prototype heuristic evaluation on synthetic fixtures, NOT model validation.")
    print("=" * 80)
    print()

    # Load and validate schema existence
    if not SCHEMA_PATH.is_file():
        print(f"ERROR: Schema not found at {SCHEMA_PATH}")
        return False

    all_passed = True
    overall_tuning = EvaluationMetrics()
    overall_heldout = EvaluationMetrics()

    for movement_name, filename in FIXTURE_FILES.items():
        fixtures = load_movement_fixtures(filename)
        tuning_metrics = EvaluationMetrics()
        heldout_metrics = EvaluationMetrics()

        print(f"--- Movement: {movement_name} ({filename}, Total: {len(fixtures)}) ---")

        for fixture in fixtures:
            expected_comp = fixture["expected_completed"]
            expected_fb = fixture["expected_feedback_code"]
            category = fixture["category"]
            held_out = is_held_out(fixture)

            actual_comp, actual_fb, _ = evaluate_fixture(fixture)

            metrics = heldout_metrics if held_out else tuning_metrics
            metrics.total += 1

            comp_match = actual_comp == expected_comp
            fb_match = actual_fb == expected_fb

            if comp_match:
                if expected_comp:
                    metrics.true_positives += 1
                else:
                    metrics.true_negatives += 1
            else:
                if actual_comp and not expected_comp:
                    metrics.false_positives += 1
                else:
                    metrics.false_negatives += 1

            if fb_match:
                metrics.feedback_code_matches += 1

            if category == "low_visibility" and fb_match:
                metrics.low_visibility_correct += 1

            if expected_fb == "full_body_missing" and fb_match:
                metrics.framing_failure_correct += 1

            status_str = "PASS" if (comp_match and fb_match) else "FAIL"
            if not (comp_match and fb_match):
                all_passed = False

            split_label = "Held-Out" if held_out else "Tuning  "
            print(
                f"  [{status_str}] [{split_label}] {fixture['fixture_id']:<50} "
                f"Exp: comp={expected_comp}, fb={expected_fb:<18} | "
                f"Act: comp={actual_comp}, fb={actual_fb:<18}"
            )

        # Aggregate overall
        overall_tuning.total += tuning_metrics.total
        overall_tuning.true_positives += tuning_metrics.true_positives
        overall_tuning.true_negatives += tuning_metrics.true_negatives
        overall_tuning.false_positives += tuning_metrics.false_positives
        overall_tuning.false_negatives += tuning_metrics.false_negatives
        overall_tuning.feedback_code_matches += tuning_metrics.feedback_code_matches
        overall_tuning.low_visibility_correct += tuning_metrics.low_visibility_correct
        overall_tuning.framing_failure_correct += tuning_metrics.framing_failure_correct

        overall_heldout.total += heldout_metrics.total
        overall_heldout.true_positives += heldout_metrics.true_positives
        overall_heldout.true_negatives += heldout_metrics.true_negatives
        overall_heldout.false_positives += heldout_metrics.false_positives
        overall_heldout.false_negatives += heldout_metrics.false_negatives
        overall_heldout.feedback_code_matches += heldout_metrics.feedback_code_matches
        overall_heldout.low_visibility_correct += heldout_metrics.low_visibility_correct
        overall_heldout.framing_failure_correct += heldout_metrics.framing_failure_correct

        print()
        print(f"  Tuning Set Metrics  : Accuracy={tuning_metrics.accuracy:.1f}% "
              f"(TP={tuning_metrics.true_positives}, TN={tuning_metrics.true_negatives}, "
              f"FP={tuning_metrics.false_positives}, FN={tuning_metrics.false_negatives}, "
              f"FB Match={tuning_metrics.feedback_code_matches}/{tuning_metrics.total})")
        print(f"  Held-Out Set Metrics: Accuracy={heldout_metrics.accuracy:.1f}% "
              f"(TP={heldout_metrics.true_positives}, TN={heldout_metrics.true_negatives}, "
              f"FP={heldout_metrics.false_positives}, FN={heldout_metrics.false_negatives}, "
              f"FB Match={heldout_metrics.feedback_code_matches}/{heldout_metrics.total})")
        print()

    print("=" * 80)
    print(" OVERALL EVALUATION SUMMARY")
    print("=" * 80)
    print(f" Tuning Set Total     : {overall_tuning.total}")
    print(f" Tuning Accuracy        : {overall_tuning.accuracy:.1f}%")
    print(f" Tuning FB Code Match   : {overall_tuning.feedback_code_matches}/{overall_tuning.total}")
    print(f" Held-Out Set Total    : {overall_heldout.total}")
    print(f" Held-Out Accuracy     : {overall_heldout.accuracy:.1f}%")
    print(f" Held-Out FB Code Match: {overall_heldout.feedback_code_matches}/{overall_heldout.total}")
    print(f" All Fixtures Passed   : {all_passed}")
    print("=" * 80)

    return all_passed


if __name__ == "__main__":
    success = run_evaluation()
    sys.exit(0 if success else 1)
