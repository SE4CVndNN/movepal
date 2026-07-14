#!/usr/bin/env python3
"""Back up current MovePal issue and Project state before applying planning updates."""

from __future__ import annotations

import argparse
import json
import subprocess
from datetime import datetime
from pathlib import Path
from typing import Any


def run_gh(args: list[str]) -> Any:
    result = subprocess.run(["gh", *args], text=True, capture_output=True)
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or result.stdout.strip())
    return json.loads(result.stdout) if result.stdout.strip() else None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repository", default="SE4CVndNN/movepal")
    parser.add_argument("--organization", default="SE4CVndNN")
    parser.add_argument("--project-number", default="1")
    parser.add_argument("--output-dir", type=Path, default=Path("bootstrap_reports"))
    args = parser.parse_args()

    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    destination = args.output_dir / f"planning_enhancement_github_backup_{stamp}.json"
    destination.parent.mkdir(parents=True, exist_ok=True)

    issues = run_gh(
        [
            "issue",
            "list",
            "--repo",
            args.repository,
            "--state",
            "all",
            "--limit",
            "1000",
            "--json",
            "number,title,body,state,url,labels,assignees,milestone",
        ]
    )
    project = run_gh(
        [
            "project",
            "view",
            str(args.project_number),
            "--owner",
            args.organization,
            "--format",
            "json",
        ]
    )
    project_items = run_gh(
        [
            "project",
            "item-list",
            str(args.project_number),
            "--owner",
            args.organization,
            "--limit",
            "1000",
            "--format",
            "json",
        ]
    )
    labels = run_gh(
        [
            "label",
            "list",
            "--repo",
            args.repository,
            "--limit",
            "200",
            "--json",
            "name,color,description",
        ]
    )

    payload = {
        "created_at_local": datetime.now().isoformat(timespec="seconds"),
        "repository": args.repository,
        "project": project,
        "issues": issues,
        "project_items": project_items,
        "labels": labels,
    }
    destination.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(f"GitHub state backup: {destination}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
