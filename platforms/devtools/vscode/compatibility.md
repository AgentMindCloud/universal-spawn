# VS Code compatibility — field-by-field

| universal-spawn v1.0 field | VS Code behavior |
|---|---|
| `version` | Required. |
| `platforms.vscode.kind` | `extension` or `devcontainer`. |
| `platforms.vscode.publisher_id` | Marketplace publisher id. |
| `platforms.vscode.extension_id` | Extension id (publisher.name). |
| `platforms.vscode.min_vscode` | Minimum VS Code engine version. |
| `platforms.vscode.image` | DevContainer image. |
| `platforms.vscode.features` | DevContainer features map. |
| `platforms.vscode.forks` | Compatible forks (`vscode`, `cursor`, `windsurf`, `code-oss`). |

## Coexistence with `package.json + devcontainer.json`

universal-spawn does NOT replace package.json + devcontainer.json. Both files coexist; consumers read both and warn on conflicts.

### `package.json + devcontainer.json` (provider-native)

```json
{
  "name": "your-extension",
  "publisher": "yourhandle",
  "engines": { "vscode": "^1.90.0" },
  "contributes": { "commands": [] }
}
```

### `universal-spawn.yaml` (platforms.vscode block)

```yaml
platforms:
  vscode:
    kind: extension
    publisher_id: yourhandle
    extension_id: yourhandle.your-extension
    min_vscode: "^1.90.0"
```

## Extension vs DevContainer

They are independent. An `extension` manifest packages a VS Code Marketplace extension. A `devcontainer` manifest describes a fully reproducible dev environment that any VS Code fork (or Codespaces, or Gitpod) can open directly. Same creation may ship both — but in two sibling manifests, not one.
