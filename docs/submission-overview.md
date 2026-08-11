# AI Developer Assistant PoC: Submission Overview

## 1. Purpose

This proof of concept demonstrates two related ways an AI assistant can support a software developer working on a sandbox password-reset application:

1. **Use Case 1: AI Agent, story to PR readiness**
2. **Use Case 2: AI Coding Assistant, task to code and review evidence**

Both use cases use the same anonymized Express repository. The difference is the developer workflow being demonstrated.

### How to read this submission

Read this document first. It explains the problem, the relationship between the two use cases, the tools, and the evidence. Then use the links below in this order:

1. Read the Use Case 1 report to see how a ticket becomes a reviewable plan.
2. Read the Use Case 2 evidence to see how a coding task becomes a code-and-review proposal.
3. Use the demo scripts to reproduce the workflows.
4. Use the architecture, tool evidence, review, reflection, and constraint documents as supporting detail.

The two use cases are deliberately sequential. Use Case 1 starts with a product-level story and establishes what should be changed. Use Case 2 starts with a developer-level task and explores how the change could be designed, tested, and reviewed. Neither workflow applies code automatically; both end with human approval.

## 2. Submission at a Glance

| Use case | Developer problem | Input | Main output | What it demonstrates |
|---|---|---|---|---|
| 1. Story to PR readiness | Turn a backlog ticket into work that is ready for developer review. | `tickets/new-ticket.json` | A structured Markdown report for the ticket. | Requirements clarification, repository-aware planning, test proposals, risk review, and PR handoff. |
| 2. Coding task to reviewed proposal | Turn a developer comment into a focused code proposal and review. | A defined coding task and role context in `coding-assistant-demo.py` | Markdown and JSON evidence containing code, tests, review findings, and refactoring guidance. | Interactive coding assistance, prompt iteration, security review, and human approval. |

Both workflows are local Python demonstrations. Deterministic mode does not need the internet. Live AI mode sends selected sandbox context to the configured OpenAI-compatible HTTPS endpoint. The Express application is separate: it is run locally with Node.js only when demonstrating the password-reset page in a browser. Neither workflow requires public hosting.

## 3. Project in Plain Language

The project uses a small password-reset application as a realistic but safe setting for demonstrating AI-assisted development. The sample application is not the product being built; it is the codebase that gives both AI workflows something concrete to inspect. A ticket asks for a clearer success experience, while a backend task asks for server-side password validation. The AI tools analyze those requests and produce recommendations. A developer remains responsible for deciding whether the recommendations are correct and for implementing and testing any approved change.

The application itself is intentionally simple. `server.js` starts Express and serves the `views` directory. `routes.js` maps GET and POST requests for `/auth/reset-password/:token`. `authController.js` displays the reset form and currently returns a success message without real token validation or database persistence. That limitation is useful evidence: the assistants can identify the missing security and testing work instead of presenting a small demonstration as production-ready authentication.

## 4. Technology Architecture

| Technology | How it is used | Why it is appropriate for this PoC |
|---|---|---|
| Python 3 | Runs `agent-demo.py` and `coding-assistant-demo.py`, reads local files, calls the API in live mode, validates responses, and writes evidence. | Provides a small, inspectable orchestration layer without requiring an agent framework. |
| OpenAI-compatible Chat Completions API | Receives the selected ticket/task and allowlisted repository context and returns structured language-model analysis. | Demonstrates live AI assistance while allowing the provider or model to be configured through environment variables. |
| JavaScript and Node.js | Runs the anonymized sample application. | Represents the backend codebase that the AI tools analyze. |
| Express | Serves the reset form and maps the reset-password routes. | Keeps the target application small enough to understand during a presentation. |
| `body-parser` | Parses form data submitted to the POST reset route. | Supports the sample HTML form with one focused dependency. |
| JSON | Stores the ticket and the structured Use Case 2 result. | Gives the workflows predictable input and output contracts. |
| Markdown | Stores reports, explanations, review findings, and presentation evidence. | Makes the results readable, versionable, and easy to submit. |
| GitHub and Git | Store and share the anonymized source, documentation, and generated evidence. | Provide version history and an accessible submission location. |
| PowerShell | Sets environment variables and runs the demonstration commands on Windows. | Matches the project environment and keeps credentials outside source files. |

The architecture has two boundaries. The **local boundary** reads files, controls the prompt inputs, validates the response schema, chooses the output path, and enforces the no-edit rule. The **AI boundary** receives selected text and returns suggestions. The model does not receive the whole workspace, does not receive the API key, and does not execute commands or modify files.

## 5. Use Case 1: Story to PR Readiness

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

In other words, Use Case 1 answers: **What needs to change, where would it change, and what should a developer check before implementation?**

### What the AI agent contributes

The agent is the local Python coordinator around the language model. It does not autonomously change the repository. Its contribution is to turn unstructured intake into a consistent review package: it identifies missing information, connects the ticket to specific files, proposes implementation steps and tests, and records risks for a human reviewer. The local program controls which ticket fields and repository files are sent, checks that the response has the required sections, and writes the report under the ticket ID. This creates traceability from the original request to the proposed work.

## 6. Use Case 2: Coding Task to Reviewed Proposal

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

In other words, Use Case 2 answers: **What might a safe implementation look like, what tests would support it, and what risks still require a developer's judgment?**

### What the AI coding assistant contributes

