# Planning enhancement summary

The existing MovePal setup remains intact: same repository, Project, teams, milestones, 63 task IDs, Sprint dates, and final-day QA model.

## Why the plan changed

The original backlog was valid but the first tasks asked the Scrum Master and Product Owner to recreate material already delivered during the instructor kickoff. The enhanced plan treats the kickoff and repository documentation as required reading, then asks for practical outputs: a verified board, scope decisions, contract examples, branch/PR rehearsal, and runnable learning spikes.

Integration risk is reduced by turning **MP-014** into a thin vertical slice. By 22 July, a deterministic sample must travel through the Flask API, pose/mock service, raise-arms rule, and visible feedback. **MP-019** then expands this proven contract into the complete three-movement flow.

## Resource model

- 177 planned development hours (70.2% of theoretical capacity).
- Individual planned loads range from 28.2 to 31.5 hours.
- The unplanned reserve covers instructor meetings, stand-ups, code review, support, integration, defects, absence, and demo preparation.
- Six external QA tasks remain manual, parallel, and restricted to the frozen release candidate on 29 July.

## GitHub synchronization

The enhancement script updates issue titles, bodies, labels, assignments, milestones, and Project fields by the existing stable `MP-NNN` markers. It creates no new issue and deletes no issue. A dry-run is mandatory before apply.
