# Linode (Akamai Cloud) compatibility — field-by-field

Linode (Akamai Cloud) already has a native config format
(`StackScript + linode-cli`). universal-spawn does not replace it; the two
coexist. A Linode (Akamai Cloud) consumer reads both:

- `StackScript + linode-cli` for provider-specific knobs the universal-spawn
  extension does not (yet) model.
- `universal-spawn.yaml` (with `platforms.linode`) for the
  cross-platform manifest.

The two files **MUST NOT** disagree on fields that appear in both; a
consumer that detects a conflict MUST warn and prefer `universal-spawn.yaml`.

## Side-by-side

### `StackScript + linode-cli` (provider-native)

```bash
#!/usr/bin/env bash
# StackScript UDF vars come in as $APP_DOMAIN etc.
set -euxo pipefail
apt-get update -y
apt-get install -y docker.io docker-compose-plugin
systemctl enable --now docker
git clone https://github.com/yourhandle/your-project /srv/app
cd /srv/app
docker compose up -d
```

### `universal-spawn.yaml` (platforms.linode block)

```yaml
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
```

## Field-by-field

| universal-spawn v1.0 field | Linode (Akamai Cloud) behavior |
|---|---|
| `version` | Required. |
| `metadata.id` | Linode label suggestion. |
| `name, description` | Card. |
| `type` | See above. |
| `safety.*` | Informational. |
| `env_vars_required` | StackScript env. |
| `platforms.linode.region` | Region. |
| `platforms.linode.instance_type` | Linode plan. |
| `platforms.linode.image` | Image. |
| `platforms.linode.stackscript` | StackScript id + UDF answers. |
| `platforms.linode.volumes` | Block-storage volumes. |
| `platforms.linode.private_ip` | Private IP toggle. |
| `platforms.linode.backups` | Automatic backups toggle. |


