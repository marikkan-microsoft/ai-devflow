---
name: idea-refine
description: Turns a vague concept into concrete, ranked proposals through structured divergent then convergent thinking. Use when the user has a rough idea, doesn't yet know what to build, or asks to brainstorm or explore options.
---

# Idea Refine

## Overview

Before you can align on requirements, the idea itself sometimes needs shaping.
This skill runs a disciplined **diverge → converge** loop: generate a breadth of
grounded options, then critically narrow to the strongest one, and route it into
`align-and-grill`. It prevents both premature commitment and endless wandering.

## When to Use

- The user has a fuzzy concept ("something to make onboarding better").
- "Brainstorm", "explore options", "surprise me", "what could we build".
- You have a goal but multiple plausible directions.

**When NOT to use:** The direction is already clear — skip straight to
`align-and-grill` / `write-spec`. Don't manufacture options for a decided change.

**Related:** Precedes `align-and-grill`. Grounds itself in
`docs/devflow/solutions/` and `CONTEXT.md`.

## Process

### 1. Ground

Do the homework first: skim the codebase area, past `solutions/`, and — if it
helps — the user's issue tracker. Note real constraints so options are grounded,
not fantasy.

### 2. Diverge

Generate 5–8 distinct options. Push for genuine variety (different mechanisms,
scopes, and risk levels), not variations on one theme. Withhold judgment here.

### 3. Converge — rank critically

Score each option against explicit criteria: user value, effort, risk,
reversibility, and fit with current architecture. Be honest about weaknesses.
Present a ranked shortlist (top 3) with a one-line rationale each.

### 4. Recommend and route

State your single recommended direction and why. On the user's pick, hand off to
`align-and-grill` (to interrogate it) or, if it's exploratory/uncertain, propose
a `prototype`-style spike.

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "First idea is good enough." | Diverging costs minutes and routinely finds better. Generate options. |
| "More options is always better." | Divergence without convergence is paralysis. Rank and recommend. |
| "I'll rank without grounding." | Ungrounded options waste everyone's time. Do the homework first. |

## Red Flags

- You offered one option and called it a brainstorm.
- Your options are near-duplicates of each other.
- You presented a list with no recommendation.
- The options ignore known constraints from `CONTEXT.md` / the codebase.

## Verification

- A ranked shortlist (with rationale) and one clear recommendation exist.
- The recommendation is grounded in real constraints, not assumptions.
- The user picked a direction and it was routed to the next skill.
