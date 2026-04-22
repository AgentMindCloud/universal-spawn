# Cloudflare — universal-spawn platform extension

Cloudflare's developer platform spans Workers, Pages, R2 (object storage), D1 (SQLite at the edge), KV (key-value), Queues, and Durable Objects. The extension covers all four primary surfaces — Workers, Pages, R2 buckets, D1 databases — plus the bindings that glue them together.

## What this platform cares about

The surface (`workers`, `pages`), the entry script, the bindings map (KV, R2, D1, Queues, Durable Objects, service bindings), and whether the creation runs on the `nodejs_compat` runtime.

## What platform-specific extras unlock

`bindings.r2[]`, `bindings.d1[]`, `bindings.kv[]` declare resources and the binding name the Worker imports them as. `nodejs_compat: true` enables the Node.js compatibility mode.

## Compatibility table

| Manifest field | Cloudflare behavior |
|---|---|
| `version` | Required `"1.0"`. |
| `name, description` | Worker / Pages project name + card. |
| `type` | `web-app`, `api-service`, `site`, `workflow`. |
| `env_vars_required` | Wrangler secret upload; missing required block deploy. |
| `deployment.targets` | Must include `cloudflare`. |
| `platforms.cloudflare` | Strict. |

### `platforms.cloudflare` fields

| Field | Purpose |
|---|---|
| `platforms.cloudflare.surface` | `workers` or `pages`. |
| `platforms.cloudflare.main` | Worker entry script path. |
| `platforms.cloudflare.build` | Pages build settings. |
| `platforms.cloudflare.compatibility_date` | Compatibility date. |
| `platforms.cloudflare.nodejs_compat` | Enable nodejs_compat. |
| `platforms.cloudflare.routes` | HTTP routes (Workers). |
| `platforms.cloudflare.bindings` | Resource bindings (R2 / D1 / KV / Queues / Durable Objects / services). |

See [`compatibility.md`](./compatibility.md) for the side-by-side diff
against `wrangler.toml`, [`deploy-button.md`](./deploy-button.md)
for the canonical Deploy-button recipe, and [`perks.md`](./perks.md) for
what a conformant Cloudflare consumer SHOULD offer manifests that
declare `platforms.cloudflare`.
