# GSD Core: the seventh pillar

[GSD Core](https://github.com/open-gsd/gsd-core) contributes **goal-backward,
context-bounded delivery with durable execution evidence**. Devflow incorporates
that discipline into its existing skills, not GSD's runtime or a second workflow.
The original six foundations remain; Awesome Copilot is still a separate,
optional specialist catalog.

## Source and scope

Research baseline: **2026-09-14**, commit
[`9b750dc00aa385e0c2d5a47089cf3158da15e97f`](https://github.com/open-gsd/gsd-core/commit/9b750dc00aa385e0c2d5a47089cf3158da15e97f).
The [pinned manifest](https://github.com/open-gsd/gsd-core/blob/9b750dc00aa385e0c2d5a47089cf3158da15e97f/package.json#L1-L10)
identifies `@opengsd/gsd-core` version **1.14.0**. It is
[MIT-licensed, copyright 2026 Open GSD](https://github.com/open-gsd/gsd-core/blob/9b750dc00aa385e0c2d5a47089cf3158da15e97f/LICENSE#L1-L21).
The adaptations here are independently written process guidance; no upstream
code, agent bodies, or bundled assets are vendored. Future copies of substantial
upstream material must retain its copyright and permission notice.

GSD's [architecture][architecture] includes commands, agents, workflows, CLI
helpers, and a `.planning/` tree. Its [roadmapper][roadmapper] and [plan
template][hierarchy] use a milestone -> phase -> plan -> task hierarchy. Devflow
keeps one unit-of-work slug, the phases/tasks already in `plan.md`, and optional
`notes.md`. There is no new milestone/slice identifier scheme or mandatory state
file, and no new skill, persona, command, or installation step.

## What is consolidated

The shared procedure is [Execution Checkpoints](../references/execution-checkpoints.md).
The table distinguishes upstream mechanisms from Devflow's adaptations.

| GSD mechanism and source | Disposition | Devflow integration |
| --- | --- | --- |
| Work backward from goals through observable truths, artifacts, and critical wiring [S1][goals] | Adopt | [Planning](../skills/plan-in-phases/SKILL.md), the [plan's delivery proof](../templates/plan.md#delivery-proof), and [artifact analysis](../skills/analyze-artifacts/SKILL.md) connect each `R#`/`SC#` to an outcome and proof. |
| Tracer-first implementation with a feedback gate before expansion [S2][tracer], [executor gate][tracer-gate] | Adapt | Existing [direct](../skills/incremental-implementation/SKILL.md) and [delegated](../skills/subagent-driven-implementation/SKILL.md) builds prove an unproven integration early. Proven local patterns need no extra tracer ceremony. |
| Explicit interface context, dependency graphs, and file ownership [S3][interfaces], [dependency implementation][dependencies] | Adapt | [Research boundary map](../templates/research.md#boundary-map), task consumes/produces, prerequisite checks, and analysis of cycles/shared state. Unknown or halted dependencies block; no scheduler is imported. |
| Plans as bounded executor packets; selective prior summaries [S4][packet], [context guidance][context] | Adapt | [Context engineering](../skills/context-engineering/SKILL.md) packages only the task's scope, decisions, interfaces, dependency evidence, proof, and stop conditions for the existing worker. No fixed token/model assumptions. |
| Structured summaries, Git-aware resumption, and recovery of missing final gates [S5][summary], [resume][resume], [tail recovery][tail] | Adapt | Verified phase closures stay in `plan.md`; the existing optional [notes artifact](../templates/notes.md) holds a small checkpoint. [The router](../skills/using-devflow/SKILL.md) reconciles actual state before continuing. |
| Locked decisions, delegated discretion, deferred ideas, semantic coverage [S6][decisions] | Adopt | [Spec decision scope](../templates/spec.md#decision-scope), classified [research inputs](../templates/research.md#planning-inputs), and `analyze-artifacts` prevent research suggestions or ID mentions from silently changing approved scope. |
| Separate implementation claims, verification, acceptance, and evidence freshness [S7][freshness], [completion predicate][completion], [milestone audit][audit] | Adapt | [Verification](../skills/verify-before-done/SKILL.md), [shipping](../skills/ship-it/SKILL.md), coverage status, and cross-phase checks require current proof. Revision/dirty-state records replace a digest engine; required human acceptance remains a gate. |
| Task-scoped fixes, read-only preconditions, bounded retry loops [S8][bounded], [autonomous retries][retries] | Adapt | [Autopilot](../skills/autopilot/SKILL.md) records a finite budget at its existing approval checkpoint, preserves attempts across handoffs, and stops with evidence. Devflow's default is three total attempts per unresolved blocker; no upstream automatic-approval default is adopted. |
| Revisit singular/plural, required/optional, derived/chosen assumptions [S9][assumptions] | Adapt | A conditional question in [domain modeling](../skills/domain-modeling/SKILL.md) and research challenges an obsolete invariant. No keyword detector or automatic architecture rewrite. |
| Prohibition checks need both a violation-sensitive failure and a clean control [S10][prohibitions] | Adopt | Existing [TDD](../skills/test-driven-development/SKILL.md) asks for an invalid fixture and a valid control; real results, not claimed fail-first evidence. No extra test runner. |
| Evidence-backed re-verification rather than endless opinion-driven scope growth [S11][convergence] | Adapt | `verify-before-done` distinguishes demonstrated regressions/criterion violations from new preferences. Real failures remain blockers. |
| Fresh workers, TDD, plan checks, atomic commits, persistent learning [S12][summary], [TDD][upstream-tdd], [state][state] | Already covered | Keep the existing build/review personas, mandatory TDD, git discipline, and `CONTEXT.md`/ADRs/`solutions/`. [Compounding](../skills/compound-learnings/SKILL.md) draws on verified phase closures, not a parallel memory system. |

Risk-first ordering is a local adaptation of the tracer and
[bounded integration spike][spike] practices, subject to dependencies. This is
not a claim that GSD implements a generic risk-ranked scheduler.

## What stays out

- **Executable distribution:** GSD's CLI/MCP entry points, SDK dependencies,
  runtime adapters, model routing, capability dispatch, and custom parsers.
  These solve [upstream runtime concerns][manifest], not Devflow's process gap.
- **Another artifact hierarchy:** no `.planning/`, `.gsd/`, roadmap/state
  database, or mandatory handoff format alongside `docs/devflow/`.
- **Automatic workers and updates:** no [update hook][updates], downloaded
  execution, background service, new telemetry, or per-model budget machinery.
- **A parallel-worktree engine:** retain explicit dependency/file/state
  coordination, not the upstream [overlap partitioner][overlap]. Different file
  names do not guarantee independence; serial execution remains the default.
- **Weaker gates:** do not port [automatic decision selection][auto-decisions],
  warning-and-dropped dependency edges, or indeterminate freshness as success.
  Devflow's approvals, mandatory TDD, two-axis review, and external-resource
  trust boundary stay authoritative.

## How to use it

Use the same `/df-plan`, `/df-build`, `/df-auto`, and `/df` entry points. Planning
adds only relevant proof/dependency detail; build skills consume it; verification
closes the phase with evidence; context engineering handles interruptions.
Existing plans remain usable and small fixes retain their fast path.
See the [multi-phase/resume example](usage.md#worked-example---multi-phase-work-and-resumption)
and [artifact ownership](artifacts.md#execution-state-without-a-second-system).

## Evidence limits

This integration is grounded in source inspection, not execution of GSD's code.
Upstream runtime correctness, numeric context/performance claims, and universal
agent compliance are **UNVERIFIED** here. In particular, a structural prose test
does not prove an agent follows a workflow; upstream's
[tracer tests make that distinction][tracer-tests] too. Devflow combines offline
artifact/link contracts with scenario review, without claiming a runtime engine.

[architecture]: https://github.com/open-gsd/gsd-core/blob/9b750dc00aa385e0c2d5a47089cf3158da15e97f/docs/ARCHITECTURE.md#L31-L65
[roadmapper]: https://github.com/open-gsd/gsd-core/blob/9b750dc00aa385e0c2d5a47089cf3158da15e97f/agents/gsd-roadmapper.md#L14-L45
[hierarchy]: https://github.com/open-gsd/gsd-core/blob/9b750dc00aa385e0c2d5a47089cf3158da15e97f/gsd-core/templates/phase-prompt.md#L6-L38
[goals]: https://github.com/open-gsd/gsd-core/blob/9b750dc00aa385e0c2d5a47089cf3158da15e97f/agents/gsd-planner.md#L443-L480
[tracer]: https://github.com/open-gsd/gsd-core/blob/9b750dc00aa385e0c2d5a47089cf3158da15e97f/agents/gsd-planner.md#L253-L279
[tracer-gate]: https://github.com/open-gsd/gsd-core/blob/9b750dc00aa385e0c2d5a47089cf3158da15e97f/agents/gsd-executor.md#L147-L172
[interfaces]: https://github.com/open-gsd/gsd-core/blob/9b750dc00aa385e0c2d5a47089cf3158da15e97f/gsd-core/references/planner-interface-context.md#L5-L61
[dependencies]: https://github.com/open-gsd/gsd-core/blob/9b750dc00aa385e0c2d5a47089cf3158da15e97f/src/phase.cts#L974-L1085
[packet]: https://github.com/open-gsd/gsd-core/blob/9b750dc00aa385e0c2d5a47089cf3158da15e97f/gsd-core/templates/phase-prompt.md#L40-L93
[context]: https://github.com/open-gsd/gsd-core/blob/9b750dc00aa385e0c2d5a47089cf3158da15e97f/gsd-core/references/context-budget.md#L9-L49
[summary]: https://github.com/open-gsd/gsd-core/blob/9b750dc00aa385e0c2d5a47089cf3158da15e97f/gsd-core/templates/summary.md#L91-L175
[resume]: https://github.com/open-gsd/gsd-core/blob/9b750dc00aa385e0c2d5a47089cf3158da15e97f/gsd-core/workflows/resume-project.md#L107-L127
[tail]: https://github.com/open-gsd/gsd-core/blob/9b750dc00aa385e0c2d5a47089cf3158da15e97f/gsd-core/workflows/execute-phase.md#L325-L388
[decisions]: https://github.com/open-gsd/gsd-core/blob/9b750dc00aa385e0c2d5a47089cf3158da15e97f/agents/gsd-planner.md#L53-L108
[freshness]: https://github.com/open-gsd/gsd-core/blob/9b750dc00aa385e0c2d5a47089cf3158da15e97f/src/verification.cts#L934-L991
[completion]: https://github.com/open-gsd/gsd-core/blob/9b750dc00aa385e0c2d5a47089cf3158da15e97f/src/verification.cts#L1043-L1098
[audit]: https://github.com/open-gsd/gsd-core/blob/9b750dc00aa385e0c2d5a47089cf3158da15e97f/gsd-core/workflows/audit-milestone.md#L110-L155
[bounded]: https://github.com/open-gsd/gsd-core/blob/9b750dc00aa385e0c2d5a47089cf3158da15e97f/agents/gsd-executor.md#L237-L272
[retries]: https://github.com/open-gsd/gsd-core/blob/9b750dc00aa385e0c2d5a47089cf3158da15e97f/gsd-core/workflows/autonomous.md#L471-L540
[assumptions]: https://github.com/open-gsd/gsd-core/blob/9b750dc00aa385e0c2d5a47089cf3158da15e97f/capabilities/assumption-delta/fragments/plan-pre.md#L30-L50
[prohibitions]: https://github.com/open-gsd/gsd-core/blob/9b750dc00aa385e0c2d5a47089cf3158da15e97f/src/prohibition-enforcement.cts#L743-L792
[convergence]: https://github.com/open-gsd/gsd-core/blob/9b750dc00aa385e0c2d5a47089cf3158da15e97f/gsd-core/references/verifier-evidence-gate.md#L46-L116
[state]: https://github.com/open-gsd/gsd-core/blob/9b750dc00aa385e0c2d5a47089cf3158da15e97f/gsd-core/templates/state.md#L65-L112
[upstream-tdd]: https://github.com/open-gsd/gsd-core/blob/9b750dc00aa385e0c2d5a47089cf3158da15e97f/agents/gsd-planner.md#L215-L229
[spike]: https://github.com/open-gsd/gsd-core/blob/9b750dc00aa385e0c2d5a47089cf3158da15e97f/gsd-core/workflows/spike.md#L62-L88
[manifest]: https://github.com/open-gsd/gsd-core/blob/9b750dc00aa385e0c2d5a47089cf3158da15e97f/package.json#L5-L65
[updates]: https://github.com/open-gsd/gsd-core/blob/9b750dc00aa385e0c2d5a47089cf3158da15e97f/hooks/gsd-check-update.js#L11-L29
[overlap]: https://github.com/open-gsd/gsd-core/blob/9b750dc00aa385e0c2d5a47089cf3158da15e97f/src/file-overlap-partitioner.cts#L14-L49
[auto-decisions]: https://github.com/open-gsd/gsd-core/blob/9b750dc00aa385e0c2d5a47089cf3158da15e97f/agents/gsd-executor.md#L331-L339
[tracer-tests]: https://github.com/open-gsd/gsd-core/blob/9b750dc00aa385e0c2d5a47089cf3158da15e97f/tests/tracer-bullet.test.cjs#L1-L19
