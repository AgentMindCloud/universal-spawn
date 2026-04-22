# Framer compatibility — field-by-field

| universal-spawn v1.0 field | Framer behavior |
|---|---|
| `version` | Required. |
| `metadata.id` | Project-slug suggestion. |
| `name, description` | Marketplace / site card. |
| `platforms.framer.kind` | `site`, `component-pack`, `project`. |
| `platforms.framer.project_id` | Framer project id. |
| `platforms.framer.custom_domain` | Optional custom domain. |
| `platforms.framer.marketplace` | Marketplace-listing settings. |

## Coexistence with `framer.project.json`

universal-spawn does NOT replace framer.project.json. Both files coexist; consumers read both and warn on conflicts.

### `framer.project.json` (provider-native)

```json
{
  "projectId": "abc123xyz",
  "customDomain": "your-site.example.com",
  "publishChannels": ["production"]
}
```

### `universal-spawn.yaml` (platforms.framer block)

```yaml
platforms:
  framer:
    kind: site
    project_id: abc123xyz
    custom_domain: your-site.example.com
```
