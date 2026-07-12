# MovePal

MovePal is a private software-engineering training project in the `SE4CVndNN` GitHub organization. It is a playful movement-practice prototype: a toy/avatar demonstrates a movement, the browser captures a frame or uses an included fallback sample, a Flask service estimates pose landmarks, and rule-based logic returns friendly feedback, points, and a short session summary.

MovePal is not a medical device, diagnostic tool, clinical rehabilitation system, or replacement for a medical professional.

## Sprint 1

- Kickoff: 13 July 2026
- Sprint: 14-29 July 2026
- Development: Team B / `team-movepal`
- External manual QA: Team A / `team-aidsign`, only on 29 July after the release candidate is frozen
- Default branch: `master`
- Repository: private, GitHub Free organization

## Bootstrap behavior

The owner PowerShell bootstrap creates or validates the organization teams, private repository, team access, labels, milestones, organization Project, custom fields, and repository link. It then imports all 63 backlog issues:

- 27 assigned Sprint 1 development issues
- 6 assigned final-day manual QA issues
- 30 post-sprint, future, or optional issues imported but left unassigned

Start with [docs/bootstrap_guide.md](docs/bootstrap_guide.md). The authoritative backlog is [backlog/product_backlog.json](backlog/product_backlog.json), and the readable version is [backlog/product_backlog.md](backlog/product_backlog.md).

## Local development after repository creation

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements-dev.txt
python -m pytest
python run.py
```

On Linux/macOS, activate with `source .venv/bin/activate`. Python code uses `pathlib` and portable paths. CI runs on Windows and Linux.

## Important files

- `scripts/bootstrap_org.ps1`: owner-run idempotent bootstrap; dry-run by default
- `scripts/validate_backlog.py`: validates all task fields, dependencies, assignments, QA policy, and workload
- `scripts/prepare_repository.py`: labels, milestones, Project, fields, and link
- `scripts/import_backlog.py`: idempotent issue and Project import using stable task markers
- `.github/workflows/prepare-project.yml`: later metadata preparation workflow
- `.github/workflows/import-backlog.yml`: later backlog re-import/update workflow
- `.github/workflows/ci.yml`: Windows/Linux quality and test workflow
