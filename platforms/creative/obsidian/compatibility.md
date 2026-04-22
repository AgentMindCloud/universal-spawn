# Obsidian compatibility — field-by-field

| universal-spawn v1.0 field | Obsidian behavior |
|---|---|
| `version` | Required. |
| `platforms.obsidian.kind` | `plugin`, `theme`, `vault-snapshot`. |
| `platforms.obsidian.manifest_file` | Obsidian `manifest.json` path. |
| `platforms.obsidian.min_app_version` | Minimum Obsidian version. |
| `platforms.obsidian.vault_archive` | Path to the vault archive when `kind: vault-snapshot`. |
| `platforms.obsidian.desktop_only` | `true` if desktop-only. |

## Coexistence with `manifest.json`

universal-spawn does NOT replace manifest.json. Both files coexist; consumers read both and warn on conflicts.

### `manifest.json` (provider-native)

```json
{
  "id": "your-plugin",
  "name": "Your Plugin",
  "version": "0.1.0",
  "minAppVersion": "1.5.0",
  "description": "",
  "author": "yourhandle",
  "isDesktopOnly": false
}
```

### `universal-spawn.yaml` (platforms.obsidian block)

```yaml
platforms:
  obsidian:
    kind: plugin
    manifest_file: manifest.json
    min_app_version: "1.5.0"
    desktop_only: false
```
