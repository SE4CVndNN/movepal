# MovePal Landmark Dataset Card

This document describes the small dataset/fixture collection used to calibrate and test MovePal's transparent movement rules. Complete every section before derived adult-volunteer data is committed or shared.

The dataset is not clinical, does not establish treatment effectiveness, and must not contain child data.

## Scope and handoff note

This version of the card covers only the MP-020 external-asset compatibility spike (one openly licensed photo run through the existing MediaPipe adapter). It is not a movement-rule accuracy evaluation and does not replace the existing synthetic fixtures in `data/landmarks/`.

**Handoff to MP-021:** MP-020's output for calibration purposes is this compatibility spike (`docs/external_asset_evaluation.md`, this dataset card, and `docs/evidence/mp-020-external-sample-landmarks.json`) — not a consent template, since MP-020 was revised to a pretrained-model/existing-asset evaluation and no longer collects new participant data. MP-021 should calibrate thresholds against the existing synthetic fixtures plus this one real-sample data point.

## 1. Dataset identity

- **Name:** MP-020 external asset compatibility spike
- **Version:** 0.1
- **Status:** draft
- **Creation date:** 2026-07-23
- **Last updated:** 2026-07-23
- **Related tasks/PRs:** MP-020 / PR #107

## 2. Intended purpose

This dataset specifically aims to:

- verify the landmark schema;
- check compatibility of a real permitted sample with the existing pose contract (pipeline compatibility), i.e. confirm that externally-derived landmarks conform to MovePal's `PoseResult` shape and conservative visibility/coverage expectations.

Explicitly prohibited uses:

- clinical assessment;
- diagnosis;
- treatment evaluation;
- unrestricted model training;
- comparison of participant ability;
- inference of health or disability;
- use with children.

## 3. Data sources and provenance

For each source category, record:

| Source category                   | Count | Provenance                                                                                               | Permission/license      | Raw media retained? | Releasable?            |
| --------------------------------- | ----: | -------------------------------------------------------------------------------------------------------- | ----------------------- | ------------------- | ---------------------- |
| Synthetic/hand-authored landmarks |       |                                                                                                          |                         | No                  |                        |
| Licensed sample media             |     1 | Pixabay photo: https://pixabay.com/photos/training-pull-up-workout-fitness-828744/ (accessed 2026-07-23) | Pixabay Content License | No                  | Derived landmarks only |
| Consented adult-derived landmarks |       |                                                                                                          |                         |                     |                        |

Do not include a source when permission or provenance is uncertain.

## 4. Data subjects and consent

- Adults only: yes
- Confirmation that no child data is included: yes — single openly licensed stock photo of an adult, not a study participant
- Consent-template version: N/A — not a study participant, no consent form required per Option A reasoning
- Consent storage location (private, not GitHub): N/A
- Anonymous-ID method: N/A
- Withdrawal/deletion contact/process: N/A
- Whether derived landmarks may be committed or published: yes — derived landmarks only
- Whether raw media may be retained, and for how long: No raw media retained in repository

Never put participant names or contact details in this file.

## 5. Representation and schema

The full landmark schema (names, `x`/`y`/`z` meaning and range, visibility meaning, anatomical left/right convention, mirrored-camera handling, missing-landmark representation, units/normalization, schema version) is documented in `app/services/pose_tracking.py` (module docstring) and `docs/movement_specification.md`, and is not duplicated here to avoid drift between two copies. This spike's evidence record follows the same convention.

The fixture in `docs/evidence/mp-020-external-sample-landmarks.json` includes:

```text
fixture_id
schema_version
source_type
provenance_reference
description
expected_status
landmarks
```

Note: this is not a full MP-007 fixture record (it omits `movement`, `requested_side`, `expected_completed`, etc., and uses `source_type: external_licensed` rather than `synthetic`), so it is not schema-validated against `data/schemas/movement_fixture.schema.json`. See `docs/external_asset_evaluation.md` §5 for the full explanation of this gap.

## 6. Movement and outcome coverage

