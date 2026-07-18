# MovePal enhanced product backlog

**Tasks:** 63 — 27 Sprint 1 development, 6 final-day manual QA, 30 later backlog.

The authoritative detailed issue bodies are stored in `product_backlog.json`. Every task includes required reading, a practical first output, detailed work sequence, dependency rationale, explicit beginner effort breakdown, acceptance criteria, Definition of Done, ownership, verification, risks, privacy, and evidence.

## MP-001 — Sprint operations setup, board readiness, and practical working agreement

- **Sprint:** sprint-1
- **Owner:** alaamadii
- **Estimate:** 3 h
- **Dependencies:** None
- **Practical first output:** Verified Sprint 1 board with correct assignments and visible dates

Turn the instructor-led kickoff into an operational Sprint workspace. The Scrum Master verifies that students can find their work, understand the board, request reviews, and report blockers without spending Sprint time rewriting Scrum theory.

## MP-002 — MVP acceptance map, demo scenarios, and safe product wording

- **Sprint:** sprint-1
- **Owner:** IslamOuda85
- **Estimate:** 5 h
- **Dependencies:** MP-001
- **Practical first output:** `docs/mvp_acceptance_map.md` mapping capabilities to evidence and owners

Convert the already-defined MovePal scope into testable acceptance examples, user-facing wording, and final-demo scenarios that implementation and QA can use directly.

## MP-003 — First useful pull requests and peer-review rotation

- **Sprint:** sprint-1
- **Owner:** alaamadii
- **Estimate:** 5 h
- **Dependencies:** MP-001
- **Practical first output:** One useful merged contribution from each development member

Verify the GitHub workflow through small changes that improve the real repository, rather than disposable practice work.

## MP-004 — Executable Flask vertical-slice spike and architecture decision

- **Sprint:** sprint-1
- **Owner:** AhmadKollab
- **Estimate:** 6 h
- **Dependencies:** MP-002, MP-003
- **Practical first output:** Executable page and JSON route in the real repository

Prove the selected Flask structure inside the real repository with a tiny executable page, JSON endpoint, and test, then document why the structure is sufficient.

## MP-005 — Executable pose spike, offline fixture, and computer-vision service contract

- **Sprint:** sprint-1
- **Owner:** myarnwas
- **Estimate:** 6 h
- **Dependencies:** MP-002, MP-003
- **Practical first output:** Reusable pose adapter or service-contract spike

Prove MediaPipe Pose compatibility and commit a mockable result contract and tiny landmark fixture that implementation and CI can use immediately.

## MP-006 — Clickable game-flow prototype and camera/fallback browser probe

- **Sprint:** sprint-1
- **Owner:** JHT127
- **Estimate:** 6 h
- **Dependencies:** MP-002, MP-003
- **Practical first output:** Clickable low-fidelity game flow in Jinja/static assets

Produce a reusable browser prototype that validates the complete interaction flow and the camera/fallback decision before final UI implementation.

## MP-007 — Movement acceptance matrix, executable landmark schema, and evaluation plan

- **Sprint:** sprint-1
- **Owner:** fatimarajab12
- **Estimate:** 6 h
- **Dependencies:** MP-005, MP-006
- **Practical first output:** Updated `docs/movement_specification.md`

Turn the three movement ideas into machine-readable examples and testable acceptance rules before movement implementation begins.

## MP-008 — Repository skeleton, dependencies, and Flask application factory

- **Sprint:** sprint-1
- **Owner:** AhmadKollab
- **Estimate:** 6 h
- **Dependencies:** MP-004
- **Practical first output:** Working Flask package and `run.py`

Turn the architecture spike into the production Sprint 1 skeleton. Establish installable dependencies, the Flask factory, configuration, routes/services/templates/static boundaries, and cross-platform startup before feature branches diverge. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## MP-009 — Initial README, contribution guide, privacy, and limitations

