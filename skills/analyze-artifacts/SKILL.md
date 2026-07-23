---
name: analyze-artifacts
description: Read-only cross-artifact audit that checks spec, research, and plan for coverage, consistency, and clarity before any code is written. Use as the gate between an approved plan and the build — or whenever spec/plan artifacts may have drifted out of sync.
---

# Analyze Artifacts

## Overview

The cheapest defect is the one caught in the plan, not the pull request. This
skill runs a **read-only, pre-build audit across `spec.md` → `research.md` →
`plan.md`** (against `CONTEXT.md` and the project `constitution.md`) to catch
coverage holes, contradictions, and ambiguity *before* a single line is written.
It is the artifact-level twin of `review-code`: `review-code` audits the diff
*after* the build; this audits the plan *before* it.

**Core principle:** measure twice, cut once. The skill **writes nothing** — it
reports findings and proposes fixes; the fixes go back through `write-spec` /
`plan-in-phases`. A **Critical** finding blocks the build.

## When to Use

- As the gate **after `plan-in-phases`** (plan `approved` or `draft`) and
  **before** `subagent-driven-implementation` / `incremental-implementation`.
- When the spec or plan is large, high-risk, or was **rewound** and edited (the
  artifacts may no longer agree).
- When a plan was generated autonomously and hasn't been cross-checked.

**When NOT to use:** A single-slice change with one task, or a bug fix (use
`fix-workflow`). Don't audit artifacts that don't exist yet — write them first.

**Related:** Consumes `spec.md`, `research.md`, `plan.md`, `CONTEXT.md`, and
`constitution.md`. Complements `review-code` (post-build). Runs inside
`feature-workflow` between the Plan ★ gate and Build. Findings route back to
`write-spec` / `plan-in-phases`.

## Process

### 1. Fix the scope and load the artifacts

Load `docs/devflow/<slug>/spec.md`, `research.md`, `plan.md`, plus
`docs/devflow/CONTEXT.md` and `docs/devflow/constitution.md` if they exist. If any
required artifact is missing, stop and route to the skill that produces it.

### 2. Coverage — bidirectional traceability

Build a coverage table mapping every spec `R#`/`SC#` to the task(s) that satisfy
it, and every task back to a requirement:

- **Uncovered requirement** — an `R#`/`SC#` with **zero** tasks → Critical.
- **Orphan task** — a task that satisfies no `R#`/`SC#` → Important (scope creep or
  a missing requirement).
- **Buildable success criteria** — an `SC#` that needs real work (a performance,
  security, or availability target) but has no task or verification step →
  Critical. (Post-launch business KPIs are exempt — they aren't build work.)

### 3. Consistency — do the artifacts agree?

- **Terminology drift** — the same concept named differently across spec/plan, or
  diverging from `CONTEXT.md`'s glossary → Important.
- **Contradictions** — the plan assumes something the spec forbids (or two tasks
  conflict) → Critical.
- **Phantom entities** — a data entity/module in the plan that the spec never
  introduced → Important.
- **Ordering** — a task depends on work sequenced after it → Important.

### 4. Clarity — is anything still vague?

- Unresolved `[NEEDS CLARIFICATION: …]` in the spec → Critical (the spec should not
  be `approved` with these open).
- Vague adjectives with no measurable criterion ("fast", "scalable", "secure",
  "intuitive") in requirements or success criteria → Important.
- Placeholders (`TODO`, `TKTK`, `???`, `<…>`) left in any artifact → Important.

### 5. Principles — constitution alignment

If `constitution.md` exists, check every requirement, plan decision, and task
against it. A conflict with a **NON-NEGOTIABLE / MUST** principle is **Critical**
and must be resolved by changing the spec/plan — never by quietly diluting the
principle. A conflict with a lower principle is Important unless justified in the
plan's Risks/Complexity note.

### 6. Report, verdict, and remediation

Emit one report:

- **Findings table:** ID · Category · Severity (Critical / Important / Suggestion)
  · Location (`file:section`) · Recommended fix.
- **Coverage table:** `R#`/`SC#` → task IDs → covered? → note.
- **Metrics:** total requirements, total tasks, coverage %, unresolved
  clarifications, contradictions, Critical count.
- **Verdict:** **READY TO BUILD** (no Critical) or **NOT READY** (≥1 Critical).

Remediation is a **proposal only** — this skill never edits artifacts. Route
Critical/Important findings to `write-spec` / `plan-in-phases`, then re-run this
audit. Proceed to build only on a READY verdict.

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "The plan looks fine, just start building." | Looks-fine plans hide uncovered requirements. Trace them. |
| "Review after the code is written covers this." | That's hours later and a bigger diff. Catch it in the plan. |
| "Every requirement is obviously covered." | Then the coverage table costs minutes and proves it. |
| "A vague success criterion is good enough." | Unmeasurable = unverifiable. Flag it now, not at verify time. |
| "I'll just tweak the plan myself while I'm here." | This skill is read-only. Fixes go through the owning skill, then re-audit. |
| "One Critical is fine, I'll fix it during build." | Critical means NOT READY. Resolve, re-audit, then build. |

## Red Flags

- You started `subagent-driven-implementation` with an open Critical finding.
- No coverage table was produced — you asserted coverage instead of tracing it.
- You edited `spec.md`/`plan.md` from inside this skill.
- A success criterion has no task and no verification step.
- Terminology in the plan doesn't match `CONTEXT.md` and it was waved through.

## Verification

- A findings report and a bidirectional coverage table exist.
- Every `R#`/`SC#` maps to a task (or is explicitly deferred); no orphan tasks.
- No unresolved `[NEEDS CLARIFICATION]`, and no MUST-principle conflicts remain.
- A clear verdict (READY TO BUILD / NOT READY) is stated, and the build did not
  start while any Critical was open.
