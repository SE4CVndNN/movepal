# MovePal complete product backlog

All tasks are imported when the bootstrap is applied. Sprint 1 development and final-day QA tasks are assigned immediately; post-sprint, future, and optional tasks remain unassigned in Backlog until a later planning event.

- Total tasks: 63
- Sprint 1 development: 27
- Final-day manual QA: 6
- Post-sprint/future/optional: 30

| Position | ID | Title | Sprint | Team | Owner | Estimate | Dependencies |
|---:|---|---|---|---|---|---:|---|
| 1 | MP-001 | Kickoff, Sprint Goal, and Scrum working agreement | sprint-1 | MovePal Development | alaamadii | 4 h | — |
| 2 | MP-002 | Product vision, user stories, MVP boundary, and ethical framing | sprint-1 | MovePal Development | IslamOuda85 | 6 h | MP-001 |
| 3 | MP-003 | Git, GitHub, pull-request, and review rehearsal | sprint-1 | MovePal Development | alaamadii | 6 h | MP-001 |
| 4 | MP-004 | Flask application-factory learning spike and architecture decision | sprint-1 | MovePal Development | AhmadKollab | 6 h | MP-002, MP-003 |
| 5 | MP-005 | MediaPipe Pose learning spike and computer-vision service contract | sprint-1 | MovePal Development | myarnwas | 6 h | MP-002, MP-003 |
| 6 | MP-006 | Game UX, webcam permission, and fallback-flow design spike | sprint-1 | MovePal Development | JHT127 | 6 h | MP-002, MP-003 |
| 7 | MP-007 | Movement specifications, landmark schema, and evaluation plan | sprint-1 | MovePal Development | MennaAllah-Alatrsh | 6 h | MP-005, MP-006 |
| 8 | MP-008 | Repository skeleton, dependencies, and Flask application factory | sprint-1 | MovePal Development | AhmadKollab | 6 h | MP-004 |
| 9 | MP-009 | Initial README, contribution guide, privacy, and limitations | sprint-1 | MovePal Development | IslamOuda85 | 6 h | MP-002, MP-008 |
| 10 | MP-010 | Frame/upload API, input validation, and safe error handling | sprint-1 | MovePal Development | AhmadKollab | 6 h | MP-008, MP-005, MP-006 |
| 11 | MP-011 | Base game interface, avatar presentation, and accessible navigation | sprint-1 | MovePal Development | JHT127 | 7 h | MP-006, MP-008 |
| 12 | MP-012 | Browser webcam capture and mandatory fallback sample mode | sprint-1 | MovePal Development | JHT127 | 8 h | MP-010, MP-011 |
| 13 | MP-013 | Pose service, landmark normalization, and visibility checks | sprint-1 | MovePal Development | myarnwas | 8 h | MP-005, MP-008, MP-010, MP-007 |
| 14 | MP-014 | Raise-both-arms rule, feedback mapping, and tests | sprint-1 | MovePal Development | myarnwas | 7 h | MP-007, MP-013 |
| 15 | MP-015 | Side-reach left/right rules, feedback, and tests | sprint-1 | MovePal Development | myarnwas | 7 h | MP-007, MP-013, MP-014 |
| 16 | MP-016 | Knee-lift or step-in-place rule, feedback, and tests | sprint-1 | MovePal Development | MennaAllah-Alatrsh | 7 h | MP-007, MP-013, MP-014 |
| 17 | MP-017 | Friendly feedback orchestration and points/star scoring | sprint-1 | MovePal Development | MennaAllah-Alatrsh | 7 h | MP-014, MP-015, MP-016, MP-002 |
| 18 | MP-018 | Session state and end-of-session summary | sprint-1 | MovePal Development | AhmadKollab | 7 h | MP-008, MP-017 |
| 19 | MP-019 | End-to-end game loop integration | sprint-1 | MovePal Development | JHT127 | 8 h | MP-010, MP-011, MP-012, MP-013, MP-014, MP-015, MP-016, MP-017, MP-018 |
| 20 | MP-020 | Adult-only calibration protocol, consent template, and landmark extraction | sprint-1 | MovePal Development | IslamOuda85 | 7 h | MP-007, MP-013, MP-009 |
| 21 | MP-021 | Landmark fixtures, threshold calibration, and rule evaluation report | sprint-1 | MovePal Development | MennaAllah-Alatrsh | 8 h | MP-014, MP-015, MP-016, MP-020 |
| 22 | MP-022 | Windows/Linux CI with lint, tests, compile, and Flask smoke check | sprint-1 | MovePal Development | alaamadii | 8 h | MP-008, MP-013, MP-014, MP-015, MP-016, MP-018 |
| 23 | MP-023 | Security, privacy, accessibility, and error-message hardening | sprint-1 | MovePal Development | IslamOuda85 | 7 h | MP-010, MP-011, MP-012, MP-019, MP-009 |
| 24 | MP-024 | Integration regression, release-candidate freeze, and QA handoff | sprint-1 | MovePal Development | alaamadii | 8 h | MP-019, MP-021, MP-022, MP-023 |
| 25 | MP-025 | Final-day QA triage, targeted fixes, retest, and release decision | sprint-1 | MovePal Development | alaamadii | 7 h | MP-024 |
| 26 | MP-026 | Final README, demonstration package, contribution record, and retrospective | sprint-1 | MovePal Development | IslamOuda85 | 7 h | MP-025 |
| 27 | MP-027 | Sprint rituals and instructor checkpoint checklist | sprint-1 | MovePal Development | alaamadii | 4 h | MP-001 |
| 28 | MP-028 | Final-day manual QA: clean installation, startup, and README sanity | sprint-1 | MovePal QA | Tojan-Naiem | 3.5 h | MP-024 |
| 29 | MP-029 | Final-day manual QA: camera permission, no-camera, browser, and fallback sanity | sprint-1 | MovePal QA | SajaZenaty | 3.5 h | MP-024 |
| 30 | MP-030 | Final-day manual QA: pose visibility and three-movement sanity | sprint-1 | MovePal QA | nezarYousef | 3.5 h | MP-024 |
| 31 | MP-031 | Final-day manual QA: feedback, scoring, repeated session, reset, and summary | sprint-1 | MovePal QA | saliqasarwi | 3.5 h | MP-024 |
| 32 | MP-032 | Final-day manual QA: invalid input, oversized file, errors, privacy, and disclaimer | sprint-1 | MovePal QA | SaadRayh | 3.5 h | MP-024 |
| 33 | MP-033 | Final-day manual QA: responsive accessibility sanity and consolidated QA report | sprint-1 | MovePal QA | BaraahMazeen | 3.5 h | MP-024 |
| 34 | MP-034 | Cross-browser compatibility baseline and support matrix | post-sprint | MovePal Development | Unassigned | 12 h | MP-024 |
| 35 | MP-035 | Performance profiling and response-time budget | post-sprint | MovePal Development | Unassigned | 14 h | MP-024 |
| 36 | MP-036 | Production-like local packaging and configuration | post-sprint | MovePal Development | Unassigned | 12 h | MP-024, MP-035 |
| 37 | MP-037 | Persistent session storage design | post-sprint | MovePal Development | Unassigned | 16 h | MP-018, MP-023 |
| 38 | MP-038 | SQLite migration and data-access layer | post-sprint | MovePal Development | Unassigned | 18 h | MP-037 |
| 39 | MP-039 | Localization architecture and message catalog | future | MovePal Development | Unassigned | 14 h | MP-024 |
| 40 | MP-040 | Arabic translation and right-to-left interface | future | MovePal Development | Unassigned | 18 h | MP-039 |
| 41 | MP-041 | Accessibility audit and remediation plan | future | MovePal Development | Unassigned | 20 h | MP-024 |
| 42 | MP-042 | Progressive Web App and offline fallback investigation | optional | MovePal Development | Unassigned | 16 h | MP-024, MP-035 |
| 43 | MP-043 | Declarative custom-movement specification | future | MovePal Development | Unassigned | 24 h | MP-014, MP-015, MP-016 |
| 44 | MP-044 | Educator-configured activity session | future | MovePal Development | Unassigned | 22 h | MP-018, MP-043 |
| 45 | MP-045 | Difficulty presets and adaptive thresholds investigation | future | MovePal Development | Unassigned | 24 h | MP-021, MP-044 |
| 46 | MP-046 | Expanded reward mechanics and session progression | future | MovePal Development | Unassigned | 18 h | MP-017, MP-018 |
| 47 | MP-047 | Avatar animation and asset pipeline | future | MovePal Development | Unassigned | 20 h | MP-011 |
| 48 | MP-048 | Optional low-latency streaming feasibility study | optional | MovePal Development | Unassigned | 28 h | MP-035 |
| 49 | MP-049 | Pose model and library version-management policy | post-sprint | MovePal Development | Unassigned | 14 h | MP-021, MP-022 |
| 50 | MP-050 | Structured logging and privacy-safe observability | post-sprint | MovePal Development | Unassigned | 16 h | MP-023, MP-036 |
| 51 | MP-051 | Threat model and automated security checks | future | MovePal Development | Unassigned | 22 h | MP-023, MP-049 |
| 52 | MP-052 | Data retention, withdrawal, and deletion workflow | future | MovePal Development | Unassigned | 14 h | MP-020, MP-037 |
| 53 | MP-053 | Expanded adult-only dataset and bias analysis | future | MovePal Development | Unassigned | 36 h | MP-020, MP-021, MP-052 |
| 54 | MP-054 | Evaluation metrics and reproducible benchmark suite | future | MovePal Development | Unassigned | 24 h | MP-021, MP-053 |
| 55 | MP-055 | Multiple-person detection and guidance | future | MovePal Development | Unassigned | 20 h | MP-013, MP-054 |
| 56 | MP-056 | Low-light and framing robustness improvements | future | MovePal Development | Unassigned | 22 h | MP-013, MP-054 |
| 57 | MP-057 | API contract documentation and schema validation | post-sprint | MovePal Development | Unassigned | 16 h | MP-010, MP-019 |
| 58 | MP-058 | Controlled cloud deployment investigation | future | MovePal Development | Unassigned | 28 h | MP-036, MP-050, MP-051 |
| 59 | MP-059 | Backup, restore, and recovery procedure | future | MovePal Development | Unassigned | 16 h | MP-037, MP-052 |
| 60 | MP-060 | Educator dashboard and aggregate session export | future | MovePal Development | Unassigned | 28 h | MP-037, MP-044, MP-052 |
| 61 | MP-061 | Release, compatibility, and deprecation policy | future | MovePal Development | Unassigned | 12 h | MP-049, MP-057 |
| 62 | MP-062 | Production-readiness evidence review | future | MovePal Development | Unassigned | 30 h | MP-035, MP-041, MP-051, MP-052, MP-054, MP-058, MP-059, MP-061 |
| 63 | MP-063 | Optional custom pose-model training research | optional | MovePal Development | Unassigned | 40 h | MP-053, MP-054, MP-062 |

## Detailed task definitions

<!-- task-id: MP-001 -->
# MP-001 — Kickoff, Sprint Goal, and Scrum working agreement

## Value
Create the shared operating agreement used during the kickoff and throughout Sprint 1. Translate the product idea into one Sprint Goal and make the Backlog → New → In Progress → In Review → Done workflow concrete for beginners. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## Detailed description and work sequence
Create the shared operating agreement used during the kickoff and throughout Sprint 1. Translate the product idea into one Sprint Goal and make the Backlog → New → In Progress → In Review → Done workflow concrete for beginners.

Work sequence:

1. Review the MovePal scope and non-medical disclaimer with the instructor.

2. Draft a one-sentence Sprint Goal and a short list of in-scope and out-of-scope items.

3. Define daily stand-up, Monday/Wednesday checkpoint, issue-status, branch, review, and escalation rules.

4. Run a 15-minute walkthrough with Team B and capture questions or disagreements.

5. Commit the approved working agreement and link it from the README.

Dependency handling:

This task has no blocking backlog dependency. It may begin once the repository and local environment are available.

## Beginner learning objectives
- Distinguish waterfall, agile, and Scrum at an introductory level.
- Understand Sprint Goal, backlog, issue, branch, pull request, review, and Definition of Done.
- Practice documenting team agreements as inspectable project artifacts.

## Deliverables
- `docs/sprint_working_agreement.md`
- Sprint Goal in `docs/project_scope.md`
- Kickoff checklist with attendance and questions

## Acceptance criteria
- The Sprint Goal describes a demonstrable Flask movement game with three movements and a fallback mode.
- The agreement explains who moves issues, when work is considered blocked, and how reviews are requested.
- The no-direct-push and no-self-approval rules are explicit.
- Students can explain the board states using one example task.

## Definition of Done
- All acceptance criteria are demonstrated with evidence in the issue or pull request.
- Relevant documentation is updated so another beginner can repeat the work.
- No credentials, personal images, student emails, or raw volunteer recordings are committed.
- The task owner records decisions, assumptions, unresolved limitations, and follow-up work.
- A focused pull request uses the task ID in its title and links the issue with `Closes #...`.
- A reviewer other than the author examines the change, requested changes are resolved, and CI passes before merge.

## Dependencies and coordination
- Blocking dependencies: None
- Related coordination tasks: None
- Initial blocking status: ready
- Do not mark this issue In Progress until required dependency outputs are available, except for a time-boxed learning spike that is explicitly recorded here.

## Ownership and review
- Team: MovePal Development
- Workstream: Testing/DevOps
- Suggested Scrum role: scrum_master
- Primary assignee: alaamadii
- Contributors: None planned
- Suggested independent reviewer: IslamOuda85
- Planned effort allocation: @alaamadii: 4 h
- Pull request: Required
- Suggested branch: `mp-001-working-agreement`

## Beginner estimate and buffers
- Focused-work estimate: 4 hours
- Investigation/learning buffer included: 1 hours
- Review/collaboration buffer included: 0.5 hours
- QA/rework buffer included: 0 hours
- This is a rough beginner estimate. Update the issue when new evidence changes the estimate; do not hide learning time.

## Planning metadata
- Priority: P0
- Sprint designation: sprint-1
- Milestone: Sprint 1 — MovePal MVP
- Initial Project stage: New
- Planned start: 2026-07-14
- Planned target: 2026-07-14
- Manual testing only: No

## Suggested verification
- Markdown links and headings are readable.

## Risks
- Agreement becomes abstract instead of actionable.
- Meeting work replaces product work rather than enabling it.

## Security and privacy
- Do not record personal attendance information beyond what the course requires.

## Helpful documentation topics
- Scrum Guide concepts: Sprint Goal, Daily Scrum, review, retrospective
- GitHub issues and pull request workflow

## Demo/evidence required
- Show the Sprint Goal and walk through one issue lifecycle.


---

<!-- task-id: MP-002 -->
# MP-002 — Product vision, user stories, MVP boundary, and ethical framing

## Value
Turn the MovePal concept into a beginner-readable product vision, prioritized user stories, narrow Sprint 1 MVP, and clear ethical boundaries. The result guides every later design decision and prevents accidental medical claims or child-data collection. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## Detailed description and work sequence
Turn the MovePal concept into a beginner-readable product vision, prioritized user stories, narrow Sprint 1 MVP, and clear ethical boundaries. The result guides every later design decision and prevents accidental medical claims or child-data collection.

Work sequence:

1. Identify the child user, supervising adult, developer, and QA perspectives without interviewing or collecting data from children.

2. Write user stories for activity selection, camera/fallback input, feedback, rewards, and summary.

3. Mark each desired capability as Sprint 1, post-sprint, future, or optional.

4. Document excluded features such as accounts, cloud deployment, real-time WebSockets, custom model training, and clinical claims.

5. Review wording for friendly, non-diagnostic language and obtain instructor approval.

Dependency handling:

This task depends on MP-001. Do not begin dependency-sensitive implementation until the listed outputs are available. The owner may perform reading or a disposable spike earlier, but must re-check assumptions after dependencies merge.

## Beginner learning objectives
- Write testable user stories and acceptance conditions.
- Separate a product prototype from medical or clinical software.
- Use scope constraints to protect a short sprint.

## Deliverables
- Expanded `docs/project_scope.md`
- Prioritized user-story list
- Ethical framing and non-medical disclaimer

## Acceptance criteria
- All three movements, fallback input, feedback, points, and summary appear in the Sprint 1 scope.
- The document states that no child data is required or collected.
- Medical treatment, diagnosis, rehabilitation effectiveness, and physiotherapy replacement are explicitly excluded.
- Each user story has an observable outcome.

## Definition of Done
- All acceptance criteria are demonstrated with evidence in the issue or pull request.
- Relevant documentation is updated so another beginner can repeat the work.
- No credentials, personal images, student emails, or raw volunteer recordings are committed.
- The task owner records decisions, assumptions, unresolved limitations, and follow-up work.
- A focused pull request uses the task ID in its title and links the issue with `Closes #...`.
- A reviewer other than the author examines the change, requested changes are resolved, and CI passes before merge.

## Dependencies and coordination
- Blocking dependencies: MP-001
- Related coordination tasks: None
- Initial blocking status: blocked
- Do not mark this issue In Progress until required dependency outputs are available, except for a time-boxed learning spike that is explicitly recorded here.

## Ownership and review
- Team: MovePal Development
- Workstream: Product/Documentation
- Suggested Scrum role: product_owner
- Primary assignee: IslamOuda85
- Contributors: None planned
- Suggested independent reviewer: alaamadii
- Planned effort allocation: @IslamOuda85: 6 h
- Pull request: Required
- Suggested branch: `mp-002-product-vision`

## Beginner estimate and buffers
- Focused-work estimate: 6 hours
- Investigation/learning buffer included: 2 hours
- Review/collaboration buffer included: 1 hours
- QA/rework buffer included: 0 hours
- This is a rough beginner estimate. Update the issue when new evidence changes the estimate; do not hide learning time.

## Planning metadata
- Priority: P0
- Sprint designation: sprint-1
- Milestone: Sprint 1 — MovePal MVP
- Initial Project stage: New
- Planned start: 2026-07-14
- Planned target: 2026-07-15
- Manual testing only: No

## Suggested verification
- Peer check that every MVP requirement maps to at least one user story.

## Risks
- Scope expands beyond one sprint.
- Friendly movement feedback is mistaken for medical advice.

## Security and privacy
- Use only hypothetical personas; do not collect child information.
- Keep the disclaimer visible in product and documentation.

## Helpful documentation topics
- User-story and acceptance-criteria examples
- Privacy by design and data minimization

## Demo/evidence required
- Present the MVP boundary and explain one deliberately deferred feature.


---

<!-- task-id: MP-003 -->
# MP-003 — Git, GitHub, pull-request, and review rehearsal

## Value
Give all Team B members a safe practical rehearsal of the company-like workflow before feature work begins. The exercise verifies local Git setup, repository access, branch creation, pull requests, independent review, CI interpretation, and squash merging. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## Detailed description and work sequence
Give all Team B members a safe practical rehearsal of the company-like workflow before feature work begins. The exercise verifies local Git setup, repository access, branch creation, pull requests, independent review, CI interpretation, and squash merging.

Work sequence:

1. Create a tiny documentation-only practice issue for each member or one coordinated rehearsal checklist.

2. Have every member clone using an OS-appropriate path and confirm Python/Git versions.

3. Each member creates a small branch, commits a harmless documentation improvement, and opens a draft PR.

4. Assign a different reviewer using a round-robin mapping.

5. Resolve at least one review comment, wait for CI, squash merge, and delete the feature branch.

6. Record any access or OS-specific problem before implementation tasks start.

Dependency handling:

This task depends on MP-001. Do not begin dependency-sensitive implementation until the listed outputs are available. The owner may perform reading or a disposable spike earlier, but must re-check assumptions after dependencies merge.

## Beginner learning objectives
- Use clone, branch, commit, push, pull request, review, and squash merge.
- Understand why the author cannot approve their own work.
- Interpret a simple CI success or failure.

## Deliverables
- Completed rehearsal checklist for six members
- At least one reviewed contribution per member
- Troubleshooting notes for Windows/Linux/macOS paths and commands

## Acceptance criteria
- Every Team B member can push a feature branch and open a PR.
- Every Team B member reviews another member’s change.
- No member self-approves.
- The checklist records CI status and merge method.
- Any blocked account is reported before feature assignment.

## Definition of Done
- All acceptance criteria are demonstrated with evidence in the issue or pull request.
- Relevant documentation is updated so another beginner can repeat the work.
- No credentials, personal images, student emails, or raw volunteer recordings are committed.
- The task owner records decisions, assumptions, unresolved limitations, and follow-up work.
- A focused pull request uses the task ID in its title and links the issue with `Closes #...`.
- A reviewer other than the author examines the change, requested changes are resolved, and CI passes before merge.

## Dependencies and coordination
- Blocking dependencies: MP-001
- Related coordination tasks: None
- Initial blocking status: blocked
- Do not mark this issue In Progress until required dependency outputs are available, except for a time-boxed learning spike that is explicitly recorded here.

## Ownership and review
- Team: MovePal Development
- Workstream: Testing/DevOps
- Suggested Scrum role: scrum_master
- Primary assignee: alaamadii
- Contributors: @IslamOuda85, @AhmadKollab, @myarnwas, @JHT127, @MennaAllah-Alatrsh
- Suggested independent reviewer: Tojan-Naiem
- Planned effort allocation: @alaamadii: 2 h, @IslamOuda85: 0.8 h, @AhmadKollab: 0.8 h, @myarnwas: 0.8 h, @JHT127: 0.8 h, @MennaAllah-Alatrsh: 0.8 h
- Pull request: Required
- Suggested branch: `mp-003-git-rehearsal`

## Beginner estimate and buffers
- Focused-work estimate: 6 hours
- Investigation/learning buffer included: 1 hours
- Review/collaboration buffer included: 2 hours
- QA/rework buffer included: 0 hours
- This is a rough beginner estimate. Update the issue when new evidence changes the estimate; do not hide learning time.

## Planning metadata
- Priority: P0
- Sprint designation: sprint-1
- Milestone: Sprint 1 — MovePal MVP
- Initial Project stage: New
- Planned start: 2026-07-14
- Planned target: 2026-07-15
- Manual testing only: No

## Suggested verification
- Verify all six usernames appear in merged PR authors/reviewers or documented co-author evidence.

## Risks
- Members use direct pushes because protection is not technically enforced.
- Git setup problems consume feature time.

## Security and privacy
- Do not place personal emails in screenshots or issue comments.

## Helpful documentation topics
- GitHub Docs: creating branches and pull requests
- Repository `CONTRIBUTING.md`

## Demo/evidence required
- Show one merged rehearsal PR and its independent review.


---

<!-- task-id: MP-004 -->
# MP-004 — Flask application-factory learning spike and architecture decision

## Value
Investigate the minimum Flask architecture needed for MovePal and record an architecture decision before building feature code. The spike must prove that an application factory, thin routes, templates, static assets, services, configuration, and tests can work together without unnecessary complexity. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## Detailed description and work sequence
Investigate the minimum Flask architecture needed for MovePal and record an architecture decision before building feature code. The spike must prove that an application factory, thin routes, templates, static assets, services, configuration, and tests can work together without unnecessary complexity.

Work sequence:

1. Read a concise Flask application-factory example and identify concepts unfamiliar to the team.

2. Create a disposable local spike with `create_app`, one page route, one JSON route, and one test client test.

3. Compare a single routes module with blueprints and choose the simplest clear structure.

4. Document configuration loading, path handling with `pathlib`, and where pose/movement logic belongs.

5. Write an ADR with alternatives, decision, consequences, and rejected complexity.

Dependency handling:

This task depends on MP-002, MP-003. Do not begin dependency-sensitive implementation until the listed outputs are available. The owner may perform reading or a disposable spike earlier, but must re-check assumptions after dependencies merge.

## Beginner learning objectives
- Create and test a Flask application factory.
- Separate routes from domain services.
- Record an architecture decision and trade-offs.

## Deliverables
- `docs/adr/001-flask-architecture.md`
- Disposable or committed minimal factory spike
- Architecture diagram updated with module boundaries

## Acceptance criteria
- The spike imports without starting a development server.
- A Flask test client receives a page and JSON response.
- Routes contain no pose or scoring implementation.
- The ADR explains why React, microservices, authentication, and a database are not Sprint 1 dependencies.
- Paths are OS-independent.

## Definition of Done
- All acceptance criteria are demonstrated with evidence in the issue or pull request.
- Relevant documentation is updated so another beginner can repeat the work.
- No credentials, personal images, student emails, or raw volunteer recordings are committed.
- The task owner records decisions, assumptions, unresolved limitations, and follow-up work.
- A focused pull request uses the task ID in its title and links the issue with `Closes #...`.
- A reviewer other than the author examines the change, requested changes are resolved, and CI passes before merge.

## Dependencies and coordination
- Blocking dependencies: MP-002, MP-003
- Related coordination tasks: None
- Initial blocking status: blocked
- Do not mark this issue In Progress until required dependency outputs are available, except for a time-boxed learning spike that is explicitly recorded here.

## Ownership and review
- Team: MovePal Development
- Workstream: Backend
- Suggested Scrum role: developer
- Primary assignee: AhmadKollab
- Contributors: None planned
- Suggested independent reviewer: alaamadii
- Planned effort allocation: @AhmadKollab: 6 h
- Pull request: Required
- Suggested branch: `mp-004-flask-architecture-spike`

## Beginner estimate and buffers
- Focused-work estimate: 6 hours
- Investigation/learning buffer included: 2 hours
- Review/collaboration buffer included: 1 hours
- QA/rework buffer included: 0 hours
- This is a rough beginner estimate. Update the issue when new evidence changes the estimate; do not hide learning time.

## Planning metadata
- Priority: P0
- Sprint designation: sprint-1
- Milestone: Sprint 1 — MovePal MVP
- Initial Project stage: New
- Planned start: 2026-07-14
- Planned target: 2026-07-15
- Manual testing only: No

## Suggested verification
- Factory import test
- Page route smoke test
- JSON route smoke test

## Risks
- Spike code becomes production code without cleanup.
- Overengineering delays the MVP.

## Security and privacy
- Logging examples must exclude images and landmark arrays.

## Helpful documentation topics
- Flask application factories
- Flask testing with the test client
- Python `pathlib`

## Demo/evidence required
- Run the spike tests and explain the chosen module boundary.


---

<!-- task-id: MP-005 -->
# MP-005 — MediaPipe Pose learning spike and computer-vision service contract

## Value
Investigate beginner-compatible pose estimation and define the stable interface between Flask and computer-vision code. Use MediaPipe Pose unless the spike finds a documented compatibility blocker; do not train a model or add real-time streaming. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## Detailed description and work sequence
Investigate beginner-compatible pose estimation and define the stable interface between Flask and computer-vision code. Use MediaPipe Pose unless the spike finds a documented compatibility blocker; do not train a model or add real-time streaming.

Work sequence:

1. Confirm Python 3.11 and supported MediaPipe installation on at least one Windows machine.

2. Run pose estimation on a permitted adult/sample image rather than child data.

3. List the landmarks needed for shoulders, elbows, wrists, hips, and knees.

4. Define input validation, result object/schema, visibility handling, no-pose behavior, and error mapping.

5. Create a mock result fixture so tests never require a camera or model download.

6. Document compatibility risks and a fallback plan.

Dependency handling:

This task depends on MP-002, MP-003. Do not begin dependency-sensitive implementation until the listed outputs are available. The owner may perform reading or a disposable spike earlier, but must re-check assumptions after dependencies merge.

## Beginner learning objectives
- Load a pretrained pose estimator and interpret landmarks, visibility, and normalized coordinates.
- Separate third-party model calls from movement rules.
- Design a mockable service contract for CI.

## Deliverables
- `docs/adr/002-pose-estimator.md`
- Pose service interface/schema
- Tiny anonymized/mock landmark fixture
- Compatibility notes

## Acceptance criteria
- A sample produces landmarks or a clear documented blocker.
- The interface returns success/no-pose/error states without exposing MediaPipe objects to routes.
- Visibility/confidence is represented explicitly.
- CI can use a fixture without camera access.
- No raw child or volunteer image is committed.

## Definition of Done
- All acceptance criteria are demonstrated with evidence in the issue or pull request.
- Relevant documentation is updated so another beginner can repeat the work.
- No credentials, personal images, student emails, or raw volunteer recordings are committed.
- The task owner records decisions, assumptions, unresolved limitations, and follow-up work.
- A focused pull request uses the task ID in its title and links the issue with `Closes #...`.
- A reviewer other than the author examines the change, requested changes are resolved, and CI passes before merge.

## Dependencies and coordination
- Blocking dependencies: MP-002, MP-003
- Related coordination tasks: None
- Initial blocking status: blocked
- Do not mark this issue In Progress until required dependency outputs are available, except for a time-boxed learning spike that is explicitly recorded here.

## Ownership and review
- Team: MovePal Development
- Workstream: Computer Vision
- Suggested Scrum role: developer
- Primary assignee: myarnwas
- Contributors: @IslamOuda85
- Suggested independent reviewer: AhmadKollab
- Planned effort allocation: @myarnwas: 5 h, @IslamOuda85: 1 h
- Pull request: Required
- Suggested branch: `mp-005-pose-spike`

## Beginner estimate and buffers
- Focused-work estimate: 6 hours
- Investigation/learning buffer included: 3 hours
- Review/collaboration buffer included: 1 hours
- QA/rework buffer included: 0 hours
- This is a rough beginner estimate. Update the issue when new evidence changes the estimate; do not hide learning time.

## Planning metadata
- Priority: P0
- Sprint designation: sprint-1
- Milestone: Sprint 1 — MovePal MVP
- Initial Project stage: New
- Planned start: 2026-07-14
- Planned target: 2026-07-15
- Manual testing only: No

## Suggested verification
- Schema validation for a mock landmark result
- No-pose fixture behavior

## Risks
- MediaPipe wheel or API incompatibility.
- Model-specific details leak into the whole application.
- Sample data contains personal imagery.

## Security and privacy
- Use an openly licensed sample or an adult volunteer with consent only for local investigation.
- Commit landmarks or synthetic fixtures, not raw recordings.

## Helpful documentation topics
- MediaPipe Pose documentation
- Normalized landmark coordinates and visibility
- Dependency version pinning

## Demo/evidence required
- Show the structured landmark result and no-pose response.


---

<!-- task-id: MP-006 -->
# MP-006 — Game UX, webcam permission, and fallback-flow design spike

## Value
Design the simplest child-friendly interaction that can be implemented with Jinja, CSS/Bootstrap, and minimal vanilla JavaScript. Validate browser camera permission behavior and ensure an equally demonstrable sample-image or sample-video path exists. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## Detailed description and work sequence
Design the simplest child-friendly interaction that can be implemented with Jinja, CSS/Bootstrap, and minimal vanilla JavaScript. Validate browser camera permission behavior and ensure an equally demonstrable sample-image or sample-video path exists.

Work sequence:

1. Sketch the start screen, activity selection, camera/fallback input, feedback, points, and summary states.

2. Build a disposable browser experiment that requests webcam permission and captures a still frame.

3. Test denial and no-device behavior and record browser messages.

4. Define the fallback upload/sample flow and supported file constraints.

5. Review wording, contrast, focus order, and touch-sized controls.

6. Produce an implementation-ready interaction specification.

Dependency handling:

This task depends on MP-002, MP-003. Do not begin dependency-sensitive implementation until the listed outputs are available. The owner may perform reading or a disposable spike earlier, but must re-check assumptions after dependencies merge.

## Beginner learning objectives
- Use `getUserMedia` safely and handle permission failures.
- Design a small state-driven UI without a frontend framework.
- Create accessible, friendly feedback for a young audience.

## Deliverables
- Wireframes or low-fidelity HTML mock
- `docs/ux_flow.md`
- Camera/fallback experiment notes
- Friendly feedback wording list

## Acceptance criteria
- The flow contains a clear camera choice and fallback choice.
- Permission denial does not trap the user.
- The design shows three movements, retry, points, and summary.
- Controls can be used by keyboard and at mobile width.
- No raw image is retained by default.

