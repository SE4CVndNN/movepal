# Data Directory

- `samples/`: tiny, non-sensitive fallback samples approved for version control.
- `schemas/`: landmark and annotation schemas (`movement_fixture.schema.json`).
- `landmarks/`: derived anonymous landmarks where publication is permitted (24 schema-validated movement fixtures across `tuning` and `held_out` splits).
- `raw/` and `private/`: never committed; reserved for consented adult-volunteer recordings.

Run `python scripts/evaluate_rules.py` to evaluate rule performance against all 24 fixtures and generate the calibration summary.

No child data is required or collected.
