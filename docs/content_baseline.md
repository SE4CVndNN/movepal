# MovePal Content Baseline

This document outlines the approved text strings for the MovePal user interface, including safety disclaimers and user feedback messages..

---

## 1. Safety & Legal Disclaimer
> **Constraint:** Do not mention treatment, rehabilitation, diagnosis, or therapist replacement.

*   **Main Disclaimer Banner:**  
    "MovePal is a playful prototype designed to encourage movement. It does not provide medical advice, diagnosis, treatment, or physical therapy. Consult a medical professional before starting any new exercise routine."

---

## 2. Input Selection Screen
*   **Camera Choice Header:**  
    "Choose Your Input Method"
*   **Webcam Button Text:**  
    "Use Live Webcam"
*   **Webcam Success Notification:**  
    "Webcam connected successfully! Prepare to move."
*   **Fallback Button Text:**  
    "Use Sample Demo Video (No Camera)"
*   **Fallback Active Notification:**  
    "Using local demo video feed. No camera access required."

---

## 3. Pose & Visibility Feedback
> **Constraint:** Use friendly, encouraging instructions when the neural network cannot detect the user's pose.

*   **General Low Visibility Alert:**  
    "We lost track of you! Please step back so your full body is visible in the frame."
*   **Camera Obstructed Alert:**  
    "Looks a bit dark or blurry. Please adjust your lighting or clean your lens."
*   **Body Part Missing Alert:**  
    "Keep your knees and hips in view so we can track your movements!"
*   **Incomplete Performance:**  
    "Please hold more for validation"
    "Please adjust your pose a bit"
---

## 4. Performance & Gamification Feedback
> **Constraint:** Focus entirely on playfulness (stars, points) rather than physical health progression.

*   **Movement Completed (Success):**  
    "Awesome job! You've earned ⭐ 1 Star!"
*   **Encouragement to Try Again (Retry):**  
    "Keep going! Adjust your position and try that movement again."
*   **Session Summary Header:**  
    "Workout Complete!"
*   **Session Summary Body:**  
    "You successfully completed your movements and earned a total of **{stars}** stars today! Thanks for moving with MovePal!"``
