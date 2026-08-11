# AI Developer Assistant PoC: Submission Index

## Start Here

Read [submission-overview.md](submission-overview.md) first. It explains the project, the two use cases, the technology choices, the local-versus-AI architecture, and the evidence path.

For the short text that accompanies an upload, use [submission-description.md](submission-description.md). It defines the abbreviation Proof of Concept, explains both use cases and tools, and makes clear that attachments are primary while videos and GitHub are optional backups.

The submission tells one story:

1. A product ticket is analyzed into a reviewable implementation plan.
2. A related backend task is explored through code proposals, tests, and AI review.
3. A learner reviews the evidence and decides whether any change should be implemented.

## Use Cases in Detail

### Use Case 1: AI Agent for Story-to-PR Readiness

The starting point is a product-facing ticket: replace the password-reset success message with a confirmation page. The local `agent-demo.py` program reads the ticket ID, title, story, and acceptance criteria, then adds context from four allowlisted Express files. In live mode, the OpenAI model analyzes that combined context and returns structured JSON. The local program validates the required fields and writes a report under the ticket ID.

The result is not an automatic code change. It is a review package containing assumptions, likely impacted files, an implementation plan, test cases, review findings, and a PR handoff summary. This use case demonstrates how an AI agent can make an incomplete request more actionable while preserving traceability and a human approval step.

### Use Case 2: AI Coding Assistant for a Backend Task

The starting point is a developer comment: validate the submitted password before reset without exposing credentials. The `coding-assistant-demo.py` program supplies the model with a backend-developer role, acceptance criteria, repository rules, and the same allowlisted Express context. The response is requested in several forms: proposed code, negative-path tests, test scaffolding, follow-up explanations, review findings, refactoring guidance, and prompt-iteration evidence.

The result is recorded as both readable Markdown and structured JSON. The assistant proposes a small validation change but also identifies what the sample does not prove, including reset-token validation, secure password persistence, error handling, and executable tests. This use case demonstrates coding assistance as an advisory review conversation rather than one-shot code generation.

The use cases complement one another: Use Case 1 organizes the product request, while Use Case 2 explores a specific implementation task. Both workflows are local-first, use the model only in live mode, and stop before editing, merging, deploying, or approving code.

## Technologies Used

| Technology | Role in the submission |
|---|---|
| Python 3 | Runs both local orchestrators, reads controlled inputs, validates model responses, and writes evidence. |
| OpenAI-compatible API | Supplies live language-model analysis when `--ai` and `OPENAI_API_KEY` are provided. |
| Node.js and Express | Runs the anonymized password-reset application used as repository context. |
| JavaScript | Implements the sample server, routes, and authentication controller. |
| `body-parser` | Parses the HTML form body sent to the sample POST route. |
| JSON | Stores the ticket input and structured Use Case 2 output. |
| Markdown | Stores human-readable reports, prompts, reviews, and reflection. |
| PowerShell | Runs the demonstrations and keeps the API key in the environment. |
| GitHub and Git | Version and share the anonymized project and its evidence. |

The local scripts control file access, prompt boundaries, schema validation, output paths, and the no-edit policy. The AI service generates analysis from the selected text. The sample Express application is only a target codebase for the demonstrations; it is not presented as production authentication.

## Primary Evidence

| Order | Document | Purpose |
|---|---|---|
| 1 | [submission-overview.md](submission-overview.md) | Complete project explanation and evaluator guide. |
| 2 | [submission-description.md](submission-description.md) | Plain-language upload description with optional video and repository links. |
| 3 | [markdown_docs/ticket-6/report.md](../markdown_docs/ticket-6/report.md) | Generated Use Case 1 story-to-PR report. |
| 4 | [markdown_docs/use-case-2/evidence.md](../markdown_docs/use-case-2/evidence.md) | Generated Use Case 2 coding-assistant evidence. |
| 5 | [markdown_docs/use-case-2/result.json](../markdown_docs/use-case-2/result.json) | Structured result and AI provenance for Use Case 2. |

## Reproduction Guides