## Definition of Done
- All acceptance criteria are demonstrated with evidence in the issue or pull request.
- Relevant documentation is updated so another beginner can repeat the work.
- No credentials, personal images, student emails, or raw volunteer recordings are committed.
- The task owner records decisions, assumptions, unresolved limitations, and follow-up work.
- A focused pull request uses the task ID in its title and links the issue with `Closes #...`.
- A reviewer other than the author examines the change, requested changes are resolved, and CI passes before merge.

## Dependencies and coordination
- Blocking dependencies: MP-002, MP-003
- Related coordination tasks: None
- Initial blocking status: blocked
- Do not mark this issue In Progress until required dependency outputs are available, except for a time-boxed learning spike that is explicitly recorded here.

## Ownership and review
- Team: MovePal Development
- Workstream: Frontend/UX
- Suggested Scrum role: developer
- Primary assignee: JHT127
- Contributors: None planned
- Suggested independent reviewer: IslamOuda85
- Planned effort allocation: @JHT127: 6 h
- Pull request: Required
- Suggested branch: `mp-006-ux-camera-spike`

## Beginner estimate and buffers
- Focused-work estimate: 6 hours
- Investigation/learning buffer included: 2 hours
- Review/collaboration buffer included: 1 hours
- QA/rework buffer included: 0 hours
- This is a rough beginner estimate. Update the issue when new evidence changes the estimate; do not hide learning time.

## Planning metadata
- Priority: P0
- Sprint designation: sprint-1
- Milestone: Sprint 1 — MovePal MVP
- Initial Project stage: New
- Planned start: 2026-07-14
- Planned target: 2026-07-15
- Manual testing only: No

## Suggested verification
- Manual permission granted/denied/no-camera checklist
- Keyboard navigation check for mock

## Risks
- Camera APIs differ by browser or require secure context.
- Design grows into a frontend framework project.
- Feedback language becomes negative or medical.

## Security and privacy
- Explain that frames are processed only for feedback and are not stored by default.

## Helpful documentation topics
- MDN `getUserMedia` and permission handling
- WCAG introductory keyboard/contrast guidance

## Demo/evidence required
- Walk through camera success, denial, and fallback wireframes.


---

<!-- task-id: MP-007 -->
# MP-007 — Movement specifications, landmark schema, and evaluation plan

## Value
Define observable, non-medical rules for raise-both-arms, side reach left/right, and knee lift/step-in-place before coding. The specification must use relative geometry and visibility checks so rules are understandable, testable, and less dependent on body size or camera distance. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## Detailed description and work sequence
Define observable, non-medical rules for raise-both-arms, side reach left/right, and knee lift/step-in-place before coding. The specification must use relative geometry and visibility checks so rules are understandable, testable, and less dependent on body size or camera distance.

Work sequence:

1. Review the pose landmarks and UX feedback vocabulary from the spikes.

2. For each movement, define start/hold/success conditions, side handling, visibility requirements, and timeout/retry behavior.

3. List examples of correct, near-correct, incorrect, partly out-of-frame, and low-confidence poses.

4. Define a JSON/CSV landmark fixture schema with no personal identifiers.

5. Specify initial thresholds as configurable values and document that they are prototype heuristics.

6. Create an evaluation matrix for later adult-only calibration.

Dependency handling:

This task depends on MP-005, MP-006. Do not begin dependency-sensitive implementation until the listed outputs are available. The owner may perform reading or a disposable spike earlier, but must re-check assumptions after dependencies merge.

## Beginner learning objectives
- Translate a physical movement into landmark relations and test cases.
- Use normalized/relative measurements instead of hard-coded pixels.
- Plan correct, borderline, and incorrect fixtures.

## Deliverables
- `docs/movement_specification.md`
- Landmark fixture schema
- Movement test matrix
- Initial configurable thresholds

## Acceptance criteria
- All three activities have unambiguous rules and feedback mappings.
- Side reach explicitly supports left and right.
- Rules use joints/relative positions rather than image pixels.
- Visibility and full-body requirements are stated.
- Thresholds are labeled heuristic and configurable.

## Definition of Done
- All acceptance criteria are demonstrated with evidence in the issue or pull request.
- Relevant documentation is updated so another beginner can repeat the work.
- No credentials, personal images, student emails, or raw volunteer recordings are committed.
- The task owner records decisions, assumptions, unresolved limitations, and follow-up work.
- A focused pull request uses the task ID in its title and links the issue with `Closes #...`.
- A reviewer other than the author examines the change, requested changes are resolved, and CI passes before merge.

## Dependencies and coordination
- Blocking dependencies: MP-005, MP-006
- Related coordination tasks: None
- Initial blocking status: blocked
- Do not mark this issue In Progress until required dependency outputs are available, except for a time-boxed learning spike that is explicitly recorded here.

## Ownership and review
- Team: MovePal Development
- Workstream: Data/Evaluation
- Suggested Scrum role: developer
- Primary assignee: MennaAllah-Alatrsh
- Contributors: @IslamOuda85
- Suggested independent reviewer: JHT127
- Planned effort allocation: @MennaAllah-Alatrsh: 5 h, @IslamOuda85: 1 h
- Pull request: Required
- Suggested branch: `mp-007-movement-specifications`

## Beginner estimate and buffers
- Focused-work estimate: 6 hours
- Investigation/learning buffer included: 2 hours
- Review/collaboration buffer included: 1 hours
- QA/rework buffer included: 0 hours
- This is a rough beginner estimate. Update the issue when new evidence changes the estimate; do not hide learning time.

## Planning metadata
- Priority: P0
- Sprint designation: sprint-1
- Milestone: Sprint 1 — MovePal MVP
- Initial Project stage: New
- Planned start: 2026-07-15
- Planned target: 2026-07-16
- Manual testing only: No

## Suggested verification
- Schema example validates
- Each rule maps to at least three positive/negative test cases

## Risks
- Rules are vague or tuned to one person.
- Side labels are interpreted inconsistently.
- Specification implies clinical correctness.

## Security and privacy
- Fixtures contain derived coordinates only.
- Do not describe scores as health or rehabilitation measures.

## Helpful documentation topics
- MediaPipe landmark index documentation
- Joint-angle and relative-position calculations

## Demo/evidence required
- Explain one movement rule using a landmark sketch and test matrix.


---

<!-- task-id: MP-008 -->
# MP-008 — Repository skeleton, dependencies, and Flask application factory

## Value
Turn the architecture spike into the production Sprint 1 skeleton. Establish installable dependencies, the Flask factory, configuration, routes/services/templates/static boundaries, and cross-platform startup before feature branches diverge. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## Detailed description and work sequence
Turn the architecture spike into the production Sprint 1 skeleton. Establish installable dependencies, the Flask factory, configuration, routes/services/templates/static boundaries, and cross-platform startup before feature branches diverge.

Work sequence:

1. Reconcile the generated repository skeleton with the approved ADR.

2. Implement `create_app`, development/testing configuration, page/API route registration, and basic error pages.

3. Pin compatible runtime and development dependencies and document installation.

4. Use `pathlib` for data and fixture paths; do not use drive letters or string-concatenated separators.

5. Add import, health, and test-client smoke tests.

6. Have the reviewer run the instructions on a second machine or OS.

Dependency handling:

This task depends on MP-004. Do not begin dependency-sensitive implementation until the listed outputs are available. The owner may perform reading or a disposable spike earlier, but must re-check assumptions after dependencies merge.

## Beginner learning objectives
- Build a maintainable Flask package from an ADR.
- Pin and separate runtime/development dependencies.
- Use environment-based configuration and portable paths.

## Deliverables
- Working Flask package and `run.py`
- Runtime and development requirement files
- Configuration module
- Smoke tests and startup documentation

## Acceptance criteria
- `python run.py` starts the development app after documented installation.
- `create_app("testing")` or equivalent can be imported without running a server.
- Windows and Linux CI install and run smoke tests.
- Routes remain thin and service modules are importable.
- Debug mode is not forced outside development.

## Definition of Done
- All acceptance criteria are demonstrated with evidence in the issue or pull request.
- Relevant documentation is updated so another beginner can repeat the work.
- No credentials, personal images, student emails, or raw volunteer recordings are committed.
- The task owner records decisions, assumptions, unresolved limitations, and follow-up work.
- A focused pull request uses the task ID in its title and links the issue with `Closes #...`.
- A reviewer other than the author examines the change, requested changes are resolved, and CI passes before merge.

## Dependencies and coordination
- Blocking dependencies: MP-004
- Related coordination tasks: None
- Initial blocking status: blocked
- Do not mark this issue In Progress until required dependency outputs are available, except for a time-boxed learning spike that is explicitly recorded here.

## Ownership and review
- Team: MovePal Development
- Workstream: Backend
- Suggested Scrum role: developer
- Primary assignee: AhmadKollab
- Contributors: None planned
- Suggested independent reviewer: alaamadii
- Planned effort allocation: @AhmadKollab: 6 h
- Pull request: Required
- Suggested branch: `mp-008-flask-skeleton`

## Beginner estimate and buffers
- Focused-work estimate: 6 hours
- Investigation/learning buffer included: 1 hours
- Review/collaboration buffer included: 1 hours
- QA/rework buffer included: 0 hours
- This is a rough beginner estimate. Update the issue when new evidence changes the estimate; do not hide learning time.

## Planning metadata
- Priority: P0
- Sprint designation: sprint-1
- Milestone: Sprint 1 — MovePal MVP
- Initial Project stage: New
- Planned start: 2026-07-16
- Planned target: 2026-07-17
- Manual testing only: No

## Suggested verification
- Factory import test
- Health endpoint test
- 404/413 error-page smoke tests

## Risks
- Dependency versions conflict with MediaPipe.
- Skeleton becomes too complex for beginners.
- OS-specific paths pass locally but fail in CI.

## Security and privacy
- Default logging excludes uploaded content and landmark arrays.

## Helpful documentation topics
- Approved Flask ADR
- Python packaging and `pathlib`
- Flask configuration patterns

## Demo/evidence required
- Fresh-install startup and test-client health response.


---

<!-- task-id: MP-009 -->
# MP-009 — Initial README, contribution guide, privacy, and limitations

## Value
Create the documentation baseline that lets a beginner install, run, contribute, and understand MovePal’s limits before the implementation is complete. Documentation is versioned with the code and updated throughout the sprint. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## Detailed description and work sequence
Create the documentation baseline that lets a beginner install, run, contribute, and understand MovePal’s limits before the implementation is complete. Documentation is versioned with the code and updated throughout the sprint.

Work sequence:

1. Document product purpose, non-medical disclaimer, architecture summary, prerequisites, install, run, test, and fallback mode.

2. Document Git workflow, branch naming, PR evidence, review, and manual master-branch policy.

3. Create privacy and limitations pages covering no child data, adult-only calibration, landmark preference, browser camera behavior, and heuristic rules.

4. Add troubleshooting placeholders for Windows and Linux.

5. Ask one teammate to follow the README literally and record unclear steps.

6. Update documents based on the dry run.

Dependency handling:

This task depends on MP-002, MP-008. Do not begin dependency-sensitive implementation until the listed outputs are available. The owner may perform reading or a disposable spike earlier, but must re-check assumptions after dependencies merge.

## Beginner learning objectives
- Write reproducible setup instructions.
- Document privacy and limitations honestly.
- Explain issue/branch/PR conventions to peers.

## Deliverables
- `README.md`
- `CONTRIBUTING.md`
- `docs/privacy.md`
- `docs/limitations.md`
- Documentation verification notes

## Acceptance criteria
- A new contributor can identify prerequisites and startup commands.
- The fallback mode is explained as mandatory demo protection.
- The README links scope, architecture, privacy, limitations, and contribution rules.
- No claim of medical validity or production readiness appears.
- The review identifies and fixes at least one ambiguity.

## Definition of Done
- All acceptance criteria are demonstrated with evidence in the issue or pull request.
- Relevant documentation is updated so another beginner can repeat the work.
- No credentials, personal images, student emails, or raw volunteer recordings are committed.
- The task owner records decisions, assumptions, unresolved limitations, and follow-up work.
- A focused pull request uses the task ID in its title and links the issue with `Closes #...`.
- A reviewer other than the author examines the change, requested changes are resolved, and CI passes before merge.

## Dependencies and coordination
- Blocking dependencies: MP-002, MP-008
- Related coordination tasks: None
- Initial blocking status: blocked
- Do not mark this issue In Progress until required dependency outputs are available, except for a time-boxed learning spike that is explicitly recorded here.

## Ownership and review
- Team: MovePal Development
- Workstream: Product/Documentation
- Suggested Scrum role: product_owner
- Primary assignee: IslamOuda85
- Contributors: None planned
- Suggested independent reviewer: MennaAllah-Alatrsh
- Planned effort allocation: @IslamOuda85: 6 h
- Pull request: Required
- Suggested branch: `mp-009-documentation-baseline`

## Beginner estimate and buffers
- Focused-work estimate: 6 hours
- Investigation/learning buffer included: 1 hours
- Review/collaboration buffer included: 1 hours
- QA/rework buffer included: 0 hours
- This is a rough beginner estimate. Update the issue when new evidence changes the estimate; do not hide learning time.

## Planning metadata
- Priority: P1
- Sprint designation: sprint-1
- Milestone: Sprint 1 — MovePal MVP
- Initial Project stage: New
- Planned start: 2026-07-16
- Planned target: 2026-07-20
- Manual testing only: No

## Suggested verification
- Follow-the-README dry run on a clean virtual environment
- Markdown link check by reviewer

## Risks
- Documentation drifts from code.
- Setup assumes the author’s machine.
- Privacy wording is hidden or vague.

## Security and privacy
- Do not publish student emails, volunteer names, or raw recordings.

## Helpful documentation topics
- Repository architecture ADRs
- Project privacy and limitation requirements

## Demo/evidence required
- Open the README and show the complete fresh-start path.


---

<!-- task-id: MP-010 -->
# MP-010 — Frame/upload API, input validation, and safe error handling

## Value
Implement the backend boundary that receives a periodically captured frame or permitted fallback file and returns structured JSON. Keep validation and errors predictable so frontend, pose service, tests, and QA can work independently. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## Detailed description and work sequence
Implement the backend boundary that receives a periodically captured frame or permitted fallback file and returns structured JSON. Keep validation and errors predictable so frontend, pose service, tests, and QA can work independently.

Work sequence:

1. Review the camera/fallback contract and define request/response examples.

2. Add an API endpoint that accepts one bounded image/frame input and rejects missing, malformed, unsupported, or oversized input.

3. Configure upload-size limits and allow only the agreed MIME types/extensions.

4. Store temporary data only when required and delete it after processing; otherwise process in memory.

5. Map pose-service success/no-pose/error results to stable JSON messages.

6. Add unit/integration tests for valid and invalid requests.

Dependency handling:

This task depends on MP-008, MP-005, MP-006. Do not begin dependency-sensitive implementation until the listed outputs are available. The owner may perform reading or a disposable spike earlier, but must re-check assumptions after dependencies merge.

## Beginner learning objectives
- Validate uploads and JSON at a Flask boundary.
- Use safe filenames, limits, allowed types, and meaningful status codes.
- Keep routes thin by delegating processing to services.

## Deliverables
- Validated frame/upload endpoint
- Request/response contract in documentation
- 413/400/415-style error handling
- Automated API tests

## Acceptance criteria
- The endpoint returns deterministic JSON fields used by the frontend.
- Unsupported and oversized files fail safely with friendly messages.
- Filenames are never trusted as server paths.
- Routes do not implement pose or movement rules.
- Temporary input is not retained after the request.

## Definition of Done
- All acceptance criteria are demonstrated with evidence in the issue or pull request.
- Relevant documentation is updated so another beginner can repeat the work.
- No credentials, personal images, student emails, or raw volunteer recordings are committed.
- The task owner records decisions, assumptions, unresolved limitations, and follow-up work.
- A focused pull request uses the task ID in its title and links the issue with `Closes #...`.
- A reviewer other than the author examines the change, requested changes are resolved, and CI passes before merge.

## Dependencies and coordination
- Blocking dependencies: MP-008, MP-005, MP-006
- Related coordination tasks: None
- Initial blocking status: blocked
- Do not mark this issue In Progress until required dependency outputs are available, except for a time-boxed learning spike that is explicitly recorded here.

## Ownership and review
- Team: MovePal Development
- Workstream: Backend
- Suggested Scrum role: developer
- Primary assignee: AhmadKollab
- Contributors: None planned
- Suggested independent reviewer: MennaAllah-Alatrsh
- Planned effort allocation: @AhmadKollab: 6 h
- Pull request: Required
- Suggested branch: `mp-010-frame-api-validation`

## Beginner estimate and buffers
- Focused-work estimate: 6 hours
- Investigation/learning buffer included: 1 hours
- Review/collaboration buffer included: 1 hours
- QA/rework buffer included: 0 hours
- This is a rough beginner estimate. Update the issue when new evidence changes the estimate; do not hide learning time.

## Planning metadata
- Priority: P0
- Sprint designation: sprint-1
- Milestone: Sprint 1 — MovePal MVP
- Initial Project stage: New
- Planned start: 2026-07-17
- Planned target: 2026-07-20
- Manual testing only: No

## Suggested verification
- Valid tiny fixture
- Missing input
- Unsupported type
- Oversized input
- Mock pose-service failure

## Risks
- Large uploads exhaust memory.
- File type checks rely only on filename.
- Error JSON differs between branches.

## Security and privacy
- Do not persist frames or include base64/image bytes in logs.

## Helpful documentation topics
- Flask upload patterns and `MAX_CONTENT_LENGTH`
- Werkzeug safe filename and request validation

## Demo/evidence required
- Call the endpoint with one valid and three invalid examples.


---

<!-- task-id: MP-011 -->
# MP-011 — Base game interface, avatar presentation, and accessible navigation

## Value
Build the reusable child-friendly page structure and visual language for MovePal. Deliver activity selection, instructions, avatar/toy placeholder, feedback area, score area, camera/fallback controls, and summary container without coupling layout to pose logic. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## Detailed description and work sequence
Build the reusable child-friendly page structure and visual language for MovePal. Deliver activity selection, instructions, avatar/toy placeholder, feedback area, score area, camera/fallback controls, and summary container without coupling layout to pose logic.

Work sequence:

1. Convert approved wireframes into a base template and game page.

2. Create reusable components/partials where they reduce duplication.

3. Add a simple original or properly licensed avatar/toy asset and attribution when required.

4. Implement responsive layout, visible focus, keyboard-reachable controls, headings, labels, and status regions.

5. Represent idle, preparing, capturing, evaluating, success, retry, and summary states using CSS/JS classes.

6. Test at desktop and mobile widths without requiring camera access.

Dependency handling:

This task depends on MP-006, MP-008. Do not begin dependency-sensitive implementation until the listed outputs are available. The owner may perform reading or a disposable spike earlier, but must re-check assumptions after dependencies merge.

## Beginner learning objectives
- Create reusable Jinja templates and static assets.
- Apply basic accessibility and responsive-design checks.
- Represent application states clearly with minimal JavaScript.

## Deliverables
- Jinja templates
- CSS and minimal state-management JavaScript
- Avatar/toy asset with attribution
- Responsive/accessibility checklist

## Acceptance criteria
- All three movement choices are visible and understandable.
- The page has dedicated feedback, score, input, and summary regions.
- Keyboard users can reach and activate controls.
- The design remains usable around 360px width.
- No third-party copyrighted image is included without permission.

## Definition of Done
- All acceptance criteria are demonstrated with evidence in the issue or pull request.
- Relevant documentation is updated so another beginner can repeat the work.
- No credentials, personal images, student emails, or raw volunteer recordings are committed.
- The task owner records decisions, assumptions, unresolved limitations, and follow-up work.
- A focused pull request uses the task ID in its title and links the issue with `Closes #...`.
- A reviewer other than the author examines the change, requested changes are resolved, and CI passes before merge.

## Dependencies and coordination
- Blocking dependencies: MP-006, MP-008
- Related coordination tasks: None
- Initial blocking status: blocked
- Do not mark this issue In Progress until required dependency outputs are available, except for a time-boxed learning spike that is explicitly recorded here.

## Ownership and review
- Team: MovePal Development
- Workstream: Frontend/UX
- Suggested Scrum role: developer
- Primary assignee: JHT127
- Contributors: None planned
- Suggested independent reviewer: IslamOuda85
- Planned effort allocation: @JHT127: 6 h, @alaamadii: 1 h
- Pull request: Required
- Suggested branch: `mp-011-base-game-ui`

## Beginner estimate and buffers
- Focused-work estimate: 7 hours
- Investigation/learning buffer included: 1.5 hours
- Review/collaboration buffer included: 1 hours
- QA/rework buffer included: 0 hours
- This is a rough beginner estimate. Update the issue when new evidence changes the estimate; do not hide learning time.

## Planning metadata
- Priority: P0
- Sprint designation: sprint-1
- Milestone: Sprint 1 — MovePal MVP
- Initial Project stage: New
- Planned start: 2026-07-17
- Planned target: 2026-07-21
- Manual testing only: No

## Suggested verification
- Template render test
- Keyboard/manual responsive checklist
- Static asset path test on Windows/Linux

## Risks
- Visual work consumes logic time.
- State changes are conveyed only by color.
- Asset licensing is unclear.

## Security and privacy
- UI explains camera use before permission request.

## Helpful documentation topics
- Jinja template inheritance
- Basic WCAG focus, labels, contrast, and status messages

## Demo/evidence required
- Navigate activity selection and state changes using keyboard only.


---

<!-- task-id: MP-012 -->
# MP-012 — Browser webcam capture and mandatory fallback sample mode

## Value
Implement browser camera permission and periodic still-frame capture while preserving a first-class fallback mode for machines, browsers, or demo rooms where a webcam is unavailable. This is deliberately not low-latency streaming. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## Detailed description and work sequence
Implement browser camera permission and periodic still-frame capture while preserving a first-class fallback mode for machines, browsers, or demo rooms where a webcam is unavailable. This is deliberately not low-latency streaming.

Work sequence:

1. Implement an explicit “Use camera” action so permission is not requested unexpectedly.

2. Display a local video preview and capture a bounded JPEG/PNG frame at a controlled interval or on user action.

3. Send the frame to the validated Flask endpoint and prevent overlapping requests.

4. Handle denied permission, absent device, unsupported API, insecure context, stopped track, and server errors.

5. Implement included sample-image/sample-video selection using tiny approved assets.

6. Stop media tracks when leaving the activity or ending the session.

7. Document browser/security-context expectations and fallback usage.

Dependency handling:

This task depends on MP-010, MP-011. Do not begin dependency-sensitive implementation until the listed outputs are available. The owner may perform reading or a disposable spike earlier, but must re-check assumptions after dependencies merge.

## Beginner learning objectives
- Use `navigator.mediaDevices.getUserMedia` and canvas capture.
- Handle asynchronous browser errors and user denial.
- Design a fallback path as part of the product rather than an afterthought.

## Deliverables
- Camera capture JavaScript
- Fallback sample selector
- Error/permission UI states
- Browser behavior documentation and tests

## Acceptance criteria
- Camera mode obtains permission only after user action.
- At least one frame reaches the API and updates the UI.
- Denial/no-camera/unsupported-browser paths lead to fallback mode.
- Only one request is active at a time.
- Tracks stop on session end.
- The final demo can run completely without a live camera.

## Definition of Done
- All acceptance criteria are demonstrated with evidence in the issue or pull request.
- Relevant documentation is updated so another beginner can repeat the work.
- No credentials, personal images, student emails, or raw volunteer recordings are committed.
- The task owner records decisions, assumptions, unresolved limitations, and follow-up work.
- A focused pull request uses the task ID in its title and links the issue with `Closes #...`.
- A reviewer other than the author examines the change, requested changes are resolved, and CI passes before merge.

## Dependencies and coordination
- Blocking dependencies: MP-010, MP-011
- Related coordination tasks: None
- Initial blocking status: blocked
- Do not mark this issue In Progress until required dependency outputs are available, except for a time-boxed learning spike that is explicitly recorded here.

## Ownership and review
- Team: MovePal Development
- Workstream: Frontend/UX
- Suggested Scrum role: developer
- Primary assignee: JHT127
- Contributors: None planned
- Suggested independent reviewer: alaamadii
- Planned effort allocation: @JHT127: 8 h
- Pull request: Required
- Suggested branch: `mp-012-webcam-fallback`

## Beginner estimate and buffers
- Focused-work estimate: 8 hours
- Investigation/learning buffer included: 2 hours
- Review/collaboration buffer included: 1 hours
- QA/rework buffer included: 0.5 hours
- This is a rough beginner estimate. Update the issue when new evidence changes the estimate; do not hide learning time.

## Planning metadata
- Priority: P0
- Sprint designation: sprint-1
- Milestone: Sprint 1 — MovePal MVP
- Initial Project stage: New
- Planned start: 2026-07-20
- Planned target: 2026-07-22
- Manual testing only: No

## Suggested verification
- JavaScript unit checks where practical
- Manual granted/denied/no-device/unsupported checklist
- Integration test with fallback upload

## Risks
- Browser requires HTTPS outside localhost.
- Repeated requests overload the development server.
- Camera remains active after navigation.

## Security and privacy
- Preview stays local until a selected frame is submitted.
- Do not save or log image data.

## Helpful documentation topics
- MDN `getUserMedia`, MediaStreamTrack stop, canvas blob capture
- Approved API contract

## Demo/evidence required
- Show camera success and then complete the same activity using fallback input.


---

<!-- task-id: MP-013 -->
# MP-013 — Pose service, landmark normalization, and visibility checks

## Value
Implement the isolated computer-vision service agreed in the spike. Convert image input into a small normalized domain representation that movement rules can consume and that tests can replace with fixtures. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## Detailed description and work sequence
Implement the isolated computer-vision service agreed in the spike. Convert image input into a small normalized domain representation that movement rules can consume and that tests can replace with fixtures.

Work sequence:

1. Pin and initialize the approved pose estimator without downloading assets during every request.

2. Decode validated image bytes safely and reject unreadable input.

3. Extract only required landmarks into typed/domain structures.

4. Implement visibility aggregation, full-body/required-joint checks, and no-person handling.

5. Normalize relative coordinates or distances needed by the specification.

6. Add dependency injection or a mock adapter for CI.

7. Document model/version assumptions and known limitations.

Dependency handling:

This task depends on MP-005, MP-008, MP-010, MP-007. Do not begin dependency-sensitive implementation until the listed outputs are available. The owner may perform reading or a disposable spike earlier, but must re-check assumptions after dependencies merge.

## Beginner learning objectives
- Wrap a third-party model behind a stable Python interface.
- Normalize landmarks and reason about visibility/confidence.
- Design deterministic tests around model boundaries.

## Deliverables
- `app/services/pose_tracking.py` implementation
- Typed landmark result structures
- Visibility/normalization helpers
- Mock adapter and unit tests

## Acceptance criteria
- The service returns a structured success, no-pose, low-visibility, or processing-error result.
- Movement modules do not import MediaPipe directly.
- Tests execute without camera access and without downloading a model.
- Unreadable bytes fail cleanly.
- The version and initialization strategy are documented.

## Definition of Done
- All acceptance criteria are demonstrated with evidence in the issue or pull request.
- Relevant documentation is updated so another beginner can repeat the work.
- No credentials, personal images, student emails, or raw volunteer recordings are committed.
- The task owner records decisions, assumptions, unresolved limitations, and follow-up work.
- A focused pull request uses the task ID in its title and links the issue with `Closes #...`.
- A reviewer other than the author examines the change, requested changes are resolved, and CI passes before merge.

## Dependencies and coordination
- Blocking dependencies: MP-005, MP-008, MP-010, MP-007
- Related coordination tasks: None
- Initial blocking status: blocked
- Do not mark this issue In Progress until required dependency outputs are available, except for a time-boxed learning spike that is explicitly recorded here.

## Ownership and review
- Team: MovePal Development
- Workstream: Computer Vision
- Suggested Scrum role: developer
- Primary assignee: myarnwas
- Contributors: None planned
- Suggested independent reviewer: AhmadKollab
- Planned effort allocation: @myarnwas: 8 h
- Pull request: Required
- Suggested branch: `mp-013-pose-service`

## Beginner estimate and buffers
- Focused-work estimate: 8 hours
- Investigation/learning buffer included: 2 hours
- Review/collaboration buffer included: 1 hours
- QA/rework buffer included: 0.5 hours
- This is a rough beginner estimate. Update the issue when new evidence changes the estimate; do not hide learning time.

## Planning metadata
- Priority: P0
- Sprint designation: sprint-1
- Milestone: Sprint 1 — MovePal MVP
- Initial Project stage: New
- Planned start: 2026-07-17
- Planned target: 2026-07-21
- Manual testing only: No

## Suggested verification
- Valid mock pose
- No-pose
- Low visibility
- Unreadable image
- Normalization invariance for scale/translation

## Risks
- MediaPipe initialization is slow or not thread-safe.
- Visibility thresholds reject valid users.
- Tests accidentally invoke the real model.

## Security and privacy
- Return only derived landmarks and status; never persist frames.

## Helpful documentation topics
- Approved pose ADR and movement schema
- OpenCV image decoding
- Python type hints/dataclasses

## Demo/evidence required
- Process one sample and show the compact structured result.


---

<!-- task-id: MP-014 -->
# MP-014 — Raise-both-arms rule, feedback mapping, and tests

## Value
Implement the first complete movement rule as the reference pattern for later rules. Detect both arms raised using visible shoulders/elbows/wrists and return friendly, specific feedback rather than a binary label. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## Detailed description and work sequence
Implement the first complete movement rule as the reference pattern for later rules. Detect both arms raised using visible shoulders/elbows/wrists and return friendly, specific feedback rather than a binary label.

Work sequence:

1. Re-read the movement specification and confirm coordinate direction and visibility conventions.

2. Implement a pure function that evaluates left and right arms independently and jointly.

3. Return structured observations such as success, one arm low, both arms low, body not visible, or hold required.

4. Map observations to friendly text without medical language.

5. Add fixture-based tests for correct, borderline, one-sided, low-confidence, and missing-joint cases.

6. Ask the reviewer to compare implementation line-by-line with the specification.

Dependency handling:

This task depends on MP-007, MP-013. Do not begin dependency-sensitive implementation until the listed outputs are available. The owner may perform reading or a disposable spike earlier, but must re-check assumptions after dependencies merge.

## Beginner learning objectives
- Implement geometric rules from a written specification.
- Separate scoring conditions from user-facing feedback.
- Use table-driven tests for boundary cases.

## Deliverables
- Raise-arms rule function
- Feedback mapping
- Unit fixtures and tests
- Threshold documentation

## Acceptance criteria
- Correct fixtures pass and incorrect fixtures do not.
- One-arm-low feedback identifies the relevant side consistently.
- Low visibility returns a visibility message rather than a movement failure.
- The rule is deterministic and independent of Flask/MediaPipe.
- Thresholds are configuration values, not unexplained literals.

## Definition of Done
- All acceptance criteria are demonstrated with evidence in the issue or pull request.
- Relevant documentation is updated so another beginner can repeat the work.
- No credentials, personal images, student emails, or raw volunteer recordings are committed.
- The task owner records decisions, assumptions, unresolved limitations, and follow-up work.
- A focused pull request uses the task ID in its title and links the issue with `Closes #...`.
- A reviewer other than the author examines the change, requested changes are resolved, and CI passes before merge.

## Dependencies and coordination
- Blocking dependencies: MP-007, MP-013
- Related coordination tasks: None
- Initial blocking status: blocked
- Do not mark this issue In Progress until required dependency outputs are available, except for a time-boxed learning spike that is explicitly recorded here.

## Ownership and review
- Team: MovePal Development
- Workstream: Computer Vision
- Suggested Scrum role: developer
- Primary assignee: myarnwas
- Contributors: @MennaAllah-Alatrsh
- Suggested independent reviewer: JHT127
- Planned effort allocation: @myarnwas: 5 h, @MennaAllah-Alatrsh: 2 h
- Pull request: Required
- Suggested branch: `mp-014-raise-arms-rule`

## Beginner estimate and buffers
- Focused-work estimate: 7 hours
- Investigation/learning buffer included: 1 hours
- Review/collaboration buffer included: 1 hours
- QA/rework buffer included: 0.5 hours
- This is a rough beginner estimate. Update the issue when new evidence changes the estimate; do not hide learning time.

