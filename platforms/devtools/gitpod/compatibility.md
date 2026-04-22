# Gitpod compatibility — field-by-field

| universal-spawn v1.0 field | Gitpod behavior |
|---|---|
| `version` | Required. |
| `platforms.gitpod.image` | Workspace image. |
| `platforms.gitpod.tasks` | Tasks Gitpod runs at start. |
| `platforms.gitpod.ports` | Exposed ports config. |
| `platforms.gitpod.tier` | Workspace tier. |
| `platforms.gitpod.tools` | Pre-installed tools (vscode, ssh). |

## Coexistence with `.gitpod.yml`

universal-spawn does NOT replace .gitpod.yml. Both files coexist; consumers read both and warn on conflicts.

### `.gitpod.yml` (provider-native)

```yaml
image: gitpod/workspace-full:latest
tasks:
  - name: install
    init: pnpm install
    command: pnpm dev
ports:
  - port: 3000
    visibility: public
    onOpen: open-preview
```

### `universal-spawn.yaml` (platforms.gitpod block)

```yaml
platforms:
  gitpod:
    image: gitpod/workspace-full:latest
    tasks:
      - { name: install, init: "pnpm install", command: "pnpm dev" }
    ports:
      - { port: 3000, visibility: public, on_open: open-preview }
    tier: standard
```
