# Using devflow

Devflow adapts to the work. Pick an on-ramp, or reach for a single skill. Every
`/df-*` command maps to a skill of the same purpose; you can also just describe
your task and let the agent route it.

## Worked example — a new feature (greenfield)

```text
/df-feature add per-user rate limiting to the public API
```

The `feature-workflow` orchestrator runs the full loop, pausing at the ★ gates:

1. **Align** — `align-and-grill` interviews you one question at a time (limits per
   what? by key or IP? what happens on breach?) until intent is ~95% clear.
2. **★ Spec** — `write-spec` writes `docs/devflow/rate-limiting/spec.md` with
   measurable success criteria. *You approve it.*
3. **Research** — `research-codebase` documents today's request pipeline with
   `file:line` into `research.md`.
4. **★ Plan** — `plan-in-phases` breaks it into thin, ordered tasks in `plan.md`.
   *You approve it.*
5. **Build** — `subagent-driven-implementation` executes each task test-first
   (`test-driven-development`), with a two-stage review and one commit per task.
6. **Verify** — `verify-before-done` runs the full suite + build and checks every
   criterion with evidence.
7. **Review** — `review-code` runs the spec and standards axes in parallel.
8. **★ Ship** — `ship-it` opens a PR behind a flag; *you approve the merge.*
9. **Compound** — `compound-learnings` writes a `solutions/` note.

Prefer to drive it yourself? Run the phases as commands: `/df-align` → `/df-spec`
→ `/df-research` → `/df-plan` → `/df-build` → `/df-review` → `/df-ship` →
`/df-compound`.

## Worked example — a bug fix (brownfield)

```text
/df-fix the checkout webhook sometimes creates duplicate invoices
```

The `fix-workflow` fast-path:

1. **Reproduce & root-cause** — `debug-root-cause` makes a deterministic repro,
   localizes, and confirms the true cause (not the symptom).
2. **Prove it** — a failing reproduction test (`test-driven-development`).
3. **Fix at the root** — minimal change; the repro test goes green.
4. **Verify** — full suite green, no regressions.
5. **Review & ship** — `review-code`, then `ship-it` with the repro test as
   evidence.
6. **Compound** — `compound-learnings` records the cause, the tell-tale signs, and
   the guardrail so this bug class is cheap next time.

## Worked example — hands-off autopilot

```text
/df-spec         # (or /df-feature through the plan gate)
/df-auto
```

`autopilot` requires an approved spec (or a confirmed bug) and a clean git tree.
After **one** approval it runs plan→build→verify→review→PR autonomously — every
task still test-driven, reviewed, and committed individually — stopping only for
blockers or irreversible steps (auth, migrations, payments, deploys, secrets). You
come back to a green, open PR.

## Reaching for a single skill

You don't need an orchestrator for small, well-understood work. Any command works
standalone:

| You want to… | Command | Skill |
| --- | --- | --- |
| Get grilled into clarity | `/df-align` | `align-and-grill` |
| Explore a fuzzy idea | `/df-idea` | `idea-refine` |
| Write a spec | `/df-spec` | `write-spec` |
| Build the shared language | `/df-domain` | `domain-modeling` |
| Understand existing code | `/df-research` | `research-codebase` |
| Plan an approved spec | `/df-plan` | `plan-in-phases` |
| Implement the next task | `/df-build` | `subagent-driven-implementation` |
| Debug a failure | `/df-debug` | `debug-root-cause` |
| Review a diff | `/df-review` | `review-code` |
| Simplify code | `/df-simplify` | `simplify-code` |
| Ship it | `/df-ship` | `ship-it` |
| Resolve PR comments | `/df-pr` | `resolve-pr-feedback` |
| Capture a learning | `/df-compound` | `compound-learnings` |

Model-invoked skills (`test-driven-development`, `security-hardening`,
`verify-before-done`, `browser-verification`, …) also activate automatically when
the task fits — you rarely call them by hand.

## Rewinding

Artifacts are checkpoints. If requirements change, edit `spec.md` and re-run
`/df-plan`. If the plan proved wrong, edit `plan.md` and re-run `/df-build`. If the
approach was misguided, `git revert` the artifacts and restart from `/df-spec`.
The files *are* the state — no special tooling.

## Compounding, over time

The payoff grows across runs. Each `compound-learnings` note and each `CONTEXT.md`
update is read as grounding by the next `align-and-grill`, `research-codebase`, and
`plan-in-phases`. The first time you solve a problem costs research; the second
time costs minutes. Keep the loop closed — don't skip the compound step.

## When Devflow stops and asks

Devflow pauses for you on: ambiguous requirements, an unapproved spec/plan, an
unfixable failure, or any **irreversible** step — auth/permissions, destructive
migrations, payments, deletions, deploys, or anything touching secrets. That's by
design, not a limitation.
