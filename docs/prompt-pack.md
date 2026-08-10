# Prompt Pack

## System Prompt
The implemented system prompt in [agent-demo.py](../agent-demo.py) is:

> You are a senior software engineer helping with a sandbox repository. Analyze the ticket and repository context, then return ONLY valid JSON with these keys: `title`, `story`, `acceptance_criteria`, `clarification`, `impacted_files`, `implementation_plan`, `test_cases`, `review_findings`, `pr_summary`. Each list value must be an array of concise strings. Do not modify files, execute commands, expose secrets, or approve a change. Include a human approval step in the implementation plan for any major change.

## Task Prompt
Given the following ticket and repository context, produce:
1. A clarification section with assumptions and missing information.
2. A list of likely impacted files.
3. An implementation plan with starter code ideas.
4. Unit and integration test cases.
5. Review findings covering readability, maintainability, security, and performance.
6. A PR summary with risks and next steps.

Only send the ticket ID, title, story, acceptance criteria, and approved repository context. Do not send prefilled analysis fields from the ticket because the model must independently produce the plan and review.

## Review Checklist
- Is the plan aligned with the user story and acceptance criteria?
- Are impacted files clearly identified and justified?
- Are tests and edge cases covered?
- Are security and maintainability risks called out?
- Is there a clear approval step before implementation?
- Does the output distinguish AI analysis from repository evidence?
- Are empty findings explicitly reported instead of being silently invented?

## Clarification Prompts
- What stack or coding standards should I follow?
- Is the goal implementation guidance, a code patch, or both?
- Should I prioritize a fast prototype or a production-ready design?
- What level of approval is required before changes are made?

## Output Contract

The response must be valid JSON and include all required fields. The local agent rejects incomplete responses before writing the report. The ticket ID remains controlled by the local application so the model cannot select an unexpected output path.
