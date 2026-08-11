# Demo Runbook

## Goal

This runbook is the short reproduction guide for both workflows in the submission. Use Case 1 turns a product ticket into a PR-readiness report. Use Case 2 then turns a focused backend task into a code, test, and review proposal. The [submission overview](submission-overview.md) explains the meaning of each result; this file focuses on running them.

## Steps
1. Create or edit a ticket JSON file under the tickets folder.
2. Run the deterministic demo script if you want to validate report generation without an API call:
   ```bash
   python agent-demo.py tickets/new-ticket.json
   ```
3. For real LLM analysis, set `OPENAI_API_KEY` in the terminal and run:
   ```bash
   python agent-demo.py --ai tickets/new-ticket.json
   ```
4. Review the generated reports in the markdown_docs folder.
5. Use the prompt pack and architecture diagram to explain the workflow to stakeholders.

For Use Case 2, run the offline coding assistant demo:

```bash
python coding-assistant-demo.py
```

Review the generated evidence in `markdown_docs/use-case-2/evidence.md`.

## Expected Evidence
- Use Case 1 produces a ticket report under `markdown_docs/<ticket-id>/report.md`.
- Use Case 2 produces `markdown_docs/use-case-2/evidence.md` and `result.json`.
- Each AI report includes clarification, impacted files, implementation guidance, tests, review findings, and a PR handoff summary.
- The workflow preserves the approval gate before major changes are suggested.
- AI mode sends repository context and ticket details to the configured model but never writes application code or merges changes.
