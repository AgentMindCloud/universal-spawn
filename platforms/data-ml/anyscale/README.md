# Anyscale — universal-spawn platform extension

Anyscale is the managed Ray platform. A universal-spawn manifest pins the service.yaml file, the Ray version, and the cluster shape.

## What this platform cares about

The service.yaml file path, Ray version, head + worker shapes, and the workspace cloud.

## Compatibility table

| Manifest field | Anyscale behavior |
|---|---|
| `version` | Required. |
| `type` | `workflow`, `api-service`, `library`. |
| `platforms.anyscale` | Strict. |

### `platforms.anyscale` fields

| Field | Purpose |
|---|---|
| `platforms.anyscale.service_file` | service.yaml path. |
| `platforms.anyscale.ray_version` | Ray version. |
| `platforms.anyscale.head_node` | Head-node instance type. |
| `platforms.anyscale.worker_nodes` | Worker-node groups. |
| `platforms.anyscale.cloud` | Anyscale cloud id. |

See [`compatibility.md`](./compatibility.md) for more.
