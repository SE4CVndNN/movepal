# Contributing to MovePal

This guide defines the required student workflow for MovePal. It applies to code, tests, documentation, fixtures, configuration, and design artifacts.

## 1. Before starting work

1. Open your assigned GitHub issue.
2. Read the entire description, acceptance criteria, Definition of Done, required reading, dependencies, reviewer, and evidence requirements.
3. Confirm that every blocking dependency is complete and merged.
4. Check the Project board for the current Sprint status.
5. Pull the latest `master`.
6. Create the issue’s practical first output before attempting the whole solution.

Do not begin a blocked task merely because time is available. Ask the Scrum Master to confirm another ready task.

## 2. Update the local repository

```bash
git switch master
git pull --ff-only origin master
```

Your working tree should be clean before creating a branch:

```bash
git status
```

## 3. Create a focused branch

Use the task ID and a short description:

```bash
git switch -c mp-014-raise-arms-vertical-slice
```

Recommended patterns:

```text
mp-<number>-<short-description>
fix-<issue-number>-<short-description>
docs-<issue-number>-<short-description>
```

Do not reuse another student’s branch and do not work directly on `master`.

## 4. Implement the smallest complete change

A contribution should be small enough to review. Prefer one coherent task or contract change rather than a large PR containing unrelated code, documentation, refactoring, and assets.

During implementation:

- keep Flask routes thin;
- put domain logic in services;
- use `pathlib.Path` for filesystem paths;
- validate external input;
- avoid global mutable state;
- use type hints where they improve clarity;
- add docstrings for non-obvious algorithms;
- do not commit secrets, raw recordings, private data, or local environment files;
- update documentation when a behavior, data shape, or API contract changes.

## 5. Test before pushing

Run:

```bash
python -m ruff check .
python -m ruff format --check .
python -m pytest
python -m compileall app tests
```

A feature is not complete because it worked once on one machine. Add deterministic tests for normal, invalid, borderline, and missing-data behavior where relevant.

Computer-vision tests must use small fixtures or mocks. They must not require a physical camera, a private recording, or a large dataset download.

## 6. Commit clearly

Use focused commits with understandable messages:

```bash
git add <files>
git commit -m "feat: add raise-arms visibility checks"
```

Useful prefixes include:

```text
feat:     new user-facing behavior
fix:      defect correction
test:     automated tests or fixtures
docs:     documentation only
refactor: internal change without intended behavior change
chore:    tooling, dependencies, or maintenance
```

Do not commit generated caches, virtual environments, raw recordings, or unrelated formatting changes.

## 7. Open a draft pull request early

Push the branch:

```bash
git push -u origin mp-014-raise-arms-vertical-slice
```

Open a draft PR as soon as the practical first output or interface contract is visible. Early PRs help other components integrate before the task is fully complete.

The PR title must include the task ID:

```text
MP-014: Add sample-to-feedback vertical slice
```

The PR body must:

- link the issue with `Closes #<issue-number>`;
- explain the purpose and changes;
- list tests run;
- include screenshots or sample output when relevant;
- explain privacy, accessibility, and cross-platform impact;
- identify known limitations and follow-up work;
- request the assigned independent reviewer.

## 8. Review responsibilities

A reviewer must not be the author or a substantive contributor to the same change.

Reviewers should check:

- agreement with the issue acceptance criteria;
- correctness and understandable design;
- tests for important success and failure paths;
- API/data contract consistency;
- cross-platform path behavior;
- privacy and safe logging;
- user-facing feedback and accessibility;
- documentation accuracy;
- unnecessary scope or complexity.

Do not approve your own PR. Do not approve merely because CI is green. Leave specific, respectful comments and distinguish blocking issues from optional suggestions.

Authors must respond to review comments, update the code, and resolve conversations only after the concern is addressed or an agreed decision is documented.

## 9. CI and merge

Before merge:

- Windows CI passes;
- Linux CI passes;
- required tests pass;
- at least one independent approval is present;
- all required conversations are resolved;
- the PR is no longer a draft;
- documentation and evidence are complete.

Use squash merge and delete the feature branch afterward.

Because this is a private repository in a GitHub Free organization, all branch restrictions may not be technically enforced. Direct student pushes to `master` remain prohibited by the course process and are visible in Git history.

## 10. Project status transitions

Use the Project board to represent reality:

```text
New → In Progress → In Review → Done
```

Use `Blocked` when a required dependency, decision, environment, or review prevents progress. Use `QA` only when the agreed workflow requires an external or formal QA step.

Update the board before or immediately after the daily stand-up.

Do not mark an issue Done until its Definition of Done is satisfied and the PR is merged.

## 11. Handling blockers

Comment on the issue with:

- what is blocked;
- the dependency or decision that is missing;
- what you already tried;
- the person or task that can unblock it;
- the next safe action.

Then move the Project item to `Blocked` and notify the Scrum Master. Do not hide the blocker by hard-coding demo behavior or bypassing validation.

## 12. Documentation and evidence

Documentation is part of the product. Update the relevant existing file rather than creating duplicate instructions.

Evidence may include:

- test output;
- a small JSON response;
- screenshots without personal information;
- a short privacy-safe recording;
- fixture examples;
- a linked CI run;
- an architecture or data-contract update.

Never attach child data, raw volunteer recordings, email addresses, tokens, private file paths, or identifying backgrounds to an issue or PR.

## 13. Scope discipline

Sprint 1 is deliberately narrow. Do not add authentication, complex databases, React, cloud deployment, WebSocket streaming, custom model training, or unrelated future features unless the Product Owner and instructor explicitly approve a scope change.

When a useful idea is outside the Sprint Goal, link it to an existing later backlog task or propose a separate future issue instead of expanding the current PR.
