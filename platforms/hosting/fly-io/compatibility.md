# Fly.io compatibility — field-by-field

Fly.io already has a native config format
(`fly.toml`). universal-spawn does not replace it; the two
coexist. A Fly.io consumer reads both:

- `fly.toml` for provider-specific knobs the universal-spawn
  extension does not (yet) model.
- `universal-spawn.yaml` (with `platforms.fly-io`) for the
  cross-platform manifest.

The two files **MUST NOT** disagree on fields that appear in both; a
consumer that detects a conflict MUST warn and prefer `universal-spawn.yaml`.

## Side-by-side

### `fly.toml` (provider-native)

```toml
app = "your-app"
primary_region = "iad"

[build]
  dockerfile = "Dockerfile"

[http_service]
  internal_port = 8080
  force_https = true
  auto_stop_machines = true
  auto_start_machines = true
  min_machines_running = 0

[[vm]]
  size = "shared-cpu-1x"
  memory = "512mb"

[[mounts]]
  source = "data"
  destination = "/data"
```

### `universal-spawn.yaml` (platforms.fly-io block)

```yaml
platforms:
  fly-io:
    app: your-app
    primary_region: iad
    vm: { size: shared-cpu-1x, memory_mb: 512 }
    http_service:
      internal_port: 8080
      force_https: true
      auto_stop_machines: true
      auto_start_machines: true
      min_machines_running: 0
    mounts:
      - { source: data, destination: /data, size_gb: 1 }
```

## Field-by-field

| universal-spawn v1.0 field | Fly.io behavior |
|---|---|
| `version` | Required. |
| `metadata.id` | Fly app-name suggestion. |
| `name, description` | Card. |
| `type` | `web-app`, `api-service`, `container`, `workflow`, `bot`. |
| `safety.min_permissions` | Informational. |
| `safety.cost_limit_usd_daily` | Advisory; Fly has its own spend guardrails. |
| `env_vars_required` | `fly secrets set`. |
| `platforms.fly-io.app` | App name. |
| `platforms.fly-io.primary_region` | Primary region. |
| `platforms.fly-io.regions` | Replica regions. |
| `platforms.fly-io.vm` | VM size. |
| `platforms.fly-io.http_service` | HTTP service ports + TLS. |
| `platforms.fly-io.mounts` | Volume mounts. |
| `platforms.fly-io.processes` | Process group commands. |
| `platforms.fly-io.healthcheck` | HTTP healthcheck. |

## What to keep where

- Use **`fly.toml`** for `[build]` args, `[env]` (non-secret), `[metrics]`, `[statics]`, and machine-level settings (kernel, swap).
- Use **`universal-spawn.yaml`** for the manifest-level safety, secrets, and cross-platform siblings.

