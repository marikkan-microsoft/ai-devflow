---
name: compound-learnings
description: Captures a solved problem or durable decision as a searchable note so the next occurrence takes minutes, not hours. Use after solving something non-obvious, fixing a tricky bug, or making a decision worth reusing.
---

# Compound Learnings

## Overview

This is the return arrow that makes the loop **compound**: after you solve
something non-obvious, you write it down so the next `align-and-grill`,
`plan-in-phases`, and `research-codebase` start from that knowledge instead of
rediscovering it. The first time a problem is solved costs research; documented,
the second occurrence costs minutes. Knowledge that isn't captured is paid for
again and again.

## When to Use

- After fixing a tricky bug or solving a non-obvious problem.
- After a decision or pattern worth reusing emerges.
- At the end of `fix-workflow`/`feature-workflow`, before you move on.

**When NOT to use:** Trivial, obvious work with nothing reusable to teach. Don't
manufacture learnings for busywork.

**Related:** Writes `docs/devflow/solutions/*.md`
([template](../../templates/solution.md)); durable decisions become ADRs via
`domain-modeling`. Read as grounding by the Align, Plan, and Research skills.

## Process

### 1. One learning per note

Scope each note to a single solved problem or decision. If a session produced
several, write several notes — don't stitch them together.

### 2. Ground against what's already captured

Skim existing `solutions/` first. If this extends or corrects an existing note,
update that one rather than adding a near-duplicate.

### 3. Write it to be found later

Use the [solution template](../../templates/solution.md). Capture:

- **Symptom** — what was observed (exact error/behavior).
- **Root cause** — the underlying cause, with `file:line`.
- **Fix** — what changed and why it works (link the commit/PR).
- **How to recognize it next time** — the tell-tale signs.
- **Guardrail** — the test/lint/assertion that stops a silent regression.

Give it searchable frontmatter (title, slug, date, tags, severity).

### 4. Make it discoverable

Add the tags future-you would search. Cross-link related `solutions/` and ADRs so
the knowledge base connects rather than fragments.

### 5. Close the loop

The note is the payoff of the work. Confirm it's written before considering the
task fully done.

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "I'll remember how I fixed this." | You won't, and the next agent can't. Write it. |
| "It's not worth documenting." | If it took real effort to solve, it'll recur. Capture it. |
| "I'll batch all today's learnings into one note." | Batched notes don't surface on search. One per learning. |
| "No time to document." | Re-solving it next month costs far more. Minutes now. |

## Red Flags

- A hard problem was solved and nobody wrote it down.
- A note describes the symptom but not the root cause or guardrail.
- Multiple distinct learnings crammed into one entry.
- The note has no tags and won't be found by search.

## Verification

- A `solutions/*.md` note exists (or an existing one was updated) with root cause,
  fix, recognition signs, and a guardrail.
- It has searchable frontmatter/tags and links to related notes/ADRs.
- Durable decisions were also recorded as ADRs where appropriate.
