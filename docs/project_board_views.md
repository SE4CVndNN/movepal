# Manual GitHub Project views

The bootstrap creates the organization Project and custom fields. Create views manually so the owner can inspect and adjust them rather than relying on fragile view automation.

Use the custom **Workflow Stage** field with:

`Backlog -> New -> In Progress -> In Review -> QA -> Blocked -> Done`

## 1. Sprint 1 Board

- Layout: Board
- Filter: `Sprint:Sprint 1`
- Column field: Workflow Stage
- Group or secondary sort: Workstream
- Show: Task ID, assignees, Estimate Hours, Target Date

## 2. Full Product Backlog

- Layout: Table
- Sort: Position ascending
- Show: Task ID, title, Sprint, Priority, Estimate Hours, Workstream, Team, Dependency

## 3. By Assignee

- Layout: Table or Board
- Filter: `Sprint:Sprint 1`
- Group: Assignees
- Sort: Position ascending

## 4. QA Queue

- Layout: Table
- Filter: `Team:"MovePal QA"`
- Sort: Position ascending
- All six planned items should show 29 July 2026 as start and target.

## 5. Blocked Tasks

- Layout: Table
- Filter: `Workflow Stage:Blocked`
- Show: Dependency, Task ID, assignees, Target Date

## 6. Review Queue

- Layout: Table
- Filter: `Workflow Stage:"In Review"`
- Show: assignees, Task ID, workstream, target date

## 7. Future Roadmap

- Layout: Table or roadmap
- Filter: `Sprint:Post-Sprint,Sprint:Future,Sprint:Optional`
- Sort: Position ascending

The imported issue body contains the independent reviewer because GitHub Projects do not provide a native reviewer field for ordinary issues.
