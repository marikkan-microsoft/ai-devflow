---
name: simplify-code
description: Reduces complexity while preserving exact behavior, guided by Chesterton's Fence. Use after fresh implementation, or on code that keeps slowing changes down, to make it clearer without changing what it does.
---

# Simplify Code

## Overview

Agents accelerate coding — and therefore accelerate entropy. This skill pays that
down: it reduces complexity **while preserving exact behavior**, so the code gets
easier to change without any functional drift. It runs best right after fresh
implementation (before review) and periodically on the files that keep absorbing
unrelated fixes.

## When to Use

- Right after implementing a feature, before `review-code`.
- On a file that keeps slowing changes down or absorbing churn.
- When code works but is harder to read/maintain than it should be.

**When NOT to use:** Behavior isn't settled yet (finish it first), or the code is
already simple. Don't refactor for its own sake.

**Related:** Runs before `review-code`. Preserve-behavior discipline leans on
`test-driven-development` (green throughout). Deep-module ideas from
`domain-modeling`.

## Process

### 1. Establish a behavior safety net

Ensure tests cover the current behavior and are green **before** you touch
anything. Simplification that isn't proven behavior-preserving is just risk.

### 2. Apply Chesterton's Fence

Before removing anything that looks unnecessary, understand **why it's there**. If
you can't explain what it guards, don't remove it yet — investigate. Odd code
often encodes a bug fix or an edge case.

### 3. Reduce, don't rewrite

Prefer the smallest clarifying changes: remove duplication, flatten nesting,
improve names, delete dead code, collapse needless indirection, and hide depth
behind a smaller interface. Keep diffs reviewable.

### 4. Keep the suite green continuously

Run tests after each change. The suite must stay green the entire time — any red
means you changed behavior, which is not simplification.

### 5. Stop at "clearer", not "clever"

The goal is clarity for the next reader, not maximum compression. Stop when it
reads plainly; don't trade readability for cleverness.

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "This code looks useless, delete it." | It may guard an edge case (Chesterton). Understand before removing. |
| "I'll refactor and add tests after." | Then you can't prove behavior held. Net first, then simplify. |
| "A full rewrite is cleaner." | Rewrites reintroduce fixed bugs. Reduce in small steps. |
| "Cleverer is simpler." | Clever is harder to read. Optimize for the next human. |

## Red Flags

- You removed code you couldn't explain the purpose of.
- Tests went red (or didn't exist) during simplification.
- The change became a sprawling rewrite.
- Readability was traded for terseness.

## Verification

- Behavior is identical: the same tests pass before and after.
- Removed code was understood first (Chesterton's Fence).
- Complexity is measurably lower (less nesting/duplication/surface).
- The diff stayed small and reviewable.
