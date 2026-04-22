# Supabase — universal-spawn platform extension

Supabase is an open-source Firebase alternative built on Postgres. A universal-spawn manifest targeting Supabase treats database provisioning as a first-class deployment concern: the manifest declares the Postgres schema migrations, the Auth providers, the Storage buckets, the Realtime channels, and any Edge Functions — all in one place.

## What this platform cares about

The project reference, the Postgres migration directory, the Auth provider list, the storage buckets, the realtime channels, and the Edge Functions.

## What platform-specific extras unlock

`db.migrations_dir` points at SQL migration files. `edge_functions[]` lists Deno-based functions deployed via `supabase functions deploy`.

## Compatibility table

| Manifest field | Supabase behavior |
|---|---|
| `version` | Required. |
| `name, description` | Project dashboard. |
| `type` | `web-app`, `api-service`, `workflow`, `container`. |
| `env_vars_required` | Supabase secrets + per-function env. |
| `deployment.targets` | Must include `supabase`. |
| `platforms.supabase` | Strict. |

### `platforms.supabase` fields

| Field | Purpose |
|---|---|
| `platforms.supabase.project_ref` | Project reference. |
| `platforms.supabase.region` | Supabase region. |
| `platforms.supabase.db` | Postgres configuration + migrations. |
| `platforms.supabase.auth` | Auth providers + redirect URLs. |
| `platforms.supabase.storage` | Storage buckets. |
| `platforms.supabase.realtime` | Realtime channels. |
| `platforms.supabase.edge_functions` | Edge Functions. |

See [`compatibility.md`](./compatibility.md) for the side-by-side diff
against `supabase/config.toml`, [`deploy-button.md`](./deploy-button.md)
for the canonical Deploy-button recipe, and [`perks.md`](./perks.md) for
what a conformant Supabase consumer SHOULD offer manifests that
declare `platforms.supabase`.
