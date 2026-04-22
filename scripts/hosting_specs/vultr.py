"""Vultr — VPS + Kubernetes + cloud-init + managed databases."""
from scripts.ai_specs._common import (
    STANDARD_PERKS, enum, str_prop, bool_prop, schema_object,
)

SPEC = {
    "id": "vultr",
    "title": "Vultr",
    "native_config_name": "cloud-init.yaml + Vultr API",
    "native_config_lang": "yaml",

    "lede": (
        "Vultr offers VPS (cloud compute), bare metal, Vultr Kubernetes "
        "Engine, object storage, and managed databases. The extension "
        "captures the region, plan, OS, cloud-init user-data, attached "
        "block storage, private networking, and managed databases."
    ),
    "cares": (
        "The region, plan id, OS, cloud-init path, attached block "
        "storage, private networks, and managed databases."
    ),
    "extras": (
        "`managed_databases[]` provisions Vultr's managed Postgres / "
        "MySQL / Redis. `vpc[]` attaches the instance to a named "
        "private VPC."
    ),

    "compat_table": [
        ("version", "Required."),
        ("type", "`web-app`, `api-service`, `container`, `workflow`."),
        ("env_vars_required", "Cloud-init injected."),
        ("deployment.targets", "Must include `vultr`."),
        ("platforms.vultr", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("metadata.id", "Label suggestion."),
        ("name, description", "Card."),
        ("type", "See above."),
        ("safety.*", "Informational."),
        ("env_vars_required", "Cloud-init env."),
        ("platforms.vultr.region", "Region slug."),
        ("platforms.vultr.plan", "Plan id."),
        ("platforms.vultr.os", "OS slug."),
        ("platforms.vultr.cloud_init", "cloud-init user-data path."),
        ("platforms.vultr.block_storage", "Attached block storage."),
        ("platforms.vultr.vpc", "Private VPCs."),
        ("platforms.vultr.managed_databases", "Managed databases."),
        ("platforms.vultr.firewall_group", "Attached firewall group."),
        ("platforms.vultr.backups", "Automatic backups."),
    ],
    "platform_fields": {
        "region": "Region.",
        "plan": "Plan id.",
        "os": "OS slug.",
        "cloud_init": "cloud-init user-data path.",
        "block_storage": "Attached block storage.",
        "vpc": "Private VPCs.",
        "managed_databases": "Managed databases.",
        "firewall_group": "Attached firewall group.",
        "backups": "Automatic backups.",
    },

    "schema_body": schema_object(
        required=["region", "plan", "os"],
        properties={
            "region": str_prop(pattern=r"^[a-z]{3,4}$"),
            "plan": str_prop(pattern=r"^[a-z0-9-]+$"),
            "os": str_prop(pattern=r"^[a-zA-Z0-9 ._-]+$"),
            "cloud_init": str_prop(),
            "block_storage": {
                "type": "array",
                "items": schema_object(
                    required=["label", "size_gb"],
                    properties={
                        "label": str_prop(pattern=r"^[a-z][a-z0-9-]{0,63}$"),
                        "size_gb": {"type": "integer", "minimum": 10, "maximum": 40960},
                        "block_type": enum(["high_perf", "storage_opt"]),
                    },
                ),
            },
            "vpc": {
                "type": "array",
                "items": str_prop(pattern=r"^[a-z0-9][a-z0-9-]{0,63}$"),
            },
            "managed_databases": {
                "type": "array",
                "items": schema_object(
                    required=["engine", "label"],
                    properties={
                        "engine": enum(["pg", "mysql", "redis"]),
                        "label": str_prop(pattern=r"^[a-z][a-z0-9-]{0,63}$"),
                        "plan": str_prop(),
                    },
                ),
            },
            "firewall_group": str_prop(),
            "backups": bool_prop(False),
        },
    ),

    "template_yaml": """
version: \"1.0\"
name: Vultr Template
type: web-app
description: Template for a Vultr-targeted universal-spawn manifest.

platforms:
  vultr:
    region: ewr
    plan: vc2-2c-4gb
    os: Ubuntu 24.04 LTS x64
    cloud_init: cloud-init.yaml
    backups: true
    firewall_group: web

safety:
  min_permissions: [network:inbound, network:outbound]

env_vars_required:
  - name: APP_SECRET
    description: App secret.
    secret: true

deployment:
  targets: [vultr]

metadata:
  license: MIT
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/vultr-template }
""",

    "native_config": """
#cloud-config
package_update: true
packages: [docker.io, docker-compose-plugin]
runcmd:
  - systemctl enable --now docker
  - docker compose -f /srv/app/docker-compose.yml up -d
""",

    "universal_excerpt": """
platforms:
  vultr:
    region: ewr
    plan: vc2-2c-4gb
    os: Ubuntu 24.04 LTS x64
    cloud_init: cloud-init.yaml
    backups: true
""",

    "compatibility_extras": "",

    "deploy_button": {
        "markdown": "[![Deploy on Vultr](https://img.shields.io/badge/Deploy%20on-Vultr-blue)](https://my.vultr.com/deploy/)",
        "html": (
            '<a href="https://my.vultr.com/deploy/">\n'
            '  <img src="https://img.shields.io/badge/Deploy%20on-Vultr-blue" alt="Deploy on Vultr" />\n'
            '</a>'
        ),
        "params_doc": "Vultr has no native Deploy button. Drive provisioning with the Vultr API or Terraform using the fields above.",
    },

    "perks": STANDARD_PERKS,

    "examples": {
        "static-site": """
version: \"1.0\"
name: Vultr Static Site
type: site
summary: Static site on a Vultr Cloud Compute instance with caddy.
description: vc2-1c-1gb in lax running caddy serving /srv/site.

platforms:
  vultr:
    region: lax
    plan: vc2-1c-1gb
    os: Debian 12 x64
    cloud_init: cloud-init-caddy.yaml
    backups: false
    firewall_group: web

safety:
  min_permissions: [network:inbound]
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [vultr]

metadata:
  license: Apache-2.0
  author: { name: Static Co., handle: static-co }
  source: { type: git, url: https://github.com/static-co/vultr-static }
  id: com.static-co.vultr-static
""",
        "serverless-api": """
version: \"1.0\"
name: Vultr Docker API
type: api-service
summary: Node API on Vultr with a managed Postgres and attached block storage.
description: vc2-2c-4gb in ewr with cloud-init provisioning Docker + Postgres client, block storage for uploads.

platforms:
  vultr:
    region: ewr
    plan: vc2-2c-4gb
    os: Ubuntu 24.04 LTS x64
    cloud_init: cloud-init-docker.yaml
    block_storage:
      - { label: uploads, size_gb: 40, block_type: high_perf }
    managed_databases:
      - { engine: pg, label: api-db, plan: vultr-dbaas-startup-cc-1-55-2 }
    firewall_group: api
    backups: true

safety:
  min_permissions: [network:inbound, network:outbound, fs:write]
  rate_limit_qps: 80

env_vars_required:
  - name: POSTGRES_PASSWORD
    description: Postgres password supplied by the managed DB.
    secret: true

deployment:
  targets: [vultr]

metadata:
  license: Apache-2.0
  author: { name: API Co., handle: api-co }
  source: { type: git, url: https://github.com/api-co/vultr-docker-api }
  id: com.api-co.vultr-docker-api
""",
        "full-stack-app": """
version: \"1.0\"
name: Vultr Full Stack VPC
type: web-app
summary: Full-stack Vultr deployment behind a VPC with managed Postgres and Redis.
description: >
  vc2-4c-8gb in fra attached to a private VPC, with managed Postgres
  and Redis. Two block volumes (uploads + logs). Daily backups on.
  Frankfurt region for data residency.

platforms:
  vultr:
    region: fra
    plan: vc2-4c-8gb
    os: Ubuntu 24.04 LTS x64
    cloud_init: cloud-init-k3s.yaml
    block_storage:
      - { label: uploads, size_gb: 100, block_type: high_perf }
      - { label: logs,    size_gb: 40,  block_type: storage_opt }
    vpc: [default-eu]
    managed_databases:
      - { engine: pg,    label: app-db,    plan: vultr-dbaas-startup-cc-1-55-2 }
      - { engine: redis, label: app-cache, plan: vultr-dbaas-startup-cc-2-55-1 }
    firewall_group: app
    backups: true

safety:
  min_permissions: [network:inbound, network:outbound, fs:read, fs:write]
  cost_limit_usd_daily: 10
  safe_for_auto_spawn: false
  data_residency: [eu]

env_vars_required:
  - name: POSTGRES_PASSWORD
    description: Managed PG password.
    secret: true
  - name: REDIS_PASSWORD
    description: Managed Redis password.
    secret: true
  - name: SESSION_SECRET
    description: Session secret.
    secret: true

deployment:
  targets: [vultr]

metadata:
  license: MIT
  author: { name: Stack Co., handle: stack-co }
  source: { type: git, url: https://github.com/stack-co/vultr-full-stack }
  id: com.stack-co.vultr-full-stack
""",
    },
}
