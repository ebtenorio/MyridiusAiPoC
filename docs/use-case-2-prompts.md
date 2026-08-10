# Use Case 2: Prompt Library

## Workspace Rules

You are assisting a backend developer in an anonymized Express sandbox. Follow the repository's existing JavaScript style. Use only explicitly allowlisted context. Do not expose secrets, invent production endpoints, modify files, execute commands, or approve changes. State assumptions, uncertainty, limitations, security concerns, and test gaps. Require human review before acceptance.

## Inline Generation

> Convert this developer comment into the smallest maintainable code proposal. Preserve existing successful behavior, show the changed function, list assumptions, and include negative-path tests. Do not write files.

## Chat: Explain and Debug

> Explain this handler line by line in the context of the supplied repository. Identify the most likely runtime failure, distinguish evidence from assumptions, and propose the smallest diagnostic step before changing code.

## Chat: Generate Tests

> Generate unit and HTTP-level test cases for valid input, missing input, malformed input, downstream failure, and sensitive-data leakage. Use the repository's existing test conventions; if none exist, state that limitation and provide framework-neutral test intent.

## Scaffolding

> Scaffold an Express route/controller test boundary for this task. Show the file tree, minimal boilerplate, interfaces between modules, error handling, and test seams. Do not add dependencies unless justified.

## Review

> Review the proposal for readability, maintainability, security, performance, error handling, and test gaps. Return findings with severity, evidence, rationale, and remediation. Flag missing token validation, secret exposure, over-generation, and unclear assumptions.

## Refactoring

> Suggest a behavior-preserving refactor. Explain what remains invariant, why the refactor helps, its trade-offs, and the tests that should pass before and after. Stop at a human approval gate.