## Planning metadata
- Priority: P0
- Sprint designation: sprint-1
- Milestone: Sprint 1 — MovePal MVP
- Initial Project stage: New
- Planned start: 2026-07-21
- Planned target: 2026-07-22
- Manual testing only: No

## Suggested verification
- Success
- Both arms low
- Left/right arm low
- Borderline threshold
- Low visibility
- Missing landmark

## Risks
- Coordinate direction is inverted.
- Threshold overfits a single pose.
- Feedback side labels are mirrored.

## Security and privacy
- Tests use synthetic or derived landmarks only.

## Helpful documentation topics
- Movement specification
- Parameterized pytest tests

## Demo/evidence required
- Run the rule test matrix and show one near-correct feedback example.


---

<!-- task-id: MP-015 -->
# MP-015 — Side-reach left/right rules, feedback, and tests

## Value
Implement side reach with explicit left and right variants, consistent camera/user-side semantics, and feedback for insufficient reach, bent posture where represented, low visibility, and success. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## Detailed description and work sequence
Implement side reach with explicit left and right variants, consistent camera/user-side semantics, and feedback for insufficient reach, bent posture where represented, low visibility, and success.

Work sequence:

1. Confirm whether labels refer to the user’s anatomical side and document the convention.

2. Implement reusable side-selection and horizontal/vertical comparison helpers.

3. Evaluate the requested side while checking required shoulder, wrist, hip, and visibility landmarks.

4. Return observations and friendly feedback for wrong side, insufficient reach, not visible, retry, and success.

5. Create mirrored fixture pairs and threshold-boundary tests.

6. Review for duplicated left/right code and inconsistent messages.

Dependency handling:

This task depends on MP-007, MP-013, MP-014. Do not begin dependency-sensitive implementation until the listed outputs are available. The owner may perform reading or a disposable spike earlier, but must re-check assumptions after dependencies merge.

## Beginner learning objectives
- Handle mirrored directional logic without duplication.
- Build reusable vector/relative-position helpers.
- Test left/right symmetry.

## Deliverables
- Side-reach rule for both directions
- Shared geometry helpers
- Feedback mappings
- Symmetry and edge-case tests

## Acceptance criteria
- Left and right variants pass mirrored test fixtures.
- The side convention is stated in UI and code documentation.
- Wrong-side movement receives a useful prompt.
- Low-confidence joints do not produce a false movement judgment.
- Pure rule tests require no web app or model.

## Definition of Done
- All acceptance criteria are demonstrated with evidence in the issue or pull request.
- Relevant documentation is updated so another beginner can repeat the work.
- No credentials, personal images, student emails, or raw volunteer recordings are committed.
- The task owner records decisions, assumptions, unresolved limitations, and follow-up work.
- A focused pull request uses the task ID in its title and links the issue with `Closes #...`.
- A reviewer other than the author examines the change, requested changes are resolved, and CI passes before merge.

## Dependencies and coordination
- Blocking dependencies: MP-007, MP-013, MP-014
- Related coordination tasks: None
- Initial blocking status: blocked
- Do not mark this issue In Progress until required dependency outputs are available, except for a time-boxed learning spike that is explicitly recorded here.

## Ownership and review
- Team: MovePal Development
- Workstream: Computer Vision
- Suggested Scrum role: developer
- Primary assignee: myarnwas
- Contributors: @MennaAllah-Alatrsh
- Suggested independent reviewer: AhmadKollab
- Planned effort allocation: @myarnwas: 4.5 h, @MennaAllah-Alatrsh: 2.5 h
- Pull request: Required
- Suggested branch: `mp-015-side-reach-rule`

## Beginner estimate and buffers
- Focused-work estimate: 7 hours
- Investigation/learning buffer included: 1 hours
- Review/collaboration buffer included: 1 hours
- QA/rework buffer included: 0.5 hours
- This is a rough beginner estimate. Update the issue when new evidence changes the estimate; do not hide learning time.

## Planning metadata
- Priority: P0
- Sprint designation: sprint-1
- Milestone: Sprint 1 — MovePal MVP
- Initial Project stage: New
- Planned start: 2026-07-22
- Planned target: 2026-07-23
- Manual testing only: No

## Suggested verification
- Left success/failure
- Right success/failure
- Mirrored symmetry
- Wrong side
- Visibility and threshold boundary

## Risks
- Mirrored preview causes confusing labels.
- One direction has different thresholds by mistake.

## Security and privacy
- Use derived fixture coordinates only.

## Helpful documentation topics
- Movement specification
- Raise-arms rule pattern
- Parameterized mirrored tests

## Demo/evidence required
- Show left and right fixture results with side-specific feedback.


---

<!-- task-id: MP-016 -->
# MP-016 — Knee-lift or step-in-place rule, feedback, and tests

## Value
Implement the third movement rule using relative knee/hip/ankle geometry and visibility checks. Support either leg so the activity remains simple and inclusive for the prototype. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## Detailed description and work sequence
Implement the third movement rule using relative knee/hip/ankle geometry and visibility checks. Support either leg so the activity remains simple and inclusive for the prototype.

Work sequence:

1. Confirm the simplest Sprint 1 interpretation: one visible knee lift or step-in-place success event.

2. Define required lower-body landmarks and full-body/partial-body behavior.

3. Implement a pure evaluator for left or right lift with configurable relative threshold.

4. Return feedback for move farther from camera, lift higher, hold briefly, low confidence, and success.

5. Add synthetic fixtures for left, right, neither, both, out-of-frame, and threshold boundary.

6. Document that this is a heuristic game rule, not exercise assessment.

Dependency handling:

This task depends on MP-007, MP-013, MP-014. Do not begin dependency-sensitive implementation until the listed outputs are available. The owner may perform reading or a disposable spike earlier, but must re-check assumptions after dependencies merge.

## Beginner learning objectives
- Design a rule for a lower-body movement.
- Handle either-side success and partial visibility.
- Test temporal/hold assumptions without adding a complex tracking system.

## Deliverables
- Knee-lift evaluator
- Feedback mapping
- Lower-body fixtures/tests
- Updated movement documentation

## Acceptance criteria
- Either valid leg can satisfy the activity.
- Out-of-frame lower body produces framing feedback.
- Threshold boundaries are tested.
- The rule stays independent of Flask and model initialization.
- No clinical interpretation is included.

## Definition of Done
- All acceptance criteria are demonstrated with evidence in the issue or pull request.
- Relevant documentation is updated so another beginner can repeat the work.
- No credentials, personal images, student emails, or raw volunteer recordings are committed.
- The task owner records decisions, assumptions, unresolved limitations, and follow-up work.
- A focused pull request uses the task ID in its title and links the issue with `Closes #...`.
- A reviewer other than the author examines the change, requested changes are resolved, and CI passes before merge.

## Dependencies and coordination
- Blocking dependencies: MP-007, MP-013, MP-014
- Related coordination tasks: None
- Initial blocking status: blocked
- Do not mark this issue In Progress until required dependency outputs are available, except for a time-boxed learning spike that is explicitly recorded here.

## Ownership and review
- Team: MovePal Development
- Workstream: Data/Evaluation
- Suggested Scrum role: developer
- Primary assignee: MennaAllah-Alatrsh
- Contributors: @myarnwas
- Suggested independent reviewer: alaamadii
- Planned effort allocation: @MennaAllah-Alatrsh: 5 h, @myarnwas: 2 h
- Pull request: Required
- Suggested branch: `mp-016-knee-lift-rule`

## Beginner estimate and buffers
- Focused-work estimate: 7 hours
- Investigation/learning buffer included: 1.5 hours
- Review/collaboration buffer included: 1 hours
- QA/rework buffer included: 0.5 hours
- This is a rough beginner estimate. Update the issue when new evidence changes the estimate; do not hide learning time.

## Planning metadata
- Priority: P0
- Sprint designation: sprint-1
- Milestone: Sprint 1 — MovePal MVP
- Initial Project stage: New
- Planned start: 2026-07-22
- Planned target: 2026-07-23
- Manual testing only: No

## Suggested verification
- Left success
- Right success
- No lift
- Out of frame
- Low visibility
- Boundary threshold

## Risks
- Lower-body landmarks are often outside the frame.
- A single frame cannot prove stepping motion.
- Rule wording implies health evaluation.

## Security and privacy
- Fixtures contain no images or identities.

## Helpful documentation topics
- Movement specification
- Pose landmark visibility
- Parameterized pytest fixtures

## Demo/evidence required
- Show correct and out-of-frame fixture responses.


---

<!-- task-id: MP-017 -->
# MP-017 — Friendly feedback orchestration and points/star scoring

## Value
Create the game-level feedback and reward service that turns rule observations into consistent messages, awards points/stars once per successful attempt, and avoids punitive or medical wording. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## Detailed description and work sequence
Create the game-level feedback and reward service that turns rule observations into consistent messages, awards points/stars once per successful attempt, and avoids punitive or medical wording.

Work sequence:

1. Collect all movement observations and define a common feedback result type.

2. Prioritize visibility/framing messages before technique messages.

3. Define retry, hold, success, and completion messages in one complete language.

4. Implement points/stars with a clear one-award-per-attempt/session rule.

5. Add tests for repeated success frames, retry, reset, and movement transition.

6. Review wording with the Product Owner for friendliness and disclaimer consistency.

Dependency handling:

This task depends on MP-014, MP-015, MP-016, MP-002. Do not begin dependency-sensitive implementation until the listed outputs are available. The owner may perform reading or a disposable spike earlier, but must re-check assumptions after dependencies merge.

## Beginner learning objectives
- Separate domain outcomes from presentation text.
- Design idempotent scoring so repeated frames do not award unlimited points.
- Test a small state machine.

## Deliverables
- Feedback service
- Scoring service
- Message catalog
- State/scoring unit tests

## Acceptance criteria
- Every rule observation maps to a user-facing message.
- Repeated identical success frames do not continually increase the score.
- Starting a new attempt/session resets the intended state.
- Messages are short, friendly, and non-medical.
- Scoring behavior is documented.

## Definition of Done
- All acceptance criteria are demonstrated with evidence in the issue or pull request.
- Relevant documentation is updated so another beginner can repeat the work.
- No credentials, personal images, student emails, or raw volunteer recordings are committed.
- The task owner records decisions, assumptions, unresolved limitations, and follow-up work.
- A focused pull request uses the task ID in its title and links the issue with `Closes #...`.
- A reviewer other than the author examines the change, requested changes are resolved, and CI passes before merge.

## Dependencies and coordination
- Blocking dependencies: MP-014, MP-015, MP-016, MP-002
- Related coordination tasks: None
- Initial blocking status: blocked
- Do not mark this issue In Progress until required dependency outputs are available, except for a time-boxed learning spike that is explicitly recorded here.

## Ownership and review
- Team: MovePal Development
- Workstream: Data/Evaluation
- Suggested Scrum role: developer
- Primary assignee: MennaAllah-Alatrsh
- Contributors: None planned
- Suggested independent reviewer: IslamOuda85
- Planned effort allocation: @MennaAllah-Alatrsh: 5 h, @alaamadii: 2 h
- Pull request: Required
- Suggested branch: `mp-017-feedback-scoring`

## Beginner estimate and buffers
- Focused-work estimate: 7 hours
- Investigation/learning buffer included: 1 hours
- Review/collaboration buffer included: 1 hours
- QA/rework buffer included: 0.5 hours
- This is a rough beginner estimate. Update the issue when new evidence changes the estimate; do not hide learning time.

## Planning metadata
- Priority: P0
- Sprint designation: sprint-1
- Milestone: Sprint 1 — MovePal MVP
- Initial Project stage: New
- Planned start: 2026-07-23
- Planned target: 2026-07-24
- Manual testing only: No

## Suggested verification
- One award per attempt
- Retry/no award
- Reset
- Visibility precedence
- Message coverage for all observations

## Risks
- Score can be farmed by repeated requests.
- Messages are inconsistent between movements.
- Feedback sounds judgmental.

## Security and privacy
- Feedback does not infer ability, health, diagnosis, or identity.

## Helpful documentation topics
- Movement observation contracts
- Simple finite-state machine patterns

## Demo/evidence required
- Replay repeated success input and show that points are awarded only once.


---

<!-- task-id: MP-018 -->
# MP-018 — Session state and end-of-session summary

## Value
Implement lightweight in-memory or browser-backed session state for selected activities, attempts, successes, points, and a short summary. Avoid authentication and a database while keeping state behavior testable and resettable. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## Detailed description and work sequence
Implement lightweight in-memory or browser-backed session state for selected activities, attempts, successes, points, and a short summary. Avoid authentication and a database while keeping state behavior testable and resettable.

Work sequence:

1. Define the minimum session record and where it lives for Sprint 1.

2. Implement start, record-attempt, record-success, next-activity, finish, and reset operations.

3. Generate a summary with activities attempted, successes, points/stars, and encouraging completion text.

4. Handle refresh, repeated finish calls, and invalid activity identifiers predictably.

5. Integrate through services/API rather than global mutable variables.

6. Add tests for independent sessions and reset behavior.

Dependency handling:

This task depends on MP-008, MP-017. Do not begin dependency-sensitive implementation until the listed outputs are available. The owner may perform reading or a disposable spike earlier, but must re-check assumptions after dependencies merge.

## Beginner learning objectives
- Choose an appropriately simple persistence boundary.
- Design session state and summary calculations.
- Test repeated and reset workflows.

## Deliverables
- Session-state service
- Summary service/API contract
- Unit and integration tests
- State limitations documentation

## Acceptance criteria
- A session records all three activities and points consistently.
- Reset starts a clean session.
- Two test clients do not accidentally share mutable state.
- Summary output is deterministic and friendly.
- No personal profile or long-term history is stored.

## Definition of Done
- All acceptance criteria are demonstrated with evidence in the issue or pull request.
- Relevant documentation is updated so another beginner can repeat the work.
- No credentials, personal images, student emails, or raw volunteer recordings are committed.
- The task owner records decisions, assumptions, unresolved limitations, and follow-up work.
- A focused pull request uses the task ID in its title and links the issue with `Closes #...`.
- A reviewer other than the author examines the change, requested changes are resolved, and CI passes before merge.

## Dependencies and coordination
- Blocking dependencies: MP-008, MP-017
- Related coordination tasks: None
- Initial blocking status: blocked
- Do not mark this issue In Progress until required dependency outputs are available, except for a time-boxed learning spike that is explicitly recorded here.

## Ownership and review
- Team: MovePal Development
- Workstream: Backend
- Suggested Scrum role: developer
- Primary assignee: AhmadKollab
- Contributors: @MennaAllah-Alatrsh
- Suggested independent reviewer: JHT127
- Planned effort allocation: @AhmadKollab: 5 h, @MennaAllah-Alatrsh: 2 h
- Pull request: Required
- Suggested branch: `mp-018-session-summary`

## Beginner estimate and buffers
- Focused-work estimate: 7 hours
- Investigation/learning buffer included: 1 hours
- Review/collaboration buffer included: 1 hours
- QA/rework buffer included: 0.5 hours
- This is a rough beginner estimate. Update the issue when new evidence changes the estimate; do not hide learning time.

## Planning metadata
- Priority: P0
- Sprint designation: sprint-1
- Milestone: Sprint 1 — MovePal MVP
- Initial Project stage: New
- Planned start: 2026-07-23
- Planned target: 2026-07-24
- Manual testing only: No

## Suggested verification
- Start/finish/reset
- Repeated finish
- Independent test clients
- Invalid movement
- Summary totals

## Risks
- Global state leaks between users.
- Refresh behavior surprises the user.
- Scope expands into accounts/history.

## Security and privacy
- Store no name, account, raw frame, or long-term movement history.

## Helpful documentation topics
- Flask session concepts or browser-local state
- Service isolation and test clients

## Demo/evidence required
- Complete a short fixture-based session and show the generated summary.


---

<!-- task-id: MP-019 -->
# MP-019 — End-to-end game loop integration

## Value
Connect activity selection, avatar/instructions, camera or fallback input, backend processing, movement rules, feedback, scoring, and session summary into one coherent user flow. This issue owns integration, not rewriting feature modules. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## Detailed description and work sequence
Connect activity selection, avatar/instructions, camera or fallback input, backend processing, movement rules, feedback, scoring, and session summary into one coherent user flow. This issue owns integration, not rewriting feature modules.

Work sequence:

1. Create an integration checklist from the contracts delivered by MP-010 through MP-018.

2. Wire the selected movement identifier and captured/fallback input to the API.

3. Render structured feedback, points, progress, retry, next movement, and summary states.

4. Prevent stale responses from updating a newer activity and handle network/server errors.

5. Add a deterministic integration path using checked-in tiny fixtures and mocked pose results.

6. Resolve contract mismatches in the owning modules through small coordinated commits.

7. Record known UI timing limitations rather than introducing WebSockets.

Dependency handling:

This task depends on MP-010, MP-011, MP-012, MP-013, MP-014, MP-015, MP-016, MP-017, MP-018. Do not begin dependency-sensitive implementation until the listed outputs are available. The owner may perform reading or a disposable spike earlier, but must re-check assumptions after dependencies merge.

## Beginner learning objectives
- Integrate independently developed frontend/backend/service contracts.
- Use browser and Flask debugging tools to isolate interface mismatches.
- Write integration tests around the user journey.

## Deliverables
- Complete playable web flow
- Integration tests and fixtures
- Integration decision notes
- Updated screenshots/demo evidence

## Acceptance criteria
- A user can complete all three activities with deterministic fallback samples.
- Camera input uses the same server contract when available.
- Feedback and score update without page errors.
- The session finishes with a summary and can restart.
- A failed request produces a recoverable message.
- No advanced streaming is required.

## Definition of Done
- All acceptance criteria are demonstrated with evidence in the issue or pull request.
- Relevant documentation is updated so another beginner can repeat the work.
- No credentials, personal images, student emails, or raw volunteer recordings are committed.
- The task owner records decisions, assumptions, unresolved limitations, and follow-up work.
- A focused pull request uses the task ID in its title and links the issue with `Closes #...`.
- A reviewer other than the author examines the change, requested changes are resolved, and CI passes before merge.

## Dependencies and coordination
- Blocking dependencies: MP-010, MP-011, MP-012, MP-013, MP-014, MP-015, MP-016, MP-017, MP-018
- Related coordination tasks: None
- Initial blocking status: blocked
- Do not mark this issue In Progress until required dependency outputs are available, except for a time-boxed learning spike that is explicitly recorded here.

## Ownership and review
- Team: MovePal Development
- Workstream: Frontend/UX
- Suggested Scrum role: developer
- Primary assignee: JHT127
- Contributors: @AhmadKollab
- Suggested independent reviewer: MennaAllah-Alatrsh
- Planned effort allocation: @JHT127: 4.7 h, @AhmadKollab: 3.3 h
- Pull request: Required
- Suggested branch: `mp-019-game-loop-integration`

## Beginner estimate and buffers
- Focused-work estimate: 8 hours
- Investigation/learning buffer included: 1 hours
- Review/collaboration buffer included: 1.5 hours
- QA/rework buffer included: 1 hours
- This is a rough beginner estimate. Update the issue when new evidence changes the estimate; do not hide learning time.

## Planning metadata
- Priority: P0
- Sprint designation: sprint-1
- Milestone: Sprint 1 — MovePal MVP
- Initial Project stage: New
- Planned start: 2026-07-23
- Planned target: 2026-07-27
- Manual testing only: No

## Suggested verification
- Full fallback journey
- Request failure/retry
- Score/summary consistency
- Activity transition
- Stale response guard

## Risks
- Contracts diverge between branches.
- Asynchronous responses update the wrong activity.
- Integration hides defects behind hard-coded demo behavior.

## Security and privacy
- Do not retain frames between requests or place them in browser storage.

## Helpful documentation topics
- API and service contracts from prerequisite tasks
- Flask integration testing

## Demo/evidence required
- Run the complete three-activity fallback journey from a clean session.


---

<!-- task-id: MP-020 -->
# MP-020 — Adult-only calibration protocol, consent template, and landmark extraction

## Value
Prepare a small, ethically bounded calibration/testing process using adults only. The task focuses on consent, collection instructions, private raw-data separation, and derived landmark extraction; it does not require a large dataset or publication of recordings. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## Detailed description and work sequence
Prepare a small, ethically bounded calibration/testing process using adults only. The task focuses on consent, collection instructions, private raw-data separation, and derived landmark extraction; it does not require a large dataset or publication of recordings.

Work sequence:

1. Define the minimum number and types of correct/incorrect examples needed to sanity-check three rules.

2. Write an adult-volunteer information/consent template and withdrawal/deletion instructions.

3. Define camera placement, lighting, framing, movement labels, anonymized IDs, and collection checklist.

4. Create an extraction script that reads a local private input folder and writes landmark JSON/CSV without names or background metadata.

5. Add `.gitignore` rules and documentation separating private recordings from derived data.

6. Run the protocol on synthetic/open examples or a consenting adult only if practical.

7. Document bias and limitations of a tiny convenience sample.

Dependency handling:

This task depends on MP-007, MP-013, MP-009. Do not begin dependency-sensitive implementation until the listed outputs are available. The owner may perform reading or a disposable spike earlier, but must re-check assumptions after dependencies merge.

## Beginner learning objectives
- Create a basic consent and withdrawal process.
- Apply data minimization to a computer-vision experiment.
- Separate private raw media from publishable derived fixtures.

## Deliverables
- `docs/consent_template.md`
- `docs/collection_protocol.md`
- `scripts/extract_landmarks.py`
- Private/derived data separation instructions
- Initial dataset card sections

## Acceptance criteria
- The protocol prohibits child participants.
- Consent explains purpose, storage, withdrawal, and no medical use.
- Raw media is ignored by Git and not required by CI.
- Extraction outputs anonymous derived landmarks.
- Correct and intentionally incorrect examples are represented in the plan.
- Known bias is documented.

## Definition of Done
- All acceptance criteria are demonstrated with evidence in the issue or pull request.
- Relevant documentation is updated so another beginner can repeat the work.
- No credentials, personal images, student emails, or raw volunteer recordings are committed.
- The task owner records decisions, assumptions, unresolved limitations, and follow-up work.
- A focused pull request uses the task ID in its title and links the issue with `Closes #...`.
- A reviewer other than the author examines the change, requested changes are resolved, and CI passes before merge.

## Dependencies and coordination
- Blocking dependencies: MP-007, MP-013, MP-009
- Related coordination tasks: None
- Initial blocking status: blocked
- Do not mark this issue In Progress until required dependency outputs are available, except for a time-boxed learning spike that is explicitly recorded here.

## Ownership and review
- Team: MovePal Development
- Workstream: Product/Documentation
- Suggested Scrum role: product_owner
- Primary assignee: IslamOuda85
- Contributors: @MennaAllah-Alatrsh
- Suggested independent reviewer: myarnwas
- Planned effort allocation: @IslamOuda85: 5 h, @MennaAllah-Alatrsh: 2 h
- Pull request: Required
- Suggested branch: `mp-020-calibration-protocol`

## Beginner estimate and buffers
- Focused-work estimate: 7 hours
- Investigation/learning buffer included: 2 hours
- Review/collaboration buffer included: 1 hours
- QA/rework buffer included: 0.5 hours
- This is a rough beginner estimate. Update the issue when new evidence changes the estimate; do not hide learning time.

## Planning metadata
- Priority: P1
- Sprint designation: sprint-1
- Milestone: Sprint 1 — MovePal MVP
- Initial Project stage: New
- Planned start: 2026-07-21
- Planned target: 2026-07-24
- Manual testing only: No

## Suggested verification
- Extraction script rejects unsupported files
- Output schema validation
- Git-ignore verification for private raw folder

## Risks
- Students accidentally commit identifiable media.
- Consent is treated as legal certification.
- Tiny sample is overgeneralized.

## Security and privacy
- Adults only; no child data.
- Keep raw recordings outside the repository.
- Use anonymized IDs and remove metadata.

## Helpful documentation topics
- Dataset cards
- Data minimization and informed consent basics
- Pose extraction service

## Demo/evidence required
- Show a local input → derived landmark output using a non-sensitive sample.


---

<!-- task-id: MP-021 -->
# MP-021 — Landmark fixtures, threshold calibration, and rule evaluation report

## Value
Build the deterministic fixture set used by tests and evaluate the three heuristic rules on correct, near-correct, incorrect, low-visibility, and framing cases. Adjust thresholds transparently without claiming validated accuracy. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## Detailed description and work sequence
Build the deterministic fixture set used by tests and evaluate the three heuristic rules on correct, near-correct, incorrect, low-visibility, and framing cases. Adjust thresholds transparently without claiming validated accuracy.

Work sequence:

1. Validate extracted/synthetic landmark files against the schema.

2. Label fixtures by movement, requested side, expected outcome, visibility, and source type.

3. Separate threshold-tuning examples from held-out sanity examples where sample size permits.

4. Run each rule across fixtures and record expected versus actual outcome.

5. Adjust only configurable thresholds with a written reason and re-run all tests.

6. Document false positives, false negatives, framing failures, and limitations.

7. Select a tiny stable subset for CI.

Dependency handling:

This task depends on MP-014, MP-015, MP-016, MP-020. Do not begin dependency-sensitive implementation until the listed outputs are available. The owner may perform reading or a disposable spike earlier, but must re-check assumptions after dependencies merge.

## Beginner learning objectives
- Create train/test-like separation for a small rule evaluation.
- Measure rule behavior with confusion-style counts and edge cases.
- Avoid tuning and reporting beyond the evidence.

## Deliverables
- Versioned anonymized landmark fixtures
- Evaluation script or parameterized tests
- `docs/calibration_report.md`
- Updated configurable thresholds

## Acceptance criteria
- Each movement has positive, negative, borderline, and low-visibility examples.
- Expected labels are documented and machine-readable.
- All changes to thresholds are traceable to evidence.
- A held-out or clearly separate sanity subset is used where possible.
- Report language says prototype heuristic evaluation, not model validation.

## Definition of Done
- All acceptance criteria are demonstrated with evidence in the issue or pull request.
- Relevant documentation is updated so another beginner can repeat the work.
- No credentials, personal images, student emails, or raw volunteer recordings are committed.
- The task owner records decisions, assumptions, unresolved limitations, and follow-up work.
- A focused pull request uses the task ID in its title and links the issue with `Closes #...`.
- A reviewer other than the author examines the change, requested changes are resolved, and CI passes before merge.

## Dependencies and coordination
- Blocking dependencies: MP-014, MP-015, MP-016, MP-020
- Related coordination tasks: None
- Initial blocking status: blocked
- Do not mark this issue In Progress until required dependency outputs are available, except for a time-boxed learning spike that is explicitly recorded here.

## Ownership and review
- Team: MovePal Development
- Workstream: Data/Evaluation
- Suggested Scrum role: developer
- Primary assignee: MennaAllah-Alatrsh
- Contributors: @myarnwas
- Suggested independent reviewer: JHT127
- Planned effort allocation: @MennaAllah-Alatrsh: 4 h, @myarnwas: 1.5 h, @alaamadii: 2.5 h
- Pull request: Required
- Suggested branch: `mp-021-landmark-evaluation`

## Beginner estimate and buffers
- Focused-work estimate: 8 hours
- Investigation/learning buffer included: 2 hours
- Review/collaboration buffer included: 1 hours
- QA/rework buffer included: 1 hours
- This is a rough beginner estimate. Update the issue when new evidence changes the estimate; do not hide learning time.

## Planning metadata
- Priority: P1
- Sprint designation: sprint-1
- Milestone: Sprint 1 — MovePal MVP
- Initial Project stage: New
- Planned start: 2026-07-23
- Planned target: 2026-07-27
- Manual testing only: No

## Suggested verification
- Schema validation
- Parameterized rule evaluation
- Regression checks for all three movements

## Risks
- Same examples are used to tune and claim success.
- Fixtures reveal volunteer identity.
- Threshold changes break another movement.

## Security and privacy
- Commit landmarks only after checking they contain no names, paths, or image metadata.

## Helpful documentation topics
- Movement test matrix
- Simple confusion matrix and error analysis
- Dataset card

## Demo/evidence required
- Show the evaluation summary and one documented failure case.


---

<!-- task-id: MP-022 -->
# MP-022 — Windows/Linux CI with lint, tests, compile, and Flask smoke check

## Value
Implement a beginner-readable GitHub Actions workflow that validates portable Python code on Windows and Linux without cameras, large datasets, private recordings, or model downloads. Treat CI as student-owned product work. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## Detailed description and work sequence
Implement a beginner-readable GitHub Actions workflow that validates portable Python code on Windows and Linux without cameras, large datasets, private recordings, or model downloads. Treat CI as student-owned product work.

Work sequence:

1. Review current workflow and dependency versions.

2. Run checkout and Python setup on `ubuntu-latest` and `windows-latest` with Python 3.11.

3. Cache pip dependencies where it improves reliability.

4. Install runtime and development dependencies.

5. Run Ruff lint/format checks, pytest, `compileall`, and Flask factory import/smoke test with clear step names.

6. Ensure tests mock pose estimation and use tiny fixtures.

7. Intentionally trigger one safe failure on a branch and document how to read the log.

8. Update contribution instructions with required checks.

Dependency handling:

This task depends on MP-008, MP-013, MP-014, MP-015, MP-016, MP-018. Do not begin dependency-sensitive implementation until the listed outputs are available. The owner may perform reading or a disposable spike earlier, but must re-check assumptions after dependencies merge.

## Beginner learning objectives
- Read and modify a GitHub Actions workflow.
- Understand matrix testing, dependency caching, linting, pytest, and smoke tests.
- Diagnose failures from logs.

## Deliverables
- `.github/workflows/ci.yml`
- CI troubleshooting documentation
- Evidence of passing Windows/Linux jobs

## Acceptance criteria
- Pushes and PRs to `master` trigger uniquely named checks.
- Both OS jobs pass on the repository state.
- No camera, secret, raw dataset, or model download is required.
- A lint/test failure is easy for a beginner to locate.
- Workflow permissions are minimal.

## Definition of Done
- All acceptance criteria are demonstrated with evidence in the issue or pull request.
- Relevant documentation is updated so another beginner can repeat the work.
- No credentials, personal images, student emails, or raw volunteer recordings are committed.
- The task owner records decisions, assumptions, unresolved limitations, and follow-up work.
- A focused pull request uses the task ID in its title and links the issue with `Closes #...`.
- A reviewer other than the author examines the change, requested changes are resolved, and CI passes before merge.

## Dependencies and coordination
- Blocking dependencies: MP-008, MP-013, MP-014, MP-015, MP-016, MP-018
- Related coordination tasks: None
- Initial blocking status: blocked
- Do not mark this issue In Progress until required dependency outputs are available, except for a time-boxed learning spike that is explicitly recorded here.

## Ownership and review
- Team: MovePal Development
- Workstream: Testing/DevOps
- Suggested Scrum role: scrum_master
- Primary assignee: alaamadii
- Contributors: @AhmadKollab
- Suggested independent reviewer: MennaAllah-Alatrsh
- Planned effort allocation: @alaamadii: 7.5 h, @AhmadKollab: 0.5 h
- Pull request: Required
- Suggested branch: `mp-022-cross-platform-ci`

## Beginner estimate and buffers
- Focused-work estimate: 8 hours
- Investigation/learning buffer included: 2 hours
- Review/collaboration buffer included: 1 hours
- QA/rework buffer included: 0.5 hours
- This is a rough beginner estimate. Update the issue when new evidence changes the estimate; do not hide learning time.

## Planning metadata
- Priority: P0
- Sprint designation: sprint-1
- Milestone: Sprint 1 — MovePal MVP
- Initial Project stage: New
- Planned start: 2026-07-20
- Planned target: 2026-07-24
- Manual testing only: No

## Suggested verification
- CI itself on Windows/Linux
- Factory import
- Unit/integration suite
- Compileall

## Risks
- MediaPipe installation differs by OS.
- Tests accidentally initialize the real camera/model.
- Workflow hides failures behind continue-on-error.

