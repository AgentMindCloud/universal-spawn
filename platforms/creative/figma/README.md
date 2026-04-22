# Figma — universal-spawn platform extension

Figma is three surfaces in one: Plugins (code running inside the editor), Widgets (code rendering inside a file), and Community files (duplicatable design assets). The extension covers all three.

## What this platform cares about

The `kind` (`plugin`, `widget`, `template`), the Figma plugin manifest path when applicable, editor types (`figma`, `figjam`, `dev`, `slides`), network-access policy, and the community-file URL for duplicate-to-workspace.

## Compatibility table

| Manifest field | Figma behavior |
|---|---|
| `version` | Required `"1.0"`. |
| `type` | `creative-tool`, `design-template`, `plugin`, `extension`. |
| `deployment.targets` | Must include `figma`. |
| `platforms.figma` | Strict. |

### `platforms.figma` fields

| Field | Purpose |
|---|---|
| `platforms.figma.kind` | `plugin`, `widget`, or `template`. |
| `platforms.figma.manifest_file` | Figma plugin / widget manifest.json path. |
| `platforms.figma.editor_type` | Editors the plugin runs in. |
| `platforms.figma.network_access` | Network policy. |
| `platforms.figma.allowed_hosts` | Allowed hosts when policy is allowed-hosts. |
| `platforms.figma.capabilities` | Figma plugin capabilities. |
| `platforms.figma.community_file` | Community-file URL or id. |

See [`compatibility.md`](./compatibility.md) and [`perks.md`](./perks.md) for more.
