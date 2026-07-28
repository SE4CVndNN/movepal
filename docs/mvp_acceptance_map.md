# MovePal MVP acceptance map

This document maps the final Sprint 1 MVP capabilities to observable behavior,
merged implementation evidence, and the checks used in QA and the
demonstration. It records the implemented product; it does not replace the
individual issue acceptance criteria.

## Capability-to-evidence mapping

| MVP capability | Observable user behavior | Evidence and test level | Owning work | Primary implementation contributors |
| --- | --- | --- | --- | --- |
| **Webcam input** | The user explicitly chooses the camera, sees a preview, receives framing guidance, captures a bounded still frame, and the camera stops after capture or cancellation. | Browser QA, frame API tests, privacy/cleanup tests, and [integration PR #117](https://github.com/SE4CVndNN/movepal/pull/117) | [MP-012](https://github.com/SE4CVndNN/movepal/issues/12), [MP-019](https://github.com/SE4CVndNN/movepal/issues/19) | `@JHT127`, `@alaamadii` |
| **Photo input** | The user can select a validated JPEG or PNG within the size limit and receives the same pose/movement feedback used by the camera path. Invalid, oversized, or non-pose input receives a safe, actionable response. | Upload/API regression tests, manual photo QA, and [hardening PR #120](https://github.com/SE4CVndNN/movepal/pull/120) | [MP-010](https://github.com/SE4CVndNN/movepal/issues/10), [MP-019](https://github.com/SE4CVndNN/movepal/issues/19), [MP-023](https://github.com/SE4CVndNN/movepal/issues/23) | `@AhmadKollab`, `@alaamadii`, `@IslamOuda85` |
| **No-camera fallback** | The user can complete the selected movement without camera hardware, a personal image, or a downloaded pose model by using a committed deterministic landmark fixture through the movement API. | Deterministic fixture/API tests and manual no-camera demo; [camera/fallback PR #103](https://github.com/SE4CVndNN/movepal/pull/103) and [integration PR #117](https://github.com/SE4CVndNN/movepal/pull/117) | [MP-012](https://github.com/SE4CVndNN/movepal/issues/12), [MP-019](https://github.com/SE4CVndNN/movepal/issues/19) | `@JHT127`, `@alaamadii` |
| **Raise both arms** | The system distinguishes success, retry, low visibility, and framing outcomes for the raise-arms rule. | Unit/API tests and [PR #101](https://github.com/SE4CVndNN/movepal/pull/101) | [MP-014](https://github.com/SE4CVndNN/movepal/issues/14) | `@myarnwas` |
| **Left/right side reach** | The selected anatomical side is evaluated independently and receives side-specific success or retry feedback. | Unit/API tests and [PR #102](https://github.com/SE4CVndNN/movepal/pull/102) | [MP-015](https://github.com/SE4CVndNN/movepal/issues/15) | `@myarnwas` |
| **Left/right knee lift** | The selected anatomical knee is evaluated independently and receives success, retry, low-visibility, or framing feedback. | Unit/API tests and [PR #104](https://github.com/SE4CVndNN/movepal/pull/104) | [MP-016](https://github.com/SE4CVndNN/movepal/issues/16) | `@alaamadii` |
| **Friendly visibility/framing help** | Before movement correction, the UI tells the user what needs to be visible or how to improve framing using short, non-medical wording. | Pose/rule tests, browser QA, content audit, and [PR #120](https://github.com/SE4CVndNN/movepal/pull/120) | MP-013 through MP-016, MP-019, and MP-023 | `@myarnwas`, `@alaamadii`, `@IslamOuda85` |
| **Stars and feedback** | A star is awarded only for a completed movement, not merely because pose extraction succeeded; retries do not increase the score. | Scoring unit/API tests and [PR #105](https://github.com/SE4CVndNN/movepal/pull/105) | [MP-017](https://github.com/SE4CVndNN/movepal/issues/17) | `@fatimarajab12` |
| **Session summary/reset** | The current session shows attempts, completions, stars, and per-movement progress; reset clears only the current non-identifying session. | Session tests, browser QA, and [PR #106](https://github.com/SE4CVndNN/movepal/pull/106) | [MP-018](https://github.com/SE4CVndNN/movepal/issues/18) | `@AhmadKollab` |
| **Non-medical/privacy boundary** | The disclaimer is visible, camera purpose is explained before permission, frames are processed transiently, and user-facing errors do not reveal technical details. | Content/privacy audit, error tests, and [PR #121](https://github.com/SE4CVndNN/movepal/pull/121) | [MP-002](https://github.com/SE4CVndNN/movepal/issues/2), [MP-023](https://github.com/SE4CVndNN/movepal/issues/23) | `@IslamOuda85` |

## Sprint 1 verification decisions

1. **No webcam or denied permission:** use the deterministic fixture fallback.
   It is not a pre-recorded personal video and does not need the MediaPipe
   model.
2. **Low light, occlusion, or incomplete framing:** return visibility/framing
   guidance before movement-specific correction; do not guess or award a star.
3. **Pose extraction versus movement success:** detecting landmarks is only the
   input to a movement rule. A star requires that the selected rule returns a
   completed result.
4. **Anatomical side:** left/right means the user's anatomical side even when
   the browser preview is mirrored.
5. **Release evidence:** automated checks support the decision but do not
   replace MP-028 through MP-033 manual QA.

## Final demonstration trace

The 10–12 minute walkthrough and contingency path are in
[`demo_plan.md`](demo_plan.md). Candidate identity, known limitations, and the
pending QA rule are in [`release_notes.md`](release_notes.md).
