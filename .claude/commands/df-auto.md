---
description: Run build→PR autonomously after one approval.
---

Follow the `autopilot` instructions directly from `skills/autopilot/SKILL.md`.
This command is the user-invocation boundary; do not try to invoke the
model-hidden orchestrator as another skill.

`$ARGUMENTS` may name the work slug or add context. Follow the skill exactly:

- Require an approved `spec.md` (or a confirmed bug) and a clean git baseline.
- Take one approval gate, then run plan → build → verify → review → PR
  autonomously, stopping only for blockers or irreversible steps.
- End at a green open PR, route learnings to `compound-learnings`, and summarize.