- **Sprint:** sprint-1
- **Owner:** IslamOuda85
- **Estimate:** 6 h
- **Dependencies:** MP-002, MP-008
- **Practical first output:** `README.md`

Create the documentation baseline that lets a beginner install, run, contribute, and understand MovePal’s limits before the implementation is complete. Documentation is versioned with the code and updated throughout the sprint. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## MP-010 — Frame/upload API, input validation, and safe error handling

- **Sprint:** sprint-1
- **Owner:** AhmadKollab
- **Estimate:** 6 h
- **Dependencies:** MP-008, MP-005, MP-006
- **Practical first output:** Validated frame/upload endpoint

Implement the backend boundary that receives a periodically captured frame or permitted fallback file and returns structured JSON. Keep validation and errors predictable so frontend, pose service, tests, and QA can work independently. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## MP-011 — Base game interface, avatar presentation, and accessible navigation

- **Sprint:** sprint-1
- **Owner:** JHT127
- **Estimate:** 7 h
- **Dependencies:** MP-006, MP-008
- **Practical first output:** Jinja templates

Build the reusable child-friendly page structure and visual language for MovePal. Deliver activity selection, instructions, avatar/toy placeholder, feedback area, score area, camera/fallback controls, and summary container without coupling layout to pose logic. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## MP-012 — Browser webcam capture and mandatory fallback sample mode

- **Sprint:** sprint-1
- **Owner:** JHT127
- **Estimate:** 8 h
- **Dependencies:** MP-010, MP-011
- **Practical first output:** Camera capture JavaScript

Implement browser camera permission and periodic still-frame capture while preserving a first-class fallback mode for machines, browsers, or demo rooms where a webcam is unavailable. This is deliberately not low-latency streaming. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## MP-013 — Pose service, landmark normalization, and visibility checks

- **Sprint:** sprint-1
- **Owner:** myarnwas
- **Estimate:** 8 h
- **Dependencies:** MP-005, MP-008, MP-010, MP-007
- **Practical first output:** `app/services/pose_tracking.py` implementation

Implement the isolated computer-vision service agreed in the spike. Convert image input into a small normalized domain representation that movement rules can consume and that tests can replace with fixtures. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## MP-014 — First vertical slice: sample input to visible raise-arms feedback

- **Sprint:** sprint-1
- **Owner:** myarnwas
- **Estimate:** 7 h
- **Dependencies:** MP-007, MP-010, MP-011, MP-013
- **Practical first output:** Raise-arms rule function

Prove early that the frontend/backend/computer-vision contracts can work together. Use a deterministic sample or landmark fixture to travel through the Flask API, pose/mock service, raise-both-arms rule, friendly feedback mapping, and a minimal visible result. This reduces late integration risk while still keeping the task small enough for beginners.

## MP-015 — Side-reach left/right rules, feedback, and tests

- **Sprint:** sprint-1
- **Owner:** myarnwas
- **Estimate:** 7 h
- **Dependencies:** MP-007, MP-013, MP-014
- **Practical first output:** Side-reach rule for both directions

Implement side reach with explicit left and right variants, consistent camera/user-side semantics, and feedback for insufficient reach, bent posture where represented, low visibility, and success. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## MP-016 — Knee-lift or step-in-place rule, feedback, and tests

- **Sprint:** sprint-1
- **Owner:** fatimarajab12
- **Estimate:** 7 h
- **Dependencies:** MP-007, MP-013, MP-014
- **Practical first output:** Knee-lift evaluator

Implement the third movement rule using relative knee/hip/ankle geometry and visibility checks. Support either leg so the activity remains simple and inclusive for the prototype. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## MP-017 — Friendly feedback orchestration and points/star scoring

- **Sprint:** sprint-1
- **Owner:** fatimarajab12
- **Estimate:** 7 h
- **Dependencies:** MP-014, MP-015, MP-016, MP-002
- **Practical first output:** Feedback service

