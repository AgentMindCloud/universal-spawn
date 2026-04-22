# Observable — universal-spawn platform extension

Observable hosts reactive notebooks and the Observable Framework (a static-site flavor of the same DAG runtime). A universal-spawn manifest covers both.

## What this platform cares about

The `kind` (`notebook`, `framework`), the notebook URL or Framework page path, and licensing.

## Compatibility table

| Manifest field | Observable behavior |
|---|---|
| `version` | Required. |
| `type` | `notebook`, `web-app`, `site`. |
| `platforms.observable` | Strict. |

### `platforms.observable` fields

| Field | Purpose |
|---|---|
| `platforms.observable.kind` | `notebook` or `framework`. |
| `platforms.observable.notebook_url` | Notebook URL. |
| `platforms.observable.framework_root` | Framework project root. |
| `platforms.observable.fork_protection` | Prompt before forking. |

See [`compatibility.md`](./compatibility.md) for more.
