# Migrating from `vercel.json`

If your repository already ships a `vercel.json`, migrating to
universal-spawn is a paste-plus-rename job: Vercel keeps honoring
your `vercel.json`, and `universal-spawn.yaml` becomes the
cross-platform manifest on top of it.

## The starting `vercel.json`

A representative `vercel.json` from a Next.js project:

```json
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "framework": "nextjs",
  "buildCommand": "pnpm build",
  "installCommand": "pnpm install --frozen-lockfile",
  "outputDirectory": ".next",
  "regions": ["iad1", "cdg1", "hnd1"],
  "functions": {
    "app/api/**/*.ts": {
      "runtime": "edge",
      "memory": 256,
      "maxDuration": 15
    }
  },
  "env": {
    "NEXT_PUBLIC_SITE_URL": "https://fielded.lab"
  }
}
```

## The target `universal-spawn.yaml`

```yaml
version: "1.0"
name: Fielded Web
type: web-app
summary: Public site for the Fielded research assistant.
description: >
  Next.js 15 app that renders Fielded's public marketing site and a
  small API for waitlist signups. Deploys to Vercel in iad1, cdg1, and
  hnd1.

platforms:
  vercel:
    framework: nextjs
    install_command: "pnpm install --frozen-lockfile"
    build_command: "pnpm build"
    output: ".next"
    node_version: "20"
    regions: [iad1, cdg1, hnd1]
    functions:
      - match: "app/api/**/*.ts"
        runtime: edge
        memory_mb: 256
        max_duration_seconds: 15
    env_promotion: [production, preview]

safety:
  min_permissions:
    - network:inbound
    - network:outbound:api.resend.com
  rate_limit_qps: 100
  cost_limit_usd_daily: 25
  safe_for_auto_spawn: false

deployment:
  targets: [vercel]
  regions: [iad1, cdg1, hnd1]
  build:
    command: "pnpm build"
    output: ".next"
    engine: "node"
    install: "pnpm install --frozen-lockfile"
    node_version: "20"

env_vars_required:
  - name: DATABASE_URL
    description: Connection string for the primary database.
    secret: true
  - name: RESEND_API_KEY
    description: Resend API key used for transactional email.
    secret: true
  - name: NEXT_PUBLIC_SITE_URL
    description: Public URL the app serves from.
    required: false
    example: "https://fielded.lab"

metadata:
  license: MIT
  author:
    name: Jani Solo
    handle: JanSol0s
    org: AgentMindCloud
  source:
    type: git
    url: https://github.com/AgentMindCloud/fielded-web
  keywords: [nextjs, vercel, waitlist]
  categories: [web]
```

## Field-by-field map

| `vercel.json`                 | `universal-spawn.yaml` (v1.0)                       |
|-------------------------------|------------------------------------------------------|
| `framework`                   | `platforms.vercel.framework`                         |
| `buildCommand`                | `platforms.vercel.build_command` + `deployment.build.command` |
| `installCommand`              | `platforms.vercel.install_command` + `deployment.build.install` |
| `outputDirectory`             | `platforms.vercel.output` + `deployment.build.output` |
| `devCommand`                  | `platforms.vercel.dev_command`                       |
| `regions`                     | `platforms.vercel.regions` + `deployment.regions`    |
| `functions[<match>]`          | `platforms.vercel.functions[*]` — each entry has `match`, `runtime`, `memory_mb`, `max_duration_seconds` |
| `env`                         | `env_vars_required[*]` with explicit `secret` flags  |
| `build.env`                   | `env_vars_required[*]` — values still live in Vercel |
| `headers`, `redirects`, `rewrites` | Keep in `vercel.json`. Platform-specific; no universal equivalent in v1.0 |
| `trailingSlash`               | Keep in `vercel.json`                                |
| `cleanUrls`                   | Keep in `vercel.json`                                |
| `crons`                       | Keep in `vercel.json`                                |
| `$schema`                     | No equivalent — drop                                 |

## What to do with `vercel.json`

**Keep it.** It is the source of truth for Vercel-specific edge
concerns that universal-spawn does not describe (headers, redirects,
trailingSlash, cleanUrls, crons). The universal-spawn manifest sits
on top of it.

At spawn time, Vercel reads `vercel.json` first; the universal-spawn
extension fills in the cross-platform gaps (`description`, `safety`,
`env_vars_required` with `secret` annotations).

## Env mapping detail

`vercel.json` allows `env` as either a map of name → default or as a
list. universal-spawn always uses the list form with one object per
variable, and requires a `description` for every entry:

```yaml
env_vars_required:
  - name: DATABASE_URL
    description: Postgres connection string for the primary database.
    secret: true
  - name: NEXT_PUBLIC_SITE_URL
    description: Public URL the app serves from.
    required: false
    example: "https://fielded.lab"
```

The `description` is non-negotiable: it is the only way a new
maintainer knows what an env var is for without reading the code.

## Functions mapping detail

`vercel.json`'s `functions` object keyed by glob becomes an array of
objects with `match`:

```yaml
platforms:
  vercel:
    functions:
      - match: "app/api/**/*.ts"
        runtime: edge
        memory_mb: 256
        max_duration_seconds: 15
      - match: "app/api/heavy/*.ts"
        runtime: nodejs
        memory_mb: 1024
        max_duration_seconds: 120
```

Field renames: `memory` → `memory_mb`, `maxDuration` →
`max_duration_seconds`. The renames make the units explicit so a
reader does not have to consult Vercel docs to know what `128` means.

## What universal-spawn adds that `vercel.json` does not

- `safety` — declared permission envelope, rate ceiling, cost ceiling.
- `metadata` — license, author, source with a pinned commit, keywords.
- `visuals` — a place for a hero plate and icon.
- Cross-platform targeting: add `platforms.netlify` and the same
  manifest builds on Netlify.
- `description` as a first-class field, long enough to matter.

## Worked example shipped in the repo

See [`examples/03-nextjs-vercel.yaml`](../examples/03-nextjs-vercel.yaml)
for the full file, which validates against the v1.0 schema.
