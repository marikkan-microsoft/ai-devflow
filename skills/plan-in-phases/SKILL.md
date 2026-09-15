---
name: plan-in-phases
description: Decomposes a spec and research into small, verifiable, dependency-ordered tasks with acceptance criteria. Use after a spec exists and before implementation, to produce a durable phased plan.
---

# Plan in Phases

## Overview

A good plan makes execution small. This skill turns `spec.md` + `research.md` into
a durable `plan.md`: phases of **thin vertical-slice tasks**, each with explicit
acceptance criteria, the spec requirement it satisfies, and its dependencies —
clear enough for an enthusiastic junior engineer (or a fresh subagent) to execute
without judgment calls. The plan is a rewindable checkpoint.

## When to Use

- After `write-spec` (status `approved`) and any needed `research-codebase`.
- Before `subagent-driven-implementation` / `incremental-implementation`.
- When a change is big enough that "just start coding" would sprawl.

**When NOT to use:** A single-slice change already covered by one task, or a bug
fix (use `fix-workflow`). Don't plan a plan.

**Related:** Consumes `spec.md` + `research.md`; produces `plan.md`
([template](../../templates/plan.md)), which `analyze-artifacts` audits before the
build skills and `verify-before-done`.

## Process

### 1. Locate the artifact

Write `docs/devflow/<slug>/plan.md` from the
[plan template](../../templates/plan.md).

### 2. Choose the seams

State the approach: which module boundaries you'll build along and in what order.
Prefer an order where each step leaves the system working (tracer-bullet slices),
not a big-bang integration at the end.

Work backward from the approved outcome through artifacts, critical connections,
and proof using [execution checkpoints](../../references/execution-checkpoints.md#plan-from-the-outcome).
For an unproven boundary, plan a real end-to-end tracer before expansion; record
why it is unnecessary when the path is already proven. Put the riskiest unknown
integration early without violating dependencies.

### 3. Decompose into tasks

Break work into tasks that are:

- **Thin vertical slices** — each delivers a testable behavior end to end.
- **Small** — implementable, testable, and committable on their own (minutes to
  an hour, not days).
- **Specified** — each task names its `Files`, the requirement(s) it `Satisfies`
  (`R#`/`SC#`), its `Acceptance` (the test that proves it), and `Depends on`.

Include bounded read-first references, delivered interfaces, exact verification,
and read-only external prerequisites where needed. Honor locked decisions and
delegated choices from the spec/ADRs; do not turn research options into scope.

### 4. Order by dependency

Sequence tasks so every task's dependencies come first. Make the dependency graph
explicit; the build skill executes in that order.

Check for missing dependencies, cycles, and shared mutable state. Record
producer/consumer contracts; only verified prerequisites release dependents.
Default to serial work unless file ownership and state independence are clear.

### 5. Plan verification and rollback

Add a verification plan that maps to the spec's success criteria, and note the
highest-risk tasks with their rollback (feature flag, `git revert`, migration
reversal).

Map `R#`/`SC#` to owning tasks and evidence in the template's coverage table.
Plan phase demos, cross-phase integration, required human acceptance, and
reassessment after each tracer/phase. Optional execution notes preserve progress;
existing small plans do not need additional artifacts.

### 6. Approve

Present the plan. On explicit approval, set status `approved` — the gate to build.
If you generated it autonomously, commit it as its own preparatory commit so it
doesn't bleed into task commits. Then hand off to `analyze-artifacts` to audit
coverage and consistency against the spec before the build begins.

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "I'll figure out the steps as I go." | Unplanned work sprawls and misses criteria. Decompose first. |
| "Big tasks are fine." | Big tasks can't be reviewed or rolled back cleanly. Slice thin. |
| "Acceptance criteria are obvious." | If obvious, writing them costs nothing and guides the build. |
| "Ordering doesn't matter." | Wrong order forces rework and broken intermediate states. |

## Red Flags

- Tasks are horizontal layers ("write all the models") instead of vertical slices.
- A task has no acceptance criteria or doesn't map to a requirement.
- The plan has no dependency order.
- No rollback story for risky tasks.
- A tracer can fail while expansion proceeds, or a summary counts as proof.

## Verification

- `docs/devflow/<slug>/plan.md` exists and follows the template.
- Every task has files, acceptance criteria, and a satisfied `R#`/`SC#`.
- Tasks are dependency-ordered and independently committable.
- A verification plan maps to the spec's success criteria.
- Critical connections, dependency contracts, and phase closure evidence are
  explicit wherever the work crosses an unproven boundary.
- The user approved the plan before implementation.
