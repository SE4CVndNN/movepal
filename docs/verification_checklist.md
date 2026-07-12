# MovePal bootstrap verification checklist

## Organization teams

- [ ] `team-movepal` exists with Team B's six active members.
- [ ] `team-aidsign` exists with Team A's six active members.
- [ ] No student is an organization owner or repository admin.
- [ ] Any pending invitation is reported and the bootstrap is rerun after acceptance.

## Repository

- [ ] Private `SE4CVndNN/movepal` exists.
- [ ] Default branch is `master`.
- [ ] `team-movepal` has Write access.
- [ ] `team-aidsign` has Triage access.
- [ ] Squash merge is enabled; merge commits/rebase merge are disabled.
- [ ] Feature branches are deleted after merge.
- [ ] No credentials or student email addresses are committed.

## Metadata and Project

- [ ] Required labels exist with descriptions.
- [ ] Four milestones exist.
- [ ] Organization Project exists and is linked to the repository.
- [ ] Custom fields exist: Workflow Stage, Sprint, Priority, Estimate Hours, Position, Workstream, Team, Task ID, Dependency, Start Date, Target Date.
- [ ] Manual views are created using `docs/project_board_views.md`.

## Complete backlog

- [ ] 63 marker-identified issues exist exactly once.
- [ ] MP-001 through MP-027 are assigned to Team B according to the backlog.
- [ ] MP-028 through MP-033 are assigned to Team A, marked manual QA, and dated only 29 July 2026.
- [ ] MP-034 through MP-063 exist in Backlog and remain unassigned.
- [ ] All issues are Project items with Task ID, position, sprint, priority, estimate, team, workstream, dependencies, and dates where applicable.
- [ ] `bootstrap_reports/backlog_import_summary.json` reports no failures.

## CI and workflow

- [ ] CI runs on Ubuntu and Windows.
- [ ] Ruff lint/format, pytest, compileall, and Flask import pass.
- [ ] CI does not access a camera, private dataset, or raw recording.
- [ ] Organization Project workflows are not run in apply mode until their optional credential is configured.

## GitHub Free manual process

- [ ] Students are told that direct pushes to `master` are prohibited by course policy even though private branch protection is unavailable on the current plan.
- [ ] Every implementation task uses an issue, feature branch, PR, independent reviewer, passing CI, and squash merge.
- [ ] Git history and PR reviews are checked at instructor checkpoints.
