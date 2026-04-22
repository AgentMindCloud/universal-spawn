# Fly.io — universal-spawn platform extension

Fly.io runs your Dockerfile as Firecracker microVMs, globally distributed, with anycast networking and built-in Postgres / Redis-compatible storage. The extension describes the VM size, regions, services, mounts, and any required app-level secrets.

## What this platform cares about

The app name (fly-unique), primary region, per-machine VM size, HTTP services (ports, TLS, auto-stop), and mounted volumes.

## What platform-specific extras unlock

`http_service` maps the primary HTTP port with TLS + force HTTPS. `mounts[]` attaches persistent volumes. `processes[]` runs multiple entry commands from the same image.

## Compatibility table

| Manifest field | Fly.io behavior |
|---|---|
| `version` | Required. |
| `name, description` | Fly app card. |
| `type` | `web-app`, `api-service`, `container`, `workflow`, `bot`. |
| `env_vars_required` | Fly secrets. |
| `deployment.targets` | Must include `fly-io`. |
| `platforms.fly-io` | Strict. |

### `platforms.fly-io` fields

| Field | Purpose |
|---|---|
| `platforms.fly-io.app` | App name. |
| `platforms.fly-io.primary_region` | Primary region. |
| `platforms.fly-io.regions` | Replica regions. |
| `platforms.fly-io.vm` | VM size. |
| `platforms.fly-io.http_service` | HTTP service port / TLS / auto-stop. |
| `platforms.fly-io.mounts` | Persistent volume mounts. |
| `platforms.fly-io.processes` | Process group commands. |
| `platforms.fly-io.healthcheck` | HTTP healthcheck. |

See [`compatibility.md`](./compatibility.md) for the side-by-side diff
against `fly.toml`, [`deploy-button.md`](./deploy-button.md)
for the canonical Deploy-button recipe, and [`perks.md`](./perks.md) for
what a conformant Fly.io consumer SHOULD offer manifests that
declare `platforms.fly-io`.
