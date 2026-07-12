# Dependency report

Dependencies are explicit in JSON and repeated in every generated issue body. Backlog position is dependency ordered; related QA evidence is represented separately to avoid circular blocking.

| Task | Blocking dependencies | Related coordination |
|---|---|---|
| MP-001 | None | None |
| MP-002 | MP-001 | None |
| MP-003 | MP-001 | None |
| MP-004 | MP-002, MP-003 | None |
| MP-005 | MP-002, MP-003 | None |
| MP-006 | MP-002, MP-003 | None |
| MP-007 | MP-005, MP-006 | None |
| MP-008 | MP-004 | None |
| MP-009 | MP-002, MP-008 | None |
| MP-010 | MP-008, MP-005, MP-006 | None |
| MP-011 | MP-006, MP-008 | None |
| MP-012 | MP-010, MP-011 | None |
| MP-013 | MP-005, MP-008, MP-010, MP-007 | None |
| MP-014 | MP-007, MP-013 | None |
| MP-015 | MP-007, MP-013, MP-014 | None |
| MP-016 | MP-007, MP-013, MP-014 | None |
| MP-017 | MP-014, MP-015, MP-016, MP-002 | None |
| MP-018 | MP-008, MP-017 | None |
| MP-019 | MP-010, MP-011, MP-012, MP-013, MP-014, MP-015, MP-016, MP-017, MP-018 | None |
| MP-020 | MP-007, MP-013, MP-009 | None |
| MP-021 | MP-014, MP-015, MP-016, MP-020 | None |
| MP-022 | MP-008, MP-013, MP-014, MP-015, MP-016, MP-018 | None |
| MP-023 | MP-010, MP-011, MP-012, MP-019, MP-009 | None |
| MP-024 | MP-019, MP-021, MP-022, MP-023 | None |
| MP-025 | MP-024 | MP-028, MP-029, MP-030, MP-031, MP-032, MP-033 |
| MP-026 | MP-025 | None |
| MP-027 | MP-001 | None |
| MP-028 | MP-024 | None |
| MP-029 | MP-024 | None |
| MP-030 | MP-024 | None |
| MP-031 | MP-024 | None |
| MP-032 | MP-024 | None |
| MP-033 | MP-024 | None |
| MP-034 | MP-024 | None |
| MP-035 | MP-024 | None |
| MP-036 | MP-024, MP-035 | None |
| MP-037 | MP-018, MP-023 | None |
| MP-038 | MP-037 | None |
| MP-039 | MP-024 | None |
| MP-040 | MP-039 | None |
| MP-041 | MP-024 | None |
| MP-042 | MP-024, MP-035 | None |
| MP-043 | MP-014, MP-015, MP-016 | None |
| MP-044 | MP-018, MP-043 | None |
| MP-045 | MP-021, MP-044 | None |
| MP-046 | MP-017, MP-018 | None |
| MP-047 | MP-011 | None |
| MP-048 | MP-035 | None |
| MP-049 | MP-021, MP-022 | None |
| MP-050 | MP-023, MP-036 | None |
| MP-051 | MP-023, MP-049 | None |
| MP-052 | MP-020, MP-037 | None |
| MP-053 | MP-020, MP-021, MP-052 | None |
| MP-054 | MP-021, MP-053 | None |
| MP-055 | MP-013, MP-054 | None |
| MP-056 | MP-013, MP-054 | None |
| MP-057 | MP-010, MP-019 | None |
| MP-058 | MP-036, MP-050, MP-051 | None |
| MP-059 | MP-037, MP-052 | None |
| MP-060 | MP-037, MP-044, MP-052 | None |
| MP-061 | MP-049, MP-057 | None |
| MP-062 | MP-035, MP-041, MP-051, MP-052, MP-054, MP-058, MP-059, MP-061 | None |
| MP-063 | MP-053, MP-054, MP-062 | None |
