# ADR 002: Pose Estimator Library and Adapter Contract

## Status

Accepted (spike; final threshold values remain open, see MP-021)

## Context

MovePal needs a pose-estimation library that can run locally on
contributor laptops (Windows and Linux, Python 3.11) without a GPU, and
whose output the rest of the application never touches directly.
`requirements.txt` already pins `mediapipe==0.10.35`, so this ADR
verifies that pin actually works end-to-end on Windows/Python 3.11 and
records the project-owned contract that routes and movement rules
(MP-007, MP-013) should build against.

docs/architecture.md section 3 requires `app/services/pose_tracking.py`
to be the only place that knows about the provider; docs/privacy.md
requires that any real sample used for local investigation be openly
licensed or a consented adult volunteer, and that only synthetic or
derived landmark fixtures — never raw images or recordings — get
committed.

## Investigation

Environment: Windows 11, Python 3.11.9 (`py -3.11`), the repository's
`.venv`, `mediapipe==0.10.35` as already pinned.

### Finding 1 — the legacy `mp.solutions.pose` API is not present in this wheel

`import mediapipe.python.solutions.pose` (the API used in most older
MediaPipe tutorials) raises `ModuleNotFoundError: No module named
'mediapipe.python'` on this wheel. Only `mediapipe.tasks` (the newer
MediaPipe Tasks API) and the bare `mp.Image` / `mp.ImageFormat` helpers
are available:

```pycon
>>> import mediapipe as mp
>>> dir(mp)
['Image', 'ImageFormat', ..., 'tasks']
```

**Decision:** build the adapter on `mediapipe.tasks.python.vision.PoseLandmarker`
(the MediaPipe Tasks API), not the legacy Solutions API. Any future
example code, tutorial, or contributor guidance referencing
`mp.solutions.pose` needs to be translated to the Tasks API for this
project.

### Finding 2 — PoseLandmarker requires a separately downloaded model bundle

`PoseLandmarker` needs a `.task` model asset file; it is not bundled in
the pip package. A model (`pose_landmarker_lite.task`, ~5.8 MB) was
downloaded locally from
`https://storage.googleapis.com/mediapipe-models/pose_landmarker/pose_landmarker_lite/float16/latest/pose_landmarker_lite.task`
for this investigation only and was **not** committed to the repository.

**Decision:** `MediaPipePoseAdapter` takes a `model_path` argument and
only touches the filesystem/network for that model when
`estimate()`/`_get_landmarker()` is actually called (lazy import and
lazy landmarker creation inside the adapter). Fixture-based tests never
construct a real `MediaPipePoseAdapter`, so `pytest` never needs a model
file, `mediapipe.tasks`, or network access. Whoever wires the adapter
into a real route (MP-013) needs to decide where the `.task` file is
provisioned in dev/CI — likely a documented one-time local download step
or a small setup script, not a repository asset.

### Finding 3 — a real permitted sample produces a usable, project-owned result

An openly licensed (Pixabay License — free for commercial and personal
use, no attribution required) photo of an adult in athletic wear was
used for local investigation only. It is the same demo image Google's
own official Pose Landmarker documentation and Colab use, which was the
basis for treating it as an acceptable permitted sample for this
one-time local check. It was **not** committed to the repository or to
any fixture file.

Running it through `MediaPipePoseAdapter.estimate()` returned 33 raw
landmarks, of which the 12 tracked by MovePal were extracted with
visibility between 0.69 and 1.0 — well above the starting 0.5 threshold
— giving `PoseStatus.SUCCESS` with a fully populated `landmarks` dict.
Reproduce with:

```
python scripts/pose_adapter_demo.py --model <path-to-task-file> --image <path-to-permitted-image>
```

### Finding 4 — landmark index/name mapping and coordinate convention

MediaPipe Pose's 33-point topology is stable across the Tasks API
(confirmed via `vision.PoseLandmark`). MovePal only needs the subset
used by the three Sprint 1 movements:

| Name | MediaPipe index |
| --- | --- |
| left/right_shoulder | 11 / 12 |
| left/right_elbow | 13 / 14 |
| left/right_wrist | 15 / 16 |
| left/right_hip | 23 / 24 |
| left/right_knee | 25 / 26 |
| left/right_ankle | 27 / 28 |

Ankle was added beyond MP-005's literal shoulder/elbow/wrist/hip/knee
list because docs/movement_specification.md's knee-lift/step movement
already requires it.

