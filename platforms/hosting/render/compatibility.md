# Render compatibility — field-by-field

Render already has a native config format
(`render.yaml`). universal-spawn does not replace it; the two
coexist. A Render consumer reads both:

- `render.yaml` for provider-specific knobs the universal-spawn
  extension does not (yet) model.
- `universal-spawn.yaml` (with `platforms.render`) for the
  cross-platform manifest.

The two files **MUST NOT** disagree on fields that appear in both; a
consumer that detects a conflict MUST warn and prefer `universal-spawn.yaml`.

## Side-by-side

### `render.yaml` (provider-native)

```yaml
services:
  - name: web
    type: web
    runtime: node
    plan: starter
    buildCommand: pnpm install && pnpm build
    startCommand: pnpm start
    healthCheckPath: /healthz
    autoDeploy: true
    envVars:
      - fromGroup: app

databases:
  - name: db
    plan: starter
    postgresMajorVersion: 16

envVarGroups:
  - name: app
```

### `universal-spawn.yaml` (platforms.render block)

```yaml
platforms:
  render:
    services:
      - name: web
        kind: web
        runtime: node
        plan: starter
        build_command: "pnpm install && pnpm build"
        start_command: "pnpm start"
        health_check_path: /healthz
        auto_deploy: true
        env_var_group: app
    databases:
      - { name: db, kind: postgresql, plan: starter, postgres_major_version: 16 }
    env_var_groups:
      - { name: app }
```

## Field-by-field

| universal-spawn v1.0 field | Render behavior |
|---|---|
| `version` | Required. |
| `metadata.id` | Suggested Blueprint name. |
| `name, description` | Blueprint card. |
| `type` | `web-app`, `api-service`, `container`, `workflow`, `bot`. |
| `safety.*` | Informational. |
| `env_vars_required` | Dashboard / envVarGroups. |
| `platforms.render.services` | Render services (`web`, `worker`, `cron`, `static`, `private_service`). |
| `platforms.render.databases` | Managed Postgres. |
| `platforms.render.env_var_groups` | Shared env var groups. |
| `platforms.render.region` | Render region. |

## What to keep where

- Use **`render.yaml`** for per-service `envVars[]` with `generateValue`, `sync: false`, and the fine-grained control over Render's environment-synchronisation rules.
- Use **`universal-spawn.yaml`** for the service-level shape and cross-platform parity.

