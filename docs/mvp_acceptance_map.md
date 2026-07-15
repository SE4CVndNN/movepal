# MovePal MVP Acceptance Map

This document maps Sprint 1 MVP capabilities to observable evidence, target test levels, and responsible task issues. It serves as the source of truth for QA and final demo verification.

---

## Capability-to-Evidence Mapping

| MVP Capability | Observable User Behavior (Acceptance Criteria) | Evidence / Test Level | Owning Issue | Owner |
| :--- | :--- | :--- | :--- | :--- |
| **1. Webcam Input** | User clicks "Use Live Webcam" and sees their live video stream on the UI. | Manual UI Test / Visual Check | `MP-006` | @IslamOuda85 |
| **2. Fallback Input** | User clicks "Use Demo Video" and a pre-recorded exercise video plays instead of the webcam. | Manual UI Test (No camera required) | `MP-006` | @IslamOuda85 |
| **3. Three Exercises** | System detects and tracks three specific exercises (arms rise, side reach, knee lift). | Model Integration Test / UI Check | `MP-009` | @IslamOuda85 |
| **4. Low-Visibility Help** | Example: If user's knees are cut off during caming, UI displays: *"Keep your knees in view..."* | Manual Pose Occlusion Test | `MP-023` | @IslamOuda85 |
| **5. Gamification (Stars)**| When a user completes an exercise rep, a star icon animates and increments their score. | UI Component Unit Test | `MP-026` | @IslamOuda85 |
| **6. Non-Medical Border**| Safe wording from `content_baseline.md` is displayed in the footer and session summary. | Content Audit / Manual Check | `MP-002` | @IslamOuda85 |

---

## Decision Log (Sprint 1 Verification)

*   **Decision 1:** What to do if tester has no webcam?
    *   *Resolution:* We use the "Fallback Input" pathway with a bundled MP4 skeleton video.
*   **Decision 2:** Do we track joints perfectly in low light?
    *   *Resolution:* No, the MVP will gracefully show the "Low Visibility" alert rather than attempting to guess wrong.
