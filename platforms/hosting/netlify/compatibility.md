# Netlify compatibility — field-by-field

Netlify already has a native config format
(`netlify.toml`). universal-spawn does not replace it; the two
coexist. A Netlify consumer reads both:

- `netlify.toml` for provider-specific knobs the universal-spawn
  extension does not (yet) model.
- `universal-spawn.yaml` (with `platforms.netlify`) for the
  cross-platform manifest.

The two files **MUST NOT** disagree on fields that appear in both; a
consumer that detects a conflict MUST warn and prefer `universal-spawn.yaml`.

## Side-by-side

### `netlify.toml` (provider-native)

```toml
[build]
  command = "pnpm build"
  publish = "dist"
  functions = "netlify/functions"

[build.environment]
  NODE_VERSION = "20"

[[plugins]]
  package = "@netlify/plugin-nextjs"
```

### `universal-spawn.yaml` (platforms.netlify block)

```yaml
platforms:
  netlify:
    build_command: "pnpm build"
    publish: dist
    functions: netlify/functions
    node_version: "20"
    plugins:
      - package: "@netlify/plugin-nextjs"
    env_contexts: [production, deploy-preview]
```

## Field-by-field

| universal-spawn v1.0 field | Netlify behavior |
|---|---|
| `version` | Required. |
| `metadata.id` | Default site-slug suggestion. |
| `name, description` | Dashboard card. |
| `type` | `web-app`, `site`, `api-service`, `container`, `workflow`. |
| `safety.min_permissions` | Informational; not sandbox-enforced. |
| `safety.cost_limit_usd_daily` | Advisory. |
| `env_vars_required` | Build-blocking gate per env context. |
| `platforms.netlify.base` | Base directory inside the repo. |
| `platforms.netlify.build_command` | Build command. |
| `platforms.netlify.publish` | Directory containing built assets. |
| `platforms.netlify.functions` | Path to Functions directory. |
| `platforms.netlify.edge_functions` | Path to Edge Functions directory. |
| `platforms.netlify.node_version` | Node.js version. |
| `platforms.netlify.plugins` | Netlify Build plugins. |
| `platforms.netlify.env_contexts` | Env contexts required secrets must exist in. |
| `platforms.netlify.redirects_file` | Path to `_redirects`. |
| `platforms.netlify.headers_file` | Path to `_headers`. |

## What to keep where

- Use **`netlify.toml`** for redirects, headers, per-branch build config, and plugin inputs that don't fit cleanly into the universal schema's flat key space.
- Use **`universal-spawn.yaml`** for discovery, safety, `env_vars_required`, and cross-platform siblings.

