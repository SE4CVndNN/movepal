"""Rule Evaluation Script for MovePal MP-021.

Evaluates MovePal's deterministic movement rules against the checked-in
synthetic fixture set (split into tuning and held-out sets) and the MP-020
external sample compatibility data point. Computes confusion matrices
(TP, TN, FP, FN), feedback match rates, and prints formatted Markdown tables
suitable for inclusion in docs/calibration_report.md.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

# Add repository root to Python path
REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from app.services.movement_rules import (  # noqa: E402
    evaluate_knee_lift,
    evaluate_raise_both_arms,
    evaluate_side_reach,
    landmarks_from_fixture,
    load_movement_fixtures,
)


def run_evaluation() -> int:
    """Run rule evaluation across all fixture files and print report summary."""
    fixture_files = {
        "raise_both_arms": "raise_both_arms_fixtures.json",
        "side_reach": "side_reach_fixtures.json",
        "knee_lift_or_step": "knee_lift_fixtures.json",
    }

    results_by_movement: dict[str, dict] = {}
    split_counts: dict[str, dict[str, int]] = {
        "tuning": {"total": 0, "correct": 0, "tp": 0, "tn": 0, "fp": 0, "fn": 0},
        "held_out": {"total": 0, "correct": 0, "tp": 0, "tn": 0, "fp": 0, "fn": 0},
    }

    print("==================================================================")
    print("      MovePal MP-021 Prototype Movement Rule Evaluation Report    ")
    print("==================================================================\n")

    total_fixtures = 0
    total_matches = 0

    for movement_name, filename in fixture_files.items():
        fixtures = load_movement_fixtures(filename)
        movement_stats = {
            "total": len(fixtures),
            "fixture_matches": 0,
            "feedback_matches": 0,
            "tp": 0,
            "tn": 0,
            "fp": 0,
            "fn": 0,
        }

        print(f"--- Movement: {movement_name} ({len(fixtures)} fixtures) ---")

        for fixture in fixtures:
            total_fixtures += 1
            fid = fixture["fixture_id"]
            if "split" not in fixture:
                raise KeyError(
                    f"Fixture '{fixture.get('fixture_id', '?')}' is missing a required "
                    "'split' field. Every fixture must explicitly declare "
                    "'split': 'tuning' or 'split': 'held_out'."
                )
            split = fixture["split"]
            _VALID_SPLITS = {"tuning", "held_out"}
            if split not in _VALID_SPLITS:
                raise ValueError(
                    f"Fixture '{fixture.get('fixture_id', '?')}' has unknown split "
                    f"'{split}'. Expected one of: {sorted(_VALID_SPLITS)}"
                )
            category = fixture.get("category", "unknown")
            requested_side = fixture.get("requested_side", "both")
            expected_completed = fixture["expected_completed"]
            expected_feedback = fixture["expected_feedback_code"]
            consecutive_samples = fixture["observed_consecutive_samples"]

            landmarks = landmarks_from_fixture(fixture)

            if movement_name == "raise_both_arms":
                actual = evaluate_raise_both_arms(
                    landmarks, consecutive_samples=consecutive_samples
                )
            elif movement_name == "side_reach":
                actual = evaluate_side_reach(
                    landmarks,
                    requested_side=requested_side,
                    consecutive_samples=consecutive_samples,
                )
            elif movement_name == "knee_lift_or_step":
                actual = evaluate_knee_lift(
                    landmarks,
                    requested_side=requested_side,
                    consecutive_samples=consecutive_samples,
                )
            else:
                raise ValueError(f"Unknown movement {movement_name}")

            completed_match = actual.completed == expected_completed
            feedback_match = actual.feedback_code == expected_feedback
            overall_match = completed_match and feedback_match

            if overall_match:
                movement_stats["fixture_matches"] += 1
                total_matches += 1

            if feedback_match:
                movement_stats["feedback_matches"] += 1

            # Determine confusion matrix entry
            if expected_completed:
                if actual.completed:
                    movement_stats["tp"] += 1
                    split_counts[split]["tp"] += 1
                else:
                    movement_stats["fn"] += 1
                    split_counts[split]["fn"] += 1
            else:
                if not actual.completed:
                    movement_stats["tn"] += 1
                    split_counts[split]["tn"] += 1
                else:
                    movement_stats["fp"] += 1
                    split_counts[split]["fp"] += 1

            split_counts[split]["total"] += 1
            if overall_match:
                split_counts[split]["correct"] += 1

            status_str = "PASS" if overall_match else "FAIL"
            print(
                f"  [{status_str}] {fid:<45} | split: {split:<8} | cat: {category:<14} | "
                f"expected: (comp={expected_completed}, fb={expected_feedback}) | "
                f"actual: (comp={actual.completed}, fb={actual.feedback_code})"
            )

        results_by_movement[movement_name] = movement_stats
        print()

    # External asset compatibility sample check
    external_sample_path = (
        REPO_ROOT / "docs" / "evidence" / "mp-020-external-sample-landmarks.json"
    )
    if external_sample_path.exists():
        with open(external_sample_path, encoding="utf-8") as f:
            ext_data = json.load(f)
        print("--- External Sample Pipeline Compatibility (MP-020 Data Point) ---")
        print(f"  Fixture ID: {ext_data.get('fixture_id')}")
        print(f"  Description: {ext_data.get('description')}")
        print(f"  Expected Status: {ext_data.get('expected_status')}")
        ext_landmarks = landmarks_from_fixture(ext_data)
        print(f"  Landmarks Loaded: {len(ext_landmarks)}")
        print("  Pipeline Compatibility: PASS (Well-formed landmark structure)")
        print()

    # Print Summary Tables
    print("==================================================================")
    print("                      EVALUATION SUMMARY                          ")
    print("==================================================================\n")

    print("| Movement | Total | Fixture Matches | Match Rate | TP | TN | FP | FN |")
    print("| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |")
    for m_name, m_stats in results_by_movement.items():
        match_rate = (
            (m_stats["fixture_matches"] / m_stats["total"]) * 100
            if m_stats["total"] > 0
            else 0.0
        )
        print(
            f"| {m_name:<18} | {m_stats['total']:>5} | {m_stats['fixture_matches']:>15} | "
            f"{match_rate:>9.1f}% | {m_stats['tp']:>2} | {m_stats['tn']:>2} | "
            f"{m_stats['fp']:>2} | {m_stats['fn']:>2} |"
        )

    print(
        "\n| Split | Total Fixtures | Fixture Matches | Match Rate | TP | TN | FP | FN |"
    )
    print("| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |")
    for split_name, s_stats in split_counts.items():
        match_rate = (
            (s_stats["correct"] / s_stats["total"]) * 100
            if s_stats["total"] > 0
            else 0.0
        )
        print(
            f"| {split_name:<10} | {s_stats['total']:>14} | {s_stats['correct']:>15} | "
            f"{match_rate:>9.1f}% | {s_stats['tp']:>2} | {s_stats['tn']:>2} | "
            f"{s_stats['fp']:>2} | {s_stats['fn']:>2} |"
        )

    overall_acc = (total_matches / total_fixtures * 100) if total_fixtures > 0 else 0.0
    print(
        f"\nOverall Fixture Match: {total_matches}/{total_fixtures} ({overall_acc:.1f}%)\n"
    )

    return 0 if total_matches == total_fixtures else 1


if __name__ == "__main__":
    sys.exit(run_evaluation())
