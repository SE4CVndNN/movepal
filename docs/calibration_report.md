# MovePal MP-021 — Landmark Fixtures, Threshold Calibration, and Rule Evaluation Report

> [!IMPORTANT]
> **Prototype Heuristic Boundary Disclaimer**:
> This document records a **prototype heuristic evaluation** of MovePal's rule-based movement logic on a small, deterministic synthetic fixture set and pipeline compatibility sample. This is **not a machine learning model validation** or a **clinical trial**. MovePal provides playful movement practice and is not intended for diagnosis, treatment, or rehabilitation.

---

## 1. Overview and Evaluation Objectives

The goal of task MP-021 is to establish a deterministic evaluation suite for MovePal's three movement rules, separate threshold-tuning data from held-out sanity examples, calibrate heuristic thresholds transparently, and record rule performance across positive, negative, borderline, low-visibility, and framing cases.

### Key Objectives

1. **Fixture Dataset Creation**: Build an inspectable 24-fixture synthetic dataset adhering strictly to `data/schemas/movement_fixture.schema.json`.
2. **Train/Test Separation**: Split the dataset into a **tuning set** (12 fixtures) used during initial parameter selection and a **held-out sanity set** (12 fixtures) reserved for unbiased evaluation.
3. **Parameterized Evaluation**: Implement `scripts/evaluate_rules.py` to calculate confusion matrix counts (True Positives, True Negatives, False Positives, False Negatives) and verify feedback codes.
4. **Threshold Transparency**: Document all configurable thresholds, their geometric rationale, and traceability to empirical evidence.

---

## 2. Deterministic Fixture Dataset Composition

The fixture set comprises 24 hand-authored synthetic landmark configurations split evenly across the three supported movements and evaluation splits.

### Dataset Summary Table

| Movement             |  Total | Tuning Split | Held-Out Split | Positive | Negative | Borderline | Low Visibility | Framing |
| :------------------- | -----: | -----------: | -------------: | -------: | -------: | ---------: | -------------: | ------: |
| **Raise Both Arms**  |      8 |            4 |              4 |        2 |        2 |          2 |              1 |       1 |
| **Side Reach**       |      8 |            4 |              4 |        2 |        2 |          2 |              1 |       1 |
| **Knee Lift / Step** |      8 |            4 |              4 |        2 |        2 |          2 |              1 |       1 |
| **Total**            | **24** |       **12** |         **12** |    **6** |    **6** |      **6** |          **3** |   **3** |

### Additional External Data Point (MP-020 Compatibility Sample)

- **Fixture ID**: `external_pixabay_demo_photo_001` (`docs/evidence/mp-020-external-sample-landmarks.json`)
- **Purpose**: Verifies pipeline compatibility for externally derived landmarks processed through `MediaPipePoseAdapter`.
- **Status**: 12 visible landmarks extracted, conforming to `PoseResult` contract.

---

## 3. Parameterized Rule Evaluation Results

Rules were evaluated using `scripts/evaluate_rules.py`. Every fixture was evaluated against its movement rule using observed consecutive sample counts.

### Performance by Movement

| Movement             | Total Fixtures | Correct Outcomes | Accuracy | True Positive (TP) | True Negative (TN) | False Positive (FP) | False Negative (FN) |
| :------------------- | -------------: | ---------------: | -------: | -----------------: | -----------------: | ------------------: | ------------------: |
| **Raise Both Arms**  |              8 |                8 |   100.0% |                  2 |                  6 |                   0 |                   0 |
| **Side Reach**       |              8 |                8 |   100.0% |                  2 |                  6 |                   0 |                   0 |
| **Knee Lift / Step** |              8 |                8 |   100.0% |                  2 |                  6 |                   0 |                   0 |

### Performance by Dataset Split

| Split               | Total Fixtures | Correct Outcomes |   Accuracy |    TP |     TN |    FP |    FN |
| :------------------ | -------------: | ---------------: | ---------: | ----: | -----: | ----: | ----: |
| **Tuning Split**    |             12 |               12 |     100.0% |     3 |      9 |     0 |     0 |
| **Held-Out Split**  |             12 |               12 |     100.0% |     3 |      9 |     0 |     0 |
| **Overall Dataset** |         **24** |           **24** | **100.0%** | **6** | **18** | **0** | **0** |

> [!NOTE]
> All 24 fixtures achieved 100% agreement between expected labels and actual rule outputs for both `completed` status and exact `feedback_code`.

---

## 4. Threshold Calibration & Rationale

MovePal's rules rely on normalized geometric scaling relative to user anatomical baselines (shoulder width and leg scale). Below is the traceability record for all configurable thresholds defined in `app/services/movement_rules.py`.

