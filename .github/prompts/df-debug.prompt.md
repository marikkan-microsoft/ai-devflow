---
mode: agent
description: Find and fix the true cause of a bug, test-first.
---

Follow the `debug-root-cause` skill in this repository
(`skills/debug-root-cause/SKILL.md`).

`${input:context}` may describe the bug or failure. Then:

- Reproduce it deterministically, then localize and confirm the true root cause.
- Write a failing repro test, fix at the root, and run the full suite green.
- Route the lesson to `compound-learnings`.
