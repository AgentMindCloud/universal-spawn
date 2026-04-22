# Vercel compatibility — field-by-field

Vercel already has a native config format
(`vercel.json`). universal-spawn does not replace it; the two
coexist. A Vercel consumer reads both:

- `vercel.json` for provider-specific knobs the universal-spawn
  extension does not (yet) model.
- `universal-spawn.yaml` (with `platforms.vercel`) for the
  cross-platform manifest.

The two files **MUST NOT** disagree on fields that appear in both; a
consumer that detects a conflict MUST warn and prefer `universal-spawn.yaml`.

## Side-by-side

### `vercel.json` (provider-native)

```json
{
  "framework": "nextjs",
  "installCommand": "pnpm install",
  "buildCommand": "pnpm build",
  "outputDirectory": ".next",
  "regions": ["iad1"],
  "functions": {
    "api/*.ts": { "runtime": "edge", "memory": 256, "maxDuration": 15 }
  }
}
```

### `universal-spawn.yaml` (platforms.vercel block)

```yaml
platforms:
  vercel:
    framework: nextjs
    install_command: "pnpm install"
    build_command: "pnpm build"
    output: .next
    regions: [iad1]
    functions:
      - match: "api/*.ts"
        runtime: edge
        memory_mb: 256
        max_duration_seconds: 15
```

## Field-by-field

| universal-spawn v1.0 field | Vercel behavior |
|---|---|
| `version` | Required. |
| `metadata.id` | Default project-name suggestion; user may rename. |
| `name, description` | Card + dashboard text. |
| `type` | `web-app`, `api-service`, `site`, `container`, `workflow`. |
| `safety.min_permissions` | Surfaced in project settings; not sandbox-enforced. |
| `safety.cost_limit_usd_daily` | Advisory; spend-management honors it when linked. |
| `env_vars_required` | Build-blocking gate. |
| `platforms.vercel.framework` | Preset → Vercel builder. |
| `platforms.vercel.install_command` | Overrides autodetect. |
| `platforms.vercel.build_command` | Overrides autodetect. |
| `platforms.vercel.output` | Build output directory. |
| `platforms.vercel.root_directory` | Monorepo subdir. |
| `platforms.vercel.regions` | Deploy-region codes (e.g. `iad1`, `cdg1`). |
| `platforms.vercel.functions` | Per-route runtime / memory / maxDuration. |
| `platforms.vercel.env_promotion` | Scopes where required secrets must exist. |

## What to keep where

- Use **`vercel.json`** for one-off knobs the schema does not yet model (`crons[]`, `headers[]`, `redirects[]`, `rewrites[]`, per-project image-optimization config).
- Use **`universal-spawn.yaml`** for everything that makes the creation discoverable and spawnable on non-Vercel platforms too (`metadata`, `safety`, `env_vars_required`, cross-platform `platforms.*` siblings).
- A minor-version bump of the universal schema will absorb `crons[]`, `redirects[]`, and `rewrites[]`; until then they stay in `vercel.json`.
