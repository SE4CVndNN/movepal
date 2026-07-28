# MP-023 hardening checklist and findings

Status: implementation and automated verification complete locally on
2026-07-28. A pull request review and cross-browser manual QA remain before a
release decision.

| Review area | Evidence and outcome | Status |
| --- | --- | --- |
| Upload input | `MAX_CONTENT_LENGTH` defaults to 5 MB; `/api/frame` and `/api/pose/preview` reject missing files and unsupported extension/MIME combinations. API errors are structured and actionable. | Complete |
| Temporary files | `process_frame` creates a private temporary file only for inference and unlinks it in `finally`; integration tests assert deletion after success and preview use. | Complete |
| Debug and error exposure | `DEBUG = False` in the app config and `run.py`. A generic 500 handler logs safe endpoint context with traceback server-side and returns a friendly page or JSON without internal details. | Complete |
| Logging and browser retention | Application logs record timing/status only; no frame bytes, landmark values, filenames, names, or secrets are emitted. The client has no `localStorage`/`sessionStorage` usage; it clears canvas/overlay and stops camera tracks after capture or navigation. | Complete |
| Privacy and disclaimer | The non-medical footer appears on every page and camera screen; camera copy states the image is used only for the game and the stream turns off after capture. `docs/privacy.md` now reflects the actual no-history MVP. | Complete |
| Keyboard and mobile basics | Core controls are native buttons/labelled file inputs; `:focus-visible` provides a high-contrast focus cue; changing screens moves focus to its heading; the layout makes buttons full width at 360px. | Complete (automated structure check) |
| Residual risk | The formal screen-reader/contrast audit, manual browser/device checks, independent review, and CI on both supported operating systems remain required before merge. See `docs/limitations.md`. | Open release work |

## Findings and decisions

1. The app already had safe upload size/type gates, short-lived temporary
   files, disabled debug mode, camera cleanup, status regions, and a visible
   disclaimer. Those controls were retained and regression-covered.
2. No generic 500 handler existed. It has been added for both HTML and API
   responses so normal users do not receive Flask's default error page or a
   traceback.
3. Screen transitions previously left keyboard focus on a control that became
   hidden. Each active screen now receives programmatic focus at its heading.
4. The previous privacy document described profiles, retained session
   analytics, optional raw-video debugging, and production transport/storage
   controls that the MVP does not implement. It was corrected rather than
   documenting capabilities that do not exist.

## Repeatable verification

The automated suite was also run after integrating the latest `master`,
including the camera-guidance and photo-upload changes from PR #120.

```powershell
python -m ruff check .
python -m ruff format --check .
python -m pytest
python -m compileall app tests
```

Manual release checks still required:

1. At 360–400px width, tab through start → activity → camera choice → upload
   or fallback and confirm every control is visible, reachable, and has a
   clear focus indicator.
2. With a screen reader, confirm camera/upload status messages are announced.
3. Demonstrate an unsupported or oversized upload, then confirm no traceback
   or private data appears in the browser or captured evidence.
4. Obtain an independent reviewer and green Windows/Linux CI before merge.
