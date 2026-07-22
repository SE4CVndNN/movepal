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
        : "A deterministic fallback result was returned for this demo move.");
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
let captureIntervalId = null;

const cameraStatus = document.querySelector("#camera-status");
const preview = document.querySelector("#camera-preview");
const fallbackReason = document.querySelector("#fallback-reason");
const captureFrameButton = document.querySelector("#capture-frame-btn");
const sampleChoiceButtons = document.querySelectorAll(".sample-choice");

function setBusyRequest(isBusy) {
  requestInFlight = isBusy;
  if (captureFrameButton) captureFrameButton.disabled = isBusy;
  sampleChoiceButtons.forEach((button) => {
    button.disabled = isBusy;
  });
}

function startPeriodicCapture() {
  stopPeriodicCapture();
  captureIntervalId = window.setInterval(() => {
    if (!requestInFlight) {
      captureFrame();
    }
  }, 8000);
}

function stopPeriodicCapture() {
  if (captureIntervalId != null) {
    window.clearInterval(captureIntervalId);
    captureIntervalId = null;
  }
}

function isSecureContextForCamera() {
  return (
    window.isSecureContext ||
    location.hostname === "localhost" ||
    location.hostname === "127.0.0.1"
  );
}

function isCameraApiSupported() {
  return Boolean(navigator.mediaDevices && navigator.mediaDevices.getUserMedia);
}

