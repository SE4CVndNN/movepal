# Owner bootstrap guide

## What is essential

Before applying the bootstrap, the owner needs:

1. Windows PowerShell, Git, GitHub CLI, and Python 3.11.
2. An authenticated GitHub CLI account that is an owner/admin of `SE4CVndNN` with `repo`, `admin:org`, and `project` scopes.
3. Valid Git author name and email for the initial commit.
4. The six usernames in each team CSV. Full names and student emails are not required.

The initial setup uses the owner's local GitHub CLI authentication. No repository secret is required for the first creation/import.

## Extract in a normal working folder

Do not run from `C:\Windows\System32`.

```powershell
New-Item -ItemType Directory -Force C:\Projects | Out-Null
Expand-Archive `
  -Path "$HOME\Downloads\movepal-full-bootstrap-v2.zip" `
  -DestinationPath C:\Projects `
  -Force
Set-Location C:\Projects\movepal-full-bootstrap-v2
```

## Confirm tools and Git identity

```powershell
gh auth status
git --version
py -3.11 --version
git config --global user.name
git config --global user.email
```

Configure missing Git identity before applying:

```powershell
git config --global user.name "Diaeddin Rimawi"
git config --global user.email "YOUR_GITHUB_COMMIT_EMAIL"
```

## Validate locally

```powershell
py -3.11 .\scripts\validate_teams.py `
  --team-a .\config\team_a.csv `
  --team-b .\config\team_b.csv

py -3.11 .\scripts\validate_backlog.py `
  --backlog .\backlog\product_backlog.json
```

Expected backlog summary:

- 63 total tasks
- 27 Sprint 1 development tasks
- 6 final-day manual QA tasks
- 30 later tasks
- Team B planned development: 180 of 252 theoretical hours (71.4%)

## Dry-run the complete bootstrap

```powershell
Set-ExecutionPolicy -Scope Process Bypass
.\scripts\bootstrap_org.ps1
```

Dry-run queries current GitHub state but does not create or change resources. Review missing/pending-member warnings and every planned mutation.

## Apply

```powershell
.\scripts\bootstrap_org.ps1 -Apply
```

The apply run creates/reuses:

- `team-movepal` and `team-aidsign`
- private `SE4CVndNN/movepal` repository with `master`
- `team-movepal` Write access and `team-aidsign` Triage access
- labels and milestones
- `MovePal - Product and Sprint Board` organization Project (GitHub displays the configured Unicode title from JSON)
- custom Project fields
- all 63 issues and Project items
- Sprint 1 assignments and final-day QA assignments

Later tasks remain unassigned.

## Safe re-runs

The scripts are idempotent. Issues are matched by markers such as:

```text
<!-- task-id: MP-001 -->
```

A normal re-run skips marker-matched issues. To update existing issue bodies, metadata, labels, assignments, and fields deliberately:

```powershell
.\scripts\bootstrap_org.ps1 -Apply -UpdateExistingIssues
```

To prepare GitHub resources without importing issues:

```powershell
.\scripts\bootstrap_org.ps1 -Apply -SkipBacklogImport
```

Use `-InviteMissingMembers` only when you intentionally want the script to invite a valid missing username. Pending members cannot be added to teams or assigned until they accept; rerun afterward.

## After apply

1. Follow `docs/verification_checklist.md`.
2. Create Project views using `docs/project_board_views.md`.
3. Confirm the first CI run passes on Windows and Linux.
4. Keep organization-level Project workflows disabled/unrun until the optional credential in `docs/github_actions_project_auth.md` is configured.
