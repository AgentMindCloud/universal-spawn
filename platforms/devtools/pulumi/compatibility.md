# Pulumi compatibility — field-by-field

| universal-spawn v1.0 field | Pulumi behavior |
|---|---|
| `version` | Required. |
| `platforms.pulumi.kind` | `program` or `component-package`. |
| `platforms.pulumi.runtime` | `nodejs`, `python`, `go`, `dotnet`, `java`. |
| `platforms.pulumi.project` | Pulumi project name. |
| `platforms.pulumi.stack` | Default stack name. |
| `platforms.pulumi.backend` | State backend. |
| `platforms.pulumi.registry` | Pulumi Registry namespace + name (component). |

## Coexistence with `Pulumi.yaml + Pulumi.<stack>.yaml`

universal-spawn does NOT replace Pulumi.yaml + Pulumi.<stack>.yaml. Both files coexist; consumers read both and warn on conflicts.

### `Pulumi.yaml + Pulumi.<stack>.yaml` (provider-native)

```yaml
name: your-infra
runtime: nodejs
description: Your infra
```

### `universal-spawn.yaml` (platforms.pulumi block)

```yaml
platforms:
  pulumi:
    kind: program
    runtime: nodejs
    project: your-infra
    stack: dev
    backend: service
```
