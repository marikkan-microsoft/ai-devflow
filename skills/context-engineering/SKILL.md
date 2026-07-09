---
name: context-engineering
description: Feeds the agent the right information at the right time — rules files, context packing, and tool/MCP integration. Use when starting a session, switching tasks, or when output quality drops because the agent lacks or is drowning in context.
---

# Context Engineering

## Overview

An agent is only as good as the context it's given. This skill manages what the
agent knows at each moment: loading the right grounding (specs, research,
`CONTEXT.md`, solutions), trimming noise, and wiring the tools/MCP servers that
supply live facts. Too little context causes hallucination; too much drowns the
signal. Both are failures this skill prevents.

## When to Use

- Starting a session or switching to a new task.
- Output quality drops, the agent forgets constraints, or it invents facts.
- After a compaction/handoff, to reconstitute the right working set.
- Setting up rules files or tool/MCP access for a project.

**When NOT to use:** A short, self-contained task where the needed context is
already present.

**Related:** Reads all `docs/devflow/` artifacts. Pairs with `research-codebase`
(internal facts) and `source-grounded-research` (external facts). `handoff`-style
compaction feeds this on resume.

## Process

### 1. Identify what the task needs

Name the minimum facts required: the spec/plan, the specific code paths, the
domain vocabulary, and the external docs. Everything else is noise for now.

### 2. Load grounding deliberately

Pull in `CONTEXT.md`, the relevant `spec.md`/`research.md`/`plan.md`, and matching
`solutions/` entries. Prefer precise slices (a function, a section) over whole
files. Progressive disclosure: load supporting detail only when reached.

### 3. Wire the right tools

Ensure the tools and MCP servers that provide live truth are available (test
runner, browser/DevTools, docs, issue tracker). A fact the agent can *fetch*
beats a fact it must *remember*.

### 4. Trim the noise

Drop stale, irrelevant, or duplicated context. If the working set has grown
sprawling and the agent is drifting, compact: summarize decisions so far into a
handoff note and reset to the essentials.

### 5. Re-ground on drift

When quality drops mid-task, stop and reload the anchoring artifacts rather than
pushing on with a degraded context.

## Common Rationalizations

| Rationalization | Reality |
| --- | --- |
| "More context is always safer." | Noise buries the signal and degrades output. Load deliberately. |
| "I'll rely on what I remember." | Memory drifts; artifacts don't. Re-ground from files. |
| "Setting up tools is overhead." | Fetchable facts beat remembered ones. Wire them once. |
| "I'll push through the confusion." | Confusion compounds. Stop and re-ground. |

## Red Flags

- The agent contradicts a spec/`CONTEXT.md` it should be following.
- It's inventing APIs or file paths (missing or wrong context).
- The context window is full of stale, unrelated material.
- Quality is dropping and no one re-grounded.

## Verification

- The task's required grounding is loaded and the noise is trimmed.
- Needed tools/MCP servers are available and working.
- The agent's outputs are consistent with the loaded artifacts.
- On drift, context was re-grounded from files rather than guessed.
