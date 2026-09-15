---
name: research-codebase
description: Documents how the existing system works before changing it, with exact file:line references, into a durable research artifact. Use for any brownfield change, before planning, or when you need to understand current behavior.
---

# Research Codebase

## Overview

Context-driven development means building understanding **before** writing code.
This skill investigates how the system works *today* in the area a change touches
and writes it down as a durable `research.md` — facts with exact `file:line`
references, not plans. Planning and implementation then build on documented
understanding instead of rediscovering it (and hallucinating).

## When to Use

- Any change to existing (brownfield) code.
- Before `plan-in-phases`, whenever the current behavior isn't already understood.
- Debugging that requires mapping control flow.
- Onboarding to an unfamiliar area.

**When NOT to use:** Pure greenfield with no existing code to understand, or a
change so localized the relevant code fits in one screen you've already read.

**Related:** Consumes `spec.md`; produces `research.md`
([template](../../templates/research.md)) for `plan-in-phases` and
`subagent-driven-implementation`. Pair with `source-grounded-research` for
framework/library facts.

## Process

### 1. Locate the artifact

Write to `docs/devflow/<slug>/research.md` using the
[research template](../../templates/research.md).

### 2. Map the territory

Identify the components involved and record each with its path and responsibility.
Trace the **current control flow** the change will touch, citing exact
`file:line`. A small diagram beats paragraphs.

### 3. Capture contracts and invariants

Document the data shapes, types, API surfaces, events, and invariants the change
must preserve. These are the constraints the plan must respect.

For cross-boundary work, fill the template's boundary map: producer/consumer,
current interface, unproven assumption, and read-only prerequisite. Prioritize a
bounded spike where an unknown could invalidate the approach. If cardinality,
optionality, or who chooses a value changed, route the domain assumption through
`domain-modeling` rather than preserving an obsolete model by accident.

### 4. Find integration points and prior art

Note what calls this code and what it calls, external dependencies, and feature
flags. Search `docs/devflow/solutions/` and `adr/` for prior art worth reusing.

### 5. Name the unknowns

List constraints, risks, and anything that needs a spike to answer. Don't guess —
mark it as unknown so planning accounts for it.

Classify planning inputs as constraints, assumptions, options, or deferred ideas.
Link locked decisions and conflicts explicitly. Research informs the approved
spec; it does not grant new scope (see
[execution checkpoints](../../references/execution-checkpoints.md#plan-from-the-outcome)).

### 6. Verify claims against the code

Every non-trivial claim must be backed by a real `file:line` you actually read.
No inferred behavior stated as fact.

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "I roughly know how this works." | Roughly is how regressions happen. Read and cite it. |
| "Reading first is slow." | Rediscovering mid-implementation is slower and buggier. |
| "I'll figure out the contracts as I code." | Broken invariants surface in production. Capture them now. |
| "I'll cite it later." | Uncited claims are guesses. Cite as you go. |

## Red Flags

- `research.md` describes behavior with no `file:line` references.
- You're planning changes to code you haven't opened.
- Stated invariants are assumptions, not observations.
- Known unknowns are silently omitted.

## Verification

- `docs/devflow/<slug>/research.md` exists and follows the template.
- Every behavioral claim cites a real `file:line`.
- Contracts/invariants to preserve are explicit.
- Unknowns and risks are listed, not hidden.
- Unproven boundaries and prerequisites are explicit; options are not presented
  as approved obligations.
