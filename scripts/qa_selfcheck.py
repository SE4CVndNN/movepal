#!/usr/bin/env python3
"""MovePal QA dry run: rehearse the MP-028/030/031/032 checks from
docs/qa_plan.md against the current commit before external QA
(team-aidsign) starts on 29 July 2026.

This does NOT replace pytest, Ruff, CI, or a real external QA pass. It is a
fast, scriptable rehearsal so the development team can catch the same
problems the external QA testers would find, using the same fixtures the
test suite already uses (data/landmarks/*.json), without a camera or
browser. It talks to the app only through Flask's test client -- no live
server, network, or webcam is required.

What it does NOT cover (needs a real browser + camera; see the companion
manual checklist docs/qa_dry_run_manual.md):

- MP-029 camera permission / denial / no-camera / browser fallback UI.
- MP-033 visual responsive layout, keyboard navigation, focus rings.

Usage:
    python scripts/qa_selfcheck.py
    python scripts/qa_selfcheck.py --skip-lint   # skip ruff/pytest subprocess checks
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

RESULTS: list[tuple[str, str, str]] = []  # (qa_id, case, "PASS"/"FAIL"/"WARN")


def record(qa_id: str, case: str, ok: bool, detail: str = "") -> None:
    status = "PASS" if ok else "FAIL"
    RESULTS.append((qa_id, case, status))
    marker = "OK  " if ok else "FAIL"
    line = f"[{marker}] {qa_id:8s} {case}"
    if detail and not ok:
        line += f" -- {detail}"
    print(line)


def warn(qa_id: str, case: str, detail: str) -> None:
    RESULTS.append((qa_id, case, "WARN"))
    print(f"[WARN] {qa_id:8s} {case} -- {detail}")


def run_subprocess_check(qa_id: str, case: str, cmd: list[str]) -> None:
    try:
        completed = subprocess.run(
            cmd, cwd=ROOT, capture_output=True, text=True, timeout=300
        )
    except FileNotFoundError as exc:
        record(qa_id, case, False, f"command not found: {exc}")
        return
    ok = completed.returncode == 0
    detail = (completed.stdout + completed.stderr).strip().splitlines()
    tail = " | ".join(detail[-3:]) if not ok else ""
    record(qa_id, case, ok, tail)


# ---------------------------------------------------------------------------
# MP-028: clean install / lint / test / startup sanity
# ---------------------------------------------------------------------------


def section_mp028(skip_lint: bool) -> None:
    print("\n--- MP-028: installation, lint, tests, startup ---")
    if skip_lint:
        warn("MP-028", "ruff/pytest/compileall", "skipped (--skip-lint)")
    else:
        run_subprocess_check(
            "MP-028", "ruff check .", [sys.executable, "-m", "ruff", "check", "."]
        )
        run_subprocess_check(
            "MP-028",
            "ruff format --check .",
            [sys.executable, "-m", "ruff", "format", "--check", "."],
        )
        run_subprocess_check("MP-028", "pytest", [sys.executable, "-m", "pytest", "-q"])
        run_subprocess_check(
            "MP-028",
            "compileall app tests",
            [sys.executable, "-m", "compileall", "-q", "app", "tests"],
        )

    model_path = ROOT / "pose_landmarker_lite.task"
    record(
        "MP-028",
        "pose model file present",
        model_path.exists(),
        f"expected at {model_path}",
    )

    from app import create_app

    app = create_app({"TESTING": True, "SECRET_KEY": "qa-selfcheck"})
    client = app.test_client()
    resp = client.get("/api/health")
    record("MP-028", "GET /api/health returns 200", resp.status_code == 200)
    record(
        "MP-028",
        "GET /api/health returns JSON body",
        resp.is_json and bool(resp.get_json()),
    )
    resp = client.get("/")
    record("MP-028", "GET / (start screen) returns 200", resp.status_code == 200)


# ---------------------------------------------------------------------------
# MP-029: camera / browser -- cannot be scripted, point at manual checklist
# ---------------------------------------------------------------------------


def section_mp029() -> None:
    print("\n--- MP-029: camera permission / browser / fallback ---")
    warn(
        "MP-029",
        "camera permission, denial, no-camera, browser fallback",
        "requires a real browser + webcam; use docs/qa_dry_run_manual.md",
    )


# ---------------------------------------------------------------------------
# MP-030: pose visibility + three movements, via the same fixtures pytest uses
# ---------------------------------------------------------------------------


def _load_fixture_file(name: str) -> list[dict[str, Any]]:
    import json

    path = ROOT / "data" / "landmarks" / name
    return json.loads(path.read_text(encoding="utf-8"))


def _observed_status(payload: dict[str, Any]) -> str:
    if not payload.get("visibility_ok", True):
        return "low_visibility"
    if payload.get("completed"):
        return "success"
    return "retry"


def section_mp030(client) -> None:
    print("\n--- MP-030: pose visibility and three movements ---")
    fixture_files = {
        "raise_both_arms": "raise_both_arms_fixtures.json",
        "side_reach": "side_reach_fixtures.json",
        "knee_lift_or_step": "knee_lift_fixtures.json",
    }
    for movement, filename in fixture_files.items():
        fixtures = _load_fixture_file(filename)
        for fx in fixtures:
            client.post("/api/session/reset")
            body: dict[str, Any] = {
                "movement": movement,
                "fixture_id": fx["fixture_id"],
            }
            if "requested_side" in fx:
                body["side"] = fx["requested_side"]
            resp = client.post("/api/movement", json=body)
            case = f"{movement}/{fx['fixture_id']} -> expect {fx['expected_status']}"
            if resp.status_code != 200:
                record("MP-030", case, False, f"HTTP {resp.status_code}")
                continue
            payload = resp.get_json()
            observed = _observed_status(payload)
            record(
                "MP-030",
                case,
                observed == fx["expected_status"],
                f"observed={observed} feedback_code={payload.get('feedback_code')}",
            )

    # No pose / unsupported movement edge cases.
    resp = client.post(
        "/api/movement", json={"movement": "not_a_real_movement", "fixture_id": "x"}
    )
    record(
        "MP-030",
        "unsupported movement code rejected",
        resp.status_code == 400,
    )
    resp = client.post("/api/movement", json={"movement": "side_reach"})
    record(
        "MP-030",
        "missing fixture_id rejected",
        resp.status_code == 400,
    )
    resp = client.post(
        "/api/movement",
        json={
            "movement": "side_reach",
            "fixture_id": "synthetic_side_reach_left_positive_001",
            "side": "sideways",
        },
    )
    record(
        "MP-030",
        "invalid side value rejected",
        resp.status_code == 400,
    )


# ---------------------------------------------------------------------------
# MP-031: feedback wording, stars, repeat/reset, session summary
# ---------------------------------------------------------------------------

_DISALLOWED_TERMS = (
    "diagnos",
    "treat",
    "therap",
    "disorder",
    "clinical",
    "prescri",
    "rehab",
)


def section_mp031(client) -> None:
    print("\n--- MP-031: feedback, scoring, repeat, reset, summary ---")

    from app.services.feedback import FEEDBACK_MESSAGES

    leaked = [
        code
        for code, text in FEEDBACK_MESSAGES.items()
        if any(term in text.lower() for term in _DISALLOWED_TERMS)
    ]
    record(
        "MP-031",
        "feedback wording avoids medical/clinical language",
        not leaked,
        f"flagged codes: {leaked}",
    )

    client.post("/api/session/reset")
    success_body = {
        "movement": "raise_both_arms",
        "fixture_id": "synthetic_raise_arms_positive_001",
    }
    first = client.post("/api/movement", json=success_body).get_json()
    record("MP-031", "first success attempt awards a star", first["stars"] == 1)

    # By design (see app/services/scoring.py ScoringSession /
    # SessionStateService.save_scoring_session), each persisted request that
    # completes a movement starts a fresh attempt, so redoing the same
    # movement in a *separate* request earns another star -- this is the
    # "repeated attempts" gameplay loop, not double-counting a single
    # attempt. format_feedback's idempotence guard only protects multiple
    # frames evaluated within one still-open attempt/request.
    repeat = client.post("/api/movement", json=success_body).get_json()
    record(
        "MP-031",
        "repeating a completed movement in a new request awards another star",
        repeat["stars"] == 1,
        f"got stars={repeat['stars']}",
    )

    summary = client.get("/api/session/summary").get_json()
    record(
        "MP-031",
        "session summary reflects attempted/completed/stars",
        summary["attempted_movements"] >= 1
        and summary["completed_movements"] >= 1
        and summary["stars"] >= 1,
        str(summary),
    )

    finish = client.post("/api/session/finish").get_json()
    record(
        "MP-031",
        "session finish returns a friendly, non-empty message",
        bool(finish.get("message")),
    )

    reset = client.post("/api/session/reset")
    record("MP-031", "session reset returns success", reset.status_code == 200)
    summary_after_reset = client.get("/api/session/summary").get_json()
    record(
        "MP-031",
        "no stale score/session data after reset",
        summary_after_reset
        == {"attempted_movements": 0, "completed_movements": 0, "stars": 0},
        str(summary_after_reset),
    )


# ---------------------------------------------------------------------------
# MP-032: invalid input, oversized upload, safe errors, privacy/disclaimer
# ---------------------------------------------------------------------------


def section_mp032(client, app) -> None:
    print("\n--- MP-032: invalid input, errors, privacy, disclaimer ---")

    resp = client.post("/api/frame", data={})
    record(
        "MP-032",
        "missing image file returns 400 without a stack trace",
        resp.status_code == 400 and "Traceback" not in resp.get_data(as_text=True),
    )

    from io import BytesIO

    resp = client.post(
        "/api/frame",
        data={"image": (BytesIO(b"not-an-image"), "note.txt")},
        content_type="multipart/form-data",
    )
    record(
        "MP-032",
        "unsupported file type returns 415",
        resp.status_code == 415,
    )

    original_limit = app.config.get("MAX_CONTENT_LENGTH")
    app.config["MAX_CONTENT_LENGTH"] = 50
    oversized_client = app.test_client()
    resp = oversized_client.post(
        "/api/frame",
        data={"image": (BytesIO(b"0" * 5000), "big.jpg")},
        content_type="multipart/form-data",
    )
    record(
        "MP-032",
        "oversized upload returns 413 with a JSON error (API path)",
        resp.status_code == 413 and resp.is_json,
    )
    app.config["MAX_CONTENT_LENGTH"] = original_limit

    resp = client.get("/does-not-exist-qa-probe")
    body = resp.get_data(as_text=True)
    record(
        "MP-032",
        "unknown route returns safe 404 without a stack trace or file path",
        resp.status_code == 404 and "Traceback" not in body and str(ROOT) not in body,
    )

    index_html = client.get("/").get_data(as_text=True)
    record(
        "MP-032",
        "non-medical disclaimer is visible on the page",
        "not a medical" in index_html.lower() or "not a doctor" in index_html.lower(),
    )

    privacy_doc = ROOT / "docs" / "privacy.md"
    linked_from_app = "privacy" in index_html.lower()
    if privacy_doc.exists() and not linked_from_app:
        warn(
            "MP-032",
            "privacy notice reachable from the running app",
            "docs/privacy.md exists but the rendered page has no visible "
            "privacy link/section -- a QA tester using only the app "
            "(not the repo) may not find it",
        )
    else:
        record(
            "MP-032", "privacy notice reachable from the running app", linked_from_app
        )


# ---------------------------------------------------------------------------
# MP-033 (partial): static accessibility smoke checks on the rendered page
# ---------------------------------------------------------------------------


def section_mp033(client) -> None:
    print("\n--- MP-033: accessibility smoke (static, partial) ---")
    html = client.get("/").get_data(as_text=True)
    record(
        "MP-033",
        "viewport meta tag present (mobile scaling)",
        'name="viewport"' in html,
    )
    record(
        "MP-033",
        "at least one aria-live region present for dynamic status text",
        "aria-live=" in html,
    )
    warn(
        "MP-033",
        "keyboard navigation, focus rings, real narrow-width layout",
        "requires a real browser; use docs/qa_dry_run_manual.md",
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--skip-lint",
        action="store_true",
        help="skip the ruff/pytest/compileall subprocess checks (faster re-runs)",
    )
    args = parser.parse_args()

    section_mp028(args.skip_lint)

    from app import create_app

    app = create_app({"TESTING": True, "SECRET_KEY": "qa-selfcheck"})
    client = app.test_client()

    section_mp029()
    section_mp030(client)
    section_mp031(client)
    section_mp032(client, app)
    section_mp033(client)

    print("\n--- Summary ---")
    failed = [r for r in RESULTS if r[2] == "FAIL"]
    warned = [r for r in RESULTS if r[2] == "WARN"]
    passed = [r for r in RESULTS if r[2] == "PASS"]
    print(f"PASS: {len(passed)}  FAIL: {len(failed)}  WARN(manual): {len(warned)}")
    if failed:
        print("\nFailed cases:")
        for qa_id, case, _ in failed:
            print(f"  - [{qa_id}] {case}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
