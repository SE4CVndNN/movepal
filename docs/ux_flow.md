# MovePal UX Flow (MP-006 / MP-011)

## Screen sequence

start → activity choice → camera choice → (live camera | fallback sample) → feedback → (retry activity | summary)

## Camera / fallback state table

| Trigger                                             | Resulting state | User-facing message                                                                                |
| --------------------------------------------------- | --------------- | -------------------------------------------------------------------------------------------------- |
| User clicks "Use Live Webcam" and grants permission | camera-live     | "Webcam connected successfully! Prepare to move."                                                  |
| User clicks "Use Live Webcam" and denies permission | camera-fallback | "Camera access was denied. Please enable camera permissions in your browser settings to continue." |
| No camera device exists                             | camera-fallback | "No camera was detected. Please connect a webcam or use the local demo sample."                    |
| User clicks "Use Local Demo Sample" directly        | camera-fallback | "Using local demo feed. No camera access required."                                                |
| User clicks "Stop Camera"                           | camera-choice   | (camera stream stopped, tracks released)                                                           |

## Game state model (MP-011)

`document.body.dataset.appState` reflects the current logical game state:

| Screen                       | App state  |
| ---------------------------- | ---------- |
| start, activity              | idle       |
| camera-choice                | preparing  |
| camera-live, camera-fallback | capturing  |
| feedback                     | evaluating |
| summary                      | summary    |

Success/retry states are not split yet — that depends on MP-014 providing
real pass/fail evaluation results instead of the current placeholder
"Simulate attempt" button.

## Avatar asset

The avatar in `partials/_avatar.html` is original SVG artwork created
directly in code for this task. It currently renders as a playful dancing
robot mascot, not a third-party or traced image. No attribution is required;
this asset is free to reuse within the project.

## Score region

A persistent star counter (`#score-region`) lives in the page header and
is visible on every screen, separate from the end-of-session summary. Its
increment logic is currently a placeholder: each "Simulate attempt"
awards exactly one star. Real scoring will be wired up once `scoring.py`
is connected to the actual game flow.

## Accessibility notes

- All interactive elements are native `<button>` elements, so keyboard focus order follows visual/DOM order automatically.
- Focus is given an explicit thick, high-contrast outline via `:focus-visible` — not left to the browser default.
- Buttons collapse to full-width on screens narrower than 22.5rem (360px), matching the MP-011 acceptance criteria width.
- Live status text (`#camera-status`, `#fallback-reason`, `#score-region`, `#health-result`) uses `aria-live="polite"` so screen readers announce state changes.

## Decisions and fixes made during implementation

- Initially wrote the permission-denied message into `#camera-status` on the camera-choice screen, but that screen gets hidden immediately when switching to the fallback screen, so the message was never visible. Fixed by adding a dedicated `#fallback-reason` element on the fallback screen itself.
- Visual/child-friendly design (MP-011) builds directly on the MP-006 flow rather than replacing it — same screens, same state machine, restyled and extended.
- Kept core flow wording aligned with `docs/content_baseline.md` for input selection, live-camera guidance, and session summary copy. Slightly friendlier start-screen wording remains only in the welcome header, to preserve a lightweight child-friendly tone while retaining the approved disclaimer text.
- Chose soft pastel colors, rounded shapes, and bright button accents to make the interface feel playful and approachable rather than clinical. The color palette is intentionally gentle and energetic, supporting a kid-friendly mood without reducing text readability.
- Chose a Comic Sans-first font stack for readability/dyslexia-friendliness; flagged for review since it's also a common design joke — easy to swap by editing one line in `app.css`.

## Known limitations / follow-up

- No real pose detection — "Simulate attempt" always shows a placeholder success message; MP-014 replaces this with real evaluation.
- No captured frame is saved or sent anywhere; MP-012 will add the real fallback sample/upload wiring.
- Score increment is a placeholder, not tied to real scoring logic yet.
- Success/retry visual states aren't split yet — pending MP-014.
- Only manually tested in Chrome on Windows — cross-browser testing is out of scope for this spike.
- The "no camera detected" (`NotFoundError`) path was verified by code review only — no hardware available to test without a camera.
