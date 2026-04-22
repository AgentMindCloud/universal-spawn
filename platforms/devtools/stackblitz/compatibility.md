# StackBlitz compatibility — field-by-field

| universal-spawn v1.0 field | StackBlitz behavior |
|---|---|
| `version` | Required. |
| `platforms.stackblitz.starter` | StackBlitz starter id. |
| `platforms.stackblitz.node_version` | Node version to boot. |
| `platforms.stackblitz.open_file` | File to open at first load. |
| `platforms.stackblitz.terminal_command` | Initial terminal command. |
| `platforms.stackblitz.embed_view` | Embed view (`editor`, `preview`, `both`). |

## Coexistence with `.stackblitzrc`

universal-spawn does NOT replace .stackblitzrc. Both files coexist; consumers read both and warn on conflicts.

### `.stackblitzrc` (provider-native)

```json
{
  "installDependencies": true,
  "startCommand": "pnpm dev",
  "env": { "NODE_VERSION": "20" }
}
```

### `universal-spawn.yaml` (platforms.stackblitz block)

```yaml
platforms:
  stackblitz:
    starter: vite
    node_version: "20"
    open_file: src/main.ts
    terminal_command: "pnpm dev"
```
