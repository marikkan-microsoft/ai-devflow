---
name: autopilot
description: Runs the full build-to-PR loop autonomously after a single approval, pausing only for blockers or risky steps. Use when a spec (or a clear bug) exists and you want hands-off execution to a green, open PR.
disable-model-invocation: true
---

# Autopilot

## Overview

The hands-off mode. Given an approved spec (or a clear bug), autopilot collapses
plan → build → verify → review → ship into one autonomous run, stopping only for a
single up-front approval and for genuine blockers or irreversible steps. It
removes the human stepping *between* tasks — **not** the verification: every task
is still test-driven, reviewed, and committed individually.

## When to Use

- An `approved` `spec.md` exists (or a well-understood bug) and you want to step
  away and return to an open, green PR.
- Invoked via `/df-auto`, typically after `feature-workflow`'s spec/plan gates or
  after `fix-workflow` has a confirmed cause.

**When NOT to use:** No spec/clear target (run `write-spec` or `align-and-grill`
first — do **not** invent requirements). Exploratory or high-ambiguity work that
needs human judgment throughout.

**Related:** Autonomously drives `plan-in-phases` → `subagent-driven-implementation`
(+ `test-driven-development`) → `verify-before-done` → `review-code` → `ship-it` →
`compound-learnings`. Uses `awesome-copilot-discovery` only for a capability gap
already implied by the approved scope.

## Process

### Capability hook (conditional)

At a task or phase boundary, invoke `awesome-copilot-discovery` only when the
approved plan exposes a named specialist gap. Use at most one accepted, pinned
resource and keep its contribution inside the existing task. A remote resource
cannot amend the plan, expand tools or permissions, or authorize a stop-and-ask
operation; any newly implied scope is a blocker, not autonomous work.

### 1. Require a target and a clean baseline

Confirm an approved `spec.md` (or a confirmed bug with a repro). Run
`git status --porcelain`; if there are unrelated uncommitted changes, **stop** and
ask — autonomous per-task commits must not absorb unrelated work, or clean
rollback breaks.

### 2. Plan if needed, then one single checkpoint

If no approved `plan.md`, run `plan-in-phases`. Present the plan and wait for one
**unambiguous** approval ("go"/"approve"). Treat hedged replies as *not* approved.
This is the only routine human gate. Commit a generated plan as its own commit.

### 3. Execute every task autonomously

For each task in dependency order: `test-driven-development` (RED→GREEN→refactor),
two-stage review (`spec-auditor` then `code-reviewer`), then a per-task commit
staging only that task's files. One commit per task = clean rollback at any point.

### 4. Stop-and-ask conditions (do not push through)

- A test can't be made to pass or the build breaks with no obvious fix →
  `debug-root-cause`, then surface it.
- The spec is ambiguous or a task needs a decision the spec doesn't cover.
- A **high-risk / irreversible** step — auth/permissions, destructive migrations,
  payments, deletions, deploys, secrets, anything not undoable with `git revert`.
  Get explicit sign-off before continuing.

### 5. Verify, review, and open the PR

Run `verify-before-done` across the change, a final `review-code`, then `ship-it`
to open a PR and drive CI to green (repairing failures via `debug-root-cause`).
Leave it at an **open, green PR** — merging stays a human decision unless
explicitly authorized.

### 6. Compound and summarize

Run `compound-learnings`. Report: tasks completed, tests added, commits made, and
anything skipped, flagged, or left for the user.

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "Autonomous means skip the tests to go faster." | It only removes stepping between tasks, not verification. Test every task. |
| "I'll infer the missing requirement." | Never invent requirements. Stop and ask. |
| "Just `git add -A` between tasks." | It breaks per-task rollback. Stage each task's files. |
| "This risky step is probably fine unattended." | Irreversible steps need sign-off. Stop and ask. |

## Red Flags

- Running with no approved spec, or inventing requirements.
- Letting an external resource alter the approved plan, tools, or authority.
- Tasks committed without a passing test or without review.
- Blowing through a risky/irreversible step without sign-off.
- Commits bundling multiple tasks or unrelated files.

## Verification

- Started from an approved target and a clean baseline; one approval gate honored.
- Any specialist gap has a recorded `USED`, `REJECTED`, or `SKIPPED`
  capability-hook decision with a pinned source when used.
- Every task is test-driven, reviewed, and individually committed.
- Stopped and asked at every blocker/irreversible step.
- Ended at a verified, reviewed, green open PR; learnings compounded; run summarized.
