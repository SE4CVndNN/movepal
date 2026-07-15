# MovePal Architecture

## 1. Architectural goals

MovePal uses a small modular monolith suitable for beginner developers and a two-week Sprint. The design should make each component understandable, testable, and replaceable without introducing microservices or unnecessary infrastructure.

The main goals are:

- thin Flask routes;
- clear service boundaries;
- deterministic testing without camera hardware;
- portable Windows/Linux behavior;
- privacy-aware data handling;
- transparent movement rules;
- early end-to-end integration;
- a reliable fallback demonstration.

## 2. System context

```text
User and browser
    │
    ├── live webcam frame
    │       or
    └── privacy-safe fallback image/video
            │
            ▼
Flask page/API layer
            │
            ▼
Input validation and decoding
            │
            ▼
Pose tracking adapter
            │
            ▼
Project landmark representation
            │
            ▼
Visibility/framing checks
            │
            ▼
Movement rule
            │
            ▼
Feedback + scoring + session update
            │
            ▼
JSON response and game UI
```

## 3. Repository responsibilities

### `app/__init__.py`

Creates the Flask application, loads configuration, and registers blueprints. It should not initialize a physical camera during import and should avoid expensive model downloads in tests.

### `app/config.py`

Defines safe defaults such as upload-size limits, allowed extensions, and portable data directories. Paths must use `pathlib.Path`.

Secrets belong in environment variables. Development defaults must never be treated as production credentials.

### `app/routes/pages.py`

Renders HTML pages. Routes should select templates and provide simple view data. Movement evaluation and file processing do not belong here.

### `app/routes/api.py`

Defines JSON endpoints. Responsibilities include:

- reading the request;
- validating required parameters;
- calling the appropriate service;
- mapping service results to HTTP/JSON responses;
- avoiding image or personal-data logging.

Routes should not contain pose mathematics, movement thresholds, or score rules.

### `app/services/pose_tracking.py`

Provides the adapter between MediaPipe or another approved pose provider and MovePal’s project-level landmark representation.

Responsibilities:

- decode/process an accepted image or sampled frame;
- extract only the landmarks required by the application;
- convert provider-specific output into stable `Landmark` objects;
- expose visibility/confidence information;
- return a controlled unable-to-process result rather than crashing;
- support deterministic fixture/mock implementations in tests.

### `app/services/movement_rules.py`

Contains pure or mostly pure movement evaluation logic. It should accept normalized landmarks and configuration, then return a structured result without depending on Flask, templates, JavaScript, or the physical camera.

### `app/services/feedback.py`

Maps result codes to friendly user-facing messages. Feedback should be short, supportive, and non-medical. Keeping messages separate from rule logic makes them easier to review and localize.

### `app/services/scoring.py`

Maps completed attempts and confidence/evaluation results to stars or points. Scores are game feedback only and must not imply health or physical-performance assessment.

### `app/services/session_summary.py`

Maintains or produces the short MVP summary: attempts, completed movements, and stars. Do not include names, biometric profiles, or long-term personal history.

### `app/templates/` and `app/static/`

Provide the game interface, camera/fallback controls, avatar presentation, feedback area, score, and summary. JavaScript handles browser APIs and calls Flask endpoints but should not duplicate backend movement rules.

## 4. Project-level landmark contract

MovePal should not let movement rules depend directly on the full MediaPipe object model. Convert provider output into a small stable structure such as:

```python
@dataclass(frozen=True)
class Landmark:
    name: str
    x: float
    y: float
    z: float
    visibility: float
```

The pose task must document:

- coordinate orientation;
- normalized ranges;
- anatomical left/right interpretation;
- camera mirroring behavior;
- missing-landmark representation;
- provider confidence/visibility mapping.

The movement specification and fixtures become the authoritative contract for rule tests.

## 5. Suggested API contract

The final endpoint names are confirmed by the responsible issue and PR. A movement-evaluation response should nevertheless have a stable shape similar to:

```json
{
  "movement": "raise_both_arms",
  "completed": true,
  "confidence": 0.91,
  "feedback_code": "great",
  "feedback": "Great!",
  "stars": 3,
  "visibility_ok": true,
  "retryable": true
}
```

A controlled failure should be explicit:

