# universal-spawn Specification

**Version**: 1.0
**Status**: Stable
**Canonical source**: `github.com/AgentMindCloud/universal-spawn`
**Editor**: Jani Solo (`@JanSol0s`), AgentMindCloud
**License**: Apache 2.0
**Normative schema**: [`universal-spawn.schema.json`](./universal-spawn.schema.json)

---

## 1. Introduction

A **universal-spawn manifest** is a single declarative file placed at
the root of a repository. It describes what a creation is, what it
needs, what it promises, and where it wants to run. It does not
describe how to do any of those things. The separation between
declaration and execution is the point of the standard.

universal-spawn is the cross-platform superset of
[`AgentMindCloud/grok-install`](https://github.com/AgentMindCloud/grok-install)
v2.14. grok-install remains the Grok-specific form; universal-spawn is
the form that works anywhere.

### 1.1 Goals

- **One file, every platform.** A single manifest at the root of a
  repository is enough for AI platforms, hosting providers, creative
  tools, game engines, social apps, and hardware tooling to spawn the
  creation. Platform-specific detail lives under `platforms.<id>`.
- **Strictly validatable.** Every spec version ships a JSON Schema
  that rejects malformed manifests unambiguously. Ambiguity is worse
  than incompatibility.
- **Safety by declaration.** The author publishes the smallest
  permission set, the maximum rate, and the cost ceiling. The platform
  enforces those numbers. The platform does not infer them.
- **Never hardcode secrets.** Secrets are declared by **name** in
  `env_vars_required`. The manifest is expected to be committed to a
  public repository.
- **Backwards compat is a feature.** Round-trip with grok-install is a
  first-class concern. Manifests valid under v1.0 remain valid under
  v1.x.

### 1.2 Non-goals

- universal-spawn is **not** a package manager or a build system. It
  references artifacts; it does not build them.
- universal-spawn does **not** define a registry. Multiple registries
  may exist; the standard does not pick a winner.
- universal-spawn does **not** attempt to abstract over platform APIs.
  The platform extensions are a thin shim for naming; each platform
  still defines what it does with the manifest.
- universal-spawn does **not** prescribe a UI. A consumer is free to
  render a manifest however it likes.

## 2. Conformance language

The key words **MUST**, **MUST NOT**, **REQUIRED**, **SHALL**, **SHALL
NOT**, **SHOULD**, **SHOULD NOT**, **RECOMMENDED**, **MAY**, and
**OPTIONAL** in this document are to be interpreted as described in
[RFC 2119](https://www.rfc-editor.org/rfc/rfc2119) when, and only when,
they appear in ALL CAPS.

## 3. File discovery

A conformant consumer scanning a repository **MUST** look for a
manifest in this order. The first file found wins; subsequent matches
are ignored for discovery purposes (but may still be inspected by
tooling for diagnostics).

1. `universal-spawn.yaml`
2. `universal-spawn.yml`
3. `universal-spawn.json`
4. `universal-spawn.toml`
5. `spawn.yaml`
6. `spawn.yml`
7. `spawn.json`
8. `spawn.toml`
9. `.spawn/config.yaml`
10. `.spawn/config.yml`
11. `.spawn/config.json`
12. `.spawn/config.toml`
13. A top-level `universalSpawn` key inside `package.json`.
14. A `[tool.universal-spawn]` section inside `pyproject.toml`.

A consumer **MUST NOT** read a manifest from any other location as
part of routine discovery. Explicit user input — for example,
"validate this specific file" — is out of scope.

The following file names are **NOT** accepted and **MUST** be ignored:

- `spawn-manifest.*`
- `us.yaml`, `us-spawn.yaml`
- Any filename embedded inside a build output directory (`dist/`,
  `build/`, `out/`, `.next/`, `.nuxt/`, `target/`).

### 3.1 Serialization equivalence

YAML, JSON, and TOML forms of a manifest describe the same JSON data
model. Consumers **SHOULD** accept all four serializations for file
discovery, but **MAY** refuse any single one.

The canonical serialization used for signing is defined in §14.

### 3.2 Character set

UTF-8. All string fields accept Unicode, but identifiers (`name`
pattern, environment variable names, `metadata.keywords` entries)
are restricted by the schema. The `name` and `description` fields
**MUST NOT** contain emoji. Lint tooling enforces the emoji rule;
JSON Schema regex cannot portably express Unicode property escapes.

## 4. Root fields

The following four fields are **REQUIRED**:

- `version` — a string, currently the literal `"1.0"`.
- `name` — a human-readable display name.
- `description` — a single paragraph, 10 to 500 characters.
- `type` — a one-of enum value (see §4.4).

A manifest **MUST** include at least one of `platforms` or
`deployment`. A manifest with neither has nothing for any consumer to
act on and **MUST** be rejected.

### 4.1 `version`

```yaml
version: "1.0"
```

Consumers **MUST** reject a manifest whose `version` they do not
implement. Tolerant parsing of unknown majors is **NOT** allowed;
silent acceptance of an unknown major is a security issue by way of
ambiguity.

### 4.2 `name`

A display name, 1–80 characters. Pattern:
`^[A-Za-z0-9](?:[A-Za-z0-9 ._-]*[A-Za-z0-9])?$`.

Allowed: alphanumerics, space, dot, underscore, dash. No leading or
trailing whitespace. No emoji.

### 4.3 `description`

A single paragraph, 10–500 characters. The first sentence **SHOULD**
stand alone as a summary — search indexers use it as a snippet.

Authors **SHOULD** prefer observational prose over marketing prose.
"Prints a greeting" beats "Revolutionary new CLI experience."

### 4.4 `type`

One of the following values. The list is exhaustive in v1.0; additions
ship in minor revisions.

```text
ai-agent, ai-skill, ai-model, web-app, api-service, cli-tool,
library, dataset, notebook, creative-tool, design-template, game-mod,
game-world, hardware-device, firmware, bot, extension, plugin, site,
container, workflow
```

If your creation spans types, pick the one a new user will expect.

## 5. Platforms object

```yaml
platforms:
  claude: { ... }     # validated by platforms/claude/schema.extension.json
  vercel: { ... }     # validated by platforms/vercel/schema.extension.json
```

Each key is a registered platform id. Each value is validated against
that platform's `schema.extension.json`. The master schema treats the
values as opaque `object`s; the platform extension schemas do the
strict validation.

### 5.1 Registered platforms in v1.0

`claude`, `gemini`, `openai`, `vercel`, `netlify`, `unity`, `figma`,
`discord`, `huggingface`. Each has a folder under `platforms/` in the
canonical repository containing the extension schema, a compatibility
matrix, and at least two worked examples.

Additional platforms register through the new-platform issue form
(`.github/ISSUE_TEMPLATE/new_platform.yml`) followed by a PR that
creates the platform folder. See [`CONTRIBUTING.md`](../../CONTRIBUTING.md#adding-a-platform).

### 5.2 Unknown platform keys

A consumer **MUST** ignore platform keys it does not recognize. An
unknown platform key is not an error; it simply means that consumer
does not spawn to that target.

A consumer that claims support for a specific platform **MUST**
validate the corresponding value against the registered extension
schema and **MUST** reject the manifest if validation fails.

## 6. Safety object

```yaml
safety:
  min_permissions:
    - network:outbound:api.anthropic.com
    - fs:read
  rate_limit_qps: 5
  cost_limit_usd_daily: 20
  safe_for_auto_spawn: false
  data_residency: [us, eu]
```

### 6.1 `min_permissions`

A list of capability strings. Each string is
`namespace:action[:scope]`. Namespace and action are lowercase; scope
accepts hostnames, filesystem paths, and key=value identifiers.

#### 6.1.1 Canonical namespaces (v1.0)

| Namespace   | Actions                             | Scope form                                      |
|-------------|-------------------------------------|-------------------------------------------------|
| `network`   | `outbound`, `inbound`               | hostname (`api.anthropic.com`) or empty          |
| `fs`        | `read`, `write`, `exec`             | absolute path (`/tmp/fielded`) or empty         |
| `clipboard` | `read`, `write`                     | empty                                           |
| `audio`     | `capture`, `playback`               | empty                                           |
| `camera`    | `capture`                           | empty                                           |
| `geo`       | `read`                              | empty                                           |
| `bluetooth` | `scan`, `connect`                   | empty                                           |
| `usb`       | `enumerate`, `claim`                | key=value (`vid=0x2341`, `vid=0x2341&pid=0x0043`) |
| `gpu`       | `compute`                           | empty                                           |
| `model`     | `call`, `train`, `finetune`         | model id (`claude-opus-4-7`)                    |
| `payments`  | `charge`, `refund`                  | empty                                           |
| `identity`  | `read`                              | attribute (`email`)                             |
| `messages`  | `read`                              | empty                                           |

A consumer that does not recognize a namespace **MUST** refuse to
spawn. A consumer that recognizes the namespace but not the action
**MUST** refuse to spawn. A consumer that recognizes both but not
the specific scope **SHOULD** refuse; narrower scope enforcement is
always stricter than broader.

#### 6.1.2 Scope narrowing

A scope narrows a permission. `network:outbound:api.anthropic.com` is
strictly narrower than `network:outbound`. A consumer that granted the
broader permission would still accept a manifest declaring the
narrower form; a consumer that granted only the narrower permission
**MUST NOT** accept a manifest declaring the broader form.

Authors **SHOULD** declare the narrowest scope they can. A manifest
that declares `network:outbound` (no scope) is making a weaker safety
claim than one that declares five named hostnames.

#### 6.1.3 Transitive permissions through dependencies

Manifests that reference other universal-spawn manifests (via a
future `dependencies[]` field tracked in v1.1) transitively inherit
those manifests' declared permissions. A spawn host resolving a
dependency tree **MUST** union all declared `min_permissions` from
the tree and present that union to the user for consent. Silent
inheritance is prohibited; a dependency cannot grant its consumer a
permission the consumer has not declared.

### 6.2 `rate_limit_qps`

Self-declared maximum outbound request rate, in queries per second.
Consumers **SHOULD** rate-limit to this number. Consumers **MAY**
apply stricter limits.

### 6.3 `cost_limit_usd_daily`

Self-declared upper bound on daily USD cost. Consumers **MUST** halt
spawning before this ceiling is exceeded when cost is attributable to
the manifest.

### 6.4 `safe_for_auto_spawn`

Boolean, default `false`. When `true`, the author certifies that
spawning is safe under `min_permissions` and the declared limits,
without human confirmation. Consumers **MAY** require confirmation
anyway; this is a floor, not a ceiling.

### 6.5 `data_residency`

An array drawn from `us, eu, uk, ca, au, jp, sg, br, in, any`. Used
to select a regional endpoint where the platform supports one.

## 7. Deployment object

```yaml
deployment:
  targets: [vercel, netlify]
  regions: [iad1, cdg1]
  build:
    command: "pnpm build"
    output: ".next"
    engine: "node"
    install: "pnpm install --frozen-lockfile"
    node_version: "20"
```

- `targets` — ordered preference list. The first entry is the
  canonical target. Values are free-form strings so creators can
  target registries (`npm`, `homebrew`, `cargo`, `pypi`, `modrinth`,
  `curseforge`) alongside platform ids.
- `regions` — platform-specific region codes. A manifest MAY declare
  region preferences even when the platform has its own
  `regions` field in its extension; the platform's field takes
  precedence for the platform's own deploy.
- `build` — optional build configuration. `command` is a string, not
  an array, because the manifest never embeds shell composition. The
  platform executes the string as-is in its builder environment.
- `build.install` — optional install step (`pnpm install`,
  `pip install -r requirements.txt`). Separated from `build.command`
  so caches line up cleanly between runs.
- `build.engine` — a free-form hint. Canonical values when present:
  `node`, `python`, `rust`, `go`, `ruby`, `java`, `dotnet`, `docker`,
  `unity`, `godot`, `gradle`. Consumers **MAY** use this to pick a
  builder image; **MAY** ignore it entirely.
- `build.node_version` — shortcut when `build.engine` is `node`.
  Equivalent information typically lives in `.nvmrc`; putting it in
  the manifest makes it visible to registries.

A manifest **MUST** include `platforms`, `deployment`, or both (per
§4). A manifest with `deployment.targets: []` is invalid.

### 7.1 Target strings

Common deployment target strings that appear in the example corpus:

| Category         | Target strings                                          |
|------------------|---------------------------------------------------------|
| AI platforms     | `claude`, `gemini`, `openai`, `grok`                   |
| Hosting          | `vercel`, `netlify`, `cloudflare`, `fly`               |
| Model / dataset  | `huggingface`                                           |
| Social           | `discord`                                               |
| Creative         | `figma`                                                 |
| Game             | `unity`, `godot`, `steam`                               |
| Package managers | `npm`, `pypi`, `homebrew`, `cargo`, `maven`             |
| Mods             | `modrinth`, `curseforge`                                |
| Embedded         | `platformio`, `esp-idf`                                 |

This list is illustrative. The core schema does not enforce an enum
because the set grows continuously. Consumers that recognize a target
act on it; unrecognized targets are ignored.

### 7.2 `deployment` vs `platforms`

`platforms.<id>` carries platform-specific options (framework preset,
runtime memory, allowed hosts). `deployment` carries cross-platform
build shape. When a manifest targets exactly one platform, the two
overlap in practice. When it targets multiple platforms, `deployment`
describes what is common; `platforms.<id>` describes what differs.

## 8. `env_vars_required`

```yaml
env_vars_required:
  - name: ANTHROPIC_API_KEY
    description: API key used for Claude model calls.
    required: true
    secret: true
  - name: PORT
    description: Port the HTTP entrypoint binds to.
    required: false
    example: "8080"
```

- `name` — SCREAMING_SNAKE_CASE, first character A–Z.
- `description` — 3+ characters. Purpose of the variable.
- `required` — defaults to `true`.
- `secret` — defaults to `false`. When `true`, the consumer **MUST**
  supply the value from its credential store, never from a manifest
  literal.
- `example` — optional illustrative value. **MUST NOT** be a real
  secret.

Secret values are never stored in a manifest. The manifest declares
the **shape** of the env; the platform provides the **values**.

## 9. Visuals object

```yaml
visuals:
  icon: assets/icon.svg
  hero_plate: assets/hero.svg
  banner: assets/banner.png
  palette: parchment
```

- `icon` — 512×512 recommended, SVG preferred.
- `hero_plate` — the hero illustration for rich cards.
- `banner` — optional wide banner.
- `palette` — one of `parchment`, `ink`, `field` (Residual
  Frequencies palette ids). Following the visual system is
  **RECOMMENDED** but not **REQUIRED**.

All three asset paths are URI references (relative paths inside the
repository, or absolute URLs).

## 10. Metadata

```yaml
metadata:
  license: Apache-2.0
  author:
    name: Jani Solo
    handle: JanSol0s
    org: AgentMindCloud
  maintainers:
    - { name: River Chen, handle: riverc }
  source:
    type: git
    url: https://github.com/AgentMindCloud/fielded
    branch: main
    commit: 1a2b3c4d5e6f7a8b9c0d
    path: .
  keywords: [research, citations, agent]
  categories: [ai, research, writing]
  id: org.agentmindcloud.fielded
```

- `license` — SPDX identifier or `proprietary`.
- `author` — primary maintainer. `handle` is the canonical social
  handle (GitHub username by convention).
- `maintainers` — additional maintainers, ordered by seniority.
- `source` — canonical source. `type` is one of `git`, `hg`, `svn`,
  `archive`. `commit` is a 7–64 char hex.
- `keywords` — up to 16 kebab-case tags.
- `categories` — up to 4 taxonomy entries.
- `id` — **OPTIONAL** reverse-DNS stable identifier. When present, it
  survives renames and forks.

## 11. Validation rules

A manifest is **valid** iff:

1. It parses as YAML, JSON, or TOML into the v1.0 data model.
2. It passes the JSON Schema at
   [`universal-spawn.schema.json`](./universal-spawn.schema.json).
3. For every key under `platforms`, the value passes the corresponding
   platform extension schema.

The following are **NOT** part of validity, but are **RECOMMENDED**
lint checks:

- Every `env_vars_required[*].name` with `required: true` exists in
  the target environment's secret store at spawn time.
- Every relative path in `visuals.*` resolves to a file in the
  repository.
- `metadata.id` matches a reverse-DNS prefix the author controls.
- `name` and `description` do not contain emoji.

Consumers **SHOULD** run lint checks and surface their output as
warnings. Consumers **MUST NOT** promote a lint warning to a
validity error.

### 11.1 Reference validator

A reference Node-based validator is run in CI for this repository:

```bash
npx ajv-cli validate --all-errors --spec=draft7 -c ajv-formats \
  -s spec/v1.0/universal-spawn.schema.json \
  -d "spec/v1.0/examples/*.yaml"
```

Python, Go, Rust, and Swift implementations **SHOULD** produce the
same verdict on every example in `spec/v1.0/examples/`.

### 11.2 Error catalog

The JSON Schema validator emits errors keyed by instance path. The
most common and their remediations:

| Symptom                                              | Remediation                                      |
|------------------------------------------------------|---------------------------------------------------|
| `required property "version" missing`                | Add `version: "1.0"` at the top.                  |
| `"version" must be equal to "1.0"`                  | Use the literal string `"1.0"`, not `1.0` or `"v1.0"`. |
| `"name" does not match pattern ...`                  | No leading/trailing whitespace; no emoji; only alphanumerics, space, dot, dash, underscore. |
| `"description" does not meet minimum length 10`      | Write at least one complete sentence.             |
| `"description" exceeds maximum length 500`           | Split long copy into `summary` + `description`.   |
| `"type" must be one of [...]`                        | Pick one from §4.4.                               |
| `must match anyOf`                                   | Add at least one of `platforms` or `deployment`.  |
| `"env_vars_required[N].name" does not match pattern` | SCREAMING_SNAKE_CASE; first char A-Z.             |
| `additional property "X" not allowed`                | Field name is misspelled or belongs in v1.1.      |
| Unknown extension key under `platforms.X`            | Check that platform's `schema.extension.json`; the extension is strict. |

### 11.3 Lint vs validity

Validity is binary: a manifest passes the JSON Schema or it does not.
Lint is a separate, softer layer that implementers **SHOULD** run:

- Reachability — every relative path under `visuals.*` resolves to a
  file in the repository.
- Secret shape — `env_vars_required[*].example` does not match common
  secret patterns (API key prefixes, JWT structure, 40-character
  hex).
- Emoji — `name` and `description` are emoji-free.
- Scope depth — each `safety.min_permissions` entry narrows past the
  bare namespace+action.
- Platform coverage — every `platforms.<id>` has an extension schema
  on disk.

Lint tools **MUST NOT** promote warnings to validity failures. An
over-eager linter that blocks a structurally valid manifest is a
bug.

## 12. Platform extension rules

Each platform folder in `platforms/<id>/` ships:

- `schema.extension.json` — a strict JSON Schema with
  `additionalProperties: false` at every level.
- `compatibility.md` — which core fields the platform honors.
- `README.md` — narrative overview.
- `examples/` — at least two complete worked examples that validate
  against both the master schema and this extension.

The extension schema's `$id` **MUST** be
`https://universal-spawn.org/platforms/<id>/v1.0.0/schema.extension.json`
(kept at `v1.0.0` within the `v1.x` line so extension minor bumps do
not require a major revision of the core spec).

Registering a new platform: open a
[`new_platform`](../../.github/ISSUE_TEMPLATE/new_platform.yml) issue,
then submit a PR creating the folder. Two maintainer approvals are
required.

## 12.5 Interoperability with adjacent standards

universal-spawn is a manifest standard; it does not replace the
adjacent standards most projects already ship. The intended pattern
is **cohabitation**.

### 12.5.1 OpenAPI

If your creation exposes an HTTP API, ship an OpenAPI document
(`openapi.yaml`) alongside your universal-spawn manifest. The
manifest's `platforms.<id>` block — for Vercel, Netlify, Claude
Actions, OpenAI Actions, or Gemini Extensions — MAY point at the
OpenAPI path so the platform's ingest uses it directly. Duplication
is not required; the OpenAPI file is the contract for HTTP shape,
and the universal-spawn manifest is the contract for identity,
safety, and deployment.

### 12.5.2 OCI images and Dockerfiles

A creation that ships as a container image declares the image tag
under `platforms.<id>` or inside `deployment.build`, and keeps its
Dockerfile alongside. universal-spawn does not try to subsume
container runtime metadata (labels, entrypoint arrays, healthchecks).
Those remain in the image.

### 12.5.3 `package.json` / `pyproject.toml`

A project may already host its dependencies and scripts in
`package.json` (JavaScript) or `pyproject.toml` (Python). The
universal-spawn manifest sits **beside** those files, not inside
them, except via the explicit embedded forms documented in §3.
Dependencies belong in the ecosystem's own manifest; universal-spawn
references, it does not redeclare.

### 12.5.4 Platform-native manifests

Each platform typically has its own manifest format — `vercel.json`,
`netlify.toml`, `.claude/skill.yaml`, Figma's `manifest.json`, Unity's
`package.json` under `Packages/`. Authors **SHOULD** keep those files
in place and describe only the cross-platform surface in
universal-spawn. Duplicating a Vercel `headers[]` array into
`platforms.vercel` is a v1.1 concern; in v1.0 the platform's own
manifest remains authoritative for platform-exclusive fields.

### 12.5.5 grok-install

Full walkthrough in §13 and
[`migration/from-grok-install.md`](./migration/from-grok-install.md).

## 13. grok-install compatibility

universal-spawn v1.0 is the cross-platform superset of
`AgentMindCloud/grok-install` v2.14. Every universal-spawn manifest
can be mechanically lowered into a grok-install manifest when the
fields needed by grok-install are present. Every grok-install manifest
can be lifted into a universal-spawn manifest without information
loss.

The canonical field mapping lives in
[`migration/from-grok-install.md`](./migration/from-grok-install.md).
The round-trip invariant is:

> For a grok-install manifest `g`, `U(g)` is a universal-spawn
> manifest that parses back to `g` under `L(U(g))`, modulo field
> ordering.

Lowering a universal-spawn manifest with no `platforms.grok` and no
grok-install-specific fields is a no-op: such a manifest is not
grok-install-bound.

## 14. Security model

The safety model is **declaration plus enforcement**. Full analysis
lives in [`docs/safety-model.md`](../../docs/safety-model.md).
Summary:

- A creation declares its envelope (§6). The consumer enforces it.
- Secrets are declared by name (§8). The consumer supplies values.
- Signatures (§15) are optional in v1.0 and hardened in v1.2.

A consumer **MUST NOT** grant capabilities outside `min_permissions`
without explicit user consent. A consumer **MUST NOT** exceed
`cost_limit_usd_daily` when the costs are attributable to the
manifest. A consumer **MUST NOT** store secret values inside the
manifest itself.

Consumers **SHOULD** log the canonical hash of every manifest they
spawn so later audits can detect silent swaps.

## 15. Signatures (informative — hardened in v1.2)

v1.0 defines the canonical serialization used for signing so that
tooling can ship today, but does not mandate signature verification.

Canonical procedure:

1. Parse the manifest into its JSON data model.
2. Remove the `signatures` field if present.
3. Serialize using [JCS — JSON Canonicalization Scheme (RFC 8785)](https://www.rfc-editor.org/rfc/rfc8785).
4. Hash with SHA-256.
5. Sign the hash with Ed25519 (preferred), ECDSA P-256, or RSA-SHA256.

Signatures are stored back under `x-ext.org.universal-spawn.signatures`
during v1.x; a first-class `signatures` field is introduced in v1.2.

## 16. IANA considerations

universal-spawn **PROPOSES** the following media types:

- `application/vnd.universal-spawn+yaml` — YAML form.
- `application/vnd.universal-spawn+json` — JSON form.
- `application/vnd.universal-spawn+toml` — TOML form.

File extensions: `.yaml`, `.yml`, `.json`, `.toml`. The discovery
order in §3 identifies which file within a repository is the
manifest; media types are for HTTP transport.

Registration with IANA is tracked under
[`spec/future-versions/v1.1-proposals.md`](../future-versions/v1.1-proposals.md).

## 17. Versioning

The specification uses strict semantic versioning.

- **Major (`X.0`)** — breaking change. Valid v1 manifests MAY be
  invalid under v2. Consumers **MUST** refuse any major version they
  do not support.
- **Minor (`X.Y`)** — additive. New optional fields, new enum values,
  new platforms, new entrypoint kinds.
- **Patch (`X.Y.Z`)** — editorial. Clarifications, schema fixes.

Within v1, a manifest valid under v1.0 stays valid under v1.5.

Deprecation: a field MAY be marked deprecated in a minor release. It
**MUST** continue to validate and be honored until the next major.

## 17.5 Tooling ecosystem

universal-spawn is deliberately small at the core so that tooling can
grow around it without coordination. A healthy ecosystem includes:

- **Validators** — at minimum, one per popular language (Node,
  Python, Go, Rust, Swift). All **SHOULD** produce identical verdicts
  on every file in `spec/v1.0/examples/`. A shared conformance test
  suite is in scope for v1.0.1.
- **Formatters** — tools that normalize manifest field order, quote
  style, and indentation. Identical input under any formatter
  **MUST** produce semantically identical output (round-trip through
  parse). Formatters **MUST NOT** drop unknown `x-ext.*` fields.
- **Linters** — tools that surface §11.3 lint warnings. A linter
  **MUST NOT** promote lint warnings to validity errors.
- **Generators** — templates that emit a first-draft manifest for a
  given project shape. The twelve examples in
  `spec/v1.0/examples/` serve as generator seeds.
- **Registries** — read-only indexes that crawl public repositories
  for manifests. A registry **MUST** validate against the master
  schema before accepting a manifest for indexing and **MUST** link
  back to the source repository at a specific commit.
- **Conformance reporters** — tools that tell a platform whether its
  implementation matches the conformance checklist in Appendix C.

All of the above live in sibling repositories or downstream projects.
None of them are part of this repository; the specification is
purposefully tool-neutral.

### 17.5.1 CI integration

A typical project wires validation into CI as a pre-merge gate:

```yaml
# .github/workflows/validate-spawn.yml (project-side example)
name: validate-spawn
on: [push, pull_request]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: "20" }
      - run: |
          npx ajv-cli validate --all-errors --spec=draft7 \
            -s https://universal-spawn.dev/spec/v1.0/universal-spawn.schema.json \
            -d universal-spawn.yaml \
            -c ajv-formats
```

This is the recommended minimum. Projects that add lint steps
(cspell, markdownlint on the adjacent README, shellcheck on the
build command) gain from doing so, but universal-spawn does not
mandate them.

## 18. Conformance

A consumer is "universal-spawn v1.0 conformant" if it:

1. Performs the file discovery in §3.
2. Validates against the master schema and every applicable extension
   schema before any other processing.
3. Refuses unknown major `version` values.
4. Enforces the safety model in §6 when spawning.
5. Preserves unknown `x-ext.*` fields on round-trip.
6. Publishes the list of platform extensions it supports.

A conformance test suite ships alongside v1.0.1 — see the roadmap.

## 19. References

- RFC 2119 — Key words for use in RFCs to indicate requirement levels.
- RFC 8259 — The JavaScript Object Notation (JSON) Data Interchange Format.
- RFC 8785 — JSON Canonicalization Scheme (JCS).
- [JSON Schema draft-07](https://json-schema.org/draft-07/json-schema-release-notes.html).
- [YAML 1.2.2](https://yaml.org/spec/1.2.2/).
- [TOML 1.0.0](https://toml.io/en/v1.0.0).
- [Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/).
- [SemVer 2.0.0](https://semver.org/spec/v2.0.0.html).
- [AgentMindCloud/grok-install](https://github.com/AgentMindCloud/grok-install) (v2.14).

## Appendix A — Discovery examples

| Repository contains                | Manifest read             |
|------------------------------------|----------------------------|
| `universal-spawn.yaml`             | `universal-spawn.yaml`    |
| `universal-spawn.yaml`, `spawn.yaml` | `universal-spawn.yaml`  |
| `spawn.toml`                       | `spawn.toml`              |
| `.spawn/config.json`               | `.spawn/config.json`      |
| `package.json` with `universalSpawn` | The embedded object     |
| `pyproject.toml` with `[tool.universal-spawn]` | The TOML table  |
| None of the above                  | No manifest               |

## Appendix B — Minimal manifest

```yaml
version: "1.0"
name: Hello
type: cli-tool
description: A small reference CLI that prints a greeting and exits.
deployment:
  targets: [npm]
```

This file validates. Adding `safety`, `env_vars_required`, `visuals`,
and `metadata` is additive.

## Appendix C — Conformance checklist for implementers

- [ ] File discovery per §3.
- [ ] Accepts YAML, JSON, TOML.
- [ ] Validates against master schema before any other processing.
- [ ] Validates each platform value against its extension schema.
- [ ] Refuses unknown majors.
- [ ] Enforces `min_permissions` at the runtime boundary.
- [ ] Enforces `rate_limit_qps` and `cost_limit_usd_daily`.
- [ ] Stores `env_vars_required` values in a credential store, not
      the manifest.
- [ ] Requires user confirmation when `safe_for_auto_spawn` is false
      or absent.
- [ ] Preserves unknown `x-ext.*` fields on round-trip.
- [ ] Publishes a list of supported platform extensions.
