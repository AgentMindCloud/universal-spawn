"""Anyscale — Ray Serve / Ray Data via service.yaml."""
from scripts.ai_specs._common import enum, str_prop, bool_prop, schema_object


SPEC = {
    "id": "anyscale",
    "title": "Anyscale",
    "lede": (
        "Anyscale is the managed Ray platform. A universal-spawn "
        "manifest pins the service.yaml file, the Ray version, and "
        "the cluster shape."
    ),
    "cares": (
        "The service.yaml file path, Ray version, head + worker "
        "shapes, and the workspace cloud."
    ),
    "compat_table": [
        ("version", "Required."),
        ("type", "`workflow`, `api-service`, `library`."),
        ("platforms.anyscale", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("platforms.anyscale.service_file", "service.yaml path."),
        ("platforms.anyscale.ray_version", "Ray version."),
        ("platforms.anyscale.head_node", "Head-node instance type."),
        ("platforms.anyscale.worker_nodes", "Worker-node groups."),
        ("platforms.anyscale.cloud", "Anyscale cloud id."),
    ],
    "platform_fields": {
        "service_file": "service.yaml path.",
        "ray_version": "Ray version.",
        "head_node": "Head-node instance type.",
        "worker_nodes": "Worker-node groups.",
        "cloud": "Anyscale cloud id.",
    },
    "schema_body": schema_object(
        required=["service_file", "ray_version"],
        properties={
            "service_file": str_prop(),
            "ray_version": str_prop(pattern=r"^[0-9]+(\.[0-9]+)+$"),
            "head_node": str_prop(),
            "worker_nodes": {
                "type": "array",
                "items": schema_object(
                    properties={
                        "instance_type": str_prop(),
                        "min": {"type": "integer", "minimum": 0},
                        "max": {"type": "integer", "minimum": 1},
                    },
                ),
            },
            "cloud": str_prop(),
        },
    ),
    "template_yaml": """
version: "1.0"
name: Anyscale Template
type: api-service
description: Template for an Anyscale-targeted universal-spawn manifest.

platforms:
  anyscale:
    service_file: service.yaml
    ray_version: "2.36"
    head_node: m6i.large
    worker_nodes:
      - { instance_type: g5.xlarge, min: 1, max: 4 }

safety:
  min_permissions: [network:inbound, network:outbound]

env_vars_required:
  - name: ANYSCALE_TOKEN
    description: Anyscale token.
    secret: true

deployment:
  targets: [anyscale]

metadata:
  license: Apache-2.0
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/anyscale-template }
""",
    "native_config_name": "service.yaml + ray cluster shape",
    "native_config_lang": "yaml",
    "native_config": """
name: your-service
applications:
  - import_path: app:deployment
ray_serve_config: { proxy_location: HeadOnly }
""",
    "universal_excerpt": """
platforms:
  anyscale:
    service_file: service.yaml
    ray_version: "2.36"
    head_node: m6i.large
""",
    "compatibility_extras": "",
    "examples": {
        "example-1": """
version: "1.0"
name: Plate Ray Serve
type: api-service
summary: Minimal Anyscale Ray Serve deployment.
description: One Ray Serve app on a single head node.

platforms:
  anyscale:
    service_file: service.yaml
    ray_version: "2.36"
    head_node: m6i.large

safety:
  min_permissions: [network:inbound, network:outbound]
  safe_for_auto_spawn: false

env_vars_required:
  - name: ANYSCALE_TOKEN
    description: Anyscale token.
    secret: true

deployment:
  targets: [anyscale]

metadata:
  license: Apache-2.0
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/anyscale-plate-serve }
  id: com.plate-studio.anyscale-plate-serve
""",
        "example-2": """
version: "1.0"
name: Plate Ray Cluster
type: workflow
summary: Full Anyscale cluster with GPU worker autoscaling for plate generation.
description: Head node + GPU workers (g5.xlarge, 1-8 autoscale).

platforms:
  anyscale:
    service_file: service.yaml
    ray_version: "2.36"
    head_node: m6i.xlarge
    worker_nodes:
      - { instance_type: g5.xlarge, min: 1, max: 8 }
    cloud: aws-us-west-2

safety:
  min_permissions: [network:inbound, network:outbound, gpu:compute]
  cost_limit_usd_daily: 60
  safe_for_auto_spawn: false

env_vars_required:
  - name: ANYSCALE_TOKEN
    description: Anyscale token.
    secret: true

deployment:
  targets: [anyscale]

metadata:
  license: Apache-2.0
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/anyscale-plate-cluster }
  id: com.plate-studio.anyscale-plate-cluster
""",
    },
}
