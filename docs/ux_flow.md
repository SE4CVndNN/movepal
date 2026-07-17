# MovePal UX Flow (MP-006 prototype)

## Screen sequence

start → activity choice → camera choice → (live camera | fallback sample) → feedback → (retry activity | summary)

## Camera / fallback state table

| Trigger | Resulting state | User-facing message |
|---|---|---|
| User clicks "Use Live Webcam" and grants permission | camera-live | "Webcam connected successfully! Prepare to move." |
| User clicks "Use Live Webcam" and denies permission | camera-fallback | "Camera access was denied. Please enable camera permissions in your browser settings to continue." |
| No camera device exists | camera-fallback | "No camera was detected. Please connect a webcam or use the local demo sample." |
| User clicks "Use Local Demo Sample" directly | camera-fallback | "Using local demo feed. No camera access required." |
| User clicks "Stop Camera" | camera-choice | (camera stream stopped, tracks released) |

## Accessibility notes

- All interactive elements are native `<button>` elements, so keyboard focus order follows visual/DOM order automatically.
- Focus outline is the browser default and was not suppressed in CSS.
- Buttons collapse to full-width on screens narrower than 30rem (~480px) to keep touch targets large.
- Live status text (`#camera-status`, `#fallback-reason`, `#health-result`) uses `aria-live="polite"` so screen readers announce state changes.

## Decisions and fixes made during implementation

- Initially wrote the permission-denied message into `#camera-status` on the camera-choice screen, but that screen gets hidden immediately when switching to the fallback screen, so the message was never visible. Fixed by adding a dedicated `#fallback-reason` element on the fallback screen itself.
- Visual/child-friendly design is intentionally out of scope here — deferred to MP-011, which explicitly owns "child-friendly page structure and visual language." This prototype only proves the flow and camera logic work.

## Known limitations / follow-up

- No real pose detection — "Simulate attempt" always shows a placeholder success message; MP-014 replaces this with real evaluation.
- No captured frame is saved or sent anywhere; MP-012 will add the real fallback sample/upload wiring.
- Star count on the summary screen is currently hardcoded, not dynamic.
- Only manually tested in Chrome on Windows — cross-browser testing is out of scope for this spike.
- The "no camera detected" (`NotFoundError`) path was verified by code review only — I don't have hardware to test without a camera. Confirming this manually is a good candidate for MP-012 or QA day.