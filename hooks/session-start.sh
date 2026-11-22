#!/bin/bash
# devflow session-start hook
# Injects the using-devflow router skill at the start of a session so the agent
# routes work to the right skill and phase. Optional: skills also activate by
# description and via /df-* commands without this hook.
#
# Output is plain text: Claude Code adds a SessionStart hook's stdout to the
# session context, but parses JSON output and drops fields it doesn't know.

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROUTER="$(dirname "$SCRIPT_DIR")/skills/using-devflow/SKILL.md"

if [ -f "$ROUTER" ]; then
  echo "devflow loaded. Route the task with using-devflow: pick the on-ramp (feature-workflow or fix-workflow), then follow the matching skill."
  echo
  cat "$ROUTER"
else
  echo "devflow: using-devflow router not found. Skills may still be available individually and via /df-* commands."
fi
