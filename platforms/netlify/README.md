# Netlify platform extension

**Id**: `netlify`
**Vendor**: Netlify
**Surfaces**: Netlify builds, Netlify Functions, Edge Functions.

A conformant Netlify consumer:

1. Validates core + extension.
2. Produces a `netlify.toml`-equivalent build configuration from the
   declared fields.
3. Blocks the build if required, non-optional `env_vars_required`
   entries are missing in the scope named by `env_contexts`.

## Notable fields

- `build_command`, `publish` — the build output directory.
- `functions` — the functions directory (path).
- `edge_functions` — the edge functions directory (path).
- `env_contexts[]` — which env contexts required vars must exist in.
- `plugins[]` — Netlify build plugins to enable.

See [`netlify-spawn.yaml`](./netlify-spawn.yaml) and
[`examples/`](./examples).