## Security and privacy
- Do not upload private fixtures or verbose logs containing input data.

## Helpful documentation topics
- GitHub Actions Python workflow documentation
- Ruff and pytest documentation

## Demo/evidence required
- Open a successful matrix run and explain each check.


---

<!-- task-id: MP-023 -->
# MP-023 — Security, privacy, accessibility, and error-message hardening

## Value
Review the integrated application against Sprint 1 safeguards before release-candidate freeze. Fix high-value issues in input handling, logging, data retention, disclaimer visibility, keyboard use, responsive layout, and user-facing errors. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## Detailed description and work sequence
Review the integrated application against Sprint 1 safeguards before release-candidate freeze. Fix high-value issues in input handling, logging, data retention, disclaimer visibility, keyboard use, responsive layout, and user-facing errors.

Work sequence:

1. Review upload limits/types, temporary files, debug configuration, error details, and dependency handling.

2. Inspect logs and browser storage to ensure no frames, landmarks, names, or secrets are retained unexpectedly.

3. Verify privacy notice and non-medical disclaimer are visible before/while using camera features.

4. Run keyboard, focus, label, contrast, status-message, and mobile-width checks.

5. Review all error messages for actionable next steps and no stack traces.

6. Open separate issues for findings too large for this sprint and fix P0/P1 findings through focused commits.

7. Document residual risk and limitations.

Dependency handling:

This task depends on MP-010, MP-011, MP-012, MP-019, MP-009. Do not begin dependency-sensitive implementation until the listed outputs are available. The owner may perform reading or a disposable spike earlier, but must re-check assumptions after dependencies merge.

## Beginner learning objectives
- Perform a focused non-exhaustive security/privacy/accessibility review.
- Turn review findings into small verifiable fixes.
- Distinguish must-fix defects from future improvements.

## Deliverables
- Hardening checklist and findings
- Focused fixes
- Updated privacy/accessibility/error documentation
- Deferred issues where needed

## Acceptance criteria
- No debug traceback is shown to normal users.
- Invalid/oversized inputs fail safely.
- No image or landmark payload appears in normal logs.
- Camera/privacy/disclaimer text is visible.
- Core controls work by keyboard at mobile width.
- All P0 findings are resolved or explicitly block release.

## Definition of Done
- All acceptance criteria are demonstrated with evidence in the issue or pull request.
- Relevant documentation is updated so another beginner can repeat the work.
- No credentials, personal images, student emails, or raw volunteer recordings are committed.
- The task owner records decisions, assumptions, unresolved limitations, and follow-up work.
- A focused pull request uses the task ID in its title and links the issue with `Closes #...`.
- A reviewer other than the author examines the change, requested changes are resolved, and CI passes before merge.

## Dependencies and coordination
- Blocking dependencies: MP-010, MP-011, MP-012, MP-019, MP-009
- Related coordination tasks: None
- Initial blocking status: blocked
- Do not mark this issue In Progress until required dependency outputs are available, except for a time-boxed learning spike that is explicitly recorded here.

## Ownership and review
- Team: MovePal Development
- Workstream: Product/Documentation
- Suggested Scrum role: product_owner
- Primary assignee: IslamOuda85
- Contributors: @alaamadii, @JHT127
- Suggested independent reviewer: myarnwas
- Planned effort allocation: @IslamOuda85: 4 h, @alaamadii: 1.5 h, @JHT127: 1.5 h
- Pull request: Required
- Suggested branch: `mp-023-hardening-review`

## Beginner estimate and buffers
- Focused-work estimate: 7 hours
- Investigation/learning buffer included: 2 hours
- Review/collaboration buffer included: 1 hours
- QA/rework buffer included: 1 hours
- This is a rough beginner estimate. Update the issue when new evidence changes the estimate; do not hide learning time.

## Planning metadata
- Priority: P0
- Sprint designation: sprint-1
- Milestone: Sprint 1 — MovePal MVP
- Initial Project stage: New
- Planned start: 2026-07-24
- Planned target: 2026-07-27
- Manual testing only: No

## Suggested verification
- Invalid/oversized input regression
- No-debug production config
- Keyboard/mobile manual checklist
- Log inspection

## Risks
- Checklist creates false confidence.
- Late fixes destabilize the app.
- Accessibility is reduced to visual inspection only.

## Security and privacy
- Privacy notice and data minimization are release criteria.

## Helpful documentation topics
- OWASP file upload basics
- Flask error handling
- WCAG introductory checks

## Demo/evidence required
- Show one rejected invalid input, keyboard navigation, and visible disclaimer.


---

<!-- task-id: MP-024 -->
# MP-024 — Integration regression, release-candidate freeze, and QA handoff

## Value
Create a stable release candidate for final-day external QA. Merge only reviewed work, run the complete deterministic journey, freeze the tested commit, and provide a precise manual QA handoff package. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## Detailed description and work sequence
Create a stable release candidate for final-day external QA. Merge only reviewed work, run the complete deterministic journey, freeze the tested commit, and provide a precise manual QA handoff package.

Work sequence:

1. Confirm all P0 feature issues are merged and statuses/dependencies are current.

2. Create a release-candidate checklist covering fresh install, startup, fallback journey, optional camera, three movements, errors, score, summary, privacy, and CI.

3. Run the complete automated suite locally and in GitHub Actions on the candidate commit.

4. Run deterministic fallback regression on Windows and, where available, another OS/browser.

5. Record exact commit SHA/version and stop merging unrelated changes.

6. Prepare QA instructions, expected behavior, sample data, environment template, and defect-report template.

7. Mark the candidate QA-ready only when blockers are absent.

Dependency handling:

This task depends on MP-019, MP-021, MP-022, MP-023. Do not begin dependency-sensitive implementation until the listed outputs are available. The owner may perform reading or a disposable spike earlier, but must re-check assumptions after dependencies merge.

## Beginner learning objectives
- Prepare a release candidate and testable handoff.
- Run regression checks across integrated features.
- Coordinate freeze, defect triage, and evidence.

## Deliverables
- Release-candidate commit/tag or documented SHA
- `docs/qa_handoff.md`
- Regression evidence
- QA-ready checklist

## Acceptance criteria
- All required CI jobs pass on the frozen commit.
- The fallback demo completes all three movements.
- Fresh-start instructions were followed from a clean environment.
- QA receives commit, environment, sample, expected results, and issue format.
- Unresolved blockers prevent QA-ready status.

## Definition of Done
- All acceptance criteria are demonstrated with evidence in the issue or pull request.
- Relevant documentation is updated so another beginner can repeat the work.
- No credentials, personal images, student emails, or raw volunteer recordings are committed.
- The task owner records decisions, assumptions, unresolved limitations, and follow-up work.
- A focused pull request uses the task ID in its title and links the issue with `Closes #...`.
- A reviewer other than the author examines the change, requested changes are resolved, and CI passes before merge.

## Dependencies and coordination
- Blocking dependencies: MP-019, MP-021, MP-022, MP-023
- Related coordination tasks: None
- Initial blocking status: blocked
- Do not mark this issue In Progress until required dependency outputs are available, except for a time-boxed learning spike that is explicitly recorded here.

## Ownership and review
- Team: MovePal Development
- Workstream: Testing/DevOps
- Suggested Scrum role: scrum_master
- Primary assignee: alaamadii
- Contributors: @AhmadKollab, @myarnwas, @JHT127
- Suggested independent reviewer: IslamOuda85
- Planned effort allocation: @alaamadii: 2 h, @AhmadKollab: 2 h, @myarnwas: 2 h, @JHT127: 2 h
- Pull request: Required
- Suggested branch: `mp-024-release-candidate`

## Beginner estimate and buffers
- Focused-work estimate: 8 hours
- Investigation/learning buffer included: 1 hours
- Review/collaboration buffer included: 1 hours
- QA/rework buffer included: 1.5 hours
- This is a rough beginner estimate. Update the issue when new evidence changes the estimate; do not hide learning time.

## Planning metadata
- Priority: P0
- Sprint designation: sprint-1
- Milestone: Sprint 1 — MovePal MVP
- Initial Project stage: New
- Planned start: 2026-07-27
- Planned target: 2026-07-28
- Manual testing only: No

## Suggested verification
- Full automated suite
- Fresh install/startup
- Fallback three-movement regression
- Optional camera smoke check

## Risks
- Release candidate is cut before documentation or fallback works.
- Late merges invalidate the tested SHA.
- QA cannot reproduce the environment.

## Security and privacy
- QA package contains no private recordings or student emails.

## Helpful documentation topics
- Definition of Done
- QA plan and issue templates

## Demo/evidence required
- Show CI for the frozen SHA and complete fallback regression.


---

<!-- task-id: MP-025 -->
# MP-025 — Final-day QA triage, targeted fixes, retest, and release decision

## Value
During the final QA day, receive manual findings from MP-028 through MP-033, classify them consistently, fix only release-critical or safely bounded defects, request retest, and record the release decision. The QA issues are related evidence rather than formal dependencies so all QA can execute in parallel from MP-024. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## Detailed description and work sequence
During the final QA day, receive manual findings from MP-028 through MP-033, classify them consistently, fix only release-critical or safely bounded defects, request retest, and record the release decision. The QA issues are related evidence rather than formal dependencies so all QA can execute in parallel from MP-024.

Work sequence:

1. Monitor the six QA issues and require complete reproduction evidence.

2. Classify each finding as must fix in Sprint 1, should fix, future improvement, or invalid/needs information.

3. Assign bugs to the feature owner and avoid broad refactoring.

4. Require a small PR, independent review, and CI for every code fix.

5. Ask the reporting QA member or another Team A member to retest the exact candidate.

6. Update the release candidate only after all must-fix issues are closed or explicitly documented as blockers.

7. Record remaining known issues and the final release decision.

Dependency handling:

This task depends on MP-024. Do not begin dependency-sensitive implementation until the listed outputs are available. The owner may perform reading or a disposable spike earlier, but must re-check assumptions after dependencies merge.

Related coordination tasks: MP-028, MP-029, MP-030, MP-031, MP-032, MP-033. These are not blockers unless the issue is explicitly marked blocked.

## Beginner learning objectives
- Triage defects by severity and Sprint Goal impact.
- Make controlled late changes and request independent retest.
- Record a transparent release/no-release decision.

## Deliverables
- QA triage table
- Targeted fix PRs
- Retest evidence
- Final release/no-release decision and known-issues list

## Acceptance criteria
- Every QA finding has a classification and owner.
- Must-fix defects are resolved and retested or the release is blocked.
- No fix bypasses review and CI.
- Known limitations are visible in release/demo documentation.
- The final tested commit is recorded.

## Definition of Done
- All acceptance criteria are demonstrated with evidence in the issue or pull request.
- Relevant documentation is updated so another beginner can repeat the work.
- No credentials, personal images, student emails, or raw volunteer recordings are committed.
- The task owner records decisions, assumptions, unresolved limitations, and follow-up work.
- A focused pull request uses the task ID in its title and links the issue with `Closes #...`.
- A reviewer other than the author examines the change, requested changes are resolved, and CI passes before merge.

## Dependencies and coordination
- Blocking dependencies: MP-024
- Related coordination tasks: MP-028, MP-029, MP-030, MP-031, MP-032, MP-033
- Initial blocking status: blocked
- Do not mark this issue In Progress until required dependency outputs are available, except for a time-boxed learning spike that is explicitly recorded here.

## Ownership and review
- Team: MovePal Development
- Workstream: Testing/DevOps
- Suggested Scrum role: scrum_master
- Primary assignee: alaamadii
- Contributors: @IslamOuda85, @AhmadKollab, @myarnwas, @JHT127, @MennaAllah-Alatrsh
- Suggested independent reviewer: Tojan-Naiem
- Planned effort allocation: @alaamadii: 2.5 h, @IslamOuda85: 0.5 h, @AhmadKollab: 1 h, @myarnwas: 1 h, @JHT127: 1 h, @MennaAllah-Alatrsh: 1 h
- Pull request: Required
- Suggested branch: `mp-025-final-qa-fixes`

## Beginner estimate and buffers
- Focused-work estimate: 7 hours
- Investigation/learning buffer included: 0.5 hours
- Review/collaboration buffer included: 2 hours
- QA/rework buffer included: 2 hours
- This is a rough beginner estimate. Update the issue when new evidence changes the estimate; do not hide learning time.

## Planning metadata
- Priority: P0
- Sprint designation: sprint-1
- Milestone: Sprint 1 — MovePal MVP
- Initial Project stage: New
- Planned start: 2026-07-29
- Planned target: 2026-07-29
- Manual testing only: No

## Suggested verification
- Targeted regression for each fix
- Full CI after final merge
- Reporter retest

## Risks
- Late fixes introduce regressions.
- QA findings lack enough evidence.
- Team treats “demo works once” as release quality.

## Security and privacy
- Bug evidence must not expose identifiable images or volunteer data.

## Helpful documentation topics
- QA issue template
- Definition of Done
- Release-candidate checklist

## Demo/evidence required
- Show triage status, retest evidence, and final tested commit.


---

<!-- task-id: MP-026 -->
# MP-026 — Final README, demonstration package, contribution record, and retrospective

## Value
Finish the course-facing package after final QA: reproducible README, live-camera and fallback demo script, contribution/review evidence, limitations, release notes, and a short retrospective focused on Scrum learning. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## Detailed description and work sequence
Finish the course-facing package after final QA: reproducible README, live-camera and fallback demo script, contribution/review evidence, limitations, release notes, and a short retrospective focused on Scrum learning.

Work sequence:

1. Re-run README instructions against the final tested commit and correct versions/commands.

2. Create a 10–12 minute demo plan with fallback samples ready before the live camera attempt.

3. Prepare release notes listing delivered MVP, known issues, privacy limitations, and deferred work.

4. Generate a contribution table from issues/PRs/reviews without ranking students by raw count alone.

5. Verify every member authored or substantively contributed and reviewed another PR.

6. Run a retrospective covering what helped, what blocked, and concrete next actions.

7. Store final screenshots or short non-sensitive evidence.

Dependency handling:

This task depends on MP-025. Do not begin dependency-sensitive implementation until the listed outputs are available. The owner may perform reading or a disposable spike earlier, but must re-check assumptions after dependencies merge.

## Beginner learning objectives
- Prepare a reliable technical demonstration.
- Summarize evidence rather than only describing intentions.
- Reflect on process, collaboration, and technical debt.

## Deliverables
- Final `README.md` and linked docs
- `docs/demo_plan.md`
- Release notes/known issues
- Contribution/review report
- `docs/retrospective.md`

## Acceptance criteria
- A clean machine can follow the final instructions.
- The demo succeeds with included fallback data if camera mode fails.
- All three movements, points, feedback, summary, privacy, and disclaimer are demonstrated.
- Contribution evidence includes authorship and reviews for all six members.
- Retrospective identifies at least one process improvement and one technical follow-up.

## Definition of Done
- All acceptance criteria are demonstrated with evidence in the issue or pull request.
- Relevant documentation is updated so another beginner can repeat the work.
- No credentials, personal images, student emails, or raw volunteer recordings are committed.
- The task owner records decisions, assumptions, unresolved limitations, and follow-up work.
- A focused pull request uses the task ID in its title and links the issue with `Closes #...`.
- A reviewer other than the author examines the change, requested changes are resolved, and CI passes before merge.

## Dependencies and coordination
- Blocking dependencies: MP-025
- Related coordination tasks: None
- Initial blocking status: blocked
- Do not mark this issue In Progress until required dependency outputs are available, except for a time-boxed learning spike that is explicitly recorded here.

## Ownership and review
- Team: MovePal Development
- Workstream: Product/Documentation
- Suggested Scrum role: product_owner
- Primary assignee: IslamOuda85
- Contributors: @alaamadii
- Suggested independent reviewer: JHT127
- Planned effort allocation: @IslamOuda85: 5.5 h, @alaamadii: 1.5 h
- Pull request: Required
- Suggested branch: `mp-026-final-demo-docs`

## Beginner estimate and buffers
- Focused-work estimate: 7 hours
- Investigation/learning buffer included: 0.5 hours
- Review/collaboration buffer included: 1 hours
- QA/rework buffer included: 0.5 hours
- This is a rough beginner estimate. Update the issue when new evidence changes the estimate; do not hide learning time.

## Planning metadata
- Priority: P0
- Sprint designation: sprint-1
- Milestone: Sprint 1 — MovePal MVP
- Initial Project stage: New
- Planned start: 2026-07-29
- Planned target: 2026-07-29
- Manual testing only: No

## Suggested verification
- Fresh README run
- Fallback demo rehearsal
- Link check
- Contribution/review completeness check

## Risks
- Documentation reflects an older commit.
- Demo relies only on live camera.
- Contribution report rewards issue count rather than substance.

## Security and privacy
- Demo assets and screenshots must be non-identifying and consented/licensed.

## Helpful documentation topics
- Definition of Done
- Final QA summary
- GitHub PR/review history

## Demo/evidence required
- Deliver the final scripted demonstration and show fallback readiness.


---

<!-- task-id: MP-027 -->
# MP-027 — Sprint rituals and instructor checkpoint checklist

## Value
Track the minimum useful Scrum rituals without creating one issue per ten-minute meeting. Use dated checklists for daily development stand-ups and Monday/Wednesday instructor checkpoints, focusing on decisions, blockers, and board accuracy. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## Detailed description and work sequence
Track the minimum useful Scrum rituals without creating one issue per ten-minute meeting. Use dated checklists for daily development stand-ups and Monday/Wednesday instructor checkpoints, focusing on decisions, blockers, and board accuracy.

Work sequence:

1. Create dated checklist entries for each sprint workday and instructor checkpoint.

2. At each development stand-up record only yesterday/today/blocker/action summaries.

3. Before each checkpoint update issue status, dependencies, estimates, and risks.

4. Record instructor decisions and assign follow-up actions to existing issues.

5. Review workload balance mid-sprint and move or pair work when necessary.

6. Close with Sprint Review/retrospective references rather than duplicating them.

Dependency handling:

This task depends on MP-001. Do not begin dependency-sensitive implementation until the listed outputs are available. The owner may perform reading or a disposable spike earlier, but must re-check assumptions after dependencies merge.

## Beginner learning objectives
- Use short Scrum events to inspect and adapt work.
- Keep the board synchronized with reality.
- Escalate blockers early without turning meetings into status theatre.

## Deliverables
- One Sprint Rituals issue/checklist
- Checkpoint decision log
- Mid-sprint workload review

## Acceptance criteria
- The issue covers all planned dates without creating meeting micro-issues.
- Blockers link to the affected work item.
- Board status is corrected during each checkpoint.
- Workload adjustments include a reason.
- Meeting notes do not expose private student information.

## Definition of Done
- All acceptance criteria are demonstrated with evidence in the issue or pull request.
- Relevant documentation is updated so another beginner can repeat the work.
- No credentials, personal images, student emails, or raw volunteer recordings are committed.
- The task owner records decisions, assumptions, unresolved limitations, and follow-up work.

## Dependencies and coordination
- Blocking dependencies: MP-001
- Related coordination tasks: None
- Initial blocking status: blocked
- Do not mark this issue In Progress until required dependency outputs are available, except for a time-boxed learning spike that is explicitly recorded here.

## Ownership and review
- Team: MovePal Development
- Workstream: Testing/DevOps
- Suggested Scrum role: scrum_master
- Primary assignee: alaamadii
- Contributors: None planned
- Suggested independent reviewer: IslamOuda85
- Planned effort allocation: @alaamadii: 4 h
- Pull request: Not required; evidence belongs in this issue and linked defects
- Suggested branch: `not-applicable`

## Beginner estimate and buffers
- Focused-work estimate: 4 hours
- Investigation/learning buffer included: 0.5 hours
- Review/collaboration buffer included: 0.5 hours
- QA/rework buffer included: 0 hours
- This is a rough beginner estimate. Update the issue when new evidence changes the estimate; do not hide learning time.

## Planning metadata
- Priority: P1
- Sprint designation: sprint-1
- Milestone: Sprint 1 — MovePal MVP
- Initial Project stage: New
- Planned start: 2026-07-14
- Planned target: 2026-07-29
- Manual testing only: No

## Suggested verification
- Instructor or Product Owner samples board accuracy twice during the sprint.

## Risks
- Checklist becomes busywork.
- Issues remain stale despite meetings.

## Security and privacy
- Record project blockers, not personal performance or sensitive circumstances.

## Helpful documentation topics
- Scrum Daily Scrum and Sprint Review purposes
- Project board workflow

## Demo/evidence required
- Show how one blocker moved through the checklist and linked issue.


---

<!-- task-id: MP-028 -->
# MP-028 — Final-day manual QA: clean installation, startup, and README sanity

## Value
Independently verify that a beginner can obtain the frozen MovePal release candidate, create a clean environment, install dependencies, run tests, start Flask, and reach the application by following only the documented instructions. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## Detailed description and work sequence
Independently verify that a beginner can obtain the frozen MovePal release candidate, create a clean environment, install dependencies, run tests, start Flask, and reach the application by following only the documented instructions.

Work sequence:

1. Use a clean folder and new Python 3.11 virtual environment.

2. Record OS, Python, Git, browser, and tested commit.

3. Follow README clone/install/test/start commands without undocumented corrections.

4. Confirm no secret, camera, private dataset, or raw recording is required to start.

5. Open the application and fallback sample mode.

6. For every failure, record command, complete relevant error, expected/actual result, severity, and evidence.

7. Retest only after Team B provides a fixed commit.

Dependency handling:

This task depends on MP-024. Do not begin dependency-sensitive implementation until the listed outputs are available. The owner may perform reading or a disposable spike earlier, but must re-check assumptions after dependencies merge.

## Beginner learning objectives
- Execute a reproducible clean-install test.
- Separate documentation defects from environment-specific failures.
- Report exact commands and versions.

## Deliverables
- Completed installation/startup checklist
- Environment and tested commit record
- Separate bug/documentation issues for failures
- Retest result

## Acceptance criteria
- A clean environment reaches the application or a reproducible blocking issue is filed.
- README commands are executed exactly and deviations are reported.
- Tests/CI expectations are compared with local behavior.
- Evidence is sufficient for Team B to reproduce.

## Definition of Done
- All acceptance criteria are demonstrated with evidence in the issue or pull request.
- Relevant documentation is updated so another beginner can repeat the work.
- No credentials, personal images, student emails, or raw volunteer recordings are committed.
- The task owner records decisions, assumptions, unresolved limitations, and follow-up work.
- Manual checks record environment, exact steps, expected result, actual result, severity, evidence, tested commit, and retest result.
- The QA member does not implement feature code as part of this issue; defects are opened as separate bug issues for Team B.

## Dependencies and coordination
- Blocking dependencies: MP-024
- Related coordination tasks: None
- Initial blocking status: blocked
- Do not mark this issue In Progress until required dependency outputs are available, except for a time-boxed learning spike that is explicitly recorded here.

## Ownership and review
- Team: MovePal QA
- Workstream: QA
- Suggested Scrum role: developer
- Primary assignee: Tojan-Naiem
- Contributors: None planned
- Suggested independent reviewer: alaamadii
- Planned effort allocation: @Tojan-Naiem: 3.5 h
- Pull request: Not required; evidence belongs in this issue and linked defects
- Suggested branch: `not-applicable`

## Beginner estimate and buffers
- Focused-work estimate: 3.5 hours
- Investigation/learning buffer included: 0.5 hours
- Review/collaboration buffer included: 0 hours
- QA/rework buffer included: 3 hours
- This is a rough beginner estimate. Update the issue when new evidence changes the estimate; do not hide learning time.

## Planning metadata
- Priority: P0
- Sprint designation: sprint-1
- Milestone: Sprint 1 — MovePal MVP
- Initial Project stage: New
- Planned start: 2026-07-29
- Planned target: 2026-07-29
- Manual testing only: Yes

## Suggested verification
- Manual clean clone/install/test/start
- Fallback page smoke test

## Risks
- The tested commit differs from the frozen release candidate.
- Evidence is incomplete or contains private imagery.
- A failure is described vaguely instead of reproducibly.

## Security and privacy
- Use included non-sensitive samples where possible.
- Redact screenshots and never attach volunteer raw recordings or student emails.

## Helpful documentation topics
- `docs/qa_handoff.md`
- QA issue template
- Frozen release-candidate commit

## Demo/evidence required
- Show the clean environment, startup command, and loaded application or blocking defect.


---

<!-- task-id: MP-029 -->
# MP-029 — Final-day manual QA: camera permission, no-camera, browser, and fallback sanity

## Value
Verify that camera use is understandable and recoverable across permission granted, denied, unavailable, unsupported, or insecure-context situations, and that fallback mode remains fully usable. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## Detailed description and work sequence
Verify that camera use is understandable and recoverable across permission granted, denied, unavailable, unsupported, or insecure-context situations, and that fallback mode remains fully usable.

Work sequence:

1. Record OS, browser/version, device availability, and tested commit.

2. Confirm camera permission is requested only after explicit user action.

3. Test granted permission when a camera is available and confirm preview/stop behavior.

4. Test denial or blocked permission and confirm a friendly recovery path.

5. Test no-camera/unsupported behavior where feasible using browser/device controls.

6. Complete at least one activity through fallback mode.

7. Check privacy wording near camera controls and file separate defects for each distinct failure.

Dependency handling:

This task depends on MP-024. Do not begin dependency-sensitive implementation until the listed outputs are available. The owner may perform reading or a disposable spike earlier, but must re-check assumptions after dependencies merge.

## Beginner learning objectives
- Test browser permission and device-failure paths.
- Recognize privacy and recovery requirements.
- Capture browser/version-specific evidence.

## Deliverables
- Permission/fallback matrix
- Screenshots or notes with no identifiable imagery
- Bug issues and retest results

## Acceptance criteria
- All tested permission states have an understandable result.
- Denial/no-camera does not trap the user.
- Fallback mode can continue the session.
- Camera stops after session/end/navigation where observable.
- Browser-specific limitations are documented.

## Definition of Done
- All acceptance criteria are demonstrated with evidence in the issue or pull request.
- Relevant documentation is updated so another beginner can repeat the work.
- No credentials, personal images, student emails, or raw volunteer recordings are committed.
- The task owner records decisions, assumptions, unresolved limitations, and follow-up work.
- Manual checks record environment, exact steps, expected result, actual result, severity, evidence, tested commit, and retest result.
- The QA member does not implement feature code as part of this issue; defects are opened as separate bug issues for Team B.

## Dependencies and coordination
- Blocking dependencies: MP-024
- Related coordination tasks: None
- Initial blocking status: blocked
- Do not mark this issue In Progress until required dependency outputs are available, except for a time-boxed learning spike that is explicitly recorded here.

## Ownership and review
- Team: MovePal QA
- Workstream: QA
- Suggested Scrum role: developer
- Primary assignee: SajaZenaty
- Contributors: None planned
- Suggested independent reviewer: JHT127
- Planned effort allocation: @SajaZenaty: 3.5 h
- Pull request: Not required; evidence belongs in this issue and linked defects
- Suggested branch: `not-applicable`

## Beginner estimate and buffers
- Focused-work estimate: 3.5 hours
- Investigation/learning buffer included: 0.5 hours
- Review/collaboration buffer included: 0 hours
- QA/rework buffer included: 3 hours
- This is a rough beginner estimate. Update the issue when new evidence changes the estimate; do not hide learning time.

## Planning metadata
- Priority: P0
- Sprint designation: sprint-1
- Milestone: Sprint 1 — MovePal MVP
- Initial Project stage: New
- Planned start: 2026-07-29
- Planned target: 2026-07-29
- Manual testing only: Yes

## Suggested verification
- Manual grant/deny/no-device/unsupported/fallback matrix

## Risks
- The tested commit differs from the frozen release candidate.
- Evidence is incomplete or contains private imagery.
- A failure is described vaguely instead of reproducibly.

## Security and privacy
- Use included non-sensitive samples where possible.
- Redact screenshots and never attach volunteer raw recordings or student emails.

## Helpful documentation topics
- `docs/qa_handoff.md`
- QA issue template
- Frozen release-candidate commit

## Demo/evidence required
- Show denial recovery and fallback completion.


---

<!-- task-id: MP-030 -->
# MP-030 — Final-day manual QA: pose visibility and three-movement sanity

## Value
Exercise pose and rule behavior for raise both arms, side reach left/right, and knee lift using included samples and, where safe, an adult tester. Focus on correct/incorrect, low-light, partial-body, multiple-person, side-direction, and low-confidence outcomes. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## Detailed description and work sequence
Exercise pose and rule behavior for raise both arms, side reach left/right, and knee lift using included samples and, where safe, an adult tester. Focus on correct/incorrect, low-light, partial-body, multiple-person, side-direction, and low-confidence outcomes.

Work sequence:

1. Record environment, commit, input source, camera placement, and lighting without identifying the tester.

2. Verify all three movements with known-correct fallback samples.

3. Try known-incorrect or near-correct examples and inspect feedback.

4. Test left/right side reach and note mirrored-preview interpretation.

5. Test partial body, person too close/far, low light, and low-confidence handling.

6. Observe multiple-person behavior without claiming unsupported accuracy.

7. File defects with movement, side, conditions, expected/actual, severity, evidence, and retest result.

Dependency handling:

This task depends on MP-024. Do not begin dependency-sensitive implementation until the listed outputs are available. The owner may perform reading or a disposable spike earlier, but must re-check assumptions after dependencies merge.

## Beginner learning objectives
- Perform black-box testing of heuristic computer-vision behavior.
- Distinguish expected limitation from defect.
- Report reproducible input conditions.

## Deliverables
- Movement/condition QA matrix
- Defect issues for false success, false failure, or unclear visibility feedback
- Retest evidence

## Acceptance criteria
- Each movement has at least one success and one failure/near-correct check.
- Left/right behavior is explicitly checked.
- Visibility/framing failures produce useful feedback or are reported.
- Known limitations are separated from regressions.
- No child participates.

## Definition of Done
- All acceptance criteria are demonstrated with evidence in the issue or pull request.
- Relevant documentation is updated so another beginner can repeat the work.
- No credentials, personal images, student emails, or raw volunteer recordings are committed.
- The task owner records decisions, assumptions, unresolved limitations, and follow-up work.
- Manual checks record environment, exact steps, expected result, actual result, severity, evidence, tested commit, and retest result.
- The QA member does not implement feature code as part of this issue; defects are opened as separate bug issues for Team B.

## Dependencies and coordination
- Blocking dependencies: MP-024
- Related coordination tasks: None
- Initial blocking status: blocked
- Do not mark this issue In Progress until required dependency outputs are available, except for a time-boxed learning spike that is explicitly recorded here.

## Ownership and review
- Team: MovePal QA
- Workstream: QA
- Suggested Scrum role: developer
- Primary assignee: nezarYousef
- Contributors: None planned
- Suggested independent reviewer: myarnwas
- Planned effort allocation: @nezarYousef: 3.5 h
- Pull request: Not required; evidence belongs in this issue and linked defects
- Suggested branch: `not-applicable`

## Beginner estimate and buffers
- Focused-work estimate: 3.5 hours
- Investigation/learning buffer included: 0.5 hours
- Review/collaboration buffer included: 0 hours
- QA/rework buffer included: 3 hours
- This is a rough beginner estimate. Update the issue when new evidence changes the estimate; do not hide learning time.

## Planning metadata
- Priority: P0
- Sprint designation: sprint-1
- Milestone: Sprint 1 — MovePal MVP
- Initial Project stage: New
- Planned start: 2026-07-29
- Planned target: 2026-07-29
- Manual testing only: Yes

## Suggested verification
- Manual movement/visibility matrix

## Risks
- The tested commit differs from the frozen release candidate.
- Evidence is incomplete or contains private imagery.
- A failure is described vaguely instead of reproducibly.

## Security and privacy
- Use included non-sensitive samples where possible.
- Redact screenshots and never attach volunteer raw recordings or student emails.

## Helpful documentation topics
- `docs/qa_handoff.md`
- QA issue template
- Frozen release-candidate commit

## Demo/evidence required
- Show the completed matrix and one reproducible edge case.


---

<!-- task-id: MP-031 -->
# MP-031 — Final-day manual QA: feedback, scoring, repeated session, reset, and summary

