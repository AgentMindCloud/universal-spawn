"""LangChain — chains + agents framework (Python / TypeScript)."""
from scripts.ai_specs._common import (
    STANDARD_PERKS, enum, str_prop, bool_prop, schema_object,
)

SPEC = {
    "id": "langchain",
    "title": "LangChain",
    "location": "multi-agent",

    "lede": (
        "LangChain is a framework, not a runtime — a manifest that "
        "targets LangChain describes how declarative data maps onto a "
        "programmatic graph of `Runnable`s. This extension captures "
        "entry chains, retriever components, and the provider/model "
        "pair LangChain should bind by default."
    ),
    "cares": (
        "The language (`python` or `typescript`), the entry chain "
        "module path, the provider/model pair, and the retriever "
        "spec. The manifest is read by scaffolding tools that emit "
        "LangChain code; LangChain itself does not enforce anything "
        "at runtime."
    ),
    "extras": (
        "`entry_chain.file` + `entry_chain.symbol` point at the entry "
        "`Runnable`. `retriever.kind` names the retriever family "
        "(`vector`, `web`, `parent-document`)."
    ),
    "compat_table": [
        ("version", "Required."),
        ("name, description", "Used in LangSmith project metadata."),
        ("type", "`ai-agent`, `ai-skill`, `workflow`."),
        ("safety.cost_limit_usd_daily", "Informational; LangChain delegates cost to the model provider."),
        ("env_vars_required", "Staged in LangSmith or the runtime host."),
        ("platforms.langchain", "Strict; drives scaffolding."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("metadata.id", "Stable key."),
        ("name, description", "LangSmith project metadata."),
        ("type", "`ai-agent`, `ai-skill`, `workflow`."),
        ("safety.*", "Informational."),
        ("env_vars_required", "Staged in LangSmith / runtime host."),
        ("platforms.langchain.language", "`python` or `typescript`."),
        ("platforms.langchain.provider", "`openai`, `anthropic`, `google`, `mistral`, `cohere`, `together`, `local`."),
        ("platforms.langchain.model", "Provider-specific model id."),
        ("platforms.langchain.entry_chain", "Entry chain module + symbol."),
        ("platforms.langchain.retriever", "Retriever configuration."),
        ("platforms.langchain.langsmith_tracing", "Enable LangSmith tracing."),
    ],
    "platform_fields": {
        "language": "`python` or `typescript`.",
        "provider": "Model-provider id.",
        "model": "Provider-specific model id.",
        "entry_chain": "`{file, symbol}` locating the entry Runnable.",
        "retriever": "Retriever family + parameters.",
        "langsmith_tracing": "Enable LangSmith tracing.",
    },
    "schema_body": schema_object(
        required=["language", "provider", "model", "entry_chain"],
        properties={
            "language": enum(["python", "typescript"]),
            "provider": enum(["openai", "anthropic", "google", "mistral", "cohere", "together", "fireworks", "local"]),
            "model": str_prop(),
            "entry_chain": schema_object(
                required=["file", "symbol"],
                properties={
                    "file": str_prop(desc="Relative path to the module exporting the entry chain."),
                    "symbol": str_prop(pattern=r"^[A-Za-z_][A-Za-z0-9_]*$"),
                },
            ),
            "retriever": schema_object(
                properties={
                    "kind": enum(["vector", "web", "parent-document", "none"]),
                    "vector_store": enum(["chroma", "pinecone", "weaviate", "qdrant", "pgvector", "faiss"]),
                    "embeddings_model": str_prop(),
                    "top_k": {"type": "integer", "minimum": 1, "maximum": 100},
                },
            ),
            "langsmith_tracing": bool_prop(False),
            "langsmith_project": str_prop(),
        },
    ),
    "template_yaml": """
version: \"1.0\"
name: LangChain Template
type: ai-agent
description: Template for a LangChain-targeted universal-spawn manifest.

platforms:
  langchain:
    language: python
    provider: anthropic
    model: claude-sonnet-4-6
    entry_chain:
      file: app/chain.py
      symbol: chain
    retriever:
      kind: vector
      vector_store: chroma
      embeddings_model: text-embedding-3-small
      top_k: 5
    langsmith_tracing: true
    langsmith_project: your-project

safety:
  min_permissions: [network:outbound:api.anthropic.com, network:outbound:api.openai.com]
  rate_limit_qps: 3
  cost_limit_usd_daily: 5

env_vars_required:
  - name: ANTHROPIC_API_KEY
    description: Anthropic API key.
    secret: true
  - name: OPENAI_API_KEY
    description: OpenAI API key used for embeddings.
    secret: true
  - name: LANGCHAIN_API_KEY
    description: LangSmith API key.
    required: false
    secret: true

deployment:
  targets: [langchain]

metadata:
  license: Apache-2.0
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/langchain-template }
""",
    "compatibility_extras": (
        "## Declarative → programmatic\n\n"
        "A scaffolding tool reads this manifest and emits LangChain "
        "bindings: a `ChatModel` for `provider`+`model`, a retriever "
        "for `retriever.*`, and imports `entry_chain.file`'s "
        "`entry_chain.symbol` as the graph entrypoint. The manifest "
        "is declarative; the generated code is programmatic. The "
        "round-trip is not two-way — code changes that stray from "
        "the manifest require regenerating the manifest."
    ),
    "perks": STANDARD_PERKS + [
        "**LangSmith project prefill** — `langsmith_project` becomes "
        "the LangSmith project id for traces from this manifest.",
    ],
    "examples": [
        {"yaml": """
version: \"1.0\"
name: LangChain QA
type: ai-agent
summary: Minimal LangChain QA chain over a Chroma vector store.
description: One chain, Anthropic Sonnet, Chroma vector store, five-result retrieval.

platforms:
  langchain:
    language: python
    provider: anthropic
    model: claude-sonnet-4-6
    entry_chain: { file: app/chain.py, symbol: chain }
    retriever:
      kind: vector
      vector_store: chroma
      embeddings_model: text-embedding-3-small
      top_k: 5

safety:
  min_permissions: [network:outbound:api.anthropic.com, network:outbound:api.openai.com]
  safe_for_auto_spawn: true

env_vars_required:
  - name: ANTHROPIC_API_KEY
    description: Anthropic API key.
    secret: true
  - name: OPENAI_API_KEY
    description: OpenAI API key for embeddings.
    secret: true

deployment:
  targets: [langchain]

metadata:
  license: Apache-2.0
  author: { name: QA Co., handle: qa-co }
  source: { type: git, url: https://github.com/qa-co/langchain-qa }
  id: com.qa-co.langchain-qa
"""},
        {"yaml": """
version: \"1.0\"
name: LangChain Research
type: ai-agent
summary: Full LangChain research chain with LangSmith tracing and parent-document retrieval.
description: >
  Research agent that pulls from a Pinecone index via parent-document
  retrieval, streams responses through a Claude Opus chat model, and
  reports every trace to LangSmith.

platforms:
  langchain:
    language: python
    provider: anthropic
    model: claude-opus-4-7
    entry_chain: { file: app/research.py, symbol: graph }
    retriever:
      kind: parent-document
      vector_store: pinecone
      embeddings_model: text-embedding-3-large
      top_k: 8
    langsmith_tracing: true
    langsmith_project: research-agent

safety:
  min_permissions:
    - network:outbound:api.anthropic.com
    - network:outbound:api.openai.com
    - network:outbound:api.pinecone.io
  rate_limit_qps: 3
  cost_limit_usd_daily: 30
  safe_for_auto_spawn: false

env_vars_required:
  - name: ANTHROPIC_API_KEY
    description: Anthropic API key.
    secret: true
  - name: OPENAI_API_KEY
    description: OpenAI key (embeddings).
    secret: true
  - name: PINECONE_API_KEY
    description: Pinecone key.
    secret: true
  - name: LANGCHAIN_API_KEY
    description: LangSmith key.
    secret: true

deployment:
  targets: [langchain]

metadata:
  license: proprietary
  author: { name: Research Lab, handle: research-lab, org: Lab }
  source: { type: git, url: https://github.com/research-lab/langchain-research }
  id: com.research-lab.langchain-research
"""},
        {"yaml": """
version: \"1.0\"
name: LangChain Plate Tutor
type: ai-skill
summary: Creative LangChain chain in TypeScript teaching parchment palette theory.
description: >
  TypeScript LangChain chain. Takes a design question, optionally
  pulls from a web retriever, returns a three-paragraph lesson in
  lab-notebook voice. Uses Cohere Command-R.

platforms:
  langchain:
    language: typescript
    provider: cohere
    model: command-r-08-2024
    entry_chain: { file: src/tutor.ts, symbol: tutorChain }
    retriever:
      kind: web
      top_k: 3

safety:
  min_permissions: [network:outbound:api.cohere.com]
  safe_for_auto_spawn: true

env_vars_required:
  - name: COHERE_API_KEY
    description: Cohere API key.
    secret: true

deployment:
  targets: [langchain]

visuals: { palette: parchment }

metadata:
  license: CC-BY-4.0
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/langchain-plate-tutor }
  categories: [ai, education, graphics]
  id: com.plate-studio.langchain-plate-tutor
"""},
    ],
}