```json
{
  "movement": "raise_both_arms",
  "completed": false,
  "confidence": 0.21,
  "feedback_code": "full_body_missing",
  "feedback": "I cannot see your full body.",
  "stars": 0,
  "visibility_ok": false,
  "retryable": true
}
```

Do not expose stack traces, local paths, raw landmarks unless needed by a documented debug mode, or raw images in normal API responses.

## 6. Input-validation flow

Validation should occur before pose processing:

1. Confirm that an input exists.
2. Confirm the selected movement is supported.
3. Enforce the configured request-size limit.
4. Check the declared and actual supported media type where practical.
5. Use safe temporary handling; do not trust uploaded filenames.
6. Attempt decoding.
7. Return a clear client error for invalid input.
8. Process only the minimum frame/sample required.
9. Delete temporary data after use unless an approved protocol explicitly retains it.

## 7. Early vertical slice

`MP-014` proves the first complete contract:

```text
deterministic sample/fixture
→ Flask API
→ pose adapter or test implementation
→ visibility check
→ raise-arms rule
→ feedback and stars
→ browser-visible result
→ integration test
```

This slice should use the same contracts later used by side reach, knee lift, and the full game loop. Do not build a throwaway demonstration that bypasses the actual services.

`MP-019` extends the vertical slice into the complete game flow and must preserve its automated contract test.

## 8. Error handling

Expected failures are product behavior, not unhandled exceptions. Define consistent responses for:

- missing input;
- unsupported extension/type;
- oversized upload;
- decode failure;
- no person detected;
- multiple-person ambiguity if not supported;
- required landmarks missing;
- visibility too low;
- unsupported movement;
- pose service unavailable;
- invalid session transition.

Log only technical context necessary to diagnose the error. Never log raw frames, landmark dumps tied to a person, emails, names, tokens, or private paths.

## 9. Session design

Sprint 1 should use minimal session state. Acceptable options include Flask session data or a small in-memory structure for one local prototype session, provided the design is documented and tests can reset it.

Do not add authentication or a production database. The summary should contain only non-identifying game data such as number of attempts, completed movements, and stars.

## 10. Testing architecture

### Unit tests

Test pure services with small deterministic inputs:

- visibility filtering;
- each movement rule;
- feedback-code mapping;
- scoring boundaries;
- session summary calculations;
- invalid/missing landmarks.

### Integration tests

Use the Flask test client to verify:

- page and health routes;
- valid evaluation request;
- invalid/oversized request;
- stable JSON contract;
- fixture-to-feedback vertical slice;
- session reset/summary behavior.

### CI constraints

CI must not:

- access a physical camera;
- require GUI interaction;
- download a large dataset;
- use private recordings;
- depend on developer-specific paths;
- rely on network access for normal tests.

## 11. Cross-platform requirements

- Use `pathlib.Path`.
- Do not assume a current working directory outside the repository contract.
- Treat filename case consistently because Linux is case-sensitive.
- Do not invoke PowerShell from application code.
- Keep shell-specific commands in documentation or owner scripts.
- Verify both Windows and Linux CI before merge.

## 12. Privacy and security architecture

- Camera permission is requested by the browser, not assumed.
- Frames should be processed transiently unless the user explicitly chooses an approved upload flow.
- Raw private recordings are excluded from Git.
- File size and type are constrained.
- Filenames are never trusted as paths.
- Debug mode remains disabled outside controlled local development.
- No credentials are committed.
- QA evidence is redacted and privacy-safe.

See [`privacy.md`](privacy.md), [`collection_protocol.md`](collection_protocol.md), and [`limitations.md`](limitations.md).

## 13. Architecture change process

A task that changes a public service interface, JSON response, data schema, coordinate convention, or storage behavior must:

1. update this document or the relevant existing specification;
2. update affected tests and fixtures;
3. identify dependent tasks/PRs;
4. request review from an owner of an affected component;
5. avoid merging incompatible contracts without coordinated updates.

Favor the simplest design that meets Sprint 1 acceptance criteria.


## 14. MP-004 Flask vertical slice structure

The initial Flask vertical slice follows this flow:

```text
Browser
   |
   v
Flask Route (routes/)
   |
   v
Service Module (services/)
   |
   v
Response (HTML/JSON)
