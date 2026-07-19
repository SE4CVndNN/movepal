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

### Confirmed convention (MP-005 spike)

`app/services/pose_tracking.py` implements and tests this convention; see [`docs/adr/002-pose-estimator.md`](adr/002-pose-estimator.md) for the full compatibility investigation.

- Supported landmark names: `left_shoulder`, `right_shoulder`, `left_elbow`, `right_elbow`, `left_wrist`, `right_wrist`, `left_hip`, `right_hip`, `left_knee`, `right_knee`, `left_ankle`, `right_ankle` (`TRACKED_LANDMARK_NAMES`).
- `x`, `y` are normalized to `[0, 1]` from the top-left of the raw (unmirrored) frame; `y` increases downward, so a raised wrist has a *smaller* `y` than the shoulder. `z` is roughly hip-relative depth on a similar scale; Sprint 1 rules do not depend on it.
- `left_*` / `right_*` refer to the subject's anatomical side in that raw frame, matching the pose provider's own convention. A mirrored ("selfie") preview must stay a display-only concern in the frontend; the frame sent for processing must not be flipped, or the anatomical labels would swap.
- A missing landmark is simply absent from the result's `landmarks` dict — callers must not assume every name is present; checking that a specific movement's required landmarks are present is the movement rule's job, not the pose service's.
- Provider confidence maps directly to project `visibility` (`0.0`-`1.0`, unmodified).

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
