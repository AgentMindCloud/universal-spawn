<!--
  universal-spawn — canonical repository
  Residual Frequencies · Parchment palette
  Hero plate: archetype F — Module Constellation
-->

<p align="center">
  <img src="assets/hero.svg" alt="Module Constellation — Residual Frequencies parchment plate" width="880">
</p>

<p align="center">
  <em>Plate F · Module Constellation · Residual Frequencies</em>
</p>

---

# universal-spawn

**A declarative manifest format for spawning any creation on any
platform.**

`universal-spawn` is an open standard. A single file at the root of your
repository — `spawn.yaml` — makes your creation discoverable,
validatable, and one-click spawnable across AI platforms, hosting
providers, creative tools, dev ecosystems, games, social apps, and
hardware.

Think of it as the **OpenAPI of installable creations**.

- Declarative only — a manifest never contains executable code.
- Strictly validatable — every spec version ships a JSON Schema.
- Universal first — the core manifest works anywhere.
- Platform extensions unlock platform-native perks.
- Safety is a declaration, not a promise: `min_permissions`,
  `rate_limit_qps`, `cost_limit_usd_daily`, `safe_for_auto_spawn`,
  `env_vars_required` — the author publishes the envelope, the platform
  enforces it.

This repository is the **canonical source**:
[`github.com/AgentMindCloud/universal-spawn`](https://github.com/AgentMindCloud/universal-spawn).
Maintained by Jani Solo ([`@JanSol0s`](https://github.com/JanSol0s)) under
the AgentMindCloud organization. Licensed Apache 2.0 in perpetuity.

---

## The minimal manifest

```yaml
spawn_version: "1.0.0"
id: com.example.hello
name: Hello
kind: cli-tool
description: >
  A small reference command-line tool that prints a greeting and exits
  zero. Used as the canonical minimal example for the universal-spawn
  specification.
license: Apache-2.0
author:
  name: Jane Doe
  handle: janedoe
source:
  type: git
  url: https://github.com/janedoe/hello
entrypoints:
  - id: cli
    kind: cli
    ref: bin/hello
min_permissions: []
```

That file, at the root of a repo, is enough to make the project
discoverable, validatable, and spawnable on any conformant platform.
More fields unlock more behavior; see
[`spec/v1.0.0/fields.md`](spec/v1.0.0/fields.md).

The canonical schema `$id` is
`https://universal-spawn.org/spec/v1.0.0/manifest.schema.json`. Beyond
the required core, the schema also admits `spawn_targets` (preferred
platform ordering), `signatures[]` (detached ed25519 / ecdsa-p256 /
rsa-sha256 over the canonical serialization), `compat.openapi`,
`compat.dockerfile`, `compat.grok_install`, and an `x-ext`
reverse-DNS-prefixed escape hatch for experimental fields. The `kind`
enum covers twenty-one categories — from `ai-agent` and `cli-tool` to
`game-mod`, `hardware-device`, and `workflow`.

---

## How it works

```
                   ┌────────────────────────────────┐
                   │        spawn.yaml (root)       │
                   │  one declarative manifest      │
                   └─────────────────┬──────────────┘
                                     │
       validated by manifest.schema.json (draft 2020-12)
                                     │
       ┌───────────┬─────────┬───────┼───────┬──────────┬──────────┐
       ▼           ▼         ▼       ▼       ▼          ▼          ▼
    claude      gemini    openai  vercel  netlify     unity      figma
    (and discord, huggingface, grok-install, …)
```

The core manifest is universal. Each platform reads the fields that
apply to it; platform-specific extensions live under
`platforms.<platform-id>` and are validated by that platform's
[`schema.extension.json`](platforms/).

---

## Why this exists

Every platform has invented its own installable-creation format. The
same AI skill gets packaged four times for four stores. The same game
mod gets re-described for three engines. The same deployable web app
gets a separate manifest per host. None of them interoperate.

We have a standard for describing HTTP APIs (OpenAPI). We have a
standard for describing containers (OCI). We have a standard for
describing JavaScript dependencies (`package.json`). We do not have a
standard for describing **a spawnable creation**.

That is what this file is.

---

## Principles

1. **Declarative only.** Manifests describe *what*, never *how*.
2. **Strict validation.** If the JSON Schema rejects it, platforms
   reject it.
3. **Universal first, platform second.** Platform perks unlock through
   extensions, not through replacing the core.
4. **Safety through declaration.** Authors publish the permission, rate,
   and cost envelope. Platforms enforce it.
5. **Never hardcode secrets.** Env vars are declared by name.
6. **Backwards compat is a feature.** Round-tripping with
   [`AgentMindCloud/grok-install`](https://github.com/AgentMindCloud/grok-install)
   v2.14 is first-class.
7. **Apache 2.0 forever.** No field of the spec may land under another
   license.

---

## Repository layout

```
spec/
  v1.0.0/
    spec.md                   ← normative prose
    manifest.schema.json      ← normative JSON Schema
    fields.md                 ← field reference
    compatibility-matrix.md   ← per-platform field coverage
  versioning.md               ← version policy
examples/                     ← complete example manifests
platforms/                    ← one folder per supported platform
  claude/
  gemini/
  openai/
  vercel/
  netlify/
  unity/
  figma/
  discord/
  huggingface/
docs/                         ← narrative docs (quickstart, safety, …)
design/                       ← design system (Residual Frequencies)
scripts/
  validate.py                 ← validator used by CI
.github/workflows/validate.yml ← CI: validate every manifest on PR
```

---

## Quickstart

1. Copy [`examples/minimal.spawn.yaml`](examples/minimal.spawn.yaml) to
   `spawn.yaml` at the root of your repo.
2. Fill in `id`, `name`, `kind`, `description`, `license`, `author`,
   `source`.
3. Declare `entrypoints` for the surfaces you expose.
4. Declare `min_permissions`, `env_vars_required`, and any cost or rate
   ceilings.
5. Add platform extensions under `platforms.<id>` as needed.
6. Validate:

   ```bash
   npx ajv-cli validate \
     -s https://universal-spawn.org/spec/v1.0.0/manifest.schema.json \
     -d spawn.yaml --spec=draft2020
   ```

   Or run the repo's own validator, which also checks every platform
   extension schema:

   ```bash
   pip install jsonschema pyyaml
   python scripts/validate.py
   ```

Full walkthrough in [`docs/quickstart.md`](docs/quickstart.md). CI
([`.github/workflows/validate.yml`](.github/workflows/validate.yml))
runs `scripts/validate.py` on every push and pull request to `main`;
any manifest that fails the core schema or its platform extension
blocks merge.

---

## Supported platforms

| Platform      | Folder                                          | Status       |
|---------------|-------------------------------------------------|--------------|
| Claude        | [`platforms/claude`](platforms/claude)           | v1.0.0 ready |
| Gemini        | [`platforms/gemini`](platforms/gemini)           | v1.0.0 ready |
| OpenAI        | [`platforms/openai`](platforms/openai)           | v1.0.0 ready |
| Vercel        | [`platforms/vercel`](platforms/vercel)           | v1.0.0 ready |
| Netlify       | [`platforms/netlify`](platforms/netlify)         | v1.0.0 ready |
| Unity         | [`platforms/unity`](platforms/unity)             | v1.0.0 ready |
| Figma         | [`platforms/figma`](platforms/figma)             | v1.0.0 ready |
| Discord       | [`platforms/discord`](platforms/discord)         | v1.0.0 ready |
| Hugging Face  | [`platforms/huggingface`](platforms/huggingface) | v1.0.0 ready |

Adding a platform is an ordinary pull request; see
[`CONTRIBUTING.md`](CONTRIBUTING.md#adding-a-platform).

---

## Examples

Every file in [`examples/`](examples) is a complete, schema-valid
manifest. CI enforces the invariant that each one validates.

| File                                                            | Demonstrates                                |
|-----------------------------------------------------------------|---------------------------------------------|
| [`minimal.spawn.yaml`](examples/minimal.spawn.yaml)             | The smallest manifest that validates.       |
| [`full.spawn.yaml`](examples/full.spawn.yaml)                   | Every field of the schema in use.           |
| [`ai-agent.spawn.yaml`](examples/ai-agent.spawn.yaml)           | A tool-calling AI agent.                    |
| [`web-app.spawn.yaml`](examples/web-app.spawn.yaml)             | A Next.js app with host extensions.         |
| [`creative-tool.spawn.yaml`](examples/creative-tool.spawn.yaml) | A Figma plugin.                             |
| [`game-mod.spawn.yaml`](examples/game-mod.spawn.yaml)           | A Unity mod with scene entrypoint.          |
| [`hardware-device.spawn.yaml`](examples/hardware-device.spawn.yaml) | Firmware for an embedded device.        |
| [`cross-platform.spawn.yaml`](examples/cross-platform.spawn.yaml)   | One manifest, six spawn targets.        |

Each platform directory also ships at least two worked examples under
`platforms/<id>/examples/`.

---

## Documentation

Narrative docs live in [`docs/`](docs):

| File                                                    | For                                            |
|---------------------------------------------------------|------------------------------------------------|
| [`quickstart.md`](docs/quickstart.md)                   | Authors adding their first `spawn.yaml`.       |
| [`field-reference.md`](docs/field-reference.md)         | Narrative walkthrough of every core field.     |
| [`validation.md`](docs/validation.md)                   | How to validate a manifest — tooling and CI.   |
| [`safety-model.md`](docs/safety-model.md)               | Threat analysis and enforcement obligations.   |
| [`grok-compat.md`](docs/grok-compat.md)                 | Round-tripping with AgentMindCloud/grok-install. |
| [`faq.md`](docs/faq.md)                                 | Decisions and non-decisions explained.         |

The visual system is documented in
[`design/residual-frequencies.md`](design/residual-frequencies.md).

---

## Relationship to `grok-install`

`universal-spawn` is the **universal sibling** to
[`AgentMindCloud/grok-install`](https://github.com/AgentMindCloud/grok-install)
(current v2.14). grok-install is the Grok-specific form; universal-spawn
is the cross-platform superset. A universal-spawn manifest can be
lowered into a grok-install manifest mechanically, and a grok-install
manifest can be lifted back into a universal-spawn manifest without
information loss when the `compat.grok_install` field is set. See
[`docs/grok-compat.md`](docs/grok-compat.md).

---

## Contributing

Read [`CONTRIBUTING.md`](CONTRIBUTING.md). The short version:

- Open an issue before writing code, especially for spec changes.
- The canonical source is this repository. Mirrors are fine; forks that
  re-brand the standard are not.
- Every PR that touches the spec updates the schema, the prose, the
  compatibility matrix, and at least one example.

---

## Governance, security, changelog

- [`GOVERNANCE.md`](GOVERNANCE.md) — how decisions are made.
- [`SECURITY.md`](SECURITY.md) — how to report vulnerabilities.
- [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md) — participation rules.
- [`CHANGELOG.md`](CHANGELOG.md) — release history (Keep a Changelog
  format; specification follows strict SemVer per
  [`spec/versioning.md`](spec/versioning.md)).

---

## License

Apache License 2.0. See [`LICENSE`](LICENSE). The specification itself
(everything under `spec/`) is also dedicated to the public under the
same license — you may implement it without permission.

---

## Entry points

Two specification tracks ship in this repository. Pick the one that
fits your tooling:

| Track               | Location              | Schema draft   | Start here                                              |
|---------------------|-----------------------|----------------|----------------------------------------------------------|
| **v1.0** (recommended)  | [`spec/v1.0/`](spec/v1.0/)       | JSON Schema draft-07 | [`spec/v1.0/spec.md`](spec/v1.0/spec.md) — RFC-style prose |
| v1.0.0 (reference)  | [`spec/v1.0.0/`](spec/v1.0.0/)   | JSON Schema draft 2020-12 | [`spec/v1.0.0/spec.md`](spec/v1.0.0/spec.md)          |

Both tracks describe the same idea; v1.0 uses the widely-supported
draft-07 and adds RFC-style conformance language. A follow-up release
will reconcile them.

### For creators

- Copy [`universal/universal-spawn.yaml`](universal/universal-spawn.yaml)
  (fully annotated reference) to your repo root and fill in the
  fields.
- [`universal/cheatsheet.md`](universal/cheatsheet.md) — one page.
- [`universal/aliases.md`](universal/aliases.md) — accepted filenames.
- [`spec/v1.0/examples/`](spec/v1.0/examples/) — twelve worked
  manifests covering every project shape.

### For implementers

- [`spec/v1.0/spec.md`](spec/v1.0/spec.md) — normative prose.
- [`spec/v1.0/universal-spawn.schema.json`](spec/v1.0/universal-spawn.schema.json) — normative JSON Schema (draft-07).
- [`spec/v1.0/migration/`](spec/v1.0/migration/) — grok-install and
  vercel.json walkthroughs.
- [`docs/safety-model.md`](docs/safety-model.md) — threat analysis
  and enforcement obligations.
