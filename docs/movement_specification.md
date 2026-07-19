# MovePal Movement Specification

## 1. Purpose

This document defines how Sprint 1 movements should be specified, implemented, tested, reviewed, and explained. The rules are transparent game heuristics. They are not clinical assessments and must not be described as medically correct movement criteria.

The implementation owner must update this document when a coordinate convention, required landmark, threshold, feedback condition, or fixture expectation changes.

## 2. Project landmark representation

Movement rules should consume a project-level representation rather than provider-specific objects:

```python
@dataclass(frozen=True)
class Landmark:
    name: str
    x: float
    y: float
    z: float
    visibility: float
```

The pose service must document and test:

- the supported landmark names;
- normalized coordinate ranges;
- axis direction;
- whether left/right names refer to the user’s anatomical side;
- how a mirrored camera preview affects display but not rule meaning;
- how missing landmarks are represented;
- how provider confidence becomes project `visibility`.

The agreed convention must be encoded in fixtures so that frontend labels, pose output, and movement rules cannot silently disagree.

## 3. Common evaluation order

Rules should evaluate conditions in this order:

1. **Input validity:** Is there a decodable frame or fixture?
2. **Person/pose availability:** Is a usable pose available?
3. **Required landmarks:** Are the required landmark names present?
4. **Visibility:** Do required landmarks meet the configured threshold?
5. **Framing:** Is enough of the body visible for this movement?
6. **Movement conditions:** Do relative positions or angles satisfy the rule?
7. **Hold/stability:** If required, is the condition stable for the agreed sample count/time?
8. **Result:** Return success, corrective feedback, framing feedback, or unable-to-evaluate.

Do not report “try harder” when the actual problem is missing input, poor visibility, or camera framing.

## 4. Threshold policy

Thresholds must:

- be named constants or configuration values;
- use normalized/relative measurements when possible;
- have a documented initial rationale;
- be tested with positive, negative, borderline, and missing-data fixtures;
- be adjusted only with recorded evaluation evidence;
- remain game heuristics, not medical ranges.

A starting visibility threshold such as `0.5` may be used during the spike, but the final value must be justified in MP-021 and should not be copied blindly across every landmark or movement.

## 5. Common result contract

A movement rule should return a structured result such as:

```python
@dataclass(frozen=True)
class MovementResult:
    movement: str
    completed: bool
    confidence: float
    feedback_code: str
```

The implementation may add fields such as `visibility_ok`, `requested_side`, or debug measurements, provided the API and tests are updated consistently.

Suggested feedback precedence:

1. invalid input;
2. no pose/person;
3. required landmark missing;
4. low visibility/full body missing;
5. move closer/farther or reposition;
6. movement-specific correction;
7. hold;
8. success.

## 6. Movement 1: Raise both arms

### User-facing goal

Raise both arms above the shoulders so the game can recognize the pose.

### Minimum required landmarks

- left shoulder;
- right shoulder;
- left elbow;
- right elbow;
- left wrist;
- right wrist;
- torso reference such as hips when needed for scale/framing.

### Provisional logical rule

A successful frame should require both arms to satisfy the same documented relationship. A practical first rule may use:

- each wrist clearly above its corresponding shoulder in the normalized image coordinate system;
- elbows not indicating that the arms remain down;
- sufficient left/right shoulder and wrist visibility;
- enough torso visibility to reject a severely cropped pose.

Use configurable margins rather than equality. Example pseudocode:

```text
left_raised  = left_wrist.y  < left_shoulder.y  - vertical_margin
right_raised = right_wrist.y < right_shoulder.y - vertical_margin
completed = left_raised AND right_raised
```

The actual axis direction and margin must match the verified pose-service convention.

### Feedback examples

- both conditions met → `great`
- one/both wrists close but below threshold → `raise_arms`
- wrists/shoulders not visible → `full_body_missing` or a more precise visibility code
- pose visible but unstable when hold is required → `hold`

### Required fixtures

- clear success;
- both arms down;
- only left arm raised;
- only right arm raised;
- borderline wrist height;
- wrist missing;
- shoulder low visibility;
- mirrored-display case that preserves anatomical meaning.

## 7. Movement 2: Side reach, left and right

### User-facing goal

Reach one arm toward the requested side while remaining visible to the camera.

### Required landmarks

At minimum for the requested side:

- shoulder;
- elbow;
- wrist;
- torso reference landmarks.

The opposite shoulder may be needed to establish body width and horizontal scale.

### Left/right convention

The requested side refers to the user’s anatomical side, not the left side of the viewer’s screen. If the camera preview is mirrored, the UI must make this understandable while backend rules keep the anatomical convention.

### Provisional logical rule

A side reach may combine:

