"""AWS — Lambda + ECS + App Runner + Amplify."""
from scripts.ai_specs._common import (
    STANDARD_PERKS, enum, str_prop, bool_prop, schema_object,
)

SPEC = {
    "id": "aws",
    "title": "AWS",
    "native_config_name": "samconfig.toml / cdk.json",
    "native_config_lang": "toml",

    "lede": (
        "AWS exposes a spectrum of application hosting surfaces. The "
        "extension models the four a universal-spawn manifest is most "
        "likely to target: Lambda (serverless functions), ECS "
        "(containers on Fargate), App Runner (managed container web "
        "service), and Amplify Hosting (static + SSR). One manifest "
        "MAY target one runtime at a time by picking `runtime`."
    ),
    "cares": (
        "The runtime (`lambda`, `ecs`, `app_runner`, `amplify`), the "
        "region, the IaC provider (`sam`, `cdk`, `terraform`, "
        "`cloudformation`, `manual`), and the runtime-specific block."
    ),
    "extras": (
        "Each runtime has its own first-class block: `lambda.functions`, "
        "`ecs.services`, `app_runner.service`, `amplify.app`. Mixing "
        "two runtimes in the same manifest is out of scope — use two "
        "sibling manifests."
    ),
    "runtimes": (
        "| Runtime      | AWS service                   | Typical shape       |\n"
        "|--------------|--------------------------------|---------------------|\n"
        "| `lambda`     | AWS Lambda + API Gateway       | Serverless functions|\n"
        "| `ecs`        | ECS on Fargate                 | Long-running containers|\n"
        "| `app_runner` | AWS App Runner                 | Single-container web service|\n"
        "| `amplify`    | AWS Amplify Hosting            | Static + SSR web app|\n"
    ),

    "compat_table": [
        ("version", "Required."),
        ("name, description", "Stack / app card."),
        ("type", "`web-app`, `api-service`, `container`, `workflow`, `bot`, `site`."),
        ("env_vars_required", "AWS Secrets Manager / SSM Parameter Store."),
        ("deployment.targets", "Must include `aws`."),
        ("platforms.aws", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("metadata.id", "Stack name suggestion."),
        ("name, description", "Stack card."),
        ("type", "See above."),
        ("safety.min_permissions", "Translated to the smallest IAM role policy."),
        ("safety.cost_limit_usd_daily", "Advisory; mapped to Budgets alert."),
        ("env_vars_required", "Secrets Manager / SSM."),
        ("platforms.aws.runtime", "`lambda`, `ecs`, `app_runner`, `amplify`."),
        ("platforms.aws.region", "AWS region."),
        ("platforms.aws.iac", "IaC provider."),
        ("platforms.aws.lambda", "Lambda function block."),
        ("platforms.aws.ecs", "ECS block."),
        ("platforms.aws.app_runner", "App Runner service block."),
        ("platforms.aws.amplify", "Amplify app block."),
    ],
    "platform_fields": {
        "runtime": "`lambda`, `ecs`, `app_runner`, `amplify`.",
        "region": "AWS region.",
        "iac": "IaC provider (`sam`, `cdk`, `terraform`, `cloudformation`, `manual`).",
        "lambda": "Lambda function(s) with memory, timeout, API Gateway routes.",
        "ecs": "ECS services with task CPU/memory and Fargate launch.",
        "app_runner": "App Runner service (container + port).",
        "amplify": "Amplify Hosting app + framework + SSR.",
    },

    "schema_body": schema_object(
        required=["runtime", "region"],
        properties={
            "runtime": enum(["lambda", "ecs", "app_runner", "amplify"]),
            "region": str_prop(pattern=r"^[a-z]{2}-[a-z]+-[0-9]+$"),
            "iac": enum(["sam", "cdk", "terraform", "cloudformation", "manual"]),
            "lambda": schema_object(
                properties={
                    "runtime_id": enum([
                        "nodejs20.x", "nodejs22.x",
                        "python3.11", "python3.12", "python3.13",
                        "java21", "provided.al2023", "container",
                    ]),
                    "functions": {
                        "type": "array",
                        "items": schema_object(
                            required=["name"],
                            properties={
                                "name": str_prop(pattern=r"^[A-Za-z][A-Za-z0-9-]{0,63}$"),
                                "handler": str_prop(),
                                "memory_mb": {"type": "integer", "minimum": 128, "maximum": 10240},
                                "timeout_seconds": {"type": "integer", "minimum": 1, "maximum": 900},
                                "route": str_prop(desc="API Gateway route."),
                            },
                        ),
                    },
                },
            ),
            "ecs": schema_object(
                properties={
                    "cluster": str_prop(),
                    "launch_type": enum(["FARGATE", "FARGATE_SPOT"]),
                    "services": {
                        "type": "array",
                        "items": schema_object(
                            required=["name", "image"],
                            properties={
                                "name": str_prop(pattern=r"^[A-Za-z][A-Za-z0-9-]{0,63}$"),
                                "image": str_prop(),
                                "cpu": {"type": "integer", "minimum": 256, "maximum": 16384},
                                "memory_mb": {"type": "integer", "minimum": 512, "maximum": 122880},
                                "desired_count": {"type": "integer", "minimum": 0, "maximum": 500},
                                "port": {"type": "integer", "minimum": 1, "maximum": 65535},
                            },
                        ),
                    },
                },
            ),
            "app_runner": schema_object(
                properties={
                    "service": schema_object(
                        required=["name", "image"],
                        properties={
                            "name": str_prop(),
                            "image": str_prop(),
                            "port": {"type": "integer", "minimum": 1, "maximum": 65535},
                            "cpu": enum(["0.25 vCPU", "0.5 vCPU", "1 vCPU", "2 vCPU", "4 vCPU"]),
                            "memory": enum(["0.5 GB", "1 GB", "2 GB", "3 GB", "4 GB", "6 GB", "8 GB", "10 GB", "12 GB"]),
                            "auto_scaling": schema_object(
                                properties={
                                    "max_concurrency": {"type": "integer", "minimum": 1, "maximum": 200},
                                    "min_size": {"type": "integer", "minimum": 1, "maximum": 25},
                                    "max_size": {"type": "integer", "minimum": 1, "maximum": 25},
                                },
                            ),
                        },
                    ),
                },
            ),
            "amplify": schema_object(
                properties={
                    "app": schema_object(
                        properties={
                            "name": str_prop(),
                            "framework": enum(["next", "remix", "astro", "vite-react", "nuxt", "svelte-kit", "gatsby", "static"]),
                            "build_spec": str_prop(desc="Path to amplify.yml."),
                            "ssr": bool_prop(False),
                            "custom_domain": str_prop(),
                        },
                    ),
                },
            ),
        },
    ),

    "template_yaml": """
version: \"1.0\"
name: AWS Template
type: api-service
description: Template for an AWS-targeted universal-spawn manifest.

platforms:
  aws:
    runtime: lambda
    region: us-east-1
    iac: sam
    lambda:
      runtime_id: nodejs22.x
      functions:
        - { name: Hello, handler: dist/handler.handler, memory_mb: 512, timeout_seconds: 10, route: \"GET /hello\" }

safety:
  min_permissions: [network:inbound, network:outbound]

env_vars_required:
  - name: API_SECRET
    description: API secret.
    secret: true

deployment:
  targets: [aws]

metadata:
  license: Apache-2.0
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/aws-template }
""",

    "native_config": """
version = 0.1

[default.deploy.parameters]
stack_name = "hello"
region = "us-east-1"
resolve_s3 = true
capabilities = "CAPABILITY_IAM"
""",

    "universal_excerpt": """
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
          route: \"GET /hello\"
""",

    "compatibility_extras": (
        "## Why only one runtime per manifest\n\n"
        "`platforms.aws.runtime` picks exactly one surface. Mixing "
        "Lambda + ECS in the same manifest would conflate two very "
        "different deployment lifecycles. Ship two sibling manifests "
        "(e.g. `api.universal-spawn.yaml` + `jobs.universal-spawn.yaml`) "
        "when a single creation needs both."
    ),

    "deploy_button": {
        "markdown": (
            "[![Launch on AWS](https://s3.amazonaws.com/cloudformation-examples/cloudformation-launch-stack.png)]"
            "(https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?stackName=your-stack&templateURL=https%3A%2F%2Fs3.amazonaws.com%2Fyour-bucket%2Ftemplate.yaml)"
        ),
        "html": (
            '<a href="https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/new?stackName=your-stack&templateURL=https%3A%2F%2Fs3.amazonaws.com%2Fyour-bucket%2Ftemplate.yaml">\n'
            '  <img src="https://s3.amazonaws.com/cloudformation-examples/cloudformation-launch-stack.png" alt="Launch Stack" />\n'
            '</a>'
        ),
        "params_doc": (
            "The CloudFormation launch URL accepts:\n\n"
            "- `region` — AWS region for the stack.\n"
            "- `stackName` — default stack name.\n"
            "- `templateURL` — URL-encoded URL of the template file "
            "(usually an S3 URL).\n\n"
            "Generators SHOULD fill `region` from `platforms.aws.region` "
            "and upload the generated template before rendering the button."
        ),
    },

    "perks": STANDARD_PERKS + [
        "**IAM minimisation** — `safety.min_permissions` translates to "
        "an IAM role with the smallest IAM policy envelope.",
        "**Region auto-pick** — `safety.data_residency` narrows region "
        "choices to the allowed set.",
    ],

    "examples": {
        "static-site": """
version: \"1.0\"
name: AWS Amplify Static Site
type: site
summary: Minimal static site hosted on AWS Amplify Hosting.
description: Astro static site; no SSR; CloudFront distribution.

platforms:
  aws:
    runtime: amplify
    region: us-east-1
    iac: manual
    amplify:
      app:
        name: docs-site
        framework: astro
        build_spec: amplify.yml
        ssr: false

safety:
  min_permissions: [network:inbound]
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [aws]

metadata:
  license: Apache-2.0
  author: { name: Docs Team, handle: docs-team }
  source: { type: git, url: https://github.com/docs-team/aws-amplify-docs }
  id: com.docs-team.aws-amplify-docs
""",
        "serverless-api": """
version: \"1.0\"
name: AWS Lambda API
type: api-service
summary: API Gateway + Lambda + DynamoDB via SAM.
description: >
  Three Lambda functions behind API Gateway HTTP routes. SAM for IaC.
  Env vars stored in SSM Parameter Store.

platforms:
  aws:
    runtime: lambda
    region: us-east-1
    iac: sam
    lambda:
      runtime_id: nodejs22.x
      functions:
        - { name: GetOrder,    handler: dist/get-order.handler,    memory_mb: 512, timeout_seconds: 10, route: \"GET /orders/{id}\" }
        - { name: CreateOrder, handler: dist/create-order.handler, memory_mb: 512, timeout_seconds: 10, route: \"POST /orders\" }
        - { name: CancelOrder, handler: dist/cancel-order.handler, memory_mb: 512, timeout_seconds: 10, route: \"POST /orders/{id}/cancel\" }

safety:
  min_permissions: [network:inbound, network:outbound]
  rate_limit_qps: 100
  cost_limit_usd_daily: 25

env_vars_required:
  - name: DDB_TABLE_NAME
    description: DynamoDB table name.
  - name: API_SECRET
    description: API signing secret stored in SSM.
    secret: true

deployment:
  targets: [aws]

metadata:
  license: Apache-2.0
  author: { name: Orders Co., handle: orders-co }
  source: { type: git, url: https://github.com/orders-co/aws-lambda-api }
  id: com.orders-co.aws-lambda-api
""",
        "full-stack-app": """
version: \"1.0\"
name: AWS ECS Full Stack
type: web-app
summary: Full-stack ECS deployment with Fargate tasks and CDK IaC.
description: >
  Two ECS services on Fargate (web + worker) in us-west-2. CDK for IaC.
  Uses an RDS Postgres cluster provisioned separately.

platforms:
  aws:
    runtime: ecs
    region: us-west-2
    iac: cdk
    ecs:
      cluster: app-cluster
      launch_type: FARGATE
      services:
        - { name: Web,    image: \"123456789012.dkr.ecr.us-west-2.amazonaws.com/app-web:latest\",    cpu: 512,  memory_mb: 1024, desired_count: 2, port: 3000 }
        - { name: Worker, image: \"123456789012.dkr.ecr.us-west-2.amazonaws.com/app-worker:latest\", cpu: 512,  memory_mb: 1024, desired_count: 1, port: 9000 }

safety:
  min_permissions: [network:inbound, network:outbound]
  cost_limit_usd_daily: 60
  safe_for_auto_spawn: false
  data_residency: [us]

env_vars_required:
  - name: DATABASE_URL
    description: RDS Postgres connection string (stored in Secrets Manager).
    secret: true
  - name: SESSION_SECRET
    description: Session signing secret.
    secret: true

deployment:
  targets: [aws]

metadata:
  license: MIT
  author: { name: Stack Co., handle: stack-co, org: Stack }
  source: { type: git, url: https://github.com/stack-co/aws-ecs-full-stack }
  id: com.stack-co.aws-ecs-full-stack
""",
    },
}
