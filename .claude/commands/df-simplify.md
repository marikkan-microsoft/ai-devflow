---
description: Reduce complexity while preserving behavior.
---

Invoke the `devflow:simplify-code` skill.

`$ARGUMENTS` may target a file or area. Follow the skill exactly:

- Start from a green test suite and apply Chesterton's Fence before removing
  anything.
- Reduce complexity without changing observable behavior.
- Keep the suite green throughout.
