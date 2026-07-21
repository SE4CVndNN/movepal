"use strict";

// --- existing health check (kept from the starter app) ---
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

// --- clickable flow state machine ---
const screens = document.querySelectorAll("[data-screen]");

function showScreen(name) {
  screens.forEach((section) => {
    section.hidden = section.dataset.screen !== name;
  });
}

document.querySelectorAll("[data-goto]").forEach((button) => {
  button.addEventListener("click", () => showScreen(button.dataset.goto));
});

// --- camera / fallback probe ---
let activeStream = null;

const cameraStatus = document.querySelector("#camera-status");
const preview = document.querySelector("#camera-preview");

document.querySelector("#use-webcam-btn")?.addEventListener("click", async () => {
  cameraStatus.textContent = "Requesting camera access…";
  const fallbackReason = document.querySelector("#fallback-reason");
  try {
    activeStream = await navigator.mediaDevices.getUserMedia({ video: true });
    preview.srcObject = activeStream;
    cameraStatus.textContent = "Webcam connected successfully! Prepare to move.";
    showScreen("camera-live");
  } catch (error) {
    let reason;
    if (error.name === "NotAllowedError") {
      reason = "Camera access was denied. Please enable camera permissions in your browser settings to continue.";
    } else if (error.name === "NotFoundError") {
      reason = "No camera was detected. Please connect a webcam or use the local demo sample.";
    } else {
      reason = "No camera was detected. Please connect a webcam or use the local demo sample.";
    }
    if (fallbackReason) fallbackReason.textContent = reason;
    showScreen("camera-fallback");
  }
});

document.querySelector("#use-fallback-btn")?.addEventListener("click", () => {
  cameraStatus.textContent = "Using local demo feed. No camera access required.";
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
const FALLBACK_FIXTURE_ID = "synthetic_raise_arms_positive_001";

const feedbackMessage = document.querySelector("#feedback-message");
const fallbackError = document.querySelector("#fallback-error");

document.querySelector("#simulate-fallback-btn")?.addEventListener("click", async () => {
  if (fallbackError) fallbackError.textContent = "Checking your pose…";
  try {
    const response = await fetch("/api/movement", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        movement: "raise_both_arms",
        fixture_id: FALLBACK_FIXTURE_ID,
      }),
    });
    const payload = await response.json();
    if (!response.ok) {
      throw new Error(payload.message || "The movement could not be evaluated.");
    }
    if (feedbackMessage) {
      const stars = "⭐".repeat(payload.stars);
      feedbackMessage.textContent = stars
        ? `${payload.feedback} ${stars}`
        : payload.feedback;
    }
    if (fallbackError) fallbackError.textContent = "";
    showScreen("feedback");
  } catch (error) {
    if (fallbackError) {
      fallbackError.textContent = "The application could not be reached.";
    }
  }
});