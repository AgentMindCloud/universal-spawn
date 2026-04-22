# Figma compatibility — field-by-field

| universal-spawn v1.0 field | Figma behavior |
|---|---|
| `version` | Required. |
| `metadata.id` | Stable key across the community registry. |
| `name, description` | Community / plugin directory card. |
| `type` | See above. |
| `platforms.figma.kind` | `plugin`, `widget`, or `template`. |
| `platforms.figma.manifest_file` | Relative path to the Figma plugin/widget `manifest.json`. |
| `platforms.figma.editor_type` | Editor types the creation runs in. |
| `platforms.figma.network_access` | `none`, `declared`, `allowed-hosts`. |
| `platforms.figma.allowed_hosts` | Hosts when `network_access: allowed-hosts`. |
| `platforms.figma.capabilities` | Figma plugin capabilities. |
| `platforms.figma.community_file` | Community-file URL or id (for `kind: template`). |

## Coexistence with `manifest.json`

universal-spawn does NOT replace manifest.json. Both files coexist; consumers read both and warn on conflicts.

### `manifest.json` (provider-native)

```json
{
  "name": "Parchment Grid",
  "id": "123456789012345678",
  "api": "1.0.0",
  "main": "dist/code.js",
  "ui": "dist/ui.html",
  "editorType": ["figma", "figjam"],
  "networkAccess": { "allowedDomains": ["none"] }
}
```

### `universal-spawn.yaml` (platforms.figma block)

```yaml
platforms:
  figma:
    kind: plugin
    manifest_file: manifest.json
    editor_type: [figma, figjam]
    network_access: none
```

## Three kinds, one extension

The `kind` field picks which Figma surface the creation targets. `plugin` and `widget` both point at a `manifest.json` (the key schema difference is which Figma fields are read). `template` carries a `community_file` URL and a `hero_plate` / `icon` for the community card; no code runs — the consumer opens Figma with the duplicate-to-workspace link.
