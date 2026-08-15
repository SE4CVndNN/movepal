# MovePal — Epics, User Stories, and Tasks Overview

This document translates the real MovePal product backlog (`product_backlog.json`, 63 tasks) into the **Epic → User Story → Task** structure requested for the Chingu Solo Project submission. The backlog itself is organized by `milestone` and `workstream` rather than this exact vocabulary, so each section below maps one real milestone (Epic) to one or more real backlog tasks (User Story), broken into their actual execution steps (Tasks).

This is a representative sample of the pattern used across all 63 items — not a rewrite of the backlog.

---

## Epic: Sprint 1 — MovePal MVP
*(milestone: "Sprint 1 — MovePal MVP")*

### User Story — MP-002: MVP acceptance map, demo scenarios, and safe product wording
**As the Product Owner, I want an approved MVP acceptance map and safe, non-medical product wording, so the team builds against agreed, testable requirements instead of inventing text independently.**

Tasks:
- Extract the required MVP capabilities (movements, camera/fallback input, feedback, privacy text, demo scenarios)
- Build an acceptance map linking each capability to observable evidence and an owning issue
- Draft the exact safe wording for disclaimers, feedback, and error states
- Define three reproducible demo scenarios: normal camera, fallback sample, graceful error

### User Story — MP-017: Friendly feedback orchestration and points/star scoring
**As the Product Owner, I want consistent, non-punitive feedback and idempotent point-awarding, so players get clear encouragement without being able to farm score by repeating a frame.**

Tasks:
- Collect all movement observations into one common feedback result type
- Prioritize visibility/framing messages before technique messages
- Implement points/stars with a strict one-award-per-attempt rule
- Test repeated success frames, retry, reset, and movement transitions

### User Story — MP-014: First vertical slice — sample input to visible raise-arms feedback
**As the Product Owner, I want a thin end-to-end slice proven by the middle of the sprint, so integration risk between frontend, API, and pose service is caught early rather than at the final-day freeze.**

Tasks:
- Select one tiny deterministic raise-arms fixture (no live camera required)
- Implement the pure raise-both-arms rule with success/retry/low-visibility outcomes
- Expose the rule through the existing Flask API using the normalized pose contract
- Add a minimal frontend path that renders the returned feedback
- Add contract and end-to-end smoke tests

---

## Epic: Post-Sprint Stabilization
*(milestone: "Post-Sprint Stabilization")*

### User Story — MP-035: Performance profiling and response-time budget
**As the Product Owner, I want a measured performance budget for image decoding, pose inference, and API response time, so future scope decisions are based on evidence rather than guesswork.**

Tasks:
- Instrument representative requests without logging image data
- Measure cold-start vs. warm-request timing and memory use
- Identify the single largest bottleneck and compare safe optimizations
- Document a request-rate / capture-interval recommendation

---

## Epic: Production Readiness
*(milestone: "Production Readiness")*

### User Story — MP-051: Threat model and automated security checks
**As the Product Owner, I want a lightweight threat model and proportionate automated checks, so known risks around camera input, uploads, and dependencies are documented and mitigated before any wider release.**

Tasks:
- Map assets, trust boundaries, and entry points (camera input, file upload, Flask endpoints)
- Prioritize threats by likelihood and impact for a prototype, not an enterprise system
- Add dependency, secret, and static-analysis checks that fit the repository
- Document false positives, update responsibility, and incident-response steps

---

## Epic: Future Extensions
*(milestone: "Future Extensions")*

### User Story — MP-043: Declarative custom-movement specification
**As the Product Owner, I want a safe, validated configuration format for adding new movements, so future contributors can extend the game without editing core Python code or introducing unsafe execution.**

Tasks:
- Extract the common rule concepts shared by the three MVP movements
- Design a constrained JSON/YAML schema instead of executable expressions
- Implement schema validation and a small interpreter
- Migrate one existing movement into the new format as a compatibility test

---

*This is a representative sample; the full 63-task backlog — with dependencies, acceptance criteria, effort tracking, and a dedicated dependency-tracking report set — is available in this repository's `backlog/` folder (`product_backlog.json`, plus `dependency_report.md`, `workload_report.md`, `blocked_task_report.md`, and related files).*
