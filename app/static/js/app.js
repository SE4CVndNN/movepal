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
let currentActivity = null;
let currentSide = null;
let activityToken = 0;

const scoreCount = document.querySelector("#score-count");
const summaryStarCount = document.querySelector("#summary-star-count");
const feedbackMessage = document.querySelector("#feedback-message");

function updateScoreDisplays() {
  if (scoreCount) scoreCount.textContent = totalStars;
  if (summaryStarCount) summaryStarCount.textContent = totalStars;
}

function updateFeedbackMessage(amount, mode) {
  if (feedbackMessage) {
    if (mode === "retry") {
      feedbackMessage.textContent =
        "Keep going! Adjust your position and try that movement again.";
    } else {
      if (amount === 1) {
        feedbackMessage.textContent = "Awesome job! You've earned ⭐ 1 Star!";
      } else {
        feedbackMessage.textContent = `Awesome job! You've earned ⭐ ${amount} Stars!`;
      }
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

function showRetryCameraButton(visible) {
  const retryButton = document.querySelector("#retry-camera-btn");
  if (retryButton) retryButton.hidden = !visible;
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

const LEAVES_CAMERA_TARGETS = new Set([
  "start",
  "activity",
  "camera-choice",
  "sample-picker",
  "summary",
]);

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
    if (button.dataset.activity) {
      currentActivity = button.dataset.activity;
      currentSide = button.dataset.side || null;
      activityToken += 1;
    }
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
    if (target !== "feedback") {
      showRetryCameraButton(false);
    }
    // Any exit from the camera flow must release the stream; only the
    // "Try again" hop back to camera-live is allowed to keep it open.
    if (LEAVES_CAMERA_TARGETS.has(target)) {
      stopCamera();
    }
    showScreen(target);
    if (target === "feedback") {
      setAppState(mode);
    }
    if (target === "camera-live") {
      startPeriodicCapture();
    }
  });
});

// --- camera / fallback probe ---
let activeStream = null;

const cameraStatus = document.querySelector("#camera-status");
const preview = document.querySelector("#camera-preview");
const fallbackReason = document.querySelector("#fallback-reason");

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
        "Webcam connected successfully! Prepare to move.";
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
const captureCountdown = document.querySelector("#capture-countdown");
const captureFlash = document.querySelector("#capture-flash");

const SUPPORTED_FALLBACK_FIXTURES = {
  raise_both_arms: "synthetic_raise_arms_positive_001",
  side_reach: "synthetic_side_reach_left_positive_001",
  knee_lift_or_step: "synthetic_knee_lift_left_positive_001",
};

