---
mode: agent
description: Route the current task to the right devflow skill and phase.
---

Follow the `using-devflow` skill in this repository
(`skills/using-devflow/SKILL.md`).

`${input:context}` may describe the task. Then:

- Read the accumulated context — `docs/devflow/CONTEXT.md` and
  `docs/devflow/solutions/` — and resume any in-progress `<slug>`.
- Pick the on-ramp: `feature-workflow` for new work, `fix-workflow` for bugs, or a
  single phase skill for a small, well-understood change.
- Announce the chosen skill, then follow it.
