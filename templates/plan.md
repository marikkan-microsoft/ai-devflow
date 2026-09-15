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

## Delivery proof

Work backward from the approved spec. For multi-phase or cross-boundary work,
make the critical connections explicit; omit inapplicable columns for small work.
Link locked decisions and delegated choices from the spec/ADRs, do not redefine
them. Research suggestions and deferred ideas are not approved scope.

| R#/SC# | Observable outcome | Required artifact | Critical connection | Verification |
| --- | --- | --- | --- | --- |
| R1, SC1 | <behavior a user/caller observes> | <real implementation path> | <producer -> consumer> | <command/procedure + expected signal> |

## Dependency contracts

Use only where task ordering alone does not describe the handoff.

| Producer task | Consumer task | Consumes / produces | Contract reference | Prerequisite / integration check |
| --- | --- | --- | --- | --- |
| T1.1 | T1.2 | <interface/data/capability> | <current file:section> | <read-only precondition and proof> |

## Phases & tasks

### Phase 1 — <name>

- **Outcome/demo:** <smallest useful behavior this phase proves>
- **Unproven boundary / risk:** <what must be learned early, or none>
- **Tracer:** <first end-to-end task, or why the path is already proven>

- [ ] **T1.1 — <task>**
  - **Files:** `src/...`
  - **Satisfies:** R1, SC1
  - **Acceptance:** <observable result; the test that proves it>
  - **Depends on:** —
  - **Read first / produces:** <bounded code/research references and delivered contract>
  - **Verification:** <exact command/procedure and expected result>
  - **Preconditions:** <external prerequisites checked read-only, or none>
- [ ] **T1.2 — <task>**
  - **Files:** `...`
  - **Satisfies:** R2
  - **Acceptance:** …
  - **Depends on:** T1.1

### Phase 2 — <name>

- [ ] **T2.1 — <task>** …

## Requirement coverage

| R#/SC# | Owning tasks | Status | Evidence / approved deferral |
| --- | --- | --- | --- |
| R1, SC1 | T1.1 | unverified | <link to actual proof, not a promised check> |

Statuses: `unverified`, `verified`, `human-needed`, `blocked`, `deferred`.
Task checkboxes track implementation/review, not acceptance. Deferral requires
approved scope change; a blocked dependency remains blocked for its consumers.

## Phase closure

Fill after each phase, not before: delivered capabilities; actual checks and
their revision/dirty-file context; decisions/deviations; remaining risks; changes
needed before the next phase. Link evidence from the coverage table rather than
duplicate it. An unproven tracer blocks expansion.

## Verification plan

How the whole change is proven at the end (maps to the spec's success criteria):
test suites to run, manual/browser checks, metrics to observe.

Check the overall outcome and cross-phase connections against the spec, not only
each task. Separate automated proof from required human acceptance; invalidate
affected evidence when the checked code or contracts change.

## Risks & rollback

Highest-risk tasks, and how to undo the change (feature flag, `git revert`,
migration reversal).

For autonomous work, record the retry limit (default three total attempts per
unresolved blocker) and any agreed observable time/cost limit. Persist consumed
attempts and the next action in optional `notes.md` when handing off.
Existing plans need no migration; use only the fields relevant to the work.
