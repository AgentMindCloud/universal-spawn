# DigitalOcean compatibility — field-by-field

DigitalOcean already has a native config format
(`app.yaml (App Platform) / project.yml (Functions)`). universal-spawn does not replace it; the two
coexist. A DigitalOcean consumer reads both:

- `app.yaml (App Platform) / project.yml (Functions)` for provider-specific knobs the universal-spawn
  extension does not (yet) model.
- `universal-spawn.yaml` (with `platforms.digitalocean`) for the
  cross-platform manifest.

The two files **MUST NOT** disagree on fields that appear in both; a
consumer that detects a conflict MUST warn and prefer `universal-spawn.yaml`.

## Side-by-side

### `app.yaml (App Platform) / project.yml (Functions)` (provider-native)

```yaml
name: your-app
region: nyc
services:
  - name: web
    instance_size_slug: basic-xs
    instance_count: 1
    build_command: pnpm build
    run_command: pnpm start
    http_port: 8080
databases:
  - name: db
    engine: PG
    size: db-s-dev
```

### `universal-spawn.yaml` (platforms.digitalocean block)

```yaml
platforms:
  digitalocean:
    surface: app_platform
    region: nyc
    services:
      - name: web
        kind: web
        instance_size: basic-xs
        instance_count: 1
        build_command: "pnpm build"
        run_command: "pnpm start"
        http_port: 8080
    databases:
      - { name: db, engine: PG, size: db-s-dev }
```

## Field-by-field

| universal-spawn v1.0 field | DigitalOcean behavior |
|---|---|
| `version` | Required. |
| `metadata.id` | App name suggestion. |
| `name, description` | Card. |
| `type` | See above. |
| `safety.*` | Informational. |
| `env_vars_required` | App Platform component env. |
| `platforms.digitalocean.surface` | `app_platform` or `functions`. |
| `platforms.digitalocean.region` | Region slug. |
| `platforms.digitalocean.services` | App Platform components. |
| `platforms.digitalocean.databases` | Managed databases. |
| `platforms.digitalocean.functions` | Functions runtime config. |


