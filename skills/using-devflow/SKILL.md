---
name: using-devflow
description: Establishes how to find and use Devflow skills. Use at the start of any task — before writing code, exploring the codebase, or asking clarifying questions — to route the work to the right skill and phase.
---

# Using Devflow

## Overview

Devflow is a compounding development loop. This router runs first on any task: it
decides which **on-ramp** the work belongs to, routes you to the right **skill**,
and enforces the operating rules that make the loop work. If there is even a 1%
chance a skill applies, you must invoke it before doing anything else — including
clarifying questions and codebase exploration.

## When to Use

- At the start of every conversation or task.
- Whenever you're unsure which skill or phase applies.
- After a compaction or handoff, to re-orient.

**When NOT to use:** If you were dispatched as a subagent to execute one specific
task, ignore this router and do that task.

**Related:** Every other skill. This is the map; they are the territory.

## Process

### 1. Read the accumulated context

Before deciding anything, load what past runs already learned:

- If `docs/devflow/CONTEXT.md` exists, read it — use its vocabulary.
- Skim `docs/devflow/solutions/` for entries relevant to this task.
- If an in-progress unit of work exists under `docs/devflow/<slug>/`, resume it.

### 2. Pick the on-ramp

```
Is the input a broken behavior (bug, regression, failure)?
        │
   ┌────┴─────┐
  yes         no
   │           │
   ▼           ▼
fix-workflow   Is it a clear, small change with an obvious approach?
(/df-fix)         │
              ┌───┴────┐
             yes        no
              │          │
              ▼          ▼
        single skill   feature-workflow (/df-feature)
        (e.g. tdd)     full path: align → spec → research → plan → build …
```

- **Broken behavior** → `fix-workflow` (or `debug-root-cause` directly).
- **New feature / non-trivial change** → `feature-workflow`.
- **Small, well-understood change** → go straight to the matching phase skill
  (e.g. `test-driven-development`, `simplify-code`), then `verify-before-done`.
- **Vague idea** → `idea-refine` first.

### 3. Route by intent

Use the intent → skill table in [AGENTS.md](../../AGENTS.md#intent--skill-mapping).
Announce the routing: *"Using `<skill>` to `<purpose>`."* Then follow that skill
exactly; if it has a checklist, create a to-do per item.

### 4. Respect the layers

- **Skills** are the *how* — invoke them, don't improvise their steps.
- **Personas** (`agents/`) are the *who* — a perspective + output format.
- **Commands** (`/df-*`) are the *when* — the orchestration layer.

The user or a slash command orchestrates. A persona never invokes another
persona; a user-invoked skill never invokes another user-invoked skill.

### 5. Close the loop

When the work resolves something non-obvious, invoke `compound-learnings` so the
next run starts smarter. That return arrow is the point of the whole system.

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "This is just a simple question." | Questions are tasks. Route it first. |
| "I need more context before choosing a skill." | The skill tells you how to get context. Route first. |
| "Let me explore the codebase, then decide." | `research-codebase` *is* how you explore. Route first. |
| "No skill really fits, I'll just do it." | Then pick the closest phase skill and follow it. Freelancing is the failure mode Devflow exists to prevent. |
| "I'll skip compounding, I'll remember this." | You won't, and the next agent can't. Write the solution note. |

## Red Flags

- You started editing files without announcing a skill.
- You asked the user a clarifying question before checking for a skill.
- You're about to implement a feature with no `spec.md`.
- You're fixing a bug without a failing test that reproduces it.
- You solved something tricky and are about to move on without compounding it.

## Verification

- You named the on-ramp and the skill you routed to before acting.
- The chosen skill's own Verification section is satisfied before you call the
  task done.
