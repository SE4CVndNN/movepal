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
- left wrist;
- right wrist;

> **MP-014 correction:** earlier drafts also required elbows and hips. The
> executable rule uses shoulder width and wrist height only; it never reads
> elbow or hip coordinates. The checked-in negative/borderline/low-visibility
> fixtures in
> [`raise_both_arms_fixtures.json`](../data/landmarks/raise_both_arms_fixtures.json)
> omit elbows entirely while still expecting a `retry`/`raise_arms` result
> rather than a missing-landmark failure. Requiring hips would also reject a
> usable upper-body camera frame even though the movement calculation does not
> need them. MP-014's implementation (`app/services/movement_rules.py`)
> therefore requires only the two shoulders and two wrists for
> `raise_both_arms`; see "MP-014 decisions" at the end of this document.

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

The checked-in synthetic fixture set is split by activity: [`raise_both_arms_fixtures.json`](../data/landmarks/raise_both_arms_fixtures.json), [`side_reach_fixtures.json`](../data/landmarks/side_reach_fixtures.json), and [`knee_lift_fixtures.json`](../data/landmarks/knee_lift_fixtures.json). Each is an MP-005-compatible JSON array with success, failure, borderline, and low-visibility cases. Every fixture has MP-005's `fixture_id`, source/provenance, `description`, `expected_status`, `annotator`, and a name-keyed `landmarks` object, with MP-007 movement outcome fields added. Its loadable contract is [`data/schemas/movement_fixture.schema.json`](../data/schemas/movement_fixture.schema.json). These values are initial, configurable game heuristics for deterministic tests only; they are not clinical measures and must be rechecked after the MP-005 pose-adapter decision and adult-only MP-021 calibration.

| Activity | Start / visibility prerequisites | Progress measurement | Success and hold | Retry outcome |
|---|---|---|---|---|
| Raise both arms | Both shoulders and wrists present; visibility >= 0.50 | Each wrist is at least `0.40 * shoulder_width` above its matching shoulder (`y` decreases upward) | Both conditions true for 2 consecutive evaluated samples | `raise_arms`; visibility/framing failure takes precedence |
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

### Fixture review mechanism

Each checked-in synthetic fixture identifies an `annotator` and carries no personal data. Before a fixture is treated as approved regression evidence, an independent reviewer must check its MP-005 metadata, landmark names and normalized ranges, anatomical side, category, expected completion, and feedback code against this specification. Record the reviewer, review date, and decision in the MP-007 pull-request review or a linked issue comment; update the fixture description or expectation when a discrepancy is found. A fixture that lacks independent review remains usable for development experiments but must not be presented as calibrated evidence.

## 13. MP-014 decisions

MP-014 built the first vertical slice (`docs/architecture.md` section 7): a deterministic `raise_both_arms` fixture travels through `POST /api/movement`, the pure rule in `app/services/movement_rules.py`, and the friendly feedback in `app/services/feedback.py`, then renders in the browser fallback path with no camera or MediaPipe model. Decisions and mismatches recorded during that work:

