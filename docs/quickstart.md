# Quickstart

Five minutes from empty repo to a validating spawn manifest.

## 1. Put a manifest at your repo root

Copy [`../examples/minimal.spawn.yaml`](../examples/minimal.spawn.yaml)
to `spawn.yaml` at the root of your project and fill in the fields:

```yaml
spawn_version: "1.0.0"
id: com.yourhandle.your-project         # reverse-DNS, lowercase
name: Your Project
kind: cli-tool                          # or ai-agent, web-app, ...
description: >
  One paragraph describing what the project does. First sentence must
  stand alone as a summary — indexers use it as the snippet.
license: Apache-2.0
author:
  name: Your Name
  handle: yourhandle
source:
  type: git
  url: https://github.com/yourhandle/your-project
```

That's the minimum. The file already validates.

## 2. Declare how to spawn it

Tell platforms how to actually invoke your creation:

```yaml
entrypoints:
  - id: cli
    kind: cli          # or http, tool-call, scene, ui-panel, ...
    ref: bin/your-tool
```

`ref` is always a path, route, image tag, or URL — **never a shell
command**. The platform wires up the invocation.

## 3. Declare your safety envelope

Tell platforms the smallest permission set and cost ceiling your
creation needs:

```yaml
env_vars_required:
  - name: API_KEY
    description: Key used for outbound API calls.
    secret: true

min_permissions:
  - network:outbound:api.example.com
  - fs:read

rate_limit_qps: 5
cost_limit_usd_daily: 10
safe_for_auto_spawn: false
```

Safety-through-declaration: the manifest is the contract, and the
platform enforces it. Never put secret values in the manifest — only
names.

## 4. Add platform extensions (optional)

If you want Claude-specific or Vercel-specific perks, add a
`platforms` block:

```yaml
platforms:
  claude:
    skill_type: subagent
    model: claude-opus-4-7
    surface: [claude-api, claude-code]
  vercel:
    framework: nextjs
    build_command: "pnpm build"
```

Each platform's extension schema lives under `platforms/<id>/`. Unknown
keys fail validation; this is deliberate.

## 5. Validate

Pick a validator. Both produce the same verdict.

**Node**:

```bash
npm i -g ajv-cli ajv-formats
ajv validate \
  -s https://universal-spawn.org/spec/v1.0.0/manifest.schema.json \
  -d spawn.yaml --spec=draft2020 -c ajv-formats
```

**Python**:

```bash
pip install jsonschema pyyaml
python - <<'PY'
import json, yaml, jsonschema
schema = json.load(open("spec/v1.0.0/manifest.schema.json"))
doc    = yaml.safe_load(open("spawn.yaml"))
jsonschema.validate(doc, schema)
print("ok")
PY
```

See [`validation.md`](./validation.md) for wiring validation into CI.

## 6. Push and publish

Commit `spawn.yaml` to your repo. Conformant consumers (a Claude spawn
host, a Vercel connect app, a search index) will discover it
automatically the next time they crawl or you connect the repo.

## Next steps

- [Field reference](./field-reference.md) — what each field means.
- [Safety model](./safety-model.md) — what the platform actually
  enforces.
- [grok-install compatibility](./grok-compat.md) — ship the same
  creation on Grok with zero effort.
- [Examples](../examples) — eight complete manifests for different
  kinds of creation.
