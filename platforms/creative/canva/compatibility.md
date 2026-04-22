# Canva compatibility — field-by-field

| universal-spawn v1.0 field | Canva behavior |
|---|---|
| `version` | Required. |
| `platforms.canva.kind` | `app`, `template`, `design`. |
| `platforms.canva.app_json` | `app.json` path for Canva Apps. |
| `platforms.canva.design_url` | Public Canva design URL. |
| `platforms.canva.design_id` | Canva design id. |
| `platforms.canva.categories` | Canva category slugs. |
| `platforms.canva.surface` | In-editor surfaces the app runs on. |

## Coexistence with `app.json (Canva Apps SDK)`

universal-spawn does NOT replace app.json (Canva Apps SDK). Both files coexist; consumers read both and warn on conflicts.

### `app.json (Canva Apps SDK)` (provider-native)

```json
{
  "id": "AAF0000000000",
  "appOrigin": "https://app.example.com",
  "surfaces": ["object-panel"],
  "capabilities": ["upload-image"]
}
```

### `universal-spawn.yaml` (platforms.canva block)

```yaml
platforms:
  canva:
    kind: app
    app_json: app.json
    surface: [object-panel]
```