Create the game-level feedback and reward service that turns rule observations into consistent messages, awards points/stars once per successful attempt, and avoids punitive or medical wording. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## MP-018 — Session state and end-of-session summary

- **Sprint:** sprint-1
- **Owner:** AhmadKollab
- **Estimate:** 7 h
- **Dependencies:** MP-008, MP-017
- **Practical first output:** Session-state service

Implement lightweight in-memory or browser-backed session state for selected activities, attempts, successes, points, and a short summary. Avoid authentication and a database while keeping state behavior testable and resettable. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## MP-019 — End-to-end game loop integration

- **Sprint:** sprint-1
- **Owner:** JHT127
- **Estimate:** 8 h
- **Dependencies:** MP-010, MP-011, MP-012, MP-013, MP-014, MP-015, MP-016, MP-017, MP-018
- **Practical first output:** Complete playable web flow

Connect activity selection, avatar/instructions, camera or fallback input, backend processing, movement rules, feedback, scoring, and session summary into one coherent user flow. This issue owns integration, not rewriting feature modules. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## MP-020 — Adult-only calibration protocol, consent template, and landmark extraction

- **Sprint:** sprint-1
- **Owner:** IslamOuda85
- **Estimate:** 7 h
- **Dependencies:** MP-007, MP-013, MP-009
- **Practical first output:** `docs/consent_template.md`

Prepare a small, ethically bounded calibration/testing process using adults only. The task focuses on consent, collection instructions, private raw-data separation, and derived landmark extraction; it does not require a large dataset or publication of recordings. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## MP-021 — Landmark fixtures, threshold calibration, and rule evaluation report

- **Sprint:** sprint-1
- **Owner:** fatimarajab12
- **Estimate:** 8 h
- **Dependencies:** MP-014, MP-015, MP-016, MP-020
- **Practical first output:** Versioned anonymized landmark fixtures

Build the deterministic fixture set used by tests and evaluate the three heuristic rules on correct, near-correct, incorrect, low-visibility, and framing cases. Adjust thresholds transparently without claiming validated accuracy. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## MP-022 — Windows/Linux CI with lint, tests, compile, and Flask smoke check

- **Sprint:** sprint-1
- **Owner:** alaamadii
- **Estimate:** 8 h
- **Dependencies:** MP-008, MP-013, MP-014, MP-015, MP-016, MP-018
- **Practical first output:** `.github/workflows/ci.yml`

Implement a beginner-readable GitHub Actions workflow that validates portable Python code on Windows and Linux without cameras, large datasets, private recordings, or model downloads. Treat CI as student-owned product work. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## MP-023 — Security, privacy, accessibility, and error-message hardening

- **Sprint:** sprint-1
- **Owner:** IslamOuda85
- **Estimate:** 7 h
- **Dependencies:** MP-010, MP-011, MP-012, MP-019, MP-009
- **Practical first output:** Hardening checklist and findings

Review the integrated application against Sprint 1 safeguards before release-candidate freeze. Fix high-value issues in input handling, logging, data retention, disclaimer visibility, keyboard use, responsive layout, and user-facing errors. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## MP-024 — Integration regression, release-candidate freeze, and QA handoff

- **Sprint:** sprint-1
- **Owner:** alaamadii
- **Estimate:** 8 h
- **Dependencies:** MP-019, MP-021, MP-022, MP-023
- **Practical first output:** Release-candidate commit/tag or documented SHA

Create a stable release candidate for final-day external QA. Merge only reviewed work, run the complete deterministic journey, freeze the tested commit, and provide a precise manual QA handoff package. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## MP-025 — Final-day QA triage, targeted fixes, retest, and release decision

- **Sprint:** sprint-1
- **Owner:** alaamadii
- **Estimate:** 7 h
- **Dependencies:** MP-024
- **Practical first output:** QA triage table