- **Elbow requirement removed for `raise_both_arms`.** See the correction note in section 6. Fixed in the rule, not the fixtures, since the fixtures and the acceptance-matrix formula already agreed with each other.
- **`feedback.py` wording corrected.** `great`, `raise_arms`, `hold`, and `full_body_missing` previously used older placeholder text that did not match this document's section 12 approved-wording table (the table was added by MP-007 after `feedback.py` was first written). `feedback.py` is the owning component for wording per section 12, so its strings were updated to match the table exactly; `move_back` and `try_again` are untouched, unused legacy codes and are out of scope here.
- **Hold/consecutive-sample tracking is per-request, not per-session.** `evaluate_raise_both_arms` accepts a caller-supplied `consecutive_samples` count (matching the fixtures' own `observed_consecutive_samples` field) rather than tracking state across HTTP requests itself. When a caller omits it, the rule assumes the hold requirement is already satisfied (a single satisfying sample succeeds immediately) so that a real single-frame request from a future camera path does not get stuck on `hold` forever. Real cross-request session tracking is left to MP-016; until then, only callers that explicitly pass a lower count (as the fixture-driven contract tests do) will see a `hold` result.
- **`POST /api/movement` only accepts a `fixture_id`, not a live image or raw landmark JSON**, keeping the new endpoint's input surface minimal and privacy-safe (no arbitrary body data). Composing a real camera frame's pose-adapter output with `evaluate_raise_both_arms` is straightforward (the shapes already match) and is deferred to MP-019's full game loop rather than built speculatively here.
- **`stars` now always matches the fixed "1 Star" wording.** The endpoint originally returned `scoring.stars_for_confidence(result.confidence)`, a 0–3 scale, alongside the approved `great` text which always says "1 Star" — an internal contradiction a reviewer caught. `app/services/scoring.py` now also exposes `stars_for_completion(completed)`, which the endpoint uses instead (1 on success, 0 otherwise). `stars_for_confidence` is kept for a possible future graduated-scoring feature but is no longer wired into this endpoint. The browser fallback path was also duplicating the star count by appending `"⭐".repeat(payload.stars)` after text that already contains a star and count; it now renders `payload.feedback` verbatim.
- **Unsupported activities are disabled in this vertical slice's UI, not silently ignored.** Only `raise_both_arms` has a rule and fixture wired up. A reviewer found that selecting "Reach to the side" or "Knee lift" still submitted a hardcoded `raise_both_arms` fixture. The activity buttons for those two moves are now `disabled` with a "coming soon" label in `app/templates/index.html`, and `app/static/js/app.js` tracks the selected activity and looks its fixture up in a small `SUPPORTED_FALLBACK_FIXTURES` map (defensive check, since the disabled buttons already prevent selection).
- **Rebased onto MP-011's merged base-interface work.** MP-011 added a persistent score region (`#score-region`, `totalStars`) and avatar partials that both touch `index.html`/`app.js`. The fixture-driven fallback handler now calls the existing `updateFeedbackStatus()`/`addStars()` helpers instead of setting `feedbackMessage` in isolation, so the score badge and status text stay consistent with the real evaluated result instead of drifting from MP-011's placeholder scoring flow.

## 14. MP-015 decisions

MP-015 implemented `evaluate_side_reach` for both anatomical sides (`app/services/movement_rules.py`), backed by new shared helpers in `app/services/geometry.py` and the `reach_left`/`reach_right` entries in `app/services/feedback.py`. It reuses the four `side_reach_fixtures.json` fixtures MP-007 already checked in and adds directly-constructed mirrored fixtures in `tests/unit/test_movement_rules.py` for cases the committed set does not cover. Decisions, assumptions, and limitations recorded during that work:

- **Elbow is not a required landmark for `side_reach`, matching the `raise_both_arms` precedent.** Section 7's prose lists elbow as a "required landmark," and the section 12 acceptance-matrix table still names it in the prerequisites column, but the executable progress formula only ever reads the requested side's shoulder and wrist. The checked-in `synthetic_side_reach_right_negative_001` fixture (the wrong-side case) has no elbow landmarks at all for either side and still expects `reach_right`, not `full_body_missing`; requiring elbow would fail it for the wrong reason. `evaluate_side_reach`'s required-landmark tuple therefore omits elbow, exactly as `evaluate_raise_both_arms` already does (section 6's correction note and section 13's first bullet). No fixture data changed; this is a rule-side decision only.
- **Only the requested side's own shoulder/wrist pair is ever read.** This is what makes "a right-arm reach does not satisfy a left request" (section 12) fall out of the rule automatically instead of needing a separate wrong-side branch or code: the opposite wrist is never inspected, so it cannot accidentally satisfy the request no matter how far it reaches. `test_opposite_arm_reaching_does_not_satisfy_requested_side` in `tests/unit/test_movement_rules.py` checks this in both directions.
- **Mirrored symmetry is proved by construction, not by hand-authoring duplicate JSON fixtures.** Beyond parametrizing the four already-committed `side_reach_fixtures.json` cases over their `requested_side`, `tests/unit/test_movement_rules.py` adds a `_side_reach_landmarks(side, outward_ratio, vertical_ratio)` builder that places the requested wrist using the same side-dependent sign `horizontal_outward_offset` uses internally. Calling it with `"left"` and `"right"` for identical ratios yields literal mirror images across the body midline, so `@pytest.mark.parametrize("side", ["left", "right"])` exercises full-reach, arm-down, both reach-ratio boundary sides (just below/at `0.85 * shoulder_width`), excess vertical offset, missing/low-visibility wrist, zero shoulder width, and the hold/default-consecutive-samples contract identically for both sides. A left/right asymmetry bug would show up as exactly one parametrized case failing rather than a silently-drifted duplicate test file.
- **`reach_left`/`reach_right` share `raise_arms`'s exact wording, not a distinct sentence.** Section 12's approved-wording table intentionally maps `raise_arms`, `reach_left`, `reach_right`, and `lift_knee` to the identical sentence ("Please adjust your pose slightly.") — the distinction between movements and sides is meant to be carried by `feedback_code`, not by different copy. `feedback.py` now defines that sentence once as `_MOVEMENT_CORRECTION_TEXT` and reuses it for all three keys so the two side codes cannot drift apart from each other or from `raise_arms`; `test_reach_left_and_reach_right_share_the_raise_arms_wording` guards this. The still-unmapped `lift_knee` code is left for the knee-lift task that implements that rule.
- **No wrong-side-specific feedback code was added.** The acceptance matrix and the checked-in fixtures already treat an insufficient or wrong-side reach identically (`reach_left`/`reach_right`, not a separate `wrong_side` code), so `evaluate_side_reach` does not introduce one; adding a new code here would be undocumented scope beyond section 12's table.
- **No "bent posture" signal is implemented for side reach.** MP-015's issue text mentions feedback for "bent posture where represented," but section 12's executable formula for side reach checks only wrist-to-shoulder horizontal and vertical offsets, not elbow angle — consistent with the elbow-exclusion decision above. Side reach therefore has no bent-posture representation in Sprint 1; this would need a new documented threshold and fixtures if a future task adds one.
- **`side_reach` is not wired into `POST /api/movement` or the UI.** Following the same scoping the MP-014 decisions record for `raise_both_arms`-only wiring, the "Reach to the side" button remains `disabled` ("coming soon") in `app/templates/index.html` and `SUPPORTED_MOVEMENTS` in `app/routes/api.py` still only contains `raise_both_arms`. `evaluate_side_reach` and `load_side_reach_fixture` are ready to be composed into the endpoint the same way `evaluate_raise_both_arms` already is; that composition, plus any UI side-selection control, is left to whichever task actually enables the "Reach to the side" activity (MP-019's full game loop, or an earlier dedicated wiring task if one is scheduled first).

## 15. MP-016 decisions

MP-016 implements the pure `knee_lift_or_step` rule for a requested anatomical
left or right side. It requires the selected hip, knee, and ankle plus the
opposite hip and ankle; missing or below-`0.50` visibility landmarks, and a
zero selected hip-to-ankle scale, return `full_body_missing` before geometry is
evaluated. Mirroring remains display-only. The selected knee passes when
`knee.y <= hip.y + 0.35 * distance(hip, ankle)`, with `0.35` configurable.
One satisfying sample returns `hold`, two return `great`, and an omitted count
assumes the hold is satisfied without adding cross-request state. Confidence
is the allowed hip-to-knee vertical offset divided by the observed downward
offset, capped to `[0.0, 1.0]`; satisfying poses return `1.0`, while unusable
input returns `0.0`. This deterministic value is game-rule progress only.

A frame that meets this static knee-position heuristic does not prove a
dynamic step. This remains a prototype game heuristic, not a clinical
assessment. API, UI, session, scoring, and full-game integration are outside
MP-016.

## 16. MP-017 decisions

MP-017 implements the game-level feedback orchestration service (`app/services/feedback.py`) and idempotent scoring state machine (`app/services/scoring.py`). Key decisions and behaviors:

- **Centralized Friendly Feedback Mapping (`FeedbackResult`):** `format_feedback` turns raw `MovementResult` evaluation outputs into structured `FeedbackResult` objects. Every feedback code (`great`, `raise_arms`, `reach_left`, `reach_right`, `lift_knee`, `hold`, `full_body_missing`, `move_back`, `try_again`) maps to approved non-medical wording per section 12 and `docs/content_baseline.md`.
- **Visibility Precedence:** `full_body_missing` and framing codes (`move_back`) set `visibility_ok=False` and immediately return framing instructions before technique feedback.
- **Idempotent Star Scoring (`ScoringSession`):** A single completed attempt awards 1 Star (`stars_awarded=1`, `total_stars += 1`). Replaying identical success frames on the same attempt returns `stars_awarded=0` while keeping `completed=True` and `total_stars` unchanged, preventing points farming.
- **Attempt Lifecycle and Reset:** Calling `session.start_new_attempt()` or `session.reset_session()` clears the attempt completion state, allowing subsequent successful attempts to earn stars. Switching movements automatically initiates a new attempt.

