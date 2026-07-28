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
let hasStartedSession = false;
let feedbackRetryTarget = "fallback-upload";

const scoreCount = document.querySelector("#score-count");
const summaryStarCount = document.querySelector("#summary-star-count");
const feedbackMessage = document.querySelector("#feedback-message");
const selectedMoveAvatar = document.querySelector("#selected-move-avatar");
const selectedMoveTitle = document.querySelector("#selected-move-title");
const selectedMoveDescription = document.querySelector(
  "#selected-move-description",
);
const fallbackMoveAvatar = document.querySelector("#fallback-move-avatar");
const fallbackMoveTitle = document.querySelector("#fallback-move-title");
const fallbackMoveDescription = document.querySelector(
  "#fallback-move-description",
);
const startDemoButton = document.querySelector("#start-demo-btn");
const cameraUploadInput = document.querySelector("#camera-upload-input");
const cameraUploadButton = document.querySelector("#camera-upload-btn");
const cameraUploadStatus = document.querySelector("#camera-upload-status");
const fallbackUploadInput = document.querySelector("#fallback-upload-input");
const fallbackUploadButton = document.querySelector("#fallback-upload-btn");
const fallbackUploadStatus = document.querySelector("#fallback-upload-status");
const cameraInstruction = document.querySelector("#camera-instruction");

async function refreshSessionSummary() {
  try {
    const response = await fetch("/api/session/summary");
    if (!response.ok) return;
    const payload = await response.json();
    totalStars = Number(payload.stars || 0);
    updateScoreDisplays();
  } catch (_error) {
    // Keep the existing client-side value if the summary cannot be refreshed.
  }
}

function updateScoreDisplays() {
  if (scoreCount) scoreCount.textContent = totalStars;
  if (summaryStarCount) summaryStarCount.textContent = totalStars;
}

function updateFeedbackMessage(amount, mode) {
  if (feedbackMessage) {
    if (mode === "retry") {
      feedbackMessage.textContent =
        "Great effort! Check the feedback above and try again with the right pose.";
    } else {
      if (amount === 1) {
        feedbackMessage.textContent = "You moved like a star! ⭐";
      } else {
        feedbackMessage.textContent = `Star power! You earned ⭐ ${amount} stars!`;
      }
    }
  }
}

function renderFeedbackText(payload) {
  if (
    payload.feedback_code === "lift_knee" &&
    currentActivity === "knee_lift_or_step" &&
    currentSide
  ) {
    return `I asked for a ${currentSide} knee lift. Try lifting your ${currentSide} knee up in front like a marching move.`;
  }
  return payload.feedback || "Try again with the right pose.";
}

function updateFeedbackStatus(mode, detailText) {
  const detail = document.querySelector("#feedback-detail");
  const feedbackSecondaryButton = document.querySelector(
    "#feedback-secondary-btn",
  );
  if (detail) {
    detail.textContent =
      detailText ??
      (mode === "retry"
        ? "Check the feedback above and try again with the right pose."
        : "Nice move! Keep going to collect more stars.");
  }
  if (feedbackSecondaryButton) {
    feedbackSecondaryButton.textContent =
      mode === "retry" ? "Try again" : "Upload another photo";
    if (mode === "retry") {
      feedbackSecondaryButton.dataset.goto = feedbackRetryTarget;
    } else {
      feedbackSecondaryButton.dataset.goto = "fallback-upload";
    }
  }
}

const MOVE_PREVIEW = {
  raise_both_arms: {
    title: "Raise both arms",
    description: "Stretch your arms up high and keep them wide.",
    avatar: "/static/images/avatars/raise_both_arms.jpg",
  },
  side_reach: {
    title: "Reach to the side",
    description: "Lift one arm over your head and bend gently to the side.",
    // Use a valid default file; specific left/right variants are applied
    // when a side is selected in `updateMovePreviews()`.
    avatar: "/static/images/avatars/reach-to-the-left.png",
  },
  knee_lift_or_step: {
    title: "Knee lift",
    description: "Lift one knee up and hold it there like a strong superhero.",
    avatar: "/static/images/avatars/knee-lift-left.png",
  },
};

function getMovePreviewData(activity) {
  return MOVE_PREVIEW[activity] || null;
}

function getMoveDescription(activity, side) {
  if (activity === "side_reach") {
    if (side === "left") {
      return "Lift your right arm over your head and bend gently to your left.";
    }
    if (side === "right") {
      return "Lift your left arm over your head and bend gently to your right.";
    }
    return "Lift one arm over your head and bend gently to the side.";
  }
  if (activity === "knee_lift_or_step") {
    return side
      ? `Lift your ${side} knee up and hold it there like a strong superhero.`
      : "Lift one knee up and hold it there like a strong superhero.";
  }
  return MOVE_PREVIEW[activity]?.description || "";
}

