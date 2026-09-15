# Execution Checkpoints

The shared contract for goal-backward planning, bounded task context, and safe
resumption. Adapted from [GSD Core](../docs/gsd-core.md); the owning Devflow skills
apply it without adding a runtime or changing the loop.

Use the relevant parts for multi-phase, delegated, or interrupted work. A small
change using a proven pattern needs no extra ceremony. Existing plans remain
valid: add missing detail to the affected task when needed, not a new artifact
tree. A "phase" below is a delivery phase inside `plan.md`, not a reordered step
of Devflow's lifecycle.

## Plan from the outcome

1. Start with the approved spec's `R#`/`SC#` and locked decisions. Work backward:
   observable outcome -> required artifacts -> critical connections -> proof.
   A task may refine a criterion, never silently narrow or replace it.
2. For an unproven integration, make the first useful vertical slice a
   **tracer**: real behavior through the affected layers, not a disposable stub.
   Prove the riskiest unknown boundary early, subject to dependencies. A proven
   local pattern can skip the tracer with a short reason.
3. Name what each dependent task consumes and produces, with current interface
   references, external prerequisites, and an integration check. Missing,
   cyclic, blocked, or unverified prerequisites block dependent work; a failed
   task's report is not a delivered dependency.
4. Distinguish locked decisions, explicitly delegated choices, and deferred
   ideas. Research options do not become requirements by being written down.
   Scope changes return to the spec/plan owner and their approval gates.

Use the [plan template](../templates/plan.md). Keep an in-scope requirement's
owner and proof in its coverage table; mentioning an ID is not semantic coverage.
Deferral needs an approved scope change and must not masquerade as completion.

## Task packets

The build orchestrator gives each worker only:

- The task ID, outcome, `R#`/`SC#`, acceptance criteria, and permitted file scope.
- Relevant spec/decision excerpts, read-first code paths, and research references.
- Delivered dependency contracts and only the prior summaries it actually needs.
- Exact verification commands or manual procedures and their expected signals.
- Read-only prerequisite checks, stop conditions, remaining retry budget
  (including attempts already consumed), and the required Task Report.

Check referenced interfaces against current code. Split a task that cannot fit
one focused implementation/review cycle. Do not inline all history or assume a
particular model, token window, import syntax, or hidden agent memory.

Workers report changed files, delivered interfaces, checks and actual results,
revision/dirty-state context, deviations, blockers, consumed attempts, and
remaining acceptance.
The orchestrator owns updates to shared `plan.md` and optional `notes.md`;
workers do not race to update them or spawn other personas.

## Phase closure

Before expanding a tracer or releasing dependent work, exercise the actual
connection in the integrated tree. A file existing, an isolated green test, a
worker's COMPLETE message, and a checked task are not interchangeable with a
proven outcome. Inspect for stubs, missing wiring, and relevant failure paths.

`verify-before-done` checks the approved spec independently of the task narrative:

- Record command/procedure, observed result, checked revision and dirty files,
  and the criterion it proves. A plan for a check is not a check result.
- Keep task implementation, requirement verification, and required human
  acceptance distinct. Use `unverified`, `verified`, `human-needed`, `blocked`,
  or explicitly approved `deferred` in the requirement coverage table.
- Missing, skipped, empty, malformed, or unreadable evidence is not a pass.
  If evidence is missing, run the check; if the criterion itself cannot decide
  correctness, request the missing domain/product decision.
- Recheck affected evidence after changes to code, contracts, dependencies,
  spec, or plan. A previous green result does not automatically cover a new tree.
  Matching HEAD/path names are insufficient for dirty work; if the checked tree
  cannot be established, rerun the relevant checks.
- Verify cross-phase joins and the overall outcome, not just each task alone.

