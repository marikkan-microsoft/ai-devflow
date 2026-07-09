---
name: review-code
description: Reviews a change on two independent axes — spec compliance and code standards — using parallel personas, then synthesizes a verdict. Use before merging any change, or when asked to review a diff, file, or PR.
---

# Review Code

## Overview

A good review catches the pattern, not just the bug. This skill reviews a change
on **two independent axes** run as parallel personas so neither contaminates the
other: **Spec** (does it faithfully implement the originating spec/task?) via
`spec-auditor`, and **Standards** (is the code correct, readable, secure,
performant?) via `code-reviewer`. It then synthesizes one verdict with severity-
labeled findings.

## When to Use

- Before merging any change.
- When asked to review a specific diff, file, or PR.
- As the gate after `verify-before-done`, before `ship-it`.

**When NOT to use:** Work that isn't verified yet — run `verify-before-done` first;
an unverified change isn't ready for review.

**Related:** Fan-out to `spec-auditor` + `code-reviewer` (and `security-auditor` /
`performance-auditor` when warranted). Rubric in
[references/code-review-rubric.md](../../references/code-review-rubric.md).

## Process

### 1. Fix the review baseline

Establish exactly what's under review: the diff since a known point (branch base
or last reviewed commit). Load the originating `spec.md`/task and `CONTEXT.md`.

### 2. Run the two axes in parallel

Dispatch both, independently, so their judgments don't blur:

- **Spec axis (`spec-auditor`):** Does the change do what the spec/task asked —
  nothing missing, nothing extra, criteria met? Ignore style here.
- **Standards axis (`code-reviewer`):** Correctness, readability, architecture,
  security, performance — against the repo's conventions and a smell baseline.
  Ignore "is it what was asked" here.

Neither persona invokes the other; orchestration stays here.

### 3. Size and label findings

Prefer small changes (~≤ a few hundred lines) — flag oversized diffs and suggest
splitting. Label every finding: **Critical** (block), **Important** (should fix),
**Suggestion** (optional). Each Critical/Important carries a specific fix.

### 4. Synthesize the verdict

Merge both reports into one: **APPROVE** or **REQUEST CHANGES**. Any Critical means
REQUEST CHANGES. Note what's done well — specific praise reinforces good patterns.

### 5. Route follow-ups

Critical/Important issues go back through the build loop; for PRs, hand structured
comments to `resolve-pr-feedback`.

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "One pass covers spec and quality." | They contaminate each other. Two independent axes. |
| "Looks good, approve." | Reviews need evidence and named findings, not vibes. |
| "It's big but fine to review whole." | Oversized diffs hide defects. Flag and split. |
| "Only list problems." | Unlabeled severity buries the blockers. Label everything. |

## Red Flags

- Spec and standards judgments are mixed into one opinion.
- Findings have no severity labels or no fix recommendations.
- A Critical issue exists but the verdict is APPROVE.
- The review ran on unverified code.

## Verification

- Both axes ran independently against a fixed baseline.
- Every finding is severity-labeled; Critical/Important include fixes.
- A single clear verdict (APPROVE / REQUEST CHANGES) is given.
- Blockers are routed to a fix; nothing Critical is approved.
