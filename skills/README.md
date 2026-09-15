# Devflow skills catalog

32 skills organized by phase of the loop. Each is a workflow with steps, an
anti-rationalization table, red flags, and evidence-based exit criteria (see
[skill anatomy](../docs/skill-anatomy.md)). Most are **model-invoked** (they
activate automatically when the task fits); the three orchestrators are
**user-invoked** (reached via a `/df-*` command).

[GSD Core, the seventh pillar](../docs/gsd-core.md), strengthens these existing
skills with outcome-first proof, bounded task packets, and safe resumption. It
adds no skill, persona, command, or required runtime.

## Meta

| Skill | Purpose |
| --- | --- |
| [using-devflow](using-devflow/SKILL.md) | Router — picks the on-ramp and routes work to the right skill and phase. |
| [awesome-copilot-discovery](awesome-copilot-discovery/SKILL.md) | Conditionally discovers, pins, audits, and temporarily applies one complementary Awesome Copilot resource. |
| [writing-devflow-skills](writing-devflow-skills/SKILL.md) | How to author and edit Devflow skills consistently. |

## Align / Define

| Skill | Command | Purpose |
| --- | --- | --- |
| [align-and-grill](align-and-grill/SKILL.md) | `/df-align` | One-question-at-a-time interview to ~95% intent clarity. |
| [idea-refine](idea-refine/SKILL.md) | `/df-idea` | Diverge then converge a vague idea into ranked proposals. |
| [write-spec](write-spec/SKILL.md) | `/df-spec` | Durable, measurable spec before code. |
| [domain-modeling](domain-modeling/SKILL.md) | `/df-domain` | Build the shared language (`CONTEXT.md`), constitution, and ADRs. |

## Research

| Skill | Command | Purpose |
| --- | --- | --- |
| [research-codebase](research-codebase/SKILL.md) | `/df-research` | Document how the system works today, with `file:line`. |
| [source-grounded-research](source-grounded-research/SKILL.md) | — | Ground framework/library facts in primary sources, cited. |

## Plan

| Skill | Command | Purpose |
| --- | --- | --- |
| [plan-in-phases](plan-in-phases/SKILL.md) | `/df-plan` | Plan backward from outcomes into small tasks, dependency contracts, and integration proof. |
| [analyze-artifacts](analyze-artifacts/SKILL.md) | — | Pre-build cross-artifact audit: coverage, consistency, constitution compliance. |

## Build

| Skill | Command | Purpose |
| --- | --- | --- |
| [subagent-driven-implementation](subagent-driven-implementation/SKILL.md) | `/df-build` | Fresh subagent per task + two-stage review. |
| [incremental-implementation](incremental-implementation/SKILL.md) | — | Thin vertical slices, commit per slice (direct execution). |
| [test-driven-development](test-driven-development/SKILL.md) | — | Red-green-refactor; Prove-It for bugs. |
| [api-and-interface-design](api-and-interface-design/SKILL.md) | — | Contract-first design; Hyrum's Law; boundary validation. |
| [frontend-ui-engineering](frontend-ui-engineering/SKILL.md) | — | Component/state architecture; accessibility by default. |
| [context-engineering](context-engineering/SKILL.md) | — | Bounded task context, tool/MCP access, and artifact-based handoff/resumption. |

## Verify

| Skill | Command | Purpose |
| --- | --- | --- |
| [verify-before-done](verify-before-done/SKILL.md) | — | Evidence gate — no "done" without proof. |
| [debug-root-cause](debug-root-cause/SKILL.md) | `/df-debug` | Reproduce → localize → fix at root → guard. |
| [browser-verification](browser-verification/SKILL.md) | — | Verify web behavior against live runtime data. |

## Review

| Skill | Command | Purpose |
| --- | --- | --- |
| [review-code](review-code/SKILL.md) | `/df-review` | Two-axis review (spec + standards), parallel personas. |
| [simplify-code](simplify-code/SKILL.md) | `/df-simplify` | Reduce complexity, preserve behavior (Chesterton's Fence). |
| [security-hardening](security-hardening/SKILL.md) | — | OWASP Top 10 prevention; auth, secrets, dependencies. |
| [performance-optimization](performance-optimization/SKILL.md) | — | Measure-first; target the real bottleneck. |

## Ship

| Skill | Command | Purpose |
| --- | --- | --- |
| [git-workflow](git-workflow/SKILL.md) | — | Trunk-based, atomic commits, deliberate staging. |
| [ship-it](ship-it/SKILL.md) | `/df-ship` | PR, green CI, staged rollout, monitoring. |
| [resolve-pr-feedback](resolve-pr-feedback/SKILL.md) | `/df-pr` | Work through PR review comments systematically. |
| [pr-review-loop](pr-review-loop/SKILL.md) | — | Isolated, reviewed, one-item-at-a-time pipeline with per-item approval. |

## Compound

| Skill | Command | Purpose |
| --- | --- | --- |
| [compound-learnings](compound-learnings/SKILL.md) | `/df-compound` | Capture solved problems so the next run is faster. |

## Orchestrators (user-invoked)

| Skill | Command | Purpose |
| --- | --- | --- |
| [feature-workflow](feature-workflow/SKILL.md) | `/df-feature` | Full greenfield loop, idea → shipped, with approval gates. |
| [fix-workflow](fix-workflow/SKILL.md) | `/df-fix` | Brownfield bug-fix fast-path. |
| [autopilot](autopilot/SKILL.md) | `/df-auto` | Hands-off build→PR after a single approval. |

---

**Personas** (`../agents/`): [software-engineer](../agents/software-engineer.md)
(build), [code-reviewer](../agents/code-reviewer.md),
[spec-auditor](../agents/spec-auditor.md),
[security-auditor](../agents/security-auditor.md),
[test-engineer](../agents/test-engineer.md),
[performance-auditor](../agents/performance-auditor.md).

**References** (`../references/`):
[definition-of-done](../references/definition-of-done.md),
[testing-patterns](../references/testing-patterns.md),
[security-checklist](../references/security-checklist.md),
[code-review-rubric](../references/code-review-rubric.md),
[execution-checkpoints](../references/execution-checkpoints.md).
