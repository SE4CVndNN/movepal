# MovePal Sprint 1 enhanced execution plan

**Kickoff:** Monday, 13 July 2026 (instructor-led)  
**Sprint:** Tuesday, 14 July–Wednesday, 29 July 2026  
**Final external QA:** Wednesday, 29 July 2026

## Planning model

- 27 development tasks, 177 planned focused hours (70.2% of 252 theoretical hours).
- Required reading replaces repeated Scrum essays; every early task produces a practical repository artifact.
- MP-014 is the first end-to-end vertical slice and must pass before MP-019 completes the game loop.
- Cross-team QA remains six parallel manual sanity checks on the frozen release candidate on 29 July.

## Execution sequence

1. **14 July — operational start:** MP-001–MP-003 verify the board, scope, contracts, branches, PRs, and review flow.
2. **14–16 July — executable learning:** MP-004–MP-007 produce runnable Flask, MediaPipe, camera/fallback, and movement-specification artifacts.
3. **16–21 July — component foundations:** MP-008–MP-013 establish structure, UI, API, services, fixtures, and pose normalization.
4. **21–22 July — early vertical slice:** MP-014 proves one sample-input → API → pose/mock → rule → visible-feedback path.
5. **22–27 July — feature completion:** MP-015–MP-023 finish movements, scoring, session, accessibility, CI, integration, and documentation.
6. **28 July — release candidate:** MP-024–MP-026 freeze, rehearse, and prepare safe fallback evidence.
7. **29 July — external QA:** MP-028–MP-033 run in parallel against the same commit; defects become separate issues.

## Sprint tasks

