const fs = require('fs');
const path = require('path');

const repoRoot = __dirname;
const outputRoot = path.join(repoRoot, 'markdown_docs');

if (!fs.existsSync(outputRoot)) {
  fs.mkdirSync(outputRoot, { recursive: true });
}

const tickets = [
  {
    id: 'ticket-1',
    title: 'Add client-side validation to the password reset form',
    story: 'As a user, I want clear feedback when I submit an invalid password reset so I can recover my account without confusion.',
    acceptanceCriteria: [
      'The form shows inline validation for short or missing passwords.',
      'The submit flow stops before the reset request is sent when validation fails.',
      'The experience remains usable on mobile and desktop.'
    ],
    impactedFiles: [
      'myridius-auth-demo/views/resetPassword.html',
      'myridius-auth-demo/auth/authController.js',
      'myridius-auth-demo/auth/routes.js'
    ],
    implementationPlan: [
      'Add a minimal validation rule in the reset form before the request is posted.',
      'Surface server-side feedback in the controller so the UI can show a helpful error message.',
      'Keep the change localized to the password reset flow to avoid broad regressions.'
    ],
    testCases: [
      'Unit: validates a password shorter than 8 characters.',
      'Unit: accepts a password meeting the minimum strength requirement.',
      'Integration: prevents submission when validation fails and preserves the existing form state.'
    ],
    reviewFindings: [
      'Readable and localized change with low complexity.',
      'Security risk remains low because the validation is client-side and should be mirrored server-side.',
      'Consider adding a stronger password policy once the product requirements are finalized.'
    ]
  },
  {
    id: 'ticket-2',
    title: 'Add audit logging for failed password reset attempts',
    story: 'As an operator, I want failed password reset attempts logged so I can investigate suspicious account activity.',
    acceptanceCriteria: [
      'Every failed reset attempt produces a structured log entry.',
      'The log captures the request context and a failure reason.',
      'The change does not block the existing reset flow.'
    ],
    impactedFiles: [
      'myridius-auth-demo/auth/authController.js',
      'myridius-auth-demo/server.js',
      'myridius-auth-demo/auth/routes.js'
    ],
    implementationPlan: [
      'Wrap the reset handler with a small logging helper that records failures.',
      'Emit a structured log entry for invalid tokens and missing passwords.',
      'Leave the primary UX intact and require human approval before shipping the logging policy.'
    ],
    testCases: [
      'Unit: records a failure when the reset token is invalid.',
      'Unit: records a failure when a password is missing from the request body.',
      'Integration: confirms the reset flow still returns a safe response after logging.'
    ],
    reviewFindings: [
      'Improves supportability and security observability.',
      'Ensure logs avoid leaking secrets or personally identifiable information.',
      'Consider a dedicated logger abstraction before expanding to more features.'
    ]
  }
];

function readFile(relativePath) {
  return fs.readFileSync(path.join(repoRoot, relativePath), 'utf8');
}

function writeMarkdown(relativePath, content) {
  const absolutePath = path.join(outputRoot, relativePath);
  fs.mkdirSync(path.dirname(absolutePath), { recursive: true });
  fs.writeFileSync(absolutePath, content, 'utf8');
}

function buildReport(ticket) {
  const repoContext = [
    `- Sample app entry point: ${readFile('myridius-auth-demo/server.js').split('\n')[0]}`,
    `- Auth routes: ${readFile('myridius-auth-demo/auth/routes.js').split('\n')[0]}`,
    `- Current reset handler: ${readFile('myridius-auth-demo/auth/authController.js').split('\n')[0]}`
  ].join('\n');

  return `# ${ticket.title}\n\n## Story\n${ticket.story}\n\n## Acceptance Criteria\n${ticket.acceptanceCriteria.map((item) => `- ${item}`).join('\n')}\n\n## Clarification\n- The repository is a sandbox password reset demo with a simple Express server.\n- Assumption: the request is for implementation guidance rather than changing production code directly.\n- Approval gate: a human reviewer should approve any code change before it is merged.\n\n## Impacted Files\n${ticket.impactedFiles.map((file) => `- ${file}`).join('\n')}\n\n## Implementation Plan\n${ticket.implementationPlan.map((step) => `- ${step}`).join('\n')}\n\n## Test Cases\n${ticket.testCases.map((testCase) => `- ${testCase}`).join('\n')}\n\n## Review Findings\n${ticket.reviewFindings.map((finding) => `- ${finding}`).join('\n')}\n\n## PR Summary\n- This PoC demonstrates a story-to-PR workflow over a sandbox authentication repository.\n- Repo context used for planning:\n${repoContext}\n- Next step: review the proposed changes, confirm the approval gate, and decide whether to implement them in the sample app.\n`;
}

for (const ticket of tickets) {
  const ticketDir = path.join(ticket.id);
  writeMarkdown(path.join(ticketDir, 'report.md'), buildReport(ticket));
}

const indexContent = `# Agent Demo Outputs\n\nThe following sample tickets were processed:\n\n- [ticket-1/report.md](ticket-1/report.md)\n- [ticket-2/report.md](ticket-2/report.md)\n\nRun with:\n\n\`\`\`bash\nnpm run demo:agent\n\`\`\`\n`;

writeMarkdown('README.md', indexContent);
console.log(`Generated ${tickets.length} demo reports in ${outputRoot}`);
