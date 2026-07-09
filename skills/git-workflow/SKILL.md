---
name: git-workflow
description: Keeps version control clean with trunk-based development and atomic, well-scoped commits. Use for any code change — to commit in small, revertible units with clear messages and deliberate staging.
---

# Git Workflow

## Overview

Version control is the safety net that makes bold changes safe. This skill keeps
that net intact: **atomic commits** (one logical change each), **deliberate
staging** (never blind `git add -A`), clear messages, and **trunk-based**
short-lived branches. Every commit is a save point you can bisect to and revert
cleanly.

## When to Use

- Any code change (this is the always-on discipline).
- Committing a slice/task during implementation.
- Structuring branches for a change.

**When NOT to use:** Nothing to commit. (There's no reason to skip this on real
changes.)

**Related:** Underlies `incremental-implementation` and
`subagent-driven-implementation` (commit per slice/task). Precedes `ship-it`.

## Process

### 1. Work on a short-lived branch

Branch off trunk for the change; keep it small and merge back quickly to avoid
long-lived divergence. Use a worktree when isolating parallel work.

### 2. Stage deliberately

Stage **only** the files that belong to this logical change. Never `git add -A`
blindly — it sweeps in unrelated edits and destroys the atomicity (and the clean
rollback) of the commit. Review the diff you're about to commit.

### 3. Commit atomically

One commit = one logical, self-consistent change that leaves the tree building.
Keep changes small (~a few hundred lines is a soft ceiling); split larger work.

### 4. Write a clear message

Imperative subject that says *what and why* ("Fix duplicate invoice on webhook
replay"), not *how*. Add a body when the reasoning isn't obvious. Reference the
issue/spec.

### 5. Keep it a clean rollback boundary

Because each commit is atomic and staged deliberately, any commit is a safe
`git revert` point. Preserve that guarantee — don't bundle unrelated work.

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "`git add -A` is faster." | It bundles unrelated changes and breaks rollback. Stage deliberately. |
| "I'll squash it all into one big commit." | Giant commits can't be bisected or reverted cleanly. Keep them atomic. |
| "The message can just be 'fix'." | Future-you needs the why. Write it. |
| "Long-lived branch is fine." | It drifts and merges painfully. Short-lived, trunk-based. |

## Red Flags

- Commits bundle unrelated changes or leave the build broken.
- `git add -A` / `git commit -am` used without reviewing the diff.
- Commit messages don't explain the change.
- A branch has lived for weeks without merging.

## Verification

- Each commit is atomic, builds, and touches only related files.
- Staging was deliberate (diff reviewed), not blanket.
- Messages state what and why and reference the spec/issue.
- Any commit is a clean `git revert` boundary.
