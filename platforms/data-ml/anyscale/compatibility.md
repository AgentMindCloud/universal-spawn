# Anyscale compatibility — field-by-field

| universal-spawn v1.0 field | Anyscale behavior |
|---|---|
| `version` | Required. |
| `platforms.anyscale.service_file` | service.yaml path. |
| `platforms.anyscale.ray_version` | Ray version. |
| `platforms.anyscale.head_node` | Head-node instance type. |
| `platforms.anyscale.worker_nodes` | Worker-node groups. |
| `platforms.anyscale.cloud` | Anyscale cloud id. |

## Coexistence with `service.yaml + ray cluster shape`

universal-spawn does NOT replace service.yaml + ray cluster shape. Both files coexist; consumers read both and warn on conflicts.

### `service.yaml + ray cluster shape` (provider-native)

```yaml
name: your-service
applications:
  - import_path: app:deployment
ray_serve_config: { proxy_location: HeadOnly }
```

### `universal-spawn.yaml` (platforms.anyscale block)

```yaml
platforms:
  anyscale:
    service_file: service.yaml
    ray_version: "2.36"
    head_node: m6i.large
```
