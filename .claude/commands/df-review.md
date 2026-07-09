---
description: Two-axis review (spec + standards) before merge.
---

Invoke the `devflow:review-code` skill.

`$ARGUMENTS` may name the branch, PR, or diff range. Follow the skill exactly:

- Run the spec axis (`spec-auditor`) and the standards axis (`code-reviewer`) in
  parallel against the diff since the branch base.
- Synthesize a single severity-labeled verdict: APPROVE or REQUEST CHANGES.
- Resolve Critical and Important findings before merge.
