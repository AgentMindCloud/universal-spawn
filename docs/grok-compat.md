# Compatibility with grok-install

[`AgentMindCloud/grok-install`](https://github.com/AgentMindCloud/grok-install)
(current v2.14) is a platform-specific spawn manifest for Grok.
universal-spawn is the cross-platform superset: every universal-spawn
manifest that sets `compat.grok_install` can be mechanically lowered
into a grok-install manifest, and a grok-install manifest can be
lifted back into universal-spawn without information loss.

This document defines the mapping.

## Declaring compatibility

```yaml
compat:
  grok_install:
    version: "2.14"
    mapping_file: compat/grok-install.map.yaml
```

- `version` — the minimum grok-install spec version the author expects
  consumers to support.
- `mapping_file` — optional relative path to a mapping file that
  overrides or extends the default mapping (documented below).

## Default field mapping

| universal-spawn field        | grok-install field              | Notes                             |
|------------------------------|---------------------------------|-----------------------------------|
| `spawn_version`              | `$schema_version`               | Always mapped to "2.14" on lowering when compat.grok_install.version is "2.14". |
| `id`                         | `name`                          | grok-install uses reverse-DNS names too. |
| `name`                       | `display_name`                  |                                   |
| `description`                | `description`                   |                                   |
| `summary`                    | `tagline`                       |                                   |
| `license`                    | `license`                       | SPDX identifiers pass through.    |
| `author.name`                | `author.name`                   |                                   |
| `author.handle`              | `author.x_handle`               | grok-install v2.14 uses X handle. |
| `source.url`                 | `source.repo_url`               |                                   |
| `source.commit`              | `source.pinned_commit`          |                                   |
| `homepage`                   | `homepage`                      |                                   |
| `icon`                       | `icon`                          |                                   |
| `keywords`                   | `tags`                          |                                   |
| `runtime.language`           | `runtime.language`              |                                   |
| `runtime.language_version`   | `runtime.language_version`      |                                   |
| `runtime.engines`            | `runtime.engines`               |                                   |
| `runtime.os`                 | `runtime.os`                    |                                   |
| `runtime.arch`               | `runtime.arch`                  |                                   |
| `entrypoints[]` kind=`cli`   | `entrypoints.cli.path`          |                                   |
| `entrypoints[]` kind=`http`  | `entrypoints.http.route`        |                                   |
| `entrypoints[]` kind=`tool-call` | `entrypoints.tool[]`        | Each entry becomes a grok tool.   |
| `entrypoints[]` kind=`webhook` | `entrypoints.webhook.route`   |                                   |
| `env_vars_required[]`        | `env[]`                         | Name and `required` pass through. |
| `min_permissions[]`          | `permissions[]`                 | Namespace syntax identical.       |
| `rate_limit_qps`             | `limits.rate_qps`               |                                   |
| `cost_limit_usd_daily`       | `limits.cost_usd_daily`         |                                   |
| `safe_for_auto_spawn`        | `auto_spawn_ok`                 |                                   |
| `data_residency`             | `residency[]`                   |                                   |
| `signatures[]`               | `signatures[]`                  | Algorithm and format compatible.  |
| `x-ext.*`                    | `x-ext.*`                       | Preserved as-is.                  |

## Unmapped fields

Lifting from grok-install → universal-spawn is always safe.

Lowering universal-spawn → grok-install drops the following fields
because grok-install 2.14 has no equivalent:

- `platforms.claude`, `platforms.gemini`, `platforms.openai`,
  `platforms.vercel`, `platforms.netlify`, `platforms.unity`,
  `platforms.figma`, `platforms.figma`, `platforms.discord`,
  `platforms.huggingface` — these are universal-spawn-specific.
- `hero_plate` — grok-install uses `icon` only.
- `spawn_targets` — grok-install implies Grok.
- `categories` — flattened into `tags`.

A lowering tool MUST emit a warning listing every dropped field.

## Round-trip invariant

Define `L(m)` as the lowering of a universal-spawn manifest `m` into
grok-install, and `U(g)` as the lifting of a grok-install manifest
`g` into universal-spawn. The specification guarantees:

> For any universal-spawn manifest `m` with `compat.grok_install` set,
> `U(L(m))` equals `m` modulo field ordering and the dropped fields
> listed above.

The inverse is not guaranteed because grok-install has fewer degrees
of freedom. A grok-install manifest can always be lifted; the result
will have empty `platforms` and `spawn_targets: [grok]`.

## Why both standards exist

grok-install is optimized for Grok specifically — it encodes Grok's
tool-calling, system-prompt, and session conventions directly.
universal-spawn is optimized for cross-platform reuse — it is a
superset that can be projected onto any platform, Grok included.

If you ship only on Grok, use grok-install; it is purpose-built.
If you ship on two or more platforms, use universal-spawn and set
`compat.grok_install` to stay Grok-compatible for free.

## Reference mapping tool

A reference `lower-to-grok` and `lift-from-grok` CLI ships in a
sibling repo (not included here). Both tools are exercise-only until
the universal-spawn v1.0.1 patch release, which will ship conformance
tests against this mapping.
