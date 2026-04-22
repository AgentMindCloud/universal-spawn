# Obsidian — universal-spawn platform extension

Obsidian is a local-first Markdown notes app with a plugin + theme ecosystem. A universal-spawn manifest targets a community plugin, a downloadable vault snapshot, or a theme.

## What this platform cares about

The `kind` (`plugin`, `theme`, `vault-snapshot`), the Obsidian `manifest.json` path (for plugins/themes), the minimum Obsidian version, and the vault snapshot archive when applicable.

## Compatibility table

| Manifest field | Obsidian behavior |
|---|---|
| `version` | Required. |
| `type` | `extension`, `plugin`, `design-template`, `creative-tool`. |
| `deployment.targets` | Must include `obsidian`. |
| `platforms.obsidian` | Strict. |

### `platforms.obsidian` fields

| Field | Purpose |
|---|---|
| `platforms.obsidian.kind` | `plugin`, `theme`, or `vault-snapshot`. |
| `platforms.obsidian.manifest_file` | Obsidian plugin/theme manifest.json. |
| `platforms.obsidian.min_app_version` | Minimum Obsidian version. |
| `platforms.obsidian.vault_archive` | Vault archive path (for vault-snapshot). |
| `platforms.obsidian.desktop_only` | Desktop-only flag. |

See [`compatibility.md`](./compatibility.md) for more.
