# MovePal Sprint 1 retrospective

## Sprint Goal result

The development team produced a frozen, reproducible release candidate that
covers the intended narrow MVP: three movement families, live camera/photo
input, deterministic fallback, pose and visibility handling, friendly
feedback, stars, session summary, safe errors, documentation, automated tests,
and Windows/Linux CI.

The application candidate is `sprint1-rc1` at
`bfde35e112f3846fbf1771bc362154b32c72249a`. MP-024 is complete and merged.
The final release decision is still **Pending QA evidence** because MP-028
through MP-033 and the MP-025 triage are not complete. The honest Sprint result
at this point is therefore **release candidate delivered; final external QA
pending**, not an unqualified production release.

## What helped

### Small modular architecture

The Flask modular monolith kept routes, pose extraction, movement rules,
feedback, scoring, sessions, templates, and fixtures understandable without
introducing microservices. This made parallel feature work and focused tests
possible.

### Deterministic fixtures and fallback

Synthetic/derived landmark fixtures allowed movement rules and the complete
fallback path to run without camera hardware, personal media, or a model
download. They also gave CI repeatable positive, negative, borderline,
low-visibility, and framing cases.

### Cross-platform automation

The Windows/Ubuntu Python 3.11 matrix caught repository-wide quality problems
and made the final handoff reproducible. The current `master` CI run is green:
[Actions run 30352942869](https://github.com/SE4CVndNN/movepal/actions/runs/30352942869).

### Independent review

Each active member authored substantive work and reviewed another member's PR.
Review caught real issues such as incomplete PR references, baseline lint
failures, contract alignment, privacy wording, and integration behavior. See
[`contribution_report.md`](contribution_report.md).

### Early fallback and integration focus

Keeping a model-free demonstration path protected the Sprint Goal from camera,
lighting, browser-permission, and local-model problems. The combined UI/CV
integration in [PR #117](https://github.com/SE4CVndNN/movepal/pull/117)
provided one coherent flow instead of separate components.

## What slowed or blocked us

### Repository-wide CI failures

The first documentation PR exposed pre-existing Ruff violations outside the
changed document. The team had to diagnose and fix the baseline in
[PR #68](https://github.com/SE4CVndNN/movepal/pull/68) before normal review
could continue.

### Local pose-model setup

Live `/api/frame` evaluation requires a separately downloaded, gitignored
MediaPipe `.task` model. Missing-model errors initially looked like frontend
upload failures. Clear readiness/setup documentation and the deterministic
fallback reduced this confusion.

### Dependency and late-integration pressure

Camera/UI, pose extraction, movement rules, scoring, and session work were
developed in separate tasks. Some behavior could only be judged after those
pieces merged, which concentrated integration and regression work near the
release-candidate date.

### Team membership continuity

A member change required assignments, active-team documentation, and future
ownership to be updated while preserving historical authorship. That handoff
was recorded in [PR #78](https://github.com/SE4CVndNN/movepal/pull/78).

### Review and evidence quality varied

Some PR descriptions began with placeholder sections or incomplete task
references. Reviewers spent extra time requesting reproducible evidence,
correct `Refs`/`Closes` usage, and accurate test/privacy statements.

## Evidence

- [MP-024 release-candidate PR #122](https://github.com/SE4CVndNN/movepal/pull/122)
- [MP-025 triage PR #123](https://github.com/SE4CVndNN/movepal/pull/123)
- [`qa_handoff.md`](qa_handoff.md)
- [`release_notes.md`](release_notes.md)
- [`contribution_report.md`](contribution_report.md)
- [current `master` CI](https://github.com/SE4CVndNN/movepal/actions/runs/30352942869)

## Improvements for the next project or Sprint

| Improvement | Owner/role | Concrete next action |
| --- | --- | --- |
| Validate the repository baseline before the first feature PR. | Testing/DevOps owner | Run the complete CI command set during kickoff and open one bounded baseline issue for any failure. |
| Integrate vertical slices earlier. | Feature owners and Scrum Master | Schedule a camera-or-fallback → API → rule → feedback smoke path before parallel polish begins. |
| Standardize local Python/model readiness. | Backend/CV owners | Provide one checked setup/readiness command and distinguish missing-model errors from upload/network errors. |
| Require complete evidence in every PR. | Authors and reviewers | Fill Purpose, Changes, Tests, Privacy, reviewer focus, and correct issue linkage before requesting review. |
| Prepare external QA evidence earlier. | Scrum Master and QA contact | Freeze the candidate and dry-run the manual checklist before the final QA day. |
| Keep late fixes bounded. | Triage owner | Classify findings first; require a small reviewed PR, CI, and independent retest for every must-fix change. |

## Technical debt and future backlog

- Replace still-frame-only movement heuristics with carefully bounded temporal
  evaluation where the product scope justifies it.
- Expand privacy-reviewed derived fixtures and calibration evidence without
  making clinical or population-accuracy claims.
- Perform formal assistive-technology, WCAG, and broader browser testing.
- Add production deployment, TLS/access-control, protected logs, retention,
  and monitoring only after a separate security/privacy design.
- Improve multiple-person rejection/selection and camera-angle robustness.
- Keep accounts, long-term history, analytics, and clinical personalization
  outside the prototype unless explicitly approved as new scope.

## Team confirmation before submission

- [ ] All six active members have reviewed the contribution summary.
- [ ] The team confirms the “helped” and “blocked” observations are fair.
- [ ] Owners accept the proposed next actions.
- [ ] MP-025 final QA/release decision is linked after completion.
