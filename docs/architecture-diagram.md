# Architecture Diagram

```mermaid
graph TD
    A[Developer submits story or bug ticket] --> B[Clarification and task framing]
    B --> C[Repository reader and context loader]
    C --> D[Implementation planner]
    D --> E[Test and review agent]
    E --> F[Approval gate]
    F --> G[PR handoff summary]
    B -.-> H[Memory store for standards and prior decisions]
    D -.-> H
    E -.-> H
```

## Components
- Developer input: stories, acceptance criteria, logs, or tickets.
- Repository reader: inspects the sandbox app structure and relevant files.
- Planner: breaks the request into implementation, testing, and review work.
- Review agent: highlights risks around readability, security, maintainability, and testing.
- Approval gate: ensures a human confirms major changes before implementation.
