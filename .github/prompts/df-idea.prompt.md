---
mode: agent
description: Turn a vague idea into ranked, grounded proposals.
---

Follow the `idea-refine` skill in this repository
(`skills/idea-refine/SKILL.md`).

`${input:context}` may describe the rough idea. Then:

- Diverge into 5–8 grounded options.
- Converge to a ranked top 3 with a single clear recommendation.
- Route the chosen pick to `align-and-grill`.
