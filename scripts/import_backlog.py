#!/usr/bin/env python3
"""Idempotently create/update MovePal issues and add them to the org Project.

Dry-run is the default. Existing issues are identified only by the stable marker
`<!-- task-id: MP-NNN -->`, not by title. Student email addresses are never read
or printed by this script.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
from pathlib import Path
from typing import Any

API_VERSION = "2022-11-28"


def run(
    args: list[str], *, check: bool = True, json_input: dict[str, Any] | None = None
) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["gh", *args],
        input=json.dumps(json_input) if json_input is not None else None,
        text=True,
        capture_output=True,
        check=check,
    )


def gh_json(args: list[str], *, default: Any = None) -> Any:
    result = run_retry(args)
    if result.returncode != 0:
        if default is not None:
            return default
        raise RuntimeError(result.stderr.strip() or result.stdout.strip())
    return json.loads(result.stdout) if result.stdout.strip() else default


def records(raw: Any, *keys: str) -> list[dict[str, Any]]:
    if isinstance(raw, list):
        return raw
    if isinstance(raw, dict):
        for key in keys:
            value = raw.get(key)
            if isinstance(value, list):
                return value
    return []


def active_member(org: str, username: str, cache: dict[str, bool]) -> bool:
    if username in cache:
        return cache[username]
    result = run(
        [
            "api",
            f"orgs/{org}/memberships/{username}",
            "-H",
            f"X-GitHub-Api-Version: {API_VERSION}",
        ],
        check=False,
    )
    if result.returncode != 0:
        cache[username] = False
    else:
        try:
            cache[username] = json.loads(result.stdout).get("state") == "active"
        except json.JSONDecodeError:
            cache[username] = False
    return cache[username]


def find_project(org: str, title: str) -> dict[str, Any] | None:
    raw = gh_json(
        ["project", "list", "--owner", org, "--limit", "100", "--format", "json"],
        default={},
    )
    return next(
        (p for p in records(raw, "projects", "items") if p.get("title") == title), None
    )


def project_context(
    org: str, number: int
) -> tuple[str, dict[str, dict[str, Any]], dict[int, str]]:
    project = gh_json(
        ["project", "view", str(number), "--owner", org, "--format", "json"]
    )
    project_id = project["id"]
    raw_fields = gh_json(
        [
            "project",
            "field-list",
            str(number),
            "--owner",
            org,
            "--limit",
            "100",
            "--format",
            "json",
        ],
        default={},
    )
    fields = {f.get("name"): f for f in records(raw_fields, "fields", "items")}
    raw_items = gh_json(
        [
            "project",
            "item-list",
            str(number),
            "--owner",
            org,
            "--limit",
            "1000",
            "--format",
            "json",
        ],
        default={},
    )
    item_by_issue: dict[int, str] = {}
    for item in records(raw_items, "items"):
        content = item.get("content") or {}
        if (
            isinstance(content, dict)
            and isinstance(content.get("number"), int)
            and item.get("id")
        ):
            item_by_issue[content["number"]] = item["id"]
    return project_id, fields, item_by_issue


def run_retry(
    args: list[str], *, attempts: int = 3, delay_seconds: float = 2.0
) -> subprocess.CompletedProcess[str]:
    """Run an idempotent gh edit command with limited retries for transient network failures."""
    result: subprocess.CompletedProcess[str] | None = None
    for attempt in range(1, attempts + 1):
        result = run(args, check=False)
        if result.returncode == 0:
            return result
        if attempt < attempts:
            time.sleep(delay_seconds * attempt)
    assert result is not None
    return result


def set_project_value(
    org: str,
    project_id: str,
    item_id: str,
    field: dict[str, Any],
    value: Any,
    apply: bool,
    expected_data_type: str | None = None,
) -> bool:
    if value in (None, ""):
        return True
    field_name = field.get("name", "<unknown>")
    args = [
        "project",
        "item-edit",
        "--id",
        item_id,
        "--project-id",
        project_id,
        "--field-id",
        field["id"],
    ]
    # `gh project field-list --format json` may expose only the GraphQL object
    # type (for example, ProjectV2Field), not the underlying NUMBER/DATE/TEXT
    # data type. Prefer the authoritative metadata configuration when present.
    data_type = (
        expected_data_type or field.get("dataType") or field.get("type") or ""
    ).upper()
    if data_type in {"SINGLE_SELECT", "SINGLESELECT"} or field.get("options"):
        option = next(
            (o for o in field.get("options", []) if o.get("name") == str(value)), None
        )
        if not option:
            print(f"[WARN] Project field '{field_name}' has no option '{value}'.")
            return False
        args += ["--single-select-option-id", option["id"]]
    elif data_type == "NUMBER":
        args += ["--number", str(value)]
    elif data_type == "DATE":
        args += ["--date", str(value)]
    else:
        args += ["--text", str(value)]
    if not apply:
        print(f"[DRY-RUN] Set Project field {field_name}={value}")
        return True
    result = run_retry(args)
    if result.returncode != 0:
        print(
            f"[WARN] Could not set Project field {field_name}: {result.stderr.strip() or result.stdout.strip()}"
        )
        return False
    return True


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--organization", default="SE4CVndNN")
    parser.add_argument("--repository", default="movepal")
    parser.add_argument("--project-title", default="MovePal — Product and Sprint Board")
    parser.add_argument(
        "--backlog", type=Path, default=Path("backlog/product_backlog.json")
    )
    parser.add_argument(
        "--metadata", type=Path, default=Path("config/project_metadata.json")
    )
    parser.add_argument(
        "--source", choices=["all", "sprint-1", "qa", "later"], default="all"
    )
    parser.add_argument("--task-id-start")
    parser.add_argument("--task-id-end")
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--update-existing", action="store_true")
    parser.add_argument("--no-assign", action="store_true")
    parser.add_argument("--no-project", action="store_true")
    parser.add_argument(
        "--report",
        type=Path,
        default=Path("bootstrap_reports/backlog_import_summary.json"),
    )
    args = parser.parse_args()

    data = json.loads(args.backlog.read_text(encoding="utf-8"))
    metadata = json.loads(args.metadata.read_text(encoding="utf-8"))
    field_data_types = {
        item["name"]: str(item["data_type"]).upper()
        for item in metadata.get("project_fields", [])
        if item.get("name") and item.get("data_type")
    }
    tasks: list[dict[str, Any]] = data["tasks"]
    if args.source == "sprint-1":
        tasks = [t for t in tasks if t["sprint_designation"] == "sprint-1"]
    elif args.source == "qa":
        tasks = [t for t in tasks if t["manual_testing_only"]]
    elif args.source == "later":
        tasks = [t for t in tasks if t["sprint_designation"] != "sprint-1"]
    if args.task_id_start:
        tasks = [t for t in tasks if t["task_id"] >= args.task_id_start]
    if args.task_id_end:
        tasks = [t for t in tasks if t["task_id"] <= args.task_id_end]

    repo = f"{args.organization}/{args.repository}"
    existing_raw = gh_json(
        [
            "issue",
            "list",
            "--repo",
            repo,
            "--state",
            "all",
            "--limit",
            "1000",
            "--json",
            "number,title,body,url",
        ],
        default=[],
    )
    existing: dict[str, dict[str, Any]] = {}
    for issue in existing_raw or []:
        body = issue.get("body") or ""
        for task in tasks:
            if f"<!-- task-id: {task['task_id']} -->" in body:
                existing[task["task_id"]] = issue
                break

    milestones_raw = gh_json(
        [
            "api",
            f"repos/{repo}/milestones?state=all&per_page=100",
            "-H",
            f"X-GitHub-Api-Version: {API_VERSION}",
        ],
        default=[],
    )
    milestones = {m["title"]: m["number"] for m in milestones_raw or []}
    member_cache: dict[str, bool] = {}

    project = (
        None if args.no_project else find_project(args.organization, args.project_title)
    )
    project_number = (
        int(project["number"])
        if project and project.get("number") is not None
        else None
    )
    project_id: str | None = None
    fields: dict[str, dict[str, Any]] = {}
    item_by_issue: dict[int, str] = {}
    if project_number is not None:
        project_id, fields, item_by_issue = project_context(
            args.organization, project_number
        )
    elif not args.no_project:
        print(
            f"[WARN] Organization Project '{args.project_title}' does not exist yet; Project item operations will be skipped in this run."
        )

    summary: dict[str, Any] = {
        "mode": "apply" if args.apply else "dry-run",
        "source": args.source,
        "selected": len(tasks),
        "created": 0,
        "updated": 0,
        "skipped": 0,
        "failed": 0,
        "assignment_warnings": [],
        "project_field_warnings": 0,
        "issue_type_warnings": 0,
        "tasks": [],
    }

    for task in tasks:
        tid = task["task_id"]
        title = f"{tid} — {task['title']}"
        desired_users = (
            [] if args.no_assign else list(task["effort_allocation_hours"].keys())
        )
        assignable: list[str] = []
        for username in desired_users:
            if active_member(args.organization, username, member_cache):
                assignable.append(username)
            else:
                message = f"{tid}: @{username} is not an active organization member; issue will be left without that assignment."
                print(f"[WARN] {message}")
                summary["assignment_warnings"].append(message)

        milestone_number = milestones.get(task["milestone"])
        if milestone_number is None:
            print(f"[WARN] {tid}: milestone '{task['milestone']}' not found.")

        payload: dict[str, Any] = {
            "title": title,
            "body": task["issue_body"],
            "labels": task["github_labels"],
            "assignees": assignable,
        }
        if milestone_number is not None:
            payload["milestone"] = milestone_number

        issue = existing.get(tid)
        action = "skipped"
        try:
            if issue is None:
                if not args.apply:
                    print(
                        f"[DRY-RUN] Create {title}; assignees={assignable or ['unassigned']}"
                    )
                    issue = {"number": -1, "url": None}
                else:
                    result = run(
                        [
                            "api",
                            "-X",
                            "POST",
                            f"repos/{repo}/issues",
                            "-H",
                            f"X-GitHub-Api-Version: {API_VERSION}",
                            "--input",
                            "-",
                        ],
                        check=False,
                        json_input=payload,
                    )
                    if result.returncode != 0:
                        raise RuntimeError(
                            result.stderr.strip() or result.stdout.strip()
                        )
                    created = json.loads(result.stdout)
                    issue = {"number": created["number"], "url": created["html_url"]}
                summary["created"] += 1
                action = "created"
            elif args.update_existing:
                if not args.apply:
                    print(f"[DRY-RUN] Update existing #{issue['number']} for {tid}")
                else:
                    result = run(
                        [
                            "api",
                            "-X",
                            "PATCH",
                            f"repos/{repo}/issues/{issue['number']}",
                            "-H",
                            f"X-GitHub-Api-Version: {API_VERSION}",
                            "--input",
                            "-",
                        ],
                        check=False,
                        json_input=payload,
                    )
                    if result.returncode != 0:
                        raise RuntimeError(
                            result.stderr.strip() or result.stdout.strip()
                        )
                    updated = json.loads(result.stdout)
                    issue["url"] = updated["html_url"]
                summary["updated"] += 1
                action = "updated"
            else:
                print(
                    f"[INFO] Skip existing #{issue['number']} for {tid}; use --update-existing to reconcile it."
                )
                summary["skipped"] += 1

            issue_type = (
                "Feature"
                if "type:feature" in task["github_labels"]
                else ("Bug" if "type:bug" in task["github_labels"] else "Task")
            )
            if int(issue["number"]) < 0:
                print(f"[DRY-RUN] Set issue type for {tid} to {issue_type}")
            elif args.apply:
                type_result = run_retry(
                    [
                        "issue",
                        "edit",
                        str(issue["number"]),
                        "--repo",
                        repo,
                        "--type",
                        issue_type,
                    ]
                )
                if type_result.returncode != 0:
                    print(
                        f"[WARN] Could not set issue type {issue_type} for {tid}: {type_result.stderr.strip() or type_result.stdout.strip()}"
                    )
                    summary["issue_type_warnings"] += 1

            if not args.no_project and project_number is not None:
                issue_number = int(issue["number"])
                item_id = item_by_issue.get(issue_number) if issue_number >= 0 else None
                if item_id is None and issue.get("url"):
                    if not args.apply:
                        print(f"[DRY-RUN] Add {tid} to Project #{project_number}")
                    else:
                        added = gh_json(
                            [
                                "project",
                                "item-add",
                                str(project_number),
                                "--owner",
                                args.organization,
                                "--url",
                                issue["url"],
                                "--format",
                                "json",
                            ]
                        )
                        item_id = added.get("id")
                        if item_id:
                            item_by_issue[issue_number] = item_id
                if item_id and project_id:
                    sprint_value = {
                        "sprint-1": "Sprint 1",
                        "post-sprint": "Post-Sprint",
                        "future": "Future",
                        "optional": "Optional",
                    }[task["sprint_designation"]]
                    values = {
                        "Workflow Stage": task["project_status"],
                        "Sprint": sprint_value,
                        "Priority": task["priority"],
                        "Estimate Hours": task["estimated_focused_work_hours"],
                        "Position": task["position"],
                        "Workstream": task["workstream"],
                        "Team": task["team"],
                        "Task ID": task["task_id"],
                        "Dependency": ", ".join(task["dependencies"]),
                        "Start Date": task["start_date"],
                        "Target Date": task["target_date"],
                    }
                    for field_name, value in values.items():
                        field = fields.get(field_name)
                        if not field:
                            print(f"[WARN] Missing Project field: {field_name}")
                            summary["project_field_warnings"] += 1
                            continue
                        if not set_project_value(
                            args.organization,
                            project_id,
                            item_id,
                            field,
                            value,
                            args.apply,
                            field_data_types.get(field_name),
                        ):
                            summary["project_field_warnings"] += 1
                elif not args.apply and issue_number < 0:
                    print(
                        f"[DRY-RUN] Set all configured Project fields for {tid} after issue creation."
                    )

            summary["tasks"].append(
                {"task_id": tid, "action": action, "issue_number": issue.get("number")}
            )
        except (
            RuntimeError,
            subprocess.CalledProcessError,
            json.JSONDecodeError,
        ) as exc:
            summary["failed"] += 1
            summary["tasks"].append(
                {"task_id": tid, "action": "failed", "error": str(exc)}
            )
            print(f"[ERROR] {tid}: {exc}", file=sys.stderr)

    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(
        json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print("\nBacklog import summary")
    for key in (
        "selected",
        "created",
        "updated",
        "skipped",
        "failed",
        "project_field_warnings",
        "issue_type_warnings",
    ):
        print(f"- {key}: {summary[key]}")
    print(f"- assignment warnings: {len(summary['assignment_warnings'])}")
    print(f"- report: {args.report}")
    return 1 if summary["failed"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
