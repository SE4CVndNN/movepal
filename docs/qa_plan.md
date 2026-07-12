# MovePal external QA plan

## Policy

Team A (`team-aidsign`) performs external MovePal QA only on Wednesday, 29 July 2026. Earlier sprint work is owned by Team B. External QA starts only after MP-024 records and freezes the release-candidate commit.

The six QA issues are manual sanity checks, not feature-development tasks:

- MP-028: clean installation, startup, and README
- MP-029: camera permission, no-camera, browser, and fallback
- MP-030: pose visibility and all three movements
- MP-031: feedback, score, repeated sessions, reset, and summary
- MP-032: invalid/oversized input, errors, privacy, and disclaimer
- MP-033: responsive/accessibility sanity and consolidated QA report

Each member has approximately 3.5 focused hours. All six issues run in parallel against the same frozen commit.

## Required manual evidence

Every check records:

- OS, Python version, browser/version, and relevant device information
- exact tested commit
- exact steps
- expected result
- actual result
- severity
- redacted evidence
- linked defect issue
- retest result and retested commit

QA members do not fix MovePal feature code through QA issues. Each failure becomes a separate bug issue. Team B triages it through MP-025 as must fix in Sprint 1, should fix, future improvement, or invalid/needs information.

No child data is used. Prefer included samples. Any adult testing follows consent and privacy documentation, and raw recordings are never attached to GitHub issues.
