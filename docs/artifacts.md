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
    notes.md                  # running decisions/log during build (optional)
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
| `solutions/*.md` | `compound-learnings` | future `align-and-grill`, `plan-in-phases`, `research-codebase` | [solution.md](../templates/solution.md) |
| `CONTEXT.md` | `domain-modeling` | every skill (naming, test vocabulary) | [CONTEXT.md](../templates/CONTEXT.md) |
| `constitution.md` | `domain-modeling` | `analyze-artifacts`, `review-code`, `plan-in-phases` | [constitution.md](../templates/constitution.md) |
| `adr/*.md` | `domain-modeling`, `api-and-interface-design` | `review-code`, future planning | [adr.md](../templates/adr.md) |

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

No special tooling required — the artifacts *are* the state.
