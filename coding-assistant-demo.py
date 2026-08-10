"""Offline-first AI coding assistant evidence generator for Use Case 2."""

from pathlib import Path
import json
import os
import re
import sys
import urllib.error
import urllib.request


REPO_ROOT = Path(__file__).resolve().parent
OUTPUT_ROOT = REPO_ROOT / 'markdown_docs' / 'use-case-2'
CONTEXT_FILES = [
    'myridius-auth-demo/auth/authController.js',
    'myridius-auth-demo/auth/routes.js',
    'myridius-auth-demo/server.js',
    'myridius-auth-demo/views/resetPassword.html'
]

TASK = {
    'id': 'coding-task-001',
    'title': 'Add server-side password reset validation',
    'comment': 'Validate the submitted password before reset and return a safe error without leaking credentials.',
    'role': 'Backend developer maintaining a small Express authentication demo.',
    'acceptance_criteria': [
        'Reject a missing or shorter-than-eight-character password.',
        'Do not expose the password or reset token in responses or logs.',
        'Preserve the existing successful reset response for valid input.'
    ]
}


def read_context() -> str:
    chunks = []
    for relative_path in CONTEXT_FILES:
        content = (REPO_ROOT / relative_path).read_text(encoding='utf-8')
        content = re.sub(r'(?i)(api[_-]?key|token|password)\s*[:=]\s*[^,\n]+', r'\1: [REDACTED]', content)
        chunks.append(f'FILE: {relative_path}\n{content}')
    return '\n\n'.join(chunks)


def load_model() -> str:
    configured_model = os.environ.get('OPENAI_MODEL')
    if configured_model:
        return configured_model
    config_path = REPO_ROOT / 'config.toml'
    for line in config_path.read_text(encoding='utf-8').splitlines():
        if line.strip().startswith('model') and '=' in line:
            return line.split('=', 1)[1].strip().strip('"')
    return 'gpt-4o-mini'


def deterministic_result() -> dict:
    return {
        'analysis_mode': 'Deterministic sandbox output',
        'result_source': 'Local deterministic fallback; no API request was made.',
        'assumptions': [
            'The sample Express app is illustrative and has no real database or token service.',
            'The requested change is guidance/evidence; the assistant does not edit application files.',
            'A human developer must adapt the response to the project test runner before acceptance.'
        ],
        'generated_code': """exports.handleReset = (req, res) => {
  const { password } = req.body;
  if (typeof password !== 'string' || password.length < 8) {
    return res.status(400).send('Password must be at least 8 characters.');
  }

  // In real app: update DB with new password
  return res.send('Password reset successful!');
};""",
        'tests': """describe('handleReset', () => {
  it('rejects a missing password without exposing request data', () => {
    const response = invoke({ body: {} });
    expect(response.statusCode).toBe(400);
    expect(response.body).not.toContain('undefined');
  });

  it('rejects passwords shorter than eight characters', () => {
    expect(invoke({ body: { password: 'short' } }).statusCode).toBe(400);
  });

  it('keeps the successful response for a valid password', () => {
    expect(invoke({ body: { password: 'valid-pass' } }).body)
      .toBe('Password reset successful!');
  });
});""",
    'scaffolding': """myridius-auth-demo/auth/passwordPolicy.js
myridius-auth-demo/test/authController.test.js

// passwordPolicy.js
exports.isValidPassword = (password) =>
  typeof password === 'string' && password.length >= 8;

// authController.test.js
// Add unit coverage for missing, short, and valid passwords.""",
        'chat_answers': [
            'Why server-side validation? Client-side rules improve UX but cannot be trusted at an HTTP boundary.',
            'What remains uncertain? The real password policy, token validation, persistence, and test framework are not present in this sandbox.',
            'What should happen next? Confirm the product policy, add token/database tests, then have a human review the patch.'
        ],
        'review_findings': [
            {'severity': 'High', 'area': 'Security', 'finding': 'The sample still lacks real reset-token validation and persistence safeguards.', 'remediation': 'Validate the token server-side, use a one-time expiry-aware store, and hash the new password before persistence.'},
            {'severity': 'Medium', 'area': 'Error handling', 'finding': 'The handler has no explicit malformed-body or downstream failure path.', 'remediation': 'Add centralized error middleware and a safe generic response for unexpected failures.'},
            {'severity': 'Medium', 'area': 'Testing', 'finding': 'There is no test runner or integration coverage in the sample repository.', 'remediation': 'Add isolated unit tests plus an HTTP test covering valid, invalid, and token-related requests.'},
            {'severity': 'Low', 'area': 'Maintainability', 'finding': 'The minimum length is a magic number.', 'remediation': 'Move the policy to a named constant or configuration value once requirements are confirmed.'}
        ],
        'refactoring': {
            'suggestion': 'Extract password validation into a pure helper and keep the controller responsible for HTTP responses.',
            'tradeoff': 'This improves unit-test isolation and makes policy changes clearer, but adds a file for a very small demo.',
            'approval_gate': 'Do not apply the refactor until the team confirms the password policy and test conventions.'
        },
        'prompt_iteration': {
            'baseline_prompt': 'Generate code for the password reset task.',
            'revised_prompt': 'Generate code and tests, provide three chat answers, scaffold the test boundary, identify at least three review issues, explain behavior-preserving refactoring trade-offs, and state assumptions. Do not edit files; require human approval.',
            'improvement': 'The revised prompt makes the required evidence explicit, reducing incomplete outputs and making the result easier to review.'
        }
    }


