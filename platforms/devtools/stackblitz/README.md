# StackBlitz — universal-spawn platform extension

StackBlitz runs Node.js in the browser via WebContainers. A universal-spawn manifest pins the project starter, the WebContainer node version, and the auto-open file.

## What this platform cares about

The starter id, the entry file, the auto-open file, and the Node.js version that should boot.

## Compatibility table

| Manifest field | StackBlitz behavior |
|---|---|
| `version` | Required. |
| `type` | `web-app`, `library`, `cli-tool`. |
| `platforms.stackblitz` | Strict. |

### `platforms.stackblitz` fields

| Field | Purpose |
|---|---|
| `platforms.stackblitz.starter` | Starter id. |
| `platforms.stackblitz.node_version` | Node version. |
| `platforms.stackblitz.open_file` | Auto-open file. |
| `platforms.stackblitz.terminal_command` | Initial terminal command. |
| `platforms.stackblitz.embed_view` | Embed view mode. |

See [`compatibility.md`](./compatibility.md) for more.
