"""Linode (Akamai Cloud) — Linodes + StackScripts + LKE."""
from scripts.ai_specs._common import (
    STANDARD_PERKS, enum, str_prop, bool_prop, schema_object,
)

SPEC = {
    "id": "linode",
    "title": "Linode (Akamai Cloud)",
    "native_config_name": "StackScript + linode-cli",
    "native_config_lang": "bash",

    "lede": (
        "Linode — now Akamai Cloud Compute — offers Linodes (VPS), "
        "Object Storage, block volumes, LKE (managed Kubernetes), and "
        "NodeBalancers. The canonical declarative layer is StackScripts: "
        "bash scripts the provisioner runs on first boot. The "
        "extension captures the Linode type, region, StackScript, "
        "volumes, and firewall."
    ),
    "cares": (
        "The region, Linode type, image, the StackScript id (+ "
        "UDF answers), attached volumes, private IP, and backups."
    ),
    "extras": (
        "`stackscript.udf[]` provides answers to StackScript UDF "
        "prompts so provisioning is fully non-interactive."
    ),

    "compat_table": [
        ("version", "Required."),
        ("type", "`web-app`, `api-service`, `container`, `workflow`, `bot`."),
        ("env_vars_required", "Baked into the StackScript."),
        ("deployment.targets", "Must include `linode`."),
        ("platforms.linode", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("metadata.id", "Linode label suggestion."),
        ("name, description", "Card."),
        ("type", "See above."),
        ("safety.*", "Informational."),
        ("env_vars_required", "StackScript env."),
        ("platforms.linode.region", "Region."),
        ("platforms.linode.instance_type", "Linode plan."),
        ("platforms.linode.image", "Image."),
        ("platforms.linode.stackscript", "StackScript id + UDF answers."),
        ("platforms.linode.volumes", "Block-storage volumes."),
        ("platforms.linode.private_ip", "Private IP toggle."),
        ("platforms.linode.backups", "Automatic backups toggle."),
    ],
    "platform_fields": {
        "region": "Region.",
        "instance_type": "Linode plan.",
        "image": "OS image.",
        "stackscript": "StackScript id + UDF answers.",
        "volumes": "Block-storage volumes.",
        "private_ip": "Private IP toggle.",
        "backups": "Automatic backups toggle.",
    },

    "schema_body": schema_object(
        required=["region", "instance_type", "image"],
        properties={
            "region": enum(["us-east", "us-central", "us-west", "us-southeast",
                            "eu-central", "eu-west", "ap-south", "ap-southeast",
                            "ap-northeast", "ca-central", "au-mel"]),
            "instance_type": str_prop(pattern=r"^g6-(nanode|standard|dedicated|highmem|premium|gpu)-[a-z0-9]+$"),
            "image": str_prop(),
            "stackscript": schema_object(
                properties={
                    "id": {"type": "integer", "minimum": 1},
                    "udf": {
                        "type": "array",
                        "items": schema_object(
                            required=["name", "value"],
                            properties={
                                "name": str_prop(),
                                "value": str_prop(),
                            },
                        ),
                    },
                },
            ),
            "volumes": {
                "type": "array",
                "items": schema_object(
                    required=["label", "size_gb"],
                    properties={
                        "label": str_prop(pattern=r"^[a-z][a-z0-9-]{0,31}$"),
                        "size_gb": {"type": "integer", "minimum": 10, "maximum": 16384},
                    },
                ),
            },
            "private_ip": bool_prop(False),
            "backups": bool_prop(False),
        },
    ),

    "template_yaml": """
version: \"1.0\"
name: Linode Template
type: api-service
description: Template for a Linode-targeted universal-spawn manifest.

platforms:
  linode:
    region: us-east
    instance_type: g6-standard-2
    image: linode/ubuntu24.04
    stackscript:
      id: 123456
      udf:
        - { name: app_domain, value: example.com }
    private_ip: true
    backups: true

safety:
  min_permissions: [network:inbound, network:outbound]

env_vars_required:
  - name: APP_SECRET
    description: App secret baked into the StackScript.
    secret: true

deployment:
  targets: [linode]

metadata:
  license: MIT
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/linode-template }
""",

    "native_config": """
#!/usr/bin/env bash
# StackScript UDF vars come in as $APP_DOMAIN etc.
set -euxo pipefail
apt-get update -y
apt-get install -y docker.io docker-compose-plugin
systemctl enable --now docker
git clone https://github.com/yourhandle/your-project /srv/app
cd /srv/app
docker compose up -d
""",

    "universal_excerpt": """
platforms:
  linode:
    region: us-east
    instance_type: g6-standard-2
    image: linode/ubuntu24.04
    stackscript:
      id: 123456
      udf: [ { name: app_domain, value: example.com } ]
    private_ip: true
    backups: true
""",

    "compatibility_extras": "",

    "deploy_button": {
        "markdown": "[![Deploy on Linode](https://img.shields.io/badge/Deploy%20on-Linode-green)](https://cloud.linode.com/stackscripts/123456)",
        "html": (
            '<a href="https://cloud.linode.com/stackscripts/123456">\n'
            '  <img src="https://img.shields.io/badge/Deploy%20on-Linode-green" alt="Deploy on Linode" />\n'
            '</a>'
        ),
        "params_doc": "Linode's canonical deploy flow links to a public StackScript id in the Cloud Manager. The UDF answers come from `stackscript.udf[]` in this manifest.",
    },

    "perks": STANDARD_PERKS,

    "examples": {
        "static-site": """
version: \"1.0\"
name: Linode Caddy Static
type: site
summary: Static site on a g6-nanode-1 with caddy via StackScript.
description: Smallest Linode running caddy serving /srv/site.

platforms:
  linode:
    region: eu-west
    instance_type: g6-nanode-1
    image: linode/debian12
    stackscript:
      id: 654321
      udf:
        - { name: site_domain, value: static.example.com }
    backups: false

safety:
  min_permissions: [network:inbound]
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [linode]

metadata:
  license: Apache-2.0
  author: { name: Static Co., handle: static-co }
  source: { type: git, url: https://github.com/static-co/linode-caddy }
  id: com.static-co.linode-caddy
""",
        "serverless-api": """
version: \"1.0\"
name: Linode API on Docker
type: api-service
summary: Node API on a g6-standard-2 with Docker Compose and an attached volume.
description: Standard Linode running Docker Compose; API + Postgres container with data volume.

platforms:
  linode:
    region: us-east
    instance_type: g6-standard-2
    image: linode/ubuntu24.04
    stackscript:
      id: 111111
      udf:
        - { name: app_domain, value: api.example.com }
    volumes:
      - { label: data, size_gb: 50 }
    private_ip: true
    backups: true

safety:
  min_permissions: [network:inbound, network:outbound, fs:write]

env_vars_required:
  - name: POSTGRES_PASSWORD
    description: Postgres password baked into the StackScript.
    secret: true

deployment:
  targets: [linode]

metadata:
  license: Apache-2.0
  author: { name: API Co., handle: api-co }
  source: { type: git, url: https://github.com/api-co/linode-docker-api }
  id: com.api-co.linode-docker-api
""",
        "full-stack-app": """
version: \"1.0\"
name: Linode LKE Full Stack
type: web-app
summary: Full-stack LKE-ready node with backups, private IP, and two volumes.
description: >
  Premium Linode bootstrapping as a worker node in an LKE cluster (via
  StackScript). Two volumes (data + logs), backups on, private IP, EU
  central region for residency.

platforms:
  linode:
    region: eu-central
    instance_type: g6-dedicated-8
    image: linode/ubuntu24.04
    stackscript:
      id: 999999
      udf:
        - { name: kube_token, value: \"\" }
        - { name: kube_server, value: https://lke-control-plane.example.com:6443 }
    volumes:
      - { label: data, size_gb: 200 }
      - { label: logs, size_gb: 50 }
    private_ip: true
    backups: true

safety:
  min_permissions: [network:inbound, network:outbound, fs:read, fs:write]
  cost_limit_usd_daily: 8
  safe_for_auto_spawn: false
  data_residency: [eu]

env_vars_required:
  - name: KUBE_TOKEN
    description: LKE join token.
    secret: true

deployment:
  targets: [linode]

metadata:
  license: MIT
  author: { name: Stack Co., handle: stack-co }
  source: { type: git, url: https://github.com/stack-co/linode-lke-node }
  id: com.stack-co.linode-lke-node
""",
    },
}