function getFallbackFixtureId(activity, side) {
  if (!activity) return null;
  const mapping = SUPPORTED_FALLBACK_FIXTURES[activity];
  if (!mapping) return null;
  if (side) return mapping[side] || mapping.any || null;
  return mapping.any || mapping.left || mapping.right || null;
}

function isFallbackDemoSupported(activity, side) {
  return Boolean(getFallbackFixtureId(activity, side));
}

function updateMovePreviews() {
  const preview = getMovePreviewData(currentActivity);
  const description = getMoveDescription(currentActivity, currentSide);
  const demoSupported = isFallbackDemoSupported(currentActivity, currentSide);
  const demoButton = document.querySelector("#use-fallback-btn");
  const startDemoButton = document.querySelector("#start-demo-btn");

  if (demoButton) {
    demoButton.disabled = !demoSupported;
    demoButton.textContent = demoSupported
      ? "Try the built-in demo"
      : "Built-in demo unavailable";
  }
  if (startDemoButton) {
    startDemoButton.disabled = !demoSupported;
  }

  if (preview) {
    // Hide decorative SVG avatars in the surrounding cards so the
    // move preview image takes clear visual precedence when a move
    // is selected.
    document.querySelectorAll(".avatar").forEach((el) => (el.hidden = true));
    if (selectedMoveTitle) selectedMoveTitle.textContent = preview.title;
    if (selectedMoveDescription) {
      selectedMoveDescription.textContent = description || preview.description;
      selectedMoveDescription.hidden = false;
    }
    if (selectedMoveAvatar) {
      let avatarUrl = preview.avatar;
      if (currentActivity === "side_reach" && currentSide) {
        avatarUrl = `/static/images/avatars/reach-to-the-${currentSide}.png`;
      }
      if (currentActivity === "knee_lift_or_step" && currentSide) {
        avatarUrl =
          currentSide === "left"
            ? "/static/images/avatars/knee-lift-left.png"
            : "/static/images/avatars/knee-lift-right.jpg";
      }
      selectedMoveAvatar.src = avatarUrl;
      selectedMoveAvatar.classList.add("full-photo");
      selectedMoveAvatar.alt = preview.title;
      selectedMoveAvatar.hidden = false;
    }

    if (fallbackMoveTitle) fallbackMoveTitle.textContent = preview.title;
    if (fallbackMoveDescription) {
      fallbackMoveDescription.textContent =
        description || "Start the demo for the move you already picked.";
      fallbackMoveDescription.hidden = false;
    }
    if (fallbackMoveAvatar) {
      let fallbackAvatar = preview.avatar;
      if (currentActivity === "side_reach" && currentSide) {
        fallbackAvatar = `/static/images/avatars/reach-to-the-${currentSide}.png`;
      }
      if (currentActivity === "knee_lift_or_step" && currentSide) {
        fallbackAvatar =
          currentSide === "left"
            ? "/static/images/avatars/knee-lift-left.png"
            : "/static/images/avatars/knee-lift-right.jpg";
      }
      fallbackMoveAvatar.src = fallbackAvatar;
      fallbackMoveAvatar.classList.add("full-photo");
      fallbackMoveAvatar.alt = preview.title;
      fallbackMoveAvatar.hidden = false;
    }
  } else {
    // No preview selected — restore decorative SVG avatars.
    document.querySelectorAll(".avatar").forEach((el) => (el.hidden = false));
    if (selectedMoveTitle) selectedMoveTitle.textContent = "Pick a move first";
    if (selectedMoveDescription) {
      selectedMoveDescription.textContent =
        "After you choose a move, you can use the camera or try the demo.";
      selectedMoveDescription.hidden = false;
    }
    if (selectedMoveAvatar) {
      selectedMoveAvatar.hidden = true;
      selectedMoveAvatar.classList.remove("full-photo");
    }

    if (fallbackMoveTitle) fallbackMoveTitle.textContent = "Your selected move";
    if (fallbackMoveDescription) {
      fallbackMoveDescription.textContent =
        "Start the demo for the move you already picked.";
      fallbackMoveDescription.hidden = false;
    }
    if (fallbackMoveAvatar) {
      fallbackMoveAvatar.hidden = true;
      fallbackMoveAvatar.classList.remove("full-photo");
    }
  }
}

function getAttemptStarReward() {
  return 1;
}

function updateCameraInstruction() {
  if (!cameraInstruction) return;

  if (currentActivity === "side_reach" && currentSide) {
    const overheadArm = currentSide === "left" ? "right" : "left";
    cameraInstruction.textContent =
      `Lift your ${overheadArm} arm overhead and bend to your ${currentSide}.`;
    return;
  }

  if (currentActivity === "knee_lift_or_step" && currentSide) {
    cameraInstruction.textContent = `Lift your ${currentSide} knee for this move.`;
    return;
  }

  cameraInstruction.textContent = "Use the selected move side above.";
}

