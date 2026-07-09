---
mode: agent
description: Run the brownfield bug-fix fast-path.
---

Follow the `fix-workflow` skill in this repository
(`skills/fix-workflow/SKILL.md`).

`${input:context}` may describe the bug. Then:

- Orchestrate the fast-path: reproduce & root-cause → failing repro test → fix at
  the root → verify → review → ship★ → compound.
- Pause for approval at the ★ ship milestone.
- Keep the fix minimal and test-first.