Coordinates are normalized image coordinates: `x`/`y` in `[0, 1]` from
the top-left of the raw (unmirrored) frame, so a raised wrist has a
*smaller* `y` than the shoulder — confirmed against the real-sample
result above. `left_*`/`right_*` are MediaPipe's own anatomical-side
convention for that raw frame. If the browser shows the user a mirrored
preview, that must stay a display-only concern in MP-013/frontend work;
the frame sent for processing must not be flipped, or the anatomical
labels would silently swap. This is recorded in
docs/movement_specification.md section 2 and in the
`app/services/pose_tracking.py` module docstring.

## Decision

- Use `mediapipe==0.10.35`'s Tasks API (`PoseLandmarker`) as the pose
  provider, wrapped by `MediaPipePoseAdapter` in
  `app/services/pose_tracking.py`. No other module may import
  `mediapipe` directly (docs/architecture.md section 3,
  MP-005 acceptance criteria).
- Represent every result as a project-owned `PoseResult`:

  ```python
  class PoseStatus(str, Enum):
      SUCCESS = "success"
      NO_POSE = "no_pose"
      LOW_VISIBILITY = "low_visibility"
      ERROR = "error"

  @dataclass(frozen=True)
  class PoseResult:
      status: PoseStatus
      landmarks: dict[str, Landmark]
      error: str | None = None
  ```

  `NO_POSE` means the provider found nobody in frame. `LOW_VISIBILITY`
  is a coarse framing pre-filter: fewer than `DEFAULT_MINIMUM_COVERAGE`
  (0.6) of the *tracked* landmarks that are present clear
  `DEFAULT_VISIBILITY_THRESHOLD` (0.5). `ERROR` wraps any decode/model/
  inference exception so the adapter never raises out of `estimate()`.
  A landmark that is simply *absent* from `landmarks` (camera framing
  cropped it out, for example) does not by itself force a non-SUCCESS
  status — checking that a specific movement's *required* landmarks are
  present is deliberately left to the movement rule (MP-007), per
  docs/movement_specification.md section 3's evaluation order, since
  required landmarks differ per movement.
- Both starting numbers (0.5 visibility, 0.6 coverage) are spike
  defaults, not validated thresholds; MP-021 must record the justified
  final values per docs/movement_specification.md section 4.
- Offline testing uses `data/landmarks/pose_fixtures.json`, loaded via
  `load_pose_fixture()`/`load_pose_fixtures()`. Fixtures are synthetic,
  hand-authored coordinate sets — no camera, image, model, or personal
  data required to load or evaluate them. `pose_result_from_fixture_data()`
  and `MediaPipePoseAdapter.estimate()` share the same
  `_status_for_landmarks()` status logic, so a fixture and a real sample
  are evaluated identically.

## Fallback decision

If MediaPipe becomes unusable on a contributor's machine or in CI (wheel
unavailable, native-library crash), the fallback is: keep developing and
testing entirely against `data/landmarks/pose_fixtures.json` through the
same `PoseResult` contract, and treat `MediaPipePoseAdapter` as an
optional, swappable implementation behind that contract. No other
Sprint 1 work should block on live MediaPipe availability, since routes
and movement rules only ever depend on `PoseResult`/`Landmark`, not on
MediaPipe. No fallback was actually needed during this spike — 0.10.35
worked on Windows/Python 3.11 once the Tasks API was used instead of the
legacy Solutions API.

## Consequences

Positive:

- Movement rules, Flask routes, and tests can be written and merged
  today against fixtures, with zero MediaPipe/network dependency in CI.
- Swapping or upgrading the pose provider later only touches
  `app/services/pose_tracking.py`.
- The mirroring/coordinate-convention pitfall is documented before any
  movement rule code is written against it.

Negative / follow-up:

- `MediaPipePoseAdapter` itself is not covered by CI (by design — it
  needs a model file), so its correctness relies on this manual spike
  plus whatever integration check MP-013 adds when it's wired into a
  real route.
- The `.task` model file provisioning story (where it lives in dev/CI,
  how a contributor gets one) is intentionally left open for MP-013.
- `DEFAULT_VISIBILITY_THRESHOLD` and `DEFAULT_MINIMUM_COVERAGE` are
  unvalidated starting points and must be revisited in MP-021.

## Evidence

- `python scripts/pose_adapter_demo.py --model <task-file> --image <permitted-sample>`
  — real sample and fixture both returned `PoseStatus.SUCCESS` through
  `PoseResult`.
- `pytest tests/unit/test_pose_tracking.py` — schema validation, all
  five fixtures' expected statuses, and the offline error path pass
  without network access.