## Value
Verify that feedback is friendly and consistent, points/stars are awarded correctly, repeated frames do not inflate scores, session restart/reset works, and the final summary matches the performed activities. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## Detailed description and work sequence
Verify that feedback is friendly and consistent, points/stars are awarded correctly, repeated frames do not inflate scores, session restart/reset works, and the final summary matches the performed activities.

Work sequence:

1. Start from a fresh session and record the tested commit.

2. Check feedback for visibility, retry, hold, success, and movement-specific adjustment.

3. Repeat a successful sample several times and observe whether points duplicate incorrectly.

4. Complete activities in different orders where supported.

5. Finish the session and compare summary activities/successes/points with observed actions.

6. Reset/restart and verify old state does not leak.

7. Repeat the session once and report any stale feedback, score, or summary.

Dependency handling:

This task depends on MP-024. Do not begin dependency-sensitive implementation until the listed outputs are available. The owner may perform reading or a disposable spike earlier, but must re-check assumptions after dependencies merge.

## Beginner learning objectives
- Test stateful behavior and boundary transitions.
- Detect duplicated awards and stale state.
- Evaluate consistency of user-facing feedback.

## Deliverables
- State/scoring test log
- Expected-versus-actual summary table
- Defect and retest records

## Acceptance criteria
- Points follow the documented award rule.
- Reset produces a clean state.
- Summary totals match the session.
- Messages remain friendly and non-medical.
- Repeated sessions do not share stale state.

## Definition of Done
- All acceptance criteria are demonstrated with evidence in the issue or pull request.
- Relevant documentation is updated so another beginner can repeat the work.
- No credentials, personal images, student emails, or raw volunteer recordings are committed.
- The task owner records decisions, assumptions, unresolved limitations, and follow-up work.
- Manual checks record environment, exact steps, expected result, actual result, severity, evidence, tested commit, and retest result.
- The QA member does not implement feature code as part of this issue; defects are opened as separate bug issues for Team B.

## Dependencies and coordination
- Blocking dependencies: MP-024
- Related coordination tasks: None
- Initial blocking status: blocked
- Do not mark this issue In Progress until required dependency outputs are available, except for a time-boxed learning spike that is explicitly recorded here.

## Ownership and review
- Team: MovePal QA
- Workstream: QA
- Suggested Scrum role: developer
- Primary assignee: saliqasarwi
- Contributors: None planned
- Suggested independent reviewer: MennaAllah-Alatrsh
- Planned effort allocation: @saliqasarwi: 3.5 h
- Pull request: Not required; evidence belongs in this issue and linked defects
- Suggested branch: `not-applicable`

## Beginner estimate and buffers
- Focused-work estimate: 3.5 hours
- Investigation/learning buffer included: 0.5 hours
- Review/collaboration buffer included: 0 hours
- QA/rework buffer included: 3 hours
- This is a rough beginner estimate. Update the issue when new evidence changes the estimate; do not hide learning time.

## Planning metadata
- Priority: P0
- Sprint designation: sprint-1
- Milestone: Sprint 1 — MovePal MVP
- Initial Project stage: New
- Planned start: 2026-07-29
- Planned target: 2026-07-29
- Manual testing only: Yes

## Suggested verification
- Manual scoring/session state matrix

## Risks
- The tested commit differs from the frozen release candidate.
- Evidence is incomplete or contains private imagery.
- A failure is described vaguely instead of reproducibly.

## Security and privacy
- Use included non-sensitive samples where possible.
- Redact screenshots and never attach volunteer raw recordings or student emails.

## Helpful documentation topics
- `docs/qa_handoff.md`
- QA issue template
- Frozen release-candidate commit

## Demo/evidence required
- Show a completed session, reset, and clean second session.


---

<!-- task-id: MP-032 -->
# MP-032 — Final-day manual QA: invalid input, oversized file, errors, privacy, and disclaimer

## Value
Verify defensive behavior and visible privacy boundaries. Test malformed, unsupported, and oversized inputs, server/client errors, logging exposure, camera explanation, data-retention wording, and non-medical disclaimer visibility. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## Detailed description and work sequence
Verify defensive behavior and visible privacy boundaries. Test malformed, unsupported, and oversized inputs, server/client errors, logging exposure, camera explanation, data-retention wording, and non-medical disclaimer visibility.

Work sequence:

1. Record environment and tested commit.

2. Submit missing, empty, unsupported, renamed, corrupted, and oversized files using safe test data.

3. Observe status, message, recovery, and whether stack traces/internal paths are exposed.

4. Inspect normal browser storage/network/log output for unexpected image, landmark, secret, or personal-data retention.

5. Verify privacy notice and disclaimer are visible and understandable before or during input use.

6. Confirm fallback samples do not contain personal data.

7. File separate defects for security/privacy, error-message, and documentation problems.

Dependency handling:

This task depends on MP-024. Do not begin dependency-sensitive implementation until the listed outputs are available. The owner may perform reading or a disposable spike earlier, but must re-check assumptions after dependencies merge.

## Beginner learning objectives
- Run negative testing safely.
- Inspect privacy/security behavior without penetration testing.
- Report information leakage and unclear errors.

## Deliverables
- Negative-input matrix
- Privacy/disclaimer checklist
- Redacted defect evidence and retest results

## Acceptance criteria
- Invalid input never crashes the normal UI.
- No stack trace or secret is exposed.
- Oversized input is rejected with a useful message.
- No normal log/browser storage unexpectedly retains frames.
- Non-medical disclaimer and no-child-data statement are visible.

## Definition of Done
- All acceptance criteria are demonstrated with evidence in the issue or pull request.
- Relevant documentation is updated so another beginner can repeat the work.
- No credentials, personal images, student emails, or raw volunteer recordings are committed.
- The task owner records decisions, assumptions, unresolved limitations, and follow-up work.
- Manual checks record environment, exact steps, expected result, actual result, severity, evidence, tested commit, and retest result.
- The QA member does not implement feature code as part of this issue; defects are opened as separate bug issues for Team B.

## Dependencies and coordination
- Blocking dependencies: MP-024
- Related coordination tasks: None
- Initial blocking status: blocked
- Do not mark this issue In Progress until required dependency outputs are available, except for a time-boxed learning spike that is explicitly recorded here.

## Ownership and review
- Team: MovePal QA
- Workstream: QA
- Suggested Scrum role: developer
- Primary assignee: SaadRayh
- Contributors: None planned
- Suggested independent reviewer: AhmadKollab
- Planned effort allocation: @SaadRayh: 3.5 h
- Pull request: Not required; evidence belongs in this issue and linked defects
- Suggested branch: `not-applicable`

## Beginner estimate and buffers
- Focused-work estimate: 3.5 hours
- Investigation/learning buffer included: 0.5 hours
- Review/collaboration buffer included: 0 hours
- QA/rework buffer included: 3 hours
- This is a rough beginner estimate. Update the issue when new evidence changes the estimate; do not hide learning time.

## Planning metadata
- Priority: P0
- Sprint designation: sprint-1
- Milestone: Sprint 1 — MovePal MVP
- Initial Project stage: New
- Planned start: 2026-07-29
- Planned target: 2026-07-29
- Manual testing only: Yes

## Suggested verification
- Manual negative-input/privacy checklist

## Risks
- The tested commit differs from the frozen release candidate.
- Evidence is incomplete or contains private imagery.
- A failure is described vaguely instead of reproducibly.

## Security and privacy
- Use included non-sensitive samples where possible.
- Redact screenshots and never attach volunteer raw recordings or student emails.

## Helpful documentation topics
- `docs/qa_handoff.md`
- QA issue template
- Frozen release-candidate commit

## Demo/evidence required
- Show safe rejection of one invalid and one oversized input plus visible disclaimer.


---

<!-- task-id: MP-033 -->
# MP-033 — Final-day manual QA: responsive accessibility sanity and consolidated QA report

## Value
Run final responsive, keyboard, readability, browser-width, and end-to-end sanity checks, then consolidate Team A findings into a release-oriented QA summary without replacing the individual defect issues. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## Detailed description and work sequence
Run final responsive, keyboard, readability, browser-width, and end-to-end sanity checks, then consolidate Team A findings into a release-oriented QA summary without replacing the individual defect issues.

Work sequence:

1. Record environment, browser, viewport widths, and tested commit.

2. Navigate activity selection, input choice, retry, next, summary, and reset using keyboard only.

3. Check visible focus, labels, heading order, readable feedback, status announcements where available, and non-color-only meaning.

4. Test desktop and approximately 360px mobile width for clipping or unusable controls.

5. Run one complete fallback journey as a final sanity pass.

6. Collect links to MP-028 through MP-032 findings and classify pass/fail/not tested.

7. Write a concise QA summary with blockers, important defects, known limitations, and retest status for MP-025.

Dependency handling:

This task depends on MP-024. Do not begin dependency-sensitive implementation until the listed outputs are available. The owner may perform reading or a disposable spike earlier, but must re-check assumptions after dependencies merge.

## Beginner learning objectives
- Perform an introductory accessibility/responsive sanity check.
- Consolidate distributed QA evidence.
- Communicate release risk and retest status.

## Deliverables
- Responsive/accessibility checklist
- Final fallback sanity evidence
- `docs/qa_final_report.md` or issue summary linking all findings

## Acceptance criteria
- Core controls are keyboard reachable or defects are filed.
- Mobile-width layout remains usable or defects are filed.
- One complete fallback journey is recorded.
- The report links every QA issue and defect.
- Blockers and retest status are unambiguous.

## Definition of Done
- All acceptance criteria are demonstrated with evidence in the issue or pull request.
- Relevant documentation is updated so another beginner can repeat the work.
- No credentials, personal images, student emails, or raw volunteer recordings are committed.
- The task owner records decisions, assumptions, unresolved limitations, and follow-up work.
- Manual checks record environment, exact steps, expected result, actual result, severity, evidence, tested commit, and retest result.
- The QA member does not implement feature code as part of this issue; defects are opened as separate bug issues for Team B.

## Dependencies and coordination
- Blocking dependencies: MP-024
- Related coordination tasks: None
- Initial blocking status: blocked
- Do not mark this issue In Progress until required dependency outputs are available, except for a time-boxed learning spike that is explicitly recorded here.

## Ownership and review
- Team: MovePal QA
- Workstream: QA
- Suggested Scrum role: developer
- Primary assignee: BaraahMazeen
- Contributors: None planned
- Suggested independent reviewer: IslamOuda85
- Planned effort allocation: @BaraahMazeen: 3.5 h
- Pull request: Not required; evidence belongs in this issue and linked defects
- Suggested branch: `not-applicable`

## Beginner estimate and buffers
- Focused-work estimate: 3.5 hours
- Investigation/learning buffer included: 0.5 hours
- Review/collaboration buffer included: 0 hours
- QA/rework buffer included: 3 hours
- This is a rough beginner estimate. Update the issue when new evidence changes the estimate; do not hide learning time.

## Planning metadata
- Priority: P0
- Sprint designation: sprint-1
- Milestone: Sprint 1 — MovePal MVP
- Initial Project stage: New
- Planned start: 2026-07-29
- Planned target: 2026-07-29
- Manual testing only: Yes

## Suggested verification
- Manual keyboard/mobile/final journey checklist

## Risks
- The tested commit differs from the frozen release candidate.
- Evidence is incomplete or contains private imagery.
- A failure is described vaguely instead of reproducibly.

## Security and privacy
- Use included non-sensitive samples where possible.
- Redact screenshots and never attach volunteer raw recordings or student emails.

## Helpful documentation topics
- `docs/qa_handoff.md`
- QA issue template
- Frozen release-candidate commit

## Demo/evidence required
- Present the consolidated QA status and release blockers/non-blockers.


---

<!-- task-id: MP-034 -->
# MP-034 — Cross-browser compatibility baseline and support matrix

## Value
Define and verify a realistic browser support policy beyond the final-day sanity checks, including camera API behavior, upload fallback, CSS/JavaScript compatibility, and documented unsupported cases. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## Detailed description and work sequence
Define and verify a realistic browser support policy beyond the final-day sanity checks, including camera API behavior, upload fallback, CSS/JavaScript compatibility, and documented unsupported cases.

Work sequence:

1. Select target desktop/mobile browsers based on course/product needs.

2. Create a reproducible compatibility matrix and browser-specific test scripts.

3. Run camera, fallback, game flow, error, and summary checks on each target.

4. Add polyfills or guarded feature detection only where justified.

5. Time-box an investigation spike and record alternatives, compatibility, cost, and risks.

6. Split implementation into pull requests small enough for one beginner working day where necessary.

7. Arrange an independent design/code review and update documentation before considering the task complete.

Dependency handling:

This task depends on MP-024. Do not begin dependency-sensitive implementation until the listed outputs are available. The owner may perform reading or a disposable spike earlier, but must re-check assumptions after dependencies merge.

## Beginner learning objectives
- Investigate the technologies and design choices needed for cross-browser compatibility baseline and support matrix before implementation.
- Break a production-oriented concern into evidence-backed, reviewable increments.
- Document trade-offs, tests, operational impact, and limitations for future maintainers.

## Deliverables
- Browser support policy
- Compatibility matrix with versions and results
- Feature-detection improvements
- Investigation notes/ADR
- Updated operational or user documentation

## Acceptance criteria
- Supported browsers complete the fallback journey.
- Unsupported features produce clear guidance instead of JavaScript failure.
- Camera-specific differences are documented.
- The selected approach is justified against at least one alternative.
- Automated or repeatable manual verification is documented.
- Remaining limitations and follow-up tasks are recorded.

## Definition of Done
- All acceptance criteria are demonstrated with evidence in the issue or pull request.
- Relevant documentation is updated so another beginner can repeat the work.
- No credentials, personal images, student emails, or raw volunteer recordings are committed.
- The task owner records decisions, assumptions, unresolved limitations, and follow-up work.
- A focused pull request uses the task ID in its title and links the issue with `Closes #...`.
- A reviewer other than the author examines the change, requested changes are resolved, and CI passes before merge.

## Dependencies and coordination
- Blocking dependencies: MP-024
- Related coordination tasks: None
- Initial blocking status: blocked
- Do not mark this issue In Progress until required dependency outputs are available, except for a time-boxed learning spike that is explicitly recorded here.

## Ownership and review
- Team: MovePal Development
- Workstream: Testing/DevOps
- Suggested Scrum role: developer
- Primary assignee: Unassigned until later sprint planning
- Contributors: None planned
- Suggested independent reviewer: Assign during later sprint planning; reviewer must differ from author
- Planned effort allocation: Not assigned in the current sprint
- Pull request: Required
- Suggested branch: `mp-034-cross-browser-compatibility-baseline-and`

## Beginner estimate and buffers
- Focused-work estimate: 12 hours
- Investigation/learning buffer included: 2.4 hours
- Review/collaboration buffer included: 1.8 hours
- QA/rework buffer included: 1.8 hours
- This is a rough beginner estimate. Update the issue when new evidence changes the estimate; do not hide learning time.

## Planning metadata
- Priority: P2
- Sprint designation: post-sprint
- Milestone: Post-Sprint Stabilization
- Initial Project stage: Backlog
- Planned start: Not scheduled
- Planned target: Not scheduled
- Manual testing only: No

## Suggested verification
- Repeatable browser checklist
- Automated frontend smoke tests where practical

## Risks
- Browser versions change rapidly.
- Testing relies on only one physical device.

## Security and privacy
- Do not use real personal recordings as compatibility fixtures.

## Helpful documentation topics
- Relevant official library/framework documentation
- Existing MovePal ADRs, tests, and limitations

## Demo/evidence required
- Demonstrate one supported and one gracefully unsupported browser.


---

<!-- task-id: MP-035 -->
# MP-035 — Performance profiling and response-time budget

## Value
Measure where time and memory are spent in image decoding, pose inference, rule evaluation, API serialization, and browser requests, then define a practical prototype performance budget. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## Detailed description and work sequence
Measure where time and memory are spent in image decoding, pose inference, rule evaluation, API serialization, and browser requests, then define a practical prototype performance budget.

Work sequence:

1. Instrument representative requests without logging image data.

2. Measure cold start, warm request, memory, and repeated-request behavior.

3. Identify the largest bottleneck and compare safe optimizations.

4. Add a documented request-rate/capture-interval recommendation.

5. Time-box an investigation spike and record alternatives, compatibility, cost, and risks.

6. Split implementation into pull requests small enough for one beginner working day where necessary.

7. Arrange an independent design/code review and update documentation before considering the task complete.

Dependency handling:

This task depends on MP-024. Do not begin dependency-sensitive implementation until the listed outputs are available. The owner may perform reading or a disposable spike earlier, but must re-check assumptions after dependencies merge.

## Beginner learning objectives
- Investigate the technologies and design choices needed for performance profiling and response-time budget before implementation.
- Break a production-oriented concern into evidence-backed, reviewable increments.
- Document trade-offs, tests, operational impact, and limitations for future maintainers.

## Deliverables
- Profiling report
- Performance budget
- Targeted optimization PRs
- Regression benchmark
- Investigation notes/ADR
- Updated operational or user documentation

## Acceptance criteria
- Representative fallback requests meet the agreed budget on a reference machine.
- Measurements distinguish model startup from steady state.
- Optimizations preserve test behavior.
- The selected approach is justified against at least one alternative.
- Automated or repeatable manual verification is documented.
- Remaining limitations and follow-up tasks are recorded.

## Definition of Done
- All acceptance criteria are demonstrated with evidence in the issue or pull request.
- Relevant documentation is updated so another beginner can repeat the work.
- No credentials, personal images, student emails, or raw volunteer recordings are committed.
- The task owner records decisions, assumptions, unresolved limitations, and follow-up work.
- A focused pull request uses the task ID in its title and links the issue with `Closes #...`.
- A reviewer other than the author examines the change, requested changes are resolved, and CI passes before merge.

## Dependencies and coordination
- Blocking dependencies: MP-024
- Related coordination tasks: None
- Initial blocking status: blocked
- Do not mark this issue In Progress until required dependency outputs are available, except for a time-boxed learning spike that is explicitly recorded here.

## Ownership and review
- Team: MovePal Development
- Workstream: Backend
- Suggested Scrum role: developer
- Primary assignee: Unassigned until later sprint planning
- Contributors: None planned
- Suggested independent reviewer: Assign during later sprint planning; reviewer must differ from author
- Planned effort allocation: Not assigned in the current sprint
- Pull request: Required
- Suggested branch: `mp-035-performance-profiling-and-response-time`

## Beginner estimate and buffers
- Focused-work estimate: 14 hours
- Investigation/learning buffer included: 2.8 hours
- Review/collaboration buffer included: 2.1 hours
- QA/rework buffer included: 2.1 hours
- This is a rough beginner estimate. Update the issue when new evidence changes the estimate; do not hide learning time.

## Planning metadata
- Priority: P2
- Sprint designation: post-sprint
- Milestone: Post-Sprint Stabilization
- Initial Project stage: Backlog
- Planned start: Not scheduled
- Planned target: Not scheduled
- Manual testing only: No

## Suggested verification
- Benchmark script with non-sensitive fixtures
- Regression comparison before/after

## Risks
- Micro-benchmarks do not represent browser use.
- Optimization reduces readability or accuracy.

## Security and privacy
- Profiling output must not contain images or identifying paths.

## Helpful documentation topics
- Relevant official library/framework documentation
- Existing MovePal ADRs, tests, and limitations

## Demo/evidence required
- Show measured latency breakdown and one justified optimization.


---

<!-- task-id: MP-036 -->
# MP-036 — Production-like local packaging and configuration

## Value
Create a reproducible non-debug way to run MovePal locally for demonstrations or controlled deployment, with environment-based configuration, a production WSGI server, and clear separation from developer settings. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## Detailed description and work sequence
Create a reproducible non-debug way to run MovePal locally for demonstrations or controlled deployment, with environment-based configuration, a production WSGI server, and clear separation from developer settings.

Work sequence:

1. Compare beginner-compatible WSGI servers and Windows/Linux support.

2. Define environment variables and secure defaults.

3. Add start commands/scripts without hard-coded paths.

4. Verify clean install and shutdown behavior on both OS families.

5. Time-box an investigation spike and record alternatives, compatibility, cost, and risks.

6. Split implementation into pull requests small enough for one beginner working day where necessary.

7. Arrange an independent design/code review and update documentation before considering the task complete.

Dependency handling:

This task depends on MP-024, MP-035. Do not begin dependency-sensitive implementation until the listed outputs are available. The owner may perform reading or a disposable spike earlier, but must re-check assumptions after dependencies merge.

## Beginner learning objectives
- Investigate the technologies and design choices needed for production-like local packaging and configuration before implementation.
- Break a production-oriented concern into evidence-backed, reviewable increments.
- Document trade-offs, tests, operational impact, and limitations for future maintainers.

## Deliverables
- Production-like run configuration
- Environment reference
- Windows/Linux startup instructions
- Investigation notes/ADR
- Updated operational or user documentation

## Acceptance criteria
- Debug mode is disabled.
- A documented command starts the app on Windows and Linux.
- Missing configuration fails clearly.
- The selected approach is justified against at least one alternative.
- Automated or repeatable manual verification is documented.
- Remaining limitations and follow-up tasks are recorded.

## Definition of Done
- All acceptance criteria are demonstrated with evidence in the issue or pull request.
- Relevant documentation is updated so another beginner can repeat the work.
- No credentials, personal images, student emails, or raw volunteer recordings are committed.
- The task owner records decisions, assumptions, unresolved limitations, and follow-up work.
- A focused pull request uses the task ID in its title and links the issue with `Closes #...`.
- A reviewer other than the author examines the change, requested changes are resolved, and CI passes before merge.

## Dependencies and coordination
- Blocking dependencies: MP-024, MP-035
- Related coordination tasks: None
- Initial blocking status: blocked
- Do not mark this issue In Progress until required dependency outputs are available, except for a time-boxed learning spike that is explicitly recorded here.

## Ownership and review
- Team: MovePal Development
- Workstream: Testing/DevOps
- Suggested Scrum role: developer
- Primary assignee: Unassigned until later sprint planning
- Contributors: None planned
- Suggested independent reviewer: Assign during later sprint planning; reviewer must differ from author
- Planned effort allocation: Not assigned in the current sprint
- Pull request: Required
- Suggested branch: `mp-036-production-like-local-packaging-and`

## Beginner estimate and buffers
- Focused-work estimate: 12 hours
- Investigation/learning buffer included: 2.4 hours
- Review/collaboration buffer included: 1.8 hours
- QA/rework buffer included: 1.8 hours
- This is a rough beginner estimate. Update the issue when new evidence changes the estimate; do not hide learning time.

## Planning metadata
- Priority: P2
- Sprint designation: post-sprint
- Milestone: Post-Sprint Stabilization
- Initial Project stage: Backlog
- Planned start: Not scheduled
- Planned target: Not scheduled
- Manual testing only: No

## Suggested verification
- Startup smoke test
- Configuration validation tests

## Risks
- Chosen server has platform limitations.
- Configuration defaults accidentally expose the app.

## Security and privacy
- No secrets are committed; bind/network exposure is documented.

## Helpful documentation topics
- Relevant official library/framework documentation
- Existing MovePal ADRs, tests, and limitations

## Demo/evidence required
- Start the packaged app from a clean environment on two OSes.


---

<!-- task-id: MP-037 -->
# MP-037 — Persistent session storage design

## Value
Investigate and implement optional persistence for anonymous session summaries without introducing accounts. Define retention, deletion, schema, concurrency, and migration behavior before replacing Sprint 1 ephemeral state. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## Detailed description and work sequence
Investigate and implement optional persistence for anonymous session summaries without introducing accounts. Define retention, deletion, schema, concurrency, and migration behavior before replacing Sprint 1 ephemeral state.

Work sequence:

1. Write concrete persistence use cases and reject unnecessary personal fields.

2. Compare JSON/CSV, SQLite, and browser-local storage.

3. Design schema, identifiers, retention, deletion, and corruption handling.

4. Implement behind a repository/service interface with migration tests.

5. Time-box an investigation spike and record alternatives, compatibility, cost, and risks.

6. Split implementation into pull requests small enough for one beginner working day where necessary.

7. Arrange an independent design/code review and update documentation before considering the task complete.

Dependency handling:

This task depends on MP-018, MP-023. Do not begin dependency-sensitive implementation until the listed outputs are available. The owner may perform reading or a disposable spike earlier, but must re-check assumptions after dependencies merge.

## Beginner learning objectives
- Investigate the technologies and design choices needed for persistent session storage design before implementation.
- Break a production-oriented concern into evidence-backed, reviewable increments.
- Document trade-offs, tests, operational impact, and limitations for future maintainers.

## Deliverables
- Persistence ADR
- Storage service and schema
- Retention/deletion tests
- Investigation notes/ADR
- Updated operational or user documentation

## Acceptance criteria
- Existing session behavior remains available.
- Stored records contain no raw images.
- Corrupt/missing storage fails safely.
- Deletion and retention are demonstrable.
- The selected approach is justified against at least one alternative.
- Automated or repeatable manual verification is documented.
- Remaining limitations and follow-up tasks are recorded.

## Definition of Done
- All acceptance criteria are demonstrated with evidence in the issue or pull request.
- Relevant documentation is updated so another beginner can repeat the work.
- No credentials, personal images, student emails, or raw volunteer recordings are committed.
- The task owner records decisions, assumptions, unresolved limitations, and follow-up work.
- A focused pull request uses the task ID in its title and links the issue with `Closes #...`.
- A reviewer other than the author examines the change, requested changes are resolved, and CI passes before merge.

## Dependencies and coordination
- Blocking dependencies: MP-018, MP-023
- Related coordination tasks: None
- Initial blocking status: blocked
- Do not mark this issue In Progress until required dependency outputs are available, except for a time-boxed learning spike that is explicitly recorded here.

## Ownership and review
- Team: MovePal Development
- Workstream: Backend
- Suggested Scrum role: developer
- Primary assignee: Unassigned until later sprint planning
- Contributors: None planned
- Suggested independent reviewer: Assign during later sprint planning; reviewer must differ from author
- Planned effort allocation: Not assigned in the current sprint
- Pull request: Required
- Suggested branch: `mp-037-persistent-session-storage-design`

## Beginner estimate and buffers
- Focused-work estimate: 16 hours
- Investigation/learning buffer included: 3.2 hours
- Review/collaboration buffer included: 2.4 hours
- QA/rework buffer included: 2.4 hours
- This is a rough beginner estimate. Update the issue when new evidence changes the estimate; do not hide learning time.

## Planning metadata
- Priority: P2
- Sprint designation: post-sprint
- Milestone: Post-Sprint Stabilization
- Initial Project stage: Backlog
- Planned start: Not scheduled
- Planned target: Not scheduled
- Manual testing only: No

## Suggested verification
- Repository/service unit tests
- Migration and corruption tests

## Risks
- Persistence quietly expands into identity tracking.
- Concurrent writes corrupt data.

## Security and privacy
- Collect only fields justified by a documented use case.
- Provide deletion and retention controls.

## Helpful documentation topics
- Relevant official library/framework documentation
- Existing MovePal ADRs, tests, and limitations

## Demo/evidence required
- Create, restart, retrieve, and delete an anonymous session summary.


---

<!-- task-id: MP-038 -->
# MP-038 — SQLite migration and data-access layer

## Value
If persistent structured data is approved, introduce SQLite through a small data-access layer with schema migration and tests rather than allowing SQL in routes. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## Detailed description and work sequence
If persistent structured data is approved, introduce SQLite through a small data-access layer with schema migration and tests rather than allowing SQL in routes.

Work sequence:

1. Confirm MP-037 selected SQLite and define schema versioning.

2. Choose a minimal migration approach.

3. Implement repository methods, transactions, and failure mapping.

4. Test upgrades from an earlier schema.

5. Time-box an investigation spike and record alternatives, compatibility, cost, and risks.

6. Split implementation into pull requests small enough for one beginner working day where necessary.

7. Arrange an independent design/code review and update documentation before considering the task complete.

Dependency handling:

This task depends on MP-037. Do not begin dependency-sensitive implementation until the listed outputs are available. The owner may perform reading or a disposable spike earlier, but must re-check assumptions after dependencies merge.

## Beginner learning objectives
- Investigate the technologies and design choices needed for sqlite migration and data-access layer before implementation.
- Break a production-oriented concern into evidence-backed, reviewable increments.
- Document trade-offs, tests, operational impact, and limitations for future maintainers.

## Deliverables
- SQLite schema/migrations
- Data-access module
- Migration and transaction tests
- Investigation notes/ADR
- Updated operational or user documentation

## Acceptance criteria
- No SQL appears in page/API routes.
- Fresh and upgraded databases behave consistently.
- Rollback/error paths are tested.
- The selected approach is justified against at least one alternative.
- Automated or repeatable manual verification is documented.
- Remaining limitations and follow-up tasks are recorded.

## Definition of Done
- All acceptance criteria are demonstrated with evidence in the issue or pull request.
- Relevant documentation is updated so another beginner can repeat the work.
- No credentials, personal images, student emails, or raw volunteer recordings are committed.
- The task owner records decisions, assumptions, unresolved limitations, and follow-up work.
- A focused pull request uses the task ID in its title and links the issue with `Closes #...`.
- A reviewer other than the author examines the change, requested changes are resolved, and CI passes before merge.

## Dependencies and coordination
- Blocking dependencies: MP-037
- Related coordination tasks: None
- Initial blocking status: blocked
- Do not mark this issue In Progress until required dependency outputs are available, except for a time-boxed learning spike that is explicitly recorded here.

## Ownership and review
- Team: MovePal Development
- Workstream: Backend
- Suggested Scrum role: developer
- Primary assignee: Unassigned until later sprint planning
- Contributors: None planned
- Suggested independent reviewer: Assign during later sprint planning; reviewer must differ from author
- Planned effort allocation: Not assigned in the current sprint
- Pull request: Required
- Suggested branch: `mp-038-sqlite-migration-and-data-access`

## Beginner estimate and buffers
- Focused-work estimate: 18 hours
- Investigation/learning buffer included: 3.6 hours
- Review/collaboration buffer included: 2.7 hours
- QA/rework buffer included: 2.7 hours
- This is a rough beginner estimate. Update the issue when new evidence changes the estimate; do not hide learning time.

## Planning metadata
- Priority: P3
- Sprint designation: post-sprint
- Milestone: Post-Sprint Stabilization
- Initial Project stage: Backlog
- Planned start: Not scheduled
- Planned target: Not scheduled
- Manual testing only: No

## Suggested verification
- Repository integration tests
- Migration forward/rollback test

## Risks
- Database work adds complexity without a real need.
- Migration damages existing records.

## Security and privacy
- Avoid personal identifiers and raw media in tables.

## Helpful documentation topics
- Relevant official library/framework documentation
- Existing MovePal ADRs, tests, and limitations

## Demo/evidence required
- Upgrade a sample database and show preserved anonymous summaries.


---

<!-- task-id: MP-039 -->
# MP-039 — Localization architecture and message catalog

## Value
Move user-facing text out of templates/services into a maintainable localization approach so English remains complete and additional languages can be added consistently. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## Detailed description and work sequence
Move user-facing text out of templates/services into a maintainable localization approach so English remains complete and additional languages can be added consistently.

Work sequence:

1. Inventory all user-facing strings including errors and feedback.

2. Compare Flask-Babel with a minimal catalog suitable for the project.

3. Define locale selection/fallback and plural/formatting rules.

4. Add missing-string validation.

5. Time-box an investigation spike and record alternatives, compatibility, cost, and risks.

6. Split implementation into pull requests small enough for one beginner working day where necessary.

7. Arrange an independent design/code review and update documentation before considering the task complete.

Dependency handling:

This task depends on MP-024. Do not begin dependency-sensitive implementation until the listed outputs are available. The owner may perform reading or a disposable spike earlier, but must re-check assumptions after dependencies merge.

## Beginner learning objectives
- Investigate the technologies and design choices needed for localization architecture and message catalog before implementation.
- Break a production-oriented concern into evidence-backed, reviewable increments.
- Document trade-offs, tests, operational impact, and limitations for future maintainers.

