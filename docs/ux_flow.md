# MovePal UX Flow (MP-006 / MP-011 / MP-012)

## Screen sequence

start → activity choice → camera choice → (live camera | fallback demo) → feedback → (retry activity | summary)

## Camera / fallback state table

| Trigger                                            | Resulting state | User-facing message                                                                                          |
| -------------------------------------------------- | --------------- | ------------------------------------------------------------------------------------------------------------ |
| User clicks "Use the camera" and grants permission | camera-live     | "Camera is on! Get ready to move."                                                                           |
| User clicks "Use the camera" and denies permission | camera-fallback | "Camera access was denied. You can still try the demo for your chosen move."                                 |
| No camera device exists                            | camera-fallback | "No camera was detected. You can still try the demo for your chosen move."                                   |
| Browser requires secure context or unsupported API | camera-fallback | "Camera access requires a secure connection. Please use the built-in demo instead."                          |
| User clicks "Try the built-in demo" directly       | camera-fallback | "Use the built-in demo for the move you already picked."                                                     |
| User clicks "Start demo" on fallback screen        | feedback        | fallback move is evaluated via `/api/movement`; deterministic raise-both-arms result transitions to feedback |
| User clicks "Stop Camera"                          | camera-choice   | (camera stream stopped, tracks released)                                                                     |

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
- The live preview uses `navigator.mediaDevices.getUserMedia`, draws one
  bounded frame to a hidden canvas, and immediately stops every camera track
  before encoding or uploading the picture.
- Every uploaded frame is sent to `/api/frame` in a `FormData` request with the field name `image`.
- Overlapping uploads are prevented with a single `requestInFlight` guard and button disabling.
- The camera-choice screen now shows a preview of the selected move before the child chooses camera or fallback demo.
- A dedicated fallback screen was added so the app can run fully without a live camera, and it shows the move the child already selected before starting the demo.
- A browser security-context failure now shows a clear message and falls back to the demo screen.
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
3. Confirm the camera indicator turns off immediately after the picture is
   copied to the canvas, before the server response is received.
4. Simulate a server or network failure, then confirm the app moves to the
   fallback screen without reopening the camera.
5. Confirm all camera `MediaStream` tracks are stopped, `activeStream` is
   cleared, and the preview is detached.
6. Confirm the fallback screen shows the already selected move and that "Start demo" begins the demo for that move.
7. Complete the deterministic fallback and confirm the fallback result comes from `/api/movement`.
8. Confirm no star is awarded from the pose extraction step alone.

## Game loop integration (MP-019)

- /api/movement now supports all three movements via a lookup table
  (\_EVALUATORS), not just raise_both_arms.
- /api/frame optionally evaluates a movement using the real captured
  landmarks when a `movement` (and `side`, where required) field is sent,
  reusing the same feedback/session code path as /api/movement — live
  camera and fallback return identical response shapes.
- Live/uploaded Side Reach requires both shoulders plus the requested
  anatomical side's elbow and wrist. The unrelated arm and hips do not block
  a clear live reach when they are cropped or briefly low visibility. Strict
  deterministic fixture evaluation keeps the full documented posture checks.
- Side Reach derives "outward" from the observed shoulder midpoint, so raw
  camera frames and horizontally mirrored input preserve the same anatomical
  left/right result.
- Fallback demo for side_reach and knee_lift_or_step is left-side only;
  no guaranteed-success right-side fixture exists yet.
- A stale-response guard (`activityToken`) discards any response that
  arrives after the user has already switched to a different activity.
- "Play again" is handled by switching the UI back to the start screen and calling POST /api/session/reset to clear the current session state.
- Reaching the summary screen is also client-side only; the frontend does not
  call POST /api/session/finish for the authoritative stars/attempted/completed
  counts.

### Known limitations

- Live camera access is one-shot: each attempt opens a short preview,
  captures one frame after the countdown, and releases the device. Retrying
  requires a new explicit camera action.
- No mid-activity movement switching while a capture is in flight; the
  stale-response guard discards the result rather than applying it.
