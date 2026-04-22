# Supabase compatibility — field-by-field

Supabase already has a native config format
(`supabase/config.toml`). universal-spawn does not replace it; the two
coexist. A Supabase consumer reads both:

- `supabase/config.toml` for provider-specific knobs the universal-spawn
  extension does not (yet) model.
- `universal-spawn.yaml` (with `platforms.supabase`) for the
  cross-platform manifest.

The two files **MUST NOT** disagree on fields that appear in both; a
consumer that detects a conflict MUST warn and prefer `universal-spawn.yaml`.

## Side-by-side

### `supabase/config.toml` (provider-native)

```toml
[db]
major_version = 16

[db.pooler]
enabled = true
default_pool_mode = "transaction"

[auth]
site_url = "http://localhost:3000"
jwt_expiry = 3600

[auth.external.github]
enabled = true

[[storage.buckets]]
name = "avatars"
public = true
file_size_limit = "5MiB"
```

### `universal-spawn.yaml` (platforms.supabase block)

```yaml
platforms:
  supabase:
    project_ref: "abcdefghijklmnopqrst"
    region: us-east-1
    db:
      postgres_major_version: 16
      migrations_dir: supabase/migrations
      pooler: transaction
    auth:
      providers: [email, github]
      site_url: https://your-app.example.com
      jwt_expiry_seconds: 3600
    storage:
      buckets:
        - { name: avatars, public: true, max_file_size_mb: 5 }
```

## Field-by-field

| universal-spawn v1.0 field | Supabase behavior |
|---|---|
| `version` | Required. |
| `metadata.id` | Project-slug suggestion. |
| `name, description` | Dashboard card. |
| `type` | `web-app`, `api-service`, `workflow`, `container`. |
| `safety.min_permissions` | Informational. |
| `safety.cost_limit_usd_daily` | Advisory; enforced at project plan level. |
| `env_vars_required` | Dashboard secrets + per-function env. |
| `platforms.supabase.project_ref` | Project reference (20 chars). |
| `platforms.supabase.region` | Supabase region. |
| `platforms.supabase.db` | Postgres configuration + migrations. |
| `platforms.supabase.auth` | Auth providers + URL. |
| `platforms.supabase.storage` | Storage buckets. |
| `platforms.supabase.realtime` | Realtime channels. |
| `platforms.supabase.edge_functions` | Deno Edge Functions. |

## DB provisioning as first-class

Supabase treats Postgres migrations as a deployment artifact, not an afterthought. `db.migrations_dir` is where a consumer finds `*.sql` files to apply with `supabase db push`. `seed_file` seeds development data. The universal-spawn consumer MUST run migrations (in the provided order) before marking the first deploy healthy.
