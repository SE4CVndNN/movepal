# ADR 003: Session State and End-of-Session Summary

## Status

Accepted (MP-018)

## Context

MP-018 asks for lightweight session state so a single gameplay session can
track attempted activities, completed activities, and stars, and produce a
short end-of-session summary. The session represents one gameplay session,
not a user account.

The MVP constraints (docs/architecture.md section 9 and the MP-018 backlog
entry) are strict:

- no authentication;
- no database;
- no long-term user history;
- no personal information stored;
- state must be testable and resettable;
- two independent clients must never share mutable state.

MP-017 already provides the scoring state machine
(`app/services/scoring.py:ScoringSession`), which awards a star exactly once
per successful attempt, and `app/services/session_summary.py:SessionSummary`,
a frozen dataclass holding `attempted_movements`, `completed_movements`, and
`stars`. MP-018 must build on both rather than re-implement scoring or invent
a second summary type.

## Decision

Store session state in **Flask's signed-cookie browser session**
(`flask.session`), and introduce a dedicated
`app/services/session_state.py:SessionStateService` that owns the translation
between that storage and the existing `ScoringSession` / `SessionSummary`
types.

Key choices:

- **Flask session (signed cookie), not a global dictionary or singleton.**
  Each browser — and each Flask test client — carries its own cookie, so
  state is isolated per client with zero server-side shared memory. This
  directly satisfies "two test clients do not accidentally share mutable
  state" and the architecture rule "avoid global mutable state". No database
  or authentication is introduced.

- **A service that accepts a dict-like storage object.**
  `SessionStateService(storage)` reads and writes a single namespaced key
  (`movepal_session`) inside any mapping. In the routes we pass
  `flask.session`; in unit tests we pass a plain `dict`. This keeps the
  service free of Flask-specific business logic and trivially unit-testable
  without a request context.

- **Distinct-movement counting for the summary.**
  `attempted_movements` and `completed_movements` count *distinct* movement
  names (e.g. `raise_both_arms`, `side_reach`, `knee_lift_or_step`), matching
  the acceptance criterion "a session records all three activities" and the
  `SessionSummary` field names. `stars` is taken directly from the persisted
  `ScoringSession` total, so star idempotency (one star per attempt) is
  preserved by MP-017's logic rather than re-derived here.

- **`SessionSummary` stays a plain data structure.**
  The service builds a `SessionSummary`; the summary type is not turned into a
  session manager. Encouraging completion text is composed in the route layer
  so the data structure stays free of presentation concerns.

## State shape

The service persists one JSON-serializable dict under `movepal_session`:

```json
{
  "total_stars": 0,
  "attempt_completed": false,
  "current_movement": null,
  "attempt_count": 0,
  "attempted": [],
  "completed": [],
  "finished": false
}
```

`attempted` / `completed` are lists (JSON-serializable) used as ordered sets of
movement names. The `total_stars` / `attempt_completed` / `current_movement` /
`attempt_count` fields mirror `ScoringSession` so it can be rehydrated on each
request and saved back afterwards. Every mutation reassigns the top-level key
so Flask's session-modified detection persists the change.

## API surface

- `POST /api/movement` — unchanged evaluation flow, now wrapped in
  load-session → `format_feedback(result, session=scoring_session)` →
  save-session, and records the attempt/completion.
- `POST /api/session/reset` — replaces state with a clean default.
- `GET /api/session/summary` — returns the current three-field summary.
- `POST /api/session/finish` — marks the session finished and returns the
  final summary plus a friendly, deterministic completion message. Idempotent:
  repeated calls return the same summary and never award extra stars.

## Rejected alternatives

- **Global in-memory dictionary / singleton session manager.** Rejected: it is
  shared mutable server state, breaks per-client isolation, leaks between
  tests, and is explicitly disallowed by the task.
- **Database or server-side session store.** Rejected: out of MVP scope; the
  task forbids a database and long-term history.
- **Extending `ScoringSession` to also track attempts/completions and
  finished state.** Rejected: `ScoringSession` is MP-017's scoring state
  machine; overloading it with persistence and summary concerns would blur its
  responsibility. The new service composes it instead.

## Limitations

- State lives only in the browser cookie. Clearing cookies, switching
  browsers, or losing the cookie loses the session — this is intended: there
  are no accounts and no history.
- The signed cookie is tamper-evident (integrity) but not encrypted; because it
  holds only non-identifying game counters, this is acceptable. No names,
  images, emails, or biometric data are ever stored.
- Cookie size limits mean the state must stay small; the current fixed set of
  counters is well within limits.
- Only `raise_both_arms` is wired through `POST /api/movement` today, so via the
  HTTP API a single session currently reaches at most one distinct attempted
  movement. The service supports all three activities directly (exercised by
  unit tests); full multi-movement play arrives with the game loop in MP-019.

See docs/limitations.md ("Session State and Persistence") for the
user-facing summary of these constraints.
