# Universal Spawn Manifest Specification

**Version**: 1.0.0
**Status**: Stable
**Canonical source**: `github.com/AgentMindCloud/universal-spawn`
**License**: Apache 2.0
**Editor**: Jani Solo (`@JanSol0s`), AgentMindCloud

---

## 1. Introduction

A **spawn manifest** is a single declarative file placed at the root of a
repository that makes the contained creation discoverable, validatable, and
one-click spawnable across any platform that understands this specification.

Universal-spawn is the OpenAPI of installable creations. It describes *what*
a creation is, *where* it runs, *what it needs*, and *what it promises*,
without ever describing *how to do it*. The separation of declaration from
execution is the entire point of the standard.

This document defines version **1.0.0** of the specification. The normative
JSON Schema is at [`manifest.schema.json`](./manifest.schema.json). When
this prose disagrees with the schema, the schema wins.

## 2. Design goals

1. **Declarative only.** A manifest MUST NOT contain executable code. It MAY
   reference files, binaries, container images, or remote endpoints.
2. **Strictly validatable.** Every version of the spec ships a JSON Schema
   that rejects malformed manifests unambiguously.
3. **Universal first, platform second.** The core fields MUST work on every
   conformant spawn target. Platform-specific extensions go under
   `platforms.<id>` and are validated against that platform's extension
   schema.
4. **Safety by declaration.** A manifest declares the smallest set of
   permissions, the maximum rate, and the cost ceiling under which the
   author certifies the creation behaves correctly. Platforms enforce those
   numbers; they do not infer them.
5. **Never embed secrets.** Secret values are declared by *name* in
   `env_vars_required`. The manifest is expected to be committed to a
   public source repository.
6. **Stable identity.** Every manifest has a reverse-DNS `id` that is stable
   across renames and forks.
7. **Forward-compatible.** Consumers MUST ignore unknown fields inside
   `x-ext` and unknown platform extensions. Consumers MUST reject manifests
   with an unknown major `spawn_version`.

## 3. File conventions

### 3.1 Filename

A repository SHOULD place its manifest at exactly one of:

- `spawn.yaml` (preferred)
- `spawn.yml`
- `spawn.json`
- `spawn.toml`

A creation MAY use a suffixed form for platform-specific manifests that
mirror the universal one, for example `claude-spawn.yaml`. Consumers that
find both a universal `spawn.yaml` and a platform-specific variant MUST
merge them with the platform variant overriding at the field level.

### 3.2 Serialization

All three serializations (YAML, JSON, TOML) describe the same JSON data
model defined by the schema. Implementations SHOULD accept all three.
The canonical serialization used for signing is defined in Appendix C.

### 3.3 Character set

UTF-8. All string fields accept Unicode, but identifiers (`id`, entrypoint
ids, keyword entries) are restricted to the patterns given by the schema.
No emoji may appear in `name` or `description`.

## 4. Core fields

Full details live in [`fields.md`](./fields.md). A brief list of required
fields:

| Field           | Type   | Purpose                                        |
|-----------------|--------|------------------------------------------------|
| `spawn_version` | string | Semantic version of the spec targeted.         |
| `id`            | string | Stable reverse-DNS identifier.                 |
| `name`          | string | Human display name.                            |
| `kind`          | enum   | Primary category (see schema enum).            |
| `description`   | string | One paragraph, ≥20 and ≤500 characters.        |
| `license`       | string | SPDX identifier or `proprietary`.              |
| `author`        | object | Primary maintainer.                            |
| `source`        | object | Canonical source location.                     |

All other fields are optional but often required by specific platforms.

## 5. Entrypoints

An entrypoint is a named, declarative reference to something a spawning
platform can invoke. The manifest lists them; the platform decides which
ones to expose.

An entrypoint has:

- `id` — stable identifier, unique within the manifest.
- `kind` — transport or surface: `http`, `cli`, `websocket`, `stdio`,
  `script`, `container`, `webhook`, `scene`, `slash-command`, `tool-call`,
  `ui-panel`.
- `ref` — a relative path, route, image tag, or URL. Never a code blob.
- `inputs` / `outputs` — typed parameter lists.
- `idempotent` — whether repeating the call is safe.

The `ref` field is **always** a reference, never a command line. A CLI
entrypoint names the binary path; the platform constructs the invocation.

## 6. Safety model

A compliant platform enforces **at least** these guarantees whenever it
spawns a creation:

