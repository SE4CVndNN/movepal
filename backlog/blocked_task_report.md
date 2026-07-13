# Blocked-task report

A task marked blocked may begin required reading or a disposable spike, but dependency-sensitive implementation must be rechecked after prerequisites merge.

| Task | Initial status | Dependencies |
|---|---|---|
| MP-002 | blocked | MP-001 |
| MP-003 | blocked | MP-001 |
| MP-004 | blocked | MP-002, MP-003 |
| MP-005 | blocked | MP-002, MP-003 |
| MP-006 | blocked | MP-002, MP-003 |
| MP-007 | blocked | MP-005, MP-006 |
| MP-008 | blocked | MP-004 |
| MP-009 | blocked | MP-002, MP-008 |
| MP-010 | blocked | MP-008, MP-005, MP-006 |
| MP-011 | blocked | MP-006, MP-008 |
| MP-012 | blocked | MP-010, MP-011 |
| MP-013 | blocked | MP-005, MP-008, MP-010, MP-007 |
| MP-014 | blocked | MP-007, MP-010, MP-011, MP-013 |
| MP-015 | blocked | MP-007, MP-013, MP-014 |
| MP-016 | blocked | MP-007, MP-013, MP-014 |
| MP-017 | blocked | MP-014, MP-015, MP-016, MP-002 |
| MP-018 | blocked | MP-008, MP-017 |
| MP-019 | blocked | MP-010, MP-011, MP-012, MP-013, MP-014, MP-015, MP-016, MP-017, MP-018 |
| MP-020 | blocked | MP-007, MP-013, MP-009 |
| MP-021 | blocked | MP-014, MP-015, MP-016, MP-020 |
| MP-022 | blocked | MP-008, MP-013, MP-014, MP-015, MP-016, MP-018 |
| MP-023 | blocked | MP-010, MP-011, MP-012, MP-019, MP-009 |
| MP-024 | blocked | MP-019, MP-021, MP-022, MP-023 |
| MP-025 | blocked | MP-024 |
| MP-026 | blocked | MP-025 |
| MP-027 | blocked | MP-001 |
| MP-028 | blocked | MP-024 |
| MP-029 | blocked | MP-024 |
| MP-030 | blocked | MP-024 |
| MP-031 | blocked | MP-024 |
| MP-032 | blocked | MP-024 |
| MP-033 | blocked | MP-024 |
| MP-034 | blocked | MP-024 |
| MP-035 | blocked | MP-024 |
| MP-036 | blocked | MP-024, MP-035 |
| MP-037 | blocked | MP-018, MP-023 |
| MP-038 | blocked | MP-037 |
| MP-039 | blocked | MP-024 |
| MP-040 | blocked | MP-039 |
| MP-041 | blocked | MP-024 |
| MP-042 | blocked | MP-024, MP-035 |
| MP-043 | blocked | MP-014, MP-015, MP-016 |
| MP-044 | blocked | MP-018, MP-043 |
| MP-045 | blocked | MP-021, MP-044 |
| MP-046 | blocked | MP-017, MP-018 |
| MP-047 | blocked | MP-011 |
| MP-048 | blocked | MP-035 |
| MP-049 | blocked | MP-021, MP-022 |
| MP-050 | blocked | MP-023, MP-036 |
| MP-051 | blocked | MP-023, MP-049 |
| MP-052 | blocked | MP-020, MP-037 |
| MP-053 | blocked | MP-020, MP-021, MP-052 |
| MP-054 | blocked | MP-021, MP-053 |
| MP-055 | blocked | MP-013, MP-054 |
| MP-056 | blocked | MP-013, MP-054 |
| MP-057 | blocked | MP-010, MP-019 |
| MP-058 | blocked | MP-036, MP-050, MP-051 |
| MP-059 | blocked | MP-037, MP-052 |
| MP-060 | blocked | MP-037, MP-044, MP-052 |
| MP-061 | blocked | MP-049, MP-057 |
| MP-062 | blocked | MP-035, MP-041, MP-051, MP-052, MP-054, MP-058, MP-059, MP-061 |
| MP-063 | blocked | MP-053, MP-054, MP-062 |