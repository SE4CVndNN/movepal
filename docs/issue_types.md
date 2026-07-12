# Issue types

GitHub organizations include the default issue types **Task**, **Bug**, and **Feature**. The backlog importer applies them as follows:

- `type:feature` label -> Feature
- `type:bug` label -> Bug
- research, setup, documentation, test, DevOps, QA, security, and accessibility work -> Task

Detailed classification remains in repository labels because it is more specific and consistent across MovePal and AidSign. The importer reports a warning rather than failing the whole backlog if an owner has disabled or renamed a default issue type.

Do not create duplicate organization issue types merely to mirror every repository label. Any organization-wide type change affects both projects and should be coordinated once by the owner.
