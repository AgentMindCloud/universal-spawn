"""Kubernetes — Helm charts + Kustomize overlays."""
from scripts.ai_specs._common import enum, str_prop, bool_prop, schema_object


SPEC = {
    "id": "kubernetes",
    "title": "Kubernetes",
    "lede": (
        "Kubernetes applications are distributed as Helm charts or "
        "Kustomize overlays. A universal-spawn manifest picks the "
        "`style` and points at the chart / overlay root, plus the "
        "compatible Kubernetes API range."
    ),
    "cares": (
        "`style` (`helm`, `kustomize`, `manifests`), the chart or "
        "overlay path, the minimum Kubernetes version, and the target "
        "namespace."
    ),
    "compat_table": [
        ("version", "Required."),
        ("type", "`container`, `workflow`, `api-service`, `web-app`."),
        ("platforms.kubernetes", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("platforms.kubernetes.style", "`helm`, `kustomize`, `manifests`."),
        ("platforms.kubernetes.chart_path", "Helm chart directory."),
        ("platforms.kubernetes.overlay_path", "Kustomize overlay directory."),
        ("platforms.kubernetes.manifests_path", "Plain manifests directory."),
        ("platforms.kubernetes.values_file", "Helm values file path."),
        ("platforms.kubernetes.min_kube_version", "Minimum k8s API version."),
        ("platforms.kubernetes.namespace", "Target namespace."),
    ],
    "platform_fields": {
        "style": "`helm`, `kustomize`, or `manifests`.",
        "chart_path": "Helm chart root.",
        "overlay_path": "Kustomize overlay root.",
        "manifests_path": "Plain manifests dir.",
        "values_file": "Helm values file.",
        "min_kube_version": "Minimum k8s API version.",
        "namespace": "Target namespace.",
    },
    "schema_body": schema_object(
        required=["style"],
        properties={
            "style": enum(["helm", "kustomize", "manifests"]),
            "chart_path": str_prop(),
            "overlay_path": str_prop(),
            "manifests_path": str_prop(),
            "values_file": str_prop(),
            "min_kube_version": str_prop(pattern=r"^[0-9]+\.[0-9]+(\.[0-9]+)?$"),
            "namespace": str_prop(pattern=r"^[a-z][a-z0-9-]{0,62}$"),
        },
    ),
    "template_yaml": """
version: "1.0"
name: Kubernetes Template
type: container
description: Template for a Kubernetes-targeted universal-spawn manifest.

platforms:
  kubernetes:
    style: helm
    chart_path: charts/your-app
    values_file: charts/your-app/values.yaml
    min_kube_version: "1.28"
    namespace: default

safety:
  min_permissions: [network:inbound, network:outbound]

env_vars_required: []

deployment:
  targets: [kubernetes]

metadata:
  license: Apache-2.0
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/k8s-template }
""",
    "native_config_name": "Chart.yaml / kustomization.yaml",
    "native_config_lang": "yaml",
    "native_config": """
apiVersion: v2
name: your-app
version: 0.1.0
appVersion: "0.1.0"
kubeVersion: ">=1.28.0"
""",
    "universal_excerpt": """
platforms:
  kubernetes:
    style: helm
    chart_path: charts/your-app
    values_file: charts/your-app/values.yaml
    min_kube_version: "1.28"
""",
    "compatibility_extras": "",
    "examples": {
        "example-1": """
version: "1.0"
name: Plate Helm Chart
type: container
summary: Minimal Helm-packaged chart for a single web service.
description: Chart with Deployment + Service + Ingress. Targets k8s 1.28+.

platforms:
  kubernetes:
    style: helm
    chart_path: charts/plate-web
    values_file: charts/plate-web/values.yaml
    min_kube_version: "1.28"
    namespace: plate

safety:
  min_permissions: [network:inbound, network:outbound]
  safe_for_auto_spawn: false

env_vars_required: []

deployment:
  targets: [kubernetes]

metadata:
  license: Apache-2.0
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/k8s-plate-helm }
  id: com.plate-studio.k8s-plate-helm
""",
        "example-2": """
version: "1.0"
name: Plate Kustomize Overlay
type: container
summary: Full kustomize overlay for production + preview environments.
description: >
  Uses kustomize overlays — one base + two overlays (production,
  preview). Targets k8s 1.30+.

platforms:
  kubernetes:
    style: kustomize
    overlay_path: deploy/overlays/production
    min_kube_version: "1.30"
    namespace: plate-prod

safety:
  min_permissions: [network:inbound, network:outbound]
  safe_for_auto_spawn: false
  data_residency: [eu]

env_vars_required:
  - name: DATABASE_URL
    description: Postgres connection string (sealed-secret).
    secret: true

deployment:
  targets: [kubernetes]

metadata:
  license: Apache-2.0
  author: { name: Stack Co., handle: stack-co }
  source: { type: git, url: https://github.com/stack-co/k8s-kustomize-overlay }
  id: com.stack-co.k8s-kustomize-overlay
""",
    },
}