During the final QA day, receive manual findings from MP-028 through MP-033, classify them consistently, fix only release-critical or safely bounded defects, request retest, and record the release decision. The QA issues are related evidence rather than formal dependencies so all QA can execute in parallel from MP-024. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## MP-026 — Final README, demonstration package, contribution record, and retrospective

- **Sprint:** sprint-1
- **Owner:** IslamOuda85
- **Estimate:** 7 h
- **Dependencies:** MP-025
- **Practical first output:** Final `README.md` and linked docs

Finish the course-facing package after final QA: reproducible README, live-camera and fallback demo script, contribution/review evidence, limitations, release notes, and a short retrospective focused on Scrum learning. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## MP-027 — Maintain Sprint board, blocker log, and instructor-checkpoint evidence

- **Sprint:** sprint-1
- **Owner:** alaamadii
- **Estimate:** 4 h
- **Dependencies:** MP-001
- **Practical first output:** Maintained Sprint Rituals issue

Keep the board synchronized with real work and use short Scrum events to remove blockers and rebalance work, without producing repetitive meeting documentation.

## MP-028 — Final-day manual QA: clean installation, startup, and README sanity

- **Sprint:** sprint-1
- **Owner:** Tojan-Naiem
- **Estimate:** 3.5 h
- **Dependencies:** MP-024
- **Practical first output:** Completed installation/startup checklist

Independently verify that a beginner can obtain the frozen MovePal release candidate, create a clean environment, install dependencies, run tests, start Flask, and reach the application by following only the documented instructions. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## MP-029 — Final-day manual QA: camera permission, no-camera, browser, and fallback sanity

- **Sprint:** sprint-1
- **Owner:** SajaZenaty
- **Estimate:** 3.5 h
- **Dependencies:** MP-024
- **Practical first output:** Permission/fallback matrix

Verify that camera use is understandable and recoverable across permission granted, denied, unavailable, unsupported, or insecure-context situations, and that fallback mode remains fully usable. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## MP-030 — Final-day manual QA: pose visibility and three-movement sanity

- **Sprint:** sprint-1
- **Owner:** nezarYousef
- **Estimate:** 3.5 h
- **Dependencies:** MP-024
- **Practical first output:** Movement/condition QA matrix

Exercise pose and rule behavior for raise both arms, side reach left/right, and knee lift using included samples and, where safe, an adult tester. Focus on correct/incorrect, low-light, partial-body, multiple-person, side-direction, and low-confidence outcomes. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## MP-031 — Final-day manual QA: feedback, scoring, repeated session, reset, and summary

- **Sprint:** sprint-1
- **Owner:** saliqasarwi
- **Estimate:** 3.5 h
- **Dependencies:** MP-024
- **Practical first output:** State/scoring test log

Verify that feedback is friendly and consistent, points/stars are awarded correctly, repeated frames do not inflate scores, session restart/reset works, and the final summary matches the performed activities. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## MP-032 — Final-day manual QA: invalid input, oversized file, errors, privacy, and disclaimer

- **Sprint:** sprint-1
- **Owner:** SaadRayh
- **Estimate:** 3.5 h
- **Dependencies:** MP-024
- **Practical first output:** Negative-input matrix

Verify defensive behavior and visible privacy boundaries. Test malformed, unsupported, and oversized inputs, server/client errors, logging exposure, camera explanation, data-retention wording, and non-medical disclaimer visibility. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## MP-033 — Final-day manual QA: responsive accessibility sanity and consolidated QA report

- **Sprint:** sprint-1
- **Owner:** BaraahMazeen
- **Estimate:** 3.5 h
- **Dependencies:** MP-024
- **Practical first output:** Responsive/accessibility checklist

Run final responsive, keyboard, readability, browser-width, and end-to-end sanity checks, then consolidate Team A findings into a release-oriented QA summary without replacing the individual defect issues. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## MP-034 — Cross-browser compatibility baseline and support matrix

- **Sprint:** post-sprint
- **Owner:** Unassigned
- **Estimate:** 12 h
- **Dependencies:** MP-024
- **Practical first output:** Browser support policy

