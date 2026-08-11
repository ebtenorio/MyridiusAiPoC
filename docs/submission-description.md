# Submission Upload Note

## Overview

This submission presents a Proof of Concept (PoC), meaning a small working demonstration, showing how artificial intelligence can support software development in two connected use cases. Both use cases use the same anonymized Express password-reset application as a safe sample repository.

The attached documents, source files, and Use Case 1 video are the primary submission evidence. The YouTube links and GitHub repository are optional backup access points in case a reviewer has difficulty opening an attachment. The written submission is intended to be understandable without opening an external link.

## Use Case 1: AI Agent for Story-to-PR Readiness

Use Case 1 begins with a product ticket requesting a clearer confirmation page after a successful password reset. The local Python program `agent-demo.py` reads the ticket, adds context from selected sample repository files, and sends that controlled context to an OpenAI-compatible language-model endpoint when live mode is enabled.

The program validates the structured response and writes a Markdown report. The report contains clarification questions, assumptions, impacted files, an implementation plan, test cases, review findings, and a pull-request handoff summary. The agent does not edit application files, merge code, deploy software, or approve its own recommendation.

This use case demonstrates how a product-level request can become a traceable, reviewable plan for a developer.

## Use Case 2: AI Coding Assistant

Use Case 2 begins with a backend developer task: validate the submitted password before reset without exposing credentials. The local Python program `coding-assistant-demo.py` supplies the language model with the developer role, task, acceptance criteria, safety rules, and the same limited Express repository context.

The generated evidence includes a proposed controller change, valid and invalid test ideas, project scaffolding, follow-up explanations, security and maintainability findings, refactoring guidance, and a comparison between a basic prompt and a more specific prompt. The assistant also identifies limitations that still require human judgment, including reset-token validation, secure password persistence, error handling, and an executable test suite.

This use case demonstrates coding assistance as a reviewable proposal rather than automatic code generation.

## Tools and Technologies

- **Python 3:** runs the two local orchestration programs and writes the evidence.
- **OpenAI-compatible API:** provides live language-model analysis when the live demonstration is run.
- **Node.js and Express:** run the anonymized password-reset sample application.
- **JavaScript:** implements the sample server, routes, and controller.
- **JSON:** stores ticket input and structured assistant output.
- **Markdown:** stores human-readable reports, prompts, reviews, and reflection.
- **PowerShell:** runs commands and keeps the API key in an environment variable.
- **Git and GitHub:** version and share the anonymized project.

The demonstrations can also run in deterministic offline mode. Live mode requires network access to the configured API endpoint; the sample application can run locally at `http://localhost:3000` and does not require public hosting.

## Submission Files and Access

- The Use Case 1 video is included with the submission as an archive. The archive was prepared for the upload system; if the uploaded extension cannot be opened, use the correctly identified RAR version or the optional YouTube backup.
- The Use Case 2 video is available on YouTube because the video exceeds the submission upload limit.
- The required written documents and generated evidence are included with the submission.
- The complete anonymized source repository is available on GitHub for optional inspection.
- An archive of the full repository is also included for offline reference.

The archive and links provide alternative ways to access the same demonstration. They are not separate use cases and do not replace the written evidence.

### Optional video links

- Use Case 1: https://www.youtube.com/watch?v=ic6pXUANFSM
- Use Case 2: https://www.youtube.com/watch?v=lrUSriu9urk

### Optional repository links

- Documentation: https://github.com/ebtenorio/MyridiusAiPoC/tree/main/docs
- Complete repository: https://github.com/ebtenorio/MyridiusAiPoC

## Recommended Reading Order

1. `submission-overview.md` for the complete explanation.
2. `README.md` for the document index and file descriptions.
3. The generated Use Case 1 and Use Case 2 evidence reports.
4. The reproduction guides, architecture, tool evidence, review, reflection, and compliance documents.

All recommendations remain subject to human review. The PoC uses anonymized sample code and does not claim to be production-ready authentication software.
