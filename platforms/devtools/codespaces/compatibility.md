# GitHub Codespaces compatibility — field-by-field

| universal-spawn v1.0 field | GitHub Codespaces behavior |
|---|---|
| `version` | Required. |
| `platforms.codespaces.devcontainer` | Path to devcontainer.json. |
| `platforms.codespaces.machine` | Default machine class. |
| `platforms.codespaces.prebuild` | Prebuild trigger. |
| `platforms.codespaces.forward_ports` | Auto-forwarded ports. |
| `platforms.codespaces.region` | Suggested region. |

## Coexistence with `.devcontainer/devcontainer.json`

universal-spawn does NOT replace .devcontainer/devcontainer.json. Both files coexist; consumers read both and warn on conflicts.

### `.devcontainer/devcontainer.json` (provider-native)

```json
{
  "image": "mcr.microsoft.com/devcontainers/typescript-node:20",
  "features": { "ghcr.io/devcontainers/features/github-cli:1": {} },
  "forwardPorts": [3000, 5432]
}
```

### `universal-spawn.yaml` (platforms.codespaces block)

```yaml
platforms:
  codespaces:
    devcontainer: .devcontainer/devcontainer.json
    machine: standardLinux32gb
    forward_ports: [3000, 5432]
```
