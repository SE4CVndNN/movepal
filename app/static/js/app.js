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
        "Almost there! Try again with a little more bounce.";
    } else {
      if (amount === 1) {
        feedbackMessage.textContent = "You moved like a star! ⭐";
      } else {
        feedbackMessage.textContent = `Star power! You earned ⭐ ${amount} stars!`;
      }
    }
  }
}

function updateFeedbackStatus(mode, detailText) {
  const detail = document.querySelector("#feedback-detail");
  if (detail) {
    detail.textContent =
      detailText ??
      (mode === "retry"
        ? "Try again with a little more space and a stronger pose."
        : "Nice move! Keep going to collect more stars.");
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
    description: "Reach out to the side with your arm and stretch.",
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
    return side
      ? `Reach out to the ${side} with your arm and stretch.`
      : "Reach out to the side with your arm and stretch.";
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

function showScreen(name) {
  screens.forEach((section) => {
    section.hidden = section.dataset.screen !== name;
  });
  setAppState(SCREEN_TO_STATE[name] ?? "idle");
  if (name === "camera-choice" || name === "camera-fallback") {
    updateMovePreviews();
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

void resetSession();

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

    cameraStatus.textContent =
      "Please allow camera access if the browser asks.";
    try {
      activeStream = await navigator.mediaDevices.getUserMedia({ video: true });
      preview.srcObject = activeStream;
      cameraStatus.textContent = "Camera is on! Get ready to move.";

      activeStream.getVideoTracks()[0].addEventListener("ended", () => {
        if (fallbackReason)
          fallbackReason.textContent =
            "The camera stopped. That is okay. You can still try the demo.";
        stopCamera();
        showScreen("camera-fallback");
      });

      showScreen("camera-live");
      startPeriodicCapture();
      cameraStatus.textContent = "Camera is on! Get ready to move.";
    } catch (error) {
      let reason;
      if (error.name === "NotAllowedError") {
        reason = "Camera permission was not given. You can still try the demo.";
      } else {
        reason = "No camera was found. You can still try the demo.";
      }
      if (fallbackReason) fallbackReason.textContent = reason;
      showScreen("camera-fallback");
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

    if (statusEl) statusEl.textContent = "Running fallback demo…";
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
      if (feedbackMessage) feedbackMessage.textContent = payload.feedback;
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

const MAX_CAPTURE_WIDTH = 640;
const MAX_CAPTURE_HEIGHT = 480;
let requestInFlight = false;
let captureCountdownTimerId = null;
let captureCountdownValue = 0;

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
    right: "synthetic_side_reach_right_negative_001",
  },
  knee_lift_or_step: {
    left: "synthetic_knee_lift_left_positive_001",
    right: "synthetic_knee_lift_right_negative_001",
  },
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

function startPeriodicCapture() {
  stopPeriodicCapture();
  if (!activeStream || !preview || requestInFlight) return;

  captureCountdownValue = 4;
  updateCaptureCountdown(captureCountdownValue);
  captureCountdownTimerId = window.setInterval(() => {
    captureCountdownValue -= 1;
    if (captureCountdownValue <= 0) {
      stopPeriodicCapture();
      showCaptureFlash();
      captureFrame();
    } else {
      updateCaptureCountdown(captureCountdownValue);
    }
  }, 1000);
}

function stopPeriodicCapture() {
  if (captureCountdownTimerId != null) {
    window.clearInterval(captureCountdownTimerId);
    captureCountdownTimerId = null;
  }
  updateCaptureCountdown(0);
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

async function uploadFrame(blob, filename, requestToken, statusEl) {
  if (requestInFlight) return null;
  setBusyRequest(true);

  const status = statusEl || getCurrentStatusElement();
  if (status) status.textContent = "Sending frame…";

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
      const message =
        payload.message ||
        "The server could not process the frame. Please use the no-camera fallback.";
      if (status) {
        status.textContent = message;
      } else {
        showCameraFallback(message);
      }
      return null;
    }

    if ("completed" in payload) {
      stopPeriodicCapture();
      const mode = payload.completed ? "success" : "retry";
      if (feedbackMessage) {
        feedbackMessage.textContent = payload.feedback;
      }
      updateFeedbackStatus(mode);
      if (payload.completed && payload.stars > 0) {
        await refreshSessionSummary();
      } else {
        await refreshSessionSummary();
      }
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

    if (document.body.dataset.appState === "capturing" && activeStream) {
      window.setTimeout(() => {
        if (document.body.dataset.appState === "capturing" && activeStream) {
          startPeriodicCapture();
        }
      }, 900);
    }

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

  if (statusEl) statusEl.textContent = "Uploading photo…";
  const requestToken = activityToken;
  return uploadFrame(file, file.name || "upload.jpg", requestToken, statusEl);
}

document.querySelector("#capture-frame-btn")?.addEventListener("click", () => {
  if (!requestInFlight) {
    startPeriodicCapture();
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
