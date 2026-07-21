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

function updateFeedbackMessage(amount, mode) {
  if (feedbackMessage) {
    const totalLabel = totalStars === 1 ? "1 Star" : `${totalStars} Stars`;
    const attemptLabel = amount === 1 ? "1 Star" : `${amount} Stars`;
    if (mode === "retry") {
      feedbackMessage.textContent =
        "Keep going! Adjust your position and try that movement again.";
    } else {
      feedbackMessage.textContent = `Awesome job! You earned ⭐ ${attemptLabel} this round. Your total is ${totalLabel}.`;
    }
  }
}

function updateFeedbackStatus(mode) {
  const statusBadge = document.querySelector("#feedback-status");
  const detail = document.querySelector("#feedback-detail");
  if (statusBadge) {
    statusBadge.textContent = mode === "retry" ? "Retry" : "Success";
    statusBadge.className = `status-badge status-${mode}`;
  }
  if (detail) {
    detail.textContent =
      mode === "retry"
        ? "Try again with a little more space and a stronger pose."
        : "This is a placeholder success result; real evaluation arrives in MP-014.";
  }
}

function getAttemptStarReward() {
  return 1;
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

function setAppState(state) {
  document.body.dataset.appState = state;
}

function showScreen(name) {
  screens.forEach((section) => {
    section.hidden = section.dataset.screen !== name;
  });
  setAppState(SCREEN_TO_STATE[name] ?? "idle");
}

document.querySelectorAll("[data-goto]").forEach((button) => {
  button.addEventListener("click", () => {
    const target = button.dataset.goto;
    const mode = button.dataset.feedback || "success";
    if (target === "feedback") {
      setAppState("evaluating");
      if (mode === "success") {
        const earnedStars = getAttemptStarReward();
        addStars(earnedStars);
        updateFeedbackMessage(earnedStars, "success");
      } else {
        updateFeedbackMessage(0, "retry");
      }
      updateFeedbackStatus(mode);
      stopCamera();
    }
    if (target === "start") {
      totalStars = 0;
      updateScoreDisplays();
    }
    showScreen(target);
    if (target === "feedback") {
      setAppState(mode);
    }
  });
});

// --- camera / fallback probe ---
let activeStream = null;

const cameraStatus = document.querySelector("#camera-status");
const preview = document.querySelector("#camera-preview");
const fallbackReason = document.querySelector("#fallback-reason");

document.querySelector("#use-webcam-btn")?.addEventListener("click", async () => {
  cameraStatus.textContent = "Requesting camera access…";
  try {
    activeStream = await navigator.mediaDevices.getUserMedia({ video: true });
    preview.srcObject = activeStream;
    cameraStatus.textContent = "Webcam connected successfully! Prepare to move.";
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
    fallbackReason.textContent = "Using local demo feed. No camera access required.";
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
