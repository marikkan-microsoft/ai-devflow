---
description: Take a verified, reviewed change to production safely.
---

Invoke the `devflow:ship-it` skill.

`$ARGUMENTS` may name the branch or add context. Follow the skill exactly:

- Open a clear PR with verification evidence and get CI green.
- Roll out behind a flag in stages, watching the signals at each step.
- Route any learnings to `compound-learnings`.
