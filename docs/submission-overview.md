# AI Developer Assistant PoC: Submission Overview

## 1. Purpose

This proof of concept demonstrates two related ways an AI assistant can support a software developer working on a sandbox password-reset application:

1. **Use Case 1: AI Agent, story to PR readiness**
2. **Use Case 2: AI Coding Assistant, task to code and review evidence**

Both use cases use the same anonymized Express repository. The difference is the developer workflow being demonstrated.

## 2. Use Case 1: Story to PR Readiness

### Scenario

A developer submits a ticket asking for a clearer confirmation page after a successful password reset.

### Input

The ticket is stored in [tickets/new-ticket.json](../tickets/new-ticket.json) and contains:

- A unique ticket ID
- A ticket title
- A user story
- Acceptance criteria

### Agent behavior

[agent-demo.py](../agent-demo.py) performs the orchestration:

1. Loads the ticket.
2. Selects only the intake fields for the AI prompt.
3. Reads the allowlisted repository files.
4. Sends the ticket and repository context to the OpenAI API.
5. Requires a structured JSON response.
6. Preserves the local ticket ID.
7. Writes a Markdown report.

### Output

The report contains:

- Clarification and assumptions
- Impacted files
- Implementation plan
- Test cases
- Review findings
- PR summary
- Repository evidence

Example evidence: [markdown_docs/ticket-6/report.md](../markdown_docs/ticket-6/report.md).

### Value

This use case reduces the manual effort required to move from a vague or incomplete ticket to a reviewable implementation plan. It keeps traceability between the original story, repository context, proposed work, tests, risks, and PR handoff.

## 3. Use Case 2: Coding Task to Reviewed Proposal

### Scenario

A backend developer comments: “Validate the submitted password before reset and return a safe error without leaking credentials.”

### Input and role context

The task is defined in [coding-assistant-demo.py](../coding-assistant-demo.py) with:

- Task ID and title
- Developer comment
- Backend developer role
- Acceptance criteria
- Explicit repository and safety rules

Prompt variants are documented in [docs/use-case-2-prompts.md](use-case-2-prompts.md).

### Assistant behavior

[coding-assistant-demo.py](../coding-assistant-demo.py) provides a narrower interactive coding workflow:

1. Loads the backend developer role and task.
2. Reads the same allowlisted Express files.
3. Sends task, role, rules, and repository context to OpenAI in live mode.
4. Requests code, tests, scaffolding, chat answers, review findings, refactoring guidance, and prompt-iteration evidence.
5. Validates and stores the response as Markdown and JSON.
6. Stops at a human approval gate.

### Output

The evidence report includes:

- Proposed controller validation
- Negative-path and valid-input tests
- Suggested project scaffolding
- Follow-up explanations
- Security and maintainability findings
- Refactoring trade-offs
- Baseline versus revised prompt comparison

Example evidence: [markdown_docs/use-case-2/evidence.md](../markdown_docs/use-case-2/evidence.md).

### Value

This use case demonstrates interactive coding assistance after a task has been identified. It shows that the assistant can generate a focused proposal and then challenge its own output by identifying token-validation, error-handling, persistence, and test-coverage gaps.

## 4. Tools and Responsibilities

| Tool or component | Responsibility | Evidence |
|---|---|---|
| VS Code | Inspect code, tickets, prompts, and reports; present the demo | Workspace and Markdown files |
| Git/GitHub | Version, retrieve, and share the anonymized repository | Git repository and remote |
| PowerShell | Set environment variables and run commands | Demo scripts |
| Python 3 | Execute the local orchestration programs | `agent-demo.py`, `coding-assistant-demo.py` |
| OpenAI API | Provide live language-model analysis | AI-mode provenance in Use Case 2 and `Analysis mode: AI-generated` in Use Case 1 |
| `agent-demo.py` | Coordinate ticket analysis and PR-readiness report generation | [agent-demo.py](../agent-demo.py) |
| `coding-assistant-demo.py` | Coordinate focused coding-assistant generation and review | [coding-assistant-demo.py](../coding-assistant-demo.py) |
| Node.js and npm | Run the sandbox Express application when demonstrating the target code | [myridius-auth-demo/package.json](../myridius-auth-demo/package.json) |
| Express and body-parser | Provide the sample backend and form-body handling | `myridius-auth-demo` dependencies |
| JSON | Define ticket and structured assistant inputs/outputs | `tickets/*.json`, `result.json` |
| Markdown | Preserve human-readable evidence and handoff reports | `markdown_docs` |
| Mermaid | Render the orchestration architecture | [architecture-diagram.md](architecture-diagram.md) |

