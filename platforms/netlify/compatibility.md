# Netlify — compatibility notes

| Field                  | Behavior on Netlify                                                        |
|------------------------|-----------------------------------------------------------------------------|
| `spawn_version`        | MUST be `1.0.0`.                                                           |
| `id`                   | Used as the default site-slug suggestion; the user may rename.             |
| `name`, `description`  | Shown on the site card.                                                    |
| `kind`                 | Accepted: `web-app`, `site`, `api-service`, `container`, `workflow`.       |
| `license`              | Informational.                                                             |
| `author`, `source`     | `source.url` links the Git provider integration.                           |
| `runtime`              | `language` and `engines.node` guide the builder.                           |
| `entrypoints`          | At least one `http` or `webhook` entrypoint.                               |
| `env_vars_required`    | Build blocked when required non-optional vars are missing in env_contexts. |
| `min_permissions`      | Surfaced only in project settings; not sandbox-enforced.                   |
| `rate_limit_qps`       | Informational.                                                             |
| `cost_limit_usd_daily` | Advisory.                                                                  |
| `safe_for_auto_spawn`  | Gates Deploy Preview auto-publish.                                         |
| `data_residency`       | Honored when the Netlify plan permits region pinning.                      |
| `compat.dockerfile`    | Used when `kind: container`.                                               |

## Entrypoint kinds

- `http` → site route (handled by the CDN or Functions).
- `webhook` → Functions endpoint.
- `websocket` → Edge Functions only.
- `container` → requires `compat.dockerfile`.

Other kinds ignored.
