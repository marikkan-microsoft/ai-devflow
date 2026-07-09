# Skill Anatomy

The single source of truth for how a Devflow skill is structured. Every skill in
`skills/` follows this format, and any new or edited skill must conform to it. If
you are authoring a skill (human or agent), read this first.

## What a skill is

A skill is a **workflow an agent follows**, not a reference doc it reads. It has
steps, checkpoints, and exit criteria. The test of a good skill: could an
enthusiastic junior engineer with no project context follow it and produce the
right outcome? If a section is background prose the agent would skim, cut it.

Skills encode **process discipline** — the judgment a senior engineer applies:
when to write a spec, what to test, how to review, when to ship. They are
opinionated and specific, never vague advice.

## File layout

```
skills/
  <kebab-case-name>/
    SKILL.md          # required — the workflow
    <supporting>.md   # optional — only when SKILL.md would exceed ~200 lines
```

- One skill per directory. Directory name = skill `name` = lowercase, hyphenated.
- Keep `SKILL.md` the entry point. Split supporting material into sibling files
  only when it is genuinely large and loaded on demand (progressive disclosure).
- Cross-project reference checklists live in `/references/`, not inside skills.

## Frontmatter

YAML frontmatter with exactly these fields:

```yaml
---
name: test-driven-development
description: Drives development with tests. Use when implementing any logic, fixing any bug, or changing any behavior.
disable-model-invocation: true   # optional — see below
---
```

Rules:

- **`name`** — matches the directory name exactly. Lowercase, hyphenated.
- **`description`** — one or two sentences. Start with what the skill does, in the
  third person ("Drives development with tests"), then the trigger conditions
  ("Use when …"). This description is the **only** thing an agent sees when
  deciding whether to invoke the skill, so make the triggers concrete.
- **`disable-model-invocation: true`** — add this **only** to *user-invoked*
  skills (orchestrators reachable via a `/df-*` command). It stops the model from
  auto-triggering the skill and reserves it for explicit user invocation. Omit it
  for *model-invoked* skills (the reusable discipline the agent reaches for
  automatically).

### The two invocation axes

| Kind | Frontmatter | Who invokes it | Job |
| --- | --- | --- | --- |
| **User-invoked** | `disable-model-invocation: true` | Only the user, via a `/df-*` command | Orchestrate — sequence model-invoked skills |
| **Model-invoked** | (omit the field) | The user *or* the agent, automatically when the task fits | Hold the reusable discipline |

A user-invoked skill may invoke model-invoked skills. A user-invoked skill must
**never** invoke another user-invoked skill. Orchestration flows one way.

## Section anatomy

Every `SKILL.md` has these sections, in this order:

### 1. `# Title` + `## Overview`
Two to four sentences: what the skill does and why it matters. State the core
principle the skill enforces.

### 2. `## When to Use`
A bulleted list of concrete triggers, plus an explicit **When NOT to use** line
and a **Related** line pointing at adjacent skills. Ambiguity here causes the
skill to fire at the wrong time.

### 3. `## Process`
The heart of the skill: numbered steps or a labelled cycle. Each step is an
action with an observable result. Include checkpoints ("stop and get approval"),
exact artifact paths, and commands where relevant. Diagrams (ASCII) are welcome
when they clarify a loop.

### 4. `## Common Rationalizations`
A two-column table of the excuses an agent uses to skip the process, paired with
the rebuttal. This is the anti-rationalization layer — it names the failure mode
so the agent catches itself.

| Rationalization | Reality |
| --- | --- |
| "I'll add the test afterwards." | Afterwards never comes. Write it first. |

### 5. `## Red Flags`
A short list of observable signs that the skill is being skipped or misapplied —
"you're rationalizing / off-track if …".

### 6. `## Verification`
The exit criteria. What **evidence** proves the work is done — tests passing,
build output, runtime data, a written artifact at a known path. "Seems right" is
never sufficient. Every skill ends here.

## Writing principles

- **Process, not prose.** If the agent would skim it, cut it.
- **Specific over general.** "Run the full test suite and paste the summary," not
  "make sure tests pass."
- **Evidence over claims.** Require artifacts, not assertions.
- **Minimal.** Only what is needed to guide the agent. Link, don't restate.
- **Composable.** Reference sibling skills by name (`test-driven-development`)
  rather than duplicating their content.
- **Durable artifacts.** When a skill produces a spec/research/plan/learning, it
  writes to a known path under `docs/devflow/` so later phases (and later runs)
  can build on it. See [artifacts.md](artifacts.md).

## Checklist before you ship a skill

- [ ] Directory name = `name` frontmatter, kebab-case.
- [ ] Description is third-person + concrete "Use when …" triggers.
- [ ] `disable-model-invocation: true` present iff the skill is user-invoked.
- [ ] All six sections present and in order.
- [ ] Rationalizations and Red Flags are real, not filler.
- [ ] Verification requires evidence.
- [ ] No duplicated content — references siblings and `/references/` instead.
