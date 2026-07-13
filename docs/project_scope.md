# MovePal Sprint 1 Scope

## 1. Product purpose

MovePal is a playful movement-practice prototype for children and families. A simple avatar demonstrates a movement, the user attempts it in front of a webcam or with a provided fallback sample, and the application uses pose landmarks and transparent rules to return friendly feedback, points, and a short session summary.

The project is also a software-engineering training environment. Students practice Scrum, issue-based planning, modular Flask development, computer-vision integration, automated testing, pull-request review, cross-team QA, and evidence-based delivery.

## 2. Product boundary

MovePal is not:

- a medical device;
- a diagnostic tool;
- a clinical rehabilitation application;
- a physical-therapy prescription;
- a measure of health, fitness, disability, or treatment progress;
- a replacement for a physiotherapist or healthcare professional.

Feedback must describe only what the prototype appears to observe in the current camera frame or short sample. Avoid statements such as “your movement is medically correct,” “you have improved,” or “this exercise will treat a condition.”

## 3. Intended Sprint 1 user journey

A successful user journey is:

1. The user opens MovePal in a supported browser.
2. The application explains that it is a playful prototype and requests camera permission only when needed.
3. The user chooses a supported movement.
4. An avatar or simple visual demonstrates the intended movement.
5. The user chooses live camera mode or a sample fallback.
6. The application checks whether the required body landmarks are visible.
7. The application evaluates a small set of transparent movement rules.
8. The user receives friendly feedback and a score/star result.
9. The user can retry or continue to another movement.
10. A short summary shows attempts, completed movements, and stars without storing personal identity.

## 4. Sprint Goal

By Wednesday, 29 July 2026, the development team will deliver a documented Flask-based MovePal prototype with three movement activities, live-camera or fallback input, pretrained pose landmarks, rule-based friendly feedback, points/stars, a session summary, automated tests, Windows/Linux CI, visible privacy and limitations information, and a reliable fallback demonstration.

The external QA team will perform final-day manual sanity testing against a frozen release-candidate commit.

## 5. Required Sprint 1 capabilities

### Application foundation

- Python 3.11 and Flask.
- Application factory pattern.
- Clear separation among routes, services, templates, static assets, tests, and data fixtures.
- Environment-based or class-based configuration.
- Portable filesystem paths using `pathlib`.

### Input

- Browser webcam permission and frame capture.
- A mandatory sample image or sample video fallback.
- Validation of supported file type and maximum upload size.
- Safe behavior when camera permission is denied, no camera exists, or the input cannot be decoded.

### Computer vision and movement rules

- Pretrained pose landmark extraction, preferably MediaPipe Pose unless the investigation task documents a better compatible choice.
- Normalized project-level landmark representation.
- Visibility and framing checks.
- Rule-based evaluation for:
  - raise both arms;
  - side reach, left and right;
  - knee lift or step in place.
- Explicit low-confidence or unable-to-evaluate behavior.
- Configurable thresholds supported by fixtures and a small evaluation report.

### User experience

- Simple child-friendly presentation.
- Friendly, non-medical feedback.
- Stars or points.
- Retry/continue flow.
- Short session summary.
- Keyboard-accessible basic navigation and readable responsive layout.
- Visible privacy and limitations information.

### Quality

- Unit tests for services and rules.
- Integration tests for Flask routes and component contracts.
- Deterministic fixtures; no real camera requirement in CI.
- Ruff lint/format checks.
- Windows and Linux GitHub Actions CI.
- Independent PR review.
- External manual QA on the final day.
- Fallback demo that does not depend on live camera conditions.

## 6. Observable acceptance conditions

Sprint 1 is acceptable when a reviewer can:

- install the project from the README in a fresh environment;
- start the Flask application;
- open the main page;
- use a live camera or fallback path;
- receive a valid JSON/API result for a deterministic sample;
- see visibility/framing guidance when required landmarks are missing;
- exercise all three movement paths;
- receive friendly success/retry feedback;
- see points/stars and a summary;
- observe safe errors for invalid or oversized input;
- find the privacy notice and non-medical disclaimer;
- run tests and Ruff successfully;
- see passing Windows and Linux CI;
- reproduce the final demo with included privacy-safe samples.

## 7. Explicitly out of scope for Sprint 1

- Medical, rehabilitation, diagnostic, or treatment claims.
- Child data collection.
- User accounts, authentication, profiles, or cloud identity.
- Long-term session history.
- Complex databases.
- Custom pose-model training.
- Full low-latency video streaming or WebSockets as a hard dependency.
- React or another heavy frontend framework.
- Microservices, Kubernetes, or production cloud infrastructure.
- Production deployment as a Sprint requirement.
- Mobile applications.
- Teacher/therapist configuration panels.
- Personalized clinical thresholds.
- Automatic conclusions about physical ability or health.

These ideas may remain in the post-Sprint, future, or optional backlog.

## 8. Data boundary

- No child data is needed or permitted for Sprint 1.
- Adult-volunteer data may be collected only with approved consent and the documented protocol.
- Derived landmarks are preferred over raw images/video.
- Private raw recordings stay outside GitHub and CI.
- Tests should primarily use synthetic, hand-authored, or privacy-reviewed derived fixtures.

## 9. Scope control during the Sprint

The Product Owner decides whether a requested change supports the Sprint Goal. The Scrum Master makes the schedule and dependency impact visible. The instructor resolves significant scope disputes.

When a new idea appears:

1. Check whether an existing later backlog task already covers it.
2. Record it there or create a future proposal only when necessary.
3. Do not expand the current Sprint issue without adjusting acceptance criteria, dependencies, estimate, and workload.
4. Protect the release-candidate date and the fallback demonstration.

The goal is a complete narrow product, not a collection of partially implemented advanced features.
