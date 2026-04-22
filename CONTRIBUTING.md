# Contributing to universal-spawn

Thank you for considering a contribution. universal-spawn is an open
standard; the quality of the ecosystem depends on the care taken with
every proposed change.

**Canonical source**:
[`github.com/AgentMindCloud/universal-spawn`](https://github.com/AgentMindCloud/universal-spawn).
All spec changes land here first. Mirrors are welcome; forks that
re-brand the standard are not.

---

## Ground rules

1. **Open an issue first.** For anything more than a typo fix. This
   avoids duplicate work and lets the editor sequence changes.
2. **One concern per PR.** Spec edit, schema edit, new platform, new
   example — separate PRs.
3. **Breaking changes are rare.** The bar for a major version bump is
   "a clear design mistake that cannot be fixed additively." See
   [`spec/versioning.md`](spec/versioning.md).
4. **The manifest never executes code.** Any proposal that adds an
   inline-script, shell-command, eval-string, or similar field will be
   closed. Declarative references only.
5. **Every PR that touches the spec must update:**
   - the prose (`spec/vX.Y.Z/spec.md`)
   - the schema (`spec/vX.Y.Z/manifest.schema.json`)
   - the field reference (`spec/vX.Y.Z/fields.md`)
   - the compatibility matrix (`spec/vX.Y.Z/compatibility-matrix.md`)
   - at least one example in `examples/` demonstrating the change
   - `CHANGELOG.md`

## Local setup

No build is required to edit specs or examples. To validate:

```bash
# Node-based validator
npm install -g ajv-cli ajv-formats
ajv validate \
  -s spec/v1.0.0/manifest.schema.json \
  -d examples/minimal.spawn.yaml \
  --spec=draft2020 \
  -c ajv-formats
```

Python alternative:

```bash
pip install jsonschema pyyaml
python - <<'PY'
import json, yaml, jsonschema
schema = json.load(open("spec/v1.0.0/manifest.schema.json"))
doc    = yaml.safe_load(open("examples/minimal.spawn.yaml"))
jsonschema.validate(doc, schema)
print("ok")
PY
```

CI runs both validators against every example and every platform sample
before merge.

## Adding an example

1. Decide what the example demonstrates — minimum, full coverage,
   specific kind, specific platform.
2. Write a manifest under `examples/<short-name>.spawn.yaml` or
   `platforms/<platform>/examples/<short-name>.<platform>-spawn.yaml`.
3. Keep identifiers in the `com.example.*` namespace unless the example
   is owned by a real project.
4. Run the validator above.
5. Cross-link the example from the relevant README.

## Adding a platform

Adding a platform is how the standard grows horizontally.

1. **Open a proposal issue** using
   `.github/ISSUE_TEMPLATE/spec_proposal.md`. Include:
   - the platform's id (short, lowercase, one word preferred)
   - which `kind`s it accepts
   - which entrypoint kinds it supports
   - the minimum extension schema you need
2. Create the folder:
   ```text
   platforms/<id>/
     README.md
     <id>-spawn.yaml          ← template
     schema.extension.json    ← strict JSON Schema, additionalProperties: false
     compatibility.md         ← which core fields you honor, which you ignore
     examples/
       <example-1>.<id>-spawn.yaml
       <example-2>.<id>-spawn.yaml
   ```
3. Update [`spec/v1.0.0/compatibility-matrix.md`](spec/v1.0.0/compatibility-matrix.md).
4. Update the platforms table in the root [`README.md`](README.md).
5. Provide two complete examples that validate against both the core
   schema and your extension schema.

A platform folder merges if:

- Two maintainers approve.
- All examples validate.
- The platform's extension schema is strict (`additionalProperties:
  false` at every level).
- The platform's `compatibility.md` is filled out completely.

## Spec change process

Summarised here; full detail in
[`spec/versioning.md`](spec/versioning.md).

1. Open a spec-proposal issue.
2. Discuss in public on the issue. The editor may request a prototype in
   a branch.
3. Two maintainer approvals are required.
4. For additive changes, bump minor. For breaking changes, create a new
   major version directory `spec/vX.0.0/` and leave the old one
   untouched.
5. Tag `spec-vX.Y.Z` on merge.

## Style

- Prose: direct, professional, builder-to-builder. No marketing fluff.
  No emoji. Plain words beat clever ones.
- Diagrams: Residual Frequencies · Parchment palette. See
  [`design/residual-frequencies.md`](design/residual-frequencies.md).
- YAML: two-space indent, no tabs, trailing newline. Order fields in
  the same order the schema lists them.
- JSON Schema: always `"$schema"`, always `"additionalProperties":
  false`, always write `"description"` for public fields.

## Code of conduct

Participation is governed by [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md).
Reports go to `conduct@agentmindcloud.org`.

## Licensing

By contributing, you agree that your contribution is licensed under
Apache License 2.0 (see [`LICENSE`](LICENSE)). No CLA is required. By
opening a PR you assert you have the right to license the contributed
material.