## Deliverables
- Localization ADR
- English message catalog
- Locale selection/fallback implementation
- Investigation notes/ADR
- Updated operational or user documentation

## Acceptance criteria
- All core UI/feedback strings come from the catalog.
- Missing translations fall back safely.
- Tests verify representative messages.
- The selected approach is justified against at least one alternative.
- Automated or repeatable manual verification is documented.
- Remaining limitations and follow-up tasks are recorded.

## Definition of Done
- All acceptance criteria are demonstrated with evidence in the issue or pull request.
- Relevant documentation is updated so another beginner can repeat the work.
- No credentials, personal images, student emails, or raw volunteer recordings are committed.
- The task owner records decisions, assumptions, unresolved limitations, and follow-up work.
- A focused pull request uses the task ID in its title and links the issue with `Closes #...`.
- A reviewer other than the author examines the change, requested changes are resolved, and CI passes before merge.

## Dependencies and coordination
- Blocking dependencies: MP-024
- Related coordination tasks: None
- Initial blocking status: blocked
- Do not mark this issue In Progress until required dependency outputs are available, except for a time-boxed learning spike that is explicitly recorded here.

## Ownership and review
- Team: MovePal Development
- Workstream: Frontend/UX
- Suggested Scrum role: developer
- Primary assignee: Unassigned until later sprint planning
- Contributors: None planned
- Suggested independent reviewer: Assign during later sprint planning; reviewer must differ from author
- Planned effort allocation: Not assigned in the current sprint
- Pull request: Required
- Suggested branch: `mp-039-localization-architecture-and-message`

## Beginner estimate and buffers
- Focused-work estimate: 14 hours
- Investigation/learning buffer included: 2.8 hours
- Review/collaboration buffer included: 2.1 hours
- QA/rework buffer included: 2.1 hours
- This is a rough beginner estimate. Update the issue when new evidence changes the estimate; do not hide learning time.

## Planning metadata
- Priority: P2
- Sprint designation: future
- Milestone: Future Extensions
- Initial Project stage: Backlog
- Planned start: Not scheduled
- Planned target: Not scheduled
- Manual testing only: No

## Suggested verification
- Catalog completeness test
- Locale fallback test

## Risks
- Mixed hard-coded/catalog text creates inconsistency.
- Translation framework is excessive for the project.

## Security and privacy
- Translations must preserve privacy and non-medical meaning.

## Helpful documentation topics
- Relevant official library/framework documentation
- Existing MovePal ADRs, tests, and limitations

## Demo/evidence required
- Switch locale and complete a fallback activity.


---

<!-- task-id: MP-040 -->
# MP-040 — Arabic translation and right-to-left interface

## Value
Add a reviewed Arabic experience after localization architecture exists, including right-to-left layout, movement/side terminology, feedback, errors, privacy, and disclaimer content. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## Detailed description and work sequence
Add a reviewed Arabic experience after localization architecture exists, including right-to-left layout, movement/side terminology, feedback, errors, privacy, and disclaimer content.

Work sequence:

1. Prepare a glossary for movement and interface terms.

2. Translate the complete catalog with human review.

3. Implement RTL layout and bidirectional-safe components.

4. Test left/right wording carefully against anatomical side and mirrored preview.

5. Time-box an investigation spike and record alternatives, compatibility, cost, and risks.

6. Split implementation into pull requests small enough for one beginner working day where necessary.

7. Arrange an independent design/code review and update documentation before considering the task complete.

Dependency handling:

This task depends on MP-039. Do not begin dependency-sensitive implementation until the listed outputs are available. The owner may perform reading or a disposable spike earlier, but must re-check assumptions after dependencies merge.

## Beginner learning objectives
- Investigate the technologies and design choices needed for arabic translation and right-to-left interface before implementation.
- Break a production-oriented concern into evidence-backed, reviewable increments.
- Document trade-offs, tests, operational impact, and limitations for future maintainers.

## Deliverables
- Arabic catalog
- RTL styles/layout
- Translation review checklist
- Investigation notes/ADR
- Updated operational or user documentation

## Acceptance criteria
- All MVP screens have Arabic text.
- RTL layout remains usable at mobile width.
- Left/right movement instructions are unambiguous.
- Disclaimer meaning is preserved.
- The selected approach is justified against at least one alternative.
- Automated or repeatable manual verification is documented.
- Remaining limitations and follow-up tasks are recorded.

## Definition of Done
- All acceptance criteria are demonstrated with evidence in the issue or pull request.
- Relevant documentation is updated so another beginner can repeat the work.
- No credentials, personal images, student emails, or raw volunteer recordings are committed.
- The task owner records decisions, assumptions, unresolved limitations, and follow-up work.
- A focused pull request uses the task ID in its title and links the issue with `Closes #...`.
- A reviewer other than the author examines the change, requested changes are resolved, and CI passes before merge.

## Dependencies and coordination
- Blocking dependencies: MP-039
- Related coordination tasks: None
- Initial blocking status: blocked
- Do not mark this issue In Progress until required dependency outputs are available, except for a time-boxed learning spike that is explicitly recorded here.

## Ownership and review
- Team: MovePal Development
- Workstream: Frontend/UX
- Suggested Scrum role: developer
- Primary assignee: Unassigned until later sprint planning
- Contributors: None planned
- Suggested independent reviewer: Assign during later sprint planning; reviewer must differ from author
- Planned effort allocation: Not assigned in the current sprint
- Pull request: Required
- Suggested branch: `mp-040-arabic-translation-and-right-to-left`

## Beginner estimate and buffers
- Focused-work estimate: 18 hours
- Investigation/learning buffer included: 3.6 hours
- Review/collaboration buffer included: 2.7 hours
- QA/rework buffer included: 2.7 hours
- This is a rough beginner estimate. Update the issue when new evidence changes the estimate; do not hide learning time.

## Planning metadata
- Priority: P2
- Sprint designation: future
- Milestone: Future Extensions
- Initial Project stage: Backlog
- Planned start: Not scheduled
- Planned target: Not scheduled
- Manual testing only: No

## Suggested verification
- RTL screenshot/manual checks
- Catalog completeness
- Bilingual side-direction tests

## Risks
- Automatic translation changes medical/privacy meaning.
- RTL styling breaks camera/game components.

## Security and privacy
- Human review is required for consent/privacy/disclaimer wording.

## Helpful documentation topics
- Relevant official library/framework documentation
- Existing MovePal ADRs, tests, and limitations

## Demo/evidence required
- Complete one activity and summary in Arabic RTL.


---

<!-- task-id: MP-041 -->
# MP-041 — Accessibility audit and remediation plan

## Value
Go beyond Sprint 1 sanity checks with a structured accessibility audit covering keyboard, focus, semantics, status messages, contrast, reduced motion, zoom, responsive layout, and assistive-technology behavior. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## Detailed description and work sequence
Go beyond Sprint 1 sanity checks with a structured accessibility audit covering keyboard, focus, semantics, status messages, contrast, reduced motion, zoom, responsive layout, and assistive-technology behavior.

Work sequence:

1. Define target conformance level and audit scope.

2. Run automated checks as supporting evidence, not sole evidence.

3. Perform keyboard, zoom, screen-reader, and reduced-motion checks.

4. Prioritize findings and implement bounded remediations.

5. Time-box an investigation spike and record alternatives, compatibility, cost, and risks.

6. Split implementation into pull requests small enough for one beginner working day where necessary.

7. Arrange an independent design/code review and update documentation before considering the task complete.

Dependency handling:

This task depends on MP-024. Do not begin dependency-sensitive implementation until the listed outputs are available. The owner may perform reading or a disposable spike earlier, but must re-check assumptions after dependencies merge.

## Beginner learning objectives
- Investigate the technologies and design choices needed for accessibility audit and remediation plan before implementation.
- Break a production-oriented concern into evidence-backed, reviewable increments.
- Document trade-offs, tests, operational impact, and limitations for future maintainers.

## Deliverables
- Accessibility audit report
- Remediation backlog/PRs
- Accessibility statement
- Investigation notes/ADR
- Updated operational or user documentation

## Acceptance criteria
- Every finding has severity, evidence, owner, and disposition.
- Core flow works without a mouse.
- Status/feedback changes are perceivable.
- The selected approach is justified against at least one alternative.
- Automated or repeatable manual verification is documented.
- Remaining limitations and follow-up tasks are recorded.

## Definition of Done
- All acceptance criteria are demonstrated with evidence in the issue or pull request.
- Relevant documentation is updated so another beginner can repeat the work.
- No credentials, personal images, student emails, or raw volunteer recordings are committed.
- The task owner records decisions, assumptions, unresolved limitations, and follow-up work.
- A focused pull request uses the task ID in its title and links the issue with `Closes #...`.
- A reviewer other than the author examines the change, requested changes are resolved, and CI passes before merge.

## Dependencies and coordination
- Blocking dependencies: MP-024
- Related coordination tasks: None
- Initial blocking status: blocked
- Do not mark this issue In Progress until required dependency outputs are available, except for a time-boxed learning spike that is explicitly recorded here.

## Ownership and review
- Team: MovePal Development
- Workstream: Frontend/UX
- Suggested Scrum role: developer
- Primary assignee: Unassigned until later sprint planning
- Contributors: None planned
- Suggested independent reviewer: Assign during later sprint planning; reviewer must differ from author
- Planned effort allocation: Not assigned in the current sprint
- Pull request: Required
- Suggested branch: `mp-041-accessibility-audit-and-remediation`

## Beginner estimate and buffers
- Focused-work estimate: 20 hours
- Investigation/learning buffer included: 4 hours
- Review/collaboration buffer included: 3 hours
- QA/rework buffer included: 3 hours
- This is a rough beginner estimate. Update the issue when new evidence changes the estimate; do not hide learning time.

## Planning metadata
- Priority: P2
- Sprint designation: future
- Milestone: Production Readiness
- Initial Project stage: Backlog
- Planned start: Not scheduled
- Planned target: Not scheduled
- Manual testing only: No

## Suggested verification
- Keyboard/zoom/screen-reader scripts
- Automated accessibility scan as supplemental evidence

## Risks
- Automated tools create false confidence.
- Animation/game design conflicts with reduced-motion needs.

## Security and privacy
- Accessibility evidence must not include identifiable camera images.

## Helpful documentation topics
- Relevant official library/framework documentation
- Existing MovePal ADRs, tests, and limitations

## Demo/evidence required
- Demonstrate remediated keyboard and status-message flow.


---

<!-- task-id: MP-042 -->
# MP-042 — Progressive Web App and offline fallback investigation

## Value
Investigate whether a lightweight PWA improves classroom/demo reliability, especially for static UI and bundled fallback samples, while documenting camera/model/server limitations offline. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## Detailed description and work sequence
Investigate whether a lightweight PWA improves classroom/demo reliability, especially for static UI and bundled fallback samples, while documenting camera/model/server limitations offline.

Work sequence:

1. Define which assets and flows can operate offline.

2. Study service-worker caching and update risks.

3. Build a disposable manifest/service-worker spike.

4. Decide whether to implement, defer, or reject.

5. Time-box an investigation spike and record alternatives, compatibility, cost, and risks.

6. Split implementation into pull requests small enough for one beginner working day where necessary.

7. Arrange an independent design/code review and update documentation before considering the task complete.

Dependency handling:

This task depends on MP-024, MP-035. Do not begin dependency-sensitive implementation until the listed outputs are available. The owner may perform reading or a disposable spike earlier, but must re-check assumptions after dependencies merge.

## Beginner learning objectives
- Investigate the technologies and design choices needed for progressive web app and offline fallback investigation before implementation.
- Break a production-oriented concern into evidence-backed, reviewable increments.
- Document trade-offs, tests, operational impact, and limitations for future maintainers.

## Deliverables
- PWA feasibility ADR
- Optional manifest/service worker
- Offline/update test plan
- Investigation notes/ADR
- Updated operational or user documentation

## Acceptance criteria
- Offline behavior is explicit and does not pretend server pose inference works when unavailable.
- Cache updates do not trap users on stale code.
- Fallback assets respect licensing/privacy.
- The selected approach is justified against at least one alternative.
- Automated or repeatable manual verification is documented.
- Remaining limitations and follow-up tasks are recorded.

## Definition of Done
- All acceptance criteria are demonstrated with evidence in the issue or pull request.
- Relevant documentation is updated so another beginner can repeat the work.
- No credentials, personal images, student emails, or raw volunteer recordings are committed.
- The task owner records decisions, assumptions, unresolved limitations, and follow-up work.
- A focused pull request uses the task ID in its title and links the issue with `Closes #...`.
- A reviewer other than the author examines the change, requested changes are resolved, and CI passes before merge.

## Dependencies and coordination
- Blocking dependencies: MP-024, MP-035
- Related coordination tasks: None
- Initial blocking status: blocked
- Do not mark this issue In Progress until required dependency outputs are available, except for a time-boxed learning spike that is explicitly recorded here.

## Ownership and review
- Team: MovePal Development
- Workstream: Frontend/UX
- Suggested Scrum role: developer
- Primary assignee: Unassigned until later sprint planning
- Contributors: None planned
- Suggested independent reviewer: Assign during later sprint planning; reviewer must differ from author
- Planned effort allocation: Not assigned in the current sprint
- Pull request: Required
- Suggested branch: `mp-042-progressive-web-app-and`

## Beginner estimate and buffers
- Focused-work estimate: 16 hours
- Investigation/learning buffer included: 3.2 hours
- Review/collaboration buffer included: 2.4 hours
- QA/rework buffer included: 2.4 hours
- This is a rough beginner estimate. Update the issue when new evidence changes the estimate; do not hide learning time.

## Planning metadata
- Priority: P3
- Sprint designation: optional
- Milestone: Future Extensions
- Initial Project stage: Backlog
- Planned start: Not scheduled
- Planned target: Not scheduled
- Manual testing only: No

## Suggested verification
- Offline/online transition tests
- Cache version/update test

## Risks
- Stale caches complicate classroom support.
- PWA scope distracts from core product.

## Security and privacy
- Never cache submitted camera frames or private data.

## Helpful documentation topics
- Relevant official library/framework documentation
- Existing MovePal ADRs, tests, and limitations

## Demo/evidence required
- Demonstrate documented offline capabilities and limitations.


---

<!-- task-id: MP-043 -->
# MP-043 — Declarative custom-movement specification

## Value
Design a safe configuration format for adding simple landmark-based movements without editing core Python code, while validating allowed joints, thresholds, sides, feedback keys, and test fixtures. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## Detailed description and work sequence
Design a safe configuration format for adding simple landmark-based movements without editing core Python code, while validating allowed joints, thresholds, sides, feedback keys, and test fixtures.

Work sequence:

1. Extract common rule concepts from the three MVP movements.

2. Design a constrained JSON/YAML schema rather than executable expressions.

3. Implement validation and a small interpreter.

4. Migrate one existing movement as a compatibility test.

5. Time-box an investigation spike and record alternatives, compatibility, cost, and risks.

6. Split implementation into pull requests small enough for one beginner working day where necessary.

7. Arrange an independent design/code review and update documentation before considering the task complete.

Dependency handling:

This task depends on MP-014, MP-015, MP-016. Do not begin dependency-sensitive implementation until the listed outputs are available. The owner may perform reading or a disposable spike earlier, but must re-check assumptions after dependencies merge.

## Beginner learning objectives
- Investigate the technologies and design choices needed for declarative custom-movement specification before implementation.
- Break a production-oriented concern into evidence-backed, reviewable increments.
- Document trade-offs, tests, operational impact, and limitations for future maintainers.

## Deliverables
- Movement schema
- Validator/interpreter
- Authoring guide and examples
- Investigation notes/ADR
- Updated operational or user documentation

## Acceptance criteria
- Invalid or unsafe rules fail with clear errors.
- One existing movement behaves equivalently through configuration.
- Schema supports test fixtures and versioning.
- The selected approach is justified against at least one alternative.
- Automated or repeatable manual verification is documented.
- Remaining limitations and follow-up tasks are recorded.

## Definition of Done
- All acceptance criteria are demonstrated with evidence in the issue or pull request.
- Relevant documentation is updated so another beginner can repeat the work.
- No credentials, personal images, student emails, or raw volunteer recordings are committed.
- The task owner records decisions, assumptions, unresolved limitations, and follow-up work.
- A focused pull request uses the task ID in its title and links the issue with `Closes #...`.
- A reviewer other than the author examines the change, requested changes are resolved, and CI passes before merge.

## Dependencies and coordination
- Blocking dependencies: MP-014, MP-015, MP-016
- Related coordination tasks: None
- Initial blocking status: blocked
- Do not mark this issue In Progress until required dependency outputs are available, except for a time-boxed learning spike that is explicitly recorded here.

## Ownership and review
- Team: MovePal Development
- Workstream: Computer Vision
- Suggested Scrum role: developer
- Primary assignee: Unassigned until later sprint planning
- Contributors: None planned
- Suggested independent reviewer: Assign during later sprint planning; reviewer must differ from author
- Planned effort allocation: Not assigned in the current sprint
- Pull request: Required
- Suggested branch: `mp-043-declarative-custom-movement-specification`

## Beginner estimate and buffers
- Focused-work estimate: 24 hours
- Investigation/learning buffer included: 4.8 hours
- Review/collaboration buffer included: 3.6 hours
- QA/rework buffer included: 3.6 hours
- This is a rough beginner estimate. Update the issue when new evidence changes the estimate; do not hide learning time.

## Planning metadata
- Priority: P2
- Sprint designation: future
- Milestone: Future Extensions
- Initial Project stage: Backlog
- Planned start: Not scheduled
- Planned target: Not scheduled
- Manual testing only: No

## Suggested verification
- Schema validation
- Equivalence tests
- Malformed rule tests

## Risks
- Configuration becomes a hidden programming language.
- Unvalidated thresholds create unsafe or misleading feedback.

## Security and privacy
- Do not allow arbitrary code execution or medical labels.

## Helpful documentation topics
- Relevant official library/framework documentation
- Existing MovePal ADRs, tests, and limitations

## Demo/evidence required
- Add a simple new movement through validated configuration.


---

<!-- task-id: MP-044 -->
# MP-044 — Educator-configured activity session

## Value
Allow an authorized local educator/facilitator to choose movement order, repetitions, difficulty preset, and session length without introducing user accounts or medical treatment plans. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## Detailed description and work sequence
Allow an authorized local educator/facilitator to choose movement order, repetitions, difficulty preset, and session length without introducing user accounts or medical treatment plans.

Work sequence:

1. Interview the instructor/facilitator role using hypothetical requirements only.

2. Define safe configurable fields and validation.

3. Design a simple setup screen and session configuration object.

4. Integrate with summary and reset behavior.

5. Time-box an investigation spike and record alternatives, compatibility, cost, and risks.

6. Split implementation into pull requests small enough for one beginner working day where necessary.

7. Arrange an independent design/code review and update documentation before considering the task complete.

Dependency handling:

This task depends on MP-018, MP-043. Do not begin dependency-sensitive implementation until the listed outputs are available. The owner may perform reading or a disposable spike earlier, but must re-check assumptions after dependencies merge.

## Beginner learning objectives
- Investigate the technologies and design choices needed for educator-configured activity session before implementation.
- Break a production-oriented concern into evidence-backed, reviewable increments.
- Document trade-offs, tests, operational impact, and limitations for future maintainers.

## Deliverables
- Session configuration model/UI
- Validation rules
- Facilitator guide
- Investigation notes/ADR
- Updated operational or user documentation

## Acceptance criteria
- Invalid configurations are rejected.
- Configured order/repetitions drive the game.
- Default session remains simple.
- Wording avoids therapy prescription.
- The selected approach is justified against at least one alternative.
- Automated or repeatable manual verification is documented.
- Remaining limitations and follow-up tasks are recorded.

## Definition of Done
- All acceptance criteria are demonstrated with evidence in the issue or pull request.
- Relevant documentation is updated so another beginner can repeat the work.
- No credentials, personal images, student emails, or raw volunteer recordings are committed.
- The task owner records decisions, assumptions, unresolved limitations, and follow-up work.
- A focused pull request uses the task ID in its title and links the issue with `Closes #...`.
- A reviewer other than the author examines the change, requested changes are resolved, and CI passes before merge.

## Dependencies and coordination
- Blocking dependencies: MP-018, MP-043
- Related coordination tasks: None
- Initial blocking status: blocked
- Do not mark this issue In Progress until required dependency outputs are available, except for a time-boxed learning spike that is explicitly recorded here.

## Ownership and review
- Team: MovePal Development
- Workstream: Product/Documentation
- Suggested Scrum role: developer
- Primary assignee: Unassigned until later sprint planning
- Contributors: None planned
- Suggested independent reviewer: Assign during later sprint planning; reviewer must differ from author
- Planned effort allocation: Not assigned in the current sprint
- Pull request: Required
- Suggested branch: `mp-044-educator-configured-activity-session`

## Beginner estimate and buffers
- Focused-work estimate: 22 hours
- Investigation/learning buffer included: 4.4 hours
- Review/collaboration buffer included: 3.3 hours
- QA/rework buffer included: 3.3 hours
- This is a rough beginner estimate. Update the issue when new evidence changes the estimate; do not hide learning time.

## Planning metadata
- Priority: P2
- Sprint designation: future
- Milestone: Future Extensions
- Initial Project stage: Backlog
- Planned start: Not scheduled
- Planned target: Not scheduled
- Manual testing only: No

## Suggested verification
- Configuration unit/integration tests
- Default/backward-compatibility flow

## Risks
- Configuration becomes complex for children.
- Settings imply clinical dosage.

## Security and privacy
- Do not store facilitator or child identity.
- Describe settings as game/session preferences.

## Helpful documentation topics
- Relevant official library/framework documentation
- Existing MovePal ADRs, tests, and limitations

## Demo/evidence required
- Configure and run a custom three-activity sequence.


---

<!-- task-id: MP-045 -->
# MP-045 — Difficulty presets and adaptive thresholds investigation

## Value
Investigate transparent difficulty presets or bounded adaptive thresholds without claiming personalization, diagnosis, or validated rehabilitation. Preserve explainability and user control. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## Detailed description and work sequence
Investigate transparent difficulty presets or bounded adaptive thresholds without claiming personalization, diagnosis, or validated rehabilitation. Preserve explainability and user control.

Work sequence:

1. Define beginner-friendly difficulty use cases.

2. Compare fixed presets with simple session calibration.

3. Specify bounds, reset, and explanation behavior.

4. Evaluate with synthetic/adult-only fixtures for unintended false feedback.

5. Time-box an investigation spike and record alternatives, compatibility, cost, and risks.

6. Split implementation into pull requests small enough for one beginner working day where necessary.

7. Arrange an independent design/code review and update documentation before considering the task complete.

Dependency handling:

This task depends on MP-021, MP-044. Do not begin dependency-sensitive implementation until the listed outputs are available. The owner may perform reading or a disposable spike earlier, but must re-check assumptions after dependencies merge.

## Beginner learning objectives
- Investigate the technologies and design choices needed for difficulty presets and adaptive thresholds investigation before implementation.
- Break a production-oriented concern into evidence-backed, reviewable increments.
- Document trade-offs, tests, operational impact, and limitations for future maintainers.

## Deliverables
- Difficulty/adaptation ADR
- Preset/configuration prototype
- Evaluation report
- Investigation notes/ADR
- Updated operational or user documentation

## Acceptance criteria
- Behavior remains deterministic and bounded.
- Users can see/reset the selected preset.
- No health inference is made.
- Regression tests cover default thresholds.
- The selected approach is justified against at least one alternative.
- Automated or repeatable manual verification is documented.
- Remaining limitations and follow-up tasks are recorded.

## Definition of Done
- All acceptance criteria are demonstrated with evidence in the issue or pull request.
- Relevant documentation is updated so another beginner can repeat the work.
- No credentials, personal images, student emails, or raw volunteer recordings are committed.
- The task owner records decisions, assumptions, unresolved limitations, and follow-up work.
- A focused pull request uses the task ID in its title and links the issue with `Closes #...`.
- A reviewer other than the author examines the change, requested changes are resolved, and CI passes before merge.

## Dependencies and coordination
- Blocking dependencies: MP-021, MP-044
- Related coordination tasks: None
- Initial blocking status: blocked
- Do not mark this issue In Progress until required dependency outputs are available, except for a time-boxed learning spike that is explicitly recorded here.

## Ownership and review
- Team: MovePal Development
- Workstream: Data/Evaluation
- Suggested Scrum role: developer
- Primary assignee: Unassigned until later sprint planning
- Contributors: None planned
- Suggested independent reviewer: Assign during later sprint planning; reviewer must differ from author
- Planned effort allocation: Not assigned in the current sprint
- Pull request: Required
- Suggested branch: `mp-045-difficulty-presets-and-adaptive`

## Beginner estimate and buffers
- Focused-work estimate: 24 hours
- Investigation/learning buffer included: 4.8 hours
- Review/collaboration buffer included: 3.6 hours
- QA/rework buffer included: 3.6 hours
- This is a rough beginner estimate. Update the issue when new evidence changes the estimate; do not hide learning time.

## Planning metadata
- Priority: P3
- Sprint designation: future
- Milestone: Future Extensions
- Initial Project stage: Backlog
- Planned start: Not scheduled
- Planned target: Not scheduled
- Manual testing only: No

## Suggested verification
- Preset regression tests
- Bounds/reset tests
- Fixture evaluation

## Risks
- Adaptive behavior is mistaken for clinical personalization.
- Small calibration data overfits one body/camera.

## Security and privacy
- Use adults/derived landmarks only; document bias.

## Helpful documentation topics
- Relevant official library/framework documentation
- Existing MovePal ADRs, tests, and limitations

## Demo/evidence required
- Compare default and one preset on the same fixtures.


---

<!-- task-id: MP-046 -->
# MP-046 — Expanded reward mechanics and session progression

## Value
Explore additional non-manipulative game mechanics such as badges, streaks, levels, and encouraging progress while keeping the experience short, optional, and understandable. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## Detailed description and work sequence
Explore additional non-manipulative game mechanics such as badges, streaks, levels, and encouraging progress while keeping the experience short, optional, and understandable.

Work sequence:

1. Define learning/play goals and anti-goals such as pressure or endless engagement.

2. Prototype reward rules separately from movement correctness.

3. Test reset, repeated sessions, and accessibility.

4. Review wording and visuals with product/privacy limitations.

5. Time-box an investigation spike and record alternatives, compatibility, cost, and risks.

6. Split implementation into pull requests small enough for one beginner working day where necessary.

7. Arrange an independent design/code review and update documentation before considering the task complete.

Dependency handling:

This task depends on MP-017, MP-018. Do not begin dependency-sensitive implementation until the listed outputs are available. The owner may perform reading or a disposable spike earlier, but must re-check assumptions after dependencies merge.

## Beginner learning objectives
- Investigate the technologies and design choices needed for expanded reward mechanics and session progression before implementation.
- Break a production-oriented concern into evidence-backed, reviewable increments.
- Document trade-offs, tests, operational impact, and limitations for future maintainers.

## Deliverables
- Reward design specification
- Game-state implementation
- Reward regression tests
- Investigation notes/ADR
- Updated operational or user documentation

## Acceptance criteria
- Rewards cannot be farmed by duplicate frames.
- A user can skip or reset progression.
- Core feedback remains usable without rewards.
- The selected approach is justified against at least one alternative.
- Automated or repeatable manual verification is documented.
- Remaining limitations and follow-up tasks are recorded.

## Definition of Done
- All acceptance criteria are demonstrated with evidence in the issue or pull request.
- Relevant documentation is updated so another beginner can repeat the work.
- No credentials, personal images, student emails, or raw volunteer recordings are committed.
- The task owner records decisions, assumptions, unresolved limitations, and follow-up work.
- A focused pull request uses the task ID in its title and links the issue with `Closes #...`.
- A reviewer other than the author examines the change, requested changes are resolved, and CI passes before merge.

## Dependencies and coordination
- Blocking dependencies: MP-017, MP-018
- Related coordination tasks: None
- Initial blocking status: blocked
- Do not mark this issue In Progress until required dependency outputs are available, except for a time-boxed learning spike that is explicitly recorded here.

## Ownership and review
- Team: MovePal Development
- Workstream: Frontend/UX
- Suggested Scrum role: developer
- Primary assignee: Unassigned until later sprint planning
- Contributors: None planned
- Suggested independent reviewer: Assign during later sprint planning; reviewer must differ from author
- Planned effort allocation: Not assigned in the current sprint
- Pull request: Required
- Suggested branch: `mp-046-expanded-reward-mechanics-and`

## Beginner estimate and buffers
- Focused-work estimate: 18 hours
- Investigation/learning buffer included: 3.6 hours
- Review/collaboration buffer included: 2.7 hours
- QA/rework buffer included: 2.7 hours
- This is a rough beginner estimate. Update the issue when new evidence changes the estimate; do not hide learning time.

## Planning metadata
- Priority: P3
- Sprint designation: future
- Milestone: Future Extensions
- Initial Project stage: Backlog
- Planned start: Not scheduled
- Planned target: Not scheduled
- Manual testing only: No

## Suggested verification
- State-transition and reset tests
- Accessibility/manual review

## Risks
- Rewards encourage excessive use or shame failure.
- State complexity creates bugs.

## Security and privacy
- Do not rank children or store identifiable performance history.

## Helpful documentation topics
- Relevant official library/framework documentation
- Existing MovePal ADRs, tests, and limitations

## Demo/evidence required
- Complete a session and show understandable reward progression.


---

<!-- task-id: MP-047 -->
# MP-047 — Avatar animation and asset pipeline

## Value
Replace the static toy/avatar with lightweight movement demonstrations using original or properly licensed assets, an explicit asset pipeline, fallbacks, and accessibility controls. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## Detailed description and work sequence
Replace the static toy/avatar with lightweight movement demonstrations using original or properly licensed assets, an explicit asset pipeline, fallbacks, and accessibility controls.

Work sequence:

1. Compare CSS/SVG, sprite, GIF/video, and skeletal animation approaches.

2. Verify license, attribution, file size, and browser support.

3. Create one movement animation and static fallback.

4. Add reduced-motion behavior and alt/instruction text.

5. Time-box an investigation spike and record alternatives, compatibility, cost, and risks.

6. Split implementation into pull requests small enough for one beginner working day where necessary.

7. Arrange an independent design/code review and update documentation before considering the task complete.

Dependency handling:

This task depends on MP-011. Do not begin dependency-sensitive implementation until the listed outputs are available. The owner may perform reading or a disposable spike earlier, but must re-check assumptions after dependencies merge.

## Beginner learning objectives
- Investigate the technologies and design choices needed for avatar animation and asset pipeline before implementation.
- Break a production-oriented concern into evidence-backed, reviewable increments.
- Document trade-offs, tests, operational impact, and limitations for future maintainers.

## Deliverables
- Asset/licensing inventory
- Avatar animation component
- Reduced-motion/static fallback
- Investigation notes/ADR
- Updated operational or user documentation

## Acceptance criteria
- Assets have documented provenance.
- Animation does not block instructions or feedback.
- Reduced-motion users receive an equivalent static representation.
- The selected approach is justified against at least one alternative.
- Automated or repeatable manual verification is documented.
- Remaining limitations and follow-up tasks are recorded.

## Definition of Done
- All acceptance criteria are demonstrated with evidence in the issue or pull request.
- Relevant documentation is updated so another beginner can repeat the work.
- No credentials, personal images, student emails, or raw volunteer recordings are committed.
- The task owner records decisions, assumptions, unresolved limitations, and follow-up work.
- A focused pull request uses the task ID in its title and links the issue with `Closes #...`.
- A reviewer other than the author examines the change, requested changes are resolved, and CI passes before merge.

## Dependencies and coordination
- Blocking dependencies: MP-011
- Related coordination tasks: None
- Initial blocking status: blocked
- Do not mark this issue In Progress until required dependency outputs are available, except for a time-boxed learning spike that is explicitly recorded here.

