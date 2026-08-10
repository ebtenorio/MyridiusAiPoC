from pathlib import Path
import json
import sys
import os
import urllib.error
import urllib.request

repo_root = Path(__file__).resolve().parent
output_root = repo_root / 'markdown_docs'
output_root.mkdir(exist_ok=True)

sample_tickets = [
    {
        'id': 'ticket-1',
        'title': 'Add client-side validation to the password reset form',
        'story': 'As a user, I want clear feedback when I submit an invalid password reset so I can recover my account without confusion.',
        'acceptance_criteria': [
            'The form shows inline validation for short or missing passwords.',
            'The submit flow stops before the reset request is sent when validation fails.',
            'The experience remains usable on mobile and desktop.'
        ],
        'impacted_files': [
            'myridius-auth-demo/views/resetPassword.html',
            'myridius-auth-demo/auth/authController.js',
            'myridius-auth-demo/auth/routes.js'
        ],
        'implementation_plan': [
            'Add a minimal validation rule in the reset form before the request is posted.',
            'Surface server-side feedback in the controller so the UI can show a helpful error message.',
            'Keep the change localized to the password reset flow to avoid broad regressions.'
        ],
        'test_cases': [
            'Unit: validates a password shorter than 8 characters.',
            'Unit: accepts a password meeting the minimum strength requirement.',
            'Integration: prevents submission when validation fails and preserves the existing form state.'
        ],
        'review_findings': [
            'Readable and localized change with low complexity.',
            'Security risk remains low because the validation is client-side and should be mirrored server-side.',
            'Consider adding a stronger password policy once the product requirements are finalized.'
        ]
    },
    {
        'id': 'ticket-2',
        'title': 'Add audit logging for failed password reset attempts',
        'story': 'As an operator, I want failed password reset attempts logged so I can investigate suspicious account activity.',
        'acceptance_criteria': [
            'Every failed reset attempt produces a structured log entry.',
            'The log captures the request context and a failure reason.',
            'The change does not block the existing reset flow.'
        ],
        'impacted_files': [
            'myridius-auth-demo/auth/authController.js',
            'myridius-auth-demo/server.js',
            'myridius-auth-demo/auth/routes.js'
        ],
        'implementation_plan': [
            'Wrap the reset handler with a small logging helper that records failures.',
            'Emit a structured log entry for invalid tokens and missing passwords.',
            'Leave the primary UX intact and require human approval before shipping the logging policy.'
        ],
        'test_cases': [
            'Unit: records a failure when the reset token is invalid.',
            'Unit: records a failure when a password is missing from the request body.',
            'Integration: confirms the reset flow still returns a safe response after logging.'
        ],
        'review_findings': [
            'Improves supportability and security observability.',
            'Ensure logs avoid leaking secrets or personally identifiable information.',
            'Consider a dedicated logger abstraction before expanding to more features.'
        ]
    }
]


def load_tickets() -> list[dict]:
    ticket_arguments = [argument for argument in sys.argv[1:] if argument != '--ai']
    if not ticket_arguments:
        return sample_tickets

    ticket_path = Path(ticket_arguments[0])
    if not ticket_path.is_absolute():
        ticket_path = repo_root / ticket_path
    ticket_data = json.loads(ticket_path.read_text(encoding='utf-8'))
    return ticket_data if isinstance(ticket_data, list) else [ticket_data]


def repository_context() -> str:
    context_files = [
        'myridius-auth-demo/server.js',
        'myridius-auth-demo/auth/routes.js',
        'myridius-auth-demo/auth/authController.js',
        'myridius-auth-demo/views/resetPassword.html'
    ]
    return '\n\n'.join(
        f"FILE: {relative_path}\n{read_text(relative_path)}"
        for relative_path in context_files
    )


def load_model() -> str:
    configured_model = os.environ.get('OPENAI_MODEL')
    if configured_model:
        return configured_model
    config_path = repo_root / 'config.toml'
    if config_path.exists():
        for line in config_path.read_text(encoding='utf-8').splitlines():
            if line.strip().startswith('model') and '=' in line:
                return line.split('=', 1)[1].strip().strip('"')
    return 'gpt-4o-mini'


