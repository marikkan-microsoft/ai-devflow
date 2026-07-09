---
mode: agent
description: Break an approved spec into a phased, dependency-ordered plan.
---

Follow the `plan-in-phases` skill in this repository
(`skills/plan-in-phases/SKILL.md`).

`${input:context}` may name the work slug or add context. Then:

- Read `docs/devflow/<slug>/spec.md` (and `research.md` if present).
- Write `docs/devflow/<slug>/plan.md` from `templates/plan.md` — thin
  vertical-slice tasks, each with files, acceptance criteria, the `R#`/`SC#` it
  satisfies, and its dependencies.
- Get explicit approval before implementation begins.