| ID | Title | Owner | Contributors | Reviewer | Hours | Start | Target |
|---|---|---|---|---|---:|---|---|
| MP-001 | Sprint operations setup, board readiness, and practical working agreement | alaamadii | — | IslamOuda85 | 3 | 2026-07-14 | 2026-07-14 |
| MP-002 | MVP acceptance map, demo scenarios, and safe product wording | IslamOuda85 | — | alaamadii | 5 | 2026-07-14 | 2026-07-15 |
| MP-003 | First useful pull requests and peer-review rotation | alaamadii | IslamOuda85, AhmadKollab, myarnwas, JHT127, fatimarajab12 | Tojan-Naiem | 5 | 2026-07-14 | 2026-07-15 |
| MP-004 | Executable Flask vertical-slice spike and architecture decision | AhmadKollab | — | alaamadii | 6 | 2026-07-14 | 2026-07-15 |
| MP-005 | Executable pose spike, offline fixture, and computer-vision service contract | myarnwas | IslamOuda85 | AhmadKollab | 6 | 2026-07-14 | 2026-07-15 |
| MP-006 | Clickable game-flow prototype and camera/fallback browser probe | JHT127 | — | IslamOuda85 | 6 | 2026-07-14 | 2026-07-15 |
| MP-007 | Movement acceptance matrix, executable landmark schema, and evaluation plan | fatimarajab12 | IslamOuda85 | JHT127 | 6 | 2026-07-15 | 2026-07-16 |
| MP-008 | Repository skeleton, dependencies, and Flask application factory | AhmadKollab | — | alaamadii | 6 | 2026-07-16 | 2026-07-17 |
| MP-009 | Initial README, contribution guide, privacy, and limitations | IslamOuda85 | — | fatimarajab12 | 6 | 2026-07-16 | 2026-07-20 |
| MP-010 | Frame/upload API, input validation, and safe error handling | AhmadKollab | — | fatimarajab12 | 6 | 2026-07-17 | 2026-07-20 |
| MP-011 | Base game interface, avatar presentation, and accessible navigation | JHT127 | — | IslamOuda85 | 7 | 2026-07-17 | 2026-07-21 |
| MP-012 | Browser webcam capture and mandatory fallback sample mode | JHT127 | — | alaamadii | 8 | 2026-07-20 | 2026-07-22 |
| MP-013 | Pose service, landmark normalization, and visibility checks | myarnwas | — | AhmadKollab | 8 | 2026-07-17 | 2026-07-21 |
| MP-014 | First vertical slice: sample input to visible raise-arms feedback | myarnwas | AhmadKollab, JHT127, fatimarajab12 | alaamadii | 7 | 2026-07-21 | 2026-07-22 |
| MP-015 | Side-reach left/right rules, feedback, and tests | myarnwas | fatimarajab12 | AhmadKollab | 7 | 2026-07-22 | 2026-07-23 |
| MP-016 | Knee-lift or step-in-place rule, feedback, and tests | fatimarajab12 | myarnwas | alaamadii | 7 | 2026-07-22 | 2026-07-23 |
| MP-017 | Friendly feedback orchestration and points/star scoring | fatimarajab12 | — | IslamOuda85 | 7 | 2026-07-23 | 2026-07-24 |
| MP-018 | Session state and end-of-session summary | AhmadKollab | fatimarajab12 | JHT127 | 7 | 2026-07-23 | 2026-07-24 |
| MP-019 | End-to-end game loop integration | JHT127 | AhmadKollab | fatimarajab12 | 8 | 2026-07-23 | 2026-07-27 |
| MP-020 | Adult-only calibration protocol, consent template, and landmark extraction | IslamOuda85 | fatimarajab12 | myarnwas | 7 | 2026-07-21 | 2026-07-24 |
| MP-021 | Landmark fixtures, threshold calibration, and rule evaluation report | fatimarajab12 | myarnwas | JHT127 | 8 | 2026-07-23 | 2026-07-27 |
| MP-022 | Windows/Linux CI with lint, tests, compile, and Flask smoke check | alaamadii | AhmadKollab | fatimarajab12 | 8 | 2026-07-20 | 2026-07-24 |
| MP-023 | Security, privacy, accessibility, and error-message hardening | IslamOuda85 | alaamadii, JHT127 | myarnwas | 7 | 2026-07-24 | 2026-07-27 |
| MP-024 | Integration regression, release-candidate freeze, and QA handoff | alaamadii | AhmadKollab, myarnwas, JHT127 | IslamOuda85 | 8 | 2026-07-27 | 2026-07-28 |
| MP-025 | Final-day QA triage, targeted fixes, retest, and release decision | alaamadii | IslamOuda85, AhmadKollab, myarnwas, JHT127, fatimarajab12 | Tojan-Naiem | 7 | 2026-07-29 | 2026-07-29 |
| MP-026 | Final README, demonstration package, contribution record, and retrospective | IslamOuda85 | alaamadii | JHT127 | 7 | 2026-07-29 | 2026-07-29 |
| MP-027 | Maintain Sprint board, blocker log, and instructor-checkpoint evidence | alaamadii | — | IslamOuda85 | 4 | 2026-07-14 | 2026-07-29 |

## Final-day QA

| ID | Title | Owner | Contributors | Reviewer | Hours | Start | Target |
|---|---|---|---|---|---:|---|---|
| MP-028 | Final-day manual QA: clean installation, startup, and README sanity | Tojan-Naiem | — | alaamadii | 3.5 | 2026-07-29 | 2026-07-29 |
| MP-029 | Final-day manual QA: camera permission, no-camera, browser, and fallback sanity | SajaZenaty | — | JHT127 | 3.5 | 2026-07-29 | 2026-07-29 |
| MP-030 | Final-day manual QA: pose visibility and three-movement sanity | nezarYousef | — | myarnwas | 3.5 | 2026-07-29 | 2026-07-29 |
| MP-031 | Final-day manual QA: feedback, scoring, repeated session, reset, and summary | saliqasarwi | — | fatimarajab12 | 3.5 | 2026-07-29 | 2026-07-29 |
| MP-032 | Final-day manual QA: invalid input, oversized file, errors, privacy, and disclaimer | SaadRayh | — | AhmadKollab | 3.5 | 2026-07-29 | 2026-07-29 |
| MP-033 | Final-day manual QA: responsive accessibility sanity and consolidated QA report | BaraahMazeen | — | IslamOuda85 | 3.5 | 2026-07-29 | 2026-07-29 |