function addStars(amount) {
  totalStars += amount;
  updateScoreDisplays();
}

async function resetSession() {
  hasStartedSession = false;
  totalStars = 0;
  updateScoreDisplays();
  try {
    await fetch("/api/session/reset", { method: "POST" });
  } catch (_error) {
    // Ignore reset failures and keep the UI responsive.
  }
}

// --- clickable flow state machine ---
const screens = document.querySelectorAll("[data-screen]");

const SCREEN_TO_STATE = {
  start: "idle",
  activity: "idle",
  "camera-choice": "preparing",
  "camera-upload": "preparing",
  "camera-live": "capturing",
  "camera-fallback": "capturing",
  "fallback-upload": "preparing",
  feedback: "evaluating",
  summary: "summary",
};

function clearUploadState() {
  if (cameraUploadInput) cameraUploadInput.value = "";
  if (cameraUploadStatus) cameraUploadStatus.textContent = "";
  if (fallbackUploadInput) fallbackUploadInput.value = "";
  if (fallbackUploadStatus) fallbackUploadStatus.textContent = "";
}

function setAppState(state) {
  document.body.dataset.appState = state;
}

function focusScreenHeading(screen) {
  const heading = screen.querySelector("h2");
  if (!heading) return;
  heading.setAttribute("tabindex", "-1");
  heading.focus({ preventScroll: true });
}

function showScreen(name) {
  if (name !== "camera-live") {
    stopCamera();
  }
  if (name !== "camera-live") {
    clearCapturedFrame();
  }
  screens.forEach((section) => {
    section.hidden = section.dataset.screen !== name;
  });
  const activeScreen = document.querySelector(`[data-screen="${name}"]`);
  if (activeScreen) focusScreenHeading(activeScreen);
  setAppState(SCREEN_TO_STATE[name] ?? "idle");
  if (name === "camera-choice" || name === "camera-fallback") {
    updateMovePreviews();
  }
  if (name === "camera-live") {
    updateCameraInstruction();
  }
  if (name !== "camera-upload" && name !== "fallback-upload") {
    clearUploadState();
  }
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
      updateFeedbackStatus(mode);
      stopCamera();
    }
    if (target === "start") {
      void resetSession();
    }
    if (target === "summary") {
      void refreshSessionSummary();
    }
    if (target === "activity") {
      hasStartedSession = true;
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
const skeletonOverlay = document.querySelector("#skeleton-overlay");
const captureCanvas = document.querySelector("#capture-canvas");
const captureProcessing = document.querySelector("#capture-processing");
const fallbackReason = document.querySelector("#fallback-reason");
const CAMERA_STATES = Object.freeze([
  "idle",
  "loading-model",
  "opening-camera",
  "finding-pose",
  "pose-ready",
  "countdown",
  "captured",
  "processing",
  "feedback",
]);
let cameraState = "idle";
let previewLoopActive = false;
let previewRequestInFlight = false;
let previewTimerId = null;
let stablePoseChecks = 0;
let lastReadyPreviewAt = 0;
let finalCaptureStarted = false;
let cameraSessionId = 0;
let readinessRequestController = null;
let previewRequestController = null;

function transitionCameraState(nextState) {
  if (!CAMERA_STATES.includes(nextState)) return;
  cameraState = nextState;
  document.body.dataset.cameraState = nextState;
  if (captureFrameButton) {
    captureFrameButton.disabled = nextState !== "pose-ready";
  }
}

function setCameraGuidance(message) {
  if (cameraStatus) cameraStatus.textContent = message;
  if (cameraInstruction && cameraState !== "loading-model") {
    cameraInstruction.textContent = message;
  }
}

void resetSession();

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
    stopCamera();
    const requestedSessionId = cameraSessionId;
    clearCapturedFrame();
    finalCaptureStarted = false;
    setBusyRequest(false);
    if (!isSecureContextForCamera()) {
      if (fallbackReason)
        fallbackReason.textContent =
          "The camera is not ready. That is okay. You can still try the demo.";
      showScreen("camera-fallback");
      return;
    }

    if (!isCameraApiSupported()) {
      if (fallbackReason)
        fallbackReason.textContent =
          "This browser cannot use the camera right now. You can still try the demo.";
      showScreen("camera-fallback");
      return;
    }

    transitionCameraState("loading-model");
    cameraStatus.textContent = "Loading the movement checker…";
    try {
      readinessRequestController = new AbortController();
      const readinessResponse = await fetch("/api/pose/readiness", {
        signal: readinessRequestController.signal,
      });
      if (requestedSessionId !== cameraSessionId) return;
      if (!readinessResponse.ok) throw new Error("readiness");
      cameraStatus.textContent =
        "Movement checker is ready. Let’s find your pose.";
      transitionCameraState("opening-camera");
      const requestedStream = await navigator.mediaDevices.getUserMedia({
        video: true,
      });
      if (requestedSessionId !== cameraSessionId) {
        requestedStream.getTracks().forEach((track) => track.stop());
        return;
      }
      activeStream = requestedStream;
      preview.srcObject = requestedStream;
      // Keep the video visible while it starts. Some browsers do not produce
      // metadata or frames for a video whose parent section is still hidden.
      showScreen("camera-live");
      await preview.play();
      await waitForVideoMetadata(preview);
      if (requestedSessionId !== cameraSessionId) {
        stopCamera();
        return;
      }
      updateCameraInstruction();

      requestedStream.getVideoTracks()[0].addEventListener("ended", () => {
        if (requestedSessionId !== cameraSessionId) return;
        if (fallbackReason)
          fallbackReason.textContent =
            "The camera stopped. That is okay. You can still try the demo.";
        stopCamera();
        showScreen("camera-fallback");
      });

      transitionCameraState("finding-pose");
      setCameraGuidance("Move into the center so I can find your pose.");
      startPosePreviewLoop();
    } catch (error) {
      if (
        error.name === "AbortError" ||
        requestedSessionId !== cameraSessionId
      ) {
        return;
      }
      let reason;
      if (error.name === "NotAllowedError") {
        reason = "Camera permission was not given. You can still try the demo.";
      } else {
        reason = "No camera was found. You can still try the demo.";
      }
      if (fallbackReason) fallbackReason.textContent = reason;
      showScreen("camera-fallback");
    } finally {
      if (requestedSessionId === cameraSessionId) {
        readinessRequestController = null;
      }
    }
  });

