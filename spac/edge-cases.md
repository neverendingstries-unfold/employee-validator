# Edge Cases Checklist

1. Missing required field (e.g., no email)
2. Bad email format (missing @, or wrong domain)
3. Bad date format (e.g., 2023-01-01 instead of 01-01-23)
4. Salary out of range (e.g., 5000 or 200000000)
5. Non-numeric salary (e.g., "fifty thousand")
6. Duplicate employee ID
7. Empty file
8. Header-only file (no data rows)
9. Malformed row (wrong column count)
10. Whitespace/case in email
11. Blank line in middle of file
12. Bad encoding (non-UTF-8)
13. Missing file
14. Unreadable file