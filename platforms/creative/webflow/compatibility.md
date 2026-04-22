# Webflow compatibility — field-by-field

| universal-spawn v1.0 field | Webflow behavior |
|---|---|
| `version` | Required. |
| `metadata.id` | Suggested site slug. |
| `platforms.webflow.kind` | `site`, `library`, `collection`. |
| `platforms.webflow.site_id` | Webflow site id. |
| `platforms.webflow.custom_domain` | Custom domain. |
| `platforms.webflow.collections` | CMS collection schemas. |
| `platforms.webflow.localization` | Localization locales. |

## Coexistence with `Webflow dashboard state (exported JSON)`

universal-spawn does NOT replace Webflow dashboard state (exported JSON). Both files coexist; consumers read both and warn on conflicts.

### `Webflow dashboard state (exported JSON)` (provider-native)

```json
{
  "siteId": "000000000000000000000000",
  "customDomain": "your-site.example.com",
  "collections": [{ "name": "posts", "singular": "post" }]
}
```

### `universal-spawn.yaml` (platforms.webflow block)

```yaml
platforms:
  webflow:
    kind: site
    site_id: "000000000000000000000000"
    custom_domain: your-site.example.com
    collections:
      - { name: posts, singular: post, fields_file: collections/posts.fields.json }
```
