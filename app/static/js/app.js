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

function updateFeedbackStatus(mode, detailText) {
  const statusBadge = document.querySelector("#feedback-status");
  const detail = document.querySelector("#feedback-detail");
  if (statusBadge) {
    statusBadge.textContent = mode === "retry" ? "Retry" : "Success";
    statusBadge.className = `status-badge status-${mode}`;
  }
  if (detail) {
    detail.textContent =
      detailText ??
      (mode === "retry"
        ? "Try again with a little more space and a stronger pose."
        : "This is a placeholder success result; real evaluation arrives in MP-014.");
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

// Safety net: stop the camera if the user navigates away without clicking "Stop".
window.addEventListener("beforeunload", stopCamera);

// --- MP-014 vertical slice: fixture -> /api/movement -> friendly feedback ---
// Only raise_both_arms has a rule and fixture wired up in this slice; the
// activity buttons for the other moves are disabled in the template.
const SUPPORTED_FALLBACK_FIXTURES = {
  raise_both_arms: "synthetic_raise_arms_positive_001",
};

let selectedActivity = null;

document.querySelectorAll("[data-activity]").forEach((button) => {
  button.addEventListener("click", () => {
    selectedActivity = button.dataset.activity;
  });
});

const fallbackError = document.querySelector("#fallback-error");

document.querySelector("#simulate-fallback-btn")?.addEventListener("click", async () => {
  const fixtureId = SUPPORTED_FALLBACK_FIXTURES[selectedActivity];
  if (!fixtureId) {
    if (fallbackError) {
      fallbackError.textContent =
        "This move isn't part of the demo yet. Please choose Raise both arms.";
    }
    return;
  }
  if (fallbackError) fallbackError.textContent = "Checking your pose…";
  try {
    const response = await fetch("/api/movement", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        movement: selectedActivity,
        fixture_id: fixtureId,
      }),
    });
    const payload = await response.json();
    if (!response.ok) {
      throw new Error(payload.message || "The movement could not be evaluated.");
    }
    const mode = payload.completed ? "success" : "retry";
    if (feedbackMessage) feedbackMessage.textContent = payload.feedback;
    updateFeedbackStatus(
      mode,
      mode === "success"
        ? "This result came from a real, deterministic movement fixture."
        : undefined,
    );
    if (payload.completed && payload.stars > 0) addStars(payload.stars);
    if (fallbackError) fallbackError.textContent = "";
    showScreen("feedback");
    setAppState(mode);
  } catch (error) {
    if (fallbackError) {
      fallbackError.textContent = "The application could not be reached.";
    }
  }
});
