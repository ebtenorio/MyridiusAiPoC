# Tool Integration Evidence

This document maps the PoC requirements to the tools that are actually implemented.

## 1. Repository reader

Implemented in `repository_context()` in [agent-demo.py](../agent-demo.py).

The reader loads these sandbox files and includes their contents in the AI request:

- [myridius-auth-demo/server.js](../myridius-auth-demo/server.js)
- [myridius-auth-demo/auth/routes.js](../myridius-auth-demo/auth/routes.js)
- [myridius-auth-demo/auth/authController.js](../myridius-auth-demo/auth/authController.js)
- [myridius-auth-demo/views/resetPassword.html](../myridius-auth-demo/views/resetPassword.html)

This provides repository-aware analysis instead of asking the model to reason from the ticket alone.

## 2. Ticket file reader

Implemented in `load_tickets()` in [agent-demo.py](../agent-demo.py).

It supports:

- One ticket JSON object
- A JSON array of tickets
- Relative or absolute ticket paths

Example:

```powershell
python agent-demo.py --ai tickets/new-ticket.json
```

## 3. OpenAI API integration

Implemented in `process_with_ai()` in [agent-demo.py](../agent-demo.py).

The tool sends an HTTP POST request to the OpenAI-compatible chat completions endpoint with:

- `OPENAI_API_KEY` authentication
- `OPENAI_MODEL` model selection
- A system prompt
- Ticket intake data
- Repository context
- JSON response mode

The API key is read from the environment and is not written to reports.

## 4. Response validator

The local agent checks that the model response includes `clarification`, `impacted_files`, `implementation_plan`, `test_cases`, `review_findings`, and `pr_summary`, in addition to the ticket summary fields. Incomplete responses fail before report generation.

## 5. Markdown report writer

Implemented in `write_markdown()` and `build_report()` in [agent-demo.py](../agent-demo.py).

Reports are stored by the locally controlled ticket ID:

- [markdown_docs/ticket-6/report.md](../markdown_docs/ticket-6/report.md)
- [markdown_docs/README.md](../markdown_docs/README.md)

## 6. Test runner and mock API status

The current PoC does not yet implement a repository test runner or mock API. The equivalent evidence is the live OpenAI integration, repository reader, file reader, schema validation, and report writer. A production extension should add an allowlisted local test command and capture its stdout, stderr, exit code, and timestamp in the report.

## Evidence boundary

The model is not allowed to edit files, execute commands, merge, deploy, or approve changes. The local process only writes Markdown reports, and the developer decides whether any recommendation should be implemented.