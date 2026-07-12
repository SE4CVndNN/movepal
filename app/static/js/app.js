"use strict";

const button = document.querySelector("#health-check");
const result = document.querySelector("#health-result");

button?.addEventListener("click", async () => {
  result.textContent = "Checking…";
  try {
    const response = await fetch("/api/health");
    const payload = await response.json();
    result.textContent = response.ok
      ? `Application status: ${payload.status}`
      : "The application returned an error.";
  } catch (_error) {
    result.textContent = "The application could not be reached.";
  }
});
