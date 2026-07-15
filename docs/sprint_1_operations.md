# Sprint 1 Operations

## 1. Purpose

This document records the team-specific operational decisions required for
MovePal Sprint 1. It complements the repository's existing contribution,
workflow, and architecture guidance; it does not replace those documents or
repeat general Scrum theory.

## 2. Reviewer Rotation

The issue-specific reviewer named in a task takes priority. The following
rotation provides a default reviewer and a fallback when an issue does not name
an available independent reviewer.

| Author | Default reviewer | Fallback reviewer |
|---|---|---|
| `@alaamadii` | `@IslamOuda85` | `@AhmadKollab` |
| `@IslamOuda85` | `@AhmadKollab` | `@myarnwas` |
| `@AhmadKollab` | `@myarnwas` | `@JHT127` |
| `@myarnwas` | `@JHT127` | `@MennaAllah-Alatrsh` |
| `@JHT127` | `@MennaAllah-Alatrsh` | `@alaamadii` |
| `@MennaAllah-Alatrsh` | `@alaamadii` | `@IslamOuda85` |

Reviewer rules:

- No self-review.
- No self-approval.
- A reviewer must not be an author or contributor to the change.
- The reviewer specified by the issue takes priority over this rotation.
- If the assigned reviewer is unavailable or ineligible, use the fallback
  reviewer only when that person is also independent of the change.
- If neither reviewer is eligible, notify the Scrum Master to assign another
  independent reviewer.

## 3. Blocked Dependency Escalation

When a dependency or decision prevents meaningful progress, the task owner
must:

1. Add a concise comment to the blocked issue.
2. Identify the missing dependency or decision by task ID where applicable.
3. Record what has already been checked or attempted.
4. Mention the person responsible for the dependency or decision.
5. State the next safe action that can be taken without bypassing the
   dependency.
6. Move the Project item to **Blocked**.
7. Notify `@alaamadii`, the Scrum Master.

Use this issue-comment format:

```markdown
## Blocker

- Blocked work:
- Missing dependency or decision:
- Checks already completed:
- Person who can unblock it:
- Next safe action:
```

Dependency-sensitive implementation must not proceed until the required output
is merged or the dependency is resolved through a recorded decision.

## 4. Sprint 1 Readiness Checklist

| GitHub Username | Repository Access | Project Access | First Assigned Issue | Dependencies | Reviewer | Practical First Output | Status |
|---|---|---|---|---|---|---|---|
| `@alaamadii` | Confirmed | Confirmed | MP-001 | None | `@IslamOuda85` | Verified Sprint 1 board with correct assignments and visible dates | In Progress |
| `@IslamOuda85` | Confirmed | Confirmed | MP-002 | MP-001 | `@alaamadii` | `docs/mvp_acceptance_map.md` mapping capabilities to evidence and owners | Ready; waiting for dependency |
| `@AhmadKollab` | Confirmed | Confirmed | MP-004 | MP-002, MP-003 | `@alaamadii` | Executable page and JSON route in the repository | Ready; waiting for dependencies |
| `@myarnwas` | Confirmed | Confirmed | MP-005 | MP-002, MP-003 | `@AhmadKollab` | Interface schema and mock fixtures for the MediaPipe Pose service contract | Ready; waiting for dependencies |
| `@JHT127` | Confirmed | Confirmed | MP-006 | MP-002, MP-003 | `@IslamOuda85` | Clickable low-fidelity game flow in Jinja/static assets | Ready; waiting for dependencies |
| `@MennaAllah-Alatrsh` | Confirmed | Confirmed | MP-007 | MP-005, MP-006 | `@JHT127` | Updated `docs/movement_specification.md` | Ready; waiting for dependencies |

Each member should acknowledge their row after confirming access and reading
their assigned issue in full.

## 5. Board Verification

- [X] Sprint 1 items are visible in the MovePal Project.
- [X] Sprint 1 assignments have been checked against the authoritative
      backlog.
- [X] Start and target dates are visible.
- [X] Workflow stages reflect the current state of the work.
- [X] Missing or incorrect assignments are recorded with an owner and next
      action.
- [X] An independent reviewer is identified for each assigned task.
- [X] Verification date recorded: `14-07-2026`.
- [X] Verified by: `@alaamadii`.

## 6. Operating Rules

- Always create a focused branch from the current `master` branch.
- Never push directly to the repository's default branch, `master`.
- Always create a pull request for a change that requires repository updates.
- Include the task ID in the pull-request title.
- Link the issue in the pull-request body using `Closes #<issue_number>`.
- Obtain an independent review before merge.
- Do not approve your own pull request.
- Required CI checks must pass before merge.
- Resolve required review conversations before merge.
- Use squash merge and delete the feature branch after merging.

## 7. Notes

This operational record complements:

- [`CONTRIBUTING.md`](../CONTRIBUTING.md)
- [`docs/student_start_here.md`](student_start_here.md)
- [`docs/manual_pr_policy.md`](manual_pr_policy.md)
- [`docs/architecture.md`](architecture.md)

Those documents remain authoritative for their respective topics. This file
records only the Sprint 1 team decisions needed to apply them in daily work.
