# Use Case 2: AI Coding Assistant Evidence

**Task:** Add server-side password reset validation  
**Analysis mode:** Deterministic sandbox output

**Result source:** Local deterministic fallback; no API request was made.  
**Model:** Not recorded  
**Provider endpoint:** Not recorded

## 1. Context and Prompt

**Role:** Backend developer maintaining a small Express authentication demo.

**Developer comment:** Validate the submitted password before reset and return a safe error without leaking credentials.

**Acceptance criteria:**
- Reject a missing or shorter-than-eight-character password.
- Do not expose the password or reset token in responses or logs.
- Preserve the existing successful reset response for valid input.

Repository context was restricted to the allowlisted sample files: myridius-auth-demo/auth/authController.js, myridius-auth-demo/auth/routes.js, myridius-auth-demo/server.js, myridius-auth-demo/views/resetPassword.html.

## 2. Assumptions and Limitations

- The sample Express app is illustrative and has no real database or token service.
- The requested change is guidance/evidence; the assistant does not edit application files.
- A human developer must adapt the response to the project test runner before acceptance.

## 3. Generated Code

```javascript
exports.handleReset = (req, res) => {
  const { password } = req.body;
  if (typeof password !== 'string' || password.length < 8) {
    return res.status(400).send('Password must be at least 8 characters.');
  }

  // In real app: update DB with new password
  return res.send('Password reset successful!');
};
```

The assistant proposes code only. It does not write this patch into the application.

## 4. Generated Tests

```javascript
describe('handleReset', () => {
  it('rejects a missing password without exposing request data', () => {
    const response = invoke({ body: {} });
    expect(response.statusCode).toBe(400);
    expect(response.body).not.toContain('undefined');
  });

  it('rejects passwords shorter than eight characters', () => {
    expect(invoke({ body: { password: 'short' } }).statusCode).toBe(400);
  });

  it('keeps the successful response for a valid password', () => {
    expect(invoke({ body: { password: 'valid-pass' } }).body)
      .toBe('Password reset successful!');
  });
});
```

## 5. Project Scaffolding

```text
myridius-auth-demo/auth/passwordPolicy.js
myridius-auth-demo/test/authController.test.js

// passwordPolicy.js
exports.isValidPassword = (password) =>
  typeof password === 'string' && password.length >= 8;

// authController.test.js
// Add unit coverage for missing, short, and valid passwords.
```

## 6. Chat Follow-up

- Why server-side validation? Client-side rules improve UX but cannot be trusted at an HTTP boundary.
- What remains uncertain? The real password policy, token validation, persistence, and test framework are not present in this sandbox.
- What should happen next? Confirm the product policy, add token/database tests, then have a human review the patch.

## 7. AI Review Checklist

- **High / Security:** The sample still lacks real reset-token validation and persistence safeguards. Remediation: Validate the token server-side, use a one-time expiry-aware store, and hash the new password before persistence.
- **Medium / Error handling:** The handler has no explicit malformed-body or downstream failure path. Remediation: Add centralized error middleware and a safe generic response for unexpected failures.
- **Medium / Testing:** There is no test runner or integration coverage in the sample repository. Remediation: Add isolated unit tests plus an HTTP test covering valid, invalid, and token-related requests.
- **Low / Maintainability:** The minimum length is a magic number. Remediation: Move the policy to a named constant or configuration value once requirements are confirmed.

## 8. Refactoring Recommendation

**Suggestion:** Extract password validation into a pure helper and keep the controller responsible for HTTP responses.

**Trade-off:** This improves unit-test isolation and makes policy changes clearer, but adds a file for a very small demo.

**Approval gate:** Do not apply the refactor until the team confirms the password policy and test conventions.

## 9. Prompt Iteration

**Baseline prompt:** Generate code for the password reset task.

**Revised prompt:** Generate code and tests, provide three chat answers, scaffold the test boundary, identify at least three review issues, explain behavior-preserving refactoring trade-offs, and state assumptions. Do not edit files; require human approval.

**Observed improvement:** The revised prompt makes the required evidence explicit, reducing incomplete outputs and making the result easier to review.

## 10. Before / After Evidence

**Before:** `handleReset` reads the request password and always returns success.

**After proposal:** the handler rejects missing or short passwords, returns a safe status, and preserves the valid-input response. Token validation and password persistence remain explicit follow-up work.

**Safety check:** no credentials, tokens, production endpoints, or application files were written by this demo. Human review is required before acceptance.
