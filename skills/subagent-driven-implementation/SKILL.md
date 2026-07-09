---
name: subagent-driven-implementation
description: Executes a plan by dispatching a fresh subagent per task with a two-stage review (spec compliance, then code quality). Use when implementing an approved multi-task plan and you want isolated, reviewed, autonomous progress.
---

# Subagent-Driven Implementation

## Overview

Long implementations degrade when one agent carries the whole plan in a
ballooning context. This skill executes the plan by dispatching a **fresh subagent
per task** with a clean context, then gates each result through a **two-stage
review** — first "does it satisfy the spec/task?", then "is the code good?". Fresh
context per task keeps quality high; the two-stage gate keeps drift out.

## When to Use

- Executing an `approved` `plan.md` with multiple tasks.
- Work large enough that a single context would degrade partway through.
- You want the agent to run for a long stretch without losing the plan.

**When NOT to use:** A single small task (use `incremental-implementation` +
`test-driven-development` directly), or when subagents aren't available in the
harness — fall back to `incremental-implementation`.

**Related:** Consumes `plan.md` + `research.md`. Each task runs
`test-driven-development`. Review stages use the `spec-auditor` and `code-reviewer`
personas. Ends at `verify-before-done`.

## Process

### 1. Establish a clean baseline

Confirm a clean git state (or a dedicated worktree/branch — see
`incremental-implementation` for the worktree pattern) and a green test baseline
before the first task. A per-task commit history is only a clean rollback if the
baseline was clean.

### 2. For each task, dispatch a fresh subagent

Give the subagent only what it needs: the single task (files, acceptance
criteria, satisfied `R#`), the relevant slice of `research.md`, and `CONTEXT.md`.
Instruct it to follow `test-driven-development` — RED, GREEN, refactor — and stop
at the task boundary. A subagent does **not** spawn further subagents.

### 3. Stage one — spec compliance (`spec-auditor`)

Review the task's diff against its acceptance criteria and the spec requirement
only: does it do what was asked, nothing missing, nothing extra? Bounce it back
if not. Keep this axis uncontaminated by style opinions.

### 4. Stage two — code quality (`code-reviewer`)

Only after spec compliance passes, review the diff for correctness, readability,
architecture, security, and performance. Critical findings block; fix before
proceeding.

### 5. Commit the slice

Stage **only** the files this task touched plus its plan-status update — never
`git add -A`. Commit with a descriptive message. One commit per task so any point
is a clean rollback. Mark the task done in `plan.md`.

### 6. Advance in dependency order

Move to the next task whose dependencies are satisfied. Stop and ask the user on
an unfixable failure, spec ambiguity, or a high-risk/irreversible task.

### 7. Finish

When all tasks are done, run `verify-before-done` across the whole change, then
route to `review-code`.

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "One context for the whole plan is simpler." | It degrades and drifts. Fresh context per task. |
| "Spec and quality review can be one pass." | They contaminate each other. Two stages, in order. |
| "I'll `git add -A` to save time." | It absorbs unrelated work and breaks rollback. Stage per task. |
| "This task can skip the test." | Then it can't be reviewed against acceptance. Test first. |

## Red Flags

- The same context has executed many tasks and is getting confused.
- A task was committed without passing both review stages.
- Commits bundle multiple tasks or unrelated files.
- A subagent spawned its own subagents.

## Verification

- Every task has its own commit touching only its files.
- Each task passed spec-compliance **and** code-quality review before commit.
- `plan.md` task statuses reflect reality.
- `verify-before-done` passed for the whole change before review.
