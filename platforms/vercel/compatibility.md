# Vercel — compatibility notes

| Field                  | Behavior on Vercel                                                        |
|------------------------|----------------------------------------------------------------------------|
| `spawn_version`        | MUST be `1.0.0`.                                                          |
| `id`                   | Used as the default project name suggestion; the user may rename.         |
| `name`, `description`  | Displayed on the project page and README integration.                     |
| `kind`                 | Accepted: `web-app`, `api-service`, `site`, `container`, `workflow`.      |
| `license`              | Informational.                                                            |
| `author`, `source`     | `source.url` links the Git provider integration.                          |
| `runtime`              | `language` and `engines.node` guide the builder preset.                   |
| `entrypoints`          | At least one `http` or `webhook` entrypoint required.                     |
| `env_vars_required`    | Build is blocked when required non-optional vars are missing in the scopes listed by `env_promotion`. |
| `min_permissions`      | Not enforced by Vercel's sandbox. Surfaced in the project settings UI.    |
| `rate_limit_qps`       | Informational.                                                            |
| `cost_limit_usd_daily` | Advisory — Vercel's spend management honors it when linked.               |
| `safe_for_auto_spawn`  | If false, branch-deploy auto-promotion is disabled.                       |
| `data_residency`       | Used to pre-select `regions[]` if that field is absent.                   |
| `compat.dockerfile`    | Used when `framework: container`.                                         |
| `signatures`           | Ignored.                                                                  |

## Entrypoint kinds

- `http` → a route, possibly the root.
- `webhook` → a webhook endpoint; the Vercel adapter wires it up.
- `websocket` → supported only on regions that allow WebSocket
  runtimes.
- `container` → requires `compat.dockerfile`.

Other kinds ignored.

## Framework preset selection

`framework` is mapped 1-to-1 onto Vercel's framework presets. `other`
uses a zero-config build; set `build_command` and `output` manually.
