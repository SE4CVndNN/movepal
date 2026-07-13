# MovePal

MovePal is a software-engineering training project in the `SE4CVndNN` GitHub organization. The team is building a playful browser-based movement game in which an avatar demonstrates a simple movement, the user tries it in front of a webcam or with an included fallback sample, and the application returns friendly feedback, stars, and a short session summary.

MovePal is a **prototype for playful movement practice**. It is not a medical device, diagnostic tool, clinical rehabilitation system, or replacement for a physiotherapist or another healthcare professional.

## Sprint 1 at a glance

- **Kickoff:** Monday, 13 July 2026
- **Sprint:** Tuesday, 14 July–Wednesday, 29 July 2026
- **Development team:** Team B / `team-movepal`
- **External QA team:** Team A / `team-aidsign`
- **Release-candidate freeze:** Tuesday, 28 July 2026
- **External manual QA:** Wednesday, 29 July 2026
- **Default branch:** `master`
- **Python:** 3.11
- **Repository:** private, under a GitHub Free organization

Instructor checkpoints are held on Monday and Wednesday at **20:00 Palestine time**, for at most one hour. The development team also holds a focused daily stand-up of approximately 10 minutes.

## Sprint Goal

By the end of Sprint 1, MovePal should provide a demonstrable Flask web application with:

1. a clear child-friendly game interface;
2. webcam capture and a reliable sample-image or sample-video fallback;
3. pretrained pose-landmark extraction;
4. three supported movements:
   - raise both arms;
   - side reach to the left or right;
   - knee lift or step in place;
5. visibility and framing checks;
6. rule-based movement evaluation;
7. friendly, non-medical feedback;
8. stars or points;
9. a short session summary;
10. invalid-input and low-confidence handling;
11. automated tests, Ruff checks, and Windows/Linux CI;
12. privacy, limitations, QA, and demonstration documentation.

The full Product Backlog contains later improvements, but students must not begin post-Sprint, future, or optional work unless the Product Owner and instructor explicitly change the Sprint scope.

## Current repository status

The repository starts with a small Flask application factory, a landing page, a health endpoint, service contracts, starter tests, and CI configuration. Some modules are intentionally incomplete because they are assigned Sprint tasks.

Do not assume a placeholder service is a finished feature. Read the assigned GitHub issue, its dependencies, and its acceptance criteria before modifying code.

## Start here

Every student should read these files before beginning an assigned issue:

1. [`docs/student_start_here.md`](docs/student_start_here.md)
2. [`docs/sprint_kickoff.md`](docs/sprint_kickoff.md)
3. [`docs/sprint_execution_plan.md`](docs/sprint_execution_plan.md)
4. [`docs/role_playbooks.md`](docs/role_playbooks.md)
5. [`docs/project_scope.md`](docs/project_scope.md)
6. [`docs/architecture.md`](docs/architecture.md)
7. [`CONTRIBUTING.md`](CONTRIBUTING.md)
8. [`docs/manual_pr_policy.md`](docs/manual_pr_policy.md)
9. [`docs/privacy.md`](docs/privacy.md)
10. [`docs/limitations.md`](docs/limitations.md)
11. [`backlog/sprint_1_plan.md`](backlog/sprint_1_plan.md)
12. the assigned GitHub issue and every dependency referenced by that issue.

Useful planning reports:

- [`backlog/assignment_report.csv`](backlog/assignment_report.csv)
- [`backlog/workload_report.md`](backlog/workload_report.md)
- [`backlog/dependency_report.md`](backlog/dependency_report.md)
- [`backlog/blocked_task_report.md`](backlog/blocked_task_report.md)
- [`backlog/review_assignment_report.md`](backlog/review_assignment_report.md)

## Local setup

### Windows PowerShell

```powershell
# From the repository root
py -3.11 -m venv .venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements-dev.txt
```

### Linux or macOS

```bash
# From the repository root
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements-dev.txt
```

If `python3.11` is not available, install Python 3.11 before continuing. Do not silently use a different major/minor version without discussing compatibility with the Scrum Master.

## Verify the environment

Run all checks from the repository root:

```bash
python -m ruff check .
python -m ruff format --check .
python -m pytest
python -m compileall app tests
```

Run the application:

```bash
python run.py
```

Then open the address printed by Flask, normally `http://127.0.0.1:5000/`.

The health endpoint is:

```text
GET /api/health
```

A healthy starter application returns JSON equivalent to:

```json
{
  "service": "movepal",
  "status": "ok"
}
```

## Repository structure