## Ownership and review
- Team: MovePal Development
- Workstream: Frontend/UX
- Suggested Scrum role: developer
- Primary assignee: Unassigned until later sprint planning
- Contributors: None planned
- Suggested independent reviewer: Assign during later sprint planning; reviewer must differ from author
- Planned effort allocation: Not assigned in the current sprint
- Pull request: Required
- Suggested branch: `mp-047-avatar-animation-and-asset`

## Beginner estimate and buffers
- Focused-work estimate: 20 hours
- Investigation/learning buffer included: 4 hours
- Review/collaboration buffer included: 3 hours
- QA/rework buffer included: 3 hours
- This is a rough beginner estimate. Update the issue when new evidence changes the estimate; do not hide learning time.

## Planning metadata
- Priority: P3
- Sprint designation: future
- Milestone: Future Extensions
- Initial Project stage: Backlog
- Planned start: Not scheduled
- Planned target: Not scheduled
- Manual testing only: No

## Suggested verification
- Asset path/load tests
- Reduced-motion manual test
- Performance size check

## Risks
- Copyright/licensing problems.
- Large assets reduce performance.
- Animation triggers discomfort.

## Security and privacy
- Assets must not depict identifiable children.

## Helpful documentation topics
- Relevant official library/framework documentation
- Existing MovePal ADRs, tests, and limitations

## Demo/evidence required
- Show animated and reduced-motion fallback versions.


---

<!-- task-id: MP-048 -->
# MP-048 — Optional low-latency streaming feasibility study

## Value
Evaluate whether WebSockets, WebRTC, or another streaming design provides enough benefit over periodic frames to justify substantial complexity. This remains optional and cannot invalidate the simple Sprint 1 path. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## Detailed description and work sequence
Evaluate whether WebSockets, WebRTC, or another streaming design provides enough benefit over periodic frames to justify substantial complexity. This remains optional and cannot invalidate the simple Sprint 1 path.

Work sequence:

1. Define measurable latency/throughput goals and classroom network assumptions.

2. Compare periodic HTTP frames, WebSockets, and client-side inference.

3. Build a disposable prototype with synthetic/sample input.

4. Measure complexity, privacy, failure recovery, and hosting implications.

5. Make an explicit adopt/defer/reject decision.

6. Time-box an investigation spike and record alternatives, compatibility, cost, and risks.

7. Split implementation into pull requests small enough for one beginner working day where necessary.

8. Arrange an independent design/code review and update documentation before considering the task complete.

Dependency handling:

This task depends on MP-035. Do not begin dependency-sensitive implementation until the listed outputs are available. The owner may perform reading or a disposable spike earlier, but must re-check assumptions after dependencies merge.

## Beginner learning objectives
- Investigate the technologies and design choices needed for optional low-latency streaming feasibility study before implementation.
- Break a production-oriented concern into evidence-backed, reviewable increments.
- Document trade-offs, tests, operational impact, and limitations for future maintainers.

## Deliverables
- Streaming feasibility ADR
- Disposable benchmark prototype
- Measured comparison
- Investigation notes/ADR
- Updated operational or user documentation

## Acceptance criteria
- Recommendation is based on measurements.
- Fallback HTTP/sample path remains supported.
- Privacy and network failure behavior are explicit.
- The selected approach is justified against at least one alternative.
- Automated or repeatable manual verification is documented.
- Remaining limitations and follow-up tasks are recorded.

## Definition of Done
- All acceptance criteria are demonstrated with evidence in the issue or pull request.
- Relevant documentation is updated so another beginner can repeat the work.
- No credentials, personal images, student emails, or raw volunteer recordings are committed.
- The task owner records decisions, assumptions, unresolved limitations, and follow-up work.
- A focused pull request uses the task ID in its title and links the issue with `Closes #...`.
- A reviewer other than the author examines the change, requested changes are resolved, and CI passes before merge.

## Dependencies and coordination
- Blocking dependencies: MP-035
- Related coordination tasks: None
- Initial blocking status: blocked
- Do not mark this issue In Progress until required dependency outputs are available, except for a time-boxed learning spike that is explicitly recorded here.

## Ownership and review
- Team: MovePal Development
- Workstream: Backend
- Suggested Scrum role: developer
- Primary assignee: Unassigned until later sprint planning
- Contributors: None planned
- Suggested independent reviewer: Assign during later sprint planning; reviewer must differ from author
- Planned effort allocation: Not assigned in the current sprint
- Pull request: Required
- Suggested branch: `mp-048-optional-low-latency-streaming-feasibility`

## Beginner estimate and buffers
- Focused-work estimate: 28 hours
- Investigation/learning buffer included: 5.6 hours
- Review/collaboration buffer included: 4.2 hours
- QA/rework buffer included: 4.2 hours
- This is a rough beginner estimate. Update the issue when new evidence changes the estimate; do not hide learning time.

## Planning metadata
- Priority: P3
- Sprint designation: optional
- Milestone: Future Extensions
- Initial Project stage: Backlog
- Planned start: Not scheduled
- Planned target: Not scheduled
- Manual testing only: No

## Suggested verification
- Latency/load benchmark
- Disconnect/reconnect tests

## Risks
- High complexity overwhelms beginners.
- Streaming increases privacy/security surface.
- Prototype is mistaken for required architecture.

## Security and privacy
- Do not store streams; document transport/security requirements.

## Helpful documentation topics
- Relevant official library/framework documentation
- Existing MovePal ADRs, tests, and limitations

## Demo/evidence required
- Compare measured periodic and streaming prototypes.


---

<!-- task-id: MP-049 -->
# MP-049 — Pose model and library version-management policy

## Value
Establish a repeatable process for pinning, testing, upgrading, and documenting MediaPipe/OpenCV/Flask dependencies so model or API changes do not silently alter movement behavior. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## Detailed description and work sequence
Establish a repeatable process for pinning, testing, upgrading, and documenting MediaPipe/OpenCV/Flask dependencies so model or API changes do not silently alter movement behavior.

Work sequence:

1. Inventory direct/transitive versions and platform support.

2. Define an upgrade cadence and compatibility test matrix.

3. Record model/configuration identifiers and threshold versions.

4. Automate dependency update proposals only after CI and fixture evaluation exist.

5. Time-box an investigation spike and record alternatives, compatibility, cost, and risks.

6. Split implementation into pull requests small enough for one beginner working day where necessary.

7. Arrange an independent design/code review and update documentation before considering the task complete.

Dependency handling:

This task depends on MP-021, MP-022. Do not begin dependency-sensitive implementation until the listed outputs are available. The owner may perform reading or a disposable spike earlier, but must re-check assumptions after dependencies merge.

## Beginner learning objectives
- Investigate the technologies and design choices needed for pose model and library version-management policy before implementation.
- Break a production-oriented concern into evidence-backed, reviewable increments.
- Document trade-offs, tests, operational impact, and limitations for future maintainers.

## Deliverables
- Version-management policy
- Compatibility matrix
- Upgrade checklist and changelog format
- Investigation notes/ADR
- Updated operational or user documentation

## Acceptance criteria
- A fresh environment resolves deterministic supported versions.
- An upgrade runs rule fixtures and OS CI before merge.
- Behavior-changing upgrades are documented.
- The selected approach is justified against at least one alternative.
- Automated or repeatable manual verification is documented.
- Remaining limitations and follow-up tasks are recorded.

## Definition of Done
- All acceptance criteria are demonstrated with evidence in the issue or pull request.
- Relevant documentation is updated so another beginner can repeat the work.
- No credentials, personal images, student emails, or raw volunteer recordings are committed.
- The task owner records decisions, assumptions, unresolved limitations, and follow-up work.
- A focused pull request uses the task ID in its title and links the issue with `Closes #...`.
- A reviewer other than the author examines the change, requested changes are resolved, and CI passes before merge.

## Dependencies and coordination
- Blocking dependencies: MP-021, MP-022
- Related coordination tasks: None
- Initial blocking status: blocked
- Do not mark this issue In Progress until required dependency outputs are available, except for a time-boxed learning spike that is explicitly recorded here.

## Ownership and review
- Team: MovePal Development
- Workstream: Testing/DevOps
- Suggested Scrum role: developer
- Primary assignee: Unassigned until later sprint planning
- Contributors: None planned
- Suggested independent reviewer: Assign during later sprint planning; reviewer must differ from author
- Planned effort allocation: Not assigned in the current sprint
- Pull request: Required
- Suggested branch: `mp-049-pose-model-and-library`

## Beginner estimate and buffers
- Focused-work estimate: 14 hours
- Investigation/learning buffer included: 2.8 hours
- Review/collaboration buffer included: 2.1 hours
- QA/rework buffer included: 2.1 hours
- This is a rough beginner estimate. Update the issue when new evidence changes the estimate; do not hide learning time.

## Planning metadata
- Priority: P2
- Sprint designation: post-sprint
- Milestone: Production Readiness
- Initial Project stage: Backlog
- Planned start: Not scheduled
- Planned target: Not scheduled
- Manual testing only: No

## Suggested verification
- Dependency resolution check
- Fixture regression after upgrade
- Windows/Linux matrix

## Risks
- Pinning becomes stale and insecure.
- Automatic upgrades change CV behavior.

## Security and privacy
- Version logs contain no user data.

## Helpful documentation topics
- Relevant official library/framework documentation
- Existing MovePal ADRs, tests, and limitations

## Demo/evidence required
- Simulate one dependency update and show the review checklist.


---

<!-- task-id: MP-050 -->
# MP-050 — Structured logging and privacy-safe observability

## Value
Add minimal structured operational logs and health indicators that help diagnose failures without recording frames, landmarks, identities, or sensitive browser details. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## Detailed description and work sequence
Add minimal structured operational logs and health indicators that help diagnose failures without recording frames, landmarks, identities, or sensitive browser details.

Work sequence:

1. Define actionable events and forbidden fields.

2. Choose log levels, correlation IDs, and retention assumptions.

3. Implement redaction and structured formatting.

4. Add health/readiness checks and test failure logging.

5. Time-box an investigation spike and record alternatives, compatibility, cost, and risks.

6. Split implementation into pull requests small enough for one beginner working day where necessary.

7. Arrange an independent design/code review and update documentation before considering the task complete.

Dependency handling:

This task depends on MP-023, MP-036. Do not begin dependency-sensitive implementation until the listed outputs are available. The owner may perform reading or a disposable spike earlier, but must re-check assumptions after dependencies merge.

## Beginner learning objectives
- Investigate the technologies and design choices needed for structured logging and privacy-safe observability before implementation.
- Break a production-oriented concern into evidence-backed, reviewable increments.
- Document trade-offs, tests, operational impact, and limitations for future maintainers.

## Deliverables
- Observability specification
- Structured logging configuration
- Redaction tests
- Health endpoints
- Investigation notes/ADR
- Updated operational or user documentation

## Acceptance criteria
- Logs explain failures without payload data.
- Secrets and image/landmark content are redacted or never accepted.
- Health checks distinguish app readiness from external services.
- The selected approach is justified against at least one alternative.
- Automated or repeatable manual verification is documented.
- Remaining limitations and follow-up tasks are recorded.

## Definition of Done
- All acceptance criteria are demonstrated with evidence in the issue or pull request.
- Relevant documentation is updated so another beginner can repeat the work.
- No credentials, personal images, student emails, or raw volunteer recordings are committed.
- The task owner records decisions, assumptions, unresolved limitations, and follow-up work.
- A focused pull request uses the task ID in its title and links the issue with `Closes #...`.
- A reviewer other than the author examines the change, requested changes are resolved, and CI passes before merge.

## Dependencies and coordination
- Blocking dependencies: MP-023, MP-036
- Related coordination tasks: None
- Initial blocking status: blocked
- Do not mark this issue In Progress until required dependency outputs are available, except for a time-boxed learning spike that is explicitly recorded here.

## Ownership and review
- Team: MovePal Development
- Workstream: Testing/DevOps
- Suggested Scrum role: developer
- Primary assignee: Unassigned until later sprint planning
- Contributors: None planned
- Suggested independent reviewer: Assign during later sprint planning; reviewer must differ from author
- Planned effort allocation: Not assigned in the current sprint
- Pull request: Required
- Suggested branch: `mp-050-structured-logging-and-privacy-safe`

## Beginner estimate and buffers
- Focused-work estimate: 16 hours
- Investigation/learning buffer included: 3.2 hours
- Review/collaboration buffer included: 2.4 hours
- QA/rework buffer included: 2.4 hours
- This is a rough beginner estimate. Update the issue when new evidence changes the estimate; do not hide learning time.

## Planning metadata
- Priority: P2
- Sprint designation: post-sprint
- Milestone: Production Readiness
- Initial Project stage: Backlog
- Planned start: Not scheduled
- Planned target: Not scheduled
- Manual testing only: No

## Suggested verification
- Log-capture/redaction unit tests
- Health endpoint tests

## Risks
- Verbose logs create a privacy leak.
- Health endpoints expose internals.

## Security and privacy
- Maintain an explicit forbidden-log-field list and retention recommendation.

## Helpful documentation topics
- Relevant official library/framework documentation
- Existing MovePal ADRs, tests, and limitations

## Demo/evidence required
- Trigger a safe error and show useful redacted logs.


---

<!-- task-id: MP-051 -->
# MP-051 — Threat model and automated security checks

## Value
Create a lightweight threat model for browser camera input, file upload, Flask endpoints, dependencies, configuration, and future deployment, then add proportionate automated checks without claiming a full security audit. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## Detailed description and work sequence
Create a lightweight threat model for browser camera input, file upload, Flask endpoints, dependencies, configuration, and future deployment, then add proportionate automated checks without claiming a full security audit.

Work sequence:

1. Map assets, trust boundaries, entry points, and likely misuse cases.

2. Prioritize threats by likelihood/impact for the prototype.

3. Add dependency, secret, and static checks that fit the repository.

4. Document false positives, update responsibility, and incident steps.

5. Time-box an investigation spike and record alternatives, compatibility, cost, and risks.

6. Split implementation into pull requests small enough for one beginner working day where necessary.

7. Arrange an independent design/code review and update documentation before considering the task complete.

Dependency handling:

This task depends on MP-023, MP-049. Do not begin dependency-sensitive implementation until the listed outputs are available. The owner may perform reading or a disposable spike earlier, but must re-check assumptions after dependencies merge.

## Beginner learning objectives
- Investigate the technologies and design choices needed for threat model and automated security checks before implementation.
- Break a production-oriented concern into evidence-backed, reviewable increments.
- Document trade-offs, tests, operational impact, and limitations for future maintainers.

## Deliverables
- Threat model
- Security-check workflows/configuration
- Findings and remediation backlog
- Investigation notes/ADR
- Updated operational or user documentation

## Acceptance criteria
- High-priority threats have mitigations or explicit acceptance.
- Checks run with minimal permissions.
- Findings do not expose secrets in logs.
- The selected approach is justified against at least one alternative.
- Automated or repeatable manual verification is documented.
- Remaining limitations and follow-up tasks are recorded.

## Definition of Done
- All acceptance criteria are demonstrated with evidence in the issue or pull request.
- Relevant documentation is updated so another beginner can repeat the work.
- No credentials, personal images, student emails, or raw volunteer recordings are committed.
- The task owner records decisions, assumptions, unresolved limitations, and follow-up work.
- A focused pull request uses the task ID in its title and links the issue with `Closes #...`.
- A reviewer other than the author examines the change, requested changes are resolved, and CI passes before merge.

## Dependencies and coordination
- Blocking dependencies: MP-023, MP-049
- Related coordination tasks: None
- Initial blocking status: blocked
- Do not mark this issue In Progress until required dependency outputs are available, except for a time-boxed learning spike that is explicitly recorded here.

## Ownership and review
- Team: MovePal Development
- Workstream: Testing/DevOps
- Suggested Scrum role: developer
- Primary assignee: Unassigned until later sprint planning
- Contributors: None planned
- Suggested independent reviewer: Assign during later sprint planning; reviewer must differ from author
- Planned effort allocation: Not assigned in the current sprint
- Pull request: Required
- Suggested branch: `mp-051-threat-model-and-automated`

## Beginner estimate and buffers
- Focused-work estimate: 22 hours
- Investigation/learning buffer included: 4.4 hours
- Review/collaboration buffer included: 3.3 hours
- QA/rework buffer included: 3.3 hours
- This is a rough beginner estimate. Update the issue when new evidence changes the estimate; do not hide learning time.

## Planning metadata
- Priority: P2
- Sprint designation: future
- Milestone: Production Readiness
- Initial Project stage: Backlog
- Planned start: Not scheduled
- Planned target: Not scheduled
- Manual testing only: No

## Suggested verification
- Secret-scan test with safe dummy pattern
- Dependency/static scan on PR

## Risks
- Tool output creates false assurance.
- Automated checks leak findings or secrets.

## Security and privacy
- Never commit real credentials to test scanning.

## Helpful documentation topics
- Relevant official library/framework documentation
- Existing MovePal ADRs, tests, and limitations

## Demo/evidence required
- Walk through one threat from entry point to mitigation/test.


---

<!-- task-id: MP-052 -->
# MP-052 — Data retention, withdrawal, and deletion workflow

## Value
Turn privacy promises into an operational procedure for any future adult-volunteer raw recordings, derived landmarks, and persisted anonymous summaries, including retention periods, access, withdrawal, deletion, and verification. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## Detailed description and work sequence
Turn privacy promises into an operational procedure for any future adult-volunteer raw recordings, derived landmarks, and persisted anonymous summaries, including retention periods, access, withdrawal, deletion, and verification.

Work sequence:

1. Inventory each data category and owner.

2. Define lawful/ethical purpose, storage location, retention, and access.

3. Create withdrawal/deletion request and verification steps.

4. Test deletion on sample data and document backups/copies.

5. Time-box an investigation spike and record alternatives, compatibility, cost, and risks.

6. Split implementation into pull requests small enough for one beginner working day where necessary.

7. Arrange an independent design/code review and update documentation before considering the task complete.

Dependency handling:

This task depends on MP-020, MP-037. Do not begin dependency-sensitive implementation until the listed outputs are available. The owner may perform reading or a disposable spike earlier, but must re-check assumptions after dependencies merge.

## Beginner learning objectives
- Investigate the technologies and design choices needed for data retention, withdrawal, and deletion workflow before implementation.
- Break a production-oriented concern into evidence-backed, reviewable increments.
- Document trade-offs, tests, operational impact, and limitations for future maintainers.

## Deliverables
- Data inventory
- Retention schedule
- Withdrawal/deletion procedure
- Deletion verification checklist
- Investigation notes/ADR
- Updated operational or user documentation

## Acceptance criteria
- Every data category has an owner and retention rule.
- Withdrawal can locate and delete linked data using anonymous IDs.
- Repository/CI never requires private raw media.
- The selected approach is justified against at least one alternative.
- Automated or repeatable manual verification is documented.
- Remaining limitations and follow-up tasks are recorded.

## Definition of Done
- All acceptance criteria are demonstrated with evidence in the issue or pull request.
- Relevant documentation is updated so another beginner can repeat the work.
- No credentials, personal images, student emails, or raw volunteer recordings are committed.
- The task owner records decisions, assumptions, unresolved limitations, and follow-up work.
- A focused pull request uses the task ID in its title and links the issue with `Closes #...`.
- A reviewer other than the author examines the change, requested changes are resolved, and CI passes before merge.

## Dependencies and coordination
- Blocking dependencies: MP-020, MP-037
- Related coordination tasks: None
- Initial blocking status: blocked
- Do not mark this issue In Progress until required dependency outputs are available, except for a time-boxed learning spike that is explicitly recorded here.

## Ownership and review
- Team: MovePal Development
- Workstream: Product/Documentation
- Suggested Scrum role: developer
- Primary assignee: Unassigned until later sprint planning
- Contributors: None planned
- Suggested independent reviewer: Assign during later sprint planning; reviewer must differ from author
- Planned effort allocation: Not assigned in the current sprint
- Pull request: Required
- Suggested branch: `mp-052-data-retention,-withdrawal,-and`

## Beginner estimate and buffers
- Focused-work estimate: 14 hours
- Investigation/learning buffer included: 2.8 hours
- Review/collaboration buffer included: 2.1 hours
- QA/rework buffer included: 2.1 hours
- This is a rough beginner estimate. Update the issue when new evidence changes the estimate; do not hide learning time.

## Planning metadata
- Priority: P1
- Sprint designation: future
- Milestone: Production Readiness
- Initial Project stage: Backlog
- Planned start: Not scheduled
- Planned target: Not scheduled
- Manual testing only: No

## Suggested verification
- Sample deletion drill
- Repository scan for prohibited raw data

## Risks
- Data copies are overlooked.
- Anonymous IDs cannot support withdrawal.
- Policy exceeds actual technical capability.

## Security and privacy
- No child data; minimize adult volunteer data and access.

## Helpful documentation topics
- Relevant official library/framework documentation
- Existing MovePal ADRs, tests, and limitations

## Demo/evidence required
- Run a sample withdrawal/deletion drill and show evidence.


---

<!-- task-id: MP-053 -->
# MP-053 — Expanded adult-only dataset and bias analysis

## Value
Design a larger but still bounded adult-only landmark dataset covering body proportions, clothing, camera distance, lighting, left/right, correct/incorrect examples, and known limitations, with consent and privacy controls. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## Detailed description and work sequence
Design a larger but still bounded adult-only landmark dataset covering body proportions, clothing, camera distance, lighting, left/right, correct/incorrect examples, and known limitations, with consent and privacy controls.

Work sequence:

1. Define sampling goals and exclusions without demographic overclaiming.

2. Update consent, protocol, annotation guide, and quality checks.

3. Collect only approved adult data and derive landmarks.

4. Analyze coverage and rule failures across documented conditions.

5. Publish only data approved for release.

6. Time-box an investigation spike and record alternatives, compatibility, cost, and risks.

7. Split implementation into pull requests small enough for one beginner working day where necessary.

8. Arrange an independent design/code review and update documentation before considering the task complete.

Dependency handling:

This task depends on MP-020, MP-021, MP-052. Do not begin dependency-sensitive implementation until the listed outputs are available. The owner may perform reading or a disposable spike earlier, but must re-check assumptions after dependencies merge.

## Beginner learning objectives
- Investigate the technologies and design choices needed for expanded adult-only dataset and bias analysis before implementation.
- Break a production-oriented concern into evidence-backed, reviewable increments.
- Document trade-offs, tests, operational impact, and limitations for future maintainers.

## Deliverables
- Updated dataset card
- Collection/annotation protocol
- Coverage and bias report
- Approved derived dataset
- Investigation notes/ADR
- Updated operational or user documentation

## Acceptance criteria
- All records have consent/provenance status.
- Correct/incorrect and environmental conditions are represented.
- Bias/coverage limitations are explicit.
- Private raw and publishable derived data remain separated.
- The selected approach is justified against at least one alternative.
- Automated or repeatable manual verification is documented.
- Remaining limitations and follow-up tasks are recorded.

## Definition of Done
- All acceptance criteria are demonstrated with evidence in the issue or pull request.
- Relevant documentation is updated so another beginner can repeat the work.
- No credentials, personal images, student emails, or raw volunteer recordings are committed.
- The task owner records decisions, assumptions, unresolved limitations, and follow-up work.
- A focused pull request uses the task ID in its title and links the issue with `Closes #...`.
- A reviewer other than the author examines the change, requested changes are resolved, and CI passes before merge.

## Dependencies and coordination
- Blocking dependencies: MP-020, MP-021, MP-052
- Related coordination tasks: None
- Initial blocking status: blocked
- Do not mark this issue In Progress until required dependency outputs are available, except for a time-boxed learning spike that is explicitly recorded here.

## Ownership and review
- Team: MovePal Development
- Workstream: Data/Evaluation
- Suggested Scrum role: developer
- Primary assignee: Unassigned until later sprint planning
- Contributors: None planned
- Suggested independent reviewer: Assign during later sprint planning; reviewer must differ from author
- Planned effort allocation: Not assigned in the current sprint
- Pull request: Required
- Suggested branch: `mp-053-expanded-adult-only-dataset-and`

## Beginner estimate and buffers
- Focused-work estimate: 36 hours
- Investigation/learning buffer included: 7.2 hours
- Review/collaboration buffer included: 5.4 hours
- QA/rework buffer included: 5.4 hours
- This is a rough beginner estimate. Update the issue when new evidence changes the estimate; do not hide learning time.

## Planning metadata
- Priority: P2
- Sprint designation: future
- Milestone: Production Readiness
- Initial Project stage: Backlog
- Planned start: Not scheduled
- Planned target: Not scheduled
- Manual testing only: No

## Suggested verification
- Schema/annotation validation
- Duplicate/outlier checks
- Rule evaluation by condition

## Risks
- Convenience sample is presented as representative.
- Consent/provenance is incomplete.
- Derived data may still be identifiable in context.

## Security and privacy
- Adults only; consent, minimization, withdrawal, controlled access.

## Helpful documentation topics
- Relevant official library/framework documentation
- Existing MovePal ADRs, tests, and limitations

## Demo/evidence required
- Show coverage dashboard and documented limitations, not participant media.


---

<!-- task-id: MP-054 -->
# MP-054 — Evaluation metrics and reproducible benchmark suite

## Value
Define and implement a reproducible benchmark for rule outcomes, visibility handling, latency, and user-flow reliability using approved landmark/image fixtures, with metrics matched to the actual prototype claims. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## Detailed description and work sequence
Define and implement a reproducible benchmark for rule outcomes, visibility handling, latency, and user-flow reliability using approved landmark/image fixtures, with metrics matched to the actual prototype claims.

Work sequence:

1. Define task-level outcomes and appropriate precision/recall/confusion counts.

2. Separate movement rule quality, no-pose/framing handling, and system reliability.

3. Create fixed benchmark splits/configuration.

4. Generate machine-readable and human-readable reports.

5. Time-box an investigation spike and record alternatives, compatibility, cost, and risks.

6. Split implementation into pull requests small enough for one beginner working day where necessary.

7. Arrange an independent design/code review and update documentation before considering the task complete.

Dependency handling:

This task depends on MP-021, MP-053. Do not begin dependency-sensitive implementation until the listed outputs are available. The owner may perform reading or a disposable spike earlier, but must re-check assumptions after dependencies merge.

## Beginner learning objectives
- Investigate the technologies and design choices needed for evaluation metrics and reproducible benchmark suite before implementation.
- Break a production-oriented concern into evidence-backed, reviewable increments.
- Document trade-offs, tests, operational impact, and limitations for future maintainers.

## Deliverables
- Benchmark specification
- Evaluation script
- Versioned result report
- Regression thresholds
- Investigation notes/ADR
- Updated operational or user documentation

## Acceptance criteria
- Metrics map directly to documented claims.
- Results are reproducible from versioned derived fixtures.
- Error cases are inspectable.
- No clinical effectiveness metric is reported.
- The selected approach is justified against at least one alternative.
- Automated or repeatable manual verification is documented.
- Remaining limitations and follow-up tasks are recorded.

## Definition of Done
- All acceptance criteria are demonstrated with evidence in the issue or pull request.
- Relevant documentation is updated so another beginner can repeat the work.
- No credentials, personal images, student emails, or raw volunteer recordings are committed.
- The task owner records decisions, assumptions, unresolved limitations, and follow-up work.
- A focused pull request uses the task ID in its title and links the issue with `Closes #...`.
- A reviewer other than the author examines the change, requested changes are resolved, and CI passes before merge.

## Dependencies and coordination
- Blocking dependencies: MP-021, MP-053
- Related coordination tasks: None
- Initial blocking status: blocked
- Do not mark this issue In Progress until required dependency outputs are available, except for a time-boxed learning spike that is explicitly recorded here.

## Ownership and review
- Team: MovePal Development
- Workstream: Data/Evaluation
- Suggested Scrum role: developer
- Primary assignee: Unassigned until later sprint planning
- Contributors: None planned
- Suggested independent reviewer: Assign during later sprint planning; reviewer must differ from author
- Planned effort allocation: Not assigned in the current sprint
- Pull request: Required
- Suggested branch: `mp-054-evaluation-metrics-and-reproducible`

## Beginner estimate and buffers
- Focused-work estimate: 24 hours
- Investigation/learning buffer included: 4.8 hours
- Review/collaboration buffer included: 3.6 hours
- QA/rework buffer included: 3.6 hours
- This is a rough beginner estimate. Update the issue when new evidence changes the estimate; do not hide learning time.

## Planning metadata
- Priority: P2
- Sprint designation: future
- Milestone: Production Readiness
- Initial Project stage: Backlog
- Planned start: Not scheduled
- Planned target: Not scheduled
- Manual testing only: No

## Suggested verification
- Deterministic benchmark run
- Per-condition error report
- Versioned threshold regression

## Risks
- Aggregate metrics hide important conditions.
- Small data produces misleading certainty.

## Security and privacy
- Use approved derived data only and report sample limitations.

## Helpful documentation topics
- Relevant official library/framework documentation
- Existing MovePal ADRs, tests, and limitations

## Demo/evidence required
- Run the benchmark and inspect a false-positive/false-negative example.


---

<!-- task-id: MP-055 -->
# MP-055 — Multiple-person detection and guidance

## Value
Investigate how the selected pose solution behaves when multiple people are visible and implement explicit guidance or safe rejection rather than silently scoring the wrong person. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## Detailed description and work sequence
Investigate how the selected pose solution behaves when multiple people are visible and implement explicit guidance or safe rejection rather than silently scoring the wrong person.

Work sequence:

1. Test multiple-person scenes using licensed/synthetic/adult-only examples.

2. Compare single-pose confidence heuristics and multi-pose alternatives.

3. Define product behavior: proceed, warn, or ask for one person.

4. Implement and evaluate the chosen guidance.

5. Time-box an investigation spike and record alternatives, compatibility, cost, and risks.

6. Split implementation into pull requests small enough for one beginner working day where necessary.

7. Arrange an independent design/code review and update documentation before considering the task complete.

Dependency handling:

This task depends on MP-013, MP-054. Do not begin dependency-sensitive implementation until the listed outputs are available. The owner may perform reading or a disposable spike earlier, but must re-check assumptions after dependencies merge.

## Beginner learning objectives
- Investigate the technologies and design choices needed for multiple-person detection and guidance before implementation.
- Break a production-oriented concern into evidence-backed, reviewable increments.
- Document trade-offs, tests, operational impact, and limitations for future maintainers.

## Deliverables
- Multiple-person ADR
- Detection/guidance behavior
- Fixture tests and limitations
- Investigation notes/ADR
- Updated operational or user documentation

## Acceptance criteria
- The app does not silently imply it selected the intended person.
- Ambiguous scenes produce friendly guidance.
- Single-person behavior remains stable.
- The selected approach is justified against at least one alternative.
- Automated or repeatable manual verification is documented.
- Remaining limitations and follow-up tasks are recorded.

## Definition of Done
- All acceptance criteria are demonstrated with evidence in the issue or pull request.
- Relevant documentation is updated so another beginner can repeat the work.
- No credentials, personal images, student emails, or raw volunteer recordings are committed.
- The task owner records decisions, assumptions, unresolved limitations, and follow-up work.
- A focused pull request uses the task ID in its title and links the issue with `Closes #...`.
- A reviewer other than the author examines the change, requested changes are resolved, and CI passes before merge.

## Dependencies and coordination
- Blocking dependencies: MP-013, MP-054
- Related coordination tasks: None
- Initial blocking status: blocked
- Do not mark this issue In Progress until required dependency outputs are available, except for a time-boxed learning spike that is explicitly recorded here.

## Ownership and review
- Team: MovePal Development
- Workstream: Computer Vision
- Suggested Scrum role: developer
- Primary assignee: Unassigned until later sprint planning
- Contributors: None planned
- Suggested independent reviewer: Assign during later sprint planning; reviewer must differ from author
- Planned effort allocation: Not assigned in the current sprint
- Pull request: Required
- Suggested branch: `mp-055-multiple-person-detection-and-guidance`

## Beginner estimate and buffers
- Focused-work estimate: 20 hours
- Investigation/learning buffer included: 4 hours
- Review/collaboration buffer included: 3 hours
- QA/rework buffer included: 3 hours
- This is a rough beginner estimate. Update the issue when new evidence changes the estimate; do not hide learning time.

