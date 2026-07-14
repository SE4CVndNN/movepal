"""Validate MovePal and AidSign student team CSV files without exposing emails."""

from __future__ import annotations

import argparse
import csv
import re
import sys
from dataclasses import dataclass
from pathlib import Path

REQUIRED_COLUMNS = {
    "member_id",
    "full_name",
    "github_username",
    "email",
    "scrum_role",
    "preferred_workstream",
    "daily_capacity_hours",
}
ALLOWED_ROLES = {"product_owner", "scrum_master", "developer"}
ALLOWED_WORKSTREAMS = {
    "product_documentation",
    "devops_testing",
    "backend",
    "computer_vision",
    "frontend_ux",
    "data_evaluation",
}
USERNAME_PATTERN = re.compile(r"^[A-Za-z0-9](?:[A-Za-z0-9-]{0,37}[A-Za-z0-9])?$")


@dataclass(frozen=True)
class Member:
    member_id: str
    github_username: str
    scrum_role: str
    preferred_workstream: str
    daily_capacity_hours: float


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--team-a", type=Path, required=True)
    parser.add_argument("--team-b", type=Path, required=True)
    return parser.parse_args()


def load_team(path: Path, expected_prefix: str) -> tuple[list[Member], list[str]]:
    errors: list[str] = []
    members: list[Member] = []

    if not path.is_file():
        return [], [f"Missing team file: {path}"]

    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        columns = set(reader.fieldnames or [])
        missing = REQUIRED_COLUMNS - columns
        if missing:
            return [], [f"{path}: missing columns: {', '.join(sorted(missing))}"]

        for line_number, row in enumerate(reader, start=2):
            member_id = row["member_id"].strip()
            username = row["github_username"].strip()
            role = row["scrum_role"].strip()
            workstream = row["preferred_workstream"].strip()

            if not member_id.startswith(expected_prefix):
                errors.append(
                    f"{path}:{line_number}: member_id must start with {expected_prefix}."
                )
            if not username:
                errors.append(f"{path}:{line_number}: github_username is required.")
            elif not USERNAME_PATTERN.fullmatch(username):
                errors.append(
                    f"{path}:{line_number}: invalid GitHub username format: {username}"
                )
            if role not in ALLOWED_ROLES:
                errors.append(f"{path}:{line_number}: unsupported Scrum role: {role}")
            if workstream not in ALLOWED_WORKSTREAMS:
                errors.append(
                    f"{path}:{line_number}: unsupported workstream: {workstream}"
                )

            try:
                capacity = float(row["daily_capacity_hours"])
            except ValueError:
                capacity = -1.0
                errors.append(
                    f"{path}:{line_number}: daily_capacity_hours must be numeric."
                )
            if capacity != -1.0 and not 3.0 <= capacity <= 4.0:
                errors.append(
                    f"{path}:{line_number}: daily capacity must be between 3 and 4 hours."
                )

            members.append(
                Member(
                    member_id=member_id,
                    github_username=username,
                    scrum_role=role,
                    preferred_workstream=workstream,
                    daily_capacity_hours=capacity,
                )
            )

    if len(members) != 6:
        errors.append(f"{path}: expected exactly 6 members, found {len(members)}.")

    ids = [member.member_id.casefold() for member in members]
    usernames = [member.github_username.casefold() for member in members]
    if len(ids) != len(set(ids)):
        errors.append(f"{path}: duplicate member_id detected.")
    if len(usernames) != len(set(usernames)):
        errors.append(f"{path}: duplicate github_username detected.")

    role_counts = {
        role: sum(member.scrum_role == role for member in members)
        for role in ALLOWED_ROLES
    }
    if role_counts["product_owner"] != 1:
        errors.append(f"{path}: exactly one product_owner is required.")
    if role_counts["scrum_master"] != 1:
        errors.append(f"{path}: exactly one scrum_master is required.")
    if role_counts["developer"] != 4:
        errors.append(f"{path}: exactly four developers are required.")

    return members, errors


def main() -> int:
    args = parse_args()
    team_a, errors_a = load_team(args.team_a, "A")
    team_b, errors_b = load_team(args.team_b, "B")
    errors = errors_a + errors_b

    all_usernames = [
        member.github_username.casefold() for member in [*team_a, *team_b]
    ]
    if len(all_usernames) != len(set(all_usernames)):
        errors.append("The same GitHub username appears in both teams.")

    if errors:
        print("Team validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("Team validation passed.")
    print("Team A: 6 members; Scrum Master: Tojan-Naiem")
    print("Team B: 6 members; Scrum Master: alaamadii")
    print("No email addresses were printed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
