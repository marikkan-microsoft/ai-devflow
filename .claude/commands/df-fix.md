---
description: Run the brownfield bug-fix fast-path.
---

Follow the `fix-workflow` instructions directly from
`skills/fix-workflow/SKILL.md`. This command is the user-invocation boundary; do
not try to invoke the model-hidden orchestrator as another skill.

`$ARGUMENTS` may describe the bug. Follow the skill exactly:

- Orchestrate the fast-path: reproduce & root-cause → failing repro test → fix at
  the root → verify → review → ship★ → compound.
- Pause for approval at the ★ ship milestone.
- Keep the fix minimal and test-first.
