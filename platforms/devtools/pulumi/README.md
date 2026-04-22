# Pulumi — universal-spawn platform extension

Pulumi programs declare cloud resources in real code (TypeScript, Python, Go, C#). Reusable component packages publish to the Pulumi Registry. A universal-spawn manifest picks program-vs-component and the language.

## What this platform cares about

The `kind` (`program`, `component-package`), the language, the project name, and the backend.

## Compatibility table

| Manifest field | Pulumi behavior |
|---|---|
| `version` | Required. |
| `type` | `workflow`, `library`, `container`. |
| `platforms.pulumi` | Strict. |

### `platforms.pulumi` fields

| Field | Purpose |
|---|---|
| `platforms.pulumi.kind` | `program` or `component-package`. |
| `platforms.pulumi.runtime` | `nodejs`, `python`, `go`, `dotnet`, `java`. |
| `platforms.pulumi.project` | Pulumi project name. |
| `platforms.pulumi.stack` | Default stack. |
| `platforms.pulumi.backend` | State backend. |
| `platforms.pulumi.registry` | Pulumi Registry namespace + name. |

See [`compatibility.md`](./compatibility.md) for more.
