# Migrating from `grok-install` v2.14

[`AgentMindCloud/grok-install`](https://github.com/AgentMindCloud/grok-install)
v2.14 is the Grok-specific spawn manifest. universal-spawn v1.0 is the
cross-platform superset. This document shows how to translate a real
grok-install manifest into a universal-spawn manifest field by field,
and asserts the round-trip guarantee.

**grok-install stays valid.** You do not have to remove your
`grok-install.yaml`. universal-spawn is additive: ship both until your
consumers are ready.

## The starting manifest

A representative `grok-install.yaml` v2.14:

```yaml
$schema_version: "2.14"
name: "org.agentmindcloud.grok-telemetry"
display_name: "Grok Telemetry"
tagline: "Grok-first agent that now ships universally."
description: >
  A Grok tool-calling agent that pings a telemetry endpoint when the
  user asks about service health.
license: "Apache-2.0"
author:
  name: "Jani Solo"
  x_handle: "JanSol0s"
source:
  repo_url: "https://github.com/AgentMindCloud/grok-telemetry"
  pinned_commit: "1a2b3c4d5e6f7a8b9c0d"
runtime:
  language: "python"
  language_version: ">=3.11"
  engines:
    uv: ">=0.4"
  os: ["linux", "macos"]
  arch: ["x86_64", "arm64"]
entrypoints:
  tool:
    - name: "telemetry_ping"
      function_ref: "tools/telemetry.json"
env:
  - name: "XAI_API_KEY"
    required: true
    secret: true
    description: "API key for the xAI / Grok platform."
permissions:
  - "network:outbound:api.x.ai"
  - "model:call:grok-4"
limits:
  rate_qps: 2
  cost_usd_daily: 5
auto_spawn_ok: false
residency: ["us"]
tags: ["grok", "telemetry"]
```

## The target manifest

The same creation as a universal-spawn v1.0 manifest:

```yaml
version: "1.0"
name: Grok Telemetry
type: ai-agent
summary: "Grok-first agent that now ships universally."
description: >
  A Grok tool-calling agent that pings a telemetry endpoint when the
  user asks about service health.

platforms:
  grok:
    tools:
      - name: telemetry_ping
        function_ref: tools/telemetry.json
    surface: [grok-api]

safety:
  min_permissions:
    - network:outbound:api.x.ai
    - model:call:grok-4
  rate_limit_qps: 2
  cost_limit_usd_daily: 5
  safe_for_auto_spawn: false
  data_residency: [us]

deployment:
  targets: [grok]

env_vars_required:
  - name: XAI_API_KEY
    description: API key for the xAI / Grok platform.
    secret: true

metadata:
  license: Apache-2.0
  author:
    name: Jani Solo
    handle: JanSol0s
  source:
    type: git
    url: https://github.com/AgentMindCloud/grok-telemetry
    commit: 1a2b3c4d5e6f7a8b9c0d
  keywords: [grok, telemetry]
  id: org.agentmindcloud.grok-telemetry

x-ext:
  org.agentmindcloud.grok-install:
    version: "2.14"
```

See [`examples/11-grok-migration.yaml`](../examples/11-grok-migration.yaml)
for the identical file, validated in CI.

## Field-by-field map

| grok-install v2.14             | universal-spawn v1.0                          |
|--------------------------------|------------------------------------------------|
| `$schema_version: "2.14"`      | `version: "1.0"` + `x-ext.org.agentmindcloud.grok-install.version: "2.14"` |
| `name` (reverse-DNS)           | `metadata.id`                                  |
| `display_name`                 | `name`                                         |
| `tagline`                      | `summary`                                      |
| `description`                  | `description`                                  |
| `license`                      | `metadata.license`                             |
| `author.name`                  | `metadata.author.name`                         |
| `author.x_handle`              | `metadata.author.handle`                       |
| `source.repo_url`              | `metadata.source.url`                          |
| `source.pinned_commit`         | `metadata.source.commit`                       |
| `runtime.language`             | (informational) — consider a `platforms.grok.runtime.language` mirror if your tooling needs it |
| `runtime.language_version`     | same                                           |
| `runtime.engines`              | same                                           |
| `runtime.os`, `runtime.arch`   | same                                           |
| `entrypoints.cli.path`         | `platforms.grok.cli.ref` (grok-platform-local) |
| `entrypoints.http.route`       | `platforms.grok.http.route`                    |
| `entrypoints.tool[*]`          | `platforms.grok.tools[*]`                      |
| `entrypoints.webhook.route`    | `platforms.grok.webhook.route`                 |
| `env[*]`                       | `env_vars_required[*]`                         |
| `permissions[*]`               | `safety.min_permissions[*]`                    |
| `limits.rate_qps`              | `safety.rate_limit_qps`                        |
| `limits.cost_usd_daily`        | `safety.cost_limit_usd_daily`                  |
| `auto_spawn_ok`                | `safety.safe_for_auto_spawn`                   |
| `residency[*]`                 | `safety.data_residency[*]`                     |
| `tags[*]`                      | `metadata.keywords[*]`                         |
| `signatures[*]`                | (reserved, handled in v1.2; stash under `x-ext` for now) |
| `x-ext.*`                      | `x-ext.*` (verbatim)                           |

Anything not on this list is either not expressible in grok-install
v2.14 (such as `visuals`) or is universal-spawn-specific (such as
`metadata.maintainers`).

## Round-trip invariant

Define:

- `U(g)` — lift a grok-install manifest into universal-spawn.
- `L(u)` — lower a universal-spawn manifest back to grok-install.

The guarantee: `L(U(g)) == g` modulo field ordering, for any
well-formed grok-install v2.14 manifest.

The inverse is not guaranteed. Lowering a universal-spawn manifest
that uses fields grok-install cannot represent — `platforms.vercel`,
`visuals.hero_plate`, `metadata.maintainers[1..]` — drops those
fields. A lowering tool **MUST** emit a warning naming every dropped
field.

## What the consumer does

- **grok** reads both forms transparently. If both files exist, the
  platform-specific `grok-install.yaml` is authoritative for
  Grok-specific fields; the universal-spawn manifest provides the
  cross-platform data.
- Any other platform reads only the universal-spawn manifest.

## When to migrate

Migrate when:

- You want to ship on Grok **plus** another platform.
- You want a single stable `metadata.id` across registries.
- You want the declarative safety envelope enforced cross-platform.

Do not migrate when:

- You ship only on Grok.
- You rely on a grok-install-specific field that has no
  universal-spawn equivalent in v1.0 (rare, but see the field map).

## Tooling

A reference `lower-to-grok` and `lift-from-grok` CLI will ship in a
sibling repository in v1.1. Until then, the mapping above is small
enough to translate by hand.
