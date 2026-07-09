---
mode: agent
description: Take a verified, reviewed change to production safely.
---

Follow the `ship-it` skill in this repository
(`skills/ship-it/SKILL.md`).

`${input:context}` may name the branch or add context. Then:

- Open a clear PR with verification evidence and get CI green.
- Roll out behind a flag in stages, watching the signals at each step.
- Route any learnings to `compound-learnings`.
