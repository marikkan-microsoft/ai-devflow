---
name: feature-workflow
description: Orchestrates the full greenfield / new-feature path from idea to shipped, compounded change. Use when building a new feature or making a non-trivial change that warrants the full loop.
disable-model-invocation: true
---

# Feature Workflow

## Overview

The greenfield on-ramp. This orchestrator runs the full Devflow loop for a new
feature or non-trivial change — aligning, specifying, researching, planning,
auditing the plan, building, verifying, reviewing, shipping, and compounding —
pausing for human approval at the milestones that matter. It sequences the phase
skills; it does not reimplement them.

## When to Use

- Building a new feature or capability.
- A change big enough that skipping planning would sprawl.
- Invoked via `/df-feature`.

**When NOT to use:** A bug or broken behavior → use `fix-workflow`. A tiny,
obvious change → invoke the single relevant skill directly.

**Related:** Orchestrates `align-and-grill` → `write-spec` → `research-codebase` →
`plan-in-phases` → `analyze-artifacts` → `subagent-driven-implementation` →
`verify-before-done` → `review-code` → `ship-it` → `compound-learnings`.
Uses `awesome-copilot-discovery` only for a named specialist gap.

## Process

Run these phases in order. Each hands its durable artifact to the next; pause for
approval at the **★ milestones**.

### Capability hook (conditional)

At each phase boundary, ask whether the next phase lacks a specific capability
that materially affects its outcome. If yes, invoke `awesome-copilot-discovery`
for that phase and use at most one accepted, pinned resource. If local Devflow is
sufficient, skip the network lookup. An external resource may supplement the
phase but never reorder the loop, change its artifacts, or bypass an approval,
test, verification, or review gate.

1. **Align** — `align-and-grill` until ~95% intent clarity. (Skip only if intent
   is already crisp.)
2. **★ Spec** — `write-spec` → `docs/devflow/<slug>/spec.md`. **Get approval.**
3. **Research** — `research-codebase` (and `source-grounded-research` for
   unfamiliar frameworks) → `research.md`.
4. **★ Plan** — `plan-in-phases` → `plan.md`. **Get approval** (the gate to build).
5. **Analyze** — `analyze-artifacts`: audit `spec` ↔ `research` ↔ `plan` for
   coverage, consistency, clarity, and constitution compliance. Resolve every
   **Critical** (route back to `write-spec` / `plan-in-phases`) before building.
6. **Build** — `subagent-driven-implementation` (or `incremental-implementation`),
   each task test-first via `test-driven-development`. Design skills
   (`api-and-interface-design`, `frontend-ui-engineering`) as the work needs.
7. **Verify** — `verify-before-done` across the whole change.
8. **Review** — `review-code` (two-axis); resolve Critical/Important findings.
9. **★ Ship** — `ship-it`: PR, green CI, staged rollout. **Get approval to merge.**
10. **Compound** — `compound-learnings` for anything non-obvious; update `CONTEXT.md`.

### Orchestration rules

- Respect the milestone gates — don't blow past an unapproved spec or plan.
- If requirements change, **rewind**: edit the earlier artifact and re-run from
  that phase (artifacts are checkpoints).
- Right-size ceremony to the change; a small feature can compress research.
- This orchestrator invokes model-invoked skills only — never another orchestrator.

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "Skip the spec, I'll just build." | The spec is the contract review measures against. Write it. |
| "Approval gates slow me down." | They prevent building the wrong thing for hours. Pause at ★. |
| "Compounding is optional." | It's the return arrow that makes the next feature faster. Do it. |
| "I'll keep artifacts in chat." | Chat evaporates; artifacts persist and rewind. Write them. |

## Red Flags

- Building with no approved `spec.md` or `plan.md`.
- Building while `analyze-artifacts` has an unresolved **Critical** finding.
- Loading an unpinned external resource or letting it replace a Devflow phase.
- Phases skipped silently rather than deliberately right-sized.
- No artifacts on disk under `docs/devflow/<slug>/`.
- The loop ended without compounding a real learning.

## Verification

- Each phase's own Verification section passed before the next began.
- Every named specialist gap has a recorded `USED`, `REJECTED`, or `SKIPPED`
  capability-hook decision.
- `spec.md`, `research.md`, `plan.md` exist and were approved at the ★ gates.
- The change is verified, reviewed, and shipped per those skills.
- A `solutions/` note (and any ADRs) captured the learnings.
