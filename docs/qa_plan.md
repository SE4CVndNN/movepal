# MovePal External QA Plan

## 1. Purpose

External QA provides an independent final-day sanity check of the MovePal release candidate. It verifies that a new user can install, run, understand, and exercise the documented MVP without relying on the development team’s local environment.

External QA complements, but does not replace, developer unit tests, integration tests, CI, peer review, and continuous testing throughout the Sprint.

## 2. Timing and ownership

- **QA date:** Wednesday, 29 July 2026
- **QA team:** Team A / `team-aidsign`
- **Development and defect-triage team:** Team B / `team-movepal`
- **Entry dependency:** MP-024 must freeze and record the release-candidate commit.
- **Final triage/release task:** MP-025

External QA begins only after the development team provides a complete QA handoff. All six testers use the same commit unless a documented critical fix creates a new retest commit.

## 3. Entry criteria

Before QA starts, MP-024 must provide:

- exact commit hash or release-candidate tag;
- fresh-install instructions;
- supported Python version;
- test and start commands;
- expected Windows/Linux behavior;
- supported browser expectations;
- fallback samples and expected outcomes;
- three-movement behavior summary;
- known non-blocking limitations;
- privacy-safe evidence rules;
- bug-report template link;
- development-team triage contact.

If the handoff is incomplete or the release candidate does not start, the QA coordinator records a blocker immediately rather than allowing six testers to repeat the same failed setup.

## 4. Common QA procedure

Each tester should:

1. Open the assigned QA issue.
2. Record the exact commit under test.
3. Record operating system, browser/version, Python version, and relevant camera/device information.
4. Follow the README from a fresh or clean environment.
5. Execute the assigned test cases without receiving undocumented setup help.
6. Record expected and actual results.
7. Capture privacy-safe evidence.
8. Open a separate bug issue for each distinct defect.
9. Link defects from the QA issue.
10. Retest only after the development team provides a fix commit.
11. Record final pass/fail and retest result.

Do not attach raw video, child data, consent forms, or identifiable participant images.

## 5. QA task allocation

### MP-028 — Clean installation, startup, and README sanity

Owner: `Tojan-Naiem`

Check:

- repository clone/access;
- Python 3.11 requirement;
- virtual-environment instructions;
- production/development dependency installation;
- Ruff and pytest commands;
- application startup;
- health endpoint;
- missing or misleading README steps;
- clean shutdown and restart.

### MP-029 — Camera permission, no-camera, browser, and fallback sanity

Owner: `SajaZenaty`

Check:

- initial camera permission request;
- permission granted;
- permission denied;
- no camera available;
- camera stopped/reset;
- supported browser behavior;
- fallback sample selection and processing;
- understandable user guidance when camera use fails.

### MP-030 — Pose visibility and three-movement sanity

Owner: `nezarYousef`

Check:

- no person detected;
- partial body outside the frame;
- low visibility;
- raise both arms success/retry;
- left and right side reach;
- knee lift or step in place;
- incorrect and borderline attempts;
- multiple-person behavior if encountered;
- no forced positive result when the pose is unclear.

### MP-031 — Feedback, scoring, repeat, reset, and summary

Owner: `saliqasarwi`

Check:

- friendly success/retry messages;
- no medical claims;
- stars/points behavior;
- repeated attempts;
- retry/continue flow;
- session summary accuracy;
- reset behavior;
- no stale score/session data after reset.

### MP-032 — Invalid input, oversized file, errors, privacy, and disclaimer

Owner: `SaadRayh`

Check:

- missing input;
- unsupported media type;
- corrupted input;
- oversized upload;
- safe user-facing errors;
- absence of private paths/stack traces;
- visible privacy notice;
- visible non-medical disclaimer;
- no unexpected retention or exposed upload files.

### MP-033 — Responsive/accessibility sanity and consolidated QA report

Owner: `BaraahMazeen`

Check:

- common desktop width;
- narrow/mobile-like width;
- keyboard navigation;
- visible focus;
- readable feedback and controls;
- label/instruction clarity;
- basic color-independent meaning;
- final cross-issue QA summary;
- release recommendation based on linked results.

## 6. Test-case recording format

For every case, record:

```text
Test ID:
Environment:
Tested commit:
Preconditions:
Steps:
Expected result:
Actual result:
Status: Pass / Fail / Blocked / Not applicable
Severity if failed:
Evidence:
Bug issue:
Retest commit:
Retest result:
```

## 7. Severity definitions

### Critical

The application cannot be installed or started; required data is exposed; the release candidate is unusable; or the main fallback demonstration cannot run.

### High

A required Sprint movement/input path is unavailable, produces unsafe/misleading behavior, or consistently crashes.

### Medium

A required behavior works only partially, provides incorrect feedback/score, has a significant accessibility/usability problem, or contradicts documentation.

### Low

A minor visual, wording, consistency, or non-blocking documentation defect with a clear workaround.

Severity is not the same as priority. Team B triages each defect using impact, effort, Sprint Goal, and release risk.

## 8. Bug-report rules

Each distinct defect becomes a separate issue using the bug template. Include:

- concise title;
- tested commit;
- environment;
- reproduction steps;
- expected and actual behavior;
- severity proposal;
- privacy-safe evidence;
- affected feature/task;
- whether the fallback path is affected.

QA members do not silently modify MovePal feature code through the QA issue. They may clarify evidence or assist with retesting.

## 9. Development-team triage

Through MP-025, Team B categorizes each finding as:

- **must fix in Sprint 1**;
- **should fix**;
- **future improvement**;
- **invalid / needs information**.

For a fix:

1. assign a developer;
2. create a focused branch/PR;
3. add or update a regression test;
4. obtain independent review;
5. pass CI;
6. provide the new commit to the original QA tester;
7. record the retest result.

## 10. Stop and escalation conditions

Pause or coordinate QA when:

- the release-candidate hash is missing or changes without notice;
- installation fails for every tester for the same reason;
- privacy-sensitive evidence appears in GitHub;
- the fallback sample is missing;
- the team discovers child data;
- a critical defect invalidates most remaining cases.

Notify the Scrum Master and instructor immediately for privacy or release-blocking incidents.

## 11. Exit criteria

External QA is complete when:

- all six QA issues contain environment and tested-commit information;
- planned cases are marked pass/fail/blocked/not applicable;
- each failure has a linked bug issue or documented explanation;
- critical/high fixes are retested where required;
- MP-033 consolidates the result;
- MP-025 records the release decision and remaining known limitations;
- evidence contains no prohibited data.
