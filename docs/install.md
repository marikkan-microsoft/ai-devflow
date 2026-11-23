# Installing devflow

Devflow is **SKILL.md-first**: one source of truth in `skills/` that installs
across every major coding agent. You can install it three ways —

1. **Universal installer** (`npx skills`) — one command, 70+ agents.
2. **Native plugin** — manifests are provided for Copilot/Claude, Cursor, and
   Codex; capabilities differ by host and installation route.
3. **Manual folder copy** — copy the folders into your agent's config. Everything
   is plain files; only the copied capabilities are configured.

> **Before you start:** the commands below install from
> `marikkan-microsoft/ai-devflow`. If you forked this repo, replace it with your
> own `owner/repo`. If you're installing from a local clone, use the manual or
> local-path methods.

---

## Quick start (any agent)

The open [`skills` CLI](https://github.com/vercel-labs/skills) installs Devflow
into Claude Code, Cursor, Copilot, Codex, Cline, Windsurf, and more:

```bash
npx skills add marikkan-microsoft/ai-devflow          # install everything
npx skills add marikkan-microsoft/ai-devflow --list   # browse first
npx skills add marikkan-microsoft/ai-devflow --skill review-code   # just one
```

Then start any task with `/df` (or ask the agent to "route this with devflow").

The optional `awesome-copilot-discovery` capability hook also needs Python 3.9+,
an authenticated GitHub CLI, and network access. Without them, Devflow records
the specialist lookup as skipped and continues with its local skills.

---

## Capability and evidence matrix

**Declared** means the repository supplies that surface, not that every host
version has been exercised. **Observed** is limited to the named version and
route. **Not configured** describes this package/route, not a limitation of the
host itself. When automatic loading is unavailable, follow the canonical skill
by name and retain the same approval and verification gates.

| Host / route | Skills and commands declared | Startup router hook | Runtime evidence / fallback |
| --- | --- | --- | --- |
| Copilot CLI, local `--plugin-dir` | [Claude-compatible manifest](../.claude-plugin/plugin.json): skills, personas, command directory | [Hook supplied](../hooks/hooks.json); host ingestion unverified | CLI **1.0.114**, Linux, 2026-11-23: local plugin discovery and `using-devflow`, research, plan, and verification skill loading observed. This does not certify marketplace installation, command expansion, or startup-hook ingestion. |
| Copilot CLI / VS Code, native plugin | Same Claude-compatible manifest | Supplied; ingestion depends on host/route | Marketplace and VS Code runtime **unverified** in this check. Use the existing commands or invoke the skill by name after confirming discovery. |
| Copilot VS Code, prompt-file copy | [Prompt files](../.github/prompts/) and instructions; skills only if also copied | Not configured by this copy recipe | Runtime **unverified**; use prompt files or canonical skill guidance. |
| Claude Code, native plugin | Claude-compatible manifest: skills, personas, command directory | Supplied; native ingestion **unverified** here | Runtime **unverified**; shell-output checks are not a Claude session receipt. |
| Cursor, native plugin | [Cursor manifest](../.cursor-plugin/plugin.json): skills; no command directory declared | Not configured by this manifest | Runtime **unverified**; manual command-copy route is separate. |
| Codex, native plugin | [Codex manifest](../.codex-plugin/plugin.json): skills; no command directory declared | Explicitly empty hook map | Runtime **unverified**; portable TOML commands are separate content, not proof this manifest loads them. |
| Universal installer / other manual routes | Only what the installer or copy recipe exposes to that host | Do not assume hooks accompany installed skills | Runtime **unverified** per route/version; check the host's current contract and invoke available skills directly. |

The local CLI observation used a fresh, isolated profile and a pinned Devflow
snapshot; it is an observation of that route, not a cross-host guarantee. The
[startup-hook tests](../tests/test_session_start_hook.py) exercise plain stdout,
an installation path with spaces, and missing-router fallback on Linux. They
do not establish native-host ingestion or Windows support.

Before upgrading a row to observed, record host/version, installation route,
loaded revision, actual command/skill result, and a hook receipt if claimed.
Keep missing capabilities explicit; do not install another runtime to make a
support claim pass.

---

## GitHub Copilot  ⭐ (primary target)

### VS Code

**Option A — prompt files + instructions (no plugin system needed).** Copy into
your project:

```bash
mkdir -p .github/prompts
cp -r path/to/devflow/.github/prompts/*.prompt.md .github/prompts/
cp path/to/devflow/.github/copilot-instructions.md .github/
cp -r path/to/devflow/skills .github/skills   # optional: skills for auto-activation
```

Reload VS Code. In Copilot Chat, run `/df-feature`, `/df-fix`, `/df-plan`, etc.
`copilot-instructions.md` orients Copilot to route through Devflow automatically.

**Option B — install the plugin from source.** Run **`Chat: Install Plugin from
Source`** from the Command Palette, point it at this repo, and select `devflow`.
Copilot reads the Claude-compatible manifests in `.claude-plugin/`.

### Copilot CLI

```bash
copilot plugin marketplace add marikkan-microsoft/ai-devflow
copilot plugin install devflow@devflow
```

Manage with `copilot plugin list`, `copilot plugin update devflow`,
`copilot plugin uninstall devflow`.

---

## Claude Code

**Marketplace (recommended):**

```text
/plugin marketplace add marikkan-microsoft/ai-devflow
/plugin install devflow@devflow
```

**Or the universal installer:** `npx skills add marikkan-microsoft/ai-devflow`.

Commands appear as `/df-*`; the session-start hook (optional) loads the router.

---

## Cursor

**Plugin marketplace** — in Cursor Agent chat:

```text
/add-plugin devflow
```

…or search "devflow" in the plugin marketplace. **Or** use
`npx skills add marikkan-microsoft/ai-devflow`, which writes Cursor-native files.

---

## Codex (App + CLI)

**Codex CLI:**

```bash
codex plugin marketplace add marikkan-microsoft/ai-devflow
codex plugin add devflow@devflow
```

**Codex App:** open **Plugins** in the sidebar → **Add plugin marketplace** →
source `marikkan-microsoft/ai-devflow`, ref `main` → install `devflow`, then
restart Codex. Portable commands ship as `commands/*.toml`.

---

## Other agents (Windsurf, Antigravity/Gemini, OpenCode, Kimi, Qwen, Droid …)

Use the universal installer — it targets all of them:

```bash
npx skills add marikkan-microsoft/ai-devflow
```

For harnesses that read a repo `AGENTS.md`, copying `AGENTS.md` + `skills/` into
the project is enough for the agent to follow the loop by name (see manual copy).

---

## Manual install (folder copy)

Everything in Devflow is plain files. Copy the folders your agent understands:

| Agent | Copy into |
| --- | --- |
| **Claude Code** (project) | `skills/` → `.claude/skills/`, `agents/` → `.claude/agents/`, `.claude/commands/` → `.claude/commands/` |
| **Claude Code** (global) | same, under `~/.claude/` |
| **Copilot (VS Code)** | `.github/prompts/` and `.github/copilot-instructions.md` → your repo's `.github/`; `skills/` → `.github/skills/` |
| **Cursor** | `skills/` → `.cursor/skills/`; `.claude/commands/` → `.cursor/commands/` (or use the plugin) |
| **Codex** | `skills/` and `commands/*.toml` → your Codex plugin/config dir |
| **Any AGENTS.md agent** | `AGENTS.md`, `skills/`, `agents/`, `references/`, `templates/` → repo root |

Exact directories vary by tool version — check your agent's docs for its skills/
commands path. The **canonical content is always `skills/`**; commands and prompt
files are thin wrappers over it.

---

## Optional: auto-load the router at session start

Harnesses that support session hooks (e.g. Claude Code) can auto-inject the
`using-devflow` router. The hook is wired in [`hooks/hooks.json`](../hooks/hooks.json)
and runs [`hooks/session-start.sh`](../hooks/session-start.sh).
Loading depends on the host and installation route; the manifest or a successful
shell check alone does not prove injection. Without it, invoke `using-devflow`
or a matching skill directly, or use the commands your route exposes.

---

## Verify your install

Ask the agent: **"What Devflow skills are available?"** or run **`/df`** and give
it a task. It should announce an on-ramp (`feature-workflow` or `fix-workflow`)
and follow the matching skill. See [usage.md](usage.md) for worked examples.
