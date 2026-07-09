---
name: align-and-grill
description: Extracts what the user actually wants through a relentless one-question-at-a-time interview until intent is ~95% clear. Use when a request is underspecified, before writing a spec or code, or when the user says "grill me" / "align" / "interview me".
---

# Align and Grill

## Overview

The most common failure in software is misalignment — building the wrong thing
confidently. This skill closes the gap by interviewing the user **one question at
a time** until you and they share the same picture of the change. It resolves the
decision tree branch by branch before any spec or code exists.

## When to Use

- A request is vague, broad, or has more than one reasonable interpretation.
- Before `write-spec`, to gather the raw material.
- The user asks to be "grilled", "interviewed", or "aligned".
- Stakes are high and building the wrong thing is expensive.

**When NOT to use:** The change is tiny and unambiguous, or a current `spec.md`
already captures the intent. Don't grill for the sake of ceremony.

**Related:** Feeds `write-spec`. Pairs with `domain-modeling` to capture new
vocabulary as it surfaces. `idea-refine` comes *before* this when the idea itself
is still fuzzy.

## Process

### 1. Ground yourself first

Read `docs/devflow/CONTEXT.md` and skim `docs/devflow/solutions/`. **Facts that
can be found by reading code or docs, look up — do not ask the user.** The user's
time is for *decisions*, not lookups.

### 2. Detect the on-ramp

Early, determine and confirm: is this a **greenfield** feature or a **brownfield**
change to existing behavior? It changes which questions matter (brownfield leans
on `research-codebase`; greenfield leans on requirements and boundaries).

### 3. Interview — one question at a time

Ask a single question, provide **your recommended answer**, and wait. Do not
stack questions; multiple questions at once are bewildering and get shallow
answers. Walk the decision tree, resolving dependencies between decisions in
order:

- Problem & who feels it → objective → success criteria (how we'll *prove* it)
- Scope boundaries (what it explicitly won't do)
- Constraints (tech, data, compatibility, security, performance)
- Edge cases and failure modes
- Unknowns that need a spike

Track confidence out loud. Continue until you estimate **~95%** shared
understanding.

### 4. Reflect back

Summarize the resolved decisions in a few short chunks the user can actually
read and confirm. Capture any new domain terms for `CONTEXT.md`.

### 5. Hand off

Offer to run `write-spec` (feature) or route to `debug-root-cause` /
`fix-workflow` (bug). Do not start building from the interview alone.

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "I get the gist, I'll start." | The gist is where wrong-thing-built lives. Reach 95%. |
| "Asking lots at once is faster." | It produces shallow answers and confusion. One at a time. |
| "I'll ask the user this detail." | If code/docs hold the fact, look it up. Ask only for decisions. |
| "Requirements are obvious." | Then confirming costs one question. Confirm. |

## Red Flags

- You asked three questions in one message.
- You're guessing at scope or success criteria instead of confirming them.
- You started drafting a spec or code below 95% confidence.
- You asked the user something the codebase already answers.

## Verification

- A short, confirmed summary of decisions exists, ready to feed `write-spec`.
- Success criteria are stated as *measurable/observable* outcomes.
- New domain terms were noted for `CONTEXT.md`.
- The user explicitly confirmed the shared understanding before you proceeded.
