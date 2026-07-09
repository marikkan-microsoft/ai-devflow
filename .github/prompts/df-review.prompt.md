---
mode: agent
description: Two-axis review (spec + standards) before merge.
---

Follow the `review-code` skill in this repository
(`skills/review-code/SKILL.md`).

`${input:context}` may name the branch, PR, or diff range. Then:

- Run the spec axis (`spec-auditor`) and the standards axis (`code-reviewer`) in
  parallel against the diff since the branch base.
- Synthesize a single severity-labeled verdict: APPROVE or REQUEST CHANGES.
- Resolve Critical and Important findings before merge.
