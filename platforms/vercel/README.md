# Vercel platform extension

**Id**: `vercel`
**Vendor**: Vercel
**Surfaces**: Vercel build / deploy, Edge Functions, Vercel AI SDK
integrations.

A conformant Vercel consumer:

1. Validates the core manifest and this extension.
2. Produces a Vercel build configuration equivalent to the declared
   fields — it never executes arbitrary shell except through the
   framework adapter chosen by `framework`.
3. Reads `env_vars_required` and blocks the build if any required-and-
   non-optional secret is missing.
4. Reads `entrypoints[*]` and expects at least one `http` or `webhook`
   surface.

## Notable fields

- `framework` — which Vercel framework preset to use.
- `build_command`, `install_command`, `output` — build configuration.
- `regions[]` — preferred deployment regions (Vercel region codes).
- `functions[]` — per-route runtime, memory, maxDuration.
- `env_promotion` — which env scope (`development`, `preview`,
  `production`) required vars must exist in.

See [`vercel-spawn.yaml`](./vercel-spawn.yaml) and
[`examples/`](./examples).
