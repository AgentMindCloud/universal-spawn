# Netlify — universal-spawn platform extension

Netlify builds a site from a Git repo, deploys it on a CDN, and runs Functions / Edge Functions alongside. The extension captures the build command, publish directory, function and edge-function paths, and which deploy contexts required secrets must exist in.

## What this platform cares about

The publish directory, the Functions / Edge Functions paths, build plugins, redirects/headers files, and the env contexts (`production`, `deploy-preview`, `branch-deploy`, `dev`) required secrets must exist in.

## What platform-specific extras unlock

`plugins[]` enables Netlify Build plugins by package name. `redirects_file` and `headers_file` point at `_redirects` / `_headers`.

## Compatibility table

| Manifest field | Netlify behavior |
|---|---|
| `version` | Required `"1.0"`. |
| `name, description` | Site name + card. |
| `type` | `web-app`, `site`, `api-service`, `container`. |
| `env_vars_required` | Build blocked when required secrets missing in listed env_contexts. |
| `deployment.targets` | Must include `netlify`. |
| `platforms.netlify` | Strict. |

### `platforms.netlify` fields

| Field | Purpose |
|---|---|
| `platforms.netlify.base` | Base directory inside the repo. |
| `platforms.netlify.install_command` | Install command. |
| `platforms.netlify.build_command` | Build command. |
| `platforms.netlify.publish` | Publish directory. |
| `platforms.netlify.functions` | Functions directory path. |
| `platforms.netlify.edge_functions` | Edge Functions directory path. |
| `platforms.netlify.node_version` | Node.js version. |
| `platforms.netlify.plugins` | Netlify Build plugins. |
| `platforms.netlify.env_contexts` | Env contexts required secrets must exist in. |
| `platforms.netlify.redirects_file` | Path to `_redirects`. |
| `platforms.netlify.headers_file` | Path to `_headers`. |

See [`compatibility.md`](./compatibility.md) for the side-by-side diff
against `netlify.toml`, [`deploy-button.md`](./deploy-button.md)
for the canonical Deploy-button recipe, and [`perks.md`](./perks.md) for
what a conformant Netlify consumer SHOULD offer manifests that
declare `platforms.netlify`.