1. **Capability containment.** Only the capabilities in `min_permissions`
   are granted. Additional grants require explicit user consent.
2. **Rate ceiling.** Outbound requests are rate-limited to
   `rate_limit_qps` (if declared).
3. **Cost ceiling.** Incurred costs are tracked and spawning halts before
   `cost_limit_usd_daily` is exceeded.
4. **Secret isolation.** Values for `env_vars_required` are provided by the
   user or platform credential store; never read from the manifest.
5. **Confirmation gate.** If `safe_for_auto_spawn` is false or absent, a
   human must confirm the first spawn.

See [`docs/safety-model.md`](../../docs/safety-model.md) for threat analysis.

## 7. Permissions vocabulary

Permissions are `namespace:action[:scope]` strings. The canonical set for
v1.0.0 is in Appendix B. A platform that cannot map a declared permission
onto its own capability model MUST refuse to spawn.

## 8. Versioning

The spec uses semantic versioning.

- **Major** bumps MAY break existing manifests. Consumers MUST refuse
  unknown majors.
- **Minor** bumps add fields or enum values. Existing manifests remain
  valid.
- **Patch** bumps are clarifications and schema fixes.

A manifest declares which spec version it targets via `spawn_version`.

## 9. Compatibility with grok-install

`grok-install` (AgentMindCloud/grok-install, current v2.14) is a
platform-specific spawn manifest for Grok. Every universal-spawn manifest
can be mechanically lowered into a grok-install manifest when the
`compat.grok_install` field is set. The mapping rules are defined in
[`docs/grok-compat.md`](../../docs/grok-compat.md). Round-tripping is a
first-class concern: a grok-install manifest produced by lowering a
universal-spawn manifest MUST, when re-lifted, produce the same universal
manifest modulo field ordering.

## 10. Extensions

- **Platform extensions** live at `platforms.<platform-id>` and are
  validated against that platform's schema extension. The canonical
  platform ids, their schemas, and examples live under `platforms/` in
  this repository.
- **Vendor extensions** live under `x-ext` and MUST use a reverse-DNS
  prefix, for example `x-ext.com.example.metric`. Consumers MAY ignore
  these.

## Appendix A — Canonical taxonomy

The `categories` field accepts exactly these values:

```text
ai, audio, code, data, devtools, education, gaming, graphics, hardware,
health, music, productivity, research, robotics, science, security,
social, video, web, writing
```

Additional values MUST NOT be added outside a minor spec bump.

## Appendix B — Permission strings

A permission is `namespace:action` or `namespace:action:scope`.

| Namespace  | Actions                               | Example scope                 |
|------------|---------------------------------------|-------------------------------|
| `network`  | `outbound`, `inbound`                 | `network:outbound:api.x.com`  |
| `fs`       | `read`, `write`, `exec`               | `fs:write:/tmp`               |
| `clipboard`| `read`, `write`                       | —                             |
| `audio`    | `capture`, `playback`                 | —                             |
| `camera`   | `capture`                             | —                             |
| `geo`      | `read`                                | —                             |
| `bluetooth`| `scan`, `connect`                     | —                             |
| `usb`      | `enumerate`, `claim`                  | `usb:claim:vid=0x2341`        |
| `gpu`      | `compute`                             | —                             |
| `model`    | `call`, `train`, `finetune`           | `model:call:claude-opus-4-7`  |
| `payments` | `charge`, `refund`                    | —                             |
| `identity` | `read`                                | `identity:read:email`         |

A platform that does not recognize a namespace MUST refuse to spawn.

## Appendix C — Canonical serialization for signing

To produce the canonical byte sequence used for computing signatures:

1. Parse the manifest into its JSON data model.
2. Strip the `signatures` field.
3. Serialize using JCS (RFC 8785 — JSON Canonicalization Scheme).
4. Hash with SHA-256. Sign the hash with the algorithm named in the
   signature entry.

Implementations MUST use this canonical form. Whitespace-sensitive
serializations (such as raw YAML bytes) MUST NOT be signed directly.

## Appendix D — Conformance

An implementation is "universal-spawn v1.0.0 conformant" if it:

1. Accepts manifests in YAML, JSON, and TOML.
2. Validates against `manifest.schema.json` before any other processing.
3. Enforces the safety model in §6 when spawning.
4. Preserves unknown `x-ext.*` fields on round-trip.
5. Publishes a list of supported platform extensions.

Conformance tests will ship alongside v1.0.1.
