# MovePal QA Handoff

Complete this document under MP-024 before external QA begins. Replace every placeholder. The handoff describes one frozen release candidate; do not mix results from different commits without recording a new retest candidate.

## 1. Release candidate

- **Commit hash:**
- **Optional tag:**
- **Date/time frozen:**
- **Prepared by:**
- **Reviewed by:**
- **Repository URL:**
- **Project/release issue:**

During the QA window, do not merge unrelated changes into the candidate. Critical fixes use a focused PR and produce a clearly recorded retest commit.

## 2. Supported environment

- **Python version:** 3.11
- **Tested operating systems:**
- **Tested browsers and versions:**
- **Optional camera prerequisites:**
- **Known unsupported environment:**

## 3. Fresh installation

### Windows PowerShell

```powershell
# Replace or confirm the exact commands
py -3.11 -m venv .venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements-dev.txt
```

### Linux/macOS

```bash
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements-dev.txt
```

Document any additional required step. Do not rely on an uncommitted local file.

## 4. Verification commands

```bash
python -m ruff check .
python -m ruff format --check .
python -m pytest
python -m compileall app tests
python run.py
```

- **Expected test count/result:**
- **Expected CI run/link:**
- **Expected application URL:**
- **Expected health response:**

## 5. Fallback assets

List every fallback asset QA may use:

| Asset/path | Movement/input case | Expected result | Provenance/privacy status |
|---|---|---|---|
|  |  |  |  |

Confirm that assets are committed, small, and usable without private storage or network downloads.

## 6. Expected movement behavior

### Raise both arms

- Success condition summary:
- Expected success feedback:
- Expected retry/framing feedback:
- Known limitation:

### Side reach

- Left/right convention:
- Expected left success:
- Expected right success:
- Expected correction:
- Known limitation:

### Knee lift or step in place

- Success condition summary:
- Expected success feedback:
- Expected retry/framing feedback:
- Known limitation:

## 7. Camera and fallback behavior

- What the user sees before permission:
- Granted-permission behavior:
- Denied-permission behavior:
- No-camera behavior:
- Stop/reset behavior:
- Fallback selection procedure:
- Known browser-specific behavior:

## 8. Session and scoring

- Number/order of movements in the expected flow:
- Star/point rules visible to QA:
- Retry behavior:
- Reset behavior:
- Expected session summary fields:

## 9. Known defects and limitations

List only accepted non-blocking findings. Link each issue.

| Issue | Summary | User impact | Workaround | Release decision |
|---|---|---|---|---|
|  |  |  |  |  |

## 10. Privacy and evidence restrictions

- No child data.
- Do not attach raw volunteer recordings.
- Do not attach consent forms.
- Do not expose tokens, private paths, emails, or identifying backgrounds.
- Prefer screenshots without people, logs, JSON, and included fixtures.
- Delete temporary local uploads after testing where applicable.

Additional restrictions:

-

## 11. Bug reporting and triage

- **Bug template:** `.github/ISSUE_TEMPLATE/bug_report.yml`
- **QA plan:** `docs/qa_plan.md`
- **Development triage owner:**
- **Product/acceptance contact:**
- **Urgent escalation channel:**

Every bug must include tested commit, environment, reproduction steps, expected/actual result, severity proposal, and privacy-safe evidence.

## 12. Handoff approval checklist

- [ ] Release-candidate hash is recorded.
- [ ] CI is green for the candidate.
- [ ] Fresh installation has been rehearsed.
- [ ] README matches the candidate.
- [ ] All three movements have a documented expected result.
- [ ] Camera denial and fallback are documented.
- [ ] Fallback assets are committed and privacy-safe.
- [ ] Known defects are linked.
- [ ] Privacy and disclaimer content is visible.
- [ ] QA issues MP-028–MP-033 are ready.
- [ ] No unrelated merge is planned during the QA window.
