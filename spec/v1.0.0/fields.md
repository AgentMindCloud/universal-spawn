# Universal Spawn — Field Reference (v1.0.0)

This file documents every field in the manifest schema with rationale,
constraints, and worked examples. The normative definition remains
[`manifest.schema.json`](./manifest.schema.json).

Fields are grouped by purpose, not alphabetical order.

---

## Identity

### `spawn_version` — required

The spec version this manifest targets. Semantic versioning.

```yaml
spawn_version: "1.0.0"
```

Consumers MUST reject manifests whose major version is not supported.
Omitting this field is an error.

### `id` — required

A reverse-DNS identifier. Lowercase, dot-separated, stable across
renames.

```yaml
id: com.jansolo.fielded
```

Conventions:

- Use an owned domain or the org's handle-DNS.
- Never reuse an `id` for a different project.
- If the project moves repositories, the `id` stays.

### `name` — required

Human display name. No emoji. Shown in UIs and rich cards.

```yaml
name: Fielded
```

### `summary`

Optional single-line summary, ≤ 140 characters. Used in social embeds.

### `description` — required

One paragraph, 20–500 characters. Observational tone. The **first
sentence** must stand alone as a summary — search indexers use it.

### `kind` — required

The primary category of the creation. One of the enum values in the
schema. If your creation spans categories, pick the one a new user will
expect.

### `categories`

Up to four taxonomy categories. Canonical values are in spec Appendix A.

### `keywords`

Up to 16 lowercase kebab-case tags.

### `icon` / `hero_plate`

Paths (relative to repo root) or URLs to visual assets. See
[`design/residual-frequencies.md`](../../design/residual-frequencies.md)
for the visual system.

---

## Authorship & source

### `license` — required

SPDX identifier. For universal-spawn manifests we prefer OSI-approved
licenses. `proprietary` is accepted for closed creations.

### `author` — required

The primary maintainer.

```yaml
author:
  name: Jani Solo
  handle: JanSol0s
  org: AgentMindCloud
  url: https://github.com/JanSol0s
```

### `maintainers`

Additional maintainers in seniority order. Same shape as `author`.

### `source` — required

Where the canonical source lives.

```yaml
source:
  type: git
  url: https://github.com/AgentMindCloud/universal-spawn
  branch: main
  commit: 1a2b3c4d5e6f
  path: .
```

`path` is used when the creation is a child of a monorepo.

### `homepage`

Canonical public URL (docs, product site, landing page).

---

## Runtime & dependencies

### `runtime`

What the creation needs in order to actually run.

```yaml
runtime:
  language: python
  language_version: ">=3.11"
  engines:
    uv: ">=0.4"
  os: [linux, macos]
  arch: [x86_64, arm64]
  memory_mb_min: 512
  disk_mb_min: 100
  gpu_required: false
  network_required: true
```

### `dependencies`

Other spawn manifests required. Use the dependency's `id` and a version
range.

```yaml
dependencies:
  - id: org.agentmindcloud.grok-install
    version: ">=2.14"
  - id: com.anthropic.claude-sdk
    version: "^0.64"
    optional: false
```

---

## Entrypoints

### `entrypoints`

Each entry is an invokable surface. See spec §5.

```yaml
entrypoints:
  - id: main
    kind: http
    label: Public API
    ref: /api/v1
    inputs:
      - name: query
        type: string
        required: true
    outputs:
      - name: result
        type: object
    idempotent: true
  - id: cli
    kind: cli
    ref: bin/fielded
    inputs:
      - name: file
        type: file
        required: true
```

A CLI entrypoint's `ref` is the binary path. The platform constructs the
invocation; the manifest never contains shell commands.

---

## Safety

### `env_vars_required`

Environment variables the creation needs. Declare by **name only** —
never a value.

```yaml
env_vars_required:
  - name: ANTHROPIC_API_KEY
    description: Claude API key used for all model calls.
    required: true
    secret: true
  - name: PORT
    description: Port to bind the HTTP entrypoint to.
    required: false
    example: "8080"
```

### `min_permissions`

The smallest capability set under which the creation functions. Platforms
will not grant more without user consent.

```yaml
min_permissions:
  - network:outbound:api.anthropic.com
  - fs:read
  - fs:write:/tmp/fielded
```

Canonical namespaces live in spec Appendix B.

### `rate_limit_qps`

Self-declared upper bound on outbound request rate in queries per
second.

### `cost_limit_usd_daily`

Hard daily USD ceiling. Platforms SHOULD halt the creation before it
exceeds this number.

### `safe_for_auto_spawn`

True only if the author asserts the creation is safe to spawn without
human confirmation under `min_permissions` + declared limits. Default
false.

### `data_residency`

Regions where generated data may reside. `any` disables the check.

---

## Platforms & compatibility

### `platforms`

Object map keyed by platform id (`claude`, `gemini`, `openai`, `vercel`,
`netlify`, `unity`, `figma`, `discord`, `huggingface`, …). Each value is
validated against the platform's `schema.extension.json`. See the
[`platforms/`](../../platforms) directory.

```yaml
platforms:
  claude:
    skill_type: subagent
    model: claude-opus-4-7
  vercel:
    framework: nextjs
    build_command: "pnpm build"
```

### `spawn_targets`

Ordered preference list. First entry is the canonical target.

```yaml
spawn_targets: [claude, openai, gemini]
```

### `compat`

Cross-standard compatibility.

```yaml
compat:
  grok_install:
    version: "2.14"
    mapping_file: compat/grok-install.map.yaml
  openapi: openapi.yaml
  dockerfile: Dockerfile
```

---

## Integrity

### `signatures`

Detached signatures over the canonical serialization (spec Appendix C).

```yaml
signatures:
  - alg: ed25519
    key_id: did:key:z6Mki...
    value: "3w5...base64..."
```

### `x-ext`

Free-form experimental fields under reverse-DNS vendor prefixes.
Consumers MAY ignore any `x-ext.*` content.

```yaml
x-ext:
  com.example.rollout:
    percentage: 10
```

---

## Patterns

### Declaring a Claude skill

```yaml
kind: ai-skill
platforms:
  claude:
    skill_type: skill
    surface: [claude-code, claude-api]
```

### Declaring a Vercel deployable web app

```yaml
kind: web-app
entrypoints:
  - id: http
    kind: http
    ref: /
platforms:
  vercel:
    framework: nextjs
    output: .next
```

### Declaring a Unity game mod

```yaml
kind: game-mod
platforms:
  unity:
    target_version: "2023.2"
    scene: Assets/Scenes/Main.unity
```

Further patterns live inside each platform folder.
