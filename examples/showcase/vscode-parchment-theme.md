# Showcase · `parchment-theme` — a VS Code theme extension

**Use case.** A VS Code color theme in the Residual Frequencies
parchment palette. Works in VS Code, Cursor, Windsurf, VSCodium.

## The manifest

```yaml
version: "1.0"
name: Parchment Theme
description: >
  A VS Code color theme in the Residual Frequencies parchment
  palette. One theme entry; works in every VS Code fork.
type: extension
platforms:
  vscode:
    kind: extension
    publisher_id: parchment-studio
    extension_id: parchment-studio.parchment-theme
    min_vscode: "^1.90.0"
    forks: [vscode, cursor, windsurf, vscodium]
safety: { min_permissions: [], safe_for_auto_spawn: true }
env_vars_required: []
deployment: { targets: [vscode] }
visuals: { palette: parchment }
metadata:
  license: MIT
  id: com.parchment-studio.vscode-theme
  author: { name: Parchment Studio, handle: parchment-studio }
  source: { type: git, url: https://github.com/parchment-studio/vscode-parchment-theme }
```

## Platforms targeted, and why

- **`vscode`** — the Marketplace publishes once, every fork installs it.

## How discovery happens

Found via the VS Code Marketplace. The manifest declares which forks
the theme has been tested on, so a Cursor/Windsurf user trusts it
will look the same.
