# How the source systems compare

Devflow is a synthesis of seven agentic-engineering systems. This document curates
what each does, compares their shapes honestly, and states what Devflow borrows
from each. If you're deciding whether to use Devflow or one of the originals, this
is the map.

## The seven systems

### [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills)
Production-grade lifecycle skills organized `DEFINE → PLAN → BUILD → VERIFY →
REVIEW → SHIP`, grounded in Google engineering practices. Its signature moves are
**anti-rationalization tables** (every skill names the excuses an agent uses to
skip a step, with rebuttals) and **non-negotiable verification** (every skill ends
in evidence requirements). Ships slash commands, review personas, and reference
checklists; installs across 70+ agents via the universal `npx skills` installer.

- **Strengths:** breadth, discipline, honest self-checks, multi-platform reach.
- **Trade-off:** comprehensive by design — a lot of surface to absorb.

### [mattpocock/skills](https://github.com/mattpocock/skills)
Small, composable, anti-framework skills "for real engineers, not vibe coding".
Explicitly rejects heavier process frameworks that "take away control". Signature
ideas: **grilling** (relentless one-question-at-a-time alignment), a **domain
model / shared language** (`CONTEXT.md` + ADRs) to cut agent verbosity and drift,
and a clean **user-invoked vs model-invoked** split so orchestration flows one way.

- **Strengths:** sharp alignment, composability, deep-module design thinking.
- **Trade-off:** deliberately minimal — you assemble the process yourself.

### [EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin)
"Each unit of engineering work should make the next easier." A tight loop
(`brainstorm → plan → work → simplify → review → compound`) where **`/ce-compound`
writes learnings that the next run reads as grounding** — knowledge literally
compounds. Also ships an autonomous end-to-end mode (`/lfg`) and broad native
platform support across coding agents.

- **Strengths:** the compounding-knowledge flywheel, autonomous pipeline, reach.
- **Trade-off:** opinionated by design; the loop assumes you adopt the whole thing.

### [lossyrob/phased-agent-workflow (PAW)](https://github.com/lossyrob/phased-agent-workflow)
Context-Driven Development: dedicated **research and planning phases produce
durable artifacts** (spec, research, plan) before code, and every implementation
step is **PR-integrated** for human review. Artifacts are **rewindable
checkpoints**; a separate Review workflow drafts evidence-based PR comments. Built
first for GitHub Copilot (CLI + VS Code).

- **Strengths:** durable/rewindable artifacts, PR-native team workflow, auditability.
- **Trade-off:** heavier ceremony; optimized for structured, reviewable work.

### [obra/superpowers](https://github.com/obra/superpowers)
A complete methodology that **auto-activates** via session hooks. Signature moves:
**subagent-driven development** (a fresh subagent per task with a two-stage review
— spec compliance, then code quality), **git worktrees** for isolation, and
strict **TDD**. Includes a `writing-skills` meta-skill and a 4-phase
`systematic-debugging` process.

- **Strengths:** autonomous long runs, fresh-context quality control, TDD rigor.
- **Trade-off:** the full methodology is a strong opinion to adopt wholesale.

### [github/spec-kit](https://github.com/github/spec-kit)
GitHub's **Spec-Driven Development** toolkit: the specification becomes the
executable source of truth. A project **constitution** (`memory/constitution.md`)
sets binding principles that gate every phase; a **`/clarify`** loop resolves
ambiguity back into the spec; and **`/analyze`** runs a read-only cross-artifact
consistency & coverage check (spec ↔ plan ↔ tasks, constitution compliance)
*before* implementation. Ships a `specify` CLI with 30+ agent integrations.

- **Strengths:** the constitution as an enforced gate, pre-implementation artifact analysis, technology-independent spec-first flow.
- **Trade-off:** heavier up-front ceremony; the spec → plan → tasks pipeline assumes you adopt SDD.

### [open-gsd/gsd-core](https://github.com/open-gsd/gsd-core)
Context-engineered, spec-driven delivery through a milestone/phase/plan/task
hierarchy. Its useful connective tissue is **goal-backward planning** (observable
outcomes, artifacts, critical wiring), **tracer-first feedback**, bounded executor
packets, durable summaries, and artifact-first resumption. Verification separates
implementation claims from current outcome evidence and required human judgment.

- **Strengths:** explicit integration proof, context-efficient handoffs, recovery
  of unfinished gates, decision traceability, and bounded autonomous execution.
- **Trade-off:** the upstream includes its own CLI, runtime adapters, and
  `.planning/` machinery. Devflow adopts compatible procedures, not that runtime.

