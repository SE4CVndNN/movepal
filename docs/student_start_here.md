# MovePal: student start here

Read this page before opening a feature branch. The instructor explains the project, waterfall/agile/Scrum, roles, and the board during kickoff; students should not spend Sprint time rewriting that material.

## 1. Find your work

1. Open **MovePal — Product and Sprint Board**.
2. Filter to **Sprint 1** and your GitHub username.
3. Open the earliest assigned issue whose dependencies are complete.
4. Read the entire issue, especially **Read first**, **Practical first output**, dependencies, acceptance criteria, and Definition of Done.
5. Confirm the planned reviewer is not an author or contributor.

## 2. Begin with a visible artifact

Before attempting the whole task, produce the issue’s practical first output: a small test, fixture, contract example, clickable screen, table, or documented decision. Link it in the issue or draft PR so misunderstanding is discovered early.

## 3. Normal engineering flow

```text
Issue → dependency check → branch → practical first output → implementation/tests
→ draft PR → independent review → CI → squash merge → board Done
```

Use the suggested branch name. Put the task ID in the PR title and `Closes #<issue>` in the PR body.

## 4. When blocked

Do not quietly work around an unresolved dependency. Add a short comment containing:

- what is blocked;
- which dependency or decision is missing;
- what you already checked;
- the person who can help;
- the next safe action.

Move the board item to Blocked and notify the Scrum Master.

## 5. Privacy and prototype boundary

- Do not collect or commit child data.
- Prefer synthetic/anonymized landmarks to raw media.
- Do not log frames or image bytes.
- MovePal is playful movement practice, not diagnosis, treatment, rehabilitation, or physiotherapy.
- Use the approved wording in `docs/content_baseline.md` once MP-002 merges.

## 6. Daily completion check

Before stopping, update the issue status, record the current evidence or blocker, push your branch, and identify the next concrete step.
