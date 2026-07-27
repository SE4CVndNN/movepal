"""Browser-backed session state for one gameplay session.

MP-018 tracks the small, non-identifying game state of a single gameplay
session: which movements were attempted and completed, how many stars were
earned, the current movement/attempt state, and whether the session has been
finished. See docs/adr/003-session-state.md for the storage decision and
docs/limitations.md ("Session State and Persistence") for the constraints.

The service reads and writes a single namespaced key inside a *dict-like*
storage object. Routes pass ``flask.session``; unit tests pass a plain
``dict``. Keeping the storage abstract means this module holds no
Flask-specific business logic and needs no request context to test.
"""

from __future__ import annotations

from collections.abc import MutableMapping
from typing import TYPE_CHECKING, Any

from app.services.scoring import ScoringSession
from app.services.session_summary import SessionSummary

if TYPE_CHECKING:
    from app.services.movement_rules import MovementResult

STORAGE_KEY = "movepal_session"
"""Single key under which the whole session state dict is stored.

Namespacing everything under one key keeps the service from colliding with
other cookie data and lets a mutation persist by reassigning just this key
(which is what triggers Flask's session-modified detection)."""


def _default_state() -> dict[str, Any]:
    """Return a fresh, JSON-serializable session-state dict.

    ``attempted`` / ``completed`` are lists used as ordered sets of movement
    names. The remaining fields mirror :class:`ScoringSession` so it can be
    rehydrated and saved back on each request.
    """
    return {
        "total_stars": 0,
        "attempt_completed": False,
        "current_movement": None,
        "attempt_count": 0,
        "attempted": [],
        "completed": [],
        "finished": False,
        "consecutive_samples": {},
    }


class SessionStateService:
    """Translate dict-like session storage to/from scoring and summary types.

    The service never holds its own copy of the state; it reads from and writes
    to the injected ``storage`` mapping so a Flask signed-cookie session and a
    plain test dict behave identically.
    """

    def __init__(self, storage: MutableMapping[str, Any]) -> None:
        self._storage = storage

    def _state(self) -> dict[str, Any]:
        """Return the live state dict, initializing it on first access."""
        state = self._storage.get(STORAGE_KEY)
        if not isinstance(state, dict):
            state = _default_state()
            self._storage[STORAGE_KEY] = state
        return state

    def _persist(self, state: dict[str, Any]) -> None:
        """Write *state* back under the top-level key.

        Reassigning the whole key (rather than relying on nested mutation)
        is what marks a Flask session as modified so the cookie is re-sent.
        """
        self._storage[STORAGE_KEY] = state

    def load_scoring_session(self) -> ScoringSession:
        """Rehydrate a :class:`ScoringSession` from persisted state."""
        state = self._state()
        session = ScoringSession()
        session.total_stars = state["total_stars"]
        session.attempt_completed = state["attempt_completed"]
        session.current_movement = state["current_movement"]
        session.attempt_count = state["attempt_count"]
        return session

    def save_scoring_session(self, session: ScoringSession) -> None:
        """Persist the mutable fields of a :class:`ScoringSession`."""
        state = self._state()
        state["total_stars"] = session.total_stars
        state["attempt_completed"] = session.attempt_completed
        state["current_movement"] = session.current_movement
        state["attempt_count"] = session.attempt_count
        self._persist(state)

    def record_attempt(self, movement: str) -> None:
        """Record that *movement* was attempted (distinct movements only)."""
        state = self._state()
        if movement not in state["attempted"]:
            state["attempted"].append(movement)
        self._persist(state)

    def reset_consecutive_samples(self, movement: str) -> None:
        """Clear the hold counter for *movement* when a new attempt starts."""
        state = self._state()
        if "consecutive_samples" not in state or not isinstance(
            state["consecutive_samples"], dict
        ):
            state["consecutive_samples"] = {}
        state["consecutive_samples"][movement] = 0
        self._persist(state)

    def record_completion(self, movement: str) -> None:
        """Record that *movement* was completed for this attempt."""
        state = self._state()
        state["completed"].append(movement)
        self._persist(state)

    def get_consecutive_samples(self, movement: str) -> int:
        """Return the current consecutive valid frame count for *movement*."""
        state = self._state()
        samples = state.get("consecutive_samples")
        if not isinstance(samples, dict):
            return 0
        return int(samples.get(movement, 0))

    def update_consecutive_samples(self, movement: str, satisfied: bool) -> int:
        """Increment or reset consecutive valid frame count for *movement*."""
        state = self._state()
        if "consecutive_samples" not in state or not isinstance(
            state["consecutive_samples"], dict
        ):
            state["consecutive_samples"] = {}
        samples = state["consecutive_samples"]
        if satisfied:
            new_count = int(samples.get(movement, 0)) + 1
        else:
            new_count = 0
        samples[movement] = new_count
        self._persist(state)
        return new_count

    def reset(self) -> None:
        """Replace all state with a clean default session."""
        self._persist(_default_state())

    def finish(self) -> SessionSummary:
        """Mark the session finished and return its final summary.

        Idempotent: finishing only sets a flag, so repeated calls return the
        same summary and never award additional stars.
        """
        state = self._state()
        state["finished"] = True
        self._persist(state)
        return self.build_summary()

    def is_finished(self) -> bool:
        """Return whether the session has been marked finished."""
        return bool(self._state()["finished"])

    def build_summary(self) -> SessionSummary:
        """Build the non-identifying end-of-session summary."""
        state = self._state()
        return SessionSummary(
            attempted_movements=len(state["attempted"]),
            completed_movements=len(state["completed"]),
            stars=state["total_stars"],
        )

    def record_result(
        self,
        result: MovementResult,
        *,
        completed: bool,
        stars_awarded: int = 0,
    ) -> None:
        """Record one evaluated movement result against the summary counters.

        Always counts the movement as attempted; counts it as completed only
        when *completed* is true and a star was awarded for this attempt.
        Star totals are owned by :class:`ScoringSession` (persisted via
        :meth:`save_scoring_session`), not re-derived here.
        """
        self.record_attempt(result.movement)
        if completed and stars_awarded > 0:
            self.record_completion(result.movement)
