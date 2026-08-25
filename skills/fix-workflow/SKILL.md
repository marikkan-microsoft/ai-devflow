---
name: fix-workflow
description: Orchestrates the brownfield bug-fix fast-path from broken behavior to a shipped, guarded fix. Use when the input is a bug, regression, or unexpected behavior rather than a new feature.
disable-model-invocation: true
---

# Fix Workflow

## Overview

The brownfield on-ramp. This orchestrator runs the bug-fix fast-path — reproduce,
find the root cause, fix it test-first, verify, review, ship, and compound — with
less ceremony than `feature-workflow` but the same discipline. It shares the
underlying skills; it just enters the loop at debugging instead of specification.

## When to Use

- A bug, regression, crash, or unexpected behavior is reported.
- A test or build is failing and needs fixing.
- Invoked via `/df-fix`.

**When NOT to use:** The "bug" is really a missing feature → use `feature-workflow`.
A large, ambiguous problem that needs requirements → start with `align-and-grill`.

**Related:** Orchestrates `debug-root-cause` (→ `research-codebase` as needed) →
`test-driven-development` → `verify-before-done` → `review-code` → `ship-it` →
`compound-learnings`. Uses `awesome-copilot-discovery` only for a named
specialist gap.

## Process

Fast-path — right-sized, but the gates still hold.

### Capability hook (conditional)

After the root cause identifies the technical domain, invoke
`awesome-copilot-discovery` only if the local fix path lacks specific expertise
(for example, a specialized migration or agent-supply-chain audit). Use at most
one accepted, pinned resource. It may sharpen diagnosis or review, but it cannot
replace the reproduction, failing test, root-cause proof, or existing review.

1. **Reproduce & root-cause** — `debug-root-cause`: get a deterministic repro,
   localize, and confirm the underlying cause (pull in `research-codebase` to map
   control flow if needed). Don't fix on a guess.
2. **Prove it** — write the failing reproduction test (`test-driven-development`'s
   Prove-It). It must fail for the right reason.
3. **Fix at the root** — minimal change that addresses the cause; watch the repro
   test go green. Consider a defense-in-depth guard.
4. **Verify** — `verify-before-done`: full suite green (no regressions), build
   clean.
5. **Review** — `review-code` on the diff (fast for small fixes, still two-axis for
   risky ones).
6. **★ Ship** — `ship-it`: PR with the repro test as evidence, green CI, merge.
   **Get approval to merge** for anything non-trivial.
7. **Compound** — `compound-learnings`: capture symptom, root cause, recognition
   signs, and the guardrail so this class of bug is cheap next time.

### Orchestration rules

- No fix before a reliable reproduction and a confirmed root cause.
- Small fixes skip specs/plans — but never skip the failing test or verification.
- Rewind if the "fix" doesn't hold: re-open `debug-root-cause`, don't pile on
  more guesses.
- Invokes model-invoked skills only — never another orchestrator.

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "I see the fix, I'll skip the repro." | Unreproduced fixes mask the cause and regress. Reproduce first. |
| "Too small for a test." | The repro test is what proves it and guards it. Write it. |
| "Symptom's gone, ship it." | Symptom gone ≠ root fixed. Confirm the cause explains all of it. |
| "No need to compound a bug fix." | Bug classes recur. The note makes the next one minutes. |

## Red Flags

- Code changed before a reliable reproduction existed.
- External guidance was used without a pinned source and capability-fit decision.
- No failing test captured the bug.
- Only the new test ran, not the full suite.
- The fix shipped with no `solutions/` note.

## Verification

- Deterministic repro and confirmed root cause preceded the fix.
- Any specialist gap has a recorded `USED`, `REJECTED`, or `SKIPPED`
  capability-hook decision.
- A test that failed before the fix now passes; full suite green.
- The change was reviewed and shipped per those skills.
- A `solutions/` note captured cause, signs, and guardrail.
