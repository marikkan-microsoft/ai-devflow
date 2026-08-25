# devflow

**The compounding development loop for coding agents.**

Devflow gives your AI coding agent a complete engineering workflow: composable
**skills**, specialist **agents**, and slash **commands** that carry a
change from intent to shipped — and fold what you learn back into the next change.
It works for **greenfield features** and **brownfield bug fixes**, on **GitHub
Copilot, Claude Code, Cursor, Codex**, and more.

```
        ┌──────────────────────────── compound ◀───────────────────────┐
        ▼                                                               │
   align ─▶ spec ─▶ research ─▶ plan ─▶ build ─▶ verify ─▶ review ─▶ ship
  (grill)         (understand)         (TDD +               (2-axis)
                                        subagents)
```

Each phase writes a **durable, rewindable artifact**. The return arrow is the
point: solved problems become notes that make the next run smarter.

> Devflow synthesizes six excellent open-source systems into one opinionated
> loop. See **[docs/comparison.md](docs/comparison.md)** for who does what and
> what Devflow borrows from each.

---

## Quick start

Install into (almost) any agent with the universal installer:

```bash
npx skills add marikkan-microsoft/ai-devflow
```

Then, in your agent, start a task:

```text
/df-feature   add per-user rate limiting to the public API   # greenfield
/df-fix       the checkout webhook creates duplicate invoices  # brownfield
```

…or just describe your task and let `/df` route it. **GitHub Copilot users** and
every other platform: see **[docs/install.md](docs/install.md)** (native plugins,
prompt files, and manual folder-copy install for each tool).

> Commands use `marikkan-microsoft/ai-devflow`. If you fork this repo, swap in
> your own `owner/repo`.

---

## Why devflow

- **Two on-ramps.** `/df-feature` runs the full loop with approval gates;
  `/df-fix` is a leaner bug-fix fast-path. Same skills underneath.
- **Durable, rewindable artifacts.** Spec, research, and plan live under
  `docs/devflow/` in git — checkpoints you can rewind to. *(inspired by PAW)*
- **Knowledge compounds.** `compound-learnings` writes `solutions/` notes that
  ground the next run. *(inspired by compound-engineering)*
- **Subagent-driven build.** A fresh subagent per task with a two-stage review —
  spec compliance, then code quality. *(inspired by superpowers)*
- **Evidence, not vibes.** Every skill ends in a verification gate; nothing is
  "done" without proof. *(inspired by agent-skills)*
- **Checked before you build.** `analyze-artifacts` audits spec↔plan for coverage
  and consistency, and a per-project `constitution.md` holds binding principles —
  caught in the plan, not the pull request. *(inspired by Spec Kit)*
- **Alignment first.** `align-and-grill` interviews you one question at a time,
  and `domain-modeling` builds a shared `CONTEXT.md`. *(inspired by mattpocock)*
- **Specialists on demand.** A workflow stage with a named capability gap can
  discover one Awesome Copilot skill or agent, pin and audit it, use only its
  bounded guidance, then discard it.
- **Portable & minimal.** One `SKILL.md`-first source; small, composable skills;
  orchestration flows one way.

---

## What's inside

- **32 skills** across `align → spec → research → plan → build → verify → review →
  ship → compound`, plus three orchestrators (`feature-workflow`, `fix-workflow`,
  `autopilot`). Full list: **[skills catalog](skills/README.md)**.
- **6 personas** — one implementer, `software-engineer`, plus five reviewers:
  `code-reviewer`, `spec-auditor`, `security-auditor`, `test-engineer`,
  `performance-auditor` (`agents/`).
- **Slash commands** in three native formats — Claude (`.claude/commands/`),
  portable TOML (`commands/`), and Copilot prompt files (`.github/prompts/`).
- **Reference checklists** and **artifact templates** (`references/`, `templates/`).

```
skills/        agents/        commands/       references/     templates/      tests/
.claude/       .github/       .claude-plugin/ .codex-plugin/  .cursor-plugin/
hooks/         docs/          AGENTS.md        CLAUDE.md       plugin.json
```

