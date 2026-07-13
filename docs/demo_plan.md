# MovePal Final Demonstration Plan

## 1. Purpose

The final demonstration should prove that the team delivered a coherent Sprint increment, not only separate components. It should show the user journey, engineering workflow, automated quality evidence, privacy boundaries, external QA result, and known limitations.

Target duration: **10–12 minutes**, leaving time for questions and transition.

## 2. Demonstration rules

- Demonstrate the frozen/released commit, not an uncommitted local version.
- Prepare and test the fallback path before attempting live camera input.
- Use no child data.
- Do not show private recordings, consent records, tokens, or local private paths.
- Do not make medical or rehabilitation claims.
- Keep the presentation focused on completed Sprint 1 acceptance criteria.
- State known limitations honestly.

## 3. Roles

Assign and record presenters before the final rehearsal:

| Segment | Presenter | Backup |
|---|---|---|
| Problem, users, Sprint Goal, disclaimer |  |  |
| Scrum/GitHub process and contribution evidence |  |  |
| Architecture and backend/API |  |  |
| Pose and movement rules |  |  |
| Frontend, camera, feedback, score, summary |  |  |
| Tests, CI, QA, limitations, close |  |  |

Every development member should be able to explain their own contribution, even if not every member speaks for the same duration.

## 4. Required pre-demo preparation

At least one day before the demo:

- freeze the release candidate;
- run fresh installation on a second environment;
- confirm Windows and Linux CI;
- verify all three movement paths;
- verify camera-denied and fallback behavior;
- verify invalid-input handling;
- prepare privacy-safe sample files;
- prepare a short backup recording or screenshots of expected behavior;
- close or document critical QA findings;
- update README, privacy, limitations, and known defects;
- rehearse within 10–12 minutes.

## 5. Suggested live sequence

### 0:00–1:00 — Project and boundary

Explain:

- the user problem and playful goal;
- the Sprint Goal;
- the three movements;
- that MovePal is a prototype, not a medical or diagnostic system;
- that no child data was collected.

### 1:00–2:00 — Scrum and engineering workflow

Show briefly:

- the Sprint board;
- one representative issue;
- its feature branch and pull request;
- independent review;
- passing CI;
- the merged result.

Do not spend the demo reading the entire backlog.

### 2:00–3:00 — Architecture

Show the pipeline:

```text
browser camera/fallback
→ Flask validation
→ pose landmarks
→ visibility/movement rules
→ feedback and scoring
→ UI and session summary
```

Mention deterministic fixtures and cross-platform CI.

### 3:00–8:00 — Product demonstration

1. Open the application and show the disclaimer.
2. Select live camera or explain the fallback choice.
3. Demonstrate raise both arms.
4. Demonstrate left/right side reach.
5. Demonstrate knee lift or step in place.
6. Show at least one incorrect, low-visibility, or framing case.
7. Show friendly correction and retry.
8. Show stars/points.
9. Complete the session and show the summary.
10. Show reset/repeat behavior if time permits.

### 8:00–9:00 — Robustness

Show one or two of:

- denied camera permission and fallback;
- invalid/unsupported input;
- oversized-file handling;
- missing body/low visibility;
- safe error message without stack trace or private path.

### 9:00–10:00 — Quality evidence

Show:

- Windows and Linux CI;
- test summary;
- external QA status;
- one defect and its fix/retest if useful;
- the frozen commit/tag.

### 10:00–11:00 — Limitations and future work

Explain the most important limitations:

- pose uncertainty;
- lighting, camera angle, framing, and occlusion;
- heuristic thresholds;
- small adult-only calibration scope;
- no medical validation;
- future backlog direction.

### 11:00–12:00 — Close

Restate the Sprint Goal achieved, acknowledge remaining documented issues, and invite questions.

## 6. Fallback plan

Use the fallback immediately when:

- camera permission cannot be granted;
- the browser/device has no camera;
- lighting or framing prevents a stable demo;
- the live pose provider fails;
- network/environment behavior threatens the time limit.

Fallback assets must:

- be committed or otherwise available before the demo;
- have documented provenance;
- contain no child data;
- reproduce expected movement and error cases;
- use the same real application path, not a hard-coded fake result.

## 7. Demonstration evidence checklist

- [ ] Release-candidate commit/tag is recorded.
- [ ] Fresh setup commands work.
- [ ] Live camera was rehearsed.
- [ ] Fallback was rehearsed independently.
- [ ] All three movements have a success case.
- [ ] At least one retry/framing case is shown.
- [ ] Points/stars and session summary are shown.
- [ ] Invalid-input or permission behavior is shown.
- [ ] Privacy and disclaimer are visible.
- [ ] CI and QA evidence are ready.
- [ ] Known limitations are stated.
- [ ] No private or identifying content appears.
- [ ] Presentation fits within 10–12 minutes.

## 8. After the demonstration

Record:

- final demonstrated commit;
- important questions and answers;
- defects discovered during the demo;
- release decision;
- retrospective observations;
- which future backlog items are most valuable next.
