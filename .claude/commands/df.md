---
description: Route the current task to the right devflow skill and phase.
---

Invoke the `devflow:using-devflow` skill.

`$ARGUMENTS` may describe the task. Follow the skill exactly:

- Read the accumulated context — `docs/devflow/CONTEXT.md` and
  `docs/devflow/solutions/` — and resume any in-progress `<slug>`.
- Pick the on-ramp: `feature-workflow` for new work, `fix-workflow` for bugs, or a
  single phase skill for a small, well-understood change.
- Announce the chosen skill, then follow it.
