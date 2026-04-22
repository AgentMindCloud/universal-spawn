# Kubernetes — universal-spawn platform extension

Kubernetes applications are distributed as Helm charts or Kustomize overlays. A universal-spawn manifest picks the `style` and points at the chart / overlay root, plus the compatible Kubernetes API range.

## What this platform cares about

`style` (`helm`, `kustomize`, `manifests`), the chart or overlay path, the minimum Kubernetes version, and the target namespace.

## Compatibility table

| Manifest field | Kubernetes behavior |
|---|---|
| `version` | Required. |
| `type` | `container`, `workflow`, `api-service`, `web-app`. |
| `platforms.kubernetes` | Strict. |

### `platforms.kubernetes` fields

| Field | Purpose |
|---|---|
| `platforms.kubernetes.style` | `helm`, `kustomize`, or `manifests`. |
| `platforms.kubernetes.chart_path` | Helm chart root. |
| `platforms.kubernetes.overlay_path` | Kustomize overlay root. |
| `platforms.kubernetes.manifests_path` | Plain manifests dir. |
| `platforms.kubernetes.values_file` | Helm values file. |
| `platforms.kubernetes.min_kube_version` | Minimum k8s API version. |
| `platforms.kubernetes.namespace` | Target namespace. |

See [`compatibility.md`](./compatibility.md) for more.