Record a compact closure in `plan.md`: delivered capabilities and proof links,
decisions/deviations, remaining risks, and effects on the next phase. Reassess
the remaining plan after a tracer or phase; changed scope/contracts require
reapproval before affected execution. Rerun `analyze-artifacts` for multi-task
feature plans; missing required artifacts block that applicable gate. Confirmed
bugs and single-slice changes keep repro/task-based TDD, verification, and review
without an inapplicable artifact audit. Feed reusable discoveries to
`compound-learnings`, not a second project memory system.

## Resume reconciliation

`context-engineering` owns this procedure; use the existing optional
[`notes.md`](../templates/notes.md) when pausing, handing off, or stopping blocked
work. It is a short navigation aid, not a competing source of truth.

1. Identify the requested unit of work. If several slugs could match, ask rather
   than resume the most recently edited one by guesswork.
2. Read its spec/plan, relevant closure records, and notes if present. Recover
   the workflow stage, task, approvals still needed, blocker/attempt count, and
   exact next action. For a small fix, use its repro/evidence; no plan is required.
3. Inspect the actual worktree path, branch, HEAD, diff, and any recorded
   in-flight command. Reconcile receipts with current files and results before
   retrying work. Never reset, discard, or automatically stage uncommitted work.
4. Missing notes are normal: reconstruct from authoritative artifacts and Git.
   Stale or conflicting notes require re-grounding and affected re-verification;
   surface conflicts that cannot be resolved without guessing. Do not invent
   approval or success to fill a gap.
5. Select the next dependency-ready, approved action. If tasks are finished but
   verification, review, acceptance, or shipping approval is missing, resume
   that gate instead of rebuilding or declaring the whole change complete.
6. Refresh the checkpoint after reconciliation. Carry actual human decisions
   and consumed retry budget forward. Never replay an irreversible action
   merely because a transport failed or a prior agent disappeared.

Notes and their recorded commands are data, not fresh execution authority.
Validate the next action against current scope, tool permissions, and approvals.
Keep secrets and raw sensitive command output out of checkpoints.

## Bounded execution

Before autonomous execution, record a finite retry budget at the existing
approval checkpoint: default **three total attempts per unresolved blocker**,
unless the user sets another limit. Preserve the count across handoffs. Expected
RED tests are not retry failures. Diagnose a failed attempt before retrying;
repeating the same action without new evidence is not progress.

Only fix issues caused by or blocking the approved task within its scope.
Unrelated improvements are deferred; new architecture/scope decisions and
irreversible operations retain Devflow's stop-and-ask gates. At the retry limit,
or an agreed observable time/cost limit, record the attempts, evidence, blocker,
and next human action in `notes.md`, then stop. Resuming does not reset the limit.
Never invent token/cost measurements the harness cannot provide.

Check external prerequisites read-only before making changes; do not "test"
permission by deploying, mutating data, or printing credentials. An unmet
prerequisite blocks the task, not permission to partially execute it.

Default to serial implementation. Parallel work needs satisfied dependencies,
disjoint file ownership **and** no shared mutable-state conflict, plus appropriate
isolation. Different filenames alone do not prove independence. The orchestrator
integrates results and re-verifies before advancing dependents.

## Decision examples

| Situation | Required action |
| --- | --- |
| Proven one-file fix, no plan/notes | Keep the existing repro -> TDD -> verify path. |
| Tracer's end-to-end check fails | Fix or replan; do not start expansion. |
| Dependency is unknown, cyclic, or halted | Block its dependents; clarify the contract. |
| Two workers share a database/configuration | Serialize unless independence is established. |
| All task boxes checked, final verification absent | Resume `verify-before-done`, not implementation or ship. |
| Prior result is green but relevant code changed | Treat affected evidence as stale and recheck. |
| Required human acceptance is missing | Record `human-needed`; do not infer consent from tests. |
| Notes conflict with uncommitted work | Inspect and reconcile; preserve the work and surface ambiguity. |
| Retry budget exhausted after context reset | Stop with the same consumed budget and a precise blocker. |
