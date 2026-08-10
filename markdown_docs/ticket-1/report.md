# Add client-side validation to the password reset form

## Story
As a user, I want clear feedback when I submit an invalid password reset so I can recover my account without confusion.

## Acceptance Criteria
- The form shows inline validation for short or missing passwords.
- The submit flow stops before the reset request is sent when validation fails.
- The experience remains usable on mobile and desktop.

## Clarification
- The repository is a sandbox password reset demo with a simple Express server.
- Assumption: the request is for implementation guidance rather than changing production code directly.
- Approval gate: a human reviewer should approve any code change before it is merged.

## Impacted Files
- myridius-auth-demo/views/resetPassword.html
- myridius-auth-demo/auth/authController.js
- myridius-auth-demo/auth/routes.js

## Implementation Plan
- Add a minimal validation rule in the reset form before the request is posted.
- Surface server-side feedback in the controller so the UI can show a helpful error message.
- Keep the change localized to the password reset flow to avoid broad regressions.

## Test Cases
- Unit: validates a password shorter than 8 characters.
- Unit: accepts a password meeting the minimum strength requirement.
- Integration: prevents submission when validation fails and preserves the existing form state.

## Review Findings
- Readable and localized change with low complexity.
- Security risk remains low because the validation is client-side and should be mirrored server-side.
- Consider adding a stronger password policy once the product requirements are finalized.

## PR Summary
- This PoC demonstrates a story-to-PR workflow over a sandbox authentication repository.
- Repo context used for planning:
- Sample app entry point: const express = require('express');
- Auth routes: const express = require('express');
- Current reset handler: exports.showResetForm = (req, res) => {
- Next step: review the proposed changes, confirm the approval gate, and decide whether to implement them in the sample app.
