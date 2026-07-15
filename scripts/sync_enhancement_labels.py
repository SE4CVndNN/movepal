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


def run(args, input_data=None):
    return subprocess.run(
        ["gh", *args],
        input=json.dumps(input_data) if input_data is not None else None,
        text=True,
        capture_output=True,
    )


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--metadata", type=Path, required=True)
    p.add_argument("--repository", default="SE4CVndNN/movepal")
    p.add_argument("--apply", action="store_true")
    a = p.parse_args()
    data = json.loads(a.metadata.read_text(encoding="utf-8"))
    selected = [x for x in data["labels"] if x["name"] in NEW_LABELS]
    failed = 0
    for label in selected:
        ep = f"repos/{a.repository}/labels/{quote(label['name'], safe='')}"
        cur = run(["api", ep, "-H", f"X-GitHub-Api-Version: {API_VERSION}"])
        if cur.returncode != 0:
            action = "Create"
            args = [
                "api",
                "-X",
                "POST",
                f"repos/{a.repository}/labels",
                "-H",
                f"X-GitHub-Api-Version: {API_VERSION}",
                "--input",
                "-",
            ]
            payload = label
        else:
            obj = json.loads(cur.stdout)
            changed = (
                obj.get("color", "").lower() != label["color"].lower()
                or (obj.get("description") or "") != label["description"]
            )
            if not changed:
                print(f"[INFO] Label unchanged: {label['name']}")
                continue
            action = "Update"
            args = [
                "api",
                "-X",
                "PATCH",
                ep,
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
        if not a.apply:
            print(f"[DRY-RUN] {action} label {label['name']}")
            continue
        print(f"[APPLY] {action} label {label['name']}")
        r = run(args, payload)
        if r.returncode != 0:
            print(f"[ERROR] {label['name']}: {r.stderr.strip() or r.stdout.strip()}")
            failed += 1
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
