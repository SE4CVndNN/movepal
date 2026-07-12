# Initial Architecture

The browser captures a periodic frame or selected sample. A thin Flask API route validates the request and delegates to services. Pose tracking produces normalized landmarks. Movement rules evaluate landmarks, scoring converts results to stars, and feedback returns friendly non-medical messages as JSON.

Application code uses `pathlib.Path` for file-system operations. CI runs on Windows and Linux. Camera hardware and large sample data are replaced by deterministic fixtures during testing.
