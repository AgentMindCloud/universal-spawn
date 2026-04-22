# Notion compatibility — field-by-field

| universal-spawn v1.0 field | Notion behavior |
|---|---|
| `version` | Required. |
| `metadata.id` | Suggested key. |
| `platforms.notion.page_url` | Public page URL (required for duplicate). |
| `platforms.notion.page_id` | Notion page UUID. |
| `platforms.notion.kind` | `template`, `database`, `workspace-pack`. |
| `platforms.notion.seed_csv` | Optional CSV to seed a duplicated database. |

## Coexistence with `Notion page`

universal-spawn does NOT replace Notion page. Both files coexist; consumers read both and warn on conflicts.

### `Notion page` (provider-native)

```text
Notion has no repo-level config format.
The source of truth is the public page itself, referenced by URL.
A consumer takes ?duplicate=true on that URL to trigger the dupe flow.
```

### `universal-spawn.yaml` (platforms.notion block)

```yaml
platforms:
  notion:
    page_url: "https://notion.so/yourhandle/0000000000000000000000000000"
    kind: template
```