def process_with_ai(ticket: dict) -> dict:
    api_key = os.environ.get('OPENAI_API_KEY')
    if not api_key:
        raise RuntimeError('AI mode requires the OPENAI_API_KEY environment variable.')

    system_prompt = '''You are a senior software engineer helping with a sandbox repository.
Analyze the ticket and repository context, then return ONLY valid JSON with these keys:
title, story, acceptance_criteria, clarification, impacted_files, implementation_plan,
test_cases, review_findings, pr_summary. Each list value must be an array of concise
strings. Do not modify files, execute commands, expose secrets, or approve a change.
Include a human approval step in the implementation plan for any major change.'''
    user_prompt = json.dumps({
        'ticket': {
            'id': ticket.get('id'),
            'title': ticket.get('title'),
            'story': ticket.get('story'),
            'acceptance_criteria': ticket.get('acceptance_criteria', [])
        },
        'repository_context': repository_context()
    }, indent=2)
    payload = json.dumps({
        'model': load_model(),
        'temperature': 0.2,
        'response_format': {'type': 'json_object'},
        'messages': [
            {'role': 'system', 'content': system_prompt},
            {'role': 'user', 'content': user_prompt}
        ]
    }).encode('utf-8')
    request = urllib.request.Request(
        os.environ.get('OPENAI_BASE_URL', 'https://api.openai.com/v1') + '/chat/completions',
        data=payload,
        headers={
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        },
        method='POST'
    )
    try:
        with urllib.request.urlopen(request, timeout=90) as response:
            response_data = json.loads(response.read().decode('utf-8'))
    except urllib.error.HTTPError as error:
        details = error.read().decode('utf-8', errors='replace')
        raise RuntimeError(f'AI request failed with HTTP {error.code}: {details}') from error
    except urllib.error.URLError as error:
        raise RuntimeError(f'AI request could not reach the configured endpoint: {error.reason}') from error

    content = response_data['choices'][0]['message']['content']
    result = json.loads(content)
    required_fields = {
        'title', 'story', 'acceptance_criteria', 'clarification', 'impacted_files',
        'implementation_plan', 'test_cases', 'review_findings', 'pr_summary'
    }
    missing_fields = required_fields - result.keys()
    if missing_fields:
        raise RuntimeError(f'AI response is missing fields: {sorted(missing_fields)}')
    result['analysis_mode'] = 'AI-generated'
    return result


def read_text(relative_path: str) -> str:
    return (repo_root / relative_path).read_text(encoding='utf-8')


def write_markdown(relative_path: str, content: str) -> None:
    destination = output_root / relative_path
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(content, encoding='utf-8')


def build_report(ticket: dict) -> str:
    repo_context = [
        f"- Sample app entry point: {read_text('myridius-auth-demo/server.js').splitlines()[0]}",
        f"- Auth routes: {read_text('myridius-auth-demo/auth/routes.js').splitlines()[0]}",
        f"- Current reset handler: {read_text('myridius-auth-demo/auth/authController.js').splitlines()[0]}"
    ]
    clarification = ticket.get('clarification') or [
        'No additional clarification was provided.'
    ]
    review_findings = ticket.get('review_findings') or [
        'No review findings were returned by the analysis.'
    ]
    pr_summary = ticket.get('pr_summary') or [
        'No PR summary was returned by the analysis.'
    ]
    lines = [
        f"# {ticket['title']}",
        '',
        f"**Analysis mode:** {ticket.get('analysis_mode', 'Deterministic demo output')}",
        '',
        '## Story',
        ticket['story'],
        '',
        '## Acceptance Criteria',
        *[f"- {item}" for item in ticket['acceptance_criteria']],
        '',
        '## Clarification',
        *[f"- {item}" for item in clarification],
        '',
        '## Impacted Files',
        *[f"- {file_path}" for file_path in ticket['impacted_files']],
        '',
        '## Implementation Plan',
        *[f"- {step}" for step in ticket['implementation_plan']],
        '',
        '## Test Cases',
        *[f"- {test_case}" for test_case in ticket['test_cases']],
        '',
        '## Review Findings',
        *[f"- {finding}" for finding in review_findings],
        '',
        '## PR Summary',
        *[f"- {item}" for item in pr_summary],
        '',
        '## Repository Evidence',
        *repo_context,
        ''
    ]
    return '\n'.join(lines)

use_ai = '--ai' in sys.argv
tickets = load_tickets()
if use_ai:
    analyzed_tickets = []
    for ticket in tickets:
        analyzed_ticket = process_with_ai(ticket)
        analyzed_ticket['id'] = ticket['id']
        analyzed_tickets.append(analyzed_ticket)
    tickets = analyzed_tickets
for ticket in tickets:
    write_markdown(f"{ticket['id']}/report.md", build_report(ticket))

report_links = '\n'.join(
    f"- [{ticket['id']}/report.md]({ticket['id']}/report.md)"
    for ticket in tickets
)
index_content = f"""# Agent Demo Outputs

The following tickets were processed:

{report_links}

Deterministic mode:

```bash
python agent-demo.py tickets/new-ticket.json
```

AI mode:

```bash
python agent-demo.py --ai tickets/new-ticket.json
```
"""
write_markdown('README.md', index_content)
print(f"Generated {len(tickets)} demo reports in {output_root}")
