---
description: Break an approved spec into a phased, dependency-ordered plan.
---

Invoke the `devflow:plan-in-phases` skill.

`$ARGUMENTS` may name the work slug or add context. Follow the skill exactly:

- Read `docs/devflow/<slug>/spec.md` (and `research.md` if present).
- Write `docs/devflow/<slug>/plan.md` from the plan template — thin vertical-slice
  tasks, each with files, acceptance criteria, the `R#`/`SC#` it satisfies, and
  its dependencies.
- Get explicit approval before implementation begins.
