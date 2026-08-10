# Constraint Compliance

## Status

| Constraint | Status | Evidence and action |
|---|---|---|
| Individual or team of up to 3 learners | Compliant by project governance | This is a participation rule rather than an application behavior. Record the learner names and confirm the team has no more than three people before submission. |
| Sandbox, sample, or anonymized repositories only | Compliant | The analyzed repository is the sandbox `myridius-auth-demo` authentication sample. The agent reads only explicitly listed sample files. |
| No secrets, credentials, production code, or customer data | Compliant with operational responsibility | `OPENAI_API_KEY` is read from the environment and is not included in prompts or reports. The repository uses sample code. The `.gitignore` excludes common environment and key files. Never place real secrets in ticket JSON or the repository. |
| No auto-merge, auto-deploy, or bypassed approval | Compliant | [agent-demo.py](../agent-demo.py) only reads context, calls the model, validates JSON, and writes Markdown. The prompt and documentation prohibit editing, merging, deploying, and self-approval. |
| Generated code and recommendations reviewed by learners | Compliant by workflow | Reports are recommendations only. A learner must inspect impacted files, proposed tests, security findings, and the final diff before implementation or merge. This is documented in [docs/architecture-diagram.md](architecture-diagram.md) and [docs/ai-review-output.md](ai-review-output.md). |
| Any approved LLM, Copilot workflow, framework, CLI, or web app | Compliant | This PoC uses the OpenAI API through a local Python CLI. The model is selected with `OPENAI_MODEL`. |

## Submission evidence

- Live AI report: [markdown_docs/ticket-6/report.md](../markdown_docs/ticket-6/report.md)
- Agent implementation: [agent-demo.py](../agent-demo.py)
- Agent rules: [.agent.md](../.agent.md)
- Architecture: [architecture-diagram.md](architecture-diagram.md)
- Tool evidence: [tool-integration-evidence.md](tool-integration-evidence.md)
- AI review: [ai-review-output.md](ai-review-output.md)
- Impact narrative: [impact-narrative.md](impact-narrative.md)

## Learner checklist

- [ ] Confirm one learner or no more than three learners.
- [ ] Confirm all repository files and tickets are sandbox or anonymized.
- [ ] Search the repository and generated artifacts for secrets before sharing.
- [ ] Keep the OpenAI key in an environment variable only.
- [ ] Review every AI recommendation before implementing it.
- [ ] Do not auto-merge, auto-deploy, or represent recommendations as completed code changes.