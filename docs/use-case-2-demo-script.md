# Use Case 2 Demo Script: AI Coding Assistant

## Demo Goal

Demonstrate an OpenAI-powered coding assistant that uses a developer role, repository context, coding rules, and a task prompt to generate code, tests, scaffolding, chat answers, review findings, and refactoring guidance.

The assistant produces suggestions and evidence only. It does not modify application files or approve changes.

## Tools Used

- **Python 3:** runs the local orchestration script.
- **OpenAI API:** generates the coding-assistant response.
- **`coding-assistant-demo.py`:** builds the request, sends repository context to OpenAI, validates the response, and writes evidence.
- **Sample Express repository:** provides anonymized backend code for context.
- **PowerShell:** sets the API key and runs the demonstration.
- **Markdown and JSON outputs:** provide human-readable and structured evidence.

## Files Used

The assistant sends only these allowlisted sample files as repository context:

- `myridius-auth-demo/auth/authController.js`
- `myridius-auth-demo/auth/routes.js`
- `myridius-auth-demo/server.js`
- `myridius-auth-demo/views/resetPassword.html`

The task and role are defined in the `TASK` dictionary in `coding-assistant-demo.py`. Prompt templates and safety rules are documented in [use-case-2-prompts.md](use-case-2-prompts.md).

## Before the Demo

Open PowerShell in the repository root:

```powershell
cd C:\MyridiusAiPoC\MyridiusAiPoC
.venv\Scripts\Activate.ps1
```

Set the API key in the current terminal session. Do not place the key in a source file or show it during the presentation:

```powershell
$env:OPENAI_API_KEY = "YOUR_OPENAI_API_KEY"
```

Optional model selection:

```powershell
$env:OPENAI_MODEL = "gpt-4o"
```

The default model is read from `config.toml` unless `OPENAI_MODEL` is set.

## Presenter Script

### 1. Introduce the Problem

Say:

> Developers often receive generic AI suggestions that do not understand their role, repository structure, security expectations, or test needs. This PoC demonstrates a backend-focused coding assistant that receives those constraints before generating a response.

### 2. Show the Developer Task

Open `coding-assistant-demo.py` and show the `TASK` dictionary:

```python
TASK = {
    'id': 'coding-task-1',
    'title': 'Add server-side password reset validation',
    'comment': 'Validate the submitted password before reset and return a safe error without leaking credentials.',
    'role': 'Backend developer maintaining a small Express authentication demo.'
}
```

Say:

> The developer provides a clear comment, role context, and acceptance criteria. The task is to reject missing or short passwords, avoid exposing sensitive values, and preserve the existing successful response.

### 3. Explain What the Assistant Sends

Show `ai_result()` in `coding-assistant-demo.py`.

Say:

> The local script sends OpenAI a system instruction and a JSON user prompt. The JSON includes the task, the allowlisted repository context, the required response fields, and safety rules. The API key is sent only in the HTTP Authorization header and is never included in the prompt.

The request uses:

```text
Provider: https://api.openai.com/v1
Endpoint: /chat/completions
Response format: JSON object
Temperature: 0.2
```

### 4. Run the Live OpenAI Demo

Run:

```powershell
python coding-assistant-demo.py --ai
```

Expected output:

```text
Generated Use Case 2 evidence in ...\markdown_docs\use-case-2
```

Say:

> The `--ai` flag selects the OpenAI path. The script validates the returned JSON, records the provider and model, and writes the response as evidence. It does not write a patch into the sample application.

### 5. Open the Evidence

Open:

```powershell
code markdown_docs/use-case-2/evidence.md
```

Point out these lines near the top:

```text
Analysis mode: AI-generated (...)
Result source: OpenAI-compatible API response
Model: ...
Provider endpoint: https://api.openai.com/v1
```

Say:

> These fields confirm that this report came from the OpenAI API path rather than the local deterministic fallback.

### 6. Demonstrate Generated Code

Show **Generated Code** in `evidence.md`.

Say:

> The assistant generated server-side validation for missing and short passwords while preserving the successful response. This is a proposal. A developer must inspect it before acceptance because the sample has no real database or token service.

### 7. Demonstrate Tests

Show **Generated Tests**.

Say:

> The assistant generated test ideas for valid, missing, and short passwords. These are meaningful test cases, but they have not been executed because the sample does not contain a test runner.

### 8. Demonstrate Project Scaffolding

Show **Project Scaffolding**.

Say:

> The assistant also produced consistent boilerplate and a project structure based on the existing Express application rather than inventing an unrelated architecture.

### 9. Demonstrate Chat Workflow

Show **Chat Follow-up**.

Say:

> The chat workflow addresses implementation questions, safe error responses, and reset-token validation. This demonstrates that the assistant can explain and improve a proposed change, not only generate code once.

### 10. Demonstrate AI Review

Show **AI Review Checklist**.

Say:

> The review identifies at least three issues across input validation, error handling, and sensitive logging. Each issue is a reason for human review before implementation.

### 11. Demonstrate Refactoring

Show **Refactoring Recommendation**.

Say:

> The assistant recommends adding validation while preserving the existing valid-input behavior. The approval gate remains with the developer, who must confirm the real password policy and testing conventions.

### 12. Demonstrate Prompt Iteration

Show **Prompt Iteration**.

Say:

> The baseline prompt is brief. The revised prompt adds explicit security and validation requirements. This makes the expected output more precise and demonstrates prompt iteration as a quality improvement technique.

### 13. Close with Safety and Limitations

Say:

> This is an anonymized sandbox. No production data, credentials, internal endpoints, or secrets are used. The assistant does not edit files, execute commands, merge code, or approve changes. Human review is required because the generated output is advisory and the sample lacks a real token service, database, and test runner.

## Success Criteria Checklist

Use this checklist while presenting:

- [x] Relevant code generated from a clear developer comment.
- [x] Useful developer chat answers generated.
- [x] Consistent project scaffolding generated.
- [x] Meaningful test cases generated.
- [x] At least three AI review issues identified.
- [x] Refactoring behavior and approval trade-offs explained.
- [x] Baseline and revised prompts shown.
- [x] Revised prompt improvement explained.
- [x] OpenAI provider, model, and analysis mode recorded.
- [x] Assumptions, limitations, and human approval gate documented.

## Output Files

After the live run, open:

```text
markdown_docs/use-case-2/evidence.md
markdown_docs/use-case-2/result.json
```

- `evidence.md` is the presentation report.
- `result.json` is the structured API response and provenance record.

## Offline Fallback

If an API key is unavailable, run:

```powershell
python coding-assistant-demo.py
```

This validates the local workflow but is not evidence of live OpenAI generation. For the final PoC demonstration, use:

```powershell
python coding-assistant-demo.py --ai
```