document.querySelector("#use-fallback-btn")?.addEventListener("click", () => {
  if (!currentActivity) {
    if (fallbackReason)
      fallbackReason.textContent =
        "Pick a move first, then we can try the demo for that move.";
    showScreen("activity");
    return;
  }
  showScreen("camera-fallback");
});

document
  .querySelector("#start-demo-btn")
  ?.addEventListener("click", async () => {
    if (!currentActivity) return;
    const statusEl = document.querySelector("#fallback-error");
    const fixtureId = getFallbackFixtureId(currentActivity, currentSide);

    if (!fixtureId) {
      if (statusEl)
        statusEl.textContent =
          "Built-in demo isn't available for this move and side yet. Upload a photo or choose another move.";
      return;
    }

    if (statusEl) statusEl.textContent = "";
    try {
      const response = await fetch("/api/movement", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          movement: currentActivity,
          side: currentSide,
          fixture_id: fixtureId,
        }),
      });
      const payload = await response.json();

      if (!response.ok) {
        throw new Error(
          payload.message || "The movement could not be evaluated.",
        );
      }

      const mode = payload.completed ? "success" : "retry";
      if (feedbackMessage)
        feedbackMessage.textContent = renderFeedbackText(payload);
      updateFeedbackStatus(
        mode,
        mode === "success"
          ? "This result came from a deterministic movement fixture."
          : undefined,
      );
      await refreshSessionSummary();
      showScreen("feedback");
      setAppState(mode);
    } catch (_error) {
      if (statusEl)
        statusEl.textContent =
          "The fallback demo could not be reached. Please try again later.";
    }
  });

document.querySelector("#stop-camera-btn")?.addEventListener("click", () => {
  stopCamera();
  showScreen("camera-choice");
});

// Safety net: stop the camera if the user navigates away without clicking "Stop".
window.addEventListener("beforeunload", stopCamera);
window.addEventListener("pagehide", stopCamera);
document.addEventListener("visibilitychange", () => {
  // Some browsers briefly mark the page hidden while their native camera
  // permission prompt is open. Do not cancel readiness/getUserMedia at that
  // point or the camera can never open. Once a real stream exists, hiding the
  // page still releases it immediately.
  if (document.hidden && activeStream !== null) {
    stopCamera();
    showScreen("camera-choice");
    if (cameraStatus) {
      cameraStatus.textContent =
        "The camera was turned off when this page was hidden.";
    }
  }
});

const MAX_CAPTURE_WIDTH = 640;
const MAX_CAPTURE_HEIGHT = 480;
const FRAME_REQUEST_TIMEOUT_MS = 15000;
let requestInFlight = false;
let captureCountdownTimerId = null;
let captureCountdownValue = 0;
const PREVIEW_INTERVAL_MS = 650;
const PREVIEW_MAX_WIDTH = 320;
const REQUIRED_STABLE_POSE_CHECKS = 2;

const captureFrameButton = document.querySelector("#capture-frame-btn");
const sampleChoiceButtons = document.querySelectorAll(".sample-choice");
const fallbackError = document.querySelector("#fallback-error");
const captureCountdown = document.querySelector("#capture-countdown");
const captureFlash = document.querySelector("#capture-flash");

