# Sprint 1 execution plan

## Days 1–2: learn by producing real artifacts

- MP-001 verifies board, access, reviewers, and blocker handling after the instructor kickoff.
- MP-002 produces the acceptance map, safe wording, and demo scenarios.
- MP-003 gives every member a useful reviewed repository contribution.
- MP-004–MP-006 create executable Flask, CV, and browser artifacts.
- MP-007 begins machine-readable movement examples as soon as MP-005 and MP-006 are available.

## Component phase

Backend, frontend, CV, movement rules, documentation, fixtures, and CI proceed in parallel according to explicit dependencies. Owners open draft PRs early and attach their practical first output.

## Early integration gate

MP-014 must prove a deterministic sample-input → API → pose/mock result → raise-arms rule → visible-feedback path before MP-019 integrates the complete game. Contract mismatches discovered here belong in the responsible component issues.

## Release phase

MP-024 freezes one release-candidate commit on 28 July with installation instructions and fallback evidence. All Team A QA tasks execute manually against that same commit on 29 July. QA findings become bug issues; MP-025 owns triage/fix/retest decisions.
