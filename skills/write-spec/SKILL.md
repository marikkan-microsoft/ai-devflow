---
name: write-spec
description: Writes a durable, measurable specification before any code. Use when starting a new feature or significant change, after aligning on intent, to capture objectives, requirements, success criteria, and boundaries.
---

# Write Spec

## Overview

The spec is the first **durable artifact** and the contract the rest of the loop
is measured against. It states what to build and why, with **measurable success
criteria** and explicit boundaries — clear enough that an implementer with no
prior context could build the right thing. It is a checkpoint you can rewind to.

## When to Use

- Starting any new feature or non-trivial change.
- Right after `align-and-grill` (or when intent is already clear).
- Any time the "what" and "why" aren't written down and agreed.

**When NOT to use:** Pure bug fixes (use `fix-workflow`), or trivial changes where
a spec would be heavier than the change. Documentation-only edits.

**Related:** Consumes output of `align-and-grill`. Produces `spec.md`, consumed by
`plan-in-phases` and by `review-code`'s Spec axis. Template:
[spec.md](../../templates/spec.md).

## Process

### 1. Locate the artifact

Write to `docs/devflow/<slug>/spec.md` using the
[spec template](../../templates/spec.md). Reuse the `<slug>` across the unit of
work.

### 2. Fill it in — synthesize, don't interview

If you just ran `align-and-grill`, synthesize from that conversation; do not
re-interrogate. Capture:

- **Problem** and who feels it.
- **Objective** — one sentence. If you can't, the scope is too big; split it.
- **User stories**, prioritized P1/P2/P3.
- **Requirements** (functional + non-functional), numbered `R1, R2, …`.
- **Success criteria**, numbered `SC1, …`, each **observable and testable**.
- **Out of scope** — what it explicitly won't do.
- **Boundaries & constraints** — tech, data, security, performance budgets.

Keep requirement IDs stable and state consequential invariants/prohibitions.
Where choices matter, record the template's **Decision scope**: locked decisions,
explicitly delegated discretion, and deferred ideas. Link ADRs rather than
duplicating them; later research cannot silently change these boundaries.

### 3. Mark unknowns, don't paper over them

Any unresolved decision gets `[NEEDS CLARIFICATION: …]`. The spec stays `draft`
while any remain — resolve them (ask, or `research-codebase`) before approval.

### 4. Right-size

Match ceremony to the change. A one-day change gets a half-page spec; a
multi-week feature gets the full template. Never pad.

### 5. Get approval

Present the spec in readable chunks. On explicit approval, set status to
`approved`. That approval is the gate to `plan-in-phases`.

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "I'll keep the requirements in my head." | The next phase and the reviewer can't read your head. Write them. |
| "Success is obvious." | If it's obvious, stating it measurably costs nothing. Do it. |
| "I'll resolve the unknown later while coding." | Unknowns resolved in code become rework. Mark and resolve first. |
| "Bigger spec = better." | Padding hides the objective. Right-size it. |

## Red Flags

- The objective needs more than one sentence.
- Success criteria are vague ("works well", "is fast") not measurable.
- Unmarked assumptions are standing in for decisions.
- The spec was written without the user confirming intent.

## Verification

- `docs/devflow/<slug>/spec.md` exists and follows the template.
- Every success criterion is observable/testable.
- No `[NEEDS CLARIFICATION]` markers remain when status is `approved`.
- The user approved it before planning began.