const SUPPORTED_FALLBACK_FIXTURES = {
  raise_both_arms: {
    left: "synthetic_raise_arms_positive_001",
    right: "synthetic_raise_arms_positive_001",
  },
  side_reach: {
    left: "synthetic_side_reach_left_positive_001",
    right: "synthetic_side_reach_right_positive_001",
  },
  knee_lift_or_step: {
    left: "synthetic_knee_lift_left_positive_001",
    right: "synthetic_knee_lift_right_positive_001",
  },
};

function setBusyRequest(isBusy) {
  requestInFlight = isBusy;
  if (captureFrameButton) captureFrameButton.disabled = isBusy;
  if (cameraUploadButton) cameraUploadButton.disabled = isBusy;
  if (fallbackUploadButton) fallbackUploadButton.disabled = isBusy;
  sampleChoiceButtons.forEach((button) => {
    button.disabled = isBusy;
  });
}

function setUploadStatus(statusEl, message) {
  if (statusEl) statusEl.textContent = message;
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

function updateCaptureCountdown(value) {
  if (!captureCountdown) return;
  if (value > 0) {
    captureCountdown.hidden = false;
    captureCountdown.textContent = value === 1 ? "📸 Cheese!" : `⏰ ${value}`;
    captureCountdown.classList.remove("is-pulse");
    void captureCountdown.offsetWidth;
    captureCountdown.classList.add("is-pulse");
  } else {
    captureCountdown.hidden = true;
    captureCountdown.textContent = "";
    captureCountdown.classList.remove("is-pulse");
  }
}

function showCaptureFlash() {
  if (!captureFlash) return;
  captureFlash.classList.remove("is-visible");
  void captureFlash.offsetWidth;
  captureFlash.classList.add("is-visible");
  window.setTimeout(() => captureFlash.classList.remove("is-visible"), 380);
}

function waitForVideoMetadata(video) {
  if (video.videoWidth > 0 && video.videoHeight > 0) return Promise.resolve();
  return new Promise((resolve, reject) => {
    const timeoutId = window.setTimeout(
      () => reject(new Error("Video metadata timed out.")),
      8000,
    );
    video.addEventListener(
      "loadedmetadata",
      () => {
        window.clearTimeout(timeoutId);
        if (video.videoWidth > 0 && video.videoHeight > 0) resolve();
        else reject(new Error("Video dimensions are unavailable."));
      },
      { once: true },
    );
  });
}

function clearSkeletonOverlay() {
  if (!skeletonOverlay) return;
  const context = skeletonOverlay.getContext("2d");
  context?.clearRect(0, 0, skeletonOverlay.width, skeletonOverlay.height);
}

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

function drawSkeleton(displayLandmarks) {
  if (!skeletonOverlay || !preview.videoWidth || !preview.videoHeight) {
    return false;
  }
  skeletonOverlay.width = preview.videoWidth;
  skeletonOverlay.height = preview.videoHeight;
  const context = skeletonOverlay.getContext("2d");
  if (!context) return false;
  context.clearRect(0, 0, skeletonOverlay.width, skeletonOverlay.height);
  context.lineWidth = Math.max(5, skeletonOverlay.width / 120);
  context.lineCap = "round";
  context.strokeStyle = "#8cf4ff";
  for (const [firstName, secondName] of SKELETON_CONNECTIONS) {
    const first = displayLandmarks[firstName];
    const second = displayLandmarks[secondName];
    if (!first || !second || first.visibility < 0.5 || second.visibility < 0.5)
      continue;
    context.beginPath();
    context.moveTo(first.x * skeletonOverlay.width, first.y * skeletonOverlay.height);
    context.lineTo(second.x * skeletonOverlay.width, second.y * skeletonOverlay.height);
    context.stroke();
  }
  context.fillStyle = "#ffe56b";
  for (const landmark of Object.values(displayLandmarks)) {
    if (landmark.visibility < 0.5) continue;
    context.beginPath();
    context.arc(
      landmark.x * skeletonOverlay.width,
      landmark.y * skeletonOverlay.height,
      Math.max(6, skeletonOverlay.width / 90),
      0,
      Math.PI * 2,
    );
    context.fill();
  }
  return Object.keys(displayLandmarks).length > 0;
}

function stopPosePreviewLoop() {
  previewLoopActive = false;
  if (previewTimerId != null) {
    window.clearTimeout(previewTimerId);
    previewTimerId = null;
  }
  stablePoseChecks = 0;
  lastReadyPreviewAt = 0;
}

function startPosePreviewLoop() {
  stopPosePreviewLoop();
  previewLoopActive = true;
  void analyzePreviewFrame();
}

async function analyzePreviewFrame() {
  if (
    !previewLoopActive ||
    previewRequestInFlight ||
    !activeStream ||
    !preview.videoWidth ||
    !preview.videoHeight
  )
    return;
  const previewSessionId = cameraSessionId;
  let requestController = null;
  previewRequestInFlight = true;
  const previewCanvas = document.createElement("canvas");
  const scale = Math.min(1, PREVIEW_MAX_WIDTH / preview.videoWidth);
  previewCanvas.width = Math.max(1, Math.round(preview.videoWidth * scale));
  previewCanvas.height = Math.max(1, Math.round(preview.videoHeight * scale));
  previewCanvas
    .getContext("2d")
    ?.drawImage(preview, 0, 0, previewCanvas.width, previewCanvas.height);

  try {
    const blob = await new Promise((resolve) =>
      previewCanvas.toBlob(resolve, "image/jpeg", 0.72),
    );
    if (!blob || !previewLoopActive) return;
    const formData = new FormData();
    formData.append("image", blob, "preview.jpg");
    formData.append("movement", currentActivity);
    if (currentSide) formData.append("side", currentSide);
    requestController = new AbortController();
    previewRequestController = requestController;
    const response = await fetch("/api/pose/preview", {
      method: "POST",
      body: formData,
      signal: requestController.signal,
    });
    const payload = await response.json();
    if (!previewLoopActive || previewSessionId !== cameraSessionId) return;
    const skeletonDrawn =
      response.ok &&
      payload.pose_status === "success" &&
      drawSkeleton(payload.display_landmarks || {});
    const ready = skeletonDrawn && payload.ready_for_capture === true;
    setCameraGuidance(payload.guidance || "Let’s find your pose.");
    if (ready) {
      stablePoseChecks += 1;
      lastReadyPreviewAt = Date.now();
      if (
        stablePoseChecks >= REQUIRED_STABLE_POSE_CHECKS &&
        cameraState !== "countdown"
      ) {
        transitionCameraState("pose-ready");
        startCountdown();
      }
    } else if (cameraState === "countdown") {
      // Readiness is latched once the skeleton has been stable long enough to
      // start the countdown. A single noisy preview must not cancel the photo.
      setCameraGuidance("Hold that pose until the picture is taken.");
    } else {
      stablePoseChecks = 0;
      lastReadyPreviewAt = 0;
      if (!skeletonDrawn) clearSkeletonOverlay();
      transitionCameraState("finding-pose");
    }
  } catch (error) {
    if (
      error.name === "AbortError" ||
      !previewLoopActive ||
      previewSessionId !== cameraSessionId
    )
      return;
    if (cameraState === "countdown") {
      setCameraGuidance("Hold that pose until the picture is taken.");
      return;
    }
    stablePoseChecks = 0;
    lastReadyPreviewAt = 0;
    clearSkeletonOverlay();
    cancelCountdown();
    transitionCameraState("finding-pose");
    setCameraGuidance(
      "I lost your pose for a moment. Hold still and try again.",
    );
  } finally {
    if (previewRequestController === requestController) {
      previewRequestController = null;
    }
    if (previewSessionId === cameraSessionId) {
      previewRequestInFlight = false;
      if (previewLoopActive) {
        previewTimerId = window.setTimeout(
          analyzePreviewFrame,
          PREVIEW_INTERVAL_MS,
        );
      }
    }
  }
}

function startCountdown() {
  if (
    cameraState === "countdown" ||
    !activeStream ||
    !previewLoopActive ||
    requestInFlight
  )
    return;
  cancelCountdown();
  transitionCameraState("countdown");
  setCameraGuidance("Great! Hold that pose.");

  captureCountdownValue = 3;
  updateCaptureCountdown(captureCountdownValue);
  captureCountdownTimerId = window.setInterval(() => {
    captureCountdownValue -= 1;
    if (captureCountdownValue <= 0) {
      cancelCountdown();
      showCaptureFlash();
      captureFrame();
    } else {
      updateCaptureCountdown(captureCountdownValue);
    }
  }, 1000);
}

function cancelCountdown() {
  if (captureCountdownTimerId != null) {
    window.clearInterval(captureCountdownTimerId);
    captureCountdownTimerId = null;
  }
  updateCaptureCountdown(0);
}

function stopCamera() {
  cameraSessionId += 1;
  readinessRequestController?.abort();
  readinessRequestController = null;
  previewRequestController?.abort();
  previewRequestController = null;
  cancelCountdown();
  stopPosePreviewLoop();
  clearSkeletonOverlay();
  activeStream?.getTracks().forEach((track) => track.stop());
  activeStream = null;
  previewRequestInFlight = false;
  if (preview) {
    preview.pause();
    preview.srcObject = null;
  }
  if (cameraState !== "feedback") transitionCameraState("idle");
}

function showCapturedFrame() {
  if (preview) preview.hidden = true;
  if (captureCanvas) captureCanvas.hidden = false;
  if (captureProcessing) captureProcessing.hidden = false;
}

function clearCapturedFrame() {
  if (captureProcessing) captureProcessing.hidden = true;
  if (captureCanvas) {
    const context = captureCanvas.getContext("2d");
    context?.clearRect(0, 0, captureCanvas.width, captureCanvas.height);
    captureCanvas.hidden = true;
  }
  if (preview) preview.hidden = false;
}

function showCameraFallback(message) {
  if (fallbackReason) fallbackReason.textContent = message;
  stopCamera();
  showScreen("camera-fallback");
}

function getCurrentStatusElement() {
  const fallbackStatus = document.querySelector("#fallback-error");
  const uploadStatus = document.querySelector("#upload-status");
  const cameraUploadStatus = document.querySelector("#camera-upload-status");
  const fallbackUploadStatus = document.querySelector(
    "#fallback-upload-status",
  );

  const fallbackScreen = fallbackStatus?.closest("[data-screen]");
  if (fallbackStatus && fallbackScreen && !fallbackScreen.hidden) {
    return fallbackStatus;
  }

  const uploadScreen = uploadStatus?.closest("[data-screen]");
  if (uploadStatus && uploadScreen && !uploadScreen.hidden) {
    return uploadStatus;
  }

  const cameraUploadScreen = cameraUploadStatus?.closest("[data-screen]");
  if (cameraUploadStatus && cameraUploadScreen && !cameraUploadScreen.hidden) {
    return cameraUploadStatus;
  }

  const fallbackUploadScreen = fallbackUploadStatus?.closest("[data-screen]");
  if (
    fallbackUploadStatus &&
    fallbackUploadScreen &&
    !fallbackUploadScreen.hidden
  ) {
    return fallbackUploadStatus;
  }

  return (
    cameraUploadStatus || uploadStatus || fallbackUploadStatus || fallbackStatus
  );
}

function captureFrame() {
  const video = document.querySelector("#camera-preview");
  const canvas = captureCanvas;
  const statusEl = getCurrentStatusElement();
  if (!video || !canvas || finalCaptureStarted) return;

  if (!video.videoWidth || !video.videoHeight) {
    if (statusEl) statusEl.textContent = "Waiting for video preview...";
    return;
  }
  finalCaptureStarted = true;
  transitionCameraState("captured");
  stopPosePreviewLoop();

  // A retry starts from the camera choice so a fresh, short-lived stream is
  // requested. The previous stream is never kept alive between attempts.
  feedbackRetryTarget = "camera-choice";
  const { width, height } = getCaptureDimensions(
    video.videoWidth,
    video.videoHeight,
  );
  canvas.width = width;
  canvas.height = height;
  const ctx = canvas.getContext("2d");
  if (ctx) {
    ctx.drawImage(video, 0, 0, width, height);
  }
  showCapturedFrame();
  const requestToken = activityToken;
  // The pixels are now copied into the canvas, so release the camera before
  // encoding or uploading the image. This keeps camera access limited to the
  // single capture instead of the rest of the game session.
  stopCamera();
  canvas.toBlob(
    (blob) => {
      if (blob) {
        transitionCameraState("processing");
        uploadFrame(blob, "frame.jpg", requestToken);
      } else {
        if (statusEl)
          statusEl.textContent =
            "The picture could not be prepared. Please try the camera again.";
        showScreen("camera-choice");
      }
    },
    "image/jpeg",
    0.85,
  );
}

async function handleFrameEvaluationResult(payload, requestToken) {
  if (requestToken !== undefined && requestToken !== activityToken) return null;
  stopCamera();
  transitionCameraState("feedback");
  feedbackRetryTarget = "camera-choice";
  const completed = payload.completed === true;
  const poseMessages = {
    no_pose:
      "I could not see your pose. Step back, face the camera, and try again.",
    low_visibility:
      "I could not see the movement clearly. Improve the lighting and try again.",
    error:
      "The movement checker needs a quick reset. Please try again or use the no-camera option.",
  };
  const mode = completed ? "success" : "retry";
  if (feedbackMessage) {
    feedbackMessage.textContent =
      payload.feedback ||
      poseMessages[payload.pose_status] ||
      "Nice try! Check the movement tip and try again.";
  }
  updateFeedbackStatus(mode);
  await refreshSessionSummary();
  showScreen("feedback");
  setAppState(mode);
  return payload;
}

async function uploadFrame(blob, filename, requestToken, statusEl) {
  if (requestInFlight) return null;
  setBusyRequest(true);

  const status = statusEl || getCurrentStatusElement();
  if (status) setUploadStatus(status, "Checking your pose…");
  updateCameraInstruction();
  const formData = new FormData();
  formData.append("image", blob, filename);
  if (currentActivity) formData.append("movement", currentActivity);
  if (currentSide) formData.append("side", currentSide);

  const progressTimeout = window.setTimeout(() => {
    if (status) {
      status.textContent = "Still checking your pose…";
    }
  }, 2500);
  const requestController = new AbortController();
  const requestTimeout = window.setTimeout(
    () => requestController.abort(),
    FRAME_REQUEST_TIMEOUT_MS,
  );

  try {
    const response = await fetch("/api/frame", {
      method: "POST",
      body: formData,
      signal: requestController.signal,
    });
    const payload = await response.json();

    if (requestToken !== undefined && requestToken !== activityToken) {
      return null; // stale: user already switched activities
    }

    if (!response.ok) {
      payload.completed = false;
      payload.pose_status = payload.pose_status || "error";
    }

    if ("completed" in payload) {
      return handleFrameEvaluationResult(payload, requestToken);
    }

    const messages = {
      success: "Pose detected — hold your position.",
      no_pose: "No pose detected in that frame — try again.",
      low_visibility: "Pose visibility was too low — try again.",
    };
    payload.completed = false;
    payload.feedback = messages[payload.pose_status] || payload.message;
    return handleFrameEvaluationResult(payload, requestToken);
  } catch (error) {
    if (requestToken !== undefined && requestToken !== activityToken) {
      return null;
    }
    const message =
      error.name === "AbortError"
        ? "Pose checking took too long. Please try again or use the no-camera fallback."
        : "Frame upload failed. Please use the no-camera fallback or try again later.";
    return handleFrameEvaluationResult(
      {
        completed: false,
        pose_status: "error",
        feedback: message,
      },
      requestToken,
    );
  } finally {
    window.clearTimeout(progressTimeout);
    window.clearTimeout(requestTimeout);
    setBusyRequest(false);
  }
}

async function uploadSelectedPhoto(file, statusEl) {
  if (!currentActivity) {
    if (statusEl)
      statusEl.textContent =
        "Pick a move first, then upload a photo for that move.";
    return null;
  }
  if (!file) {
    if (statusEl) statusEl.textContent = "Choose a photo first.";
    return null;
  }

  if (statusEl)
    setUploadStatus(statusEl, "Uploading photo… This may take a few seconds.");
  feedbackRetryTarget = "camera-upload";
  const requestToken = activityToken;
  return uploadFrame(file, file.name || "upload.jpg", requestToken, statusEl);
}

document.querySelector("#capture-frame-btn")?.addEventListener("click", () => {
  if (!requestInFlight && cameraState === "pose-ready") {
    startCountdown();
  }
});

document.querySelector("#use-upload-btn")?.addEventListener("click", () => {
  if (!currentActivity) {
    if (cameraStatus)
      cameraStatus.textContent =
        "Pick a move first, then upload a photo for that move.";
    showScreen("activity");
    return;
  }
  showScreen("camera-upload");
});

document
  .querySelector("#show-fallback-upload-btn")
  ?.addEventListener("click", () => {
    feedbackRetryTarget = "fallback-upload";
    showScreen("fallback-upload");
  });

document
  .querySelector("#camera-upload-btn")
  ?.addEventListener("click", async () => {
    if (cameraUploadInput?.files?.length) {
      await uploadSelectedPhoto(cameraUploadInput.files[0], cameraUploadStatus);
    } else if (cameraUploadStatus) {
      cameraUploadStatus.textContent = "Choose a photo first.";
    }
  });

document
  .querySelector("#fallback-upload-btn")
  ?.addEventListener("click", async () => {
    if (fallbackUploadInput?.files?.length) {
      await uploadSelectedPhoto(
        fallbackUploadInput.files[0],
        fallbackUploadStatus,
      );
    } else if (fallbackUploadStatus) {
      fallbackUploadStatus.textContent = "Choose a photo first.";
    }
  });

cameraUploadInput?.addEventListener("change", async () => {
  if (cameraUploadInput.files?.length) {
    await uploadSelectedPhoto(cameraUploadInput.files[0], cameraUploadStatus);
  }
});

fallbackUploadInput?.addEventListener("change", async () => {
  if (fallbackUploadInput.files?.length) {
    await uploadSelectedPhoto(
      fallbackUploadInput.files[0],
      fallbackUploadStatus,
    );
  }
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

    const fixtureId = getFallbackFixtureId(
      activity,
      button.dataset.side || null,
    );
    if (!fixtureId) {
      if (fallbackError) {
        fallbackError.textContent =
          "This move is not available in the current fallback demo. Please choose Raise both arms or use upload instead.";
      }
      return;
    }

    if (statusEl) statusEl.textContent = "";
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
      if (feedbackMessage)
        feedbackMessage.textContent = renderFeedbackText(payload);
      updateFeedbackStatus(
        mode,
        mode === "success"
          ? "This result came from a deterministic movement fixture."
          : undefined,
      );
      await refreshSessionSummary();
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
