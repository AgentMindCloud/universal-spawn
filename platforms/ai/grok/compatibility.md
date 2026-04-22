# Grok compatibility — universal-spawn ↔ grok-install v2.14

This file is the authoritative field-by-field map between:

- the universal-spawn v1.0 manifest (`universal-spawn.yaml`), and
- the platform-specific form (`grok-spawn.yaml`), and
- the prior `grok-install.yaml` v2.14 format.

All three cohabit in a repository. They describe the same creation;
they differ in how much is Grok-specific.

## Universal ↔ grok-install v2.14

| universal-spawn v1.0                             | grok-install v2.14                    | Notes                                       |
|--------------------------------------------------|---------------------------------------|----------------------------------------------|
| `version`                                        | `$schema_version`                     | v1.0 literal ⇆ `"2.14"` on lowering.         |
| `metadata.id`                                    | `name`                                | Reverse-DNS identifier.                      |
| `name`                                           | `display_name`                        |                                              |
| `summary`                                        | `tagline`                             |                                              |
| `description`                                    | `description`                         |                                              |
| `type`                                           | — (implied `ai-agent`)                | grok-install is always an AI shape.          |
| `platforms.grok.model`                           | `model`                               |                                              |
| `platforms.grok.surface[*]`                      | `surfaces[*]`                         |                                              |
| `platforms.grok.tools[*].name`                   | `entrypoints.tool[*].name`            |                                              |
| `platforms.grok.tools[*].function_ref`           | `entrypoints.tool[*].function_ref`    |                                              |
| `platforms.grok.tools[*].strict`                 | `entrypoints.tool[*].strict`          |                                              |
| `platforms.grok.system_prompt_file`              | `system_prompt`                       |                                              |
| `platforms.grok.streaming`                       | `streaming`                           |                                              |
| `platforms.grok.real_time_data`                  | `x_live_feed`                         | Legacy key name in v2.14.                    |
| `platforms.grok.temperature`                     | `sampling.temperature`                |                                              |
| `platforms.grok.max_tokens`                      | `sampling.max_tokens`                 |                                              |
| `safety.min_permissions[*]`                      | `permissions[*]`                      | Same namespace vocabulary.                   |
| `safety.rate_limit_qps`                          | `limits.rate_qps`                     |                                              |
| `safety.cost_limit_usd_daily`                    | `limits.cost_usd_daily`               |                                              |
| `safety.safe_for_auto_spawn`                     | `auto_spawn_ok`                       |                                              |
| `safety.data_residency[*]`                       | `residency[*]`                        |                                              |
| `env_vars_required[*]`                           | `env[*]`                              |                                              |
| `metadata.license`                               | `license`                             | SPDX.                                        |
| `metadata.author.name`                           | `author.name`                         |                                              |
| `metadata.author.handle`                         | `author.x_handle`                     | grok-install stores X handle specifically.   |
| `metadata.source.url`                            | `source.repo_url`                     |                                              |
| `metadata.source.commit`                         | `source.pinned_commit`                |                                              |
| `metadata.keywords[*]`                           | `tags[*]`                             |                                              |
| `x-ext.org.agentmindcloud.grok-install.version`  | `$schema_version`                     | Consumed by the lowering tool.               |

## Universal ↔ grok-spawn.yaml (v1.0 platform-specific form)

The platform-specific file is a pure projection of the universal
manifest onto Grok. All fields present in `grok-spawn.yaml` are a
subset of the universal manifest; nothing is unique to
`grok-spawn.yaml`.

Projection rules:

1. Copy `version`, `name`, `summary`, `description`, `type`,
   `metadata`, `env_vars_required`, and `safety` verbatim.
2. Copy `platforms.grok` verbatim.
3. Drop every other `platforms.<id>` block.
4. If `deployment` is present, keep only `targets: [grok]`.
5. Drop `visuals` unless the Grok card will use it.
6. Drop `x-ext.*` unless the downstream tool needs it (the
   grok-install lowering tool needs
   `x-ext.org.agentmindcloud.grok-install`).

A manifest that sets `spawn_targets: [grok]` under the v1.0.0 legacy
track projects identically.

## Unmapped fields

Lifting grok-install → universal-spawn is always safe.

Lowering universal-spawn → grok-install drops:

- `platforms.<non-grok>` — not representable.
- `visuals.hero_plate`, `visuals.banner`, `visuals.palette` —
  grok-install has `icon` only.
- `metadata.maintainers[1..]` — grok-install tracks a single author.
- `metadata.categories[*]` — flattened into `tags`.

A lowering tool MUST emit a warning listing every dropped field.

## Round-trip invariant

For a v2.14 grok-install manifest `g`:

- `U(g)` lifts to universal-spawn.
- `L(U(g))` lowers back to grok-install.
- `L(U(g)) == g` modulo field ordering.

For a universal-spawn manifest `u` that targets only Grok:

- `L(u)` lowers to grok-install.
- `U(L(u)) == u` only if `u` contained no fields outside the map
  above. Otherwise dropped fields are lost (by design — grok-install
  cannot carry them).

## Cohabitation

A repository may ship all three of:

1. `universal-spawn.yaml` — the cross-platform manifest.
2. `grok-spawn.yaml` — the projected Grok-only view (optional).
3. `grok-install.yaml` — the legacy v2.14 manifest (optional).

Grok consumers read in that order and stop at the first match.
universal-spawn consumers only read `universal-spawn.yaml`.
