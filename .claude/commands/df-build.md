---
description: Implement the plan test-first; add `auto` for one-approval autonomous run.
---

Invoke the `devflow:subagent-driven-implementation` skill.

With no arguments, implement the **next pending task** from
`docs/devflow/<slug>/plan.md`:

- Dispatch it to a fresh `software-engineer` subagent, built test-first via `test-driven-development`
  (RED → GREEN → refactor).
- Run the two-stage review (spec compliance, then code quality); make one commit
  per task, then stop.

If `$ARGUMENTS` is `auto` (or `all`), invoke the `devflow:autopilot` skill instead
— one approval gate, then run every remaining task autonomously, stopping only for
blockers or irreversible steps.
