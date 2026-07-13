# MovePal Landmark Annotation Guide

## 1. Purpose

Annotation assigns a clear expected result and provenance record to each synthetic, licensed, or consented adult-derived fixture. These labels support deterministic tests and threshold evaluation; they do not describe medical correctness.

## 2. Required fixture fields

Every fixture or fixture metadata record should contain:

```text
fixture_id
schema_version
movement
requested_side
expected_completed
expected_feedback_code
category
landmarks
source_type
provenance_reference
consent_or_license_status
collection_condition
annotation_note
annotator
reviewer
review_status
```

Do not include participant name, email, contact information, exact location, private filesystem path, raw recording, or identifying background description.

## 3. Stable identifiers

Use non-identifying IDs such as:

```text
synthetic_raise_arms_positive_001
adult_P001_side_left_borderline_001
```

A public/repository fixture ID may retain an anonymous participant code only when approved. Do not include the raw source filename if it contains private information.

## 4. Movement values

Use stable machine-readable values:

```text
raise_both_arms
side_reach
knee_lift_or_step
```

Use `requested_side`:

```text
left
right
both
not_applicable
```

The side refers to the user’s anatomical side under the convention defined in [`movement_specification.md`](movement_specification.md).

## 5. Categories

### `positive`

The fixture clearly satisfies the intended rule under the documented threshold and visibility conditions.

### `negative`

The fixture clearly does not satisfy the movement rule while still providing enough valid landmarks to evaluate it.

### `borderline`

The fixture is close to a threshold and is useful for boundary testing. The annotation note must identify the relevant measurement.

### `missing_landmark`

One or more required landmarks are absent.

### `low_visibility`

Required landmarks exist but do not meet visibility requirements.

### `framing_failure`

The body area required by the movement is outside the frame or cannot be reliably evaluated.

### `ambiguous`

The correct expected result cannot be agreed. Ambiguous fixtures should not enter the main regression suite until resolved; keep them in a private review set or exclude them.

## 6. Expected outcome

Record:

- `expected_completed`: `true` or `false`;
- `expected_feedback_code`: the expected stable code;
- optional expected measurement ranges;
- why the result is expected.

Do not select a success label only because the original recording was intended to be correct. Label what the landmarks actually show under the project rule.

## 7. Collection-condition metadata

Use non-identifying categories such as:

```text
normal_lighting
low_lighting
far_from_camera
close_to_camera
partial_body
occluded_wrist
neutral_background
synthetic
```

Do not record a home address, room name, institution, or other identifying location.

## 8. Provenance values

Use one of:

```text
synthetic
hand_authored
licensed_sample
consented_adult_derived
```

For licensed or consented sources, maintain a private/reference record proving permission. The fixture must not be committed when permission for the intended derived use is uncertain.

## 9. Annotation procedure

1. Load the fixture using the documented schema.
2. Validate required fields and coordinate ranges.
3. Confirm movement and requested side.
4. Check required landmark availability and visibility.
5. Apply the documented rule manually or with an inspection script.
6. Assign category, expected result, and feedback code.
7. Write a concise annotation note.
8. Check for identifiers/private paths.
9. Submit for independent review.
10. Mark `review_status` only after agreement.

## 10. Second-review process

The reviewer checks:

- schema validity;
- anatomical left/right;
- movement/category consistency;
- expected feedback precedence;
- borderline measurement rationale;
- provenance/permission status;
- privacy safety;
- usefulness and duplication.

If annotator and reviewer disagree:

1. record both interpretations;
2. inspect the rule/specification;
3. correct an unclear specification when necessary;
4. exclude the fixture until agreement;
5. do not tune the rule merely to force one ambiguous sample to pass.

## 11. Regression-suite inclusion

A fixture can enter checked-in tests only when:

- schema validation passes;
- provenance is documented;
- privacy review passes;
- expected result is reviewed;
- it adds useful coverage;
- no raw media is required to run the test;
- the test does not depend on camera hardware or network access.

## 12. Example metadata

```json
{
  "fixture_id": "synthetic_raise_arms_borderline_001",
  "schema_version": "1.0",
  "movement": "raise_both_arms",
  "requested_side": "both",
  "expected_completed": false,
  "expected_feedback_code": "raise_arms",
  "category": "borderline",
  "source_type": "synthetic",
  "provenance_reference": "hand-authored for MP-007",
  "consent_or_license_status": "not_applicable",
  "collection_condition": "synthetic",
  "annotation_note": "Both wrists are just below the configured vertical margin.",
  "annotator": "github-username",
  "reviewer": "different-github-username",
  "review_status": "approved"
}
```
