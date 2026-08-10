# Demo Runbook

## Goal
Demonstrate a story-to-PR readiness workflow for a sandbox authentication sample repository.

## Steps
1. Create or edit a ticket JSON file under the tickets folder.
2. Run the deterministic demo script:
   ```bash
   python agent-demo.py tickets/new-ticket.json
   ```
3. For real LLM analysis, set `OPENAI_API_KEY` in the terminal and run:
   ```bash
   python agent-demo.py --ai tickets/new-ticket.json
   ```
4. Review the generated reports in the markdown_docs folder.
5. Use the prompt pack and architecture diagram to explain the workflow to stakeholders.

## Expected Evidence
- Two sample tickets are processed end-to-end.
- Each report includes clarification, impacted files, implementation guidance, tests, review findings, and a PR handoff summary.
- The workflow preserves the approval gate before major changes are suggested.
- AI mode sends repository context and ticket details to the configured model but never writes application code or merges changes.
