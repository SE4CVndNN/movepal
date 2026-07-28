# MovePal QA Handoff

This handoff describes one frozen Sprint 1 release candidate. External QA must
use the recorded commit or tag and must not combine results from different
commits. A critical fix creates a new documented retest candidate.

## 1. Release candidate

- **Application commit:** `bfde35e112f3846fbf1771bc362154b32c72249a`
- **Release tag:** `sprint1-rc1`
- **Freeze date:** 2026-07-28
- **Prepared by:** `@alaamadii`
- **Independent reviewer:** Pending review by `@IslamOuda85`
- **Repository:** `https://github.com/SE4CVndNN/movepal`
- **Release issue:** `https://github.com/SE4CVndNN/movepal/issues/24`
- **QA status:** Automated entry checks pass; browser/camera rehearsal must be
  recorded before the candidate is announced as QA-ready.

The application commit includes the merged outputs of MP-019, MP-021, MP-022,
and MP-023. Issues MP-001 through MP-023 were confirmed closed on 2026-07-28.
During the QA window, do not merge unrelated work into the candidate. Testers
can always recover the frozen code with:

```bash
git fetch --tags origin
git switch --detach sprint1-rc1
```

## 2. Supported environment

- **Required Python:** 3.11.
- **CI environments:** GitHub-hosted `windows-latest` and `ubuntu-latest`.
- **Local rehearsal environment:** Windows NT 10.0.22631, Chrome
  150.0.7871.184, and Edge 150.0.4078.99.
- **Camera prerequisites:** a camera-enabled Chrome/Edge browser on
  `http://127.0.0.1` or another secure context, explicit user permission, and
  the local MediaPipe model described below.
- **Not release-tested:** Safari, Firefox, remote plain-HTTP camera access,
  multiple-person selection, and Python versions other than 3.11.

## 3. Fresh installation

Clone the private repository using an authorized GitHub account, then check out
the frozen tag.

### Windows PowerShell

```powershell
git clone https://github.com/SE4CVndNN/movepal.git
cd movepal
git fetch --tags origin
git switch --detach sprint1-rc1
py -3.11 -m venv .venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements-dev.txt
```

### Linux

```bash
git clone https://github.com/SE4CVndNN/movepal.git
cd movepal
git fetch --tags origin
git switch --detach sprint1-rc1
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements-dev.txt
```

The deterministic built-in demo and automated tests do not require a model
download. Live camera or photo inference requires the gitignored MediaPipe
model beside `run.py`:

```bash
python -c "import urllib.request; urllib.request.urlretrieve('https://storage.googleapis.com/mediapipe-models/pose_landmarker/pose_landmarker_lite/float16/latest/pose_landmarker_lite.task', 'pose_landmarker_lite.task')"
```

Do not commit the `.task` file. Do not create or commit a `.env` file unless a
local override is needed. If required, copy `.env.example` and replace its
development-only secret locally.

## 4. Verification commands and evidence

```bash
python -m ruff check .
python -m ruff format --check .
python -m pytest
python -m compileall app tests
python scripts/qa_selfcheck.py
python run.py
```

- **Frozen-commit test result:** 219 tests pass.
- **MP-024 regression result:** 46 deterministic checks pass, 0 fail; three
  browser/manual checks remain explicitly marked as warnings.
- **Frozen-commit CI:** Windows and Ubuntu Python 3.11 jobs passed:
  `https://github.com/SE4CVndNN/movepal/actions/runs/30350950029`
- **Application URL:** `http://127.0.0.1:5000/`
- **Health URL:** `http://127.0.0.1:5000/api/health`
- **Expected health response:** HTTP 200 with
  `{"service": "movepal", "status": "ok"}`.

## 5. Deterministic fallback assets

All fallback data is synthetic derived landmark JSON. It contains no photos,
recordings, names, or identity-linked data.

| Asset | Built-in success fixture | Movement/input | Expected result |
| --- | --- | --- | --- |
| `data/landmarks/raise_both_arms_fixtures.json` | `synthetic_raise_arms_positive_001` | Raise both arms | `completed=true`, `feedback_code=great`, one star |
| `data/landmarks/side_reach_fixtures.json` | `synthetic_side_reach_left_positive_001` / `synthetic_side_reach_right_positive_001` | Left/right side reach | Requested side succeeds with `great`, one star |
| `data/landmarks/knee_lift_fixtures.json` | `synthetic_knee_lift_left_positive_001` / `synthetic_knee_lift_right_positive_001` | Left/right knee lift | Requested side succeeds with `great`, one star |

Each file also contains negative, borderline, low-visibility, and framing
fixtures. `python scripts/qa_selfcheck.py` evaluates all 24 movement fixtures
through `POST /api/movement`.

## 6. Expected movement behavior

### Raise both arms

- Both shoulders and wrists must be available and visible.
- Both wrists must be sufficiently above their matching shoulders.
- Success returns `great` and one star.
- Incorrect height returns `raise_arms`; missing/low-visibility landmarks
  return `full_body_missing`.