## 5. Shared Repository Context

The AI tools use only these sandbox files:

- [myridius-auth-demo/server.js](../myridius-auth-demo/server.js): starts Express and registers `/auth` routes.
- [myridius-auth-demo/auth/routes.js](../myridius-auth-demo/auth/routes.js): maps GET and POST password-reset requests.
- [myridius-auth-demo/auth/authController.js](../myridius-auth-demo/auth/authController.js): displays the reset form and handles the submitted password.
- [myridius-auth-demo/views/resetPassword.html](../myridius-auth-demo/views/resetPassword.html): provides the reset form UI.

This context makes the model's recommendations repository-aware. It also limits the data sent to the provider.

## 6. End-to-End Flow

```text
Developer task or ticket
        |
        v
Local Python orchestrator
        |
        +--> ticket/task reader
        +--> allowlisted repository reader
        +--> prompt and role rules
        |
        v
OpenAI API
        |
        v
Structured response validation
        |
        +--> Markdown report
        +--> JSON evidence where applicable
        |
        v
Learner review and approval
        |
        v
Optional implementation by the learner
```

The local programs do not upload themselves to OpenAI. They send selected text as an API request. The API key is supplied through `OPENAI_API_KEY` and is never placed in a prompt, ticket, or report.

## 7. Commands for Demonstration

### Use Case 1 live run

```powershell
$env:OPENAI_API_KEY = "your-api-key"
$env:OPENAI_MODEL = "gpt-4o-mini"
python agent-demo.py --ai tickets/new-ticket.json
```

Review the generated report for the ticket ID under `markdown_docs`.

### Use Case 2 live run

```powershell
python coding-assistant-demo.py --ai
```

Review:

- [markdown_docs/use-case-2/evidence.md](../markdown_docs/use-case-2/evidence.md)
- [markdown_docs/use-case-2/result.json](../markdown_docs/use-case-2/result.json)

### Offline validation

```powershell
python agent-demo.py tickets/new-ticket.json
python coding-assistant-demo.py
```

Offline mode validates local report generation but is not evidence of a live LLM call.

## 8. Safety and Human Oversight

The PoC follows these boundaries:

- Only sandbox or anonymized code is used.
- No customer data, production code, credentials, or secrets belong in the repository.
- API keys are environment variables and are excluded by [.gitignore](../.gitignore).
- The assistants generate recommendations and evidence only.
- They do not edit application files, auto-merge, auto-deploy, or approve changes.
- Learners review the generated code, tests, risks, and assumptions before implementation.

The complete constraint mapping is in [constraint-compliance.md](constraint-compliance.md).

## 9. Evaluation Evidence Map

| Expected capability | Demonstrated by |
|---|---|
| Tool use | Allowlisted repository reader, ticket reader, OpenAI API call, Markdown/JSON writers |
| Multi-step planning | Use Case 1 clarification, impact analysis, plan, testing, review, and handoff sections |
| Context management | Role prompts, `.agent.md`, `config.toml`, allowlisted repository context, and output contracts |
| Human-in-the-loop | Explicit approval gates in both use cases and no-edit behavior |
| AI-assisted review | Use Case 1 review findings and Use Case 2 severity-based review output |
| Test proposals | Test sections in both generated reports |
| Traceability | Ticket/task input linked to repository evidence and generated reports |

## 10. Presentation Order

For a cohesive presentation:

1. Explain the developer problem.
2. Introduce the shared sandbox repository.
3. Present Use Case 1 as the ticket-to-PR workflow.
4. Show the OpenAI connection and generated report.
5. Present Use Case 2 as the focused coding-task workflow.
6. Show generated code, tests, review findings, and refactoring trade-offs.
7. Explain the shared safety controls and human approval gate.
8. Close with productivity benefits, limitations, and production-readiness considerations.

This order gives the evaluator one continuous story: intake, context, reasoning, proposal, review, approval, and optional implementation.