---

## On-demand Awesome Copilot specialists

Devflow does not bundle the broad
[Awesome Copilot](https://github.com/github/awesome-copilot) catalog. Instead,
relevant phases expose a **conditional capability hook**: when the local skills
have a concrete gap, `awesome-copilot-discovery` searches live skill and agent
metadata, resolves the catalog to a full commit SHA, and considers at most one
complementary resource.

The trust boundary is strict:

1. Search metadata before loading a candidate body.
2. Fetch one exact `github/awesome-copilot:path@sha` into a temporary directory.
3. Verify its catalog identity, paths, file count, size, and Git blob digests.
4. Statically audit it, then manually review every file and finding.
5. Use only the relevant process or specialist perspective. Remote instructions
   cannot change Devflow's scope, tools, approvals, tests, or review gates.
6. Never execute downloaded scripts, hooks, binaries, install commands, or MCP
   servers; delete the staging directory after the phase.

For example, a security phase can discover a prompt-supply-chain reviewer or a
threat-modeling skill without permanently installing either:

```bash
python3 skills/awesome-copilot-discovery/scripts/awesome_copilot.py discover \
  --phase security \
  --query "prompt injection and threat modeling" \
  --kind all
```

The bridge is optional and requires Python 3.9+, an authenticated
[GitHub CLI](https://cli.github.com/), and network access. If any is unavailable,
the hook records `SKIPPED` and continues with local Devflow; existing safeguards
are never disabled. See
[`awesome-copilot-discovery`](skills/awesome-copilot-discovery/SKILL.md) and its
[trust policy](skills/awesome-copilot-discovery/references/trust-policy.md).

---

## Documentation

| Doc | What it covers |
| --- | --- |
| [docs/install.md](docs/install.md) | Install on Copilot, Claude, Cursor, Codex, and others (native + manual). |
| [docs/usage.md](docs/usage.md) | Worked examples for both on-ramps and single skills. |
| [docs/architecture.md](docs/architecture.md) | The design: the loop, layers, artifacts, principles. |
| [docs/comparison.md](docs/comparison.md) | How the five source systems compare and what Devflow curates. |
| [docs/artifacts.md](docs/artifacts.md) | The durable-artifact contracts and rewind model. |
| [docs/skill-anatomy.md](docs/skill-anatomy.md) | How a skill is structured (for contributors). |
| [AGENTS.md](AGENTS.md) | The agent operating manual (intent map, orchestration rules). |

---

## How a skill works

Every skill is a **process, not prose** — steps, checkpoints, and exit criteria:

```
SKILL.md
├─ frontmatter: name + description ("Use when …")
├─ Overview            — what it does, the principle it enforces
├─ When to Use         — concrete triggers (+ when NOT to)
├─ Process             — numbered steps with observable results
├─ Common Rationalizations — the excuse + the rebuttal
├─ Red Flags           — "you're off-track if …"
└─ Verification        — the evidence that proves it's done
```

---

## Credits

Devflow stands on the shoulders of six outstanding, MIT-licensed projects. If an
idea here resonates, read the original in full:

- [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) — lifecycle discipline, anti-rationalization, verification gates.
- [mattpocock/skills](https://github.com/mattpocock/skills) — grilling, domain models, composable design.
- [EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin) — the compounding-knowledge loop and autopilot.
- [lossyrob/phased-agent-workflow](https://github.com/lossyrob/phased-agent-workflow) — durable, rewindable artifacts and PR-integrated review.
- [obra/superpowers](https://github.com/obra/superpowers) — subagent-driven development and two-stage review.
- [github/spec-kit](https://github.com/github/spec-kit) — spec-driven development; the pre-build cross-artifact `analyze-artifacts` gate and the project `constitution`.

Devflow also integrates with
[github/awesome-copilot](https://github.com/github/awesome-copilot) as an
on-demand, pinned specialist catalog. Its resources are inspected at runtime,
not vendored or trusted implicitly.

## License

[MIT](LICENSE). Use it, fork it, make it your own.