Define and verify a realistic browser support policy beyond the final-day sanity checks, including camera API behavior, upload fallback, CSS/JavaScript compatibility, and documented unsupported cases. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## MP-035 — Performance profiling and response-time budget

- **Sprint:** post-sprint
- **Owner:** Unassigned
- **Estimate:** 14 h
- **Dependencies:** MP-024
- **Practical first output:** Profiling report

Measure where time and memory are spent in image decoding, pose inference, rule evaluation, API serialization, and browser requests, then define a practical prototype performance budget. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## MP-036 — Production-like local packaging and configuration

- **Sprint:** post-sprint
- **Owner:** Unassigned
- **Estimate:** 12 h
- **Dependencies:** MP-024, MP-035
- **Practical first output:** Production-like run configuration

Create a reproducible non-debug way to run MovePal locally for demonstrations or controlled deployment, with environment-based configuration, a production WSGI server, and clear separation from developer settings. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## MP-037 — Persistent session storage design

- **Sprint:** post-sprint
- **Owner:** Unassigned
- **Estimate:** 16 h
- **Dependencies:** MP-018, MP-023
- **Practical first output:** Persistence ADR

Investigate and implement optional persistence for anonymous session summaries without introducing accounts. Define retention, deletion, schema, concurrency, and migration behavior before replacing Sprint 1 ephemeral state. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## MP-038 — SQLite migration and data-access layer

- **Sprint:** post-sprint
- **Owner:** Unassigned
- **Estimate:** 18 h
- **Dependencies:** MP-037
- **Practical first output:** SQLite schema/migrations

If persistent structured data is approved, introduce SQLite through a small data-access layer with schema migration and tests rather than allowing SQL in routes. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## MP-039 — Localization architecture and message catalog

- **Sprint:** future
- **Owner:** Unassigned
- **Estimate:** 14 h
- **Dependencies:** MP-024
- **Practical first output:** Localization ADR

Move user-facing text out of templates/services into a maintainable localization approach so English remains complete and additional languages can be added consistently. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## MP-040 — Arabic translation and right-to-left interface

- **Sprint:** future
- **Owner:** Unassigned
- **Estimate:** 18 h
- **Dependencies:** MP-039
- **Practical first output:** Arabic catalog

Add a reviewed Arabic experience after localization architecture exists, including right-to-left layout, movement/side terminology, feedback, errors, privacy, and disclaimer content. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## MP-041 — Accessibility audit and remediation plan

- **Sprint:** future
- **Owner:** Unassigned
- **Estimate:** 20 h
- **Dependencies:** MP-024
- **Practical first output:** Accessibility audit report

Go beyond Sprint 1 sanity checks with a structured accessibility audit covering keyboard, focus, semantics, status messages, contrast, reduced motion, zoom, responsive layout, and assistive-technology behavior. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## MP-042 — Progressive Web App and offline fallback investigation

- **Sprint:** optional
- **Owner:** Unassigned
- **Estimate:** 16 h
- **Dependencies:** MP-024, MP-035
- **Practical first output:** PWA feasibility ADR

Investigate whether a lightweight PWA improves classroom/demo reliability, especially for static UI and bundled fallback samples, while documenting camera/model/server limitations offline. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## MP-043 — Declarative custom-movement specification

- **Sprint:** future
- **Owner:** Unassigned
- **Estimate:** 24 h
- **Dependencies:** MP-014, MP-015, MP-016
- **Practical first output:** Movement schema

Design a safe configuration format for adding simple landmark-based movements without editing core Python code, while validating allowed joints, thresholds, sides, feedback keys, and test fixtures. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## MP-044 — Educator-configured activity session

- **Sprint:** future
- **Owner:** Unassigned
- **Estimate:** 22 h
- **Dependencies:** MP-018, MP-043
- **Practical first output:** Session configuration model/UI

