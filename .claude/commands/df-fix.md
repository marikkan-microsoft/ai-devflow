---
description: Run the brownfield bug-fix fast-path.
---

Invoke the `devflow:fix-workflow` skill.

`$ARGUMENTS` may describe the bug. Follow the skill exactly:

- Orchestrate the fast-path: reproduce & root-cause → failing repro test → fix at
  the root → verify → review → ship★ → compound.
- Pause for approval at the ★ ship milestone.
- Keep the fix minimal and test-first.