- horizontal wrist displacement from the corresponding shoulder;
- elbow extension or wrist-to-shoulder distance;
- wrist within an acceptable vertical band relative to the shoulder;
- required torso/shoulder visibility;
- requested-side match.

Example relative measurement:

```text
body_scale = distance(left_shoulder, right_shoulder)
reach_ratio = horizontal_distance(wrist, shoulder) / body_scale
completed = reach_ratio >= configured_reach_ratio
```

Guard against zero or unreliable body scale.

### Feedback examples

- requested side reaches threshold → `great`
- wrong side extended → side-specific correction
- correct side started but not far enough → “Reach a little farther to your left/right.”
- landmarks missing/low visibility → framing feedback
- vertical position too high/low if the specification requires a band → neutral correction

### Required fixtures

For both left and right:

- clear success;
- insufficient reach;
- wrong side;
- arm down;
- borderline reach ratio;
- elbow/wrist missing;
- shoulder-width unavailable;
- mirrored-preview contract test.

## 8. Movement 3: Knee lift or step in place

### User-facing goal

Lift one knee or make a visible step-in-place movement while the required lower-body landmarks remain in frame.

### Required landmarks

For at least one side:

- hip;
- knee;
- ankle;
- a stable torso/hip reference;
- optionally the opposite leg for relative comparison.

### Provisional logical rule

The final rule depends on whether Sprint 1 evaluates a single frame or a short sequence.

A single-frame knee-lift rule may use:

- knee position raised relative to a standing baseline or hip-to-ankle scale;
- sufficient hip, knee, and ankle visibility;
- the other leg or torso as a reference;
- a minimum change/displacement margin.

A short-sequence step rule may compare the same landmark across sampled frames. Do not claim to recognize a dynamic step from one ambiguous still image without documenting that limitation.

### Example procedure: left or right knee lift

1. The game selects and displays an anatomical side: `left` or `right`.
2. The player stands where the selected hip, knee, ankle, opposite hip, and opposite ankle remain visible. A mirrored preview may reverse the display, but it does not change the selected anatomical side.
3. The player lifts the selected knee while keeping the other leg available as a reference.
4. For each sampled pose, the rule checks visibility first, then compares the selected knee's vertical position with that side's hip-to-ankle scale:

   ```text
   leg_scale = distance(selected_hip, selected_ankle)
   knee_lifted = selected_knee.y <= selected_hip.y + 0.35 * leg_scale
   ```

5. When `knee_lifted` is true for two consecutive evaluated samples, return `great`. If it is true for fewer than two samples, return `hold`. If the selected knee is not raised enough, return `lift_knee`; missing or low-visibility required landmarks return `full_body_missing` before any movement correction.

For example, in a left-knee fixture with `left_hip.y = 0.50` and `distance(left_hip, left_ankle) = 0.20`, the initial cutoff is `0.57`. A `left_knee.y` of `0.56` passes; `0.58` retries. This is a configurable prototype heuristic, not a measure of movement quality or safety.

### Feedback examples

- clear knee-lift condition → `great`
- knee visible but below threshold → “Lift your knee a little higher.”
- feet/legs outside the frame → `full_body_missing` or lower-body framing feedback
- low visibility → “I cannot see your leg clearly.”
- transient condition not held/sampled enough → `hold`

### Required fixtures

- left knee success;
- right knee success;
- both feet/legs neutral;
- borderline lift;
- lower body cropped;
- hip/knee/ankle low visibility;
- ambiguous single-frame step;
- sequence fixture if the final rule uses temporal information.

## 9. Fixture schema expectations

Each fixture should document:

- stable fixture ID;
- movement code;
- requested side, if applicable;
- landmark coordinates and visibility;
- expected completion result;
- expected feedback code;
- category: positive, negative, borderline, missing, low visibility, or framing failure;
- provenance: synthetic, hand-authored, licensed, or consented adult-derived;
- reviewer and review date/version.

See [`annotation_guide.md`](annotation_guide.md) and [`dataset_card.md`](dataset_card.md).

## 10. Test expectations

Each movement implementation needs:

- unit tests for each fixture category;
- threshold-boundary tests;
- missing-landmark tests;
- low-visibility tests;
- left/right convention tests where applicable;
- one API/integration test using the stable JSON contract;
- evidence that changing one movement does not break the others.

Use approximate comparisons for floating-point values and keep rule tests independent from Flask and the physical pose model.

## 11. Review checklist

A reviewer should confirm:

- [ ] Rule input matches the documented landmark contract.
- [ ] Anatomical left/right is unambiguous.
- [ ] Thresholds are named and configurable.
- [ ] Visibility and framing are checked before movement correction.
- [ ] Positive, negative, borderline, and missing fixtures exist.
- [ ] Feedback is friendly and non-medical.
- [ ] Tests do not use a real camera.
- [ ] Limitations are documented.
- [ ] No claim of medical correctness is made.

