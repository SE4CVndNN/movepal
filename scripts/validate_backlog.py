#!/usr/bin/env python3
"""Validate MovePal backlog structure, dependencies, assignments, and capacity."""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any

TASK_ID = re.compile(r"^MP-(\d{3})$")
SPRINT_VALUES = {"sprint-1", "post-sprint", "future", "optional"}
TEAM_B = {"alaamadii", "IslamOuda85", "AhmadKollab", "myarnwas", "JHT127", "MennaAllah-Alatrsh"}
TEAM_A = {"Tojan-Naiem", "SajaZenaty", "nezarYousef", "saliqasarwi", "SaadRayh", "BaraahMazeen"}
REQUIRED = {
    "task_id", "position", "title", "value", "description", "beginner_learning_objective",
    "deliverables", "acceptance_criteria", "definition_of_done", "dependencies",
    "blocking_status", "workstream", "suggested_scrum_role", "team", "primary_assignee",
    "suggested_reviewer", "estimated_focused_work_hours", "investigation_buffer_hours",
    "review_buffer_hours", "qa_buffer_hours", "effort_allocation_hours", "priority",
    "sprint_designation", "github_labels", "milestone", "project_status", "risks",
    "helpful_references", "pull_request_required", "suggested_branch_name",
    "suggested_test_requirements", "security_privacy_considerations", "demo_evidence_required",
    "start_date", "target_date", "manual_testing_only", "issue_body",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--backlog", type=Path, default=Path("backlog/product_backlog.json"))
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    data: dict[str, Any] = json.loads(args.backlog.read_text(encoding="utf-8"))
    tasks: list[dict[str, Any]] = data.get("tasks", [])
    errors: list[str] = []
    warnings: list[str] = []

    if len(tasks) != 63:
        errors.append(f"Expected 63 tasks, found {len(tasks)}.")

    ids: dict[str, dict[str, Any]] = {}
    positions: set[int] = set()
    for task in tasks:
        missing = REQUIRED - task.keys()
        if missing:
            errors.append(f"{task.get('task_id', '<unknown>')}: missing fields {sorted(missing)}")
            continue
        tid = task["task_id"]
        match = TASK_ID.fullmatch(tid)
        if not match:
            errors.append(f"Invalid task ID: {tid}")
        elif int(match.group(1)) != task["position"]:
            errors.append(f"{tid}: position must equal numeric ID, found {task['position']}.")
        if tid in ids:
            errors.append(f"Duplicate task ID: {tid}")
        ids[tid] = task
        if task["position"] in positions:
            errors.append(f"Duplicate position: {task['position']}")
        positions.add(task["position"])
        if task["sprint_designation"] not in SPRINT_VALUES:
            errors.append(f"{tid}: invalid sprint designation {task['sprint_designation']}")
        if float(task["estimated_focused_work_hours"]) <= 0:
            errors.append(f"{tid}: estimate must be positive.")
        if len(task["description"]) < 500 or len(task["issue_body"]) < 1500:
            errors.append(f"{tid}: description/issue body is not sufficiently detailed.")
        if not task["acceptance_criteria"] or not task["deliverables"] or not task["definition_of_done"]:
            errors.append(f"{tid}: deliverables, acceptance criteria, and DoD must be non-empty.")
        marker = f"<!-- task-id: {tid} -->"
        if marker not in task["issue_body"]:
            errors.append(f"{tid}: stable marker missing from issue body.")

    for task in tasks:
        tid = task["task_id"]
        for dep in task["dependencies"]:
            if dep not in ids:
                errors.append(f"{tid}: unknown dependency {dep}")
            elif ids[dep]["position"] >= task["position"]:
                errors.append(f"{tid}: dependency {dep} is not earlier in dependency order.")
        allocations = {u: float(h) for u, h in task["effort_allocation_hours"].items()}
        if task["sprint_designation"] == "sprint-1":
            if not task["primary_assignee"]:
                errors.append(f"{tid}: Sprint 1 task has no primary assignee.")
            if abs(sum(allocations.values()) - float(task["estimated_focused_work_hours"])) > 0.01:
                errors.append(f"{tid}: effort allocations do not sum to estimate.")
            expected_team = TEAM_A if task["manual_testing_only"] else TEAM_B
            invalid = set(allocations) - expected_team
            if invalid:
                errors.append(f"{tid}: unexpected assignees for team: {sorted(invalid)}")
            if task["primary_assignee"] not in expected_team:
                errors.append(f"{tid}: primary assignee is not in expected team.")
            if task["suggested_reviewer"] in allocations:
                errors.append(f"{tid}: reviewer is also an author/contributor allocation.")
        elif allocations:
            errors.append(f"{tid}: future task should remain unassigned at bootstrap.")

        if task["manual_testing_only"]:
            if task["start_date"] != "2026-07-29" or task["target_date"] != "2026-07-29":
                errors.append(f"{tid}: manual QA must be scheduled only on 2026-07-29.")
            if task["pull_request_required"]:
                errors.append(f"{tid}: manual QA issue should not require a feature PR.")
            if task["dependencies"] != ["MP-024"]:
                errors.append(f"{tid}: final-day QA must depend only on MP-024 release candidate.")

    qa = [t for t in tasks if t["manual_testing_only"]]
    sprint_dev = [t for t in tasks if t["sprint_designation"] == "sprint-1" and not t["manual_testing_only"]]
    if len(qa) != 6:
        errors.append(f"Expected six manual QA tasks, found {len(qa)}.")
    if len(sprint_dev) != 27:
        errors.append(f"Expected 27 Sprint 1 development tasks, found {len(sprint_dev)}.")

    loads: defaultdict[str, float] = defaultdict(float)
    for task in sprint_dev:
        for user, hours in task["effort_allocation_hours"].items():
            loads[user] += float(hours)
    if set(loads) != TEAM_B:
        errors.append("All six Team B members must have Sprint 1 development allocations.")
    elif max(loads.values()) - min(loads.values()) > 4:
        errors.append(f"Team B workload spread is too large: {max(loads.values())-min(loads.values()):.1f} hours.")
    planned = sum(float(t["estimated_focused_work_hours"]) for t in sprint_dev)
    theoretical = 6 * 12 * 3.5
    ratio = planned / theoretical
    if not 0.65 <= ratio <= 0.75:
        errors.append(f"Planned development ratio {ratio:.1%} is outside 65–75%.")

    print(f"Validated {len(tasks)} tasks: {len(sprint_dev)} Sprint 1 development, {len(qa)} final-day QA, {len(tasks)-len(sprint_dev)-len(qa)} later backlog.")
    print(f"Team B planned focused work: {planned:.1f}/{theoretical:.1f} hours ({ratio:.1%}).")
    for user in sorted(TEAM_B):
        print(f"  {user}: {loads[user]:.1f} h")
    if warnings:
        for warning in warnings:
            print(f"WARNING: {warning}", file=sys.stderr)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("Backlog validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
