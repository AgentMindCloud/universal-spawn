# AWS — universal-spawn platform extension

AWS exposes a spectrum of application hosting surfaces. The extension models the four a universal-spawn manifest is most likely to target: Lambda (serverless functions), ECS (containers on Fargate), App Runner (managed container web service), and Amplify Hosting (static + SSR). One manifest MAY target one runtime at a time by picking `runtime`.

## What this platform cares about

The runtime (`lambda`, `ecs`, `app_runner`, `amplify`), the region, the IaC provider (`sam`, `cdk`, `terraform`, `cloudformation`, `manual`), and the runtime-specific block.

## What platform-specific extras unlock

Each runtime has its own first-class block: `lambda.functions`, `ecs.services`, `app_runner.service`, `amplify.app`. Mixing two runtimes in the same manifest is out of scope — use two sibling manifests.

## Supported runtime targets

| Runtime      | AWS service                   | Typical shape       |
|--------------|--------------------------------|---------------------|
| `lambda`     | AWS Lambda + API Gateway       | Serverless functions|
| `ecs`        | ECS on Fargate                 | Long-running containers|
| `app_runner` | AWS App Runner                 | Single-container web service|
| `amplify`    | AWS Amplify Hosting            | Static + SSR web app|


## Compatibility table

| Manifest field | AWS behavior |
|---|---|
| `version` | Required. |
| `name, description` | Stack / app card. |
| `type` | `web-app`, `api-service`, `container`, `workflow`, `bot`, `site`. |
| `env_vars_required` | AWS Secrets Manager / SSM Parameter Store. |
| `deployment.targets` | Must include `aws`. |
| `platforms.aws` | Strict. |

### `platforms.aws` fields

| Field | Purpose |
|---|---|
| `platforms.aws.runtime` | `lambda`, `ecs`, `app_runner`, `amplify`. |
| `platforms.aws.region` | AWS region. |
| `platforms.aws.iac` | IaC provider (`sam`, `cdk`, `terraform`, `cloudformation`, `manual`). |
| `platforms.aws.lambda` | Lambda function(s) with memory, timeout, API Gateway routes. |
| `platforms.aws.ecs` | ECS services with task CPU/memory and Fargate launch. |
| `platforms.aws.app_runner` | App Runner service (container + port). |
| `platforms.aws.amplify` | Amplify Hosting app + framework + SSR. |

See [`compatibility.md`](./compatibility.md) for the side-by-side diff
against `samconfig.toml / cdk.json`, [`deploy-button.md`](./deploy-button.md)
for the canonical Deploy-button recipe, and [`perks.md`](./perks.md) for
what a conformant AWS consumer SHOULD offer manifests that
declare `platforms.aws`.
