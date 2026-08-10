from pathlib import Path
import os

repo_root = Path(__file__).resolve().parent
output_root = repo_root / 'markdown_docs'
output_root.mkdir(exist_ok=True)

tickets = [
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
    lines = [
        f"# {ticket['title']}",
        '',
        '## Story',
        ticket['story'],
        '',
        '## Acceptance Criteria',
        *[f"- {item}" for item in ticket['acceptance_criteria']],
        '',
        '## Clarification',
        '- The repository is a sandbox password reset demo with a simple Express server.',
        '- Assumption: the request is for implementation guidance rather than changing production code directly.',
        '- Approval gate: a human reviewer should approve any code change before it is merged.',
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
        *[f"- {finding}" for finding in ticket['review_findings']],
        '',
        '## PR Summary',
        '- This PoC demonstrates a story-to-PR workflow over a sandbox authentication repository.',
        '- Repo context used for planning:',
        *repo_context,
        '- Next step: review the proposed changes, confirm the approval gate, and decide whether to implement them in the sample app.',
        ''
    ]
    return '\n'.join(lines)

for ticket in tickets:
    write_markdown(f"{ticket['id']}/report.md", build_report(ticket))

index_content = """# Agent Demo Outputs\n\nThe following sample tickets were processed:\n\n- [ticket-1/report.md](ticket-1/report.md)\n- [ticket-2/report.md](ticket-2/report.md)\n\nRun with:\n\n```bash\nnpm run demo:agent\n```\n"""
write_markdown('README.md', index_content)
print(f"Generated {len(tickets)} demo reports in {output_root}")
