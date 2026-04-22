"""Semantic Kernel (Microsoft) — skills + planners (C# / Python)."""
from scripts.ai_specs._common import (
    STANDARD_PERKS, enum, str_prop, bool_prop, schema_object,
)

SPEC = {
    "id": "semantic-kernel",
    "title": "Semantic Kernel (Microsoft)",
    "location": "multi-agent",

    "lede": (
        "Semantic Kernel is Microsoft's orchestration framework "
        "organized around skills (collections of native or prompt "
        "functions) and planners (auto-invoked via function calling). "
        "A manifest declares the language runtime, the connector, the "
        "skills that get loaded at boot, and the planner kind."
    ),
    "cares": (
        "The language (`csharp`, `python`, `java`), the connector "
        "(OpenAI / Azure OpenAI / HuggingFace / local), the "
        "skills array, and which planner runs the show."
    ),
    "extras": (
        "`skills[].kind` is `native`, `prompt`, or `openapi`. "
        "`planner` picks `function-calling`, `handlebars`, `sequential`, "
        "or `none`."
    ),
    "compat_table": [
        ("version", "Required."),
        ("type", "`ai-agent`, `workflow`, `library`."),
        ("safety.*", "Informational; enforced at the connector."),
        ("env_vars_required", "Runtime host secret store."),
        ("platforms.semantic-kernel", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("metadata.id", "Stable key."),
        ("name, description", "Kernel metadata."),
        ("type", "`ai-agent`, `workflow`, `library`."),
        ("safety.*", "Informational."),
        ("env_vars_required", "Secret store."),
        ("platforms.semantic-kernel.language", "`csharp`, `python`, `java`."),
        ("platforms.semantic-kernel.connector", "Kernel connector."),
        ("platforms.semantic-kernel.model", "Model id passed to the connector."),
        ("platforms.semantic-kernel.skills", "Array of skill definitions."),
        ("platforms.semantic-kernel.planner", "Planner kind."),
    ],
    "platform_fields": {
        "language": "`csharp`, `python`, or `java`.",
        "connector": "`openai`, `azure-openai`, `huggingface`, `ollama`, `local`.",
        "model": "Model id for the connector.",
        "skills": "Array of `{name, kind, path}` skill definitions.",
        "planner": "`function-calling`, `handlebars`, `sequential`, `none`.",
    },
    "schema_body": schema_object(
        required=["language", "connector", "model"],
        properties={
            "language": enum(["csharp", "python", "java"]),
            "connector": enum(["openai", "azure-openai", "huggingface", "ollama", "local"]),
            "model": str_prop(),
            "endpoint_url": str_prop(),
            "skills": {
                "type": "array",
                "items": schema_object(
                    required=["name", "kind"],
                    properties={
                        "name": str_prop(pattern=r"^[A-Za-z][A-Za-z0-9_]{0,63}$"),
                        "kind": enum(["native", "prompt", "openapi"]),
                        "path": str_prop(desc="Relative path to the skill directory or OpenAPI file."),
                    },
                ),
            },
            "planner": enum(["function-calling", "handlebars", "sequential", "none"]),
            "memory": schema_object(
                properties={
                    "store": enum(["volatile", "chroma", "pinecone", "azure-cognitive-search"]),
                },
            ),
        },
    ),
    "template_yaml": """
version: \"1.0\"
name: Semantic Kernel Template
type: ai-agent
description: Template for a Semantic-Kernel-targeted universal-spawn manifest.

platforms:
  semantic-kernel:
    language: csharp
    connector: azure-openai
    model: gpt-5
    skills:
      - { name: Search, kind: native, path: Skills/Search }
      - { name: Summarize, kind: prompt, path: Skills/Summarize }
    planner: function-calling
    memory: { store: volatile }

safety:
  min_permissions: [network:outbound:acme-openai.openai.azure.com]
  rate_limit_qps: 3
  cost_limit_usd_daily: 10

env_vars_required:
  - name: AZURE_OPENAI_ENDPOINT
    description: Azure OpenAI endpoint URL.
  - name: AZURE_OPENAI_API_KEY
    description: Azure OpenAI API key.
    secret: true

deployment:
  targets: [semantic-kernel]

metadata:
  license: MIT
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/sk-template }
""",
    "compatibility_extras": "",
    "perks": STANDARD_PERKS,
    "examples": [
        {"yaml": """
version: \"1.0\"
name: SK Hello
type: ai-skill
summary: Minimal Semantic Kernel skill in Python with one prompt function.
description: Single-skill kernel. Python. OpenAI connector. Function-calling planner.

platforms:
  semantic-kernel:
    language: python
    connector: openai
    model: gpt-4o-mini
    skills:
      - { name: Greet, kind: prompt, path: skills/greet }
    planner: function-calling

safety:
  min_permissions: [network:outbound:api.openai.com]
  safe_for_auto_spawn: true

env_vars_required:
  - name: OPENAI_API_KEY
    description: OpenAI API key.
    secret: true

deployment:
  targets: [semantic-kernel]

metadata:
  license: MIT
  author: { name: SK Co., handle: sk-co }
  source: { type: git, url: https://github.com/sk-co/sk-hello }
  id: com.sk-co.sk-hello
"""},
        {"yaml": """
version: \"1.0\"
name: SK Enterprise Agent
type: ai-agent
summary: Full Semantic Kernel agent on Azure OpenAI with Cognitive Search memory.
description: >
  C# kernel on Azure OpenAI. Four skills (Search, Summarize, Email,
  Calendar), Cognitive Search memory, handlebars planner. Production-
  shaped manifest.

platforms:
  semantic-kernel:
    language: csharp
    connector: azure-openai
    model: gpt-5
    endpoint_url: https://acme-openai.openai.azure.com
    skills:
      - { name: Search, kind: native, path: Skills/Search }
      - { name: Summarize, kind: prompt, path: Skills/Summarize }
      - { name: Email, kind: openapi, path: openapi/email.yaml }
      - { name: Calendar, kind: openapi, path: openapi/calendar.yaml }
    planner: handlebars
    memory: { store: azure-cognitive-search }

safety:
  min_permissions:
    - network:outbound:acme-openai.openai.azure.com
    - network:outbound:acme-search.search.windows.net
    - network:outbound:graph.microsoft.com
  rate_limit_qps: 5
  cost_limit_usd_daily: 40
  safe_for_auto_spawn: false
  data_residency: [us, eu]

env_vars_required:
  - name: AZURE_OPENAI_ENDPOINT
    description: Azure OpenAI endpoint URL.
  - name: AZURE_OPENAI_API_KEY
    description: Azure OpenAI key.
    secret: true
  - name: AZURE_SEARCH_ENDPOINT
    description: Cognitive Search endpoint.
  - name: AZURE_SEARCH_KEY
    description: Cognitive Search key.
    secret: true

deployment:
  targets: [semantic-kernel]

metadata:
  license: proprietary
  author: { name: Acme IT, handle: acme-it, org: Acme }
  source: { type: git, url: https://github.com/acme-it/sk-enterprise }
  id: com.acme-it.sk-enterprise
"""},
        {"yaml": """
version: \"1.0\"
name: SK Plate Judge
type: ai-skill
summary: Creative Semantic Kernel skill that judges plate submissions offline.
description: >
  Java kernel wrapping a local Ollama connector. One skill (Judge)
  applies the Residual Frequencies rubric to a plate image + caption.
  Offline, no network beyond local Ollama.

platforms:
  semantic-kernel:
    language: java
    connector: ollama
    model: llama3.3
    endpoint_url: http://localhost:11434
    skills:
      - { name: Judge, kind: prompt, path: skills/judge }
    planner: none
    memory: { store: volatile }

safety:
  min_permissions: [network:outbound:localhost]
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [semantic-kernel]

visuals: { palette: parchment }

metadata:
  license: Apache-2.0
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/sk-plate-judge }
  categories: [ai, graphics]
  id: com.plate-studio.sk-plate-judge
"""},
    ],
}
