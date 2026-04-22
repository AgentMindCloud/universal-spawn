# AWS compatibility — field-by-field

AWS already has a native config format
(`samconfig.toml / cdk.json`). universal-spawn does not replace it; the two
coexist. A AWS consumer reads both:

- `samconfig.toml / cdk.json` for provider-specific knobs the universal-spawn
  extension does not (yet) model.
- `universal-spawn.yaml` (with `platforms.aws`) for the
  cross-platform manifest.

The two files **MUST NOT** disagree on fields that appear in both; a
consumer that detects a conflict MUST warn and prefer `universal-spawn.yaml`.

## Side-by-side

### `samconfig.toml / cdk.json` (provider-native)

```toml
version = 0.1

[default.deploy.parameters]
stack_name = "hello"
region = "us-east-1"
resolve_s3 = true
capabilities = "CAPABILITY_IAM"
```

### `universal-spawn.yaml` (platforms.aws block)

```yaml
platforms:
  aws:
    runtime: lambda
    region: us-east-1
    iac: sam
    lambda:
      runtime_id: nodejs22.x
      functions:
        - name: Hello
          handler: dist/handler.handler
          memory_mb: 512
          timeout_seconds: 10
          route: "GET /hello"
```

## Field-by-field

| universal-spawn v1.0 field | AWS behavior |
|---|---|
| `version` | Required. |
| `metadata.id` | Stack name suggestion. |
| `name, description` | Stack card. |
| `type` | See above. |
| `safety.min_permissions` | Translated to the smallest IAM role policy. |
| `safety.cost_limit_usd_daily` | Advisory; mapped to Budgets alert. |
| `env_vars_required` | Secrets Manager / SSM. |
| `platforms.aws.runtime` | `lambda`, `ecs`, `app_runner`, `amplify`. |
| `platforms.aws.region` | AWS region. |
| `platforms.aws.iac` | IaC provider. |
| `platforms.aws.lambda` | Lambda function block. |
| `platforms.aws.ecs` | ECS block. |
| `platforms.aws.app_runner` | App Runner service block. |
| `platforms.aws.amplify` | Amplify app block. |

## Why only one runtime per manifest

`platforms.aws.runtime` picks exactly one surface. Mixing Lambda + ECS in the same manifest would conflate two very different deployment lifecycles. Ship two sibling manifests (e.g. `api.universal-spawn.yaml` + `jobs.universal-spawn.yaml`) when a single creation needs both.