```text
app/
├── __init__.py              Flask application factory
├── config.py                Portable configuration and upload limits
├── routes/                  Thin HTML and JSON routes
├── services/                Pose, movement, feedback, scoring, session logic
├── templates/               Jinja HTML templates
└── static/                  CSS, JavaScript, images, and movement assets

data/
├── samples/                 Small privacy-safe fallback samples
├── schemas/                 Landmark and evaluation schemas
└── landmarks/               Small derived fixtures; no raw private recordings

tests/
├── unit/                    Service-level deterministic tests
├── integration/             Flask route and component-contract tests
└── fixtures/                Tiny checked-in test inputs

docs/                        Product, architecture, privacy, data, QA, and demo guidance
backlog/                     Authoritative machine-readable and readable planning data
.github/                    Issue templates, PR template, and CI workflows
```

Use `pathlib.Path` for filesystem paths. Do not hard-code Windows drive letters or platform-specific separators in Python code.

## Development workflow

```text
Assigned issue
→ verify dependencies
→ create a feature branch
→ produce the practical first output
→ implement and test
→ open a draft pull request
→ obtain independent review
→ pass Windows and Linux CI
→ resolve comments
→ squash merge into master
→ move the issue to Done
```

Example branch:

```text
mp-014-raise-arms-vertical-slice
```

Example PR title:

```text
MP-014: Add sample-to-feedback vertical slice
```

Follow [`CONTRIBUTING.md`](CONTRIBUTING.md) and [`docs/manual_pr_policy.md`](docs/manual_pr_policy.md). Students must not push directly to `master`.

## Design rules

- Keep Flask routes thin.
- Put pose, movement, scoring, feedback, and session logic in services.
- Validate uploads before processing them.
- Use allowed file types and configured size limits.
- Do not log images, raw frames, personal information, or private file paths.
- Use deterministic landmark fixtures in automated tests.
- Do not require a real camera or a large model/data download in CI.
- Return an explicit retry or low-confidence result instead of forcing success.
- Keep feedback friendly and non-medical.
- Update documentation when behavior or contracts change.

## Data and privacy

Sprint 1 requires no child data. Calibration or usability work may use consenting adult volunteers only after the instructor approves the collection procedure.

Prefer storing derived landmarks rather than video. Keep raw recordings under private, ignored storage such as `data/private/` or `data/raw/`; never commit them, upload them to Actions, or attach them to issues.

Read:

- [`docs/privacy.md`](docs/privacy.md)
- [`docs/dataset_card.md`](docs/dataset_card.md)
- [`docs/collection_protocol.md`](docs/collection_protocol.md)
- [`docs/annotation_guide.md`](docs/annotation_guide.md)
- [`docs/consent_template.md`](docs/consent_template.md)

## Movement implementation

The movement rules are transparent game heuristics, not clinical measurements. Thresholds must be configurable, tested with positive/negative/borderline fixtures, and justified in the evaluation notes.

Read [`docs/movement_specification.md`](docs/movement_specification.md) before implementing or reviewing movement logic.

## External QA and final demonstration

External QA is performed by `team-aidsign` on 29 July against one frozen release-candidate commit. QA members run manual sanity checks and open separate bug issues; they do not silently modify MovePal code.

Read:

- [`docs/qa_plan.md`](docs/qa_plan.md)
- [`docs/qa_handoff.md`](docs/qa_handoff.md)
- [`docs/demo_plan.md`](docs/demo_plan.md)

## Common problems

### PowerShell will not activate the virtual environment

Use a process-only policy change:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force
.\.venv\Scripts\Activate.ps1
```

This applies only to the current PowerShell session.

### MediaPipe does not install

Confirm that the active interpreter is Python 3.11:

```bash
python --version
python -m pip --version
```

Delete and recreate the virtual environment if it was created with another Python version.

### The camera is unavailable or permission is denied

Do not block the Sprint on a specific device. Use the required fallback sample path once MP-012 is merged. Record the browser, operating system, and observed permission behavior in the issue or PR.

### Tests work locally but fail in CI

Check both Windows and Linux logs. Common causes include case-sensitive paths, hard-coded separators, files not committed to Git, current-working-directory assumptions, and tests that access real hardware.

### A dependency is not ready

Do not bypass it silently. Comment on the issue, move the item to `Blocked`, identify the missing output, and notify the Scrum Master. Continue another ready task only after coordination.

## Administration scripts

The owner/bootstrap scripts are for project administration. Students should not rerun them unless explicitly instructed:

- `scripts/bootstrap_org.ps1`
- `scripts/prepare_repository.py`
- `scripts/import_backlog.py`

The authoritative task descriptions are the GitHub issues and [`backlog/product_backlog.json`](backlog/product_backlog.json).
