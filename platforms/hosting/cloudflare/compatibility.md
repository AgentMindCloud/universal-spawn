# Cloudflare compatibility — field-by-field

Cloudflare already has a native config format
(`wrangler.toml`). universal-spawn does not replace it; the two
coexist. A Cloudflare consumer reads both:

- `wrangler.toml` for provider-specific knobs the universal-spawn
  extension does not (yet) model.
- `universal-spawn.yaml` (with `platforms.cloudflare`) for the
  cross-platform manifest.

The two files **MUST NOT** disagree on fields that appear in both; a
consumer that detects a conflict MUST warn and prefer `universal-spawn.yaml`.

## Side-by-side

### `wrangler.toml` (provider-native)

```toml
name = "my-worker"
main = "src/index.ts"
compatibility_date = "2025-01-15"
compatibility_flags = ["nodejs_compat"]

[[r2_buckets]]
binding = "ASSETS"
bucket_name = "my-assets"

[[d1_databases]]
binding = "DB"
database_name = "my-db"
database_id = "00000000-0000-0000-0000-000000000000"

[[kv_namespaces]]
binding = "CACHE"
id = "00000000000000000000000000000000"
```

### `universal-spawn.yaml` (platforms.cloudflare block)

```yaml
platforms:
  cloudflare:
    surface: workers
    main: src/index.ts
    compatibility_date: "2025-01-15"
    nodejs_compat: true
    bindings:
      r2:
        - { binding: ASSETS, bucket_name: my-assets }
      d1:
        - { binding: DB, database_name: my-db, database_id: 00000000-0000-0000-0000-000000000000 }
      kv:
        - { binding: CACHE, id: "00000000000000000000000000000000" }
```

## Field-by-field

| universal-spawn v1.0 field | Cloudflare behavior |
|---|---|
| `version` | Required. |
| `metadata.id` | Default Worker name. |
| `name, description` | Dashboard card. |
| `type` | `web-app`, `api-service`, `site`, `workflow`. |
| `safety.min_permissions` | Informational. |
| `safety.cost_limit_usd_daily` | Advisory; Cloudflare's billing is plan-based. |
| `env_vars_required` | Wrangler secrets; missing required blocks deploy. |
| `platforms.cloudflare.surface` | `workers` or `pages`. |
| `platforms.cloudflare.main` | Entry script path (Workers surface). |
| `platforms.cloudflare.build` | Pages build command + output dir. |
| `platforms.cloudflare.compatibility_date` | Compatibility date (YYYY-MM-DD). |
| `platforms.cloudflare.nodejs_compat` | nodejs_compat flag. |
| `platforms.cloudflare.routes` | HTTP routes (Workers). |
| `platforms.cloudflare.bindings.r2` | R2 bucket bindings. |
| `platforms.cloudflare.bindings.d1` | D1 database bindings. |
| `platforms.cloudflare.bindings.kv` | KV namespace bindings. |
| `platforms.cloudflare.bindings.queues` | Queue bindings (producer + consumer). |
| `platforms.cloudflare.bindings.durable_objects` | Durable Object bindings. |
| `platforms.cloudflare.bindings.services` | Service bindings (Worker-to-Worker). |

## What to keep where

- Use **`wrangler.toml`** for per-environment overrides (`[env.preview]`, `[env.production]`), `triggers.crons[]`, custom domains, and tail logs config.
- Use **`universal-spawn.yaml`** for cross-platform siblings (e.g. a `platforms.vercel` parallel deployment) plus `env_vars_required`, safety, metadata.

