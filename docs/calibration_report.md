# MovePal Prototype Heuristic Rule Calibration and Evaluation Report

> [!NOTE]
> This document represents a **prototype heuristic evaluation** of deterministic game rules against synthetic landmark fixtures. It is **not** a clinical assessment or a validated model performance validation.

This report summarizes the performance, thresholds, and edge-case evaluations of the three core game movement rules in MovePal: **Raise Both Arms**, **Side Reach**, and **Knee Lift**.

---

## 1. Methodology & Data Splits

To ensure a robust and transparent evaluation, we compiled a total of **34 versioned, anonymized synthetic landmark fixtures**. These fixtures are split into a **Tuning Set** (used to calibrate rule thresholds) and a **Held-Out Sanity Set** (used to verify that threshold adjustments generalize well without overfitting).

*   **Total Fixtures:** 34
    *   **Tuning Set:** 17 fixtures
    *   **Held-Out Set:** 17 fixtures
*   **Fixture Categories:** Each movement contains positive (success), negative (incorrect execution), borderline, and low-visibility/framing failure cases.

---

## 2. Overall Evaluation Metrics

Below is the summary of the rule evaluations executed via the parameterized tests and the evaluation script:

| Movement | Dataset Split | Total | Accuracy | True Positives (TP) | True Negatives (TN) | False Positives (FP) | False Negatives (FN) | Feedback Code Match |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Raise Both Arms** | Tuning | 5 | 100.0% | 1 | 4 | 0 | 0 | 5/5 |
| | Held-Out | 5 | 100.0% | 3 | 2 | 0 | 0 | 5/5 |
| **Side Reach** | Tuning | 6 | 100.0% | 2 | 4 | 0 | 0 | 6/6 |
| | Held-Out | 6 | 100.0% | 3 | 3 | 0 | 0 | 6/6 |
| **Knee Lift / Step** | Tuning | 6 | 100.0% | 2 | 4 | 0 | 0 | 6/6 |
| | Held-Out | 6 | 100.0% | 3 | 3 | 0 | 0 | 6/6 |
| **TOTAL** | **Combined** | **34** | **100.0%** | **12** | **22** | **0** | **0** | **34/34** |

---

## 3. Movement-Specific Threshold Calibration

### A. Raise Both Arms
*   **Configured Thresholds:**
    *   `vertical_margin_ratio` = `0.40` (Each wrist must clear at least 40% of the shoulder width above its corresponding shoulder).
    *   `minimum_visibility` = `0.50` (Cutoff for key joints: shoulders, wrists, hips).
    *   `required_consecutive_samples` = `2`.
*   **Evaluation Highlights:**
    *   **Borderline Handling:** `synthetic_raise_arms_borderline_001` (below the 0.40 height margin) correctly triggers a corrective `raise_arms` feedback.
    *   **Low-Visibility / Framing:** Correctly flags `full_body_missing` when required shoulder or hip landmarks fall below `0.50` visibility.

### B. Side Reach
*   **Configured Thresholds:**
    *   `reach_ratio` = `0.85` (Wrist must extend outward beyond shoulder by at least 85% of shoulder width).
    *   `vertical_ratio` = `0.50` (Wrist must not drift vertically above the shoulder by more than 50% of shoulder width during a pure side reach).
    *   `minimum_visibility` = `0.50`.
*   **Evaluation Highlights:**
    *   **Vertical Drift:** `synthetic_side_reach_heldout_left_vertical_drift_001` was correctly flagged with `reach_left` corrective feedback instead of success because the vertical deviation exceeded the 50% margin.
    *   **Wrong Arm:** Moving the wrong arm (e.g. right arm when left side was requested) is successfully captured as a negative case.

### C. Knee Lift
*   **Configured Thresholds:**
    *   `lift_ratio` = `0.35` (Knee must clear the hip height by 35% of the hip-to-ankle leg scale).
    *   `minimum_visibility` = `0.50`.
*   **Evaluation Highlights:**
    *   **Wrong Leg:** `synthetic_knee_lift_heldout_left_wrong_leg_001` correctly returns `lift_knee` indicating the movement is incomplete.
    *   **Zero Leg Scale:** A framing failure where the distance between hips and shoulders approaches zero (`synthetic_knee_lift_heldout_left_zero_leg_scale_001`) correctly falls back to `full_body_missing` to avoid division-by-zero errors.

---

## 4. Edge Cases & False Positives/Negatives Analysis

*   **Low-Visibility & Occlusions:** Both the tuning and held-out subsets contain examples where visibility of key body parts is simulated as poor (`visibility < 0.5`). In all instances, the rules successfully prioritized safety and feedback, returning `full_body_missing` rather than incorrectly reporting a completion or incorrect movement.
*   **Framing & Positioning:** Extreme cases where the user is too close (resulting in missing ankles/knees for Knee Lift) or offset to the side are correctly mapped to framing failures rather than coaching instructions.
