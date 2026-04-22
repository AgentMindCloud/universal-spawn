# Modal — universal-spawn platform extension

Modal runs Python functions and apps as serverless workloads. A universal-spawn manifest pins the entry app file, the GPU type if any, the image kind, and any persistent volumes.

## What this platform cares about

The entry file, the App name, the GPU class, the image (prebuilt vs custom), and persistent volumes.

## Compatibility table

| Manifest field | Modal behavior |
|---|---|
| `version` | Required. |
| `type` | `workflow`, `web-app`, `api-service`, `library`. |
| `platforms.modal` | Strict. |

### `platforms.modal` fields

| Field | Purpose |
|---|---|
| `platforms.modal.entry_file` | Modal app entry file. |
| `platforms.modal.app_name` | Modal App name. |
| `platforms.modal.gpu` | GPU class. |
| `platforms.modal.image_kind` | Image kind. |
| `platforms.modal.volumes` | Persistent volume names. |
| `platforms.modal.secrets` | Modal Secret names. |

See [`compatibility.md`](./compatibility.md) for more.
