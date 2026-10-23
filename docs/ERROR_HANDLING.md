# Error Handling

Errors should be actionable without exposing internal secrets or sensitive data.

- Validate input at application boundaries.
- Use consistent error responses.
- Log diagnostic context without passwords, tokens, or sensitive payloads.
- Distinguish expected validation failures from unexpected system failures.
- Add regression tests for fixed error conditions.
