# AI Developer Assistant PoC: Submission Index

## Start Here

Read [submission-overview.md](submission-overview.md) first. It explains the project, the two use cases, the technology choices, the local-versus-AI architecture, and the evidence path.

The submission tells one story:

1. A product ticket is analyzed into a reviewable implementation plan.
2. A related backend task is explored through code proposals, tests, and AI review.
3. A learner reviews the evidence and decides whether any change should be implemented.

## Primary Evidence

| Order | Document | Purpose |
|---|---|---|
| 1 | [submission-overview.md](submission-overview.md) | Complete project explanation and evaluator guide. |
| 2 | [markdown_docs/ticket-6/report.md](../markdown_docs/ticket-6/report.md) | Generated Use Case 1 story-to-PR report. |
| 3 | [markdown_docs/use-case-2/evidence.md](../markdown_docs/use-case-2/evidence.md) | Generated Use Case 2 coding-assistant evidence. |
| 4 | [markdown_docs/use-case-2/result.json](../markdown_docs/use-case-2/result.json) | Structured result and AI provenance for Use Case 2. |

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