| Movement             | Positive | Negative | Borderline | Missing/low visibility | Framing failure | Total |
| --------------------- | -------: | -------: | ---------: | ---------------------: | --------------: | ----: |
| Raise both arms      |          |          |            |                        |                 |       |
| Side reach left      |          |          |            |                        |                 |       |
| Side reach right     |          |          |            |                        |                 |       |
| Knee lift/step left  |          |          |            |                        |                 |       |
| Knee lift/step right |          |          |            |                        |                 |       |

Not applicable to this version of the card. This spike validates pipeline *compatibility* (does an external sample produce a well-formed, `SUCCESS`-status `PoseResult`?), not movement-rule accuracy, so no movement/outcome labels were assigned. Populating this table against real or synthetic per-movement examples is MP-021's job.

## 7. Collection conditions

N/A — no participants were involved. The single sample is a pre-existing, openly licensed stock photograph, not media collected by this project.

## 8. Annotation process

N/A — no manual annotation was performed. The landmark coordinates and visibility values came directly from `MediaPipePoseAdapter`'s inference on the photo; no human labeled or adjusted them.

## 9. Split and evaluation policy

N/A — this card describes a single compatibility example, not a calibration or held-out evaluation set. Separating tuning data from held-out sanity fixtures is in scope for MP-021, once real per-movement fixtures exist.

Do not claim general accuracy from a tiny convenience sample.

## 10. Privacy and security

- Raw private storage location: local machine only, outside the repository; never committed
- Derived-data storage location: `docs/evidence/mp-020-external-sample-landmarks.json` (numeric landmark values only)
- Access list/role: standard repository contributor access — no restricted data is stored, so no special access list is needed
- Git exclusions checked: yes — `data/raw/` and `pose_landmarker*.task` are ignored (see `.gitignore`); verified the photo and model file are absent from `git status`
- Metadata removal process: only `x`/`y`/`z`/`visibility` numeric fields were extracted; no EXIF, filename, or image metadata was copied into the repository
- Temporary-file deletion process: the local photo was deleted from disk after generating the evidence JSON; it was never tracked by Git
- Retention period: no raw media retained (none to retain); the derived JSON is retained indefinitely as versioned evidence
- Withdrawal/deletion process: N/A — subject is not a study participant. If the Pixabay license were ever revoked, the derived evidence would be removed and this spike re-run against a replacement source
- Release/privacy review completed by: pending — see version history for reviewer sign-off

## 11. Known limitations and bias

Note: this dataset contains a single licensed sample used to demonstrate pipeline compatibility only. It does not provide evidence of accuracy, representativeness, or generalizability across populations, camera types, or clothing/occlusion conditions. Convenience-sampled from one stock photo; no left/right balance, body-type variation, or environment coverage is represented. See `docs/external_asset_evaluation.md` for the full candidate comparison and rejected-alternative reasoning.

## 12. Version history

| Version | Date       | Change                                            | Related issue/PR | Reviewer  |
| ------- | ---------- | -------------------------------------------------- | ----------------- | --------- |
| 0.1     | 2026-07-23 | Initial MP-020 external-asset compatibility spike | MP-020 / PR #107  | @myarnwas |

A schema, threshold, consent, provenance, or release change requires a new recorded version.

## 13. Release checklist

- [x] No child data.
- [x] Every fixture has provenance. *(the one external fixture in this spike is fully sourced — see §3)*
- [x] Consent/license permits the intended use. *(Pixabay Content License; not a study participant)*
- [x] Raw private media is not in Git. *(verified — see §10)*
- [x] Schema and coordinate convention are documented. *(via `pose_tracking.py` / `movement_specification.md` — see §5)*
- [ ] Movement/outcome counts are reported. *(not applicable to this spike — see §6; deferred to MP-021)*
- [ ] Annotation review is complete. *(N/A — no annotation performed, see §8)*
- [ ] Calibration and held-out use are distinguished. *(N/A — single example, not an evaluation set, see §9)*
- [x] Limitations and prohibited uses are explicit. *(see §2 and §11)*
- [ ] Privacy review is complete. *(pending reviewer sign-off — see §10 and §12)*
