# MovePal Privacy and Data-Handling Guide

## 1. Privacy objective

MovePal should demonstrate movement recognition while collecting and retaining as little personal data as possible. Privacy is part of the Definition of Done, not a task postponed until the final day.

## 2. Non-negotiable rules

- Sprint 1 requires no child data.
- Do not collect, request, upload, or publish recordings of children.
- Adult-volunteer collection requires approved informed consent.
- Prefer derived landmarks over raw images or video.
- Keep raw recordings outside GitHub, GitHub Actions, issue attachments, and pull requests.
- Do not log frames, images, personal identifiers, email addresses, or identifiable backgrounds.
- Do not commit secrets or private storage paths.
- Collect only what is required for a documented test or calibration purpose.

## 3. Sprint 1 data flow

### Live camera mode

The intended flow is:

```text
browser camera permission
→ capture a frame or short sample
→ send the minimum required input to Flask
→ extract pose landmarks
→ evaluate movement
→ return feedback
→ discard temporary media
```

The application should not silently save live frames. Any retention behavior must be explicit, documented, approved, and visible to the user.

### Fallback mode

Use included privacy-safe samples or derived fixtures. Samples must have known provenance and permission. Synthetic or landmark-only fixtures are preferred for automated tests.

### Adult calibration mode

Adult-volunteer collection is separate from normal gameplay and follows:

- [`consent_template.md`](consent_template.md)
- [`collection_protocol.md`](collection_protocol.md)
- [`annotation_guide.md`](annotation_guide.md)
- [`dataset_card.md`](dataset_card.md)

## 4. Data categories

### Allowed in the repository after review

- synthetic landmark fixtures;
- manually created non-identifying fixtures;
- derived landmarks from consented adults when publication/repository use is explicitly permitted;
- schemas and annotation examples;
- aggregated evaluation results;
- privacy-safe screenshots without people or identifying information.

### Private and excluded from Git

- raw adult images or video;
- signed consent records;
- participant contact information;
- mapping between anonymous IDs and identities;
- private collection logs;
- temporary uploads;
- unreviewed derived data.

Use ignored locations such as:

```text
data/raw/
data/private/
data/uploads/
```

Do not rely only on `.gitignore`; check `git status` before every commit.

## 5. Identifiers and filenames

Use anonymous IDs such as:

```text
P001_session01_raise_arms_correct
```

Do not include a participant’s name, initials, email, exact date of birth, address, workplace, or location in filenames or metadata.

Store the identity-to-ID mapping separately with restricted access only when it is needed for withdrawal requests.

## 6. Logging

Permitted logs may include:

- request success/failure category;
- selected movement code;
- generic validation error code;
- processing duration;
- application version or commit.

Do not log:

- raw request bodies containing media;
- raw frames or image bytes;
- complete landmark arrays from a real participant by default;
- participant IDs in general application logs;
- IP addresses beyond unavoidable server defaults without review;
- local private paths;
- consent details.

Use generic messages such as “input could not be decoded” rather than printing private filenames or stack traces to the user.

## 7. Browser and interface requirements

The UI should:

- explain why camera permission is requested;
- work through a fallback when permission is denied or no camera exists;
- display the non-medical prototype disclaimer;
- state whether frames are stored or processed transiently;
- avoid starting the camera before an intentional user action;
- provide a clear stop/reset control;
- avoid hidden recording indicators or misleading wording.

## 8. Consent and adult-volunteer collection

Before collection:

1. confirm the participant is an adult;
2. use an instructor/institution-approved consent form;
3. explain purpose, procedure, storage, access, retention, publication, risks, and withdrawal;
4. receive consent before recording;
5. assign an anonymous ID;
6. collect only the minimum examples required by the test matrix.

Consent for this activity does not authorize unrelated future use.

## 9. Retention and deletion

The collection owner must document:

- where raw and derived data are stored;
- who has access;
- the retention period;
- how temporary copies are removed;
- how a participant requests withdrawal using the anonymous ID;
- which derived/public artifacts can still be deleted;
- whether already aggregated anonymous results can be separated.

A withdrawal or deletion request must be recorded privately and completed across all known copies under the team’s control.

## 10. QA, issues, and pull-request evidence

Use evidence that demonstrates behavior without exposing people:

- test logs;
- JSON responses;
- synthetic fixtures;
- cropped UI screenshots with no person visible;
- diagrams;
- redacted screenshots;
- short approved adult-derived material only when absolutely necessary and explicitly permitted.

Never attach raw volunteer recordings or consent forms to GitHub.

## 11. Security controls

- Validate file type and size before processing.
- Never construct a path from an untrusted filename without safe handling.
- Delete temporary uploads after processing.
- Keep debug mode disabled outside controlled local use.
- Do not commit `.env` or tokens.
- Use minimal GitHub Actions permissions.
- Do not upload private data as CI artifacts.

## 12. Student checklist

Before merging a data- or media-related PR, confirm:

- [ ] No child data is included.
- [ ] Provenance and permission are documented.
- [ ] Raw private media is outside Git.
- [ ] Logs contain no personal or media data.
- [ ] Tests use privacy-safe fixtures.
- [ ] Temporary files are cleaned up.
- [ ] UI wording accurately describes processing/storage.
- [ ] Documentation reflects any data-flow change.
- [ ] The reviewer checked privacy impact.
