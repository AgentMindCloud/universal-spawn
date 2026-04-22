# Railway compatibility — field-by-field

Railway already has a native config format
(`railway.json`). universal-spawn does not replace it; the two
coexist. A Railway consumer reads both:

- `railway.json` for provider-specific knobs the universal-spawn
  extension does not (yet) model.
- `universal-spawn.yaml` (with `platforms.railway`) for the
  cross-platform manifest.

The two files **MUST NOT** disagree on fields that appear in both; a
consumer that detects a conflict MUST warn and prefer `universal-spawn.yaml`.

## Side-by-side

### `railway.json` (provider-native)

```json
{
  "$schema": "https://railway.app/railway.schema.json",
  "build": { "builder": "NIXPACKS" },
  "deploy": {
    "startCommand": "pnpm start",
    "healthcheckPath": "/healthz",
    "healthcheckTimeout": 10,
    "numReplicas": 1,
    "restartPolicyType": "ON_FAILURE"
  }
}
```

### `universal-spawn.yaml` (platforms.railway block)

```yaml
platforms:
  railway:
    build: { provider: nixpacks }
    start_command: "pnpm start"
    healthcheck: { path: /healthz, timeout_seconds: 10 }
    replicas: 1
    plugins:
      - { kind: postgresql, name: db }
```

## Field-by-field

| universal-spawn v1.0 field | Railway behavior |
|---|---|
| `version` | Required. |
| `metadata.id` | Service-id suggestion. |
| `name, description` | Railway card. |
| `type` | `web-app`, `api-service`, `container`, `workflow`, `bot`. |
| `safety.min_permissions` | Informational. |
| `safety.cost_limit_usd_daily` | Advisory; Railway enforces at project. |
| `env_vars_required` | Railway secrets. |
| `platforms.railway.build` | Build provider + Dockerfile/Nixpacks settings. |
| `platforms.railway.start_command` | Start command. |
| `platforms.railway.healthcheck` | Healthcheck path. |
| `platforms.railway.plugins` | Managed services (Postgres/Redis/Mongo/MySQL). |
| `platforms.railway.replicas` | Replica count. |
| `platforms.railway.region` | Railway region. |
| `platforms.railway.template` | Template-registration block. |

## What to keep where

- Use **`railway.json`** for the `restartPolicyType`, preview deploy triggers, and webhook configuration.
- Use **`universal-spawn.yaml`** for cross-platform parity and the plugin roster.

