"""Mastra — agent + workflow runtime (TypeScript)."""
from scripts.ai_specs._common import (
    STANDARD_PERKS, enum, str_prop, bool_prop, schema_object,
)

SPEC = {
    "id": "mastra",
    "title": "Mastra",
    "location": "multi-agent",

    "lede": (
        "Mastra is a TypeScript framework combining an agent runtime, "
        "a workflow engine, and first-class integrations with the "
        "Vercel AI SDK. A manifest declares the agents, the workflows, "
        "and the memory backend. Typed state, streaming by default."
    ),
    "cares": (
        "The agents array (each with model + tools + memory), the "
        "workflows array (each a typed state machine), and the "
        "memory backend (`libsql`, `pg`, `upstash-redis`)."
    ),
    "extras": (
        "`telemetry.otlp_endpoint_env` sends OpenTelemetry traces to "
        "the named endpoint. `deploy.runtime` picks `nextjs`, `vercel-"
        "edge`, `cloudflare`, or `node`."
    ),
    "compat_table": [
        ("version", "Required."),
        ("type", "`ai-agent`, `workflow`."),
        ("safety.*", "Informational."),
        ("env_vars_required", "Runtime host secrets."),
        ("platforms.mastra", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("metadata.id", "Stable key."),
        ("name, description", "Mastra card."),
        ("type", "`ai-agent`, `workflow`."),
        ("safety.*", "Informational."),
        ("env_vars_required", "Secret store."),
        ("platforms.mastra.agents", "Agents array."),
        ("platforms.mastra.workflows", "Workflows array."),
        ("platforms.mastra.memory", "Memory backend."),
        ("platforms.mastra.telemetry", "OTLP telemetry."),
        ("platforms.mastra.deploy", "Deployment runtime."),
    ],
    "platform_fields": {
        "agents": "Agents array (name, model, tools, memory).",
        "workflows": "Workflows array (name, entry step).",
        "memory": "Memory backend.",
        "telemetry": "OpenTelemetry endpoint.",
        "deploy": "Deployment runtime (`nextjs`, `vercel-edge`, `cloudflare`, `node`).",
    },
    "schema_body": schema_object(
        properties={
            "agents": {
                "type": "array",
                "items": schema_object(
                    required=["name", "model"],
                    properties={
                        "name": str_prop(pattern=r"^[a-z][a-zA-Z0-9_-]{0,63}$"),
                        "model": str_prop(desc="Vercel-AI-SDK-style model id, e.g. anthropic/claude-sonnet-4-6."),
                        "instructions_file": str_prop(),
                        "tools": {"type": "array", "items": str_prop()},
                        "memory": bool_prop(False),
                    },
                ),
            },
            "workflows": {
                "type": "array",
                "items": schema_object(
                    required=["name", "entry"],
                    properties={
                        "name": str_prop(pattern=r"^[a-z][a-zA-Z0-9_-]{0,63}$"),
                        "entry": str_prop(desc="Entry step id."),
                        "schema_ref": str_prop(desc="Relative path to the workflow state zod schema."),
                    },
                ),
            },
            "memory": schema_object(
                properties={
                    "store": enum(["libsql", "pg", "upstash-redis"]),
                    "url_env": str_prop(pattern=r"^[A-Z][A-Z0-9_]*$"),
                },
            ),
            "telemetry": schema_object(
                properties={
                    "otlp_endpoint_env": str_prop(pattern=r"^[A-Z][A-Z0-9_]*$"),
                },
            ),
            "deploy": schema_object(
                properties={
                    "runtime": enum(["nextjs", "vercel-edge", "cloudflare", "node"]),
                },
            ),
        },
    ),
    "template_yaml": """
version: \"1.0\"
name: Mastra Template
type: ai-agent
description: Template for a Mastra-targeted universal-spawn manifest.

platforms:
  mastra:
    agents:
      - name: assistant
        model: anthropic/claude-sonnet-4-6
        instructions_file: agents/assistant.md
        tools: [search, math]
        memory: true
    workflows:
      - name: triage
        entry: classify
        schema_ref: workflows/triage.state.ts
    memory:
      store: libsql
      url_env: MASTRA_LIBSQL_URL
    deploy:
      runtime: nextjs

safety:
  min_permissions: [network:outbound:api.anthropic.com]
  rate_limit_qps: 3
  cost_limit_usd_daily: 10

env_vars_required:
  - name: ANTHROPIC_API_KEY
    description: Anthropic key.
    secret: true
  - name: MASTRA_LIBSQL_URL
    description: libSQL URL.
    secret: true

deployment:
  targets: [mastra]

metadata:
  license: MIT
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/mastra-template }
""",
    "compatibility_extras": "",
    "perks": STANDARD_PERKS,
    "examples": [
        {"yaml": """
version: \"1.0\"
name: Mastra Hello
type: ai-agent
summary: Minimal Mastra agent on Anthropic Sonnet.
description: One agent, no workflow, in-memory state.

platforms:
  mastra:
    agents:
      - name: assistant
        model: anthropic/claude-sonnet-4-6
    deploy: { runtime: node }

safety:
  min_permissions: [network:outbound:api.anthropic.com]
  safe_for_auto_spawn: true

env_vars_required:
  - name: ANTHROPIC_API_KEY
    description: Anthropic key.
    secret: true

deployment:
  targets: [mastra]

metadata:
  license: MIT
  author: { name: Hello Co., handle: hello-co }
  source: { type: git, url: https://github.com/hello-co/mastra-hello }
  id: com.hello-co.mastra-hello
"""},
        {"yaml": """
version: \"1.0\"
name: Mastra Booking Flow
type: workflow
summary: Full Mastra booking flow with three agents, two workflows, Postgres memory, Cloudflare deploy.
description: >
  Booking flow for a gym. Three agents (triage, search, confirm)
  and two workflows (book, cancel). Postgres memory, Cloudflare Edge
  runtime, OTEL telemetry to Axiom.

platforms:
  mastra:
    agents:
      - name: triage
        model: anthropic/claude-haiku-4-5-20251001
        instructions_file: agents/triage.md
      - name: search
        model: anthropic/claude-sonnet-4-6
        instructions_file: agents/search.md
        tools: [find_slot]
      - name: confirm
        model: anthropic/claude-sonnet-4-6
        instructions_file: agents/confirm.md
        tools: [reserve_slot]
        memory: true
    workflows:
      - name: book
        entry: triage
        schema_ref: workflows/book.state.ts
      - name: cancel
        entry: lookup
        schema_ref: workflows/cancel.state.ts
    memory:
      store: pg
      url_env: MASTRA_PG_URL
    telemetry:
      otlp_endpoint_env: OTEL_EXPORTER_OTLP_ENDPOINT
    deploy:
      runtime: cloudflare

safety:
  min_permissions:
    - network:outbound:api.anthropic.com
    - network:outbound:db.internal.gym.example
  rate_limit_qps: 10
  cost_limit_usd_daily: 25
  safe_for_auto_spawn: false

env_vars_required:
  - name: ANTHROPIC_API_KEY
    description: Anthropic key.
    secret: true
  - name: MASTRA_PG_URL
    description: Postgres URL.
    secret: true
  - name: OTEL_EXPORTER_OTLP_ENDPOINT
    description: OTEL endpoint.
    secret: true

deployment:
  targets: [mastra, cloudflare]

metadata:
  license: proprietary
  author: { name: Gym Co., handle: gym-co, org: Gym }
  source: { type: git, url: https://github.com/gym-co/mastra-booking }
  id: com.gym-co.mastra-booking
"""},
        {"yaml": """
version: \"1.0\"
name: Mastra Plate Curator
type: ai-agent
summary: Creative Mastra agent curating a parchment plate feed.
description: >
  One agent subscribed to an RSS plate feed. Scores each item against
  the Residual Frequencies rubric, posts scores to libSQL for a later
  digest. Deploys on Vercel Edge.

platforms:
  mastra:
    agents:
      - name: curator
        model: mistral/mistral-large-latest
        instructions_file: agents/curator.md
        tools: [score_plate]
        memory: true
    memory:
      store: libsql
      url_env: MASTRA_LIBSQL_URL
    deploy: { runtime: vercel-edge }

safety:
  min_permissions: [network:outbound:api.mistral.ai]
  cost_limit_usd_daily: 3
  safe_for_auto_spawn: true

env_vars_required:
  - name: MISTRAL_API_KEY
    description: Mistral key.
    secret: true
  - name: MASTRA_LIBSQL_URL
    description: libSQL URL.
    secret: true

deployment:
  targets: [mastra]

visuals: { palette: parchment }

metadata:
  license: CC-BY-4.0
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/mastra-curator }
  categories: [ai, graphics]
  id: com.plate-studio.mastra-curator
"""},
    ],
}
