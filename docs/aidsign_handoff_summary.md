# Handoff summary for the AidSign project chat

Use this after the MovePal bootstrap has been successfully applied. Verify the resources before assuming completion.

## Organization resources already created and shared

Organization: `SE4CVndNN`

Two organization teams already exist and must be reused rather than recreated:

### `team-movepal`

Members:

- `alaamadii` - Scrum Master for Team B
- `IslamOuda85` - Product Owner for Team B
- `AhmadKollab`
- `myarnwas`
- `JHT127`
- `fatimarajab12`

Membership continuity note: `@fatimarajab12` replaced
`@MennaAllah-Alatrsh` in the active MovePal team on 18 July 2026. Existing
commits, reviews, and completed-task history remain attributed to their
original authors.

Responsibilities:

- MovePal development
- AidSign external QA

### `team-aidsign`

Members:

- `Tojan-Naiem` - Scrum Master for Team A
- `SajaZenaty` - Product Owner for Team A
- `nezarYousef`
- `saliqasarwi`
- `SaadRayh`
- `BaraahMazeen`

Responsibilities:

- AidSign development
- MovePal external QA

Do not invite these users again unless a membership check shows that someone is missing or pending. Do not create duplicate teams with different names.

## MovePal-specific resources already created

- Private repository: `SE4CVndNN/movepal`
- Default branch: `master`
- MovePal Project: `MovePal — Product and Sprint Board`
- `team-movepal`: Write on MovePal
- `team-aidsign`: Triage on MovePal
- MovePal labels, milestones, issue templates, workflows, 63 backlog issues, Sprint 1 assignments, and manual QA issues

These are MovePal-specific and must not be recreated or overwritten by the AidSign bootstrap.

## What AidSign still needs

The AidSign chat should create only AidSign-specific resources:

- private `SE4CVndNN/aidsign` repository, default branch `master`
- AidSign organization Project and Project fields/views
- AidSign repository labels and milestones
- AidSign repository skeleton, documentation, tests, and CI
- complete AidSign product backlog and AidSign Sprint 1 assignments
- final-day manual AidSign QA tasks assigned to `team-movepal`
- AidSign repository permissions:
  - `team-aidsign`: Write
  - `team-movepal`: Triage

Repository labels and milestones are repository-specific, so AidSign creates its own equivalent metadata. Project fields/views are Project-specific, so AidSign creates its own Project configuration. Organization teams and memberships are shared and should only be verified/reused.

## Shared decisions to keep consistent

- GitHub organization plan: Free
- repositories: private
- default branch: `master`
- owner bootstrap environment: Windows PowerShell
- project code/scripts must use OS-independent paths such as Python `pathlib`
- CI should include Windows and Linux
- no student becomes organization owner or repository admin
- private branch protection is not available under this plan, so the course manually enforces issue -> branch -> PR -> independent review -> passing CI -> squash merge
- no author approves their own PR
- all backlog tasks are imported at initial project creation; only the selected sprint is assigned
- external QA is manual and concentrated on the final sprint day after a frozen release candidate
- do not expose student email addresses or owner credentials

## Automation credential note

The initial MovePal setup used the owner's local authenticated GitHub CLI and required no Actions secret. If a GitHub App or narrowly scoped organization-Project automation credential is later created, the AidSign setup may reuse the same organization app only after its installation/repository access is deliberately extended to AidSign. Do not copy or expose the owner's broad `gh` OAuth token.
