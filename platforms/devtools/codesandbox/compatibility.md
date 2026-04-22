# CodeSandbox compatibility — field-by-field

| universal-spawn v1.0 field | CodeSandbox behavior |
|---|---|
| `version` | Required. |
| `platforms.codesandbox.kind` | `sandbox`, `devbox`. |
| `platforms.codesandbox.template` | Template id. |
| `platforms.codesandbox.config_dir` | .codesandbox directory. |
| `platforms.codesandbox.preview_port` | Preview port. |

## Coexistence with `.codesandbox/`

universal-spawn does NOT replace .codesandbox/. Both files coexist; consumers read both and warn on conflicts.

### `.codesandbox/` (provider-native)

```json
{
  "template": "vite-react",
  "tasks": { "dev": { "command": "pnpm dev", "preview": { "port": 5173 } } }
}
```

### `universal-spawn.yaml` (platforms.codesandbox block)

```yaml
platforms:
  codesandbox:
    kind: sandbox
    template: vite-react
    preview_port: 5173
    config_dir: .codesandbox
```
