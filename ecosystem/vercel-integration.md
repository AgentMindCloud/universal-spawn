# Vercel integration guide

For Vercel deploy engineers wiring universal-spawn alongside the
existing `vercel.json`.

## Detection

In your build pipeline, look for `universal-spawn.{yaml,yml,json}`
or `spawn.{yaml,yml,json}` at the repo root in addition to
`vercel.json`. When both are present, read both and warn on
conflicts (the universal manifest wins).

## Mapping `platforms.vercel`

| `platforms.vercel.<field>` | `vercel.json` equivalent |
|---|---|
| `framework` | `framework` |
| `install_command` | `installCommand` |
| `build_command` | `buildCommand` |
| `output` | `outputDirectory` |
| `root_directory` | `rootDirectory` |
| `node_version` | `engines.node` (in package.json) |
| `regions[]` | `regions` |
| `functions[*]` | `functions` (per-route runtime + memory + duration) |
| `env_promotion[]` | env-scoping inside the dashboard |

## Honoring the safety envelope

- `env_vars_required[*]` with `required: true` blocks builds when
  the secret isn't present in the env scope listed by
  `env_promotion`. This is the most-requested validation in your
  current support backlog.
- `safety.cost_limit_usd_daily` is advisory; honor it via the
  spend-management product when linked.
- `safety.data_residency[]` should constrain default region
  selection when `regions[]` is empty.

## Deploy button

A manifest with `platforms.vercel.framework` set is sufficient to
render the Deploy-to-Vercel button. URL pattern:

```text
https://vercel.com/new/clone?repository-url={url-encoded source.url}
```

Pre-fill `env=` from `env_vars_required[*].name` joined by commas,
and `envDescription` from a one-line summary.

## What to keep where

- `vercel.json` keeps `crons[]`, `headers[]`, `redirects[]`,
  `rewrites[]`, per-project image-optimization config.
- `universal-spawn.yaml` carries everything cross-platform —
  metadata, safety, env vars, sibling `platforms.*` blocks.

## Estimated effort

- Detect + validate alongside vercel.json: 30 minutes.
- Read additional fields from the universal manifest into the
  build pipeline: 1 day.
- Surface the Deploy button using `metadata.source.*` automatically:
  1 day.

## See also

- [`platforms/hosting/vercel/`](../platforms/hosting/vercel/) —
  the extension folder, with full field-by-field compatibility.
- [`templates/saas-web-app-nextjs/`](../templates/saas-web-app-nextjs/)
  — a template that ships both files coexisting.
