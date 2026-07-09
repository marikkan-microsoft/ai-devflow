---
name: debug-root-cause
description: Finds and fixes the true cause of a bug through a systematic reproduce-localize-fix-guard process. Use when a test fails, a build breaks, behavior is unexpected, or a bug is reported — instead of guessing at fixes.
---

# Debug Root Cause

## Overview

Guess-and-check debugging fixes symptoms and breeds regressions. This skill runs a
disciplined loop — **reproduce → localize → hypothesize → fix → guard** — that
finds the actual cause and leaves behind a test so it can't come back. It is the
core of the brownfield/bugfix fast-path (`fix-workflow`).

## When to Use

- A test fails, a build breaks, or behavior is unexpected.
- A bug is reported from any source.
- A performance regression appears.

**When NOT to use:** The "bug" is actually a missing feature (use
`write-spec`/`plan-in-phases`). Don't debug unfinished work — build it.

**Related:** Uses `test-driven-development`'s Prove-It pattern. May need
`research-codebase` to map control flow. Findings feed `compound-learnings`.

## Process

### 1. Reproduce — reliably

Get a deterministic reproduction before touching anything. If it's flaky, make it
consistent first (control timing, seeds, inputs). You cannot fix what you can't
reproduce, and you can't prove a fix without it.

### 2. Localize — narrow the search space

Bisect the problem: shrink inputs, add targeted instrumentation/logging, use
`git bisect` for regressions, and read the actual `file:line`. Follow the evidence
toward the smallest failing case. Don't theorize in the abstract.

### 3. Hypothesize and confirm the root cause

Form a specific hypothesis about the **underlying** cause (not the surface
symptom) and confirm it with evidence — a log, a value, a failing assertion. Keep
going until the cause explains **all** the observed behavior.

### 4. Write the failing test (Prove-It)

Encode the bug as a test that fails now (confirming the cause). This is the proof
your fix works and the guardrail against regression.

### 5. Fix at the root

Fix the cause, not the symptom. Prefer the minimal change that addresses the root.
Watch the reproduction test go green.

### 6. Guard and verify

Run the full suite (`verify-before-done`) — the fix must not regress anything.
Consider defense-in-depth (an assertion/validation nearer the source). Then
`compound-learnings` to capture the cause, the tell-tale signs, and the guardrail.

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "I think I know the fix, I'll just apply it." | Unconfirmed fixes mask the real cause. Reproduce and confirm first. |
| "It's too flaky to reproduce." | Then make it deterministic — that's step one, not a skip. |
| "The symptom is gone, done." | Symptom gone ≠ cause fixed. Confirm the root explains everything. |
| "No need for a test, I saw it work." | Without a repro test it silently regresses. Prove-It. |

## Red Flags

- You changed code before reliably reproducing the bug.
- The fix addresses a symptom and you're unsure why it worked.
- No failing test captured the bug.
- The full suite wasn't run after the fix.

## Verification

- A deterministic reproduction existed before the fix.
- The root cause is confirmed by evidence and explains all symptoms.
- A test that failed before the fix now passes.
- Full suite green; the learning is captured via `compound-learnings`.
