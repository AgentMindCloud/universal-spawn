# Vultr compatibility — field-by-field

Vultr already has a native config format
(`cloud-init.yaml + Vultr API`). universal-spawn does not replace it; the two
coexist. A Vultr consumer reads both:

- `cloud-init.yaml + Vultr API` for provider-specific knobs the universal-spawn
  extension does not (yet) model.
- `universal-spawn.yaml` (with `platforms.vultr`) for the
  cross-platform manifest.

The two files **MUST NOT** disagree on fields that appear in both; a
consumer that detects a conflict MUST warn and prefer `universal-spawn.yaml`.

## Side-by-side

### `cloud-init.yaml + Vultr API` (provider-native)

```yaml
#cloud-config
package_update: true
packages: [docker.io, docker-compose-plugin]
runcmd:
  - systemctl enable --now docker
  - docker compose -f /srv/app/docker-compose.yml up -d
```

### `universal-spawn.yaml` (platforms.vultr block)

```yaml
platforms:
  vultr:
    region: ewr
    plan: vc2-2c-4gb
    os: Ubuntu 24.04 LTS x64
    cloud_init: cloud-init.yaml
    backups: true
```

## Field-by-field

| universal-spawn v1.0 field | Vultr behavior |
|---|---|
| `version` | Required. |
| `metadata.id` | Label suggestion. |
| `name, description` | Card. |
| `type` | See above. |
| `safety.*` | Informational. |
| `env_vars_required` | Cloud-init env. |
| `platforms.vultr.region` | Region slug. |
| `platforms.vultr.plan` | Plan id. |
| `platforms.vultr.os` | OS slug. |
| `platforms.vultr.cloud_init` | cloud-init user-data path. |
| `platforms.vultr.block_storage` | Attached block storage. |
| `platforms.vultr.vpc` | Private VPCs. |
| `platforms.vultr.managed_databases` | Managed databases. |
| `platforms.vultr.firewall_group` | Attached firewall group. |
| `platforms.vultr.backups` | Automatic backups. |


