# Add audit logging for failed password reset attempts

## Story
As an operator, I want failed password reset attempts logged so I can investigate suspicious account activity.

## Acceptance Criteria
- Every failed reset attempt produces a structured log entry.
- The log captures the request context and a failure reason.
- The change does not block the existing reset flow.

## Clarification
- The repository is a sandbox password reset demo with a simple Express server.
- Assumption: the request is for implementation guidance rather than changing production code directly.
- Approval gate: a human reviewer should approve any code change before it is merged.

## Impacted Files
- myridius-auth-demo/auth/authController.js
- myridius-auth-demo/server.js
- myridius-auth-demo/auth/routes.js

## Implementation Plan
- Wrap the reset handler with a small logging helper that records failures.
- Emit a structured log entry for invalid tokens and missing passwords.
- Leave the primary UX intact and require human approval before shipping the logging policy.

## Test Cases
- Unit: records a failure when the reset token is invalid.
- Unit: records a failure when a password is missing from the request body.
- Integration: confirms the reset flow still returns a safe response after logging.

## Review Findings
- Improves supportability and security observability.
- Ensure logs avoid leaking secrets or personally identifiable information.
- Consider a dedicated logger abstraction before expanding to more features.

## PR Summary
- This PoC demonstrates a story-to-PR workflow over a sandbox authentication repository.
- Repo context used for planning:
- Sample app entry point: const express = require('express');
- Auth routes: const express = require('express');
- Current reset handler: exports.showResetForm = (req, res) => {
- Next step: review the proposed changes, confirm the approval gate, and decide whether to implement them in the sample app.
