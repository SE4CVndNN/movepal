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
- **Release-candidate tag:** `sprint1-rc1`
- **Frozen application SHA:** `bfde35e112f3846fbf1771bc362154b32c72249a`
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

Sprint 1 development and the MP-024 release-candidate handoff are complete on
`master`. The frozen `sprint1-rc1` application includes the Flask game loop,
live camera and photo input, a deterministic model-free fallback, MediaPipe
pose extraction, three movement families, friendly feedback, session scoring
and summary, privacy/error hardening, automated tests, and Windows/Linux CI.

External QA is coordinated through MP-025 and MP-028 through MP-033. The
release decision remains **Pending QA evidence** until those reports and any
required retests are recorded. See
[`docs/release_notes.md`](docs/release_notes.md) and
[`docs/qa_handoff.md`](docs/qa_handoff.md).

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

Final delivery package:

- [`docs/demo_plan.md`](docs/demo_plan.md)
- [`docs/release_notes.md`](docs/release_notes.md)
- [`docs/contribution_report.md`](docs/contribution_report.md)
- [`docs/retrospective.md`](docs/retrospective.md)

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

### Environment configuration (optional)

The application runs with development defaults, so this step is optional for
local testing. [`.env.example`](.env.example) documents the available variable
names, but `python run.py` does not automatically load a `.env` file. Set an
override in the shell that starts Flask.

```powershell
$env:SECRET_KEY = "replace-with-a-random-local-value"
$env:MAX_CONTENT_LENGTH_MB = "5"
python run.py
```

Linux/macOS:

```bash
export SECRET_KEY="replace-with-a-random-local-value"
export MAX_CONTENT_LENGTH_MB="5"
python run.py
```

Never commit a real secret or a local `.env` file.

## Verify the environment

Run all checks from the repository root:

```bash
python -m ruff check .
python -m ruff format --check .
python -m pytest
python -m compileall app tests scripts
python scripts/qa_selfcheck.py --skip-lint
python -c "from app import create_app; assert create_app().name == 'app'"
```

If Node.js is already installed, an additional JavaScript syntax check is:

```bash
node --check app/static/js/app.js
```

This is the same sequence Windows and Linux CI run on every push and pull request to `master` (see `.github/workflows/ci.yml`).

Run the application:

```bash
python run.py
```

Then open the address printed by Flask, normally `http://127.0.0.1:5000/`.

### Pose model file (only needed for a live `/api/frame` request)

`POST /api/frame` uses `MediaPipePoseAdapter`, which needs a downloaded
MediaPipe Pose Landmarker `.task` model bundle on disk. This file is **not**
committed to the repository (privacy/size — see
[`docs/adr/002-pose-estimator.md`](docs/adr/002-pose-estimator.md)) and is
ignored by `.gitignore`. Automated tests never need it: `pytest` runs entirely
against the offline fixtures in `data/landmarks/`.

To exercise a real frame locally, download the model once into the repository
root (or any path, if you also set `POSE_MODEL_PATH`):

```bash
python -c "import urllib.request; urllib.request.urlretrieve(
    'https://storage.googleapis.com/mediapipe-models/pose_landmarker/'
    'pose_landmarker_lite/float16/latest/pose_landmarker_lite.task',
    'pose_landmarker_lite.task')"
```

By default the app looks for `pose_landmarker_lite.task` next to `run.py`.
Set the `POSE_MODEL_PATH` environment variable to point somewhere else
instead. Never commit the downloaded file or any real captured frame.

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
├── templates/                Jinja HTML templates
└── static/                   CSS, JavaScript, images, and movement assets

data/
├── schemas/                 Landmark and evaluation schemas
└── landmarks/               Synthetic/derived fallback and test fixtures

tests/
├── unit/                    Service-level deterministic tests
├── integration/              Flask route and component-contract tests
└── fixtures/                 Tiny checked-in test inputs

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

External QA is performed by `team-aidsign` on 29 July against
`sprint1-rc1`. QA members run manual sanity checks and open separate bug
issues; they do not silently modify MovePal code. If a release-critical fix is
required, the existing tag stays immutable and a separately reviewed and
retested candidate must be recorded.

Read:

- [`docs/qa_plan.md`](docs/qa_plan.md)
- [`docs/qa_handoff.md`](docs/qa_handoff.md)
- [`docs/demo_plan.md`](docs/demo_plan.md)
- [`docs/release_notes.md`](docs/release_notes.md)
- [`docs/contribution_report.md`](docs/contribution_report.md)
- [`docs/retrospective.md`](docs/retrospective.md)

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

Do not block the demonstration on a specific device. Use the built-in
deterministic fallback, which evaluates the selected movement through the same
movement API without requiring a camera or pose-model download. Record the
browser, operating system, and observed permission behavior in the QA issue.

### Tests work locally but fail in CI

Check both Windows and Linux logs. Common causes include case-sensitive paths, hard-coded separators, files not committed to Git, current-working-directory assumptions, and tests that access real hardware.

### A dependency is not ready

Do not bypass it silently. Comment on the issue, move the item to `Blocked`, identify the missing output, and notify the Scrum Master. Continue another ready task only after coordination.

## Administration scripts

The owner/bootstrap scripts are for project administration. Students should not rerun them unless explicitly instructed:

- `scripts/bootstrap_org.ps1`
- `scripts/prepare_repository.py`
- `scripts/import_backlog.py`
- `scripts/validate_external_asset.py`

The authoritative task descriptions are the GitHub issues and [`backlog/product_backlog.json`](backlog/product_backlog.json).
