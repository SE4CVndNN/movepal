#!/usr/bin/env python3
"""Create/update MovePal labels, milestones, Project, fields, and repository link.

Dry-run is the default. This script uses the authenticated GitHub CLI session and
never reads or prints the token.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any
from urllib.parse import quote

API_VERSION = "2022-11-28"


def run(args: list[str], *, check: bool = True, json_input: dict[str, Any] | None = None) -> subprocess.CompletedProcess[str]:
    cmd = ["gh", *args]
    return subprocess.run(
        cmd,
        input=json.dumps(json_input) if json_input is not None else None,
        text=True,
        capture_output=True,
        check=check,
    )


_MISSING = object()

def gh_json(args: list[str], *, default: Any = _MISSING) -> Any:
    result = run(args, check=False)
    if result.returncode != 0:
        if default is not _MISSING:
            return default
        raise RuntimeError(result.stderr.strip() or result.stdout.strip())
    text = result.stdout.strip()
    if text:
        return json.loads(text)
    return None if default is _MISSING else default


def mutate(apply: bool, description: str, args: list[str], json_input: dict[str, Any] | None = None) -> None:
    if not apply:
        print(f"[DRY-RUN] {description}")
        return
    print(f"[APPLY] {description}")
    result = run(args, check=False, json_input=json_input)
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or result.stdout.strip())


def project_records(raw: Any) -> list[dict[str, Any]]:
    if isinstance(raw, list):
        return raw
    if isinstance(raw, dict):
        return raw.get("projects", raw.get("items", []))
    return []


def field_records(raw: Any) -> list[dict[str, Any]]:
    if isinstance(raw, list):
        return raw
    if isinstance(raw, dict):
        return raw.get("fields", raw.get("items", []))
    return []


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--organization", required=True)
    parser.add_argument("--repository", required=True)
    parser.add_argument("--project-title", required=True)
    parser.add_argument("--metadata", type=Path, required=True)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    metadata = json.loads(args.metadata.read_text(encoding="utf-8"))
    repo = f"{args.organization}/{args.repository}"
    counts = {"labels_created": 0, "labels_updated": 0, "labels_unchanged": 0,
              "milestones_created": 0, "milestones_updated": 0, "milestones_unchanged": 0,
              "fields_created": 0, "fields_existing": 0}

    # Labels: create or reconcile color/description.
    for label in metadata["labels"]:
        endpoint = f"repos/{repo}/labels/{quote(label['name'], safe='')}"
        existing = gh_json(["api", endpoint, "-H", f"X-GitHub-Api-Version: {API_VERSION}"], default=None)
        if existing is None:
            mutate(args.apply, f"Create label {label['name']}", [
                "api", "-X", "POST", f"repos/{repo}/labels",
                "-H", f"X-GitHub-Api-Version: {API_VERSION}",
                "--input", "-",
            ], {"name": label["name"], "color": label["color"], "description": label["description"]})
            counts["labels_created"] += 1
        elif existing.get("color", "").lower() != label["color"].lower() or (existing.get("description") or "") != label["description"]:
            mutate(args.apply, f"Update label {label['name']}", [
                "api", "-X", "PATCH", endpoint,
                "-H", f"X-GitHub-Api-Version: {API_VERSION}",
                "--input", "-",
            ], {"new_name": label["name"], "color": label["color"], "description": label["description"]})
            counts["labels_updated"] += 1
        else:
            counts["labels_unchanged"] += 1

    # Milestones.
    milestones = gh_json(["api", f"repos/{repo}/milestones?state=all&per_page=100", "-H", f"X-GitHub-Api-Version: {API_VERSION}"], default=[])
    by_title = {m["title"]: m for m in milestones or []}
    for desired in metadata["milestones"]:
        current = by_title.get(desired["title"])
        payload = {"title": desired["title"], "description": desired["description"], "state": "open"}
        if desired.get("due_on"):
            payload["due_on"] = desired["due_on"]
        if current is None:
            mutate(args.apply, f"Create milestone {desired['title']}", [
                "api", "-X", "POST", f"repos/{repo}/milestones",
                "-H", f"X-GitHub-Api-Version: {API_VERSION}", "--input", "-",
            ], payload)
            counts["milestones_created"] += 1
        else:
            current_due = current.get("due_on")
            desired_due = desired.get("due_on")
            changed = (current.get("description") or "") != desired["description"] or bool(current_due) != bool(desired_due)
            if desired_due and current_due and current_due[:10] != desired_due[:10]:
                changed = True
            if changed:
                mutate(args.apply, f"Update milestone {desired['title']}", [
                    "api", "-X", "PATCH", f"repos/{repo}/milestones/{current['number']}",
                    "-H", f"X-GitHub-Api-Version: {API_VERSION}", "--input", "-",
                ], payload)
                counts["milestones_updated"] += 1
            else:
                counts["milestones_unchanged"] += 1

    # Project creation/reuse.
    raw_projects = gh_json(["project", "list", "--owner", args.organization, "--limit", "100", "--format", "json"], default={})
    projects = project_records(raw_projects)
    project = next((p for p in projects if p.get("title") == args.project_title), None)
    project_number: int | None = int(project["number"]) if project and project.get("number") is not None else None
    if project_number is None:
        if not args.apply:
            print(f"[DRY-RUN] Create organization Project: {args.project_title}")
            print("[DRY-RUN] Project fields and repository link will be created after the Project exists.")
        else:
            print(f"[APPLY] Create organization Project: {args.project_title}")
            created = gh_json(["project", "create", "--owner", args.organization, "--title", args.project_title, "--format", "json"])
            project_number = int(created["number"])
    else:
        print(f"[INFO] Reusing Project #{project_number}: {args.project_title}")

    if project_number is not None:
        mutate(args.apply, f"Link {repo} to Project #{project_number}", [
            "project", "link", str(project_number), "--owner", args.organization, "--repo", repo,
        ])
        fields_raw = gh_json(["project", "field-list", str(project_number), "--owner", args.organization, "--limit", "100", "--format", "json"], default={})
        existing_fields = {f.get("name"): f for f in field_records(fields_raw)}
        for field in metadata["project_fields"]:
            if field["name"] in existing_fields:
                counts["fields_existing"] += 1
                existing = existing_fields[field["name"]]
                desired_options = field.get("options", [])
                current_options = [o.get("name") for o in existing.get("options", []) if isinstance(o, dict)]
                if desired_options and current_options and current_options != desired_options:
                    print(f"[WARN] Existing field '{field['name']}' options differ. Review manually; this script will not delete/recreate fields.")
                continue
            create_args = ["project", "field-create", str(project_number), "--owner", args.organization,
                           "--name", field["name"], "--data-type", field["data_type"]]
            if field.get("options"):
                create_args += ["--single-select-options", ",".join(field["options"])]
            mutate(args.apply, f"Create Project field {field['name']}", create_args)
            counts["fields_created"] += 1

    mode = "APPLY" if args.apply else "DRY-RUN"
    print(f"\nPreparation summary ({mode})")
    for key, value in counts.items():
        print(f"- {key.replace('_', ' ')}: {value}")
    if project_number is not None:
        print(f"- project number: {project_number}")
    print("- Project views remain a deliberate manual step; see docs/project_board_views.md.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (RuntimeError, subprocess.CalledProcessError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
