# CodeSandbox — universal-spawn platform extension

CodeSandbox runs sandboxes (browser-based code editors) and devboxes (microVMs). A universal-spawn manifest pins the kind, the entry template, and the optional `.codesandbox/` config directory.

## What this platform cares about

The `kind` (`sandbox`, `devbox`), the template id, and the config directory.

## Compatibility table

| Manifest field | CodeSandbox behavior |
|---|---|
| `version` | Required. |
| `type` | `web-app`, `container`, `workflow`. |
| `platforms.codesandbox` | Strict. |

### `platforms.codesandbox` fields

| Field | Purpose |
|---|---|
| `platforms.codesandbox.kind` | `sandbox` or `devbox`. |
| `platforms.codesandbox.template` | Template id. |
| `platforms.codesandbox.config_dir` | .codesandbox dir. |
| `platforms.codesandbox.preview_port` | Preview port. |

See [`compatibility.md`](./compatibility.md) for more.
