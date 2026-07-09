# Plan: <title>

- **Slug:** <kebab-slug>
- **From:** [spec.md](spec.md) · [research.md](research.md)
- **Status:** draft | approved
- **Date:** <yyyy-mm-dd>

> Right-sized, dependency-ordered tasks. Each task is a **thin vertical slice** an
> agent can implement, test, and commit on its own — small enough to review, big
> enough to be meaningful. Each task names its acceptance criteria and the spec
> requirement(s) it satisfies.

## Approach

Two to four sentences on the strategy: the seams you'll build along, the order,
and why. Note any feature flag or migration strategy.

## Phases & tasks

### Phase 1 — <name>

- [ ] **T1.1 — <task>**
  - **Files:** `src/...`
  - **Satisfies:** R1, SC1
  - **Acceptance:** <observable result; the test that proves it>
  - **Depends on:** —
- [ ] **T1.2 — <task>**
  - **Files:** `...`
  - **Satisfies:** R2
  - **Acceptance:** …
  - **Depends on:** T1.1

### Phase 2 — <name>

- [ ] **T2.1 — <task>** …

## Verification plan

How the whole change is proven at the end (maps to the spec's success criteria):
test suites to run, manual/browser checks, metrics to observe.

## Risks & rollback

Highest-risk tasks, and how to undo the change (feature flag, `git revert`,
migration reversal).
