# AGENTS.md

Guidance for AI coding agents (GitHub Copilot, Claude Code, Cursor, Codex, and
others) operating in a repository where **Devflow** is installed.

Devflow is a set of composable **skills** (workflows), specialist **agents**
(review personas), and **slash commands** (entry points) that carry a change
through the full engineering lifecycle and compound what you learn back into the
next change.

## The loop

```
        ┌──────────────────────────── compound ◀───────────────────────┐
        ▼                                                               │
   align ─▶ spec ─▶ research ─▶ plan ─▶ build ─▶ verify ─▶ review ─▶ ship
   (grill)         (understand)        (TDD +                (2-axis)
                                        subagents)
```

Each phase produces a **durable artifact** under `docs/devflow/` (spec, research,
plan, solution notes). Artifacts are checkpoints: they accumulate context for the
next phase and are rewindable if requirements change. See
[docs/artifacts.md](docs/artifacts.md).

## Two on-ramps

Pick the entry point that matches the work:

- **Greenfield / new feature** → `feature-workflow` (`/df-feature`): align → spec
  → research → plan → build → verify → review → ship → compound. Full ceremony.
- **Brownfield / bug fix** → `fix-workflow` (`/df-fix`): reproduce → root-cause →
  minimal test-first fix → verify → review → ship → compound. Fast-path, shares
  the same underlying skills, less ceremony.

When unsure which applies, invoke the `using-devflow` router.

## Intent → skill mapping

Map the user's intent to a skill and invoke it **before** acting:

| Intent | Start with |
| --- | --- |
| "Let's build X" / new feature | `feature-workflow`, or `align-and-grill` then `write-spec` |
| Vague idea, not sure what to build | `idea-refine` |
| "Fix this bug" / failure / regression | `fix-workflow` or `debug-root-cause` |
| Nail down requirements | `align-and-grill` → `write-spec` |
| Understand existing code before changing it | `research-codebase` |
| Break a spec into tasks | `plan-in-phases` |
| Audit spec/plan before building (coverage, consistency, principles) | `analyze-artifacts` |
| Establish project principles / non-negotiables | `domain-modeling` → `constitution.md` |
| Implement a plan | `subagent-driven-implementation` (or `incremental-implementation`) |
| Write/modify behavior | `test-driven-development` |
| Design an API or module boundary | `api-and-interface-design` |
| UI work | `frontend-ui-engineering` |
| "Is it actually done?" | `verify-before-done` |
| Review a change before merge | `review-code` |
| Reduce complexity | `simplify-code` |
| Security-sensitive change | `security-hardening` |
| Performance concern | `performance-optimization` |
| Commit / open a PR / ship | `git-workflow` → `ship-it` |
| Address PR review comments | `resolve-pr-feedback` |
| Work PR review items one-by-one, isolated + approved | `pr-review-loop` |
| Capture a learning after solving something | `compound-learnings` |

## Orchestration: three layers

Devflow has three composable layers with different jobs — do not confuse them:

- **Skills** (`skills/<name>/SKILL.md`) — workflows with steps and exit criteria.
  The *how*. Mandatory when an intent matches.
- **Agents / personas** (`agents/<role>.md`) — a role with a perspective and an
  output format. The *who*.
- **Slash commands** (`/df-*`) — user-facing entry points. The *when*. The
  orchestration layer.

**Composition rule: the user (or a slash command) is the orchestrator.** A
persona may invoke skills, but **a persona never invokes another persona**, and a
user-invoked skill never invokes another user-invoked skill. The one endorsed
multi-persona pattern is **parallel fan-out with a merge step** (e.g. `review-code`
runs `code-reviewer` and `spec-auditor` concurrently, then synthesizes).

## Operating rules

1. **Check for a skill first.** If there is even a small chance a skill applies,
   invoke it before writing code, exploring the codebase, or asking questions.
2. **Follow the skill exactly.** If it has a checklist, make a to-do per item.
3. **Verification is non-negotiable.** No task is done without evidence — tests
   passing, build output, runtime data, or a written artifact at a known path.
4. **Compound the learning.** After solving something non-obvious, run
   `compound-learnings` so the next change starts smarter.

## Anti-rationalization

These thoughts are wrong. Ignore them:

| Thought | Reality |
| --- | --- |
| "This is too small for a skill." | Small things become big. Check first. |
| "I'll just implement it quickly." | The skill *is* the fast path to correct. |
| "I'll add tests later." | Later never comes. Tests come first. |
| "I'll gather context first." | Skills tell you *how* to gather context. |
| "Seems right." | Evidence, not vibes. Verify. |

## Platform notes

- **GitHub Copilot** — slash commands are in `.github/prompts/*.prompt.md`; repo
  instructions in `.github/copilot-instructions.md`. Copilot CLI installs the
  Claude-compatible plugin manifests in `.claude-plugin/`.
- **Claude Code** — commands in `.claude/commands/`, plugin in `.claude-plugin/`.
- **Codex / Cursor** — portable commands in `commands/*.toml`; plugin manifests in
  `.codex-plugin/` and `.cursor-plugin/`.
- **Harnesses without slash commands** — use the intent map above to reach skills
  by name.

See [docs/install.md](docs/install.md) for per-platform setup and
[docs/usage.md](docs/usage.md) for worked examples.

## Contributing to Devflow itself

If you are editing this repository (not just using it), every skill must follow
[docs/skill-anatomy.md](docs/skill-anatomy.md). Prefer extending an existing skill
over adding a near-duplicate.
