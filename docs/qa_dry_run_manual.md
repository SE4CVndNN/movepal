# MovePal internal QA dry run (manual, browser-only)

This is `team-movepal`'s own rehearsal of the parts of `docs/qa_plan.md` that
`scripts/qa_selfcheck.py` cannot script (no camera, no real browser). Run
this once against the intended release-candidate commit *before* handing off
to `team-aidsign` on 29 July 2026, so the same problems are found and fixed
internally first.

Use the recording format from `docs/qa_plan.md` section 6 for anything that
fails. This document only needs a quick pass/fail per row, not full test-case
records — open a bug issue for anything that fails.

## Before you start

- [ ] Run `python scripts/qa_selfcheck.py` and confirm 0 FAIL.
- [ ] `python run.py`, open the printed URL in the target browser.
- [ ] Note browser + version and OS.

## MP-029 — camera permission, no-camera, browser, fallback

| # | Case | Steps | Expected | Pass? |
|---|---|---|---|---|
| 1 | Initial permission prompt | Choose "Use the camera" on a move | Browser asks for camera permission | |
| 2 | Permission granted | Allow the prompt | Live preview appears, `camera-status` updates | |
| 3 | Permission denied | Reload, choose camera, deny the prompt | Friendly message shown, no raw browser error, user is guided to fallback/upload | |
| 4 | No camera device | Test on a machine/VM with no camera, or disable it in OS settings | Friendly "no camera" guidance, fallback offered | |
| 5 | Stop/reset camera | Start camera, click "Cancel camera" | Camera light turns off, stream stops immediately | |
| 6 | Fallback demo | Choose "Try the built-in demo" | Demo runs without a camera and reaches feedback | |
| 7 | Upload instead of camera | Choose "Upload a photo" | File picker accepts jpg/png; non-image files rejected client-side or by `/api/frame` (415) | |

## MP-033 — responsive layout, keyboard, accessibility sanity

| # | Case | Steps | Expected | Pass? |
|---|---|---|---|---|
| 1 | Desktop width | View at ~1280px wide | Layout readable, nothing overlapping/cut off | |
| 2 | Narrow/mobile width | Resize to ~375px wide (or device emulation) | Buttons/text remain usable, no horizontal scroll | |
| 3 | Keyboard-only nav | Tab through start → activity → camera-choice screens using only keyboard | Every button reachable in a sensible order | |
| 4 | Visible focus | Tab through controls | A visible focus outline/ring appears on the focused control | |
| 5 | Screen-reader-ish sanity | Check `role="status" aria-live="polite"` regions announce camera/upload status changes (already confirmed present by `qa_selfcheck.py`) | Status text changes are exposed, not just visual | |
| 6 | Color-independent meaning | Squint/grayscale the page | Success vs. retry feedback is still distinguishable by text/icon, not color alone | |

## Cross-cutting spot checks worth 5 minutes

- [ ] Full end-to-end run: start → pick a move → camera or fallback → feedback → summary → "Play again" resets stars to 0.
- [ ] Refresh mid-session: confirm no crash, and that reset behavior matches `docs/limitations.md` section 4 (session is cookie-only, not resumable across browsers/devices).

## Findings log

Record anything found here (or directly as GitHub issues) so MP-024's handoff
can list known non-blocking limitations up front instead of `team-aidsign`
rediscovering them:

| Finding | Severity (qa_plan.md §7) | Fixed before hand-off? |
|---|---|---|
| | | |
