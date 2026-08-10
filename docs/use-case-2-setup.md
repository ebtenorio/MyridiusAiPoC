# Use Case 2: Setup and Runbook

## Purpose

This PoC demonstrates a role-aware AI coding assistant for a backend developer working in the anonymized Express password-reset sample. It supports comment-driven generation, chat follow-up, scaffolding/test ideas, review, and behavior-preserving refactoring suggestions.

## Configuration

- Provider: OpenAI-compatible Chat Completions endpoint.
- Default model: `gpt-4o` from `config.toml`; override with `OPENAI_MODEL`.
- Endpoint: `OPENAI_BASE_URL` or `https://api.openai.com/v1`.
- Credential: `OPENAI_API_KEY` only in the local environment; never in a file or prompt.
- Context: four allowlisted sample files, with secret-like values redacted before an AI request.
- Output: `markdown_docs/use-case-2/evidence.md` and `result.json`.

## Run

Offline deterministic demonstration:

```bash
python coding-assistant-demo.py
```

Optional live model demonstration:

```bash
python coding-assistant-demo.py --ai
```

The live mode generates suggestions only. It does not edit files, run commands, merge code, or approve a change.

## Safety and Limitations

The sample has no real database, token service, authentication provider, or test runner. A developer must verify generated code against the real application contract, add integration coverage, inspect dependencies, and approve any change. The assistant must disclose assumptions, uncertainty, security findings, and test gaps.

## End-to-End Demonstration

1. Select `coding-task-1` in the demo script.
2. Load the role, repository rules, allowlisted context, and prompt templates in `docs/use-case-2-prompts.md`.
3. Generate code and tests from the developer comment.
4. Ask the chat follow-ups shown in the evidence report.
5. Review the security, error-handling, performance, maintainability, and test checklist.
6. Record the before/after proposal and require human approval before implementation.