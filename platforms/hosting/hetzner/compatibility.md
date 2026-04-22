# Hetzner Cloud compatibility — field-by-field

Hetzner Cloud already has a native config format
(`cloud-init.yaml (+ hcloud CLI)`). universal-spawn does not replace it; the two
coexist. A Hetzner Cloud consumer reads both:

- `cloud-init.yaml (+ hcloud CLI)` for provider-specific knobs the universal-spawn
  extension does not (yet) model.
- `universal-spawn.yaml` (with `platforms.hetzner`) for the
  cross-platform manifest.

The two files **MUST NOT** disagree on fields that appear in both; a
consumer that detects a conflict MUST warn and prefer `universal-spawn.yaml`.

## Side-by-side

### `cloud-init.yaml (+ hcloud CLI)` (provider-native)

```yaml
#cloud-config
package_update: true
package_upgrade: true
packages: [docker.io, docker-compose-plugin]
runcmd:
  - systemctl enable --now docker
  - docker compose -f /srv/app/docker-compose.yml up -d
```

### `universal-spawn.yaml` (platforms.hetzner block)

```yaml
platforms:
  hetzner:
    location: fsn1
    server_type: cx22
    image: debian-12
    ssh_keys: [ops-key]
    cloud_init: cloud-init.yaml
    firewall_rules:
      - { direction: in, protocol: tcp, port_range: "22",  source_cidrs: ["0.0.0.0/0", "::/0"] }
      - { direction: in, protocol: tcp, port_range: "443", source_cidrs: ["0.0.0.0/0", "::/0"] }
```

## Field-by-field

| universal-spawn v1.0 field | Hetzner Cloud behavior |
|---|---|
| `version` | Required. |
| `metadata.id` | Server name suggestion. |
| `name, description` | Card. |
| `type` | See above. |
| `safety.*` | Informational. |
| `env_vars_required` | Cloud-init / dotenv. |
| `platforms.hetzner.location` | Datacenter. |
| `platforms.hetzner.server_type` | Server type id. |
| `platforms.hetzner.image` | OS image. |
| `platforms.hetzner.ssh_keys` | SSH key names. |
| `platforms.hetzner.cloud_init` | cloud-init config path. |
| `platforms.hetzner.volumes` | Attached volumes. |
| `platforms.hetzner.networks` | Attached private networks. |
| `platforms.hetzner.firewall_rules` | Firewall ruleset. |


