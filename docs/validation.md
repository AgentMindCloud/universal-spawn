# Validation

How to know a manifest is correct before a platform tells you it
isn't.

## What "valid" means

A manifest is **valid** if and only if:

1. It parses as YAML, JSON, or TOML into a JSON data model.
2. The data model is accepted by
   [`../spec/v1.0.0/manifest.schema.json`](../spec/v1.0.0/manifest.schema.json).
3. For every key under `platforms`, the corresponding extension schema
   (`../platforms/<id>/schema.extension.json`) accepts the value.

The spec does not require any other checks to call the manifest valid
— but a few additional checks are good hygiene:

- Every `ref` inside an entrypoint resolves to a file in the
  repository (or a reachable URL).
- Every `env_vars_required[*].name` with `required: true` exists in
  the target environment's secret store at spawn time.
- `id` matches a reverse-DNS prefix you can prove you control.

The last three are **runtime** checks, not validity checks — they
depend on context the manifest doesn't carry.

## Node

```bash
npm i -D ajv ajv-cli ajv-formats js-yaml
npx ajv validate \
  -s spec/v1.0.0/manifest.schema.json \
  -d spawn.yaml \
  --spec=draft2020 \
  -c ajv-formats
```

Ajv CLI can read YAML directly; `js-yaml` is used by some ecosystems
to pre-convert to JSON.

## Python

```bash
pip install jsonschema pyyaml referencing
python - <<'PY'
import json, yaml, jsonschema
schema = json.load(open("spec/v1.0.0/manifest.schema.json"))
doc    = yaml.safe_load(open("spawn.yaml"))
jsonschema.Draft202012Validator(schema).validate(doc)
print("ok")
PY
```

To also validate platform extensions:

```python
for platform_id, ext_value in (doc.get("platforms") or {}).items():
    ext_schema = json.load(open(f"platforms/{platform_id}/schema.extension.json"))
    jsonschema.Draft202012Validator(ext_schema).validate(ext_value)
```

## Go

Use `github.com/santhosh-tekuri/jsonschema/v5`:

```go
c := jsonschema.NewCompiler()
c.Draft = jsonschema.Draft2020
schema, err := c.Compile("spec/v1.0.0/manifest.schema.json")
// then schema.Validate(doc)
```

## Rust

Use `jsonschema` (from `jsonschema` crate) with
`Draft::Draft202012`.

## CI recipes

### GitHub Actions — minimal

```yaml
name: validate-manifest
on: [push, pull_request]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: "20" }
      - run: npm i -g ajv-cli ajv-formats
      - run: |
          ajv validate \
            -s spec/v1.0.0/manifest.schema.json \
            -d spawn.yaml \
            --spec=draft2020 -c ajv-formats
```

### Pre-commit (local)

```yaml
# .pre-commit-config.yaml
repos:
  - repo: local
    hooks:
      - id: validate-spawn
        name: validate universal-spawn manifest
        entry: ./scripts/validate-spawn.sh
        language: script
        files: ^spawn\.(yaml|yml|json|toml)$
```

## Common validation errors

| Symptom                                  | Cause                                              |
|------------------------------------------|-----------------------------------------------------|
| `additional property "X" not allowed`    | Unknown field. Spec is strict by design; check the field name and case. |
| `"id" does not match pattern`            | The `id` must be reverse-DNS, lowercase, dot-separated. |
| `"description" is too short`             | Descriptions must be ≥ 20 chars.                   |
| `"spawn_version" does not match pattern` | Use strict `MAJOR.MINOR.PATCH`.                    |
| `"env_vars_required[N].name" does not match pattern` | ENV names are SCREAMING_SNAKE_CASE.  |
| `required property "source" missing`     | Every manifest needs a `source`.                   |
| Unknown extension key under `platforms.X`| The platform extension schema is strict; unknown keys fail. |

If validation passes but a platform still refuses to spawn, the
problem is platform-specific (a missing secret, a declined
permission). Check the platform's `compatibility.md`.
