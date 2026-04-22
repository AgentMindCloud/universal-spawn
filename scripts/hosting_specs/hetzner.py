"""Hetzner Cloud — VPS + snapshots + cloud-init."""
from scripts.ai_specs._common import (
    STANDARD_PERKS, enum, str_prop, bool_prop, schema_object,
)

SPEC = {
    "id": "hetzner",
    "title": "Hetzner Cloud",
    "native_config_name": "cloud-init.yaml (+ hcloud CLI)",
    "native_config_lang": "yaml",

    "lede": (
        "Hetzner Cloud gives you VPS servers, snapshots, volumes, "
        "networks, and load balancers through `hcloud` or Terraform. "
        "The extension captures the server type, image, cloud-init "
        "script path, networking, and firewalls — everything an "
        "installer needs to provision reproducibly."
    ),
    "cares": (
        "The location (datacenter), server type, image, cloud-init "
        "script, attached volumes, assigned networks, and SSH keys."
    ),
    "extras": (
        "`firewall_rules[]` applies a set of hcloud firewall rules. "
        "`networks[]` attaches the server to private networks by name."
    ),

    "compat_table": [
        ("version", "Required."),
        ("type", "`web-app`, `api-service`, `container`, `workflow`, `bot`."),
        ("env_vars_required", "Cloud-init-injected env or dotenv on disk."),
        ("deployment.targets", "Must include `hetzner`."),
        ("platforms.hetzner", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("metadata.id", "Server name suggestion."),
        ("name, description", "Card."),
        ("type", "See above."),
        ("safety.*", "Informational."),
        ("env_vars_required", "Cloud-init / dotenv."),
        ("platforms.hetzner.location", "Datacenter."),
        ("platforms.hetzner.server_type", "Server type id."),
        ("platforms.hetzner.image", "OS image."),
        ("platforms.hetzner.ssh_keys", "SSH key names."),
        ("platforms.hetzner.cloud_init", "cloud-init config path."),
        ("platforms.hetzner.volumes", "Attached volumes."),
        ("platforms.hetzner.networks", "Attached private networks."),
        ("platforms.hetzner.firewall_rules", "Firewall ruleset."),
    ],
    "platform_fields": {
        "location": "Datacenter (`fsn1`, `nbg1`, `hel1`, `ash`, `hil`, `sin`).",
        "server_type": "Server type id (`cx22`, `cpx31`, `ax41-nvme`, …).",
        "image": "OS image.",
        "ssh_keys": "SSH key names.",
        "cloud_init": "cloud-init user-data path.",
        "volumes": "Attached volumes.",
        "networks": "Attached private networks.",
        "firewall_rules": "Firewall ruleset.",
    },

    "schema_body": schema_object(
        required=["location", "server_type", "image"],
        properties={
            "location": enum(["fsn1", "nbg1", "hel1", "ash", "hil", "sin"]),
            "server_type": str_prop(pattern=r"^[a-z][a-z0-9-]{1,31}$"),
            "image": str_prop(),
            "ssh_keys": {"type": "array", "items": str_prop()},
            "cloud_init": str_prop(),
            "volumes": {
                "type": "array",
                "items": schema_object(
                    required=["name", "size_gb"],
                    properties={
                        "name": str_prop(pattern=r"^[a-z][a-z0-9-]{0,63}$"),
                        "size_gb": {"type": "integer", "minimum": 10, "maximum": 10240},
                        "mount": str_prop(),
                    },
                ),
            },
            "networks": {
                "type": "array",
                "items": str_prop(pattern=r"^[a-z][a-z0-9-]{0,63}$"),
            },
            "firewall_rules": {
                "type": "array",
                "items": schema_object(
                    required=["direction", "protocol"],
                    properties={
                        "direction": enum(["in", "out"]),
                        "protocol": enum(["tcp", "udp", "icmp"]),
                        "port_range": str_prop(),
                        "source_cidrs": {"type": "array", "items": str_prop()},
                    },
                ),
            },
        },
    ),

    "template_yaml": """
version: \"1.0\"
name: Hetzner Template
type: api-service
description: Template for a Hetzner Cloud-targeted universal-spawn manifest.

platforms:
  hetzner:
    location: fsn1
    server_type: cx22
    image: debian-12
    ssh_keys: [ops-key]
    cloud_init: cloud-init.yaml
    firewall_rules:
      - { direction: in, protocol: tcp, port_range: \"22\",  source_cidrs: [\"0.0.0.0/0\", \"::/0\"] }
      - { direction: in, protocol: tcp, port_range: \"80\",  source_cidrs: [\"0.0.0.0/0\", \"::/0\"] }
      - { direction: in, protocol: tcp, port_range: \"443\", source_cidrs: [\"0.0.0.0/0\", \"::/0\"] }

safety:
  min_permissions: [network:inbound, network:outbound]

env_vars_required:
  - name: DATABASE_URL
    description: Postgres connection string.
    secret: true

deployment:
  targets: [hetzner]

metadata:
  license: MIT
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/hetzner-template }
""",

    "native_config": """
#cloud-config
package_update: true
package_upgrade: true
packages: [docker.io, docker-compose-plugin]
runcmd:
  - systemctl enable --now docker
  - docker compose -f /srv/app/docker-compose.yml up -d
""",

    "universal_excerpt": """
platforms:
  hetzner:
    location: fsn1
    server_type: cx22
    image: debian-12
    ssh_keys: [ops-key]
    cloud_init: cloud-init.yaml
    firewall_rules:
      - { direction: in, protocol: tcp, port_range: \"22\",  source_cidrs: [\"0.0.0.0/0\", \"::/0\"] }
      - { direction: in, protocol: tcp, port_range: \"443\", source_cidrs: [\"0.0.0.0/0\", \"::/0\"] }
""",

    "compatibility_extras": "",

    "deploy_button": {
        "markdown": "[![Create Hetzner server](https://img.shields.io/badge/Create%20on-Hetzner-red)](https://console.hetzner.cloud/projects)",
        "html": (
            '<a href="https://console.hetzner.cloud/projects">\n'
            '  <img src="https://img.shields.io/badge/Create%20on-Hetzner-red" alt="Create on Hetzner" />\n'
            '</a>'
        ),
        "params_doc": "Hetzner has no native Deploy button. Use Terraform or `hcloud` CLI driven by this manifest; the linked console shortcut is for convenience.",
    },

    "perks": STANDARD_PERKS,

    "examples": {
        "static-site": """
version: \"1.0\"
name: Hetzner Static Site
type: site
summary: Static site on Hetzner Cloud via cloud-init and caddy.
description: cx22 in fsn1 with caddy serving static files from /srv/site.

platforms:
  hetzner:
    location: fsn1
    server_type: cx22
    image: debian-12
    ssh_keys: [ops-key]
    cloud_init: cloud-init-caddy.yaml
    firewall_rules:
      - { direction: in, protocol: tcp, port_range: \"80\",  source_cidrs: [\"0.0.0.0/0\", \"::/0\"] }
      - { direction: in, protocol: tcp, port_range: \"443\", source_cidrs: [\"0.0.0.0/0\", \"::/0\"] }

safety:
  min_permissions: [network:inbound]
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [hetzner]

metadata:
  license: Apache-2.0
  author: { name: Static Co., handle: static-co }
  source: { type: git, url: https://github.com/static-co/hetzner-static }
  id: com.static-co.hetzner-static
""",
        "serverless-api": """
version: \"1.0\"
name: Hetzner Docker API
type: api-service
summary: Dockerised API on Hetzner Cloud with an attached volume.
description: cpx31 in nbg1 with docker-compose starting the API and Postgres container; a 20GB volume for Postgres data.

platforms:
  hetzner:
    location: nbg1
    server_type: cpx31
    image: debian-12
    ssh_keys: [ops-key]
    cloud_init: cloud-init-docker.yaml
    volumes:
      - { name: postgres, size_gb: 20, mount: /var/lib/postgresql }
    firewall_rules:
      - { direction: in, protocol: tcp, port_range: \"443\", source_cidrs: [\"0.0.0.0/0\", \"::/0\"] }
      - { direction: in, protocol: tcp, port_range: \"22\",  source_cidrs: [\"10.0.0.0/8\"] }

safety:
  min_permissions: [network:inbound, network:outbound, fs:write:/var/lib/postgresql]
  rate_limit_qps: 50

env_vars_required:
  - name: POSTGRES_PASSWORD
    description: Postgres password baked into cloud-init.
    secret: true

deployment:
  targets: [hetzner]

metadata:
  license: Apache-2.0
  author: { name: API Co., handle: api-co }
  source: { type: git, url: https://github.com/api-co/hetzner-docker-api }
  id: com.api-co.hetzner-docker-api
""",
        "full-stack-app": """
version: \"1.0\"
name: Hetzner Full Stack
type: web-app
summary: Full-stack Hetzner deployment with private network, two volumes, k3s, and restrictive firewall.
description: >
  Single-node k3s on a cpx41 in helsinki with two volumes (data +
  logs), attached to a private network, reachable only over TLS + SSH
  from the office CIDR.

platforms:
  hetzner:
    location: hel1
    server_type: cpx41
    image: debian-12
    ssh_keys: [ops-key]
    cloud_init: cloud-init-k3s.yaml
    volumes:
      - { name: data, size_gb: 100, mount: /var/lib/rancher/k3s }
      - { name: logs, size_gb: 20,  mount: /var/log/app }
    networks: [private]
    firewall_rules:
      - { direction: in,  protocol: tcp, port_range: \"443\", source_cidrs: [\"0.0.0.0/0\", \"::/0\"] }
      - { direction: in,  protocol: tcp, port_range: \"22\",  source_cidrs: [\"203.0.113.0/24\"] }
      - { direction: out, protocol: tcp, port_range: \"1-65535\" }

safety:
  min_permissions: [network:inbound, network:outbound, fs:read, fs:write]
  cost_limit_usd_daily: 5
  safe_for_auto_spawn: false
  data_residency: [eu]

env_vars_required:
  - name: ACME_EMAIL
    description: Email used for Let's Encrypt ACME.
  - name: POSTGRES_PASSWORD
    description: Postgres password baked into cloud-init.
    secret: true

deployment:
  targets: [hetzner]

metadata:
  license: MIT
  author: { name: Stack Co., handle: stack-co }
  source: { type: git, url: https://github.com/stack-co/hetzner-full-stack }
  id: com.stack-co.hetzner-full-stack
""",
    },
}
