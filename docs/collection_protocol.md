# MovePal Adult-Only Collection Protocol

## 1. Scope

This protocol applies only when Sprint 1 tasks require a small number of adult-volunteer samples for landmark extraction, threshold calibration, usability checks, or regression fixtures.

Collection is optional unless the instructor approves it and the task cannot be completed with synthetic, licensed, or existing privacy-safe fixtures.

No child data may be collected.

## 2. Roles

Before collection, identify:

- collection lead;
- consent administrator;
- recording operator;
- landmark-extraction owner;
- annotation owner;
- privacy/release reviewer;
- private deletion/withdrawal contact.

One person may hold multiple roles in a small course exercise, but responsibilities must remain explicit.

## 3. Pre-collection approval

Do not record until all items are complete:

- [ ] The participant is confirmed to be an adult.
- [ ] The instructor approves the purpose and minimum sample plan.
- [ ] The consent template has been reviewed for the course/institution.
- [ ] The participant has had time to ask questions.
- [ ] Signed consent is obtained before recording.
- [ ] An anonymous participant ID is assigned.
- [ ] Private raw-storage and access rules are ready.
- [ ] Required movements and correct/incorrect cases are listed.
- [ ] The deletion/withdrawal process is understood.

## 4. Minimize collection

Create a test matrix before recording. Collect only the examples required to cover planned cases, such as:

- clear correct attempt;
- intentionally incomplete attempt;
- borderline attempt;
- partial body/framing failure;
- low-visibility condition;
- left and right side where relevant.

Do not collect long continuous sessions when short clips or selected frames are sufficient.

## 5. Recording environment

Use a safe, neutral environment where possible:

- avoid identifiable addresses, documents, screens, photographs, or bystanders;
- avoid recording audio unless explicitly required and consented (Sprint 1 normally does not require audio);
- use adequate but not overly revealing lighting;
- position the camera according to the test matrix;
- explain when recording starts and stops;
- allow the participant to pause or stop at any time;
- do not pressure participants to perform uncomfortable movement.

MovePal is not a medical activity. Participants choose whether to attempt each movement.

## 6. Anonymous naming

Use filenames such as:

```text
P001_S01_raise_arms_positive_001.mp4
P001_S01_side_reach_left_borderline_001.mp4
```

Do not include name, email, address, workplace, exact birth date, or location.

The identity-to-ID mapping and signed consent record remain in separate restricted storage outside GitHub.

## 7. Raw storage

Store raw recordings only in approved private locations such as:

```text
data/private/
data/raw/
```

These paths are ignored by Git, but students must still verify `git status` before committing.

Document:

- storage owner;
- access list;
- encryption/device protection where available;
- backup policy;
- retention end date;
- deletion method.

Do not place raw recordings in shared chat, GitHub issues, PRs, Actions artifacts, or public cloud links.

## 8. Collection procedure

For each sample:

1. Confirm anonymous ID and consent status.
2. State the movement and requested side.
3. Confirm whether the sample is intended as positive, negative, borderline, visibility, or framing evidence.
4. Start recording only for the minimum required duration.
5. Stop and review whether the sample matches the intended category.
6. Record non-identifying environment notes.
7. Repeat only when necessary.
8. Allow the participant to request immediate deletion.

Do not label an accidental or ambiguous movement as a verified case merely to fill the dataset.

## 9. Landmark extraction

Perform extraction locally:

1. Read from private raw storage.
2. Use the documented pose-service/schema version.
3. Export only required landmarks and metadata.
4. Remove raw filenames and identifying paths from the derived file.
5. Assign a stable fixture ID.
6. Validate coordinate range, visibility values, required fields, and movement label.
7. Record provenance and consent status.
8. Store derived data in a review area before committing.

## 10. Annotation and review

Follow [`annotation_guide.md`](annotation_guide.md).

A second reviewer should check:

- movement and side label;
- expected outcome;
- category;
- visibility/framing interpretation;
- provenance status;
- absence of identifiers;
- suitability for repository use.

Ambiguous samples should be corrected, reclassified, or excluded.

## 11. Quality checks

Before using a fixture:

- [ ] Required fields are present.
- [ ] Coordinates and visibility values are valid.
- [ ] Anatomical left/right follows the project convention.
- [ ] Expected result is independently reviewed.
- [ ] Provenance is known.
- [ ] Consent allows the derived use.
- [ ] No private path or identity remains.
- [ ] The fixture adds useful coverage rather than duplicating another case.

## 12. Retention and cleanup

After extraction/review:

- delete unnecessary temporary copies;
- update the private inventory;
- retain raw media only for the documented period/purpose;
- record any participant withdrawal;
- remove all controlled copies when deletion is required;
- update the dataset card and version history.

## 13. Stop conditions

Stop collection and notify the instructor when:

- a participant is not an adult;
- consent is missing or unclear;
- a participant withdraws;
- the requested movement causes discomfort;
- identifying bystanders/backgrounds cannot be avoided;
- private storage is not available;
- data appears in Git or another unauthorized location;
- the planned purpose changes beyond the consent scope.