document
  .querySelector("#use-webcam-btn")
  ?.addEventListener("click", async () => {
    if (!isSecureContextForCamera()) {
      if (fallbackReason)
        fallbackReason.textContent =
          "Camera access requires a secure connection (HTTPS). Please use the local demo sample instead.";
      showScreen("camera-fallback");
      return;
    }

    if (!isCameraApiSupported()) {
      if (fallbackReason)
        fallbackReason.textContent =
          "This browser does not support camera access. Please use the local demo sample instead.";
      showScreen("camera-fallback");
      return;
    }

    cameraStatus.textContent = "Requesting camera access…";
    try {
      activeStream = await navigator.mediaDevices.getUserMedia({ video: true });
      preview.srcObject = activeStream;
      cameraStatus.textContent =
        "Webcam connected successfully! Prepare to move.";

      activeStream.getVideoTracks()[0].addEventListener("ended", () => {
        if (fallbackReason)
          fallbackReason.textContent =
            "The camera stopped unexpectedly. Please use the local demo sample instead.";
        stopCamera();
        showScreen("camera-fallback");
      });

      showScreen("camera-live");
      startPeriodicCapture();
      cameraStatus.textContent =
        "Webcam connected successfully! Capturing a frame every 8 seconds.";
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
  showScreen("sample-picker");
});

document.querySelector("#stop-camera-btn")?.addEventListener("click", () => {
  stopCamera();
  showScreen("camera-choice");
});

// Safety net: stop the camera if the user navigates away without clicking "Stop".
window.addEventListener("beforeunload", stopCamera);

const MAX_CAPTURE_WIDTH = 640;
const MAX_CAPTURE_HEIGHT = 480;
let requestInFlight = false;
let captureIntervalId = null;

const captureFrameButton = document.querySelector("#capture-frame-btn");
const sampleChoiceButtons = document.querySelectorAll(".sample-choice");
const fallbackError = document.querySelector("#fallback-error");

const SUPPORTED_FALLBACK_FIXTURES = {
  raise_both_arms: "synthetic_raise_arms_positive_001",
};

function setBusyRequest(isBusy) {
  requestInFlight = isBusy;
  if (captureFrameButton) captureFrameButton.disabled = isBusy;
  sampleChoiceButtons.forEach((button) => {
    if (!button.disabled) button.disabled = isBusy;
  });
}

function getCaptureDimensions(sourceWidth, sourceHeight) {
  const sourceRatio = sourceWidth / sourceHeight;
  let width = sourceWidth;
  let height = sourceHeight;

  if (width > MAX_CAPTURE_WIDTH) {
    width = MAX_CAPTURE_WIDTH;
    height = Math.round(width / sourceRatio);
  }
  if (height > MAX_CAPTURE_HEIGHT) {
    height = MAX_CAPTURE_HEIGHT;
    width = Math.round(height * sourceRatio);
  }

  return { width, height };
}

function startPeriodicCapture() {
  stopPeriodicCapture();
  captureIntervalId = window.setInterval(() => {
    if (!requestInFlight) captureFrame();
  }, 8000);
}

function stopPeriodicCapture() {
  if (captureIntervalId != null) {
    window.clearInterval(captureIntervalId);
    captureIntervalId = null;
  }
}

function stopCamera() {
  stopPeriodicCapture();
  activeStream?.getTracks().forEach((track) => track.stop());
  activeStream = null;
  if (preview) preview.srcObject = null;
}

function showCameraFallback(message) {
  if (fallbackReason) fallbackReason.textContent = message;
  stopPeriodicCapture();
  stopCamera();
  showScreen("camera-fallback");
}

function captureFrame() {
  const video = document.querySelector("#camera-preview");
  const canvas = document.querySelector("#capture-canvas");
  const statusEl = document.querySelector("#upload-status");
  if (!video || !canvas) return;

  if (!video.videoWidth || !video.videoHeight) {
    if (statusEl) statusEl.textContent = "Waiting for video preview...";
    return;
  }

  const { width, height } = getCaptureDimensions(
    video.videoWidth,
    video.videoHeight,
  );
  canvas.width = width;
  canvas.height = height;
  canvas.getContext("2d").drawImage(video, 0, 0, width, height);
  canvas.toBlob(
    (blob) => {
      if (blob) uploadFrame(blob, "frame.jpg");
    },
    "image/jpeg",
    0.85,
  );
}

async function uploadFrame(blob, filename) {
  if (requestInFlight) return null;
  setBusyRequest(true);

  const statusEl =
    document.querySelector("#upload-status") ||
    document.querySelector("#sample-upload-status");
  if (statusEl) statusEl.textContent = "Sending frame…";

  const formData = new FormData();
  formData.append("image", blob, filename);

  try {
    const response = await fetch("/api/frame", {
      method: "POST",
      body: formData,
    });
    const payload = await response.json();

    if (!response.ok) {
      showCameraFallback(
        payload.message ||
          "The server could not process the frame. Please use the no-camera fallback.",
      );
      return null;
    }

    const messages = {
      success:
        "Pose detected. Movement evaluation is separate from pose capture.",
      no_pose: "No pose detected in that frame — try again.",
      low_visibility: "Pose visibility was too low — try again.",
    };
    if (statusEl)
      statusEl.textContent = messages[payload.pose_status] || payload.message;

    if (payload.pose_status === "success") {
      if (fallbackReason) {
        fallbackReason.textContent =
          "Pose detected. The approved fallback path is still the best way to complete the demo without a camera.";
      }
    }

    return payload;
  } catch (_error) {
    showCameraFallback(
      "Could not reach the server. Please use the no-camera fallback.",
    );
    return null;
  } finally {
    setBusyRequest(false);
  }
}

document.querySelector("#capture-frame-btn")?.addEventListener("click", () => {
  const video = document.querySelector("#camera-preview");
  const canvas = document.querySelector("#capture-canvas");
  if (!video || !canvas) return;

  const { width, height } = getCaptureDimensions(
    video.videoWidth,
    video.videoHeight,
  );
  canvas.width = width;
  canvas.height = height;
  canvas.getContext("2d").drawImage(video, 0, 0, width, height);
  canvas.toBlob(
    (blob) => {
      if (blob) uploadFrame(blob, "frame.jpg");
    },
    "image/jpeg",
    0.85,
  );
});

document.querySelectorAll(".sample-choice").forEach((button) => {
  button.addEventListener("click", async () => {
    const activity = button.dataset.activity;
    const statusEl = document.querySelector("#sample-upload-status");
    if (!activity) return;

    if (button.disabled) {
      if (fallbackError) {
        fallbackError.textContent =
          "This move is not available in the current fallback demo. Please choose Raise both arms.";
      }
      return;
    }

    const fixtureId = SUPPORTED_FALLBACK_FIXTURES[activity];
    if (!fixtureId) {
      if (fallbackError) {
        fallbackError.textContent =
          "This move is not available in the current fallback demo. Please choose Raise both arms.";
      }
      return;
    }

    if (statusEl) statusEl.textContent = "Running fallback demo…";
    if (fallbackError) fallbackError.textContent = "";

    try {
      const response = await fetch("/api/movement", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ movement: activity, fixture_id: fixtureId }),
      });
      const payload = await response.json();

      if (!response.ok) {
        throw new Error(
          payload.message || "The movement could not be evaluated.",
        );
      }

      const mode = payload.completed ? "success" : "retry";
      if (feedbackMessage) feedbackMessage.textContent = payload.feedback;
      updateFeedbackStatus(
        mode,
        mode === "success"
          ? "This result came from a deterministic movement fixture."
          : undefined,
      );
      if (payload.completed && payload.stars > 0) addStars(payload.stars);
      showScreen("feedback");
      setAppState(mode);
    } catch (_error) {
      if (fallbackError) {
        fallbackError.textContent =
          "The fallback demo could not be reached. Please try again later.";
      }
    }
  });
});
