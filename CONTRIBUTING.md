# Contributing to MovePal

Thank you for contributing to MovePal. This document provides guidelines and conventions for contributing to the project to ensure a smooth workflow and clean code repository.

---

## Code of Conduct

By participating in this project, you agree to foster an open and welcoming environment. Please keep discussions respectful, constructive, and focused on collaborative problem-solving.

---

## Getting Started

1. **Fork or Clone the Repository:**
   Ensure you have cloned the project repository locally:
   ```bash
   git clone [https://github.com/your-org/movepal.git](https://github.com/your-org/movepal.git)
   cd movepal
   ```

2. **Set Up the Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   pip install -r requirements.txt
   ```

---

## Git Workflow & Branching Strategy

We follow a feature-branch / Pull Request (PR) workflow off the `master` branch.

### 1. Branch Naming Conventions
Always create a new branch from an updated `master`. Use descriptive branch names with appropriate prefixes:

* **Features / Tasks:** `feature/task-<number>-<short-description>` (e.g., `feature/task-9-scoring-rules`)
* **Bug Fixes:** `fix/<issue-description>` (e.g., `fix/landmark-angle-calculation`)
* **Documentation:** `docs/<description>` (e.g., `docs/update-readme`)
* **Refactoring:** `refactor/<description>` (e.g., `refactor/feedback-service`)

### 2. Keeping Your Branch Updated
Before submitting a Pull Request or starting work, pull the latest changes from `master`:

```bash
git checkout master
git pull origin master
git checkout <your-branch-name>
git merge master
```

---

## Commit Message Guidelines

Write clear, concise commit messages that describe the intent of your changes. We encourage following the Conventional Commits specification:

* `feat:` A new feature or capability (e.g., `feat: add knee angle verification in movement_rules`)
* `fix:` A bug fix (e.g., `fix: resolve frame rate lag in pose_tracking`)
* `docs:` Documentation changes only (e.g., `docs: update setup steps in README`)
* `refactor:` Code changes that neither fix a bug nor add a feature (e.g., `refactor: optimize scoring algorithm`)
* `test:` Adding or updating tests (e.g., `test: add pytest fixtures for squat landmarks`)
* `chore:` Maintenance tasks, dependency updates, or project configuration

---

## Coding Standards

### Python Guidelines
* **Style:** Follow standard **PEP 8** formatting conventions.
* **Type Hints:** Use type hints for function arguments and return values where applicable.
* **Docstrings:** Provide concise docstrings for functions, classes, and service modules.

Example:
```python
def calculate_joint_angle(point_a: tuple, point_b: tuple, point_c: tuple) -> float:
    """Calculates the angle between three 2D/3D joint landmarks."""
    # Implementation logic
    pass
```

### Testing
* Write unit tests for new service modules and movement rules.
* Place test files in the appropriate `tests/` directory or alongside tests.
* Ensure all existing and new tests pass before opening a PR:
  ```bash
  pytest
  ```
* Include landmark JSON test fixtures in `data/landmarks/` when introducing new pose fixtures.

---

## Pull Request Process

1. **Self-Review:** Review your code changes and remove any unneeded debug logs or temporary commented code.
2. **Push Branch:** Push your feature branch to the remote repository:
   ```bash
   git push origin <your-branch-name>
   ```
3. **Open Pull Request:** Open a PR targeting the `master` branch.
4. **PR Description Checklist:**
   * Summarize the changes introduced.
   * Reference relevant task numbers (e.g., `Closes Task 9`).
   * List testing steps taken to verify the changes.
5. **Code Review:** Address any feedback provided by reviewers. Once approved and checks pass, the PR will be merged into `master`.
