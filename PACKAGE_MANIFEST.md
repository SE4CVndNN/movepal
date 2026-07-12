# Package manifest

This package bootstraps the complete MovePal training project in `SE4CVndNN`.

## Planning contents

- Total backlog tasks: **63**
- Sprint 1 development tasks: **27**
- Final-day manual QA tasks: **6**
- Later backlog tasks: **30**
- Team B planned Sprint 1 focused work: **180.0 hours**
- Theoretical Team B capacity: **252.0 hours**
- Planning utilization: **71.4%**
- External QA date: **29 July 2026**

All tasks are imported during the initial apply run. Sprint 1 development and final-day QA tasks receive assignments; later tasks are visible in the Product Backlog and remain unassigned.

## Automation contents

- Owner-run idempotent PowerShell bootstrap with dry-run/apply modes
- Team and backlog validators
- Label, milestone, organization Project, and custom-field preparation
- Idempotent issue importer using stable `<!-- task-id: MP-NNN -->` markers
- Repository CI for Windows and Linux
- Manually triggered preparation/import workflows for later maintenance

## Files

The package contains **82** version-controlled files before Git initialization.

- `.env.example`
- `.github/ISSUE_TEMPLATE/bug_report.yml`
- `.github/ISSUE_TEMPLATE/config.yml`
- `.github/ISSUE_TEMPLATE/task.yml`
- `.github/pull_request_template.md`
- `.github/workflows/ci.yml`
- `.github/workflows/import-backlog.yml`
- `.github/workflows/prepare-project.yml`
- `.gitignore`
- `CODE_OF_CONDUCT.md`
- `CONTRIBUTING.md`
- `LICENSE`
- `README.md`
- `SECURITY.md`
- `app/__init__.py`
- `app/config.py`
- `app/routes/__init__.py`
- `app/routes/api.py`
- `app/routes/pages.py`
- `app/services/__init__.py`
- `app/services/feedback.py`
- `app/services/movement_rules.py`
- `app/services/pose_tracking.py`
- `app/services/scoring.py`
- `app/services/session_summary.py`
- `app/static/css/app.css`
- `app/static/js/app.js`
- `app/templates/base.html`
- `app/templates/index.html`
- `backlog/README.md`
- `backlog/assignment_report.csv`
- `backlog/backlog_schema.json`
- `backlog/dependency_report.md`
- `backlog/product_backlog.json`
- `backlog/product_backlog.md`
- `backlog/qa_backlog.json`
- `backlog/sprint_1.json`
- `backlog/sprint_1_plan.md`
- `backlog/workload_report.md`
- `config/bootstrap_config.json`
- `config/project_metadata.json`
- `config/team_a.csv`
- `config/team_a.example.csv`
- `config/team_b.csv`
- `config/team_b.example.csv`
- `data/README.md`
- `data/landmarks/.gitkeep`
- `data/samples/.gitkeep`
- `data/schemas/.gitkeep`
- `docs/aidsign_handoff_summary.md`
- `docs/annotation_guide.md`
- `docs/architecture.md`
- `docs/bootstrap_guide.md`
- `docs/collection_protocol.md`
- `docs/consent_template.md`
- `docs/dataset_card.md`
- `docs/demo_plan.md`
- `docs/github_actions_project_auth.md`
- `docs/issue_types.md`
- `docs/limitations.md`
- `docs/manual_pr_policy.md`
- `docs/movement_specification.md`
- `docs/privacy.md`
- `docs/project_board_views.md`
- `docs/project_scope.md`
- `docs/qa_handoff.md`
- `docs/qa_plan.md`
- `docs/retrospective.md`
- `docs/sprint_kickoff.md`
- `docs/verification_checklist.md`
- `pyproject.toml`
- `requirements-dev.txt`
- `requirements.txt`
- `run.py`
- `scripts/bootstrap_org.ps1`
- `scripts/import_backlog.py`
- `scripts/prepare_repository.py`
- `scripts/validate_backlog.py`
- `scripts/validate_teams.py`
- `tests/conftest.py`
- `tests/integration/test_app.py`
- `tests/unit/test_scoring.py`
