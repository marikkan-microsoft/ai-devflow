---
mode: agent
description: Reduce complexity while preserving behavior.
---

Follow the `simplify-code` skill in this repository
(`skills/simplify-code/SKILL.md`).

`${input:context}` may target a file or area. Then:

- Start from a green test suite and apply Chesterton's Fence before removing
  anything.
- Reduce complexity without changing observable behavior.
- Keep the suite green throughout.
