# VS Code — universal-spawn platform extension

VS Code has two independent spawn surfaces: Marketplace extensions (via `package.json` + VS Code-specific contrib points) and Dev Containers (via `.devcontainer/devcontainer.json`). A universal-spawn manifest picks exactly one via `kind` and maps into the native config.

## What this platform cares about

The `kind` (`extension`, `devcontainer`), publisher id + extension id (for extensions), the DevContainer image and features (for devcontainers), and the target VS Code forks.

## Compatibility table

| Manifest field | VS Code behavior |
|---|---|
| `version` | Required. |
| `type` | `extension`, `plugin`, `container`. |
| `platforms.vscode` | Strict. |

### `platforms.vscode` fields

| Field | Purpose |
|---|---|
| `platforms.vscode.kind` | `extension` or `devcontainer`. |
| `platforms.vscode.publisher_id` | Marketplace publisher id. |
| `platforms.vscode.extension_id` | Extension id (publisher.name). |
| `platforms.vscode.min_vscode` | Minimum VS Code engine. |
| `platforms.vscode.image` | DevContainer image. |
| `platforms.vscode.features` | DevContainer features. |
| `platforms.vscode.forks` | Compatible VS Code forks. |

See [`compatibility.md`](./compatibility.md) and [`perks.md`](./perks.md) for more.
