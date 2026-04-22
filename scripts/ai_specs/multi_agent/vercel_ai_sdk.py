"""Vercel AI SDK — streaming + generateObject (TypeScript)."""
from scripts.ai_specs._common import (
    STANDARD_PERKS, enum, str_prop, bool_prop, schema_object,
)

SPEC = {
    "id": "vercel-ai-sdk",
    "title": "Vercel AI SDK",
    "location": "multi-agent",

    "lede": (
        "The Vercel AI SDK is a provider-agnostic library for TypeScript "
        "apps: `streamText`, `generateObject` (typed via Zod), `tool`, "
        "and a common tool-calling loop. A manifest declares the "
        "default provider/model, the tools, the Zod schema refs for "
        "structured output, and the deployment runtime."
    ),
    "cares": (
        "The provider + model default, the array of tools with Zod "
        "schema paths, and whether `generateObject` is wired up with "
        "its own schema."
    ),
    "extras": (
        "`generate_object.schema_ref` points at a Zod schema module. "
        "`stream` defaults to true; set false for non-streaming one-"
        "shot calls."
    ),
    "compat_table": [
        ("version", "Required."),
        ("type", "`ai-agent`, `ai-skill`, `library`, `web-app`."),
        ("safety.*", "Informational."),
        ("env_vars_required", "Host runtime (typically Vercel)."),
        ("platforms.vercel-ai-sdk", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("metadata.id", "Stable key."),
        ("name, description", "Card."),
        ("type", "`ai-agent`, `ai-skill`, `library`, `web-app`."),
        ("safety.*", "Informational."),
        ("env_vars_required", "Secrets."),
        ("platforms.vercel-ai-sdk.provider", "Default provider id."),
        ("platforms.vercel-ai-sdk.model", "Default model id."),
        ("platforms.vercel-ai-sdk.tools", "Array of `{name, zod_schema_ref, handler_ref}` tools."),
        ("platforms.vercel-ai-sdk.generate_object", "Schema ref for `generateObject`."),
        ("platforms.vercel-ai-sdk.stream", "Streaming on/off."),
        ("platforms.vercel-ai-sdk.runtime", "`node`, `edge`, `nextjs`."),
    ],
    "platform_fields": {
        "provider": "Default provider (`openai`, `anthropic`, `google`, `mistral`, `cohere`, `xai`, `groq`).",
        "model": "Default model id.",
        "tools": "Array of tools (`{name, zod_schema_ref, handler_ref}`).",
        "generate_object": "Zod schema ref for `generateObject`.",
        "stream": "Streaming mode.",
        "runtime": "`node`, `edge`, or `nextjs`.",
    },
    "schema_body": schema_object(
        required=["provider", "model"],
        properties={
            "provider": enum(["openai", "anthropic", "google", "mistral", "cohere", "xai", "groq", "together", "fireworks"]),
            "model": str_prop(),
            "tools": {
                "type": "array",
                "items": schema_object(
                    required=["name", "zod_schema_ref", "handler_ref"],
                    properties={
                        "name": str_prop(pattern=r"^[a-zA-Z][a-zA-Z0-9_]{0,63}$"),
                        "zod_schema_ref": str_prop(desc="Relative path to the Zod schema module exporting the tool params schema."),
                        "handler_ref": str_prop(desc="Relative path to the handler module."),
                    },
                ),
            },
            "generate_object": schema_object(
                properties={
                    "schema_ref": str_prop(),
                    "mode": enum(["auto", "json", "tool"]),
                },
            ),
            "stream": bool_prop(True),
            "runtime": enum(["node", "edge", "nextjs"]),
            "temperature": {"type": "number", "minimum": 0, "maximum": 2},
            "system_prompt_file": str_prop(),
        },
    ),
    "template_yaml": """
version: \"1.0\"
name: Vercel AI SDK Template
type: ai-agent
description: Template for a Vercel-AI-SDK-targeted universal-spawn manifest.

platforms:
  vercel-ai-sdk:
    provider: anthropic
    model: claude-sonnet-4-6
    tools:
      - name: search
        zod_schema_ref: tools/search.schema.ts
        handler_ref: tools/search.handler.ts
    generate_object:
      schema_ref: schemas/response.schema.ts
      mode: auto
    stream: true
    runtime: nextjs
    temperature: 0.2

safety:
  min_permissions: [network:outbound:api.anthropic.com]
  rate_limit_qps: 5
  cost_limit_usd_daily: 10

env_vars_required:
  - name: ANTHROPIC_API_KEY
    description: Anthropic key.
    secret: true

deployment:
  targets: [vercel-ai-sdk]

metadata:
  license: MIT
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/vercel-ai-sdk-template }
""",
    "compatibility_extras": "",
    "perks": STANDARD_PERKS,
    "examples": [
        {"yaml": """
version: \"1.0\"
name: AI SDK Chat
type: ai-agent
summary: Minimal Vercel AI SDK chat route on Next.js.
description: Streaming chat on Anthropic Sonnet, one tool, Next.js runtime.

platforms:
  vercel-ai-sdk:
    provider: anthropic
    model: claude-sonnet-4-6
    stream: true
    runtime: nextjs

safety:
  min_permissions: [network:outbound:api.anthropic.com]
  safe_for_auto_spawn: true

env_vars_required:
  - name: ANTHROPIC_API_KEY
    description: Anthropic key.
    secret: true

deployment:
  targets: [vercel-ai-sdk, vercel]

metadata:
  license: MIT
  author: { name: Chat Co., handle: chat-co }
  source: { type: git, url: https://github.com/chat-co/ai-sdk-chat }
  id: com.chat-co.ai-sdk-chat
"""},
        {"yaml": """
version: \"1.0\"
name: AI SDK Typed Agent
type: ai-agent
summary: Full Vercel AI SDK agent with four Zod-typed tools and generateObject output.
description: >
  Production agent backed by the AI SDK on the Edge runtime. Four
  tools with Zod schemas, generateObject for the final typed response,
  streaming enabled.

platforms:
  vercel-ai-sdk:
    provider: anthropic
    model: claude-opus-4-7
    tools:
      - name: search
        zod_schema_ref: tools/search.schema.ts
        handler_ref: tools/search.handler.ts
      - name: fetch_url
        zod_schema_ref: tools/fetch_url.schema.ts
        handler_ref: tools/fetch_url.handler.ts
      - name: summarize
        zod_schema_ref: tools/summarize.schema.ts
        handler_ref: tools/summarize.handler.ts
      - name: cite
        zod_schema_ref: tools/cite.schema.ts
        handler_ref: tools/cite.handler.ts
    generate_object:
      schema_ref: schemas/report.schema.ts
      mode: tool
    stream: true
    runtime: edge
    temperature: 0.2

safety:
  min_permissions: [network:outbound:api.anthropic.com]
  rate_limit_qps: 10
  cost_limit_usd_daily: 30
  safe_for_auto_spawn: false

env_vars_required:
  - name: ANTHROPIC_API_KEY
    description: Anthropic key.
    secret: true

deployment:
  targets: [vercel-ai-sdk, vercel]

metadata:
  license: proprietary
  author: { name: Platform Co., handle: platform-co, org: Platform }
  source: { type: git, url: https://github.com/platform-co/ai-sdk-agent }
  id: com.platform-co.ai-sdk-agent
"""},
        {"yaml": """
version: \"1.0\"
name: AI SDK Plate Generator
type: ai-skill
summary: Creative AI SDK route that generates Residual Frequencies plate captions.
description: >
  Node-runtime route that emits a typed plate caption object (id,
  archetype, caption, scoring) via generateObject on Mistral Large.

platforms:
  vercel-ai-sdk:
    provider: mistral
    model: mistral-large-latest
    generate_object:
      schema_ref: schemas/plate.schema.ts
      mode: json
    stream: false
    runtime: node
    temperature: 0.6

safety:
  min_permissions: [network:outbound:api.mistral.ai]
  safe_for_auto_spawn: true

env_vars_required:
  - name: MISTRAL_API_KEY
    description: Mistral key.
    secret: true

deployment:
  targets: [vercel-ai-sdk, vercel]

visuals: { palette: parchment }

metadata:
  license: CC-BY-4.0
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/ai-sdk-plate-generator }
  categories: [ai, graphics, writing]
  id: com.plate-studio.ai-sdk-plate-generator
"""},
    ],
}
