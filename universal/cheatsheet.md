# universal-spawn cheatsheet

One page for the creator who has forgotten everything except that
their repo needs a manifest.

## Minimum viable manifest

```yaml
version: "1.0"
name: My Thing
type: cli-tool
description: >
  One paragraph. What it does, for whom, what's distinct about it.
deployment:
  targets: [npm]
```

Copy, edit four fields, commit. You are done.

## The four required fields

| Field         | Value                                                      |
|---------------|-------------------------------------------------------------|
| `version`     | Literal `"1.0"`.                                            |
| `name`        | Display name. Alphanumerics, space, dot, dash, underscore.  |
| `type`        | One of the enum; see below.                                 |
| `description` | 10–500 characters.                                          |

Plus at least one of `platforms` or `deployment`.

## Type enum (pick one)

```text
ai-agent   ai-skill       ai-model     web-app          api-service
cli-tool   library        dataset      notebook         creative-tool
design-template           game-mod     game-world       hardware-device
firmware   bot            extension    plugin           site
container  workflow
```

## Safety envelope

```yaml
safety:
  min_permissions: [network:outbound:api.example.com, fs:read]
  rate_limit_qps: 5
  cost_limit_usd_daily: 20
  safe_for_auto_spawn: false
  data_residency: [us, eu]
```

## Env vars (declare names, never values)

```yaml
env_vars_required:
  - name: MY_API_KEY
    description: API key used for outbound calls.
    secret: true
```

Name pattern: `^[A-Z][A-Z0-9_]*$`. First char A–Z, rest A–Z/0–9/`_`.

## Target one platform

```yaml
platforms:
  claude:
    skill_type: subagent
    model: claude-opus-4-7
    surface: [claude-api]
```

Each platform's allowed fields live under
[`../platforms/<id>/schema.extension.json`](../platforms/).

## Target many platforms

```yaml
platforms:
  claude:  { skill_type: subagent, model: claude-opus-4-7, surface: [claude-api] }
  openai:  { model: gpt-5, tools: [{ name: ask, function_ref: tools/ask.json, strict: true }] }
  vercel:  { framework: nextjs, build_command: "pnpm build", output: ".next" }
```

## Validate

```bash
# one-shot, online
npx ajv-cli validate --all-errors --spec=draft7 -c ajv-formats \
  -s https://universal-spawn.dev/spec/v1.0/universal-spawn.schema.json \
  -d universal-spawn.yaml

# local schema
npx ajv-cli validate --all-errors --spec=draft7 -c ajv-formats \
  -s spec/v1.0/universal-spawn.schema.json \
  -d universal-spawn.yaml
```

Expected output: `universal-spawn.yaml valid`.

## Common validation errors

| Error                                               | Fix                                                 |
|-----------------------------------------------------|------------------------------------------------------|
| `additional property "X" not allowed`               | Typo in a field name, or using a v1.1 field on v1.0. |
| `"version" must be one of ["1.0"]`                  | Set `version: "1.0"` literally.                      |
| `"name" does not match pattern ...`                 | Remove emoji / leading or trailing whitespace.       |
| `"description" must be at least 10 characters`      | Write one sentence. Placeholder descriptions fail.   |
| `"type" must be one of [...]`                       | Pick a value from the enum.                          |
| `must have at least one of "platforms", "deployment"` | Add one of them.                                   |
| `"env_vars_required[0].name" does not match pattern` | Use SCREAMING_SNAKE_CASE.                           |

## Checklist before you commit

- [ ] `version: "1.0"`.
- [ ] `name`, `description`, `type` filled in.
- [ ] At least one of `platforms` or `deployment`.
- [ ] `safety.min_permissions` lists only what you need.
- [ ] Every `env_vars_required` entry has a `description`.
- [ ] `metadata.license` is an SPDX id.
- [ ] Validator exits zero.
- [ ] No emoji in `name` or `description`.

## More

- Full spec: [`../spec/v1.0/spec.md`](../spec/v1.0/spec.md).
- Full annotated reference: [`universal-spawn.yaml`](./universal-spawn.yaml).
- Discovery rules: [`aliases.md`](./aliases.md).
- Twelve worked examples: [`../spec/v1.0/examples/`](../spec/v1.0/examples/).
