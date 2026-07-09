---
mode: agent
description: Implement the plan test-first; add `auto` for one-approval autonomous run.
---

Follow the `subagent-driven-implementation` skill in this repository
(`skills/subagent-driven-implementation/SKILL.md`).

With no `${input:context}`, implement the **next pending task** from
`docs/devflow/<slug>/plan.md`:

- Dispatch it to a fresh subagent, built test-first via `test-driven-development`
  (RED → GREEN → refactor).
- Run the two-stage review (spec compliance, then code quality); make one commit
  per task, then stop.

If `${input:context}` is `auto` (or `all`), follow the `autopilot` skill
(`skills/autopilot/SKILL.md`) instead — one approval gate, then run every
remaining task autonomously, stopping only for blockers or irreversible steps.