| Parameter Name                         | Value  | Movement        | Rationale & Traceability                                                                                                                                         |
| :------------------------------------- | :----- | :-------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `DEFAULT_MINIMUM_VISIBILITY`           | `0.50` | All             | Per-landmark MediaPipe cutoff. Landmarks with visibility `< 0.50` return `full_body_missing` to prevent false motion triggers in dim light or partial occlusion. |
| `DEFAULT_VERTICAL_MARGIN_RATIO`        | `0.40` | Raise Both Arms | Requires each wrist to be at least `0.40 * shoulder_width` vertically higher than its matching shoulder (smaller `y`).                                           |
| `DEFAULT_SIDE_BEND_RATIO`              | `0.18` | Side Reach      | Torso bend angle threshold as a fraction of body scale for standing side-bend movement.                                                                          |
| `DEFAULT_OVERHEAD_HEIGHT_RATIO`        | `0.35` | Side Reach      | Overhead arm must reach at least 35% of body height above shoulder in side-bend position.                                                                        |
| `DEFAULT_OVERHEAD_CROSS_RATIO`         | `0.20` | Side Reach      | Overhead arm must cross inward by at least 20% of shoulder width to complete the side-bend.                                                                      |
| `DEFAULT_KNEE_LIFT_RATIO`              | `0.35` | Knee Lift       | Caps the hip-to-knee vertical offset at `<= 0.35 * leg_scale` (hip-to-ankle distance), ensuring the knee is raised significantly off the ground.                 |
| `DEFAULT_REQUIRED_CONSECUTIVE_SAMPLES` | `2`    | All             | Temporal stability filter requiring the satisfying position to hold for 2 consecutive frames before triggering completion (`great`).                             |

---

## 5. Edge Cases & Documented Failure Analysis

Evaluation on edge cases highlighted key rule behaviors under improper execution and poor camera framing:

### 1. Borderline Motion Rejection

- **Raise Both Arms (`synthetic_raise_arms_borderline_001` & `002`)**: Wrists raised to shoulder height (`y = 0.40`) or just under the `0.40` margin ratio fail completion and correctly prompt `"raise_arms"`.
- **Side Reach (`synthetic_side_reach_left_borderline_001`)**: Torso bend just below the required threshold in standing side-bend position returns `completed=False` and feedback `"reach_left"`.
- **Knee Lift (`synthetic_knee_lift_right_borderline_001`)**: Knee lifted to offset `0.15` relative to leg scale `0.40` (ratio `0.375 > 0.35`) correctly returns `completed=False` and feedback `"lift_knee"`.

### 2. Framing & Partial Body Occlusion (Documented Failure Case)

- **Documented Failure Case — `synthetic_knee_lift_right_framing_001`**:
  - _Scenario_: User stands too close to the camera, cutting off the lower legs. Right ankle landmark is missing (`None`).
  - _Expected & Actual Outcome_: `completed=False`, `feedback_code="full_body_missing"`.
  - _Analysis_: Knee lift rule strictly requires `(selected_hip, selected_knee, selected_ankle, opposite_hip, opposite_ankle)`. Missing any landmark correctly yields `full_body_missing` rather than attempting uncalibrated distance math.
- **Documented Failure Case — `synthetic_side_reach_left_framing_001`**:
  - _Scenario_: User extends left arm outwards but droops wrist downward (`vertical_offset = 0.20`, ratio `0.67 > 0.50`).
  - _Expected & Actual Outcome_: `completed=False`, `feedback_code="reach_left"`.
  - _Analysis_: Wrist vertical drift filter successfully rejects improper arm positioning.

---

## 6. CI Integration and Stable Subset Selection

To maintain high developer velocity and fast CI test runs:

- All 24 fixtures are validated in CI under `tests/unit/test_movement_fixtures.py` (schema structure and metadata integrity) and `tests/unit/test_movement_rules.py` (rule outcome accuracy).
- Running `pytest` validates the entire suite in `< 1.0` second.
- `scripts/evaluate_rules.py` is included as a standalone script for detailed calibration reports.

---

## 7. Unresolved Limitations & Future Handoff

1. **Synthetic Data Focus**: The 24 main evaluation fixtures are hand-authored synthetic landmark sets. While ideal for unit testing, synthetic landmarks do not capture real-world MediaPipe jitter or lighting variations.
2. **Camera Distance Variations**: Normalization relies on shoulder width and leg scale, but extreme camera tilt or wide-angle distortion may affect calculated ratios.
3. **Future Work**: Post-MVP work should consider expanding live participant calibration across diverse age groups and camera setups.
