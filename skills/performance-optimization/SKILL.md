---
name: performance-optimization
description: Improves performance with a measure-first workflow against explicit targets. Use when performance requirements exist, a regression is suspected, or before optimizing — so you profile before you change anything.
---

# Performance Optimization

## Overview

Optimizing without measuring is guessing, and guesses make code worse for no gain.
This skill enforces a **measure-first** workflow: define the target, profile to
find the real bottleneck, fix that bottleneck, then measure again to prove the
win. It targets the metric that matters (often Core Web Vitals on the web) rather
than micro-optimizing what feels slow.

## When to Use

- A performance requirement or budget exists.
- A regression is suspected or reported.
- Before optimizing anything (to avoid optimizing the wrong thing).

**When NOT to use:** No evidence or requirement of a performance problem —
premature optimization adds complexity for nothing.

**Related:** Uses `browser-verification` for web runtime metrics; feeds the
`performance-auditor` persona. Targets/checklist in
[references/definition-of-done.md](../../references/definition-of-done.md).

## Process

### 1. Set the target

Define the metric and the number to beat before touching code: e.g. LCP < 2.5s, a
p95 latency, a memory ceiling, a throughput. Optimization without a target has no
finish line.

### 2. Measure the baseline

Profile under realistic conditions and capture the baseline. Identify the **actual**
bottleneck from data (profiler, traces, Core Web Vitals, query logs) — not
intuition.

### 3. Fix the biggest bottleneck first

Address the dominant cost, then re-measure. Common real culprits: N+1 queries,
unbounded/unpaginated fetches, sync work that should be async, missing
indexes/caching, oversized bundles, unnecessary re-renders.

### 4. Prove the win

Measure again the same way. Keep the change only if the target metric actually
improved and nothing regressed functionally (full test suite green). Discard
changes that add complexity without measured benefit.

### 5. Guard against regression

Where feasible, add a performance check/budget (bundle-size limit, a benchmark, a
query-count assertion) so the win doesn't silently erode.

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "This looks slow, I'll optimize it." | Feelings mislead. Profile; fix what the data shows. |
| "No need to measure, the fix is obvious." | Unmeasured wins are often losses. Baseline first. |
| "Micro-optimize everything." | It adds complexity for noise. Target the dominant cost. |
| "It's faster on my machine." | Measure under realistic conditions, then compare. |

## Red Flags

- Code was optimized with no profile or baseline.
- There's no numeric target to hit.
- Complexity increased with no measured improvement.
- Micro-optimizations were made while the real bottleneck was untouched.

## Verification

- A numeric target existed before the change.
- Baseline and post-change measurements were taken the same way.
- The target metric improved; the full suite still passes.
- A regression guard/budget was added where feasible.
