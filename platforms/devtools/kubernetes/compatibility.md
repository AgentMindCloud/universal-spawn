# Kubernetes compatibility — field-by-field

| universal-spawn v1.0 field | Kubernetes behavior |
|---|---|
| `version` | Required. |
| `platforms.kubernetes.style` | `helm`, `kustomize`, `manifests`. |
| `platforms.kubernetes.chart_path` | Helm chart directory. |
| `platforms.kubernetes.overlay_path` | Kustomize overlay directory. |
| `platforms.kubernetes.manifests_path` | Plain manifests directory. |
| `platforms.kubernetes.values_file` | Helm values file path. |
| `platforms.kubernetes.min_kube_version` | Minimum k8s API version. |
| `platforms.kubernetes.namespace` | Target namespace. |

## Coexistence with `Chart.yaml / kustomization.yaml`

universal-spawn does NOT replace Chart.yaml / kustomization.yaml. Both files coexist; consumers read both and warn on conflicts.

### `Chart.yaml / kustomization.yaml` (provider-native)

```yaml
apiVersion: v2
name: your-app
version: 0.1.0
appVersion: "0.1.0"
kubeVersion: ">=1.28.0"
```

### `universal-spawn.yaml` (platforms.kubernetes block)

```yaml
platforms:
  kubernetes:
    style: helm
    chart_path: charts/your-app
    values_file: charts/your-app/values.yaml
    min_kube_version: "1.28"
```
