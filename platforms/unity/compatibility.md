# Unity — compatibility notes

| Field                  | Behavior on Unity                                                     |
|------------------------|------------------------------------------------------------------------|
| `spawn_version`        | MUST be `1.0.0`.                                                      |
| `id`                   | Used as the UPM package id; must match `name.space.project` style.     |
| `name`, `description`  | Shown in the importer dialog and Asset Store listing.                  |
| `kind`                 | Accepted: `game-mod`, `game-world`, `creative-tool`, `extension`.      |
| `license`              | Required; Unity refuses to publish unlicensed packages.                |
| `author`, `source`     | Required.                                                              |
| `runtime`              | `engines.unity` pinned against `target_version`.                       |
| `entrypoints`          | At least one of kind `scene` or `script`.                              |
| `env_vars_required`    | Applied only to Play Mode, not Editor Mode.                            |
| `min_permissions`      | Enforced on runtime-side scripts. Editor scripts are out of envelope. |
| `rate_limit_qps`       | Ignored.                                                               |
| `cost_limit_usd_daily` | Ignored.                                                               |
| `safe_for_auto_spawn`  | Gates automatic import in a CI-driven pipeline.                        |
| `data_residency`       | Ignored.                                                               |
| `compat.dockerfile`    | Ignored.                                                               |

## Entrypoint kinds

- `scene` → a `.unity` file to open on spawn.
- `script` → an Editor script (runs at import time only if whitelisted
  by the consumer).

Other kinds ignored.

## Pipeline compatibility

If the host project's render pipeline differs from the declared
`render_pipeline`, the Unity consumer refuses to import unless the
creation provides fallback variants (documented separately per
creation).
