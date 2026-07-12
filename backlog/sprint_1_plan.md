# MovePal Sprint 1 plan

**Kickoff:** 13 July 2026  
**Sprint:** 14–29 July 2026  
**Final external QA day:** 29 July 2026

All product backlog issues are imported at bootstrap. Only the tasks below are assigned for Sprint 1. Team A manual QA begins only after MP-024 freezes the release candidate.

## Development tasks

| ID | Title | Owner | Contributors | Reviewer | Hours | Target |
|---|---|---|---|---|---:|---|
| MP-001 | Kickoff, Sprint Goal, and Scrum working agreement | alaamadii | — | IslamOuda85 | 4 | 2026-07-14 |
| MP-002 | Product vision, user stories, MVP boundary, and ethical framing | IslamOuda85 | — | alaamadii | 6 | 2026-07-15 |
| MP-003 | Git, GitHub, pull-request, and review rehearsal | alaamadii | IslamOuda85, AhmadKollab, myarnwas, JHT127, MennaAllah-Alatrsh | Tojan-Naiem | 6 | 2026-07-15 |
| MP-004 | Flask application-factory learning spike and architecture decision | AhmadKollab | — | alaamadii | 6 | 2026-07-15 |
| MP-005 | MediaPipe Pose learning spike and computer-vision service contract | myarnwas | IslamOuda85 | AhmadKollab | 6 | 2026-07-15 |
| MP-006 | Game UX, webcam permission, and fallback-flow design spike | JHT127 | — | IslamOuda85 | 6 | 2026-07-15 |
| MP-007 | Movement specifications, landmark schema, and evaluation plan | MennaAllah-Alatrsh | IslamOuda85 | JHT127 | 6 | 2026-07-16 |
| MP-008 | Repository skeleton, dependencies, and Flask application factory | AhmadKollab | — | alaamadii | 6 | 2026-07-17 |
| MP-009 | Initial README, contribution guide, privacy, and limitations | IslamOuda85 | — | MennaAllah-Alatrsh | 6 | 2026-07-20 |
| MP-010 | Frame/upload API, input validation, and safe error handling | AhmadKollab | — | MennaAllah-Alatrsh | 6 | 2026-07-20 |
| MP-011 | Base game interface, avatar presentation, and accessible navigation | JHT127 | — | IslamOuda85 | 7 | 2026-07-21 |
| MP-012 | Browser webcam capture and mandatory fallback sample mode | JHT127 | — | alaamadii | 8 | 2026-07-22 |
| MP-013 | Pose service, landmark normalization, and visibility checks | myarnwas | — | AhmadKollab | 8 | 2026-07-21 |
| MP-014 | Raise-both-arms rule, feedback mapping, and tests | myarnwas | MennaAllah-Alatrsh | JHT127 | 7 | 2026-07-22 |
| MP-015 | Side-reach left/right rules, feedback, and tests | myarnwas | MennaAllah-Alatrsh | AhmadKollab | 7 | 2026-07-23 |
| MP-016 | Knee-lift or step-in-place rule, feedback, and tests | MennaAllah-Alatrsh | myarnwas | alaamadii | 7 | 2026-07-23 |
| MP-017 | Friendly feedback orchestration and points/star scoring | MennaAllah-Alatrsh | — | IslamOuda85 | 7 | 2026-07-24 |
| MP-018 | Session state and end-of-session summary | AhmadKollab | MennaAllah-Alatrsh | JHT127 | 7 | 2026-07-24 |
| MP-019 | End-to-end game loop integration | JHT127 | AhmadKollab | MennaAllah-Alatrsh | 8 | 2026-07-27 |
| MP-020 | Adult-only calibration protocol, consent template, and landmark extraction | IslamOuda85 | MennaAllah-Alatrsh | myarnwas | 7 | 2026-07-24 |
| MP-021 | Landmark fixtures, threshold calibration, and rule evaluation report | MennaAllah-Alatrsh | myarnwas | JHT127 | 8 | 2026-07-27 |
| MP-022 | Windows/Linux CI with lint, tests, compile, and Flask smoke check | alaamadii | AhmadKollab | MennaAllah-Alatrsh | 8 | 2026-07-24 |
| MP-023 | Security, privacy, accessibility, and error-message hardening | IslamOuda85 | alaamadii, JHT127 | myarnwas | 7 | 2026-07-27 |
| MP-024 | Integration regression, release-candidate freeze, and QA handoff | alaamadii | AhmadKollab, myarnwas, JHT127 | IslamOuda85 | 8 | 2026-07-28 |
| MP-025 | Final-day QA triage, targeted fixes, retest, and release decision | alaamadii | IslamOuda85, AhmadKollab, myarnwas, JHT127, MennaAllah-Alatrsh | Tojan-Naiem | 7 | 2026-07-29 |
| MP-026 | Final README, demonstration package, contribution record, and retrospective | IslamOuda85 | alaamadii | JHT127 | 7 | 2026-07-29 |
| MP-027 | Sprint rituals and instructor checkpoint checklist | alaamadii | — | IslamOuda85 | 4 | 2026-07-29 |

## Final-day manual QA

| ID | Manual sanity area | QA member | Team B contact/reviewer | Hours |
|---|---|---|---|---:|
| MP-028 | Final-day manual QA: clean installation, startup, and README sanity | Tojan-Naiem | alaamadii | 3.5 |
| MP-029 | Final-day manual QA: camera permission, no-camera, browser, and fallback sanity | SajaZenaty | JHT127 | 3.5 |
| MP-030 | Final-day manual QA: pose visibility and three-movement sanity | nezarYousef | myarnwas | 3.5 |
| MP-031 | Final-day manual QA: feedback, scoring, repeated session, reset, and summary | saliqasarwi | MennaAllah-Alatrsh | 3.5 |
| MP-032 | Final-day manual QA: invalid input, oversized file, errors, privacy, and disclaimer | SaadRayh | AhmadKollab | 3.5 |
| MP-033 | Final-day manual QA: responsive accessibility sanity and consolidated QA report | BaraahMazeen | IslamOuda85 | 3.5 |

## QA rule

Team A tests the frozen MP-024 commit manually. QA tasks do not contain feature implementation. Each failure becomes a separate bug issue with environment, reproduction steps, expected/actual result, severity, evidence, affected commit, and retest result. MP-025 owns Team B triage and fixes.
