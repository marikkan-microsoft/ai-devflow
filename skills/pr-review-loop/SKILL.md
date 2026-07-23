---
name: pr-review-loop
description: Works through PR review items one at a time through an isolated, reviewed pipeline — understand → implement (fresh subagent + two-stage review) → re-verify → approve → commit → reply. Use when a PR has many or risky review threads, or a review-items file must be processed one-by-one with per-item user approval, and you want each fix isolated and reviewed before it lands.
---

# PR Review Loop

## Overview

Some reviews can't be swept in one pass — the threads are numerous, risky, or
contested, and batching them hides defects and skips consent. This skill runs
each review item through an **isolated, reviewed pipeline**: understand at root
cause → implement in a fresh subagent that reviews before returning → re-verify →
get the user's explicit approval → commit → reply on the thread. **One item at a
time.** The reviewer, never this skill, resolves the thread.

**Core principle:** every item is understood before it's implemented, reviewed
before the user sees it, and approved before it's committed — and the fix isolation
+ code review come from `subagent-driven-implementation`'s fresh-subagent + two-stage
gate, not from a separate review or planning pass.

## When to Use

- A PR has **many** unresolved review threads, or **risky/contested** ones, where a
  single batched pass would drop or muddle items.
- A review-items file (`review.md`, collected comments) must be worked one-by-one
  with a validation-and-approval gate on each.
- You want each fix isolated in its own context and reviewed *before* it's shown,
  with a per-item commit that maps to a thread.

**When NOT to use:** A short, low-risk comment list — use `resolve-pr-feedback` (the
lightweight systematic pass, `/df-pr`). A single trivial comment — just address it.
Tightly-coupled items that must land as one atomic change — address them together.

**Related:** Extends `resolve-pr-feedback`'s reply-honestly / resolve-honestly
discipline with per-item isolation. Each item's fix runs through
`subagent-driven-implementation` (fresh subagent + `spec-auditor`→`code-reviewer`
two-stage review) using `test-driven-development`; understanding uses
`debug-root-cause` / `research-codebase`; the change is re-gated by
`verify-before-done`; commits follow `git-workflow`; capture reusable fixes with
`compound-learnings`.

## Process

```
gather items (PR threads and/or review file)  →  one todo per item (verbatim text + thread id)
for each item, in order, never batched:
  understand (read-only)  →  valid? ──no──▶ ask user: skip (reply why) or override
        │yes
  implement one item  =  subagent-driven-implementation (fresh subagent,
                          TDD fix, spec-auditor then code-reviewer)   ◀── loop until it passes review
  re-verify (verify-before-done)  →  show diff + review verdict  →  ask user "approve?"
        │approved
  commit (git-workflow, one per item)  →  reply on thread (never resolve)  →  next item
final summary: addressed (+commit+reply), skipped (+why), threads left for the reviewer
```

### 1. Gather and enumerate items

Pull items from the **active PR** and/or a **review file**. For a PR, list
unresolved threads verbatim (keep each thread `id`, `path`, and text):

```bash
gh api graphql -f query='
query($owner:String!,$repo:String!,$pr:Int!){
  repository(owner:$owner,name:$repo){ pullRequest(number:$pr){
    reviewThreads(first:100){ nodes{ id isResolved path
      comments(first:20){ nodes{ author{login} body } } } } } } }' \
  -F owner=OWNER -F repo=REPO -F pr=NUMBER
```

Take threads where `isResolved` is `false`. From a review file, extract each item
verbatim. Create **one todo per item** (order by file for coherence — ordering is
readability, **not** batching) and confirm the count with the user.

### 2. Understand the item at root cause (read-only)

Before touching code, understand what the reviewer is protecting. For a
bug/behavior comment use `debug-root-cause` (reproduce first); to map control flow
use `research-codebase`. Decide: does this warrant a change, or is it a nitpick /
false positive? This is read-only — no edits yet.

### 3. Validate with the user

