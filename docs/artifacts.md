# Durable Artifacts

Devflow's signature is that every phase leaves behind a **durable, versioned
artifact** rather than ephemeral chat context. Artifacts are checkpoints: they
accumulate understanding, make the work auditable, survive context compaction,
and are **rewindable** — if requirements drift, restart from the spec, the plan,
or any phase without losing the reasoning.

## Where artifacts live

In the project that *uses* Devflow, artifacts are written under `docs/devflow/`:

```
docs/devflow/
  <slug>/                     # one directory per unit of work (feature or fix)
    spec.md                   # what & why  (write-spec)
    research.md               # how the system works today  (research-codebase)
    plan.md                   # phased task breakdown  (plan-in-phases)
    notes.md                  # bounded execution/resume checkpoint (optional)
  solutions/                  # compounding knowledge base (compound-learnings)
    <yyyy-mm-dd>-<slug>.md
  CONTEXT.md                  # the project's shared language / domain model
  constitution.md             # binding, project-wide principles  (domain-modeling)
  adr/                        # Architecture Decision Records
    NNNN-<slug>.md
```

`<slug>` is a short kebab-case name for the change (e.g. `retry-safe-webhooks`).

> Small fixes don't need every file. The `fix-workflow` fast-path may only produce
> a `solutions/` entry. The `feature-workflow` full path produces the whole set.

## Artifact contracts

Each artifact has a canonical shape so later phases (and later runs) can rely on
it. Starter templates are in [`/templates/`](../templates); the owning skill fills
them in.

| Artifact | Produced by | Consumed by | Template |
| --- | --- | --- | --- |
| `spec.md` | `write-spec` | `plan-in-phases`, `review-code` (Spec axis) | [spec.md](../templates/spec.md) |
| `research.md` | `research-codebase` | `plan-in-phases`, `subagent-driven-implementation` | [research.md](../templates/research.md) |
| `plan.md` | `plan-in-phases` | `analyze-artifacts`, `subagent-driven-implementation`, `verify-before-done` | [plan.md](../templates/plan.md) |
| `notes.md` (optional) | `context-engineering` with the build orchestrator | `using-devflow`, `context-engineering`, both build paths, `autopilot` | [notes.md](../templates/notes.md) |
| `solutions/*.md` | `compound-learnings` | future `align-and-grill`, `plan-in-phases`, `research-codebase` | [solution.md](../templates/solution.md) |
| `CONTEXT.md` | `domain-modeling` | every skill (naming, test vocabulary) | [CONTEXT.md](../templates/CONTEXT.md) |
| `constitution.md` | `domain-modeling` | `analyze-artifacts`, `review-code`, `plan-in-phases` | [constitution.md](../templates/constitution.md) |
| `adr/*.md` | `domain-modeling`, `api-and-interface-design` | `review-code`, future planning | [adr.md](../templates/adr.md) |

## Execution state without a second system

[GSD Core's contribution](gsd-core.md) extends these existing contracts:

- **`spec.md` owns intent:** stable `R#`/`SC#`, invariants, locked decisions,
  delegated choices, and deferred scope. Research cannot silently amend it.
- **`research.md` owns facts:** current boundary contracts, unproven assumptions,
  prerequisites, and classified planning inputs, all grounded in source.
- **`plan.md` owns delivery:** outcome/artifact/connection proof, dependency
  contracts, task checkboxes, requirement coverage, and verified phase closures.
  Planning owns the approved approach; build/verification update progress and
  evidence. Changed scope/contracts return to approval and applicable artifact
  analysis.
- **Optional `notes.md` owns navigation:** current stage/task, repository
  revision and dirty files, evidence references, consumed retries, blockers,
  pending approvals, and the exact next action. It is not a new authority or a
  transcript. Reconcile it with the actual repository before continuing.

Implementation complete, requirement verified, and required human acceptance
are different facts. Coverage can be `unverified`, `verified`, `human-needed`,
`blocked`, or explicitly approved `deferred`; a checked task or a worker report
does not make the whole phase complete. Changed inputs make affected evidence
stale. See [execution checkpoints](../references/execution-checkpoints.md).

No migration is needed for older plans; fill relevant missing detail before the
affected task runs. Missing notes are normal. Small fixes retain their fast
path without mandatory spec, plan, or checkpoint files. Project-wide `CONTEXT.md`
and `solutions/` remain the durable knowledge layer, not session-progress logs.

## The compounding contract

`compound-learnings` writes a `solutions/` entry after a non-obvious problem is
solved. The next `align-and-grill`, `plan-in-phases`, and `research-codebase`
**read** the `solutions/` directory and `CONTEXT.md` as grounding. That return
arrow — learnings feeding the next run — is what makes the loop *compound*: the
first time you solve a problem costs research; the second time costs minutes.

## Rewind

Because artifacts are plain files in git, rewinding is just reverting to an
earlier artifact and re-running from that phase:

- Requirements changed → edit `spec.md`, re-run `plan-in-phases`.
- Plan proved wrong → edit `plan.md`, re-run the build.
- Approach was misguided → `git revert` the artifacts and restart from `write-spec`.

Reapprove changed scope/contracts and rerun `analyze-artifacts` when applicable
before affected execution. Invalidate affected coverage/closure evidence and
reconcile the checkpoint; never use stale approval or completion records to skip
a gate.

No special tooling required — the artifacts *are* the state.