def ai_result() -> dict:
    api_key = os.environ.get('OPENAI_API_KEY')
    if not api_key:
        raise RuntimeError('AI mode requires OPENAI_API_KEY; deterministic mode is available offline.')
    prompt = {
        'task': TASK,
        'repository_context': read_context(),
        'response_contract': list(deterministic_result().keys()),
        'safety_rules': ['Do not edit files or execute commands.', 'List assumptions and limitations.', 'Flag secrets and insecure code.', 'Require human approval.']
    }
    payload = json.dumps({
        'model': load_model(),
        'temperature': 0.2,
        'response_format': {'type': 'json_object'},
        'messages': [
            {'role': 'system', 'content': 'You are a cautious senior coding assistant. Return only valid JSON matching the response contract. Provide at least three developer chat answers, a project scaffolding proposal, at least three review findings across different risk areas, a behavior-preserving refactoring explanation with trade-offs, and a baseline-versus-revised prompt iteration showing improvement. Do not edit files, execute commands, expose secrets, or approve changes.'},
            {'role': 'user', 'content': json.dumps(prompt)}
        ]
    }).encode('utf-8')
    request = urllib.request.Request(
        os.environ.get('OPENAI_BASE_URL', 'https://api.openai.com/v1') + '/chat/completions',
        data=payload,
        headers={'Authorization': f'Bearer {api_key}', 'Content-Type': 'application/json'},
        method='POST'
    )
    try:
        with urllib.request.urlopen(request, timeout=90) as response:
            response_data = json.loads(response.read().decode('utf-8'))
    except urllib.error.HTTPError as error:
        raise RuntimeError(f'AI request failed with HTTP {error.code}.') from error
    except urllib.error.URLError as error:
        raise RuntimeError(f'AI request could not reach the configured endpoint: {error.reason}') from error
    result = json.loads(response_data['choices'][0]['message']['content'])
    required = set(deterministic_result())
    missing = required - set(result)
    if missing:
        raise RuntimeError(f'AI response is missing fields: {sorted(missing)}')
    if len(result.get('chat_answers', [])) < 3:
        raise RuntimeError('AI response must contain at least three chat answers.')
    if len(result.get('review_findings', [])) < 3:
        raise RuntimeError('AI response must contain at least three review findings.')
    result['analysis_mode'] = f"AI-generated ({load_model()})"
    result['result_source'] = 'OpenAI-compatible API response'
    result['provider'] = os.environ.get('OPENAI_BASE_URL', 'https://api.openai.com/v1')
    result['model'] = load_model()
    return result


