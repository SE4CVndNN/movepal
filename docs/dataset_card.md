# MovePal Landmark Dataset Card

This document describes the small dataset/fixture collection used to calibrate and test MovePal’s transparent movement rules. Complete every section before derived adult-volunteer data is committed or shared.

The dataset is not clinical, does not establish treatment effectiveness, and must not contain child data.

## 1. Dataset identity

- **Name:** MP-020 external asset compatibility spike
- **Version:** 0.1
- **Status:** draft
- **Creation date:** 2026-07-23
- **Last updated:** 2026-07-23
- **Related tasks/PRs:** MP-020 / PR #107

## 2. Intended purpose

Describe the exact narrow purpose, for example:

- verify the landmark schema;
- test success/retry/framing behavior;
- select prototype thresholds;
- provide deterministic CI fixtures;
- check regression behavior for three Sprint movements.

Explicitly list prohibited uses:

- clinical assessment;
- diagnosis;
- treatment evaluation;
- unrestricted model training;
- comparison of participant ability;
- inference of health or disability;
- use with children.

This dataset specifically aims to:

- verify the landmark schema;
- check compatibility of a real permitted sample with the existing pose contract (pipeline compatibility), i.e. confirm that externally-derived landmarks conform to MovePal's `PoseResult` shape and conservative visibility/coverage expectations.

Prohibited uses remain as listed above.

## 3. Data sources and provenance

For each source category, record:

| Source category                   | Count | Provenance                                                                                               | Permission/license      | Raw media retained? | Releasable?            |
| --------------------------------- | ----: | -------------------------------------------------------------------------------------------------------- | ----------------------- | ------------------- | ---------------------- |
| Synthetic/hand-authored landmarks |       |                                                                                                          |                         | No                  |                        |
| Licensed sample media             |     1 | Pixabay photo: https://pixabay.com/photos/training-pull-up-workout-fitness-828744/ (accessed 2026-07-23) | Pixabay Content License | No                  | Derived landmarks only |
| Consented adult-derived landmarks |       |                                                                                                          |                         |                     |                        |

Do not include a source when permission or provenance is uncertain.

## 4. Data subjects and consent

- Adults only: yes/no
- Confirmation that no child data is included:
- Consent-template version:
- Consent storage location (private, not GitHub):
- Anonymous-ID method:
- Withdrawal/deletion contact/process:
- Whether derived landmarks may be committed or published:
- Whether raw media may be retained, and for how long:

Never put participant names or contact details in this file.

- Adults only: yes
- Confirmation that no child data is included: yes — single openly licensed stock photo of an adult, not a study participant
- Consent-template version: N/A — not a study participant, no consent form required per Option A reasoning
- Consent storage location (private, not GitHub): N/A
- Anonymous-ID method: N/A
- Withdrawal/deletion contact/process: N/A
- Whether derived landmarks may be committed or published: yes — derived landmarks only
- Whether raw media may be retained, and for how long: No raw media retained in repository

## 5. Representation and schema

Document the project landmark schema, including:

- landmark names;
- `x`, `y`, and `z` meaning/range;
- visibility/confidence meaning;
- anatomical left/right convention;
- mirrored-camera handling;
- missing-landmark representation;
- frame or sequence representation;
- units/normalization;
- schema version.

Each fixture should include or reference:

```text
fixture_id
movement
requested_side
expected_completed
expected_feedback_code
category
landmarks
provenance_type
consent_or_license_status
collection_condition
annotation_note
schema_version
```

## 6. Movement and outcome coverage

Record counts for each category:

| Movement             | Positive | Negative | Borderline | Missing/low visibility | Framing failure | Total |
| -------------------- | -------: | -------: | ---------: | ---------------------: | --------------: | ----: |
| Raise both arms      |          |          |            |                        |                 |       |
| Side reach left      |          |          |            |                        |                 |       |
| Side reach right     |          |          |            |                        |                 |       |
| Knee lift/step left  |          |          |            |                        |                 |       |
| Knee lift/step right |          |          |            |                        |                 |       |

Explain gaps rather than presenting a small incomplete sample as comprehensive.

## 7. Collection conditions

Summarize:

- camera/device types;
- resolution;
- distance and camera height;
- lighting variation;
- background variation;
- clothing variation;
- standing/seated conditions;
- occlusion cases;
- whether multiple people were present;
- instructions given to participants.

Avoid documenting identifying locations.

## 8. Annotation process

Describe:

- who assigned movement/outcome labels;
- the annotation guide version;
- how correct, incorrect, borderline, and framing cases were defined;
- how ambiguous cases were resolved;
- whether a second reviewer checked labels;
- changes made after review.

## 9. Split and evaluation policy

Separate data used to choose thresholds from held-out sanity/regression fixtures where possible.

Document:

- calibration/tuning subset;
- held-out subset;
- duplicate/near-duplicate handling;
- participant separation when adult-derived data is used;
- how leakage was avoided;
- metrics or case counts reported;
- why the evaluation remains limited.

Do not claim general accuracy from a tiny convenience sample.

## 10. Privacy and security

- Raw private storage location:
- Derived-data storage location:
- Access list/role:
- Git exclusions checked:
- Metadata removal process:
- Temporary-file deletion process:
- Retention period:
- Withdrawal/deletion process:
- Release/privacy review completed by:

## 11. Known limitations and bias

Discuss:

- sample size;
- convenience sampling;
- participant/body variation;
- camera/environment coverage;
- clothing and occlusion coverage;
- left/right balance;
- rule-threshold sensitivity;
- synthetic-fixture realism;
- unsupported cases;
- prohibited interpretations.

Note: this dataset contains a single licensed sample used to demonstrate pipeline compatibility only. It does not provide evidence of accuracy, representativeness, or generalizability across populations, camera types, or clothing/occlusion conditions.

## 12. Version history

| Version | Date       | Change                                            | Related issue/PR | Reviewer         |
| ------- | ---------- | ------------------------------------------------- | ---------------- | ---------------- |
| 0.1     | 2026-07-23 | Initial MP-020 external-asset compatibility spike | MP-020 / PR #107 | MovePal reviewer |

A schema, threshold, consent, provenance, or release change requires a new recorded version.

## 13. Release checklist

- [ ] No child data.
- [ ] Every fixture has provenance.
- [ ] Consent/license permits the intended use.
- [ ] Raw private media is not in Git.
- [ ] Schema and coordinate convention are documented.
- [ ] Movement/outcome counts are reported.
- [ ] Annotation review is complete.
- [ ] Calibration and held-out use are distinguished.
- [ ] Limitations and prohibited uses are explicit.
- [ ] Privacy review is complete.
