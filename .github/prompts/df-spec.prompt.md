---
mode: agent
description: Write a durable, measurable spec before code.
---

Follow the `write-spec` skill in this repository
(`skills/write-spec/SKILL.md`).

`${input:context}` may name the work slug or add context. Then:

- Synthesize the aligned intent into `docs/devflow/<slug>/spec.md` from
  `templates/spec.md`.
- Make every success criterion measurable; mark open questions
  `[NEEDS CLARIFICATION]`.
- Get explicit approval before moving on.
