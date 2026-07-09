#!/bin/bash
# devflow session-start hook
# Injects the using-devflow router skill at the start of a session so the agent
# routes work to the right skill and phase. Optional: skills also activate by
# description and via /df-* commands without this hook.

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROUTER="$(dirname "$SCRIPT_DIR")/skills/using-devflow/SKILL.md"

if ! command -v jq >/dev/null 2>&1; then
  echo '{"priority": "INFO", "message": "devflow: jq is required for the session-start hook but was not found on PATH. Install jq (e.g. `brew install jq` or `apt-get install jq`) to enable router injection. Skills remain available individually and via /df-* commands."}'
  exit 0
fi

if [ -f "$ROUTER" ]; then
  CONTENT=$(cat "$ROUTER")
  jq -cn \
    --arg message "devflow loaded. Route the task with using-devflow: pick the on-ramp (feature-workflow or fix-workflow), then follow the matching skill.

$CONTENT" \
    '{priority: "IMPORTANT", message: $message}'
else
  echo '{"priority": "INFO", "message": "devflow: using-devflow router not found. Skills may still be available individually and via /df-* commands."}'
fi
