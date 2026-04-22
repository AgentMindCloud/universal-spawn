# Deno Deploy compatibility — field-by-field

Deno Deploy already has a native config format
(`deno.json`). universal-spawn does not replace it; the two
coexist. A Deno Deploy consumer reads both:

- `deno.json` for provider-specific knobs the universal-spawn
  extension does not (yet) model.
- `universal-spawn.yaml` (with `platforms.deno-deploy`) for the
  cross-platform manifest.

The two files **MUST NOT** disagree on fields that appear in both; a
consumer that detects a conflict MUST warn and prefer `universal-spawn.yaml`.

## Side-by-side

### `deno.json` (provider-native)

```json
{
  "tasks": { "start": "deno run -A main.ts" },
  "imports": { "std/": "https://deno.land/std@0.224.0/" },
  "deploy": {
    "entrypoint": "main.ts",
    "include": ["**/*.ts"],
    "exclude": ["tests/"]
  }
}
```

### `universal-spawn.yaml` (platforms.deno-deploy block)

```yaml
platforms:
  deno-deploy:
    entrypoint: main.ts
    import_map: import_map.json
    deno_version: "2"
    deno_permissions: [allow-net, allow-env]
```

## Field-by-field

| universal-spawn v1.0 field | Deno Deploy behavior |
|---|---|
| `version` | Required. |
| `metadata.id` | Project-slug suggestion. |
| `name, description` | Card. |
| `type` | `api-service`, `web-app`, `workflow`, `cli-tool`. |
| `safety.min_permissions` | Mirrored into `deno_permissions[]`. |
| `env_vars_required` | Deno Deploy env vars. |
| `platforms.deno-deploy.entrypoint` | Entry module path or URL. |
| `platforms.deno-deploy.import_map` | Path to import_map.json. |
| `platforms.deno-deploy.deno_permissions` | Deno permission flags. |
| `platforms.deno-deploy.kv_namespaces` | Deno KV namespaces. |
| `platforms.deno-deploy.regions` | Regions. |

## Deno permissions map

A `safety.min_permissions` entry maps onto a `deno_permissions` flag where equivalent:

| universal                               | Deno flag       |
|------------------------------------------|------------------|
| `network:outbound`, `network:inbound`    | `allow-net`      |
| `fs:read`                                | `allow-read`     |
| `fs:write:*`                             | `allow-write`    |
| `fs:exec:*`                              | `allow-run`      |

A consumer that finds both MUST union them (widest wins).
