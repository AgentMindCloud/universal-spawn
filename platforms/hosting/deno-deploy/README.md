# Deno Deploy — universal-spawn platform extension

Deno Deploy runs Deno (and increasingly Node.js) modules at the edge. A manifest captures the entry module, import map, required permissions for Deno's permission model, and KV namespaces.

## What this platform cares about

The entry module, the Deno version or std @ version, the import map path, the granted permissions (`--allow-net`, `--allow-read`, etc.), and Deno KV namespaces.

## What platform-specific extras unlock

`deno_permissions[]` maps to the Deno permission flags the consumer grants at run time. `kv_namespaces[]` lists Deno KV namespaces the module uses.

## Compatibility table

| Manifest field | Deno Deploy behavior |
|---|---|
| `version` | Required `"1.0"`. |
| `name, description` | Project name + card. |
| `type` | `api-service`, `web-app`, `workflow`, `cli-tool`. |
| `env_vars_required` | Deno Deploy environment variables. |
| `deployment.targets` | Must include `deno-deploy`. |
| `platforms.deno-deploy` | Strict. |

### `platforms.deno-deploy` fields

| Field | Purpose |
|---|---|
| `platforms.deno-deploy.entrypoint` | Entry module path or URL. |
| `platforms.deno-deploy.import_map` | Path to `import_map.json`. |
| `platforms.deno-deploy.deno_version` | Deno version (major). |
| `platforms.deno-deploy.deno_permissions` | Deno permission flags. |
| `platforms.deno-deploy.kv_namespaces` | Deno KV namespaces. |
| `platforms.deno-deploy.regions` | Deno Deploy regions. |

See [`compatibility.md`](./compatibility.md) for the side-by-side diff
against `deno.json`, [`deploy-button.md`](./deploy-button.md)
for the canonical Deploy-button recipe, and [`perks.md`](./perks.md) for
what a conformant Deno Deploy consumer SHOULD offer manifests that
declare `platforms.deno-deploy`.
