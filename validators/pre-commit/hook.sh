#!/usr/bin/env bash
#
# universal-spawn — git pre-commit hook
#
# Blocks the commit if any staged manifest at the repo root fails
# validation. Looks for the canonical filenames:
#   universal-spawn.{yaml,yml,json}
#   spawn.{yaml,yml,json}
#
# Install one of two ways:
#   1) Copy this file to .git/hooks/pre-commit and chmod +x.
#   2) Use the pre-commit framework (https://pre-commit.com) and reference
#      this script as a `local` hook (see snippet at the bottom).
#
# Requires: the `universal-spawn` CLI installed (Python or Node version).

set -euo pipefail

CLI="${UNIVERSAL_SPAWN_CLI:-universal-spawn}"

if ! command -v "$CLI" >/dev/null 2>&1; then
  echo "pre-commit: '$CLI' not on PATH. Install the universal-spawn CLI:"
  echo "  pip install universal-spawn        # Python"
  echo "  npm i -g universal-spawn           # Node"
  exit 1
fi

REPO_ROOT="$(git rev-parse --show-toplevel)"
cd "$REPO_ROOT"

CANDIDATES=(
  universal-spawn.yaml universal-spawn.yml universal-spawn.json
  spawn.yaml spawn.yml spawn.json
)

STAGED="$(git diff --cached --name-only --diff-filter=ACM)"
FAILED=0

for cand in "${CANDIDATES[@]}"; do
  if echo "$STAGED" | grep -qx "$cand"; then
    if "$CLI" validate "$cand"; then
      echo "pre-commit: $cand ok"
    else
      echo "pre-commit: $cand FAILED — fix the manifest or stash it"
      FAILED=1
    fi
  fi
done

exit "$FAILED"

# ---- pre-commit framework usage --------------------------------------
# Add this to .pre-commit-config.yaml:
#
#   repos:
#     - repo: local
#       hooks:
#         - id: universal-spawn
#           name: universal-spawn validate
#           entry: validators/pre-commit/hook.sh
#           language: script
#           pass_filenames: false
#           stages: [commit]
