# GitHub Copilot instructions — devflow

This repository uses **devflow**, a compounding development loop. As the coding
agent, route work through Devflow's skills instead of jumping straight to code.

## Start every task by routing

1. Decide the on-ramp:
   - **Bug / regression / broken behavior** → follow `skills/fix-workflow/SKILL.md`
     (or run `/df-fix`).
   - **New feature / non-trivial change** → follow `skills/feature-workflow/SKILL.md`
     (or run `/df-feature`).
   - **Small, well-understood change** → go straight to the matching phase skill.
2. Read accumulated context first: `docs/devflow/CONTEXT.md` and
   `docs/devflow/solutions/` if they exist.
3. Announce the skill you're following, then follow it exactly.

## The loop

`align → spec → research → plan → build (TDD) → verify → review → ship → compound`

Each phase writes a durable artifact under `docs/devflow/` (see
[docs/artifacts.md](../docs/artifacts.md)). Artifacts are rewindable checkpoints.

## Slash commands

Prompt files live in `.github/prompts/` and are invoked as `/df-*` in Copilot
Chat — e.g. `/df-feature`, `/df-fix`, `/df-spec`, `/df-plan`, `/df-build`,
`/df-review`, `/df-ship`, `/df-compound`. Full list mirrors the skills.

## Non-negotiables

- **Tests first.** Write a failing test before the code; reproduce bugs with a
  failing test before fixing (see `skills/test-driven-development/SKILL.md`).
- **Verify with evidence**, not vibes — run the full suite and the build before
  calling anything done (`skills/verify-before-done/SKILL.md`).
- **Review on two axes** before merge — spec compliance and code standards
  (`skills/review-code/SKILL.md`).
- **Compound the learning** after solving something non-obvious
  (`skills/compound-learnings/SKILL.md`).
- **Keep external specialists subordinate.** Use
  `skills/awesome-copilot-discovery/SKILL.md` only for a named capability gap;
  pin, audit, manually review, never execute bundled assets, then clean up.
- **Stop and ask** on ambiguous requirements or irreversible steps (auth,
  migrations, payments, deploys, secrets).

For the full operating manual, intent→skill map, and orchestration rules, read
[AGENTS.md](../AGENTS.md).
