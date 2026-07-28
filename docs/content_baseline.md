# MovePal Content Baseline

This document outlines the approved text strings for the MovePal user interface, including safety disclaimers and user feedback messages.

---

## 1. Page Header & Safety Text

> **Constraint:** Keep the player-facing copy simple, clear, and non-medical.

- **Brand Title:**  
  "MovePal"
- **Header Subtitle:**  
  "Play, move, and collect stars."
- **Start Screen Title:**  
  "Let’s move and collect stars!"
- **Start Screen Body:**  
  "MovePal is a fun game for moving, smiling, and playing."
- **Start Screen Disclaimer:**  
  "This is just a game, not a doctor tool."
- **Footer Disclaimer:**  
  "MovePal is a playful prototype, not a medical or diagnostic tool."

---

## 2. Input Selection Screen

> **Constraint:** Use brief labels and gentle camera guidance.

- **Camera Choice Header:**  
  "Choose how to play"
- **Camera Choice Body:**  
  "After you choose a move, you can use the camera, upload a photo, or try the built-in demo."
- **Webcam Button Text:**  
  "Use the camera"
- **Upload Button Text:**  
  "Upload a photo"
- **Fallback Button Text:**  
  "Try the built-in demo"
- **Camera Permission Prompt:**  
  "Please allow camera access if the browser asks."
- **Secure-context fallback:**  
  "The camera is not ready. That is okay. You can still try the demo."
- **Unsupported browser fallback:**  
  "This browser cannot use the camera right now. You can still try the demo."
- **Camera stopped fallback:**  
  "The camera stopped. That is okay. You can still try the demo."
- **Permission denied fallback:**  
  "Camera permission was not given. You can still try the demo."
- **No camera found fallback:**  
  "No camera was found. You can still try the demo."
- **Webcam success notification:**  
  "Camera is on! Get ready to move."

### Live camera guidance

> **Constraint:** Show one short instruction at a time in large, high-contrast
> text. Use encouraging language and tell the child what to do next.

- **Person not centered:** "Stand in the middle so I can see you!"
- **Pose ready:** "Great pose! Hold still!"
- **Low light or visibility:** "A little more light, please!"
- **Raise-arms framing:** "Step back and show me your hands!"
- **Side-reach framing:** "Show your hips and {side} arm!"
- **Knee-lift framing:** "Show your {side} knee and ankle!"
- **Countdown guidance:** "Hold still—picture time!"
- **Temporary pose loss:** "I lost you—stand still and try again!"

### Uploaded photo guidance

> **Constraint:** Do not upload immediately after file selection. Show a
> local preview, validate the file, and ask for an explicit check action.
> Uploaded photos use the same pose adapter and movement rules as camera
> captures.

- **Allowed file summary:** "JPEG or PNG, up to 5 MB."
- **Check action:** "Check my move"
- **Looking for a pose:** "Looking for you…"
- **No person found:** "I can’t find a person. Choose a clear full-body photo!"
- **Unreadable file:** "That file doesn’t look like a photo!"
- **Photo too large:** "That photo is too big. Choose one under 5 MB."
- **Photo too small:** "That photo is too small. Choose a clearer one!"
- **Ready for evaluation:** "Great! I found you. Press “Check my move”."

---

## 3. Demo & Move Selection

> **Constraint:** Keep the demo flow straightforward and kid-friendly.

- **Demo Picker Title:**  
  "Pick a demo move"
- **Demo picker note:**  
  "Pick the side you want to practice."

---

## 4. Feedback & Result Messaging

> **Constraint:** Use positive, encouraging language for success and retry flows.

- **Success feedback:**  
  "You moved like a star! ⭐"
- **Success feedback (plural):**  
  "Star power! You earned ⭐ {count} stars!"
- **Success detail:**  
  "Nice move! Keep going to collect more stars."
- **Retry feedback:**  
  "Great effort! Check the feedback above and try again with the right pose."
- **Retry detail:**  
  "Check the feedback above and try again with the right pose."

---

## 5. Session Summary

> **Constraint:** Keep the completion screen celebratory.

- **Summary Title:**  
  "You did it!"
- **Summary body:**  
  "You earned ⭐ {count} stars! Thanks for playing with MovePal!"
