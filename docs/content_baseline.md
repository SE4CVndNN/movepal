# MovePal Content Baseline

This document outlines the approved text strings for the MovePal user interface, including safety disclaimers and user feedback messages.

---

## 1. Safety & Legal Disclaimer
> **Constraint:** Do not mention treatment, rehabilitation, diagnosis, or therapist replacement.

* **Main Disclaimer Banner:**  
  "MovePal is a playful movement-practice prototype created for software-engineering education. It is not a medical device, diagnostic tool, rehabilitation system, treatment, or replacement for a physiotherapist or healthcare professional.

  A success result means only that the current pose landmarks satisfied the project’s configured game rules. It does not establish that a movement is medically correct, safe for a particular person, or beneficial for a health condition."

---

## 2. Input Selection Screen
* **Camera Choice Header:**  
  "Choose Your Input Method"
* **Webcam Button Text:**  
  "Use Live Webcam"
* **Explain why camera permission is requested:**  
  "Please allow live camera access so you can have a live experience with MovePal."
* **Permission Denied Message:**  
  "Camera access was denied. Please enable camera permissions in your browser settings to continue."
* **No Camera Detected Message:**  
  "No camera was detected. Please connect a webcam or use the local demo sample."
* **Transient processing and no-storage-by-default wording:**  
  "Camera frames are processed temporarily and are not stored by default."
* **Stop/Reset behavior:**  
  "Please click on Stop Camera or Reset to stop recording."
* **Webcam Success Notification:**  
  "Webcam connected successfully! Prepare to move."
* **Fallback Button Text:**  
  "Use Local Demo Sample (No Camera)"
* **Fallback Active Notification:**  
  "Using local demo feed. No camera access required."

---

## 3. Pose & Visibility Feedback
> **Constraint:** Use friendly, encouraging instructions when the neural network cannot detect the user's pose.

* **General Low Visibility Alert:**  
  "We lost track of you! Please step back so your full body is visible in the frame."
* **Camera Obstructed Alert:**  
  "Looks a bit dark or blurry. Please adjust your lighting or clean your lens."
* **Body Part Missing Alert:**  
  "Keep your knees and hips in view so we can track your movements!"
* **Incomplete Performance - not holding for enough time:**  
  "Please hold a bit longer for better validation."
* **Incomplete Performance - incorrect position:**  
  "Please adjust your pose slightly."

---

## 4. Performance & Gamification Feedback
> **Constraint:** Focus entirely on playfulness (stars, points) rather than physical health progression.

* **Movement Completed (Success):**  
  * **Singular Success:** "Awesome job! You've earned ⭐ 1 Star!"
  * **Plural Success:** "Awesome job! You've earned ⭐ {count} Stars!"
* **Encouragement to Try Again (Retry):**  
  "Keep going! Adjust your position and try that movement again."
* **Session Summary Header:**  
  "Session Complete!"
* **Session Summary Body:**  
  "You successfully completed your movements today and earned a total of ⭐ {count} Stars! Thanks for playing with MovePal!"
