#!/usr/bin/env python3
"""Create or update only labels required by the enhancement. Dry-run by default."""

from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path
from urllib.parse import quote

API_VERSION = "2022-11-28"
NEW_LABELS = {
    "type:integration",
    "type:data",
    "area:integration",
    "status:ready-for-integration",
    "status:needs-retest",
    "backlog:post-sprint",
    "backlog:optional",
}


def run(
    args: list[str], input_data: dict[str, str] | None = None
) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["gh", *args],
        input=json.dumps(input_data) if input_data is not None else None,
        text=True,
        capture_output=True,
        check=False,
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--metadata", type=Path, required=True)
    parser.add_argument("--repository", default="SE4CVndNN/movepal")
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    data = json.loads(args.metadata.read_text(encoding="utf-8"))
    selected = [label for label in data["labels"] if label["name"] in NEW_LABELS]
    failed = 0

    for label in selected:
        endpoint = f"repos/{args.repository}/labels/{quote(label['name'], safe='')}"
        current = run(["api", endpoint, "-H", f"X-GitHub-Api-Version: {API_VERSION}"])

        if current.returncode != 0:
            action = "Create"
            command = [
                "api",
                "-X",
                "POST",
                f"repos/{args.repository}/labels",
                "-H",
                f"X-GitHub-Api-Version: {API_VERSION}",
                "--input",
                "-",
            ]
            payload = label
        else:
            existing = json.loads(current.stdout)
            changed = (
                existing.get("color", "").lower() != label["color"].lower()
                or (existing.get("description") or "") != label["description"]
            )
            if not changed:
                print(f"[INFO] Label unchanged: {label['name']}")
                continue
            action = "Update"
            command = [
                "api",
                "-X",
                "PATCH",
                endpoint,
                "-H",
                f"X-GitHub-Api-Version: {API_VERSION}",
                "--input",
                "-",
            ]
            payload = {
                "new_name": label["name"],
                "color": label["color"],
                "description": label["description"],
            }

        if not args.apply:
            print(f"[DRY-RUN] {action} label {label['name']}")
            continue

        print(f"[APPLY] {action} label {label['name']}")
        result = run(command, payload)
        if result.returncode != 0:
            message = result.stderr.strip() or result.stdout.strip()
            print(f"[ERROR] {label['name']}: {message}")
            failed += 1

    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
