# MovePal UX Flow (MP-006 / MP-011 / MP-012)

## Screen sequence

start → activity choice → camera choice → (live camera | fallback sample) → feedback → (retry activity | summary)

## Camera / fallback state table

| Trigger                                             | Resulting state | User-facing message                                                                                   |
| --------------------------------------------------- | --------------- | ----------------------------------------------------------------------------------------------------- |
| User clicks "Use Live Webcam" and grants permission | camera-live     | "Webcam connected successfully! Prepare to move."                                                     |
| User clicks "Use Live Webcam" and denies permission | camera-fallback | "Camera access was denied. Please enable camera permissions in your browser settings to continue."    |
| No camera device exists                             | camera-fallback | "No camera was detected. Please connect a webcam or use the local demo sample."                       |
| Browser requires secure context or unsupported API  | camera-fallback | "Camera access requires a secure connection (HTTPS). Please use the local demo sample instead."       |
| User clicks "Use Local Demo Sample" directly        | sample-picker   | "Using local demo feed. No camera access required."                                                   |
| Sample selected for fallback evaluation             | feedback        | sample is evaluated via `/api/movement`; deterministic raise-both-arms result transitions to feedback |
| User clicks "Stop Camera"                           | camera-choice   | (camera stream stopped, tracks released)                                                              |

## Game state model (MP-011)

`document.body.dataset.appState` reflects the current logical game state:

| Screen                       | App state  |
| ---------------------------- | ---------- |
| start, activity              | idle       |
| camera-choice                | preparing  |
| camera-live, camera-fallback | capturing  |
| feedback (processing)        | evaluating |
| feedback (success)           | success    |
| feedback (retry)             | retry      |
| summary                      | summary    |

The app now includes separate placeholder `success` and `retry` states for
feedback. The `evaluating` state is used while waiting for the current
attempt result, and the final feedback state switches to `success` or
`retry` once the placeholder result is known.

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

- Camera permission is requested only after the user clicks "Use Live Webcam".
- The live preview uses `navigator.mediaDevices.getUserMedia`, then draws bounded frames to a hidden canvas for upload.
- Every uploaded frame is sent to `/api/frame` in a `FormData` request with the field name `image`.
- Overlapping uploads are prevented with a single `requestInFlight` guard and button disabling.
- A dedicated fallback sample picker was added so the app can run fully without a live camera.
- A browser security-context failure now shows a clear message and falls back to sample mode.
- Initially wrote the permission-denied message into `#camera-status` on the camera-choice screen, but that screen gets hidden immediately when switching to the fallback screen, so the message was never visible. Fixed by adding a dedicated `#fallback-reason` element on the fallback screen itself.
- Visual/child-friendly design (MP-011) builds directly on the MP-006 flow rather than replacing it — same screens, same state machine, restyled and extended.
- Kept core flow wording aligned with `docs/content_baseline.md` for input selection, live-camera guidance, and session summary copy. Slightly friendlier start-screen wording remains only in the welcome header, to preserve a lightweight child-friendly tone while retaining the approved disclaimer text.
- Chose soft pastel colors, rounded shapes, and bright button accents to make the interface feel playful and approachable rather than clinical. The color palette is intentionally gentle and energetic, supporting a kid-friendly mood without reducing text readability.
- Chose a Comic Sans-first font stack for readability/dyslexia-friendliness; flagged for review since it's also a common design joke — easy to swap by editing one line in `app.css`.

## Known limitations / follow-up

- Real frame capture is implemented and sent to `/api/frame`. The backend may still return `no_pose` or `low_visibility` depending on the image content.
- Score increment is a placeholder, not tied to real scoring logic yet.
- The no-camera fallback path is now deterministic for Raise Both Arms and uses the merged `/api/movement` endpoint.
- The legacy `/api/samples/<filename>` path and generated sample PNG assets are no longer wired into the current UI fallback path.
- Only manually tested in Chrome on Windows — cross-browser testing is out of scope for this spike.
- The "no camera detected" (`NotFoundError`) path was verified by code review only — no hardware available to test without a camera.

## Manual verification evidence

Use this sequence to confirm the current fallback behavior end to end:

1. Start camera mode and grant browser camera permission.
2. Capture one frame and observe that the upload is bounded to at most `640 × 480` pixels.
3. Simulate a server or network failure, then confirm the app stops periodic capture and moves to the fallback screen.
4. Confirm all camera `MediaStream` tracks are stopped, `activeStream` is cleared, and the preview is detached.
5. Enter the fallback selector and verify Raise Both Arms remains selectable while Side Reach and Knee Lift stay disabled.
6. Complete the deterministic fallback and confirm the fallback result comes from `/api/movement`.
7. Confirm no star is awarded from the pose extraction step alone.
