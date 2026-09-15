---
name: incremental-implementation
description: Implements changes as thin vertical slices — build, test, verify, commit — with rollback-friendly defaults. Use for any change touching more than one file, or when subagent-driven execution isn't available.
---

# Incremental Implementation

## Overview

Small, deliberate steps are the speed limit of good software: the rate of
feedback governs how fast you can safely go. This skill implements a plan (or a
standalone change) as **thin vertical slices**, each built test-first, verified,
and committed on its own — with feature flags and safe defaults so any slice is
reversible. It's the direct-execution counterpart to
`subagent-driven-implementation`.

## When to Use

- Any change touching more than one file.
- Executing a `plan.md` without dispatching subagents.
- When you want a clean, per-slice commit history you can bisect and revert.

**When NOT to use:** A one-line, zero-risk change. Don't ceremony-wrap a typo fix.

**Related:** Drives `test-driven-development` per slice, applying the
`software-engineer` persona's build standards. Optionally isolates work
with a git worktree/branch (see below). Feeds `verify-before-done` and `review-code`.

## Process

### 1. Isolate the work

Work on a dedicated branch — or a **git worktree** for true isolation when running
long or in parallel with other work. Confirm a green test baseline before you
start; you can't tell what you broke without one.

On interruption, use `context-engineering` and
[resume reconciliation](../../references/execution-checkpoints.md#resume-reconciliation)
before choosing work. Preserve existing changes and recover the missing task or
gate; a checkpoint is not permission to reset files or repeat side effects.

### 2. Take the next thin slice

Pick the next task/slice from `plan.md`. A slice delivers one testable behavior
end-to-end (not a horizontal layer). If it's bigger than that, split it.

Use the same bounded [task packet](../../references/execution-checkpoints.md#task-packets)
as delegated execution. Confirm dependencies and external prerequisites before
changing files; an unknown or halted producer does not release its consumers.

### 3. Build it test-first

Follow `test-driven-development`: write a failing test (RED), minimal code to pass
(GREEN), then refactor. Prefer feature flags and safe defaults so the slice can
ship dark and roll back cleanly.

### 4. Verify the slice

Run the full test suite (catch regressions) and the build (catch compile breaks).
Green before you commit — never commit on red.

Before expanding a tracer or advancing a phase, exercise the critical connection
in the integrated tree and record
[phase closure](../../references/execution-checkpoints.md#phase-closure) in the
plan. Check the approved target, not only task claims; return changed
scope/contracts to approval and applicable artifact analysis.

### 5. Commit the slice

Stage only the files this slice touched (never `git add -A`) plus its plan-status
update. Commit with a descriptive message. This commit is a save point and a
clean rollback boundary.

### 6. Repeat, then hand off

Continue in dependency order. When done, run `verify-before-done`, then
`review-code`. Stop and ask on unfixable failures or high-risk/irreversible steps.
Apply the shared [execution bounds](../../references/execution-checkpoints.md#bounded-execution);
checkpoint blockers, consumed attempts, and the exact next gate before stopping.

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "I'll implement it all, then test at the end." | Big-bang integration hides which slice broke. Slice and verify. |
| "Commit everything at once." | One giant commit can't be bisected or reverted. Commit per slice. |
| "`git add -A` is fine." | It sweeps in unrelated changes. Stage deliberately. |
| "Skip the flag, it's faster." | Un-flagged risky changes can't ship dark or roll back. Flag it. |

## Red Flags

- Many files changed with no test added.
- You're committing on a red build/test run.
- One commit spans several unrelated slices.
- No clean baseline was established before starting.
- A completed task checkbox substitutes for tracer/integration proof.

## Verification

- Each slice is a separate commit touching only its files.
- Every slice added/updated a test and left the suite green.
- The build passes at each commit.
- Risky slices are behind a flag or have a stated rollback.
- Tracers/phases have current outcome evidence; interrupted work resumes from
  reconciled artifacts without granting new scope or resetting retries.
