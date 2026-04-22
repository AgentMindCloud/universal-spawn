# PlatformIO — universal-spawn platform extension

PlatformIO drives embedded builds via `platformio.ini`. A universal-spawn manifest pins the entry environment, the board, and the framework.

## What this platform cares about

The active environment, board, framework, and library deps.

## Compatibility table

| Manifest field | PlatformIO behavior |
|---|---|
| `version` | Required. |
| `type` | `firmware`, `library`, `cli-tool`. |
| `platforms.platform-io` | Strict. |

### `platforms.platform-io` fields

| Field | Purpose |
|---|---|
| `platforms.platform-io.entry_env` | platformio.ini env. |
| `platforms.platform-io.board` | Board id. |
| `platforms.platform-io.framework` | Framework. |
| `platforms.platform-io.libraries` | Library deps. |

See [`compatibility.md`](./compatibility.md) for more.