## Planning metadata
- Priority: P2
- Sprint designation: future
- Milestone: Future Extensions
- Initial Project stage: Backlog
- Planned start: Not scheduled
- Planned target: Not scheduled
- Manual testing only: No

## Suggested verification
- Single/multiple/ambiguous fixture tests

## Risks
- Estimator cannot reliably count people.
- Warning creates false certainty.

## Security and privacy
- Do not collect group images without explicit adult consent.

## Helpful documentation topics
- Relevant official library/framework documentation
- Existing MovePal ADRs, tests, and limitations

## Demo/evidence required
- Show single-person success and ambiguous-scene guidance.


---

<!-- task-id: MP-056 -->
# MP-056 — Low-light and framing robustness improvements

## Value
Improve feedback and preprocessing for common low-light, distance, crop, orientation, and framing problems using measurable heuristics while avoiding expensive enhancement pipelines. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## Detailed description and work sequence
Improve feedback and preprocessing for common low-light, distance, crop, orientation, and framing problems using measurable heuristics while avoiding expensive enhancement pipelines.

Work sequence:

1. Collect approved synthetic/adult-only condition fixtures.

2. Measure brightness, blur, crop, orientation, and visibility indicators.

3. Prototype lightweight preprocessing or guidance.

4. Evaluate trade-offs and false warnings.

5. Time-box an investigation spike and record alternatives, compatibility, cost, and risks.

6. Split implementation into pull requests small enough for one beginner working day where necessary.

7. Arrange an independent design/code review and update documentation before considering the task complete.

Dependency handling:

This task depends on MP-013, MP-054. Do not begin dependency-sensitive implementation until the listed outputs are available. The owner may perform reading or a disposable spike earlier, but must re-check assumptions after dependencies merge.

## Beginner learning objectives
- Investigate the technologies and design choices needed for low-light and framing robustness improvements before implementation.
- Break a production-oriented concern into evidence-backed, reviewable increments.
- Document trade-offs, tests, operational impact, and limitations for future maintainers.

## Deliverables
- Condition-detection helpers
- User guidance updates
- Robustness evaluation
- Investigation notes/ADR
- Updated operational or user documentation

## Acceptance criteria
- Common framing/lighting problems receive actionable guidance.
- Preprocessing does not materially slow normal requests.
- False warnings are documented.
- The selected approach is justified against at least one alternative.
- Automated or repeatable manual verification is documented.
- Remaining limitations and follow-up tasks are recorded.

## Definition of Done
- All acceptance criteria are demonstrated with evidence in the issue or pull request.
- Relevant documentation is updated so another beginner can repeat the work.
- No credentials, personal images, student emails, or raw volunteer recordings are committed.
- The task owner records decisions, assumptions, unresolved limitations, and follow-up work.
- A focused pull request uses the task ID in its title and links the issue with `Closes #...`.
- A reviewer other than the author examines the change, requested changes are resolved, and CI passes before merge.

## Dependencies and coordination
- Blocking dependencies: MP-013, MP-054
- Related coordination tasks: None
- Initial blocking status: blocked
- Do not mark this issue In Progress until required dependency outputs are available, except for a time-boxed learning spike that is explicitly recorded here.

## Ownership and review
- Team: MovePal Development
- Workstream: Computer Vision
- Suggested Scrum role: developer
- Primary assignee: Unassigned until later sprint planning
- Contributors: None planned
- Suggested independent reviewer: Assign during later sprint planning; reviewer must differ from author
- Planned effort allocation: Not assigned in the current sprint
- Pull request: Required
- Suggested branch: `mp-056-low-light-and-framing-robustness`

## Beginner estimate and buffers
- Focused-work estimate: 22 hours
- Investigation/learning buffer included: 4.4 hours
- Review/collaboration buffer included: 3.3 hours
- QA/rework buffer included: 3.3 hours
- This is a rough beginner estimate. Update the issue when new evidence changes the estimate; do not hide learning time.

## Planning metadata
- Priority: P2
- Sprint designation: future
- Milestone: Post-Sprint Stabilization
- Initial Project stage: Backlog
- Planned start: Not scheduled
- Planned target: Not scheduled
- Manual testing only: No

## Suggested verification
- Condition fixture matrix
- Latency regression
- Movement regression after preprocessing

## Risks
- Heuristics behave differently across cameras/skin tones/backgrounds.
- Image enhancement changes landmark behavior.

## Security and privacy
- Adults/derived fixtures only; document fairness and limitations.

## Helpful documentation topics
- Relevant official library/framework documentation
- Existing MovePal ADRs, tests, and limitations

## Demo/evidence required
- Compare normal and low-light/framing feedback on approved samples.


---

<!-- task-id: MP-057 -->
# MP-057 — API contract documentation and schema validation

## Value
Formalize the browser–Flask API using machine-readable schemas and examples, then validate requests/responses so frontend/backend changes fail early and remain understandable to students. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## Detailed description and work sequence
Formalize the browser–Flask API using machine-readable schemas and examples, then validate requests/responses so frontend/backend changes fail early and remain understandable to students.

Work sequence:

1. Inventory endpoints and error variants.

2. Choose a lightweight JSON Schema/OpenAPI approach.

3. Document examples and status codes.

4. Add contract validation/tests and versioning guidance.

5. Time-box an investigation spike and record alternatives, compatibility, cost, and risks.

6. Split implementation into pull requests small enough for one beginner working day where necessary.

7. Arrange an independent design/code review and update documentation before considering the task complete.

Dependency handling:

This task depends on MP-010, MP-019. Do not begin dependency-sensitive implementation until the listed outputs are available. The owner may perform reading or a disposable spike earlier, but must re-check assumptions after dependencies merge.

## Beginner learning objectives
- Investigate the technologies and design choices needed for api contract documentation and schema validation before implementation.
- Break a production-oriented concern into evidence-backed, reviewable increments.
- Document trade-offs, tests, operational impact, and limitations for future maintainers.

## Deliverables
- API schema/documentation
- Validation layer
- Contract regression tests
- Investigation notes/ADR
- Updated operational or user documentation

## Acceptance criteria
- Every endpoint and error response is documented.
- Frontend fixture examples validate.
- Breaking changes require explicit version/update notes.
- The selected approach is justified against at least one alternative.
- Automated or repeatable manual verification is documented.
- Remaining limitations and follow-up tasks are recorded.

## Definition of Done
- All acceptance criteria are demonstrated with evidence in the issue or pull request.
- Relevant documentation is updated so another beginner can repeat the work.
- No credentials, personal images, student emails, or raw volunteer recordings are committed.
- The task owner records decisions, assumptions, unresolved limitations, and follow-up work.
- A focused pull request uses the task ID in its title and links the issue with `Closes #...`.
- A reviewer other than the author examines the change, requested changes are resolved, and CI passes before merge.

## Dependencies and coordination
- Blocking dependencies: MP-010, MP-019
- Related coordination tasks: None
- Initial blocking status: blocked
- Do not mark this issue In Progress until required dependency outputs are available, except for a time-boxed learning spike that is explicitly recorded here.

## Ownership and review
- Team: MovePal Development
- Workstream: Backend
- Suggested Scrum role: developer
- Primary assignee: Unassigned until later sprint planning
- Contributors: None planned
- Suggested independent reviewer: Assign during later sprint planning; reviewer must differ from author
- Planned effort allocation: Not assigned in the current sprint
- Pull request: Required
- Suggested branch: `mp-057-api-contract-documentation-and`

## Beginner estimate and buffers
- Focused-work estimate: 16 hours
- Investigation/learning buffer included: 3.2 hours
- Review/collaboration buffer included: 2.4 hours
- QA/rework buffer included: 2.4 hours
- This is a rough beginner estimate. Update the issue when new evidence changes the estimate; do not hide learning time.

## Planning metadata
- Priority: P2
- Sprint designation: post-sprint
- Milestone: Post-Sprint Stabilization
- Initial Project stage: Backlog
- Planned start: Not scheduled
- Planned target: Not scheduled
- Manual testing only: No

## Suggested verification
- Request/response schema tests
- Example contract tests

## Risks
- Documentation drifts from implementation.
- Schema tool adds excessive complexity.

## Security and privacy
- Schemas exclude image bodies from logs/examples and contain no personal data.

## Helpful documentation topics
- Relevant official library/framework documentation
- Existing MovePal ADRs, tests, and limitations

## Demo/evidence required
- Validate a correct and incorrect response against the schema.


---

<!-- task-id: MP-058 -->
# MP-058 — Controlled cloud deployment investigation

## Value
Evaluate and document a small controlled deployment only after local production-like packaging, privacy, security, and performance work. Compare platforms, cost, HTTPS/camera behavior, resource limits, and data handling. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## Detailed description and work sequence
Evaluate and document a small controlled deployment only after local production-like packaging, privacy, security, and performance work. Compare platforms, cost, HTTPS/camera behavior, resource limits, and data handling.

Work sequence:

1. Define deployment purpose and non-goals.

2. Compare at least two beginner-compatible platforms and local hosting.

3. Estimate cost/resource/startup/model constraints.

4. Prototype one disposable deployment with no private data.

5. Document rollback, shutdown, and access limitations.

6. Time-box an investigation spike and record alternatives, compatibility, cost, and risks.

7. Split implementation into pull requests small enough for one beginner working day where necessary.

8. Arrange an independent design/code review and update documentation before considering the task complete.

Dependency handling:

This task depends on MP-036, MP-050, MP-051. Do not begin dependency-sensitive implementation until the listed outputs are available. The owner may perform reading or a disposable spike earlier, but must re-check assumptions after dependencies merge.

## Beginner learning objectives
- Investigate the technologies and design choices needed for controlled cloud deployment investigation before implementation.
- Break a production-oriented concern into evidence-backed, reviewable increments.
- Document trade-offs, tests, operational impact, and limitations for future maintainers.

## Deliverables
- Deployment ADR
- Infrastructure/configuration files if adopted
- Runbook and cost/privacy notes
- Investigation notes/ADR
- Updated operational or user documentation

## Acceptance criteria
- HTTPS supports camera permission where expected.
- Secrets are managed outside Git.
- Deployment can be removed/rolled back.
- No production-readiness claim is made solely from deployment.
- The selected approach is justified against at least one alternative.
- Automated or repeatable manual verification is documented.
- Remaining limitations and follow-up tasks are recorded.

## Definition of Done
- All acceptance criteria are demonstrated with evidence in the issue or pull request.
- Relevant documentation is updated so another beginner can repeat the work.
- No credentials, personal images, student emails, or raw volunteer recordings are committed.
- The task owner records decisions, assumptions, unresolved limitations, and follow-up work.
- A focused pull request uses the task ID in its title and links the issue with `Closes #...`.
- A reviewer other than the author examines the change, requested changes are resolved, and CI passes before merge.

## Dependencies and coordination
- Blocking dependencies: MP-036, MP-050, MP-051
- Related coordination tasks: None
- Initial blocking status: blocked
- Do not mark this issue In Progress until required dependency outputs are available, except for a time-boxed learning spike that is explicitly recorded here.

## Ownership and review
- Team: MovePal Development
- Workstream: Testing/DevOps
- Suggested Scrum role: developer
- Primary assignee: Unassigned until later sprint planning
- Contributors: None planned
- Suggested independent reviewer: Assign during later sprint planning; reviewer must differ from author
- Planned effort allocation: Not assigned in the current sprint
- Pull request: Required
- Suggested branch: `mp-058-controlled-cloud-deployment-investigation`

## Beginner estimate and buffers
- Focused-work estimate: 28 hours
- Investigation/learning buffer included: 5.6 hours
- Review/collaboration buffer included: 4.2 hours
- QA/rework buffer included: 4.2 hours
- This is a rough beginner estimate. Update the issue when new evidence changes the estimate; do not hide learning time.

## Planning metadata
- Priority: P3
- Sprint designation: future
- Milestone: Production Readiness
- Initial Project stage: Backlog
- Planned start: Not scheduled
- Planned target: Not scheduled
- Manual testing only: No

## Suggested verification
- Deployment smoke test
- Configuration/secret checks
- Rollback drill

## Risks
- Cloud cost or account requirements block students.
- Public exposure increases risk.
- Model resources exceed free tier.

## Security and privacy
- Deploy only non-sensitive fixtures; document data region/retention.

## Helpful documentation topics
- Relevant official library/framework documentation
- Existing MovePal ADRs, tests, and limitations

## Demo/evidence required
- Open the controlled deployment, run fallback flow, and perform rollback.


---

<!-- task-id: MP-059 -->
# MP-059 — Backup, restore, and recovery procedure

## Value
For any approved persistent configuration or anonymous session data, define backups, restore testing, version compatibility, corruption handling, and responsibility; keep the procedure proportionate to a prototype. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## Detailed description and work sequence
For any approved persistent configuration or anonymous session data, define backups, restore testing, version compatibility, corruption handling, and responsibility; keep the procedure proportionate to a prototype.

Work sequence:

1. Inventory what actually needs backup.

2. Define backup format, schedule, encryption/access, and retention.

3. Implement export/restore scripts with dry-run.

4. Perform a restore drill into an isolated environment.

5. Time-box an investigation spike and record alternatives, compatibility, cost, and risks.

6. Split implementation into pull requests small enough for one beginner working day where necessary.

7. Arrange an independent design/code review and update documentation before considering the task complete.

Dependency handling:

This task depends on MP-037, MP-052. Do not begin dependency-sensitive implementation until the listed outputs are available. The owner may perform reading or a disposable spike earlier, but must re-check assumptions after dependencies merge.

## Beginner learning objectives
- Investigate the technologies and design choices needed for backup, restore, and recovery procedure before implementation.
- Break a production-oriented concern into evidence-backed, reviewable increments.
- Document trade-offs, tests, operational impact, and limitations for future maintainers.

## Deliverables
- Backup/restore scripts
- Recovery runbook
- Restore drill evidence
- Investigation notes/ADR
- Updated operational or user documentation

## Acceptance criteria
- A backup can be restored to a clean environment.
- Corrupt/incompatible backups fail safely.
- Retention/deletion policies also apply to backups.
- The selected approach is justified against at least one alternative.
- Automated or repeatable manual verification is documented.
- Remaining limitations and follow-up tasks are recorded.

## Definition of Done
- All acceptance criteria are demonstrated with evidence in the issue or pull request.
- Relevant documentation is updated so another beginner can repeat the work.
- No credentials, personal images, student emails, or raw volunteer recordings are committed.
- The task owner records decisions, assumptions, unresolved limitations, and follow-up work.
- A focused pull request uses the task ID in its title and links the issue with `Closes #...`.
- A reviewer other than the author examines the change, requested changes are resolved, and CI passes before merge.

## Dependencies and coordination
- Blocking dependencies: MP-037, MP-052
- Related coordination tasks: None
- Initial blocking status: blocked
- Do not mark this issue In Progress until required dependency outputs are available, except for a time-boxed learning spike that is explicitly recorded here.

## Ownership and review
- Team: MovePal Development
- Workstream: Testing/DevOps
- Suggested Scrum role: developer
- Primary assignee: Unassigned until later sprint planning
- Contributors: None planned
- Suggested independent reviewer: Assign during later sprint planning; reviewer must differ from author
- Planned effort allocation: Not assigned in the current sprint
- Pull request: Required
- Suggested branch: `mp-059-backup,-restore,-and-recovery`

## Beginner estimate and buffers
- Focused-work estimate: 16 hours
- Investigation/learning buffer included: 3.2 hours
- Review/collaboration buffer included: 2.4 hours
- QA/rework buffer included: 2.4 hours
- This is a rough beginner estimate. Update the issue when new evidence changes the estimate; do not hide learning time.

## Planning metadata
- Priority: P3
- Sprint designation: future
- Milestone: Production Readiness
- Initial Project stage: Backlog
- Planned start: Not scheduled
- Planned target: Not scheduled
- Manual testing only: No

## Suggested verification
- Backup/restore integration test
- Corruption/version mismatch test

## Risks
- Backups create hidden long-term personal data copies.
- Restore is never tested.

## Security and privacy
- Encrypt/restrict backups when sensitive; honor deletion and retention.

## Helpful documentation topics
- Relevant official library/framework documentation
- Existing MovePal ADRs, tests, and limitations

## Demo/evidence required
- Restore approved sample data into a clean instance.


---

<!-- task-id: MP-060 -->
# MP-060 — Educator dashboard and aggregate session export

## Value
Investigate a local educator-facing overview of anonymous session results and export, with explicit purpose, minimal fields, retention, accessibility, and no child profiling or ranking. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## Detailed description and work sequence
Investigate a local educator-facing overview of anonymous session results and export, with explicit purpose, minimal fields, retention, accessibility, and no child profiling or ranking.

Work sequence:

1. Define educator decisions the dashboard should support.

2. Reject identity, ranking, or health inference fields.

3. Prototype aggregate summaries and CSV/JSON export.

4. Add access/control assumptions and deletion behavior.

5. Time-box an investigation spike and record alternatives, compatibility, cost, and risks.

6. Split implementation into pull requests small enough for one beginner working day where necessary.

7. Arrange an independent design/code review and update documentation before considering the task complete.

Dependency handling:

This task depends on MP-037, MP-044, MP-052. Do not begin dependency-sensitive implementation until the listed outputs are available. The owner may perform reading or a disposable spike earlier, but must re-check assumptions after dependencies merge.

## Beginner learning objectives
- Investigate the technologies and design choices needed for educator dashboard and aggregate session export before implementation.
- Break a production-oriented concern into evidence-backed, reviewable increments.
- Document trade-offs, tests, operational impact, and limitations for future maintainers.

## Deliverables
- Dashboard requirements/ADR
- Aggregate view/export prototype
- Privacy and interpretation guide
- Investigation notes/ADR
- Updated operational or user documentation

## Acceptance criteria
- Exports contain only justified anonymous fields.
- No individual child ranking or diagnostic interpretation exists.
- Users can delete underlying records.
- Aggregates match source sessions.
- The selected approach is justified against at least one alternative.
- Automated or repeatable manual verification is documented.
- Remaining limitations and follow-up tasks are recorded.

## Definition of Done
- All acceptance criteria are demonstrated with evidence in the issue or pull request.
- Relevant documentation is updated so another beginner can repeat the work.
- No credentials, personal images, student emails, or raw volunteer recordings are committed.
- The task owner records decisions, assumptions, unresolved limitations, and follow-up work.
- A focused pull request uses the task ID in its title and links the issue with `Closes #...`.
- A reviewer other than the author examines the change, requested changes are resolved, and CI passes before merge.

## Dependencies and coordination
- Blocking dependencies: MP-037, MP-044, MP-052
- Related coordination tasks: None
- Initial blocking status: blocked
- Do not mark this issue In Progress until required dependency outputs are available, except for a time-boxed learning spike that is explicitly recorded here.

## Ownership and review
- Team: MovePal Development
- Workstream: Product/Documentation
- Suggested Scrum role: developer
- Primary assignee: Unassigned until later sprint planning
- Contributors: None planned
- Suggested independent reviewer: Assign during later sprint planning; reviewer must differ from author
- Planned effort allocation: Not assigned in the current sprint
- Pull request: Required
- Suggested branch: `mp-060-educator-dashboard-and-aggregate`

## Beginner estimate and buffers
- Focused-work estimate: 28 hours
- Investigation/learning buffer included: 5.6 hours
- Review/collaboration buffer included: 4.2 hours
- QA/rework buffer included: 4.2 hours
- This is a rough beginner estimate. Update the issue when new evidence changes the estimate; do not hide learning time.

## Planning metadata
- Priority: P3
- Sprint designation: future
- Milestone: Future Extensions
- Initial Project stage: Backlog
- Planned start: Not scheduled
- Planned target: Not scheduled
- Manual testing only: No

## Suggested verification
- Aggregate calculation tests
- Export schema tests
- Deletion consistency test

## Risks
- Dashboard encourages surveillance or comparison.
- Anonymous data becomes re-identifiable in small groups.

## Security and privacy
- Perform privacy review for small-group re-identification; no child data in development.

## Helpful documentation topics
- Relevant official library/framework documentation
- Existing MovePal ADRs, tests, and limitations

## Demo/evidence required
- Show aggregate/export using synthetic anonymous sessions.


---

<!-- task-id: MP-061 -->
# MP-061 — Release, compatibility, and deprecation policy

## Value
Define versioning, release notes, supported Python/browser/dependency versions, data/config migration, deprecation warnings, and maintenance ownership for MovePal. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## Detailed description and work sequence
Define versioning, release notes, supported Python/browser/dependency versions, data/config migration, deprecation warnings, and maintenance ownership for MovePal.

Work sequence:

1. Choose a simple versioning convention.

2. Define release candidate, tag, notes, artifact, and rollback steps.

3. Document compatibility support windows and deprecation process.

4. Create release checklist and template.

5. Time-box an investigation spike and record alternatives, compatibility, cost, and risks.

6. Split implementation into pull requests small enough for one beginner working day where necessary.

7. Arrange an independent design/code review and update documentation before considering the task complete.

Dependency handling:

This task depends on MP-049, MP-057. Do not begin dependency-sensitive implementation until the listed outputs are available. The owner may perform reading or a disposable spike earlier, but must re-check assumptions after dependencies merge.

## Beginner learning objectives
- Investigate the technologies and design choices needed for release, compatibility, and deprecation policy before implementation.
- Break a production-oriented concern into evidence-backed, reviewable increments.
- Document trade-offs, tests, operational impact, and limitations for future maintainers.

## Deliverables
- Release policy
- Release-note template
- Compatibility/deprecation checklist
- Investigation notes/ADR
- Updated operational or user documentation

## Acceptance criteria
- A maintainer can cut and document a release consistently.
- Breaking changes and migration needs are visible.
- Supported versions match CI evidence.
- The selected approach is justified against at least one alternative.
- Automated or repeatable manual verification is documented.
- Remaining limitations and follow-up tasks are recorded.

## Definition of Done
- All acceptance criteria are demonstrated with evidence in the issue or pull request.
- Relevant documentation is updated so another beginner can repeat the work.
- No credentials, personal images, student emails, or raw volunteer recordings are committed.
- The task owner records decisions, assumptions, unresolved limitations, and follow-up work.
- A focused pull request uses the task ID in its title and links the issue with `Closes #...`.
- A reviewer other than the author examines the change, requested changes are resolved, and CI passes before merge.

## Dependencies and coordination
- Blocking dependencies: MP-049, MP-057
- Related coordination tasks: None
- Initial blocking status: blocked
- Do not mark this issue In Progress until required dependency outputs are available, except for a time-boxed learning spike that is explicitly recorded here.

## Ownership and review
- Team: MovePal Development
- Workstream: Testing/DevOps
- Suggested Scrum role: developer
- Primary assignee: Unassigned until later sprint planning
- Contributors: None planned
- Suggested independent reviewer: Assign during later sprint planning; reviewer must differ from author
- Planned effort allocation: Not assigned in the current sprint
- Pull request: Required
- Suggested branch: `mp-061-release,-compatibility,-and-deprecation`

## Beginner estimate and buffers
- Focused-work estimate: 12 hours
- Investigation/learning buffer included: 2.4 hours
- Review/collaboration buffer included: 1.8 hours
- QA/rework buffer included: 1.8 hours
- This is a rough beginner estimate. Update the issue when new evidence changes the estimate; do not hide learning time.

## Planning metadata
- Priority: P2
- Sprint designation: future
- Milestone: Production Readiness
- Initial Project stage: Backlog
- Planned start: Not scheduled
- Planned target: Not scheduled
- Manual testing only: No

## Suggested verification
- Dry-run release checklist
- Tag/version consistency test

## Risks
- Policy promises support the team cannot provide.
- Versions diverge from tested matrix.

## Security and privacy
- Release artifacts exclude private data and credentials.

## Helpful documentation topics
- Relevant official library/framework documentation
- Existing MovePal ADRs, tests, and limitations

## Demo/evidence required
- Perform a dry-run release from a candidate commit.


---

<!-- task-id: MP-062 -->
# MP-062 — Production-readiness evidence review

## Value
Conduct a structured evidence review across functionality, security, privacy, accessibility, performance, deployment, maintenance, data governance, and incident/recovery readiness. This task decides readiness gaps; it does not declare clinical validity. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## Detailed description and work sequence
Conduct a structured evidence review across functionality, security, privacy, accessibility, performance, deployment, maintenance, data governance, and incident/recovery readiness. This task decides readiness gaps; it does not declare clinical validity.

Work sequence:

1. Define readiness criteria and required evidence links.

2. Review each criterion with independent reviewers.

3. Classify pass, partial, fail, not applicable, and evidence missing.

4. Create blocking remediation tasks and an honest readiness statement.

5. Time-box an investigation spike and record alternatives, compatibility, cost, and risks.

6. Split implementation into pull requests small enough for one beginner working day where necessary.

7. Arrange an independent design/code review and update documentation before considering the task complete.

Dependency handling:

This task depends on MP-035, MP-041, MP-051, MP-052, MP-054, MP-058, MP-059, MP-061. Do not begin dependency-sensitive implementation until the listed outputs are available. The owner may perform reading or a disposable spike earlier, but must re-check assumptions after dependencies merge.

## Beginner learning objectives
- Investigate the technologies and design choices needed for production-readiness evidence review before implementation.
- Break a production-oriented concern into evidence-backed, reviewable increments.
- Document trade-offs, tests, operational impact, and limitations for future maintainers.

## Deliverables
- Readiness review report
- Evidence index
- Remediation backlog
- Go/no-go recommendation
- Investigation notes/ADR
- Updated operational or user documentation

## Acceptance criteria
- Every conclusion links to test/report evidence.
- Unresolved high risks block the relevant deployment claim.
- Medical/clinical validity is explicitly outside scope.
- The selected approach is justified against at least one alternative.
- Automated or repeatable manual verification is documented.
- Remaining limitations and follow-up tasks are recorded.

## Definition of Done
- All acceptance criteria are demonstrated with evidence in the issue or pull request.
- Relevant documentation is updated so another beginner can repeat the work.
- No credentials, personal images, student emails, or raw volunteer recordings are committed.
- The task owner records decisions, assumptions, unresolved limitations, and follow-up work.
- A focused pull request uses the task ID in its title and links the issue with `Closes #...`.
- A reviewer other than the author examines the change, requested changes are resolved, and CI passes before merge.

## Dependencies and coordination
- Blocking dependencies: MP-035, MP-041, MP-051, MP-052, MP-054, MP-058, MP-059, MP-061
- Related coordination tasks: None
- Initial blocking status: blocked
- Do not mark this issue In Progress until required dependency outputs are available, except for a time-boxed learning spike that is explicitly recorded here.

## Ownership and review
- Team: MovePal Development
- Workstream: Product/Documentation
- Suggested Scrum role: developer
- Primary assignee: Unassigned until later sprint planning
- Contributors: None planned
- Suggested independent reviewer: Assign during later sprint planning; reviewer must differ from author
- Planned effort allocation: Not assigned in the current sprint
- Pull request: Required
- Suggested branch: `mp-062-production-readiness-evidence-review`

## Beginner estimate and buffers
- Focused-work estimate: 30 hours
- Investigation/learning buffer included: 6 hours
- Review/collaboration buffer included: 4.5 hours
- QA/rework buffer included: 4.5 hours
- This is a rough beginner estimate. Update the issue when new evidence changes the estimate; do not hide learning time.

## Planning metadata
- Priority: P2
- Sprint designation: future
- Milestone: Production Readiness
- Initial Project stage: Backlog
- Planned start: Not scheduled
- Planned target: Not scheduled
- Manual testing only: No

## Suggested verification
- Evidence-link validation
- Independent review sampling

## Risks
- Checklist becomes a box-ticking exercise.
- Deployment is confused with production readiness.

## Security and privacy
- Privacy/security evidence is access-controlled where necessary.

## Helpful documentation topics
- Relevant official library/framework documentation
- Existing MovePal ADRs, tests, and limitations

## Demo/evidence required
- Present the readiness gaps and justified go/no-go decision.


---

<!-- task-id: MP-063 -->
# MP-063 — Optional custom pose-model training research

## Value
Investigate custom model training only after the rule-based pretrained approach has a documented limitation that cannot be addressed more simply. Define data, labeling, compute, evaluation, bias, maintenance, and deployment implications before any training. This task is intentionally bounded for beginners and includes explicit investigation, implementation or preparation, evidence, peer review, and documentation time rather than treating learning as unpaid overhead.

## Detailed description and work sequence
Investigate custom model training only after the rule-based pretrained approach has a documented limitation that cannot be addressed more simply. Define data, labeling, compute, evaluation, bias, maintenance, and deployment implications before any training.

Work sequence:

1. State the concrete failure and compare simpler alternatives.

2. Define ethically approved adult-only data and labeling needs.

3. Estimate compute, skills, reproducibility, and deployment cost.

4. Design train/validation/test separation and meaningful metrics.

5. Make an adopt/defer/reject recommendation before implementation.

6. Time-box an investigation spike and record alternatives, compatibility, cost, and risks.

7. Split implementation into pull requests small enough for one beginner working day where necessary.

8. Arrange an independent design/code review and update documentation before considering the task complete.

Dependency handling:

This task depends on MP-053, MP-054, MP-062. Do not begin dependency-sensitive implementation until the listed outputs are available. The owner may perform reading or a disposable spike earlier, but must re-check assumptions after dependencies merge.

## Beginner learning objectives
- Investigate the technologies and design choices needed for optional custom pose-model training research before implementation.
- Break a production-oriented concern into evidence-backed, reviewable increments.
- Document trade-offs, tests, operational impact, and limitations for future maintainers.

## Deliverables
- Research proposal/ADR
- Data and evaluation plan
- Cost/risk assessment
- Adopt/defer/reject decision
- Investigation notes/ADR
- Updated operational or user documentation

## Acceptance criteria
- A custom model is justified by evidence, not novelty.
- No child data is proposed or collected.
- Evaluation avoids training/test leakage.
- Maintenance and rollback are addressed.
- The selected approach is justified against at least one alternative.
- Automated or repeatable manual verification is documented.
- Remaining limitations and follow-up tasks are recorded.

## Definition of Done
- All acceptance criteria are demonstrated with evidence in the issue or pull request.
- Relevant documentation is updated so another beginner can repeat the work.
- No credentials, personal images, student emails, or raw volunteer recordings are committed.
- The task owner records decisions, assumptions, unresolved limitations, and follow-up work.
- A focused pull request uses the task ID in its title and links the issue with `Closes #...`.
- A reviewer other than the author examines the change, requested changes are resolved, and CI passes before merge.

## Dependencies and coordination
- Blocking dependencies: MP-053, MP-054, MP-062
- Related coordination tasks: None
- Initial blocking status: blocked
- Do not mark this issue In Progress until required dependency outputs are available, except for a time-boxed learning spike that is explicitly recorded here.

## Ownership and review
- Team: MovePal Development
- Workstream: Computer Vision
- Suggested Scrum role: developer
- Primary assignee: Unassigned until later sprint planning
- Contributors: None planned
- Suggested independent reviewer: Assign during later sprint planning; reviewer must differ from author
- Planned effort allocation: Not assigned in the current sprint
- Pull request: Required
- Suggested branch: `mp-063-optional-custom-pose-model-training`

## Beginner estimate and buffers
- Focused-work estimate: 40 hours
- Investigation/learning buffer included: 8 hours
- Review/collaboration buffer included: 6 hours
- QA/rework buffer included: 6 hours
- This is a rough beginner estimate. Update the issue when new evidence changes the estimate; do not hide learning time.

## Planning metadata
- Priority: P3
- Sprint designation: optional
- Milestone: Future Extensions
- Initial Project stage: Backlog
- Planned start: Not scheduled
- Planned target: Not scheduled
- Manual testing only: No

## Suggested verification
- Proposed reproducible experiment plan
- Baseline comparison design

## Risks
- Dataset and compute requirements are unrealistic.
- Model worsens bias/interpretability.
- Research distracts from maintainable rules.

## Security and privacy
- Adults only, informed consent, minimization, bias analysis, withdrawal.

## Helpful documentation topics
- Relevant official library/framework documentation
- Existing MovePal ADRs, tests, and limitations

## Demo/evidence required
- Present evidence supporting the adopt/defer/reject decision; no training required.


---
