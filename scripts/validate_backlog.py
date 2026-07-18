#!/usr/bin/env python3
"""Validate the enhanced MovePal backlog and Sprint 1 resource plan."""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

TASK_ID = re.compile(r"^MP-(\d{3})$")
SPRINT_VALUES = {"sprint-1", "post-sprint", "future", "optional"}
TEAM_B = {
    "alaamadii",
    "IslamOuda85",
    "AhmadKollab",
    "myarnwas",
    "JHT127",
    "fatimarajab12",
}
TEAM_A = {
    "Tojan-Naiem",
    "SajaZenaty",
    "nezarYousef",
    "saliqasarwi",
    "SaadRayh",
    "BaraahMazeen",
}
REQUIRED = {
    "task_id",
    "position",
    "title",
    "value",
    "description",
    "beginner_learning_objective",
    "deliverables",
    "acceptance_criteria",
    "definition_of_done",
    "dependencies",
    "related_tasks",
    "blocking_status",
    "workstream",
    "suggested_scrum_role",
    "team",
    "primary_assignee",
    "contributors",
    "suggested_reviewer",
    "estimated_focused_work_hours",
    "investigation_buffer_hours",
    "preparation_learning_hours",
    "implementation_hours",
    "testing_hours",
    "review_buffer_hours",
    "qa_buffer_hours",
    "effort_allocation_hours",
    "priority",
    "sprint_designation",
    "github_labels",
    "milestone",
    "project_status",
    "risks",
    "helpful_references",
    "pull_request_required",
    "suggested_branch_name",
    "suggested_test_requirements",
    "security_privacy_considerations",
    "demo_evidence_required",
    "start_date",
    "target_date",
    "manual_testing_only",
    "required_reading",
    "practical_output",
    "dependency_rationale",
    "handoff_to",
    "issue_body",
}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--backlog", type=Path, default=Path("backlog/product_backlog.json")
    )
    args = parser.parse_args()

    data = json.loads(args.backlog.read_text(encoding="utf-8"))
    tasks = data.get("tasks", [])
    errors: list[str] = []
    ids: dict[str, dict] = {}
    positions: set[int] = set()

    if len(tasks) != 63:
        errors.append(f"Expected 63 stable tasks, found {len(tasks)}.")

    for task in tasks:
        tid = task.get("task_id", "<unknown>")
        missing = REQUIRED - set(task)
        if missing:
            errors.append(f"{tid}: missing fields {sorted(missing)}")
            continue

        match = TASK_ID.fullmatch(tid)
        if not match:
            errors.append(f"Invalid task ID: {tid}")
        elif int(match.group(1)) != task["position"]:
            errors.append(f"{tid}: position must equal numeric ID.")
        if tid in ids:
            errors.append(f"Duplicate task ID: {tid}")
        if task["position"] in positions:
            errors.append(f"Duplicate position: {task['position']}")
        ids[tid] = task
        positions.add(task["position"])

        if task["sprint_designation"] not in SPRINT_VALUES:
            errors.append(f"{tid}: invalid sprint designation")
        if len(task["description"]) < 500 or len(task["issue_body"]) < 1800:
            errors.append(f"{tid}: description/issue body is not sufficiently detailed")
        if f"<!-- task-id: {tid} -->" not in task["issue_body"]:
            errors.append(f"{tid}: stable marker missing")
        if (
            not task["required_reading"]
            or not task["practical_output"]
            or not task["dependency_rationale"]
        ):
            errors.append(
                f"{tid}: reading, practical output, and dependency rationale are required"
            )

        parts = sum(
            float(task[name])
            for name in (
                "investigation_buffer_hours",
                "preparation_learning_hours",
                "implementation_hours",
                "testing_hours",
                "review_buffer_hours",
                "qa_buffer_hours",
            )
        )
        if abs(parts - float(task["estimated_focused_work_hours"])) > 0.01:
            errors.append(
                f"{tid}: effort breakdown {parts:g} does not equal estimate "
                f"{task['estimated_focused_work_hours']}"
            )

    # Validate dependency graph and assignment rules.
    graph: dict[str, list[str]] = {}
    for task in tasks:
        tid = task["task_id"]
        graph[tid] = list(task["dependencies"])
        for dep in task["dependencies"]:
            if dep not in ids:
                errors.append(f"{tid}: unknown dependency {dep}")
            elif ids[dep]["position"] >= task["position"]:
                errors.append(f"{tid}: dependency {dep} is not numerically earlier")

        allocations = {
            user: float(hours)
            for user, hours in task["effort_allocation_hours"].items()
        }
        if task["sprint_designation"] == "sprint-1":
            expected_team = TEAM_A if task["manual_testing_only"] else TEAM_B
            if (
                not task["primary_assignee"]
                or task["primary_assignee"] not in expected_team
            ):
                errors.append(f"{tid}: invalid Sprint assignee")
            if set(allocations) - expected_team:
                errors.append(
                    f"{tid}: allocation contains a member outside the responsible team"
                )
            if (
                abs(
                    sum(allocations.values())
                    - float(task["estimated_focused_work_hours"])
                )
                > 0.01
            ):
                errors.append(f"{tid}: allocations do not sum to estimate")
            if task["suggested_reviewer"] in allocations:
                errors.append(f"{tid}: reviewer is also an author/contributor")
        elif allocations or task["primary_assignee"]:
            errors.append(f"{tid}: later task must remain unassigned")

        if task["manual_testing_only"]:
            if (
                task["start_date"] != "2026-07-29"
                or task["target_date"] != "2026-07-29"
            ):
                errors.append(f"{tid}: final QA date must be 2026-07-29")
            if task["dependencies"] != ["MP-024"]:
                errors.append(
                    f"{tid}: final QA must depend only on release-candidate freeze MP-024"
                )

    # Explicit cycle check, even though ordered dependencies should already prevent cycles.
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(node: str) -> None:
        if node in visited:
            return
        if node in visiting:
            errors.append(f"Dependency cycle detected at {node}")
            return
        visiting.add(node)
        for dep in graph.get(node, []):
            if dep in graph:
                visit(dep)
        visiting.remove(node)
        visited.add(node)

    for tid in graph:
        visit(tid)

    qa = [t for t in tasks if t["manual_testing_only"]]
    dev = [
        t
        for t in tasks
        if t["sprint_designation"] == "sprint-1" and not t["manual_testing_only"]
    ]
    later = [t for t in tasks if t["sprint_designation"] != "sprint-1"]
    if len(qa) != 6:
        errors.append(f"Expected 6 final-day QA tasks, found {len(qa)}")
    if len(dev) != 27:
        errors.append(f"Expected 27 Sprint development tasks, found {len(dev)}")
    if len(later) != 30:
        errors.append(f"Expected 30 later tasks, found {len(later)}")

    loads: defaultdict[str, float] = defaultdict(float)
    for task in dev:
        for user, hours in task["effort_allocation_hours"].items():
            loads[user] += float(hours)
    if set(loads) != TEAM_B:
        errors.append("All six Team B members need Sprint allocations")
    elif max(loads.values()) - min(loads.values()) > 4:
        errors.append(
            f"Workload spread too large: {max(loads.values()) - min(loads.values()):.1f} h"
        )

    planned = sum(float(t["estimated_focused_work_hours"]) for t in dev)
    theoretical = 252.0
    ratio = planned / theoretical
    if not 0.65 <= ratio <= 0.75:
        errors.append(f"Planned ratio {ratio:.1%} is outside 65–75%")

    # Enhancement invariants.
    if ids.get("MP-014", {}).get("workstream") != "Integration":
        errors.append("MP-014 must be the early integration vertical slice")
    if "MP-014" not in ids.get("MP-019", {}).get("dependencies", []):
        errors.append("MP-019 must depend on MP-014")
    if (
        ids.get("MP-034", {}).get("title")
        != "Cross-browser compatibility baseline and support matrix"
    ):
        errors.append("MP-034 must remain the later cross-browser task")
    for tid in ("MP-001", "MP-002", "MP-003"):
        if "Do not repeat documentation" not in ids[tid]["issue_body"]:
            errors.append(f"{tid}: must direct students from reading to practical work")

    print(
        f"Validated {len(tasks)} tasks: {len(dev)} Sprint 1 development, "
        f"{len(qa)} final-day QA, {len(later)} later backlog."
    )
    print(
        f"Team B planned focused work: {planned:.1f}/{theoretical:.1f} hours ({ratio:.1%})."
    )
    for user in sorted(TEAM_B):
        print(f"  {user}: {loads[user]:.1f} h")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("Enhanced backlog validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
