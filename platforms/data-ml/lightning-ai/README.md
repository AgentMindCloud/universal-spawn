# Lightning AI — universal-spawn platform extension

Lightning AI runs Studios — cloud dev environments that pair a notebook + terminal + jobs runner. A universal-spawn manifest pins the Studio template, machine class, and default app entry.

## What this platform cares about

The Studio template, the machine class (CPU/GPU), and the entry app or notebook.

## Compatibility table

| Manifest field | Lightning AI behavior |
|---|---|
| `version` | Required. |
| `type` | `notebook`, `workflow`, `web-app`. |
| `platforms.lightning-ai` | Strict. |

### `platforms.lightning-ai` fields

| Field | Purpose |
|---|---|
| `platforms.lightning-ai.template` | Studio template. |
| `platforms.lightning-ai.machine` | Machine class. |
| `platforms.lightning-ai.entry_file` | Entry file. |
| `platforms.lightning-ai.team_id` | Lightning team id. |

See [`compatibility.md`](./compatibility.md) for more.
