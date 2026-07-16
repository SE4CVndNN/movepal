# MovePal Content Baseline

This document outlines the approved text strings for the MovePal user interface, including safety disclaimers and user feedback messages..

---

## 1. Safety & Legal Disclaimer
> **Constraint:** Do not mention treatment, rehabilitation, diagnosis, or therapist replacement.

*   **Main Disclaimer Banner:**  
    "Developed as an educational prototype for software engineering, MovePal is a playful movement application. It is not intended for medical diagnosis, rehabilitation, or treatment, and should not replace professional healthcare advice.

A "success" outcome indicates solely that the user's pose met the pre-configured gameplay criteria; it is not an endorsement of medical correctness, personal safety, or therapeutic benefit."
---

## 2. Input Selection Screen
*   **Camera Choice Header:**  
    "Choose Your Input Method"
*   **Webcam Button Text:**  
    "Use Live Webcam"
*   **Explain why camera permission is requested:**  
    "Please allow for live camera review so you could have a live experience with MovePal"
*   **permission-denied and no-camera behavior:**  
    "Please try again or upload a fallback video"
*   **transient processing and no-storage-by-default wording:**  
    "This action do *not* store any data and relies on live processing"
*   **stop/reset behavior:**  
    "PLease click on `Esc` to exit"
*   **Webcam Success Notification:**  
    "Webcam connected successfully! Prepare to move."
*   **Fallback Button Text:**  
    "Use Local Demo Sample (No Camera)"
*   **Fallback Active Notification:**  
    "Using local demo feed. No camera access required."

---

## 3. Pose & Visibility Feedback
> **Constraint:** Use friendly, encouraging instructions when the neural network cannot detect the user's pose.

*   **General Low Visibility Alert:**  
    "We lost track of you! Please step back so your full body is visible in the frame."
*   **Camera Obstructed Alert:**  
    "Looks a bit dark or blurry. Please adjust your lighting or clean your lens."
*   **Body Part Missing Alert:**  
    "Keep your knees and hips in view so we can track your movements!"
*   **Incomplete Performance - not holding for enough time:**  
    "Please hold more for better validation"
*   **Incomplete Performance - incorrect position:**  
    "Please change your pose a bit"
---

## 4. Performance & Gamification Feedback
> **Constraint:** Focus entirely on playfulness (stars, points) rather than physical health progression.

*   **Movement Completed (Success):**  
    -(Singular Success)"Awesome job! You've earned ⭐ 1 Star!"
    -(plurlar Success)"Awesome job! You've earned ⭐ {count} Stars!"
*   **Encouragement to Try Again (Retry):**  
    "Keep going! Adjust your position and try that movement again."
*   **Session Summary Header:**  
    "session Complete!"
*   **Session Summary Body:**  
    "You successfully completed your movements today! Thanks for playing with MovePal!"``
