# MP-020 — External asset / pretrained-model evaluation

**Status:** Draft
**Author:** Joud
**Reviewer:** Islam
**Related task:** MP-020 (Closes #20)

## Scope note

This evaluation follows the **revised** MP-020 description in the GitHub
Issue (existing dataset / pretrained-model evaluation only — no new
recruitment, no consent template). The entry for MP-020 in
`backlog/product_backlog.json` and `backlog/dependency_report.md` still shows
the **old** scope ("adult-only calibration protocol, consent template,
landmark extraction"). That backlog file is a stale planning snapshot; the
Issue is authoritative. Flagging this here so reviewers aren't confused by
the mismatch.

## 1. Minimum project need (from MP-007 / MP-013 contracts)

- Landmarks required by the three Sprint 1 movements (raise both arms, side
  reach, knee lift/step): shoulders, elbows, wrists, hips, knees, ankles —
  see `TRACKED_LANDMARK_NAMES` in `app/services/pose_tracking.py`.
- Anatomical left/right consistency (MediaPipe's own convention, unmirrored
  frame — `docs/adr/002-pose-estimator.md` Finding 4).
- Normalized `x`/`y` in `[0, 1]`, `z` roughly hip-relative, `visibility` in
  `[0, 1]` (schema: `data/schemas/movement_fixture.schema.json`).
- Must produce output compatible with the project-owned `PoseResult` /
  `Landmark` contract in `app/services/pose_tracking.py`.
- Must not require a network download or model binary in CI.

## 2. Candidate comparison

| Candidate                                                                                           | Asset type                                     | Source/version                                                                           | License                                                                 | Movement coverage                                                                                                                       | Landmark compatibility                                                                                          | Privacy risk                                                                                     | Download/runtime cost                                           | Decision                                                                                                                     |
| --------------------------------------------------------------------------------------------------- | ---------------------------------------------- | ---------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ | --------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| MediaPipe Pose Landmarker (`pose_landmarker_lite.task`)                                             | Pretrained model                               | Google, MediaPipe Tasks API, `mediapipe==0.10.35` (already pinned in `requirements.txt`) | Apache 2.0 (MediaPipe); model file separately hosted by Google          | Full — all 6 tracked joint pairs present in its 33-point topology                                                                       | Already mapped 1:1 in `app/services/pose_tracking.py` (`_MEDIAPIPE_LANDMARK_INDEX`)                             | Low — no bundled personal data; model is geometry weights, not training images                   | ~5.8 MB one-time download, local inference, no ongoing cost     | **SELECTED (already implemented, MP-013)**                                                                                   |
| Openly licensed single stock/demo photo (Pixabay License / Google's own Pose Landmarker demo image) | Licensed sample media                          | Same source ADR-002 already used for its one-time local check                            | Pixabay License — free commercial/personal use, no attribution required | Covers upper+lower body in one frame (sufficient for a single compatibility spike)                                                      | Verified compatible — ADR-002 ran it and got `PoseStatus.SUCCESS` with visibility 0.69–1.0                      | Adult, non-study subject, openly licensed — no consent form required (not a study participant)   | Free, one download, never committed                             | **SELECTED for this task's compatibility spike (Option A)**                                                                  |
| COCO 2017 Keypoints dataset                                                                         | Public dataset (images + keypoint annotations) | cocodataset.org, 2017 release                                                            | CC BY 4.0 (annotations); images have mixed source licenses              | Partial — 17-keypoint COCO topology overlaps MovePal's needs but uses different point definitions/order; would need a translation layer | Would require writing and maintaining a new index-mapping layer — out of scope for a "small reproducible spike" | Contains real, identifiable people at scale, with no per-subject consent for this specific reuse | Tens of GB if downloaded in full; large for a single-spike need | **Rejected** — disproportionate size/engineering cost and privacy review burden for what a single-photo spike already proves |
| Existing synthetic fixtures (`data/landmarks/*.json`)                                               | Hand-authored synthetic landmarks              | Already in repo, MP-005/MP-007                                                           | N/A (authored in-house)                                                 | Full coverage of the three movements' positive/negative/borderline cases                                                                | Native — already the schema's only accepted `source_type`                                                       | None — no real people involved at all                                                            | Zero cost, zero risk                                            | **Fallback / always-available baseline** — kept as-is, this is what MP-021 uses if no external asset were viable             |

## 3. License, provenance, and privacy detail (selected candidates)

### MediaPipe Pose Landmarker

- Official source: Google MediaPipe (`https://ai.google.dev/edge/mediapipe/solutions/vision/pose_landmarker`), model asset hosted at `storage.googleapis.com/mediapipe-models/...`.
- Version: `mediapipe==0.10.35` (pinned in `requirements.txt`); model file `pose_landmarker_lite.task`, float16.
- Redistribution: model file is **not** redistributed by this repo — every contributor downloads it locally (`.gitignore`: `pose_landmarker*.task`).
- Contains only geometry-detection weights, no identifiable training media shipped with the package.
- No child data involved — it is a general-purpose pose detector, not a dataset of people.


### Stock/demo photo 

- Exact source URL: https://pixabay.com/photos/training-pull-up-workout-fitness-828744/
- License: Pixabay Content License
- Access date: 2026-07-23
- Subject: One adult in athletic wear used as a one-time compatibility sample for MediaPipe Pose Landmarker.
- Raw photo is stored locally for the compatibility check only and is excluded from version control.
- Recorded provenance is documented here and in `docs/dataset_card.md`; only the derived landmark data may be committed.


## 4. Decision

**Primary:** Continue using MediaPipe Pose Landmarker as the pretrained model
(already implemented — this task doesn't change that) and use one openly
licensed demo photo (Option A) as the one-time compatibility-spike sample,
converted into a schema-shaped JSON record for evidence only (see the
"Known compatibility gap" note below — it is not inserted into the three
schema-enforced fixture files).

**Fallback:** If no external asset were suitable, MP-021 continues to use the
existing synthetic fixtures in `data/landmarks/`. (Not needed here — the spike
succeeded — but documented per the acceptance criteria.)

- Why it fits Sprint 1: zero training, zero annotation, already wired end to
  end, and now has one additional reproducible real-sample proof point.
- What it does not support: it doesn't give us bulk labeled movement
  examples — that remains MP-021's calibration job using the synthetic
  fixtures plus this one real-sample data point.
- Local download required: yes, one-time, for the `.task` model file only
  (already documented in `README.md`); the photo is a one-time local file,
  never committed.
- May the asset be committed: no — neither the photo nor the model file.
  Only the derived JSON landmark numbers may be committed.
- What must stay outside Git: the `.task` model file, the source photo.
- How MP-021 can use this: as one additional real-sample compatibility data
  point alongside the synthetic fixtures when calibrating thresholds.
- Why COCO was rejected: disproportionate size/engineering/privacy cost for
  what this spike needs to prove.

## 5. Known compatibility gap (please read before merging)

`data/schemas/movement_fixture.schema.json` currently requires
`"source_type": "synthetic"` and a `fixture_id` matching
`^synthetic_[a-z0-9_]+$`. A real-photo-derived landmark record is honestly
not synthetic, so it cannot pass that schema's `const`/`pattern` checks as-is,
and `tests/unit/test_movement_fixtures.py` only schema-validates three named
files under `data/landmarks/`. This task does not change MP-007's schema or
those three files. The derived record from this spike is kept as standalone
evidence (`docs/evidence/mp-020-external-sample-landmarks.json`) and validated
against the same field/shape/range rules by
`scripts/validate_external_asset.py`, without claiming `source_type:
synthetic`. If the team wants real-sample fixtures to become first-class
citizens later, that's a schema-owner (MP-007) decision, flagged here for
MP-021.

## 6. Reproduction

```bash
python scripts/validate_external_asset.py --fixture-json docs/evidence/mp-020-external-sample-landmarks.json
```

or, with a real permitted photo and the downloaded `.task` model:

```bash
python scripts/validate_external_asset.py --model pose_landmarker_lite.task --image <path-to-permitted-photo>
```
