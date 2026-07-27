# CLAUDE.md

This is the **devflow** project — a comprehensive, multi-platform agentic
engineering system for AI coding agents.

For how agents should *behave* when Devflow is installed (the loop, intent
mapping, orchestration rules), read [AGENTS.md](AGENTS.md). This file covers the
repository's structure and conventions for contributors.

## Project structure

```
skills/            → Skills (SKILL.md per directory) — the workflows
agents/            → Personas — build (software-engineer) + review (code-reviewer, spec-auditor, security-auditor, test-engineer, performance-auditor)
commands/          → Portable slash commands (*.toml) for Codex / Antigravity / Gemini
.claude/commands/  → Claude Code slash commands (*.md)
.github/prompts/   → GitHub Copilot prompt files (*.prompt.md)
.github/copilot-instructions.md → Copilot repo instructions
references/        → Cross-cutting checklists (definition-of-done, security, testing, performance, review)
templates/         → Starter templates for durable artifacts (spec, research, plan, solution, ADR, CONTEXT)
hooks/             → Optional session-start hook that loads the router skill
docs/              → Skill anatomy, artifacts spec, comparison, architecture, install, usage
.claude-plugin/    → Claude Code plugin + marketplace manifests (also read by Copilot CLI, Codex, Droid)
.codex-plugin/     → Codex plugin manifest
.cursor-plugin/    → Cursor plugin manifest
plugin.json        → Root manifest (Antigravity / generic)
```

## The loop (skills by phase)

- **Meta:** using-devflow (router), writing-devflow-skills
- **Align / Define:** align-and-grill, idea-refine, write-spec, domain-modeling
- **Research:** research-codebase, source-grounded-research
- **Plan:** plan-in-phases
- **Build:** subagent-driven-implementation, incremental-implementation,
  test-driven-development, api-and-interface-design, frontend-ui-engineering,
  context-engineering
- **Verify:** verify-before-done, debug-root-cause, browser-verification
- **Review:** review-code, simplify-code, security-hardening,
  performance-optimization
- **Ship:** git-workflow, ship-it, resolve-pr-feedback
- **Compound:** compound-learnings
- **Orchestrators:** feature-workflow (greenfield), fix-workflow (brownfield),
  autopilot

## Conventions

- Every skill lives in `skills/<name>/SKILL.md` with YAML frontmatter (`name`,
  `description`, optional `disable-model-invocation`).
- Description starts third-person, then trigger conditions ("Use when …").
- Every skill has: Overview, When to Use, Process, Common Rationalizations, Red
  Flags, Verification.
- User-invoked orchestrators set `disable-model-invocation: true` and get a
  `/df-*` command in all three command formats.
- Cross-cutting checklists go in `references/`, not inside skill directories.
- Supporting files inside a skill only when `SKILL.md` would exceed ~200 lines.
- [docs/skill-anatomy.md](docs/skill-anatomy.md) is the single source of truth for
  skill structure — follow it; don't restate it.

## Validate

- Check every `SKILL.md` has valid YAML frontmatter with `name` and `description`.
- Check `name` matches its directory.
- Check every `/df-*` command exists in `.claude/commands/`, `commands/`, and
  `.github/prompts/`.

## Boundaries

- **Always:** follow skill-anatomy.md for new skills; keep skills as process, not
  prose; require evidence in Verification.
- **Never:** add vague-advice skills; duplicate content between skills (reference
  instead); invoke a persona from another persona.
