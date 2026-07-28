# MovePal privacy and data handling

MovePal is a local Sprint 1 prototype for playful movement practice. It is
not a medical, diagnostic, rehabilitation, or treatment product. The MVP does
not need child data, accounts, names, email addresses, or raw recordings.

## What the MVP processes

- A user may explicitly choose a live camera capture or select a JPG/PNG
  photo. The browser requests camera permission only after the user selects
  **Use the camera**.
- A short-lived preview frame may be sent while the camera screen is open so
  the app can tell the user whether the selected body parts are visible.
- The server derives pose landmarks in memory to return game feedback and a
  score. The browser may draw a transient skeleton overlay from those points.
- The included test fixtures contain synthetic or privacy-reviewed derived
  landmark values, not raw participant media.

## What the MVP stores and retains

- Camera frames and uploaded image bytes are written to a private temporary
  file only while the pose adapter reads them. The file is deleted in a
  `finally` block before the request finishes, including when processing
  fails.
- The browser clears the capture canvas, skeleton overlay, and camera stream
  when the user leaves the camera flow. The app does not use `localStorage` or
  `sessionStorage` for frames, landmarks, names, or secrets.
- The current game session uses a signed browser cookie with only aggregate,
  non-identifying counters: attempted movements, completed movements, and
  stars. It is not encrypted, so it must never contain personal or sensitive
  data. Clearing browser cookies ends the session.
- The MVP has no user accounts, database, server-side session history,
  historical analytics, or deletion-request workflow because it stores no
  identity-linked activity history.

## Logging and error handling

Normal logs contain operational timing and safe route-level failure context;
they must not include image bytes, uploaded filenames, raw landmarks, names,
or secrets. Unexpected server failures are logged for diagnosis and return a
generic response to the browser without a traceback or internal file path.

## User controls and safety notices

The footer disclaimer is visible on every screen, including during camera use:
“MovePal is a playful prototype, not a medical or diagnostic tool.” The camera
screen also says that the picture is used only for the game and that the camera
turns off automatically after the capture. Users can cancel camera access in
the app or revoke permission through their browser settings.

## Scope and future deployment

This local MVP does not claim transport encryption, production access controls,
or cloud-storage protections because it has no production deployment or cloud
backend. Any future deployment, recording feature, account system, or
analytics feature requires a new privacy review, retention policy, security
design, consent decision, and updated user-facing notice before release.