Allow an authorized local educator/facilitator to choose movement order, repetitions, difficulty preset, and session length without introducing user accounts or medical treatment plans. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## MP-045 — Difficulty presets and adaptive thresholds investigation

- **Sprint:** future
- **Owner:** Unassigned
- **Estimate:** 24 h
- **Dependencies:** MP-021, MP-044
- **Practical first output:** Difficulty/adaptation ADR

Investigate transparent difficulty presets or bounded adaptive thresholds without claiming personalization, diagnosis, or validated rehabilitation. Preserve explainability and user control. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## MP-046 — Expanded reward mechanics and session progression

- **Sprint:** future
- **Owner:** Unassigned
- **Estimate:** 18 h
- **Dependencies:** MP-017, MP-018
- **Practical first output:** Reward design specification

Explore additional non-manipulative game mechanics such as badges, streaks, levels, and encouraging progress while keeping the experience short, optional, and understandable. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## MP-047 — Avatar animation and asset pipeline

- **Sprint:** future
- **Owner:** Unassigned
- **Estimate:** 20 h
- **Dependencies:** MP-011
- **Practical first output:** Asset/licensing inventory

Replace the static toy/avatar with lightweight movement demonstrations using original or properly licensed assets, an explicit asset pipeline, fallbacks, and accessibility controls. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## MP-048 — Optional low-latency streaming feasibility study

- **Sprint:** optional
- **Owner:** Unassigned
- **Estimate:** 28 h
- **Dependencies:** MP-035
- **Practical first output:** Streaming feasibility ADR

Evaluate whether WebSockets, WebRTC, or another streaming design provides enough benefit over periodic frames to justify substantial complexity. This remains optional and cannot invalidate the simple Sprint 1 path. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## MP-049 — Pose model and library version-management policy

- **Sprint:** post-sprint
- **Owner:** Unassigned
- **Estimate:** 14 h
- **Dependencies:** MP-021, MP-022
- **Practical first output:** Version-management policy

Establish a repeatable process for pinning, testing, upgrading, and documenting MediaPipe/OpenCV/Flask dependencies so model or API changes do not silently alter movement behavior. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## MP-050 — Structured logging and privacy-safe observability

- **Sprint:** post-sprint
- **Owner:** Unassigned
- **Estimate:** 16 h
- **Dependencies:** MP-023, MP-036
- **Practical first output:** Observability specification

Add minimal structured operational logs and health indicators that help diagnose failures without recording frames, landmarks, identities, or sensitive browser details. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## MP-051 — Threat model and automated security checks

- **Sprint:** future
- **Owner:** Unassigned
- **Estimate:** 22 h
- **Dependencies:** MP-023, MP-049
- **Practical first output:** Threat model

Create a lightweight threat model for browser camera input, file upload, Flask endpoints, dependencies, configuration, and future deployment, then add proportionate automated checks without claiming a full security audit. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## MP-052 — Data retention, withdrawal, and deletion workflow

- **Sprint:** future
- **Owner:** Unassigned
- **Estimate:** 14 h
- **Dependencies:** MP-020, MP-037
- **Practical first output:** Data inventory

Turn privacy promises into an operational procedure for any future adult-volunteer raw recordings, derived landmarks, and persisted anonymous summaries, including retention periods, access, withdrawal, deletion, and verification. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## MP-053 — Expanded adult-only dataset and bias analysis

- **Sprint:** future
- **Owner:** Unassigned
- **Estimate:** 36 h
- **Dependencies:** MP-020, MP-021, MP-052
- **Practical first output:** Updated dataset card

Design a larger but still bounded adult-only landmark dataset covering body proportions, clothing, camera distance, lighting, left/right, correct/incorrect examples, and known limitations, with consent and privacy controls. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## MP-054 — Evaluation metrics and reproducible benchmark suite

- **Sprint:** future
- **Owner:** Unassigned
- **Estimate:** 24 h
- **Dependencies:** MP-021, MP-053
- **Practical first output:** Benchmark specification