- [demo-runbook.md](demo-runbook.md): shortest run instructions for both workflows.
- [use-case-1-demo-script.md](use-case-1-demo-script.md): presenter script for the ticket-to-PR workflow.
- [use-case-2-setup.md](use-case-2-setup.md): configuration and setup for the coding assistant.
- [use-case-2-demo-script.md](use-case-2-demo-script.md): presenter script for the coding-assistant workflow.

## Technical and Quality Evidence

- [architecture-diagram.md](architecture-diagram.md): system flow and data boundaries.
- [tool-integration-evidence.md](tool-integration-evidence.md): implemented readers, API integration, validation, and report writer.
- [prompt-pack.md](prompt-pack.md): Use Case 1 system prompt, task prompt, and output contract.
- [use-case-2-prompts.md](use-case-2-prompts.md): role-aware coding prompts and safety rules.
- [use-case-2-sample-code-evidence.md](use-case-2-sample-code-evidence.md): before/after proposal and test ideas.
- [use-case-2-ai-review-report.md](use-case-2-ai-review-report.md): severity-based review findings and remediations.

## Reflection and Compliance

- [impact-narrative.md](impact-narrative.md): expected benefits, limitations, and measurement plan.
- [use-case-2-reflection.md](use-case-2-reflection.md): what helped, what remained uncertain, and next improvements.
- [constraint-compliance.md](constraint-compliance.md): submission rules, safety boundaries, and learner checklist.
- [ai-review-output.md](ai-review-output.md): review of the confirmation-page proposal.

## File Naming Convention

- `submission-overview.md` and `README.md` are navigation documents.
- `use-case-1-*` and `use-case-2-*` are use-case-specific guides or evidence.
- Descriptive shared names such as `architecture-diagram.md`, `tool-integration-evidence.md`, and `impact-narrative.md` identify cross-cutting project evidence.
- Generated runtime outputs remain under `markdown_docs/` so they are visibly separate from explanatory source documents.

The documents use Markdown for readability and version control. They can be converted to Word for submission without changing the recommended reading order.

## Complete Document Register

| Category | Filename | Descriptive title and purpose |
|---|---|---|
| Navigation | `README.md` | Submission index and reading order. |
| Navigation | `submission-overview.md` | Full project overview, architecture, use cases, tools, and evaluation map. |
| Submission description | `submission-description.md` | Plain-language text for the upload description and optional access links. |
| Reproduction | `demo-runbook.md` | Short run instructions for both workflows. |
| Reproduction | `use-case-1-demo-script.md` | Presenter script for the AI agent workflow. |
| Reproduction | `use-case-2-setup.md` | Configuration and setup for the AI coding assistant. |
| Reproduction | `use-case-2-demo-script.md` | Presenter script for the AI coding assistant workflow. |
| Deliverables | `use-case-2-deliverables.md` | Maps the Use Case 2 setup, prompts, evidence, review, and reflection files. |
| Architecture | `architecture-diagram.md` | Workflow diagram, components, and data boundaries. |
| Tool evidence | `tool-integration-evidence.md` | Repository reader, ticket reader, API call, validator, and report writer. |
| Prompt evidence | `prompt-pack.md` | Use Case 1 prompts and structured output contract. |
| Prompt evidence | `use-case-2-prompts.md` | Use Case 2 role, coding, testing, review, and refactoring prompts. |
| Code evidence | `use-case-2-sample-code-evidence.md` | Before/after proposal, diff, and generated test ideas. |
| Review evidence | `use-case-2-ai-review-report.md` | Severity-based findings, remediation, and human decisions. |
| Review evidence | `ai-review-output.md` | Review of the confirmation-page ticket proposal. |
| Reflection | `use-case-2-reflection.md` | Benefits, limitations, and next improvements for Use Case 2. |
| Impact | `impact-narrative.md` | Expected productivity impact and measurement plan. |
| Compliance | `constraint-compliance.md` | Safety, submission constraints, and learner checklist. |

This register uses stable, descriptive categories while retaining the repository's existing filenames so that links, video instructions, and generated evidence remain valid.