## 12. MP-007 executable acceptance matrix

The checked-in synthetic fixture set is split by activity: [`raise_both_arms_fixtures.json`](../data/landmarks/raise_both_arms_fixtures.json), [`side_reach_fixtures.json`](../data/landmarks/side_reach_fixtures.json), and [`knee_lift_fixtures.json`](../data/landmarks/knee_lift_fixtures.json). Each is an MP-005-compatible JSON array with success, failure, borderline, and low-visibility cases. Every fixture has MP-005's `fixture_id`, source/provenance, `description`, `expected_status`, `annotator`, and a name-keyed `landmarks` object, with MP-007 movement outcome fields added. Its loadable contract is [`data/schemas/landmark_fixture.schema.json`](../data/schemas/landmark_fixture.schema.json). These values are initial, configurable game heuristics for deterministic tests only; they are not clinical measures and must be rechecked after the MP-005 pose-adapter decision and adult-only MP-021 calibration.

| Activity | Start / visibility prerequisites | Progress measurement | Success and hold | Retry outcome |
|---|---|---|---|---|
| Raise both arms | Both shoulders, wrists, elbows, and hips present; visibility >= 0.50 | Each wrist is at least `0.40 * shoulder_width` above its matching shoulder (`y` decreases upward) | Both conditions true for 2 consecutive evaluated samples | `raise_arms`; visibility/framing failure takes precedence |
| Side reach — left | Both shoulders, left elbow/wrist, and hips present; visibility >= 0.50 | Left wrist is outward by >= `0.85 * shoulder_width`; its vertical offset is <= `0.50 * shoulder_width` | Condition true for 2 consecutive samples | `reach_left`; a right-arm reach does not satisfy the request |
| Side reach — right | Both shoulders, right elbow/wrist, and hips present; visibility >= 0.50 | Right wrist is outward by >= `0.85 * shoulder_width`; its vertical offset is <= `0.50 * shoulder_width` | Condition true for 2 consecutive samples | `reach_right`; a left-arm reach does not satisfy the request |
| Knee lift / step — requested side | Target hip, knee, ankle, opposite hip, and opposite ankle present; visibility >= 0.50 | `knee.y <= hip.y + 0.35 * distance(hip, ankle)` | Condition true for 2 consecutive samples | `lift_knee`; a still frame cannot independently prove a dynamic step |

`shoulder_width` is Euclidean distance between anatomical left and right shoulders. A zero or unavailable scale is a framing failure. The pose adapter must preserve the fixture convention: `x` grows toward the viewer's right, `y` grows downward, and `left`/`right` always mean the user's anatomical side. Mirroring changes only the preview, never the rule input or requested side.

### Result and friendly-feedback mapping

Rules must use this precedence: missing/low-visibility required landmark or unusable scale → `full_body_missing`; insufficient consecutive samples after a valid condition → `hold`; otherwise the activity-specific retry code; success → `great`.

| Code | Approved wording source |
|---|---|
| `great` | “Awesome job! You've earned ⭐ 1 Star!” |
| `raise_arms`, `reach_left`, `reach_right`, `lift_knee` | “Please adjust your pose slightly.” |
| `hold` | “Please hold a bit longer for better validation.” |
| `full_body_missing` | “We lost track of you! Please step back so your full body is visible in the frame.” |

The wording is intentionally centralized in `feedback.py`; MP-017 should add the new side/knee code mappings without changing their meanings.

### Evaluation plan

| Evaluation stage | Data | Pass criterion | Limitation |
|---|---|---|---|
| Schema regression | All checked-in synthetic fixtures | Fixture load and structural validation pass in CI | Valid JSON does not prove pose accuracy |
| Rule regression | Positive, borderline, negative, and low-visibility fixtures per family | Returned `completed` and feedback code equal fixture expectation | Synthetic geometry is not representative calibration |
| Boundary checks | Values immediately below, at, and above each threshold | Inclusive/exclusive comparison matches this table | Floating-point tolerance must be explicit in rule tests |
| Adult-only calibration (MP-021) | Consent-approved derived landmarks, separate from held-out fixtures | Record per-movement counts and all mismatches before changing thresholds | Small convenience sample cannot establish general accuracy |
| Manual mirrored-preview check | Left/right synthetic fixtures and UI labels | Backend anatomical-side result is unchanged by mirror setting | Does not replace usability study |

Side-specific fixtures use `requested_side: "left"` or `requested_side: "right"` for both side reach and knee lift; they are never represented by a generic side case. Open limitations: no dynamic sequence fixture is included because the Sprint-1 rule is a two-sample knee-lift hold, not a claim that a single frame recognizes a step. Fixture labels are pending independent review; do not promote them to calibrated evidence until that review and MP-005/MP-006 dependency recheck are complete.