function setBusyRequest(isBusy) {
  requestInFlight = isBusy;
  if (captureFrameButton) captureFrameButton.disabled = isBusy;
  sampleChoiceButtons.forEach((button) => {
    button.disabled = isBusy;
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

// The user gets a visible "Get ready… 3, 2, 1" before the shutter fires, so
// they know exactly which instant is being judged. The first two seconds read
// as "Get ready…"; the last three count down as large numerals.
const COUNTDOWN_SECONDS = 5;
const COUNTDOWN_NUMERAL_FROM = 3;
const FLASH_DURATION_MS = 180;
let flashTimeoutId = null;

function renderCountdown(text, isCounting) {
  if (!captureCountdown) return;
  captureCountdown.textContent = text;
  captureCountdown.classList.toggle("is-counting", Boolean(isCounting));
}

function clearShutterFlash() {
  if (flashTimeoutId != null) {
    window.clearTimeout(flashTimeoutId);
    flashTimeoutId = null;
  }
  captureFlash?.classList.remove("is-flashing");
}

function flashShutter() {
  if (!captureFlash) return;
  clearShutterFlash();
  // Force a reflow so a back-to-back capture restarts the animation.
  void captureFlash.offsetWidth;
  captureFlash.classList.add("is-flashing");
  // A timer, not `animationend`: browsers suspend CSS animations in
  // backgrounded tabs, and a never-firing animationend would leave the white
  // overlay covering the preview for good.
  flashTimeoutId = window.setTimeout(clearShutterFlash, FLASH_DURATION_MS + 60);
}

function startPeriodicCapture() {
  stopPeriodicCapture();

  let remaining = COUNTDOWN_SECONDS;
  const tick = () => {
    if (remaining > COUNTDOWN_NUMERAL_FROM) {
      renderCountdown("Get ready…", false);
    } else if (remaining > 0) {
      renderCountdown(String(remaining), true);
    } else {
      stopPeriodicCapture();
      flashShutter();
      captureFrame();
      return;
    }
    remaining -= 1;
  };

  tick(); // show "Get ready…" immediately instead of a silent first second
  captureIntervalId = window.setInterval(tick, 1000);
}

function stopPeriodicCapture() {
  if (captureIntervalId != null) {
    window.clearInterval(captureIntervalId);
    captureIntervalId = null;
  }
  clearShutterFlash();
  renderCountdown("", false);
}

function stopCamera() {
  stopPeriodicCapture();
  activeStream?.getTracks().forEach((track) => track.stop());
  activeStream = null;
  if (preview) preview.srcObject = null;
}

function showCameraFallback(message) {
  if (fallbackReason) fallbackReason.textContent = message;
  stopCamera();
  showScreen("camera-fallback");
}

function getCurrentStatusElement() {
  const sampleStatus = document.querySelector("#sample-upload-status");
  const uploadStatus = document.querySelector("#upload-status");

  const sampleScreen = sampleStatus?.closest("[data-screen]");
  if (sampleStatus && sampleScreen && !sampleScreen.hidden) {
    return sampleStatus;
  }

  const uploadScreen = uploadStatus?.closest("[data-screen]");
  if (uploadStatus && uploadScreen && !uploadScreen.hidden) {
    return uploadStatus;
  }

  return sampleStatus || uploadStatus;
}

function captureFrame() {
  const video = document.querySelector("#camera-preview");
  const canvas = document.querySelector("#capture-canvas");
  const statusEl = getCurrentStatusElement();
  if (!video || !canvas) return;

  if (!video.videoWidth || !video.videoHeight) {
    if (statusEl) statusEl.textContent = "Waiting for video preview...";
    // No periodic tick backs us up any more, so restart the countdown rather
    // than leaving the user staring at a preview that never captures.
    startPeriodicCapture();
    return;
  }

  const { width, height } = getCaptureDimensions(
    video.videoWidth,
    video.videoHeight,
  );
  canvas.width = width;
  canvas.height = height;
  canvas.getContext("2d").drawImage(video, 0, 0, width, height);
  renderCountdown("Checking your pose…", false);

  const requestToken = activityToken;
  canvas.toBlob(
    (blob) => {
      if (blob) uploadFrame(blob, "frame.jpg", requestToken);
    },
    "image/jpeg",
    0.85,
  );
}

async function uploadFrame(blob, filename, requestToken) {
  if (requestInFlight) return null;
  setBusyRequest(true);

  const statusEl = getCurrentStatusElement();
  if (statusEl) statusEl.textContent = "Sending frame…";

  const formData = new FormData();
  formData.append("image", blob, filename);
  if (currentActivity) formData.append("movement", currentActivity);
  if (currentSide) formData.append("side", currentSide);

  try {
    const response = await fetch("/api/frame", {
      method: "POST",
      body: formData,
    });
    const payload = await response.json();

    if (requestToken !== undefined && requestToken !== activityToken) {
      return null; // stale: user already switched activities
    }

    if (!response.ok) {
      showCameraFallback(
        payload.message ||
          "The server could not process the frame. Please use the no-camera fallback.",
      );
      return null;
    }

    if ("completed" in payload) {
      stopPeriodicCapture();
      const mode = payload.completed ? "success" : "retry";
      if (feedbackMessage) feedbackMessage.textContent = payload.feedback;
      updateFeedbackStatus(
        mode,
        mode === "success"
          ? "This result came from your live camera frame."
          : undefined,
      );
      if (payload.completed && payload.stars > 0) addStars(payload.stars);
      // Keep the stream open so "Try again" can restart the countdown without
      // a second permission prompt; leaving the flow stops it (see data-goto).
      showRetryCameraButton(mode === "retry" && Boolean(activeStream));
      showScreen("feedback");
      setAppState(mode);
      return payload;
    }

    const messages = {
      success: "Pose detected — hold your position.",
      no_pose: "No pose detected in that frame — try again.",
      low_visibility: "Pose visibility was too low — try again.",
    };
    if (statusEl)
      statusEl.textContent = messages[payload.pose_status] || payload.message;

    // Pose detection failed, so there is no verdict to show. The old 8s poll
    // would have retried on its own; the countdown is one-shot, so restart it
    // rather than leaving the user on a preview that never captures again.
    startPeriodicCapture();

    return payload;
  } catch (_error) {
    if (requestToken !== undefined && requestToken !== activityToken) {
      return null;
    }
    showCameraFallback(
      "Frame upload failed. Please use the no-camera fallback or try again later.",
    );
    return null;
  } finally {
    setBusyRequest(false);
  }
}

// "Capture Now" skips the remaining countdown rather than queueing a second one.
captureFrameButton?.addEventListener("click", () => {
  stopPeriodicCapture();
  flashShutter();
  captureFrame();
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

    const requestToken = activityToken;

    try {
      const response = await fetch("/api/movement", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          movement: activity,
          side: button.dataset.side || null,
          fixture_id: fixtureId,
        }),
      });
      const payload = await response.json();

      if (requestToken !== activityToken) return; // stale: activity changed

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
