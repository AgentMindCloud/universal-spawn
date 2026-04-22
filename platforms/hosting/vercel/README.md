# Vercel — universal-spawn platform extension

Vercel ships static sites, Next.js apps, Edge Functions, and background functions from a Git repository. The extension captures the framework preset, build command, output directory, regions, per-route function config, and the env scopes required secrets must exist in.

## What this platform cares about

The framework preset (`nextjs`, `remix`, `svelte-kit`, `astro`, `vite`, `other`), install/build commands, output directory, regions, per-route functions, and env promotion scopes (`production`, `preview`, `development`).

## What platform-specific extras unlock

`functions[]` sets per-route runtime, memory, maxDuration. `env_promotion[]` blocks builds missing required secrets in a listed scope.

## Supported runtime targets

| Route kind | Runtime options |
|---|---|
| `api/*`            | `nodejs`, `edge`, `python`, `go` |
| `app/*` (Next.js)  | Node.js server runtime or React server components |
| static assets      | CDN only |


## Compatibility table

| Manifest field | Vercel behavior |
|---|---|
| `version` | Required `"1.0"`. |
| `name, description` | Project name + card metadata. |
| `type` | `web-app`, `api-service`, `site`, `container`, `workflow`. |
| `env_vars_required` | Build blocked when a required non-optional secret is missing in a scope listed by `env_promotion`. |
| `deployment.targets` | Must include `vercel`. |
| `platforms.vercel` | Strict; see below. |

### `platforms.vercel` fields

| Field | Purpose |
|---|---|
| `platforms.vercel.framework` | Vercel framework preset. |
| `platforms.vercel.install_command` | Install command override. |
| `platforms.vercel.build_command` | Build command override. |
| `platforms.vercel.output` | Output directory. |
| `platforms.vercel.root_directory` | Monorepo sub-directory. |
| `platforms.vercel.node_version` | Node.js major version (`18`, `20`, `22`). |
| `platforms.vercel.regions` | Preferred Vercel regions. |
| `platforms.vercel.functions` | Per-route runtime/memory/duration. |
| `platforms.vercel.env_promotion` | Env scopes required secrets must exist in. |

See [`compatibility.md`](./compatibility.md) for the side-by-side diff
against `vercel.json`, [`deploy-button.md`](./deploy-button.md)
for the canonical Deploy-button recipe, and [`perks.md`](./perks.md) for
what a conformant Vercel consumer SHOULD offer manifests that
declare `platforms.vercel`.