def markdown(result: dict) -> str:
    findings = '\n'.join(format_review_finding(item) for item in result['review_findings'])
    refactoring = format_refactoring(result['refactoring'])
    prompt_iteration = format_prompt_iteration(result['prompt_iteration'])
    return f"""# Use Case 2: AI Coding Assistant Evidence

**Task:** {TASK['title']}  
**Analysis mode:** {result['analysis_mode']}

**Result source:** {result.get('result_source', 'Not recorded')}  
**Model:** {result.get('model', 'Not recorded')}  
**Provider endpoint:** {result.get('provider', 'Not recorded')}

## 1. Context and Prompt

**Role:** {TASK['role']}

**Developer comment:** {TASK['comment']}

**Acceptance criteria:**
{chr(10).join(f'- {item}' for item in TASK['acceptance_criteria'])}

Repository context was restricted to the allowlisted sample files: {', '.join(CONTEXT_FILES)}.

## 2. Assumptions and Limitations

{chr(10).join(f'- {item}' for item in result['assumptions'])}

## 3. Generated Code

```javascript
{result['generated_code']}
```

The assistant proposes code only. It does not write this patch into the application.

## 4. Generated Tests

```javascript
{result['tests']}
```

## 5. Project Scaffolding

```text
{result['scaffolding']}
```

## 6. Chat Follow-up

{chr(10).join(f'- {item}' for item in result['chat_answers'])}

## 7. AI Review Checklist

{findings}

## 8. Refactoring Recommendation

{refactoring}

## 9. Prompt Iteration

{prompt_iteration}

## 10. Before / After Evidence

**Before:** `handleReset` reads the request password and always returns success.

**After proposal:** the handler rejects missing or short passwords, returns a safe status, and preserves the valid-input response. Token validation and password persistence remain explicit follow-up work.

**Safety check:** no credentials, tokens, production endpoints, or application files were written by this demo. Human review is required before acceptance.
"""


def format_prompt_iteration(item: dict | list | str) -> str:
    if isinstance(item, str):
        return f'**Iteration:** {item}\n\n**Observed improvement:** Human review is required to assess the improvement.'
    if isinstance(item, list):
        steps = '\n'.join(f'- {step}' for step in item)
        return f'**Iteration steps:**\n{steps}\n\n**Observed improvement:** Human review is required to assess the improvement.'
    baseline = item.get('baseline_prompt', item.get('baseline', 'Not supplied by the model.'))
    revised = item.get('revised_prompt', item.get('revised', 'Not supplied by the model.'))
    improvement = item.get(
        'improvement',
        'The revised prompt adds explicit security and validation requirements; compare both outputs during human review.'
    )
    return f'**Baseline prompt:** {baseline}\n\n**Revised prompt:** {revised}\n\n**Observed improvement:** {improvement}'


def format_refactoring(item: dict | list | str) -> str:
    if isinstance(item, str):
        return f'**Suggestion:** {item}\n\n**Approval gate:** Human review is required before applying it.'
    if isinstance(item, list):
        suggestions = '\n'.join(f'- {suggestion}' for suggestion in item)
        return f'**Suggestions:**\n{suggestions}\n\n**Approval gate:** Human review is required before applying them.'
    suggestion = item.get('suggestion', item.get('explanation', 'No refactoring suggestion supplied.'))
    tradeoff = item.get('tradeoff', item.get('trade_offs', 'Trade-offs require human assessment.'))
    approval_gate = item.get('approval_gate', 'Human review is required before applying it.')
    return f'**Suggestion:** {suggestion}\n\n**Trade-off:** {tradeoff}\n\n**Approval gate:** {approval_gate}'


def format_review_finding(item: dict | str) -> str:
    if isinstance(item, str):
        return f'- **Model finding:** {item}'
    area = item.get('area', item.get('risk_area', 'General'))
    finding = item.get('finding', 'No finding details supplied.')
    remediation = item.get('remediation', 'Human review required.')
    return (
        f"- **{item.get('severity', 'Unspecified')} / {area}:** {finding} "
        f"Remediation: {remediation}"
    )


def main() -> None:
    use_ai = '--ai' in sys.argv
    result = ai_result() if use_ai else deterministic_result()
    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)
    (OUTPUT_ROOT / 'evidence.md').write_text(markdown(result), encoding='utf-8')
    (OUTPUT_ROOT / 'result.json').write_text(json.dumps(result, indent=2), encoding='utf-8')
    print(f"Generated Use Case 2 evidence in {OUTPUT_ROOT}")


if __name__ == '__main__':
    main()