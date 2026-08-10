# Use Case 2 Deliverables

Use Case 2 is the OpenAI-powered AI Coding Assistant PoC. Deliverable 1 is excluded because the live CLI demo was recorded separately.

## Deliverable 2: Setup and Configuration Guide

- [Setup and runbook](use-case-2-setup.md)
- [Presenter demo script](use-case-2-demo-script.md)

Tools, model settings, workspace rules, API configuration, safety controls, limitations, and the live command are documented there.

Live command:

```powershell
.venv\Scripts\Activate.ps1
$env:OPENAI_API_KEY = "YOUR_OPENAI_API_KEY"
python coding-assistant-demo.py --ai
```

## Deliverable 3: Prompt Library

- [Prompt library](use-case-2-prompts.md)

It contains workspace rules and prompts for inline generation, chat/debugging, tests, scaffolding, review, and refactoring.

## Deliverable 4: Sample Code Evidence

- [Sample code evidence](use-case-2-sample-code-evidence.md)
- [Generated evidence report](../markdown_docs/use-case-2/evidence.md)
- [Structured result](../markdown_docs/use-case-2/result.json)

The evidence includes before/after code, a diff, generated tests, boilerplate, assumptions, and human verification requirements.

## Deliverable 5: AI Review Report

- [AI review report](use-case-2-ai-review-report.md)

The report identifies security, error handling, testing, and maintainability issues with severity, evidence, rationale, remediation, and human decisions.

## Deliverable 6: Reflection Note

- [Reflection note](use-case-2-reflection.md)

It records where the assistant helped, where human judgment was required, and how the workflow can be improved.

## Evidence Provenance

For live OpenAI output, `evidence.md` and `result.json` must show:

```text
Analysis mode: AI-generated (...)
Result source: OpenAI-compatible API response
Provider endpoint: https://api.openai.com/v1
```

If the files show `Deterministic sandbox output`, rerun the live command with `OPENAI_API_KEY` set. The deterministic run validates the local workflow but is not evidence of a live OpenAI response.
