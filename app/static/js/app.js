"use strict";

// --- health check (kept from the starter app) ---
const healthButton = document.querySelector("#health-check");
const healthResult = document.querySelector("#health-result");

healthButton?.addEventListener("click", async () => {
  healthResult.textContent = "Checking…";
  try {
    const response = await fetch("/api/health");
    const payload = await response.json();
    healthResult.textContent = response.ok
      ? `Application status: ${payload.status}`
      : "The application returned an error.";
  } catch (_error) {
    healthResult.textContent = "The application could not be reached.";
  }
});

// --- persistent score region ---
let totalStars = 0;
const scoreCount = document.querySelector("#score-count");
const summaryStarCount = document.querySelector("#summary-star-count");
const feedbackMessage = document.querySelector("#feedback-message");

function updateScoreDisplays() {
  if (scoreCount) scoreCount.textContent = totalStars;
  if (summaryStarCount) summaryStarCount.textContent = totalStars;
}

function updateFeedbackMessage(amount) {
  if (feedbackMessage) {
    feedbackMessage.textContent = `Awesome job! You've earned ⭐ ${amount} Star${amount === 1 ? "" : "s"}!`;
  }
}

function getAttemptStarReward() {
  // Placeholder reward logic for the current movement attempt.
  // Replace with real scoring logic once pose evaluation is wired up.
  return Math.floor(Math.random() * 3) + 1;
}

function addStars(amount) {
  totalStars += amount;
  updateScoreDisplays();
}

// --- clickable flow state machine ---
const screens = document.querySelectorAll("[data-screen]");

const SCREEN_TO_STATE = {
  start: "idle",
  activity: "idle",
  "camera-choice": "preparing",
  "camera-live": "capturing",
  "camera-fallback": "capturing",
  feedback: "evaluating",
  summary: "summary",
};

function showScreen(name) {
  screens.forEach((section) => {
    section.hidden = section.dataset.screen !== name;
  });
  document.body.dataset.appState = SCREEN_TO_STATE[name] ?? "idle";
}

document.querySelectorAll("[data-goto]").forEach((button) => {
  button.addEventListener("click", () => {
    // Placeholder: award a star whenever the feedback screen is reached.
    // Replaced once real scoring logic (scoring.py) is wired up in a
    // later task.
    if (button.dataset.goto === "feedback") {
      const earnedStars = getAttemptStarReward();
      addStars(earnedStars);
      updateFeedbackMessage(earnedStars);
    }
    showScreen(button.dataset.goto);
  });
});

// --- camera / fallback probe ---
let activeStream = null;

const cameraStatus = document.querySelector("#camera-status");
const preview = document.querySelector("#camera-preview");
const fallbackReason = document.querySelector("#fallback-reason");

document
  .querySelector("#use-webcam-btn")
  ?.addEventListener("click", async () => {
    cameraStatus.textContent = "Requesting camera access…";
    try {
      activeStream = await navigator.mediaDevices.getUserMedia({ video: true });
      preview.srcObject = activeStream;
      cameraStatus.textContent =
        "Webcam connected successfully! Prepare to move.";
      showScreen("camera-live");
    } catch (error) {
      let reason;
      if (error.name === "NotAllowedError") {
        reason =
          "Camera access was denied. Please enable camera permissions in your browser settings to continue.";
      } else {
        reason =
          "No camera was detected. Please connect a webcam or use the local demo sample.";
      }
      if (fallbackReason) fallbackReason.textContent = reason;
      showScreen("camera-fallback");
    }
  });

document.querySelector("#use-fallback-btn")?.addEventListener("click", () => {
  if (fallbackReason) {
    fallbackReason.textContent =
      "Using local demo feed. No camera access required.";
  }
  showScreen("camera-fallback");
});

function stopCamera() {
  activeStream?.getTracks().forEach((track) => track.stop());
  activeStream = null;
  if (preview) preview.srcObject = null;
}

document.querySelector("#stop-camera-btn")?.addEventListener("click", () => {
  stopCamera();
  showScreen("camera-choice");
});

window.addEventListener("beforeunload", stopCamera);