- This is a configurable game heuristic, not a clinical measurement.

### Side reach

- Left/right always means the user's anatomical side, not the mirrored preview.
- A left bend uses the right arm overhead; a right bend uses the left arm.
- Correct requested-side geometry returns `great`.
- Wrong/insufficient geometry returns `reach_left` or `reach_right`;
  missing/low-visibility required landmarks return `full_body_missing`.
- The rule assumes one primary visible person.

### Knee lift or step in place

- The selected hip, knee, and ankle plus the opposite hip/ankle must be
  available and visible.
- The selected knee must rise above the configurable leg-relative threshold.
- Success returns `great`; an insufficient lift returns `lift_knee`;
  framing/visibility failure returns `full_body_missing`.
- A still-frame heuristic cannot independently prove a dynamic step.

## 7. Camera, upload, and fallback behavior

- Camera permission is requested only after **Use the camera** is selected.
- While permission is granted, the preview shows a transient skeleton and
  short framing guidance. The final frame is bounded before upload.
- The camera stops after final capture, cancel, navigation, or an upload/server
  failure.
- Denied permission, an unavailable device, unsupported browser APIs, or an
  insecure context produces friendly guidance to fallback/upload.
- Upload accepts JPEG/PNG only, at most 5 MB, previews the selected image, and
  requires a detectable person before **Check my move** is enabled.
- The built-in demo uses the selected movement's committed synthetic success
  fixture and requires no camera, photo, model, or network.
- No captured personal frame should be attached to QA evidence.

## 8. Session and scoring

- QA should try the three movement families; side reach and knee lift each
  expose explicit anatomical left/right choices.
- Each successful submitted attempt awards one star.
- Retry/framing results award no star and keep a retry path available.
- **Play again** and `POST /api/session/reset` clear stars and movement counts.
- The summary reports attempted movements, completed movements, and stars.
- Session state is non-identifying and stored only in a signed, unencrypted
  browser cookie; it must never contain personal data.

## 9. Accepted limitations

| Reference | Limitation | User impact/workaround | QA decision |
| --- | --- | --- | --- |
| `docs/limitations.md`, MP-021 | Rules are calibrated on a small deterministic fixture set and one compatibility sample. | Treat output as playful feedback, not accuracy or clinical evidence. | Accepted for prototype QA |
| `docs/limitations.md`, MP-016 | A still frame does not prove a dynamic step. | Evaluate the documented knee-position game heuristic only. | Accepted for prototype QA |
| `docs/hardening_checklist.md`, MP-023 | Formal WCAG/screen-reader and cross-browser audits are incomplete. | MP-033 performs final keyboard/responsive/accessibility sanity. | In external QA scope |
| `README.md` pose-model section | Live inference needs a separately downloaded gitignored model. | Use the documented one-time download; fallback requires no model. | Accepted with setup instruction |

Any new Critical or High finding blocks QA-ready status and must be linked from
issue #24. A focused fix must receive review and CI before a new retest
candidate is announced.

## 10. Privacy and evidence restrictions

- Do not collect or attach child data.
- Do not attach raw volunteer recordings, consent forms, captured camera
  frames, or identifiable backgrounds.
- Do not expose tokens, private paths, student emails, or credentials.
- Prefer logs, redacted screenshots without people, JSON responses, and the
  committed synthetic fixtures.
- Camera/upload bytes are processed through a temporary file and deleted in a
  `finally` block; they are not release artifacts.
- The MediaPipe `.task` model and local `.env` remain outside Git.

## 11. Bug reporting and triage

- **Bug template:** `.github/ISSUE_TEMPLATE/bug_report.yml`
- **QA plan:** `docs/qa_plan.md`
- **Development triage owner:** `@alaamadii` / Team B (`team-movepal`)
- **Product/acceptance contact:** `@dmrimawi`
- **Urgent escalation:** comment on issue #24, notify the Scrum Master, and use
  the instructor-approved team channel. Do not place private data in GitHub.

Every defect must record the tag/commit, environment, reproduction steps,
expected/actual result, severity proposal, privacy-safe evidence, linked task,
and retest result.

## 12. Handoff approval checklist

- [x] Release-candidate SHA and tag are specified.
- [x] Windows and Ubuntu Python 3.11 CI are green for the frozen application
      commit.
- [ ] Fresh installation has been rehearsed from the tag.
- [x] README installation/start/model instructions match the candidate.
- [x] All three movements and expected outcomes are documented.
- [x] Camera denial, upload, and fallback behavior are documented.
- [x] Fallback fixtures are committed and privacy-safe.
- [x] Accepted limitations and blocker rules are recorded.
- [x] Privacy and non-medical restrictions are recorded.
- [x] QA issues MP-028 through MP-033 are open and assigned.
- [ ] Internal browser/camera and responsive/keyboard rehearsal is recorded.
- [ ] Independent review is complete.
- [x] No unrelated merge is planned during the QA window.

External QA may begin only after every unchecked entry above is resolved or an
explicit blocker/release decision is recorded in issue #24.
