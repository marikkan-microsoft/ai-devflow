---
name: ship-it
description: Takes a verified, reviewed change to production safely — PR, CI, staged rollout, and monitoring. Use when a change has passed review and is ready to merge and deploy.
---

# Ship It

## Overview

Shipping is a discipline, not a moment. This skill takes a verified, reviewed
change to production with a repeatable path: open a clear PR, get CI green, roll
out behind a flag in stages, and watch the signals — with a rollback ready. Faster
*is* safer when each step is small and reversible.

## When to Use

- A change has passed `verify-before-done` and `review-code` and is ready to merge.
- Preparing a deploy or release.

**When NOT to use:** Unverified or unreviewed work — go back and finish those gates
first. Shipping is the last step, not a shortcut past them.

**Related:** Follows `review-code`; uses `git-workflow` for the merge; PR feedback
goes to `resolve-pr-feedback`. Pre-launch items in
[references/definition-of-done.md](../../references/definition-of-done.md).

## Process

### 1. Open a clear PR

Summarize what changed and why, link the `spec.md`/issue, and note the
verification evidence (tests, runtime checks). A reviewer should understand the
change without spelunking. Teach any new concept the change introduces.

### 2. Get CI green

All checks pass — tests, build, lint, type, security scans. A red pipeline is a
stop, not a suggestion. Fix failures at the root (`debug-root-cause`), don't
bypass gates (`--no-verify`, force-merge).

### 3. Ship dark, then roll out in stages

Prefer merging behind a **feature flag** so deploy ≠ release. Roll out
progressively (internal → small % → full), watching at each step rather than
flipping everything at once.

### 4. Watch the signals

After each stage, monitor errors, key metrics, and logs for regressions. Know your
rollback (flag off, revert, redeploy previous) and be ready to use it fast.

### 5. Confirm and close

Confirm the success criteria hold in production. Close out the PR/issue, and route
any learning to `compound-learnings`.

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "CI is flaky, I'll force-merge." | Bypassing gates ships the break. Fix the pipeline. |
| "Deploy everything at once, it's fine." | No blast-radius control. Flag + staged rollout. |
| "I'll watch it later." | Regressions need catching now. Watch each stage. |
| "Big PR is fine, I'll explain in review." | Oversized PRs hide risk. Keep it small and clear. |

## Red Flags

- Merging with a red or skipped CI.
- No feature flag and no rollback plan for a risky change.
- Nobody is watching metrics after deploy.
- The PR has no verification evidence or context.

## Verification

- CI fully green; no gates bypassed.
- Change is flagged and/or has a stated, tested rollback.
- Rollout was staged and monitored; success criteria hold in production.
- Learnings routed to `compound-learnings`.
