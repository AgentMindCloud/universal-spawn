# Notion — universal-spawn platform extension

Notion doesn't have a plugin API, but it does have a strong 'duplicate this page' pattern. A universal-spawn manifest pointing at a Notion page lets consumers render a one-click duplicate button that brings the template into the user's own workspace.

## What this platform cares about

The public Notion page URL, the page id, optional CSV seed files for database duplication, and icons / covers.

## Compatibility table

| Manifest field | Notion behavior |
|---|---|
| `version` | Required. |
| `type` | `design-template`, `creative-tool`. |
| `deployment.targets` | Must include `notion`. |
| `platforms.notion` | Strict. |

### `platforms.notion` fields

| Field | Purpose |
|---|---|
| `platforms.notion.page_url` | Public page URL used for the duplicate button. |
| `platforms.notion.page_id` | Notion page UUID (32 hex chars). |
| `platforms.notion.kind` | `template`, `database`, `workspace-pack`. |
| `platforms.notion.seed_csv` | Optional CSV to seed a duplicated database. |

See [`compatibility.md`](./compatibility.md) for more.