See the [pinned source/adaptation ledger](gsd-core.md) for what is incorporated,
what is already covered, exclusions, and evidence limits.

## Side-by-side

| Dimension | agent-skills | mattpocock | compound-eng | PAW | superpowers | spec-kit | GSD Core |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Core shape | Lifecycle suite | Composable toolkit | Compounding loop | Phased + PR | Auto methodology | Spec-driven | Context-engineered phase loop |
| Alignment | `interview-me` | **grilling** | `brainstorm` | spec phase | `brainstorming` | `/clarify` | Discuss + decision scope |
| Durable artifacts | partial | `CONTEXT.md`/ADR | `solutions/` | **spec/research/plan** | plans | **spec/plan/tasks** + constitution | Roadmap, state, plans, summaries |
| Knowledge compounding | — | — | **`/ce-compound`** | — | — | — | Decisions + dependency summaries |
| Execution | incremental | `implement` | `work` | phased | **subagent 2-stage** | `/implement` | **Tracer-first + bounded packets** |
| Verification | **evidence gates** | tdd | review | review | tdd + verify | **`/analyze`** x-artifact | **Outcomes + wiring + freshness** |
| Anti-rationalization | **tables** | — | — | — | **red-flag tables** | — | Scoped execution/verification rules |
| Review | 5-axis persona | 2-axis parallel | reviewer skills | AI PR review | 2-stage | `/analyze` | Plan checker + verifier + milestone audit |
| Autonomy | `/build auto` | — | **`/lfg`** | policies | subagent runs | `/implement` | Bounded retries + checkpoint recovery |
| Distribution | universal + native | universal | native (widest) | Copilot + VS Code | marketplace + native | `specify` CLI, 30+ agents | CLI + runtime adapters |

## What Devflow curates from each

Devflow's thesis: these systems are complementary, not competing. It takes the
strongest, compatible idea from each and fuses them into one loop.

| From | Devflow adopts |
| --- | --- |
| **agent-skills** | Anti-rationalization + Red Flags tables and **evidence-based Verification** in every skill; the DEFINE→SHIP breadth; review personas; the universal installer. |
| **mattpocock** | **`align-and-grill`** (one-question alignment), the **`CONTEXT.md` domain model**, and the user-invoked-vs-model-invoked discipline. |
| **compound-engineering** | **`compound-learnings`** — the return arrow where `solutions/` notes feed the next run — and an **`autopilot`** mode. |
| **PAW** | **Durable, rewindable artifacts** (`spec.md`/`research.md`/`plan.md`) and the PR-integrated review path (`resolve-pr-feedback`). |
| **superpowers** | **`subagent-driven-implementation`** with the two-stage (spec, then quality) review, strict **TDD**, and the `writing-devflow-skills` meta-skill. |
| **spec-kit** | **`analyze-artifacts`** — a read-only, pre-build cross-artifact coverage & consistency gate — and a per-project **`constitution.md`** of binding principles, enforced in `review-code`. |
| **GSD Core** | **Goal-backward proof**, tracer feedback before expansion, dependency/interface contracts, bounded task packets, reconciled checkpoints, and current acceptance evidence — through existing skills and artifacts, not a new runtime. |

## Targeted ECC contributions

