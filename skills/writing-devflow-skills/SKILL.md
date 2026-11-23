---
name: writing-devflow-skills
description: Guides authoring and editing Devflow skills so they stay consistent and effective. Use when creating a new skill, editing an existing one, or reviewing a skill contribution.
---

# Writing Devflow Skills

## Overview

Skills are the product. This meta-skill keeps them consistent: it walks you
through authoring or editing a skill to match [the skill anatomy](../../docs/skill-anatomy.md),
so every skill is a followable process with real anti-rationalizations and
evidence-based exit criteria — not vague advice.

## When to Use

- Creating a new skill or splitting/merging skills.
- Editing an existing skill's process, triggers, or verification.
- Reviewing a proposed skill contribution.

**When NOT to use:** Ordinary product work — that's what the other skills are for.

**Related:** [docs/skill-anatomy.md](../../docs/skill-anatomy.md) is the source of
truth for structure; this skill is the *process* for applying it.

## Process

### 1. Justify the gap

Before adding a skill, search the catalog. If an existing skill covers ~80% of the
idea, **extend it** instead of adding a near-duplicate. A new skill needs a
distinct trigger and a distinct process.

For a refinement proposed by `compound-learnings`, inspect its current evidence,
applicability, and counterexample, and obtain approval for the broader scope.
A recurring project-specific pattern is not automatically a shared rule; keep
it as a scoped note when the evidence does not generalize.

### 2. Choose the invocation axis

Decide: is this a **model-invoked** discipline (auto-reachable when the task fits —
omit the frontmatter flag) or a **user-invoked orchestrator** (sequences other
skills — set `disable-model-invocation: true` and give it a `/df-*` command)? A
user-invoked skill may call model-invoked skills, never another user-invoked one.

### 3. Write the frontmatter triggers concretely

`name` matches the directory (kebab-case). `description` = third-person purpose +
concrete "Use when …" triggers. The description is the *only* thing an agent sees
when deciding to invoke — vague triggers mean the skill fires at the wrong time or
never.

### 4. Draft as process, not prose

Fill the six sections in order: Overview, When to Use, Process, Common
Rationalizations, Red Flags, Verification. Steps must be actions with observable
results. Cut anything an agent would merely skim.

### 5. Make the guards real

The **Rationalizations** are the actual excuses an agent uses to skip this
process, each with a rebuttal. The **Red Flags** are observable "you're off-track"
signs. The **Verification** demands evidence. Filler here defeats the point.

### 6. Keep it minimal and composable

Reference sibling skills and `/references/` instead of duplicating. Split content
into supporting files only when `SKILL.md` would exceed ~200 lines. Produce
durable artifacts to known paths where relevant.

### 7. Test the trigger and the flow

For behavioral changes, use the shared
[skill evaluations](../../references/skill-evaluation.md): define a bounded
capability/regression case and its observable criteria before editing, record
the baseline, then exercise the affected candidate behavior. Inspect actual
actions and artifacts, not just matching prose. Record unavailable host evidence
as unverified; do not install a runner or launch unapproved repeat trials.

Wording-only edits need the existing structural/link checks, not fresh agent
runs. A matching request should still trigger the skill, and its process should
remain followable to a verified outcome.

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "This deserves its own skill." | Most ideas extend an existing one. Justify the gap first. |
| "The description can be short and generic." | Then it won't trigger correctly. Make the triggers concrete. |
| "Rationalizations/Red Flags are filler." | They're the anti-skip layer. Make them real or the skill leaks. |
| "Verification can be 'looks done'." | Every skill ends in evidence. No exceptions. |

## Red Flags

- The new skill overlaps an existing one by most of its process.
- Sections are prose to read, not steps to follow.
- Rationalizations/Red Flags are generic platitudes.
- Verification asks for confidence, not evidence.
- A structural test or an agent's summary is presented as observed workflow behavior.

## Verification

- The skill matches [skill-anatomy.md](../../docs/skill-anatomy.md): all six
  sections, correct frontmatter, correct invocation axis.
- Triggers are concrete; the gap over existing skills is justified.
- Rationalizations, Red Flags, and Verification are specific and evidence-based.
- No duplicated content — siblings and references are linked.
- Affected behavior has baseline/candidate receipts under the shared evaluation
  procedure; structural checks and remaining human acceptance are explicit.
