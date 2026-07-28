# MP-025 final QA triage

## 1. Purpose

This document records final-day QA findings, classification, ownership, retest
evidence, known issues, and the release decision for one exact MovePal release
candidate. It must not combine evidence from different candidates.

## 2. Candidate identity

| Field | Value |
| --- | --- |
| Release candidate tag | `sprint1-rc1` |
| Frozen application SHA | `bfde35e112f3846fbf1771bc362154b32c72249a` |
| MP-025 base SHA | `7e359be25d0a697c79df37bf0142d5f17d1090f8` |
| Test date | 2026-07-28 |
| Triage owner | `@alaamadii` |
| Independent reviewer | Pending review by `@Tojan-Naiem` |
| Supported environment | Python 3.11; CI: Windows `windows-latest` and Ubuntu `ubuntu-latest`; local rehearsal: Windows NT 10.0.22631 with Chrome 150.0.7871.184 and Edge 150.0.4078.99 |

The local `sprint1-rc1` tag resolves to the frozen application SHA above.
The MP-025 base SHA contains the completed and merged MP-024 handoff work after
the frozen application commit. MP-024 is closed; MP-025 now waits for the
independent results from MP-028 through MP-033.

## 3. Classification rules

- **Must fix:** blocks the Sprint 1 release or core demo.
- **Should fix:** important, but a documented workaround exists.
- **Future improvement:** outside the bounded Sprint 1 MVP.
- **Invalid / Needs information:** evidence is insufficient or the reported
  behavior is not reproducible.

Severity is recorded separately:

- **Critical:** release candidate unusable, cannot install/start, required data
  exposed, or the main fallback demonstration cannot run.
- **High:** a required Sprint movement/input path is unavailable, unsafe,
  misleading, or consistently crashes.
- **Medium:** required behavior works only partly, feedback/score is incorrect,
  or accessibility/usability/documentation is significantly affected.
- **Low:** minor visual, wording, consistency, or non-blocking documentation
  defect with a clear workaround.

## 4. QA triage table

| ID | QA task | Finding | Reproduction evidence | Severity | Classification | Owner | Fix reference | Retest owner | Retest commit | Retest result | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|
| MP-028 | Clean installation, startup, and README sanity | Pending QA result | No QA report has been submitted yet | Pending | Pending | `@Tojan-Naiem` | Pending | `@Tojan-Naiem` | Pending | Pending QA result | Waiting |
| MP-029 | Camera permission, no-camera, browser, and fallback sanity | Pending QA result | No QA report has been submitted yet | Pending | Pending | `@SajaZenaty` | Pending | `@SajaZenaty` | Pending | Pending QA result | Waiting |
| MP-030 | Pose visibility and three-movement sanity | Pending QA result | No QA report has been submitted yet | Pending | Pending | `@nezarYousef` | Pending | `@nezarYousef` | Pending | Pending QA result | Waiting |
| MP-031 | Feedback, scoring, repeat, reset, and summary | Pending QA result | No QA report has been submitted yet | Pending | Pending | `@saliqasarwi` | Pending | `@saliqasarwi` | Pending | Pending QA result | Waiting |
| MP-032 | Invalid input, oversized file, errors, privacy, and disclaimer | Pending QA result | No QA report has been submitted yet | Pending | Pending | `@SaadRayh` | Pending | `@SaadRayh` | Pending | Pending QA result | Waiting |
| MP-033 | Responsive/accessibility sanity and consolidated QA report | Pending QA result | No QA report has been submitted yet | Pending | Pending | `@BaraahMazeen` | Pending | `@BaraahMazeen` | Pending | Pending QA result | Waiting |

## 5. Targeted fixes

No targeted code fix was implemented because no reproducible release-critical defect was available in the provided evidence.

## 6. Retest evidence

No fix retest can be recorded because no confirmed defect or targeted fix is
available locally. For every future fix, record the original reproduction
steps, exact retested commit, tester, environment, expected result, actual
result, Pass/Fail result, and related automated tests. A retest remains
Pending until a tester actually executes it.

## 7. Known issues and accepted limitations