[affaan-m/ECC](https://github.com/affaan-m/ECC) adds useful feedback and
compatibility practices to those seven foundations. Research is pinned to
[`4adeee6732a12d1540f49a4d50a38ce8c97f9a53`](https://github.com/affaan-m/ECC/commit/4adeee6732a12d1540f49a4d50a38ce8c97f9a53)
(2026-11-20). ECC is [MIT-licensed, copyright 2026 Affaan Mustafa][ecc-license].
These are independently written process adaptations; no upstream code, skill
bodies, or bundled assets are vendored. Copies or substantial portions of its
material must retain the copyright and permission notice.

| ECC mechanism / source | Devflow adaptation |
| --- | --- |
| [Capability/regression evaluations, graders, and repeated-trial distinctions][ecc-evals] | One [behavior scorecard](../references/skill-evaluation.md), consumed by [skill authoring](../skills/writing-devflow-skills/SKILL.md) and [verification](../skills/verify-before-done/SKILL.md). Inspect actual actions/artifacts; keep structural checks and human acceptance separate. |
| [Project-scoped evidence-backed learning][ecc-learning] and [reviewable promotion][ecc-promotion] | [Compounding](../skills/compound-learnings/SKILL.md) and the [solution template](../templates/solution.md) make applicability, contradictions, and proposed promotion explicit. Extend existing guidance only through normal approval/review; no confidence score grants authority. |
| [Explicit host capability declarations][ecc-hosts] | The [installation matrix](install.md#capability-and-evidence-matrix) separates declared content, observed version/route behavior, and unverified hooks. A portable skill file is not proof of runtime parity. |
| [Catalog validation workflow][ecc-validation] | [Minimal CI](../.github/workflows/validate.yml) runs Devflow's existing Python checks with read-only permissions and pinned actions. No upstream Node validation stack or warn-only contract defaults. |
| [Agent-configuration security surfaces][ecc-security] | The existing [security checklist](../references/security-checklist.md) covers instruction authority, tool/MCP permissions, hooks, secrets, provenance, and recording consent. No external scanner or automatic fixes. |
| [Phase-boundary compaction][ecc-compaction] | Already substantially covered by [execution checkpoints](../references/execution-checkpoints.md) and context engineering. Keep that contract; no extra hook, token counter, or state directory. |

**What stays out:** ECC's automatic observers, instinct database, generated skill
catalog, global promotion, hook-profile framework, model routing, telemetry,
installers, and evaluation runtime. The inspected [candidate execution
gate][ecc-gate] refuses execution; it is not a ready backend for Devflow. This
does not imply that every ECC evaluation utility is disabled.

**Evidence limits:** offline tests validate contracts and actual local hook
output, not universal agent compliance. Native scenario observations are bounded
by their fixture, loaded source, host/model, and permissions; missing evidence
stays unverified. No measured reliability, token-saving, or speed claim is made.
Hosted CI execution requires an authorized push/PR; a locally passing command
does not certify the hosted job.

[ecc-evals]: https://github.com/affaan-m/ECC/blob/4adeee6732a12d1540f49a4d50a38ce8c97f9a53/skills/eval-harness/SKILL.md#L29-L105
[ecc-learning]: https://github.com/affaan-m/ECC/blob/4adeee6732a12d1540f49a4d50a38ce8c97f9a53/skills/continuous-learning-v2/SKILL.md#L26-L79
[ecc-promotion]: https://github.com/affaan-m/ECC/blob/4adeee6732a12d1540f49a4d50a38ce8c97f9a53/skills/continuous-learning-v2/scripts/instinct-cli.py#L1617-L1765
[ecc-hosts]: https://github.com/affaan-m/ECC/blob/4adeee6732a12d1540f49a4d50a38ce8c97f9a53/scripts/lib/harness-capabilities.js#L31-L168
[ecc-validation]: https://github.com/affaan-m/ECC/blob/4adeee6732a12d1540f49a4d50a38ce8c97f9a53/.github/workflows/reusable-validate.yml#L12-L64
[ecc-security]: https://github.com/affaan-m/ECC/blob/4adeee6732a12d1540f49a4d50a38ce8c97f9a53/skills/security-scan/SKILL.md#L10-L43
[ecc-compaction]: https://github.com/affaan-m/ECC/blob/4adeee6732a12d1540f49a4d50a38ce8c97f9a53/skills/strategic-compact/SKILL.md#L78-L124
[ecc-gate]: https://github.com/affaan-m/ECC/blob/4adeee6732a12d1540f49a4d50a38ce8c97f9a53/scripts/lib/eval-harness/gate.js#L189-L197
[ecc-license]: https://github.com/affaan-m/ECC/blob/4adeee6732a12d1540f49a4d50a38ce8c97f9a53/LICENSE#L1-L21

## When to use Devflow vs an original

- Want **one opinionated loop** that fuses alignment, durable artifacts,
  subagent execution, verification, and compounding — with **dual on-ramps** for
  greenfield and brownfield, across Copilot/Claude/Cursor/Codex? → **Devflow.**
- Want the **broadest catalog** of lifecycle skills? → agent-skills.
- Want the **most minimal, hackable** pieces to assemble yourself? → mattpocock.
- Already all-in on **one vendor's ecosystem/loop**? → compound-engineering or
  superpowers.
- Need a **PR-first, phase-gated team process** on Copilot? → PAW.
- Want GSD's **full milestone runtime and tooling**, rather than selected
  procedures integrated into Devflow's portable loop? → GSD Core.

Devflow stands on their shoulders. If you like an idea here, the original that
inspired it is worth reading in full — all seven are excellent and MIT-licensed.
The optional Awesome Copilot specialist catalog is an integration, not an eighth
foundational system.
