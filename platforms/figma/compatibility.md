# Figma — compatibility notes

| Field                  | Behavior on Figma                                                      |
|------------------------|-------------------------------------------------------------------------|
| `spawn_version`        | MUST be `1.0.0`.                                                       |
| `id`                   | Linked to the Figma plugin's `id` for cross-registry deduplication.    |
| `name`, `description`  | Shown on the plugin detail page.                                       |
| `kind`                 | `creative-tool`, `design-template`, `plugin`, `extension`.             |
| `license`              | Informational.                                                         |
| `author`, `source`     | Required.                                                              |
| `runtime`              | Informational; Figma runs plugins in its own sandbox.                  |
| `entrypoints`          | At least one `ui-panel` or `script` entrypoint.                        |
| `env_vars_required`    | Ignored. Figma plugins pass configuration through storage APIs.        |
| `min_permissions`      | Mapped onto Figma's declared permissions (clientStorage, network).     |
| `rate_limit_qps`       | Ignored.                                                               |
| `cost_limit_usd_daily` | Ignored.                                                               |
| `safe_for_auto_spawn`  | Gates auto-install via a Figma org policy.                             |
| `data_residency`       | Ignored.                                                               |

## Entrypoint kinds

- `ui-panel` → the iframe UI file.
- `script` → the main plugin script file.

Other kinds ignored.

## Network access

The Figma consumer enforces `network_access`:

- `none` — plugin cannot open any network connection.
- `declared` — network calls are allowed but logged.
- `allowed-hosts` — only `allowed_hosts[]` are reachable.

If `min_permissions` includes `network:outbound:<host>`, the Figma
consumer sets `network_access: allowed-hosts` automatically and
populates `allowed_hosts` to match.
