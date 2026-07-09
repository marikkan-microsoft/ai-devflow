---
name: domain-modeling
description: Builds and sharpens the project's shared language (domain model) and records architectural decisions. Use when new domain terms surface, naming feels inconsistent, or an architectural decision needs capturing in CONTEXT.md and ADRs.
---

# Domain Modeling

## Overview

When agent and humans speak different languages, the agent uses twenty words
where one would do, names things inconsistently, and drifts from the domain. This
skill builds a **ubiquitous language** in `CONTEXT.md` and captures hard decisions
as ADRs — so code is named consistently, the codebase is navigable, and every
later skill reasons in the project's own vocabulary.

## When to Use

- New domain terms appear during `align-and-grill`, `write-spec`, or `research-codebase`.
- Naming in the code or conversation feels vague or inconsistent.
- A real architectural decision (more than one defensible option) needs recording.
- Onboarding an agent to an unfamiliar codebase's concepts.

**When NOT to use:** No new vocabulary or decisions are involved. Don't invent a
glossary for a trivial change.

**Related:** Writes `docs/devflow/CONTEXT.md`
([template](../../templates/CONTEXT.md)) and `docs/devflow/adr/*.md`
([template](../../templates/adr.md)). Read by every skill.

## Process

### 1. Harvest terms

Collect the domain nouns and verbs in play. For each, write a precise one-line
definition and, where useful, what it is **not** (the adjacent term it's confused
with).

### 2. Challenge and stress-test

Put each term against edge-case scenarios. If two terms overlap, force the
distinction or merge them. Prefer the words users/business actually use over
invented jargon.

### 3. Model deep modules

Describe the main modules as **deep modules** — a lot of capability behind a
small, stable interface — and name the seam each sits behind. Record the small
public surface and the depth it hides.

### 4. Record decisions as ADRs

When a real architectural choice is made, write an ADR (context, decision,
options considered, consequences). Number them sequentially; supersede rather
than rewrite.

### 5. Keep it live

Update `CONTEXT.md` inline as understanding sharpens — this is a living document,
not a one-time deliverable.

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "Everyone knows what that term means." | Then defining it costs one line and prevents drift. Define it. |
| "The code is the documentation." | Code shows *what*, not the agreed *meaning*. Capture the language. |
| "I'll remember why we chose this." | You won't. Write the ADR while the context is fresh. |
| "A glossary is overhead." | Inconsistent naming is bigger overhead. It compounds. |

## Red Flags

- The same concept has three names across the conversation/code.
- A significant decision was made with no ADR.
- Definitions are circular or describe implementation, not meaning.
- `CONTEXT.md` contradicts the current code.

## Verification

- `CONTEXT.md` exists with precise, non-circular definitions for the terms in play.
- Deep modules are described by their small interface + hidden depth.
- Every significant decision has an ADR with options and consequences.
- Naming in new code matches `CONTEXT.md`.
