# Field reference (narrative)

A prose walkthrough of every core field. For the normative definition,
see [`../spec/v1.0.0/fields.md`](../spec/v1.0.0/fields.md) and the
schema itself.

## Identity you can rely on

**`spawn_version`.** What spec version you target. We chose `1.0.0`
for the first public release because bumping to 1 is a commitment.
Pre-1 specs invite "I'll rewrite everything later" engineering; this
spec does not.

**`id`.** A reverse-DNS string that survives project renames. Pick
once, never change. The `id` is how registries deduplicate and how a
manifest declares itself across the universe of platforms. `id`
collisions are a registry issue; the spec itself does not police them.

**`name` / `summary` / `description`.** Three fields that exist because
different surfaces have different space budgets. `name` is short and
displayed in UIs. `summary` is one line, for cards. `description` is a
paragraph, for detail pages. The first sentence of `description` is
used as a search snippet; write it like one.

## Kind and categories

`kind` is a one-of from a fixed list because downstream platforms key
their acceptance decisions on it. Categories are softer — up to four
values from a flat taxonomy to aid search.

If you can't find the right `kind`, open a spec proposal. If you can't
find the right `category`, pick the closest one; the taxonomy evolves
in minor releases.

## Author, maintainers, source

`author` is the primary accountable person or organization. Adding
`maintainers[]` is additive — the `author` is always listed first in
credit displays. `source` names a canonical code location; every
universal-spawn manifest MUST be reachable from its `source.url`.

## Runtime and dependencies

`runtime` is a statement about what the creation actually needs —
language, engine, memory floor. Platforms use this to pick install
paths. It is never prescriptive in the other direction; a manifest
that says `os: [linux]` cannot force a platform to provision Linux.

`dependencies[]` references other universal-spawn manifests by `id`
and version range. It is not a package manager; a real package manager
(npm, pip, uv, cargo) does the transitive resolution. The dependency
list exists so a spawn host can decline to spawn if any dependency is
absent or blocked.

## Entrypoints

An entrypoint is an **invocable handle**. The manifest names them; the
platform wires them up. Entrypoints are:

| Kind             | What the platform sees                              |
|------------------|------------------------------------------------------|
| `http`           | A route on a server.                                |
| `cli`            | A binary at `ref`.                                  |
| `websocket`      | A WebSocket URL.                                    |
| `stdio`          | An MCP server over stdin/stdout.                    |
| `script`         | A file that is loaded rather than executed.         |
| `container`      | A container image reference.                        |
| `webhook`        | An idempotent HTTP endpoint.                        |
| `scene`          | A Unity scene file.                                 |
| `slash-command`  | A Discord / Claude Code slash command JSON.         |
| `tool-call`      | A function definition consumable by LLMs.           |
| `ui-panel`       | A Figma / plugin iframe UI.                         |

The `ref` field is always a **reference** — a path, URL, or image
identifier. If you find yourself wanting to put `bash -lc "..."` in an
entrypoint, the spec is telling you that the thing you are trying to
reference doesn't have a clean handle yet. Fix that first.

## Safety envelope

Three fields together describe what the platform is allowed to do on
behalf of your creation:

- `env_vars_required` — **names** of environment variables. Never
  values. Mark `secret: true` to indicate the platform must use its
  credential store.
- `min_permissions` — the smallest capability set the creation needs.
  Use the canonical namespaces in spec Appendix B. `network:outbound`
  is not the same as `network:outbound:api.example.com`; the second
  is narrower and better.
- `rate_limit_qps`, `cost_limit_usd_daily` — numerical ceilings. The
  platform enforces; the manifest declares.

Add `safe_for_auto_spawn: true` only if you are confident that under
the declared envelope the creation is safe to run without human
confirmation. The default — false — means "the first spawn is gated
by a human."

## Platforms and compat

The `platforms` object lets one manifest target many surfaces. Each
key is a platform `id` (see [`../platforms/`](../platforms)), and the
value is a platform-specific extension object whose shape is defined
by that platform's `schema.extension.json`. Consumers validate both
the core manifest and the extension; an unknown extension key is an
error by design.

The `compat` object lets a manifest declare compatibility with other
standards:

- `compat.grok_install` — enables round-trip with
  AgentMindCloud/grok-install. See
  [`grok-compat.md`](./grok-compat.md).
- `compat.openapi` — path to an OpenAPI document.
- `compat.dockerfile` — path to a Dockerfile.

## Integrity

`signatures[]` is an array of detached signatures over the canonical
serialization of the manifest minus its `signatures` field. The
procedure is defined in spec Appendix C: JCS (RFC 8785) → SHA-256 →
sign. In v1.0.0 a platform MAY ignore missing signatures; internal
deployments often choose to require them via external policy.

`x-ext` is the escape hatch. If you want to carry a field the spec
does not define, nest it under a reverse-DNS key inside `x-ext`.
Consumers are free to ignore anything under `x-ext`.

## Field choices you might second-guess

- *Why no `version`?* Because the creation's version belongs on the
  tag of the source repository, not inside the manifest. A manifest
  describes "what this repo is"; the version is "which snapshot you
  looked at."
- *Why no `runbook`?* Runbooks are documentation, not declaration. A
  homepage link covers it.
- *Why so much ceremony for permissions?* Because capability
  containment is the only real safety boundary. Everything else is
  policy in a trench coat.
