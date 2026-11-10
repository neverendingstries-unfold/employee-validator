# Acceptance criteria — Employee Record Validator

## Valid record
A record is valid if ALL of:
- `employee_id`: present, non-empty after trim, unique within the file.
  The first row with a given ID is valid; later rows with the same ID are
  rejected with reason `duplicate employee_id`.
- `email`: matches `^[a-z0-9._-]+@company\.com$`, case-insensitive.
- `hire_date`: parses as `DD-MM-YY`.
- `salary`: parses as a number, between 118000 and 120000000 inclusive
  (formatted: 1,18,000 to 12,00,00,000). Non-numeric salary is a rejection
  reason, not a crash.
- `role`: optional, free text, not validated.
- `experience`: optional float; if empty, ignored; if present, must parse as
  float in 0–40 inclusive.
- Required fields — `employee_id`, `email`, `hire_date`, `salary` — are
  non-empty after trimming.

## Rejected record
A record is rejected if any of the above fails.
Each rejected row in the report must include:
- row number
- `employee_id`, or `<missing>` if absent
- ALL reasons it failed, not just the first

A row with the wrong number of columns is rejected with reason
`malformed row`; processing continues.
Blank lines are skipped, not reported as rejected.

## File handling
- Missing / unreadable / non-CSV file: message to stderr, exit code 1,
  no report printed.
- File that does not decode as UTF-8: treated as unreadable — stderr, exit 1.
- Readable file (even with rejected rows): full report to stdout, exit code 0.
- Empty file or header-only file: report to stdout showing 0 rows read,
  exit 0 — the file was readable, there was simply no data to validate.

## Out of scope for Week 1
- `role` is not validated.
- No email uniqueness check.
- No cross-file duplicate detection (uniqueness is within one file only).
- No name-based email rule.
- No validation of numeric edge cases beyond parse and range.