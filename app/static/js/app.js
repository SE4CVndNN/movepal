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
const movementHint = document.querySelector("#movement-hint");
const poseOverlay = document.querySelector("#pose-overlay");

const MOVEMENT_HINTS = {
  raise_both_arms:
    "Raise both arms above your shoulders. Keep your full body visible.",
  side_reach:
    "Reach your arm straight out to the side at shoulder height. Hips and shoulders must stay visible.",
  knee_lift_or_step:
    "Lift the selected knee toward your hip. Keep your full body in frame.",
};

const SKELETON_CONNECTIONS = [
  ["left_shoulder", "right_shoulder"],
  ["left_shoulder", "left_elbow"],
  ["left_elbow", "left_wrist"],
  ["right_shoulder", "right_elbow"],
  ["right_elbow", "right_wrist"],
  ["left_shoulder", "left_hip"],
  ["right_shoulder", "right_hip"],
  ["left_hip", "right_hip"],
  ["left_hip", "left_knee"],
  ["left_knee", "left_ankle"],
  ["right_hip", "right_knee"],
  ["right_knee", "right_ankle"],
];

function updateMovementHint() {
  if (!movementHint) return;
  let hint = MOVEMENT_HINTS[currentActivity] || "";
  if (currentSide && currentActivity !== "raise_both_arms") {
    hint += ` Use your ${currentSide} side.`;
  }
  movementHint.textContent = hint;
}

async function startServerAttempt() {
  if (!currentActivity) return;
  try {
    await fetch("/api/session/start-attempt", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        movement: currentActivity,
        side: currentSide,
      }),
    });
  } catch (_error) {
    // Non-blocking: scoring still works if this fails.
  }
}

function syncOverlaySize() {
  const video = document.querySelector("#camera-preview");
  if (!video || !poseOverlay) return;
  const rect = video.getBoundingClientRect();
  if (!rect.width || !rect.height) return;
  poseOverlay.width = Math.round(rect.width);
  poseOverlay.height = Math.round(rect.height);
}

function drawSkeleton(landmarks) {
  if (!poseOverlay || !landmarks) return;
  syncOverlaySize();
  const ctx = poseOverlay.getContext("2d");
  if (!ctx) return;
  ctx.clearRect(0, 0, poseOverlay.width, poseOverlay.height);

  const minVisibility = 0.5;
  const toPoint = (name) => {
    const lm = landmarks[name];
    if (!lm || lm.visibility < minVisibility) return null;
    return { x: lm.x * poseOverlay.width, y: lm.y * poseOverlay.height };
  };

  ctx.lineWidth = 3;
  ctx.strokeStyle = "#8bd3dd";
  ctx.fillStyle = "#f582ae";

  for (const [fromName, toName] of SKELETON_CONNECTIONS) {
    const from = toPoint(fromName);
    const to = toPoint(toName);
    if (!from || !to) continue;
    ctx.beginPath();
    ctx.moveTo(from.x, from.y);
    ctx.lineTo(to.x, to.y);
    ctx.stroke();
  }

  for (const name of Object.keys(landmarks)) {
    const point = toPoint(name);
    if (!point) continue;
    ctx.beginPath();
    ctx.arc(point.x, point.y, 5, 0, Math.PI * 2);
    ctx.fill();
  }

  // #region agent log
  fetch("http://127.0.0.1:7512/ingest/731cd992-bc96-42cb-9847-963b7cdf60a0", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-Debug-Session-Id": "583a4f",
    },
    body: JSON.stringify({
      sessionId: "583a4f",
      hypothesisId: "H1-H2",
      location: "app.js:drawSkeleton",
      message: "skeleton drawn",
      data: {
        landmarkCount: Object.keys(landmarks).length,
        overlayW: poseOverlay.width,
        overlayH: poseOverlay.height,
      },
      timestamp: Date.now(),
    }),
  }).catch(() => {});
  // #endregion
}

function clearSkeletonOverlay() {
  if (!poseOverlay) return;
  const ctx = poseOverlay.getContext("2d");
  if (ctx) ctx.clearRect(0, 0, poseOverlay.width, poseOverlay.height);
}

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
  button.addEventListener("click", async () => {
    if (button.dataset.activity) {
      currentActivity = button.dataset.activity;
      currentSide = button.dataset.side || null;
      activityToken += 1;
      await startServerAttempt();
      updateMovementHint();
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
      updateMovementHint();
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

function startPeriodicCapture() {
  stopPeriodicCapture();
  captureIntervalId = window.setInterval(() => {
    if (!requestInFlight) captureFrame();
  }, 1000);
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
  clearSkeletonOverlay();
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
    return;
  }

  const { width, height } = getCaptureDimensions(
    video.videoWidth,
    video.videoHeight,
  );
  canvas.width = width;
  canvas.height = height;
  canvas.getContext("2d").drawImage(video, 0, 0, width, height);
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
  if (statusEl) statusEl.textContent = "Evaluating move…";

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

    if (payload.landmarks) {
      drawSkeleton(payload.landmarks);
    } else {
      clearSkeletonOverlay();
    }

    // #region agent log
    fetch("http://127.0.0.1:7512/ingest/731cd992-bc96-42cb-9847-963b7cdf60a0", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-Debug-Session-Id": "583a4f",
      },
      body: JSON.stringify({
        sessionId: "583a4f",
        hypothesisId: "H1-H6",
        location: "app.js:uploadFrame",
        message: "frame response received",
        data: {
          hasLandmarks: Boolean(payload.landmarks),
          completed: payload.completed,
          feedbackCode: payload.feedback_code,
          stars: payload.stars,
          movement: currentActivity,
          side: currentSide,
        },
        timestamp: Date.now(),
      }),
    }).catch(() => {});
    // #endregion

    if ("completed" in payload) {
      if (payload.completed) {
        stopPeriodicCapture();
        if (feedbackMessage) feedbackMessage.textContent = payload.feedback;
        updateFeedbackStatus("success");
        if (payload.stars > 0) addStars(payload.stars);
        showScreen("feedback");
        setAppState("success");
        stopCamera();
        return payload;
      }

      // Live frame evaluated but not yet completed (e.g. hold required or correction needed)
      if (statusEl) {
        statusEl.textContent = payload.feedback || "Adjust position and try again.";
      }
      return payload;
    }

    const messages = {
      success: "Pose detected — hold your position.",
      no_pose: "No pose detected in that frame — try again.",
      low_visibility: "Pose visibility was too low — try again.",
    };
    if (statusEl)
      statusEl.textContent = messages[payload.pose_status] || payload.message;

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

window.addEventListener("resize", syncOverlaySize);
preview?.addEventListener("loadedmetadata", syncOverlaySize);

document.querySelector("#capture-frame-btn")?.addEventListener("click", captureFrame);

document.querySelectorAll(".sample-choice").forEach((button) => {
  button.addEventListener("click", async () => {
    const activity = button.dataset.activity;
    const statusEl = document.querySelector("#sample-upload-status");
    if (!activity) return;

    currentActivity = activity;
    currentSide = button.dataset.side || null;
    activityToken += 1;
    await startServerAttempt();

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
