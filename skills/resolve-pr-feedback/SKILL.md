---
name: resolve-pr-feedback
description: Works through pull-request review comments systematically, addressing or responding to each and re-verifying. Use when a PR has review feedback (human or automated) to resolve before merge.
---

# Resolve PR Feedback

## Overview

Review comments are a to-do list with context, not a nuisance. This skill works
through PR feedback systematically — understand each comment, address it or
respond with reasoning, re-verify, and reply — so threads close on evidence and
nothing is silently dropped. It's how the PR-integrated loop stays honest.

## When to Use

- A PR has review comments (from a human reviewer or an automated one).
- After `review-code` produced structured findings on a PR.

**When NOT to use:** No outstanding feedback. Don't re-litigate resolved threads.

**Related:** Consumes findings from `review-code`; fixes go through
`test-driven-development` + `verify-before-done`; merge via `ship-it`.

## Process

### 1. Collect and triage every comment

Gather all comments into a checklist. Triage by severity (blocking vs
suggestion). Don't cherry-pick the easy ones — every thread gets a resolution.

### 2. Understand before changing

For each comment, understand what the reviewer is protecting. If it's ambiguous,
ask rather than guess. If you disagree, that's a conversation, not a silent
ignore.

### 3. Address with evidence

Fix accepted comments test-first (`test-driven-development`), one focused commit
per concern (or per thread). For anything behavioral, add/adjust a test so the
fix is proven.

### 4. Respond to each thread

Reply to every comment: what you changed (link the commit) or why you didn't (the
reasoning). A reviewer should never have to wonder whether a comment was seen.

### 5. Re-verify the whole change

After addressing feedback, re-run `verify-before-done` — fixes can introduce
regressions. Push, and let CI re-run.

### 6. Resolve threads honestly

Mark threads resolved only when actually addressed or explicitly agreed. Leave
open anything still in discussion.

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "I'll fix the easy comments and merge." | Dropped comments erode trust and hide defects. Resolve all. |
| "I disagree, so I'll just ignore it." | Silent disagreement festers. Reply with reasoning. |
| "Small fix, no test needed." | Behavioral fixes need proof. Test it. |
| "I addressed comments, no need to re-verify." | Fixes regress. Re-run the full gate. |

## Red Flags

- Comments were addressed in code but never replied to.
- Threads marked resolved that weren't actually fixed.
- Fixes landed with no test and no re-verification.
- Disagreements were ignored rather than discussed.

## Verification

- Every comment is addressed or answered with reasoning; each thread has a reply.
- Behavioral fixes have tests; commits are focused per concern.
- `verify-before-done` re-run green after the changes; CI passing.
- Only genuinely-resolved threads are marked resolved.