If the item does **not** warrant a change, report the reasoning and ask: skip
(reply on the thread explaining why, leave it open) or override and implement
anyway. If it warrants a change, proceed. Don't silently ignore, and don't
implement an item you judged invalid without the user's say-so.

### 4. Implement the item in isolation

Run **this one item** through `subagent-driven-implementation`: dispatch a fresh
subagent with only this item's text, the understanding from step 2, and
`CONTEXT.md`; it fixes test-first (`test-driven-development`) and passes the
**two-stage review** — `spec-auditor` (does it address the comment, nothing extra)
then `code-reviewer` (correctness, readability, security, performance) — looping
until both pass. This is where the review happens; do not skip it as "trivial."

### 5. Re-verify the whole change

Run `verify-before-done` — a per-item fix can regress the rest. Full suite + build
green is the evidence, not vibes.

### 6. Get explicit approval

Show the user: a one-line summary of what changed, the review verdict + any
remaining nits, and the diff. Ask "Approve this item? (yes / feedback)." On
feedback, re-dispatch step 4, re-verify, re-ask. Never commit without an explicit
"yes" for *this* item.

### 7. Commit — one per item

Only after approval, commit via `git-workflow`: stage only this item's files, one
focused commit whose message references the review item/thread. Never
`--no-verify`.

### 8. Reply on the thread — never resolve

If the item came from a live PR, reply with what changed (reference the commit),
or why no change was made for a skipped item. **Do not resolve the thread** —
resolution is the reviewer's decision (per `resolve-pr-feedback`). Resolve only if
the user explicitly asks.

```bash
gh api graphql -f query='mutation($t:ID!,$b:String!){addPullRequestReviewThreadReply(input:{pullRequestReviewThreadId:$t,body:$b}){comment{id}}}' -f t="<threadId>" -f b="<reply>"
```

For a review-file item, flip its checkbox (`- [ ]` → `- [x]`) so the artifact
reflects reality.

### 9. Mark the todo done, move to the next item

Then a final summary: items addressed (with commit + that a reply was posted),
items skipped (with reasoning), and the list of threads left **open for the
reviewer** to verify and resolve, plus any follow-up questions.

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "These threads are in the same file, I'll batch them." | Same file ≠ same change. Order, don't batch. One item at a time. |
| "The item is obviously valid, skip understanding." | Understanding is cheap and catches nitpicks/false positives. Always do step 2. |
| "The diff is tiny, skip the review." | The two-stage review is the contract, even for trivial fixes. Route through `subagent-driven-implementation`. |
| "I'll re-use the reviewer/context from the last item." | Fresh context per item keeps quality high. New subagent each item. |
| "I addressed items, no need to re-verify." | Fixes regress. Re-run `verify-before-done` across the whole change. |
| "I'll tidy up by resolving the threads I fixed." | Resolution is the reviewer's call. Reply — never auto-resolve. |
| "I'll commit now, they'll see it next message." | Approval = explicit 'yes' before the commit. No pre-commits. |
| "This whole list is small — full pipeline is overkill." | Then this isn't the skill — use `resolve-pr-feedback`. |

## Red Flags

- About to implement or review two items together, or in one context.
- About to edit code before understanding the item (step 2) or before the user
  validated a questionable one (step 3).
- About to skip the fresh-subagent + two-stage review by fixing an item "directly."
- About to `git commit` without an explicit "yes" for that item, or `git add -A`
  sweeping unrelated files.
- About to resolve a PR thread this skill fixed — it replies but never resolves.
- Moving to item N+1 before N is committed and its thread replied to.

## Verification

- Each item has its **own** commit touching only its files, referencing the thread.
- Each item was understood, passed the two-stage review inside
  `subagent-driven-implementation`, and had explicit user approval before its commit.
- `verify-before-done` is green across the whole change; CI passing.
- Every addressed thread has a reply; skipped items have a "why" reply; **no thread
  was auto-resolved** — the final summary lists threads left for the reviewer.