The coding assistant starts after the task has been framed for a backend developer. It receives the developer's comment, role, acceptance criteria, coding rules, and the same limited Express context. It then produces several forms of assistance in one response: a possible controller change, negative-path tests, test-boundary scaffolding, explanations to likely follow-up questions, a review of security and maintainability risks, and a behavior-preserving refactoring suggestion. The important result is not only the proposed validation; it is the review that explains what the proposal still does not solve, including token validation, password persistence, error handling, and executable tests.

The distinction between the two systems is therefore practical: the **AI agent organizes and assesses a product request**, while the **AI coding assistant explores an implementation for a defined developer task**. Both remain advisory, and neither replaces testing or human approval.

## 7. Tools and Responsibilities

The tools have distinct roles. VS Code and GitHub present and share the work; Python controls the workflows; OpenAI supplies live language-model analysis; and Node.js/Express provides the sample application that gives the analysis a realistic codebase.

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

## 8. Submission File Map

The files are grouped by their role in the evaluator's reading path. The names use `use-case-<number>-<purpose>.md` for use-case-specific material; shared project material keeps a short descriptive name.

| Reading purpose | File | Why it is included |
|---|---|---|
| Start here | [submission-overview.md](submission-overview.md) | Explains the project, use cases, tools, relationship, and evidence path. |
| Reproduce both workflows | [demo-runbook.md](demo-runbook.md) | Gives the shortest local and live execution instructions. |
| Understand Use Case 1 | [use-case-1-demo-script.md](use-case-1-demo-script.md) and [markdown_docs/ticket-6/report.md](../markdown_docs/ticket-6/report.md) | Shows the presentation sequence and the generated ticket report. |
| Understand Use Case 2 | [use-case-2-setup.md](use-case-2-setup.md), [use-case-2-demo-script.md](use-case-2-demo-script.md), and [markdown_docs/use-case-2/evidence.md](../markdown_docs/use-case-2/evidence.md) | Explains setup, presentation, and the generated coding-assistant evidence. |
| Inspect prompts and tools | [use-case-2-prompts.md](use-case-2-prompts.md), [prompt-pack.md](prompt-pack.md), and [tool-integration-evidence.md](tool-integration-evidence.md) | Shows the instructions, data boundary, API call, validation, and report-writing tools. |
| Evaluate quality and limits | [use-case-2-ai-review-report.md](use-case-2-ai-review-report.md), [use-case-2-reflection.md](use-case-2-reflection.md), [impact-narrative.md](impact-narrative.md), and [constraint-compliance.md](constraint-compliance.md) | Separates AI findings, human reflection, expected impact, and rule compliance. |

Generated reports and structured results are evidence outputs, not additional workflows. They should be read after the overview and the relevant use-case explanation.

## 9. Shared Repository Context

The AI tools use only these sandbox files:

- [myridius-auth-demo/server.js](../myridius-auth-demo/server.js): starts Express and registers `/auth` routes.
- [myridius-auth-demo/auth/routes.js](../myridius-auth-demo/auth/routes.js): maps GET and POST password-reset requests.
- [myridius-auth-demo/auth/authController.js](../myridius-auth-demo/auth/authController.js): displays the reset form and handles the submitted password.
- [myridius-auth-demo/views/resetPassword.html](../myridius-auth-demo/views/resetPassword.html): provides the reset form UI.

This context makes the model's recommendations repository-aware. It also limits the data sent to the provider.

## 10. End-to-End Flow

The shared flow is simple: a developer supplies a task, the local program supplies limited repository context, the model returns structured advice, and the learner reviews that advice before any implementation decision.

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

## 11. Commands for Demonstration

The demonstrations have three distinct execution requirements:

- **Offline evidence generation:** Python runs locally and writes Markdown/JSON files. No browser or internet connection is required.
- **Live AI evidence:** Python runs locally and makes an outbound HTTPS request. A valid `OPENAI_API_KEY` is required; no public web page is required.
- **Browser application demo:** Node.js runs the sample Express server at `http://localhost:3000`. Public deployment is optional and is outside this PoC's scope.

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

## 12. Safety and Human Oversight

The PoC follows these boundaries:

- Only sandbox or anonymized code is used.
- No customer data, production code, credentials, or secrets belong in the repository.
- API keys are environment variables and are excluded by [.gitignore](../.gitignore).
- The assistants generate recommendations and evidence only.
- They do not edit application files, auto-merge, auto-deploy, or approve changes.
- Learners review the generated code, tests, risks, and assumptions before implementation.

The complete constraint mapping is in [constraint-compliance.md](constraint-compliance.md).

## 13. Evaluation Evidence Map

The evidence is intentionally split across inputs, implementation, generated outputs, and reflection. This lets the evaluator distinguish what the local program did from what the model suggested and what still requires human approval.

| Expected capability | Demonstrated by |
|---|---|
| Tool use | Allowlisted repository reader, ticket reader, OpenAI API call, Markdown/JSON writers |
| Multi-step planning | Use Case 1 clarification, impact analysis, plan, testing, review, and handoff sections |
| Context management | Role prompts, `.agent.md`, `config.toml`, allowlisted repository context, and output contracts |
| Human-in-the-loop | Explicit approval gates in both use cases and no-edit behavior |
| AI-assisted review | Use Case 1 review findings and Use Case 2 severity-based review output |
| Test proposals | Test sections in both generated reports |
| Traceability | Ticket/task input linked to repository evidence and generated reports |

## 14. Presentation Order

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