Define and implement a reproducible benchmark for rule outcomes, visibility handling, latency, and user-flow reliability using approved landmark/image fixtures, with metrics matched to the actual prototype claims. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## MP-055 — Multiple-person detection and guidance

- **Sprint:** future
- **Owner:** Unassigned
- **Estimate:** 20 h
- **Dependencies:** MP-013, MP-054
- **Practical first output:** Multiple-person ADR

Investigate how the selected pose solution behaves when multiple people are visible and implement explicit guidance or safe rejection rather than silently scoring the wrong person. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## MP-056 — Low-light and framing robustness improvements

- **Sprint:** future
- **Owner:** Unassigned
- **Estimate:** 22 h
- **Dependencies:** MP-013, MP-054
- **Practical first output:** Condition-detection helpers

Improve feedback and preprocessing for common low-light, distance, crop, orientation, and framing problems using measurable heuristics while avoiding expensive enhancement pipelines. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## MP-057 — API contract documentation and schema validation

- **Sprint:** post-sprint
- **Owner:** Unassigned
- **Estimate:** 16 h
- **Dependencies:** MP-010, MP-019
- **Practical first output:** API schema/documentation

Formalize the browser–Flask API using machine-readable schemas and examples, then validate requests/responses so frontend/backend changes fail early and remain understandable to students. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## MP-058 — Controlled cloud deployment investigation

- **Sprint:** future
- **Owner:** Unassigned
- **Estimate:** 28 h
- **Dependencies:** MP-036, MP-050, MP-051
- **Practical first output:** Deployment ADR

Evaluate and document a small controlled deployment only after local production-like packaging, privacy, security, and performance work. Compare platforms, cost, HTTPS/camera behavior, resource limits, and data handling. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## MP-059 — Backup, restore, and recovery procedure

- **Sprint:** future
- **Owner:** Unassigned
- **Estimate:** 16 h
- **Dependencies:** MP-037, MP-052
- **Practical first output:** Backup/restore scripts

For any approved persistent configuration or anonymous session data, define backups, restore testing, version compatibility, corruption handling, and responsibility; keep the procedure proportionate to a prototype. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## MP-060 — Educator dashboard and aggregate session export

- **Sprint:** future
- **Owner:** Unassigned
- **Estimate:** 28 h
- **Dependencies:** MP-037, MP-044, MP-052
- **Practical first output:** Dashboard requirements/ADR

Investigate a local educator-facing overview of anonymous session results and export, with explicit purpose, minimal fields, retention, accessibility, and no child profiling or ranking. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## MP-061 — Release, compatibility, and deprecation policy

- **Sprint:** future
- **Owner:** Unassigned
- **Estimate:** 12 h
- **Dependencies:** MP-049, MP-057
- **Practical first output:** Release policy

Define versioning, release notes, supported Python/browser/dependency versions, data/config migration, deprecation warnings, and maintenance ownership for MovePal. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## MP-062 — Production-readiness evidence review

- **Sprint:** future
- **Owner:** Unassigned
- **Estimate:** 30 h
- **Dependencies:** MP-035, MP-041, MP-051, MP-052, MP-054, MP-058, MP-059, MP-061
- **Practical first output:** Readiness review report

Conduct a structured evidence review across functionality, security, privacy, accessibility, performance, deployment, maintenance, data governance, and incident/recovery readiness. This task decides readiness gaps; it does not declare clinical validity. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## MP-063 — Optional custom pose-model training research

- **Sprint:** optional
- **Owner:** Unassigned
- **Estimate:** 40 h
- **Dependencies:** MP-053, MP-054, MP-062
- **Practical first output:** Research proposal/ADR

Investigate custom model training only after the rule-based pretrained approach has a documented limitation that cannot be addressed more simply. Define data, labeling, compute, evaluation, bias, maintenance, and deployment implications before any training. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.
