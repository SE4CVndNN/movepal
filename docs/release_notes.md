# MovePal Sprint 1 release notes

## Candidate identity and status

| Field | Value |
| --- | --- |
| Candidate | `sprint1-rc1` |
| Frozen application SHA | `bfde35e112f3846fbf1771bc362154b32c72249a` |
| Freeze date | 2026-07-28 |
| Current `master` handoff SHA | `7e359be25d0a697c79df37bf0142d5f17d1090f8` |
| Release decision | **Pending QA evidence** |
| QA coordination | [MP-025](https://github.com/SE4CVndNN/movepal/issues/25) and [PR #123](https://github.com/SE4CVndNN/movepal/pull/123) |

`sprint1-rc1` is an immutable release candidate, not a declaration that final
external QA has passed. If a release-critical code fix is required, the old tag
must remain unchanged and a new reviewed and retested candidate must be
recorded.

## Delivered Sprint 1 MVP

- Flask modular-monolith application with an application factory and health
  endpoint.
- Child-friendly browser flow with an original avatar, visible disclaimer,
  responsive controls, keyboard focus, retry, and session summary.
- Explicit live-camera permission flow, still-frame capture, bounded upload,
  camera cleanup, and friendly permission/error recovery.
- Validated JPEG/PNG photo input with a 5 MB request limit.
- Model-free deterministic fallback based on committed synthetic landmark
  fixtures.
- MediaPipe pose-landmark extraction for local live camera/photo evaluation.
- Visibility and framing guidance.
- Transparent game rules for:
  - raise both arms;
  - left/right side reach;
  - left/right knee lift.
- Friendly, non-medical feedback, stars, attempts/completions, reset, and
  summary.
- Safe HTML/API errors that do not expose stack traces or private paths.
- Unit/integration regression coverage, Ruff checks, compile checks, Flask
  health smoke, and Python 3.11 CI on Windows and Ubuntu.
- Privacy, limitations, architecture, movement, QA, and demonstration
  documentation.

## Verification evidence

- [MP-024 handoff PR #122](https://github.com/SE4CVndNN/movepal/pull/122)
  froze and documented the candidate.
- [Current `master` CI run](https://github.com/SE4CVndNN/movepal/actions/runs/30352942869)
  passed on Windows and Ubuntu using Python 3.11.
- The clean MP-024 rehearsal installed the frozen application from scratch on
  Linux/Python 3.11.15, downloaded the gitignored pose model, and passed Ruff,
  formatting, 219 frozen-application tests, compileall, and the health smoke.
- The merged MP-024 handoff adds two QA self-check regression tests; the
  current suite contains 221 tests.
- Deterministic QA self-check evidence records 46 passes, 0 failures, and three
  explicitly manual warnings.

These automated results do not replace MP-028 through MP-033 manual QA.

## Known limitations

- Movement results are playful prototype heuristics, not medical, diagnostic,
  rehabilitation, treatment, fitness, or safety conclusions.
- Pose reliability depends on lighting, framing, camera angle, visibility,
  occlusion, clothing, and one primary visible person.
- The small synthetic/derived fixture set verifies deterministic contracts; it
  is not a population-level accuracy measurement.
- A still-frame knee-position heuristic does not prove a dynamic step.
- Live camera/photo inference needs the separately downloaded, gitignored
  `pose_landmarker_lite.task` model. The built-in fallback does not.
- Session state is a signed, unencrypted, non-identifying browser cookie. It
  has no accounts, cross-device history, or database.
- Formal assistive-technology/WCAG and broad cross-browser audits remain
  outside the completed automated checks.
- Client-provided MIME metadata is a first validation gate; the prototype does
  not provide production malware scanning.
- The prototype has no production deployment, cloud-storage guarantee, or
  production access-control claim.

See [`limitations.md`](limitations.md), [`privacy.md`](privacy.md), and
[`qa_handoff.md`](qa_handoff.md) for the exact boundaries and workarounds.

## Deferred work

- Production hosting, TLS/access-control design, monitoring, and operational
  retention policies.
- User accounts, profiles, databases, analytics, or long-term history.
- Custom model training and population-scale calibration.
- Multiple-person selection and advanced temporal movement tracking.
- Formal accessibility and multi-browser certification.
- Medical/clinical validation or personalized thresholds.

These are future ideas, not incomplete Sprint 1 acceptance claims.

## Finalization rule

Before changing the release decision from **Pending QA evidence**:

1. record MP-028 through MP-033 results;
2. classify every reported finding;
3. resolve and independently retest every must-fix defect, or block release;
4. run full CI on the final tested SHA;
5. update PR #123 and the final QA triage;
6. record **Release**, **Release with known limitations**, or **No release**.
