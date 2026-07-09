---
mode: agent
description: Run the full greenfield loop from idea to shipped.
---

Follow the `feature-workflow` skill in this repository
(`skills/feature-workflow/SKILL.md`).

`${input:context}` may describe the feature. Then:

- Orchestrate the full loop: align → spec★ → research → plan★ → build → verify →
  review → ship★ → compound.
- Pause for approval at each ★ milestone (spec, plan, ship).
- Hand each durable artifact to the next phase; rewind if requirements change.
