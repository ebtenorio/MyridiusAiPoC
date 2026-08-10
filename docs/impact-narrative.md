# Impact Narrative

## Expected Time Savings
This PoC reduces the effort needed to translate a ticket into an implementation plan by giving developers a structured starting point for analysis, design, testing, review, and PR handoff. A measured production result still requires a baseline and repeated ticket trials.

## Productivity Gain
Teams can use the workflow to accelerate repository discovery, improve consistency, surface security concerns earlier, and reduce boilerplate planning work. The developer remains responsible for technical decisions and approval.

## Limitations
- The demo uses a small sandbox repository and therefore does not capture the full complexity of production systems.
- The generated plan should still be reviewed by a developer before code is changed.
- The approach depends on the quality of the repository context and the prompt instructions.
- Model output can be incomplete, conservative, or incorrect; structured validation does not guarantee correctness.
- The current repository reader is intentionally narrow and does not run tests, lint, or a mock API.

## Production Readiness Considerations
- Add a secure tool layer for real repository access and test execution.
- Introduce stronger approval and audit controls for change execution.
- Connect the workflow to real CI pipelines for evidence-based review.
- Add access controls, redaction, retention policies, rate-limit handling, and cost monitoring.
- Add deterministic automated tests for the ticket schema, API response schema, and report output.

## Suggested measurement plan

- Record baseline time from ticket intake to first implementation plan.
- Compare AI-assisted and manual completion time across at least 10 anonymized tickets.
- Measure reviewer correction rate for impacted files, tests, and review findings.
- Track API cost per ticket and the percentage of reports requiring clarification.