| Limitation | Impact | Workaround | Release decision | Follow-up reference |
| --- | --- | --- | --- | --- |
| Pose rules use a small deterministic fixture set and one compatibility sample. | Results are not accuracy or clinical evidence. | Treat output only as playful prototype feedback. | Accepted prototype limitation; verify behavior stays within the documented boundary. | `docs/limitations.md`, MP-021 |
| A still-frame knee heuristic cannot prove a dynamic step. | Dynamic movement quality is not measured. | Evaluate only the documented knee-position game heuristic. | Accepted prototype limitation. | `docs/limitations.md`, MP-016 |
| Single-person pose tracking is assumed. | Multiple people may cause landmark swapping or incorrect selection. | Keep one person in frame. | Accepted prototype limitation unless QA finds behavior outside this boundary. | `docs/limitations.md` section 2 |
| Formal assistive-technology, WCAG, and cross-browser audits are incomplete. | Accessibility or browser-specific defects may remain. | Perform MP-033 keyboard, responsive, readability, and browser sanity checks. | Pending external QA. | `docs/limitations.md` section 6; MP-033 |
| Live camera/photo inference needs a separately downloaded, gitignored MediaPipe `.task` model. | Live inference does not work without local model setup. | Follow README setup or use the model-free built-in fallback. | Accepted with documented setup; fallback remains mandatory. | `README.md`; `docs/qa_handoff.md` |
| Session state is a signed, unencrypted browser cookie and is not resumable across browsers/devices. | Clearing cookies ends progress; no cross-device history exists. | Complete one local session in one browser; store no personal data. | Accepted MVP limitation. | `docs/privacy.md`; `docs/limitations.md` section 4 |

## 8. Final regression evidence

| Check | Command | Environment | Result | Count / relevant error |
| --- | --- | --- | --- | --- |
| Ruff lint | `python -m ruff check . --exclude .tmp` | Windows 11 10.0.22631; Python 3.13.12 | Pass | All checks passed |
| Ruff formatting | `python -m ruff format --check . --exclude .tmp` | Windows 11 10.0.22631; Python 3.13.12 | Pass | 43 files already formatted |
| pytest | `python -m pytest -p no:cacheprovider` | Windows 11 10.0.22631; Python 3.13.12; pytest 9.0.2 | Pass | 221 passed in 2.40s |
| compileall | `python -m compileall -q app tests scripts` | Windows 11 10.0.22631; Python 3.13.12 | Pass | Exit code 0; no errors |
| JavaScript syntax | `node --check app/static/js/app.js` | Windows 11 10.0.22631; Node v24.14.0 | Pass | Exit code 0; no errors |
| Deterministic QA self-check | `python scripts/qa_selfcheck.py --skip-lint` | Windows 11 10.0.22631; Python 3.13.12 | Pass with manual warnings | 46 pass, 0 fail, 3 manual warnings |
| Flask health smoke | Flask test client `GET /api/health` | Windows 11 10.0.22631; Python 3.13.12 | Pass | HTTP 200; `{"service": "movepal", "status": "ok"}` |
| Git status/privacy scan | `git status --short`, `git diff`, `git ls-files`, targeted prohibited-data pattern scan | Local working tree | Pass with expected untracked files | Only `.tmp/` and this document are untracked; `.tmp/` was not inspected or modified; no prohibited file name or private-data pattern found in this document |
| Manual browser/camera | Permission grant/deny, stop/reset, upload, fallback journey | Pending | Pending | Not performed |
| Manual responsive/keyboard | 375px, keyboard-only navigation, visible focus | Pending | Pending | Not performed |

## 9. Release decision

**Pending evidence**

MP-024 is complete and merged, and the release-candidate identity is recorded.
Results for mandatory QA tasks MP-028 through MP-033, including the MP-033
consolidated recommendation, have not been submitted. There is therefore no
evidence-based basis to claim Release or Release with known limitations, and
no confirmed defect evidence on which to declare No release. Local automated
checks pass, but they do not replace the missing independent QA evidence.

If a confirmed defect requires code changes, `sprint1-rc1` must remain at its
existing SHA. After review and full retest, create a new candidate such as
`sprint1-rc2`; do not move the old tag.

## 10. Completion checklist

- [x] MP-024 completed and reviewed.
- [ ] MP-028 through MP-033 results recorded.
- [ ] Every finding classified.
- [x] Every finding has an owner.
- [ ] Must-fix defects resolved or release blocked.
- [ ] Every fix has a focused regression test.
- [ ] Every fix has independent retest evidence.
- [x] Full automated suite passes.
- [ ] Manual browser/camera QA recorded.
- [x] Known limitations documented.
- [x] Final tested SHA recorded.
- [ ] Independent review completed.
- [x] Final release decision recorded.
