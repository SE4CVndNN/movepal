# MovePal Limitations and Disclaimer

## 1. Required disclaimer

MovePal is a playful movement-practice prototype created for software-engineering education. It is not a medical device, diagnostic tool, rehabilitation system, treatment, or replacement for a physiotherapist or healthcare professional.

A success result means only that the current pose landmarks satisfied the project’s configured game rules. It does not establish that a movement is medically correct, safe for a particular person, or beneficial for a health condition.

## 2. Technical limitations

### Pose-estimation uncertainty

The pretrained pose model can miss or misplace landmarks. Visibility/confidence values are estimates, not guarantees.

### Camera and environment

Results can change because of:

- low or uneven lighting;
- strong backlighting;
- camera angle or height;
- user distance from the camera;
- image blur;
- low camera resolution;
- cropped body parts;
- occlusion by furniture or another person;
- cluttered backgrounds;
- clothing that reduces landmark visibility.

### Multiple people

Sprint 1 may not reliably support multiple people in the frame. The application should avoid selecting an arbitrary person without explaining the limitation.

### Browser and hardware variation

Camera permission, media formats, browser APIs, and performance vary across operating systems, browsers, and devices. A tested fallback sample is therefore mandatory.

### Performance

Processing periodic frames through Flask is appropriate for the prototype but is not designed as low-latency continuous production streaming.

## 3. Rule-based movement limitations

The movement rules use configurable relative-position or joint/landmark heuristics. They do not model the full quality, safety, speed, balance, comfort, or intent of a real movement.

Thresholds may be affected by:

- body proportions;
- mobility range;
- standing or seated posture;
- camera perspective;
- left/right mirroring;
- loose clothing;
- assistive devices;
- incomplete calibration data.

A rule may return a false success or false retry. The application should provide a low-confidence/unable-to-evaluate path and should not force a positive classification.

## 4. Movement-specific limitations

### Raise both arms

The rule can detect relative wrist/shoulder position but cannot determine whether the movement is comfortable, symmetrical, medically appropriate, or maintained safely.

### Side reach

Camera mirroring and anatomical left/right interpretation can cause confusion. The UI, pose service, specification, and tests must use one documented convention.

### Knee lift or step in place

Leg landmarks may leave the frame or be occluded. A single image may not reliably distinguish a knee lift from a transitional pose or a step sequence.

## 5. Human variation and fairness

A small convenience sample cannot represent all bodies, movement styles, clothing, environments, or accessibility needs. The team must document who and what was included in calibration and avoid claims of broad fairness or generalization.

MovePal must not grade a person’s physical ability, compare participants, or infer health/disability status.

## 6. Data and evaluation limitations

Sprint 1 fixtures and adult-volunteer calibration data are small and intended only to test software behavior and tune transparent prototype thresholds.

They are not:

- a clinical dataset;
- a representative population sample;
- evidence of treatment effectiveness;
- sufficient for medical validation;
- suitable for unrestricted model training.

Reported accuracy or pass rates must state the sample size, fixture source, test conditions, and limitations.

## 7. Privacy limitations

Camera input and adult-volunteer recordings may contain identifiable visual information. The project reduces risk through transient processing, minimal collection, derived landmarks, private storage, and consent, but these measures do not eliminate all privacy risk.

No child data is permitted.

## 8. Accessibility limitations

Sprint 1 targets basic keyboard use, readable feedback, understandable controls, and a responsive layout. It does not claim full conformance with every accessibility standard or suitability for every motor, visual, cognitive, or sensory need.

Feedback should not shame users or treat one movement style as a statement about ability.

## 9. Language and interpretation

Friendly messages describe the prototype’s current observation. They should remain simple, supportive, and non-medical. Arabic localization may be incomplete in Sprint 1; one complete language is preferable to partially translated critical instructions.

## 10. Operational limitations

- The application is not an emergency service.
- It is not intended for unsupervised clinical use.
- It is not production-hardened.
- The starter repository and Sprint increment may contain known non-critical defects documented in issues.
- A live camera demonstration may fail because of environment or permission differences; use the prepared fallback.

## 11. Prohibited claims

Do not claim that MovePal:

- diagnoses a condition;
- corrects rehabilitation exercises;
- measures recovery;
- replaces a professional;
- is safe for every user;
- is accurate for every body or environment;
- has been clinically validated;
- protects privacy absolutely.

## 12. Reporting a limitation

When a limitation is discovered:

1. reproduce it with privacy-safe evidence;
2. record environment and tested commit;
3. decide whether it is a defect, documented limitation, or future improvement;
4. update the relevant issue and documentation;
5. avoid hiding it with hard-coded demo behavior;
6. add a regression test when practical.
