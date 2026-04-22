# Matrix — universal-spawn platform extension

Matrix is the federated messaging protocol. A universal-spawn manifest declares a bot or an Application Service (appservice) bridge with its registration YAML.

## What this platform cares about

The `kind` (`bot`, `appservice`), the homeserver, the bot/appservice id, and (for appservice) the registration YAML path and namespaces.

## Compatibility table

| Manifest field | Matrix behavior |
|---|---|
| `version` | Required. |
| `type` | `bot`, `extension`, `workflow`. |
| `platforms.matrix` | Strict. |

### `platforms.matrix` fields

| Field | Purpose |
|---|---|
| `platforms.matrix.kind` | `bot` or `appservice`. |
| `platforms.matrix.homeserver` | Homeserver URL. |
| `platforms.matrix.identifier` | MXID or appservice id. |
| `platforms.matrix.registration_file` | Registration YAML path. |
| `platforms.matrix.namespaces` | Appservice namespaces. |

See [`compatibility.md`](./compatibility.md) for more.
