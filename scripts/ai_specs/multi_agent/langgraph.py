"""LangGraph — graph state machines (Python / TypeScript)."""
from scripts.ai_specs._common import (
    STANDARD_PERKS, enum, str_prop, bool_prop, schema_object,
)

SPEC = {
    "id": "langgraph",
    "title": "LangGraph",
    "location": "multi-agent",

    "lede": (
        "LangGraph is a graph runtime on top of LangChain. Agents and "
        "tools are nodes; edges are routing decisions; the run "
        "replays a typed state dictionary. A manifest captures the "
        "graph topology so scaffolding can emit the bindings."
    ),
    "cares": (
        "The nodes, the edges (typed conditionals), the state schema "
        "reference, and the checkpoint store so the graph survives "
        "restarts."
    ),
    "extras": (
        "`checkpoint.store` picks the checkpoint backend (`memory`, "
        "`sqlite`, `postgres`, `redis`). `interrupt.before[]` and "
        "`interrupt.after[]` mark nodes where the graph pauses for a "
        "human."
    ),
    "compat_table": [
        ("version", "Required."),
        ("type", "`ai-agent`, `workflow`."),
        ("safety.*", "Informational."),
        ("env_vars_required", "Runtime host + checkpoint store."),
        ("platforms.langgraph", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("metadata.id", "Stable key."),
        ("name, description", "LangSmith metadata."),
        ("type", "`ai-agent`, `workflow`."),
        ("safety.*", "Informational."),
        ("env_vars_required", "Secret store."),
        ("platforms.langgraph.language", "`python`, `typescript`."),
        ("platforms.langgraph.entry_graph", "`{file, symbol}` locating the compiled graph."),
        ("platforms.langgraph.state_schema_ref", "Path to the state Pydantic / zod schema source."),
        ("platforms.langgraph.nodes", "Declared node list."),
        ("platforms.langgraph.edges", "Declared edges (static + conditional)."),
        ("platforms.langgraph.checkpoint", "Checkpoint store settings."),
        ("platforms.langgraph.interrupt", "Human-in-the-loop interrupts."),
    ],
    "platform_fields": {
        "language": "`python` or `typescript`.",
        "entry_graph": "`{file, symbol}` locating the compiled graph.",
        "state_schema_ref": "Path to the state schema module.",
        "nodes": "Declared node list.",
        "edges": "Static + conditional edges.",
        "checkpoint": "Checkpoint store (`memory`, `sqlite`, `postgres`, `redis`).",
        "interrupt": "`{before[], after[]}` human-in-the-loop interrupts.",
    },
    "schema_body": schema_object(
        required=["language", "entry_graph", "nodes"],
        properties={
            "language": enum(["python", "typescript"]),
            "entry_graph": schema_object(
                required=["file", "symbol"],
                properties={
                    "file": str_prop(),
                    "symbol": str_prop(pattern=r"^[A-Za-z_][A-Za-z0-9_]*$"),
                },
            ),
            "state_schema_ref": str_prop(),
            "nodes": {
                "type": "array",
                "minItems": 1,
                "items": schema_object(
                    required=["name"],
                    properties={
                        "name": str_prop(pattern=r"^[a-z][a-z0-9_-]{0,63}$"),
                        "kind": enum(["agent", "tool", "router", "reducer", "human"]),
                        "llm": schema_object(
                            properties={
                                "provider": enum(["openai", "anthropic", "google", "mistral", "cohere", "local"]),
                                "model": str_prop(),
                            },
                        ),
                        "tools": {"type": "array", "items": str_prop()},
                    },
                ),
            },
            "edges": {
                "type": "array",
                "items": schema_object(
                    required=["from"],
                    properties={
                        "from": str_prop(),
                        "to": str_prop(),
                        "conditional_ref": str_prop(desc="Relative path to a conditional routing function."),
                    },
                ),
            },
            "checkpoint": schema_object(
                properties={
                    "store": enum(["memory", "sqlite", "postgres", "redis"]),
                    "dsn_env": str_prop(pattern=r"^[A-Z][A-Z0-9_]*$"),
                },
            ),
            "interrupt": schema_object(
                properties={
                    "before": {"type": "array", "items": str_prop()},
                    "after":  {"type": "array", "items": str_prop()},
                },
            ),
        },
    ),
    "template_yaml": """
version: \"1.0\"
name: LangGraph Template
type: workflow
description: Template for a LangGraph-targeted universal-spawn manifest.

platforms:
  langgraph:
    language: python
    entry_graph: { file: app/graph.py, symbol: graph }
    state_schema_ref: app/state.py
    nodes:
      - name: router
        kind: router
      - name: agent
        kind: agent
        llm: { provider: anthropic, model: claude-sonnet-4-6 }
        tools: [search]
      - name: tools
        kind: tool
      - name: reducer
        kind: reducer
    edges:
      - { from: START, to: router }
      - { from: router, conditional_ref: app/router_edges.py }
      - { from: agent, to: tools }
      - { from: tools, to: reducer }
      - { from: reducer, to: END }
    checkpoint:
      store: sqlite
      dsn_env: LANGGRAPH_CHECKPOINT_DSN
    interrupt:
      before: [tools]

safety:
  min_permissions: [network:outbound:api.anthropic.com]
  rate_limit_qps: 3
  cost_limit_usd_daily: 10

env_vars_required:
  - name: ANTHROPIC_API_KEY
    description: Anthropic API key.
    secret: true
  - name: LANGGRAPH_CHECKPOINT_DSN
    description: SQLite path for the checkpoint store.
    example: \"file:///var/lib/langgraph/ckpt.sqlite\"

deployment:
  targets: [langgraph]

metadata:
  license: Apache-2.0
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/langgraph-template }
""",
    "compatibility_extras": "",
    "perks": STANDARD_PERKS + [
        "**Graph preview** — registries render the declared graph as "
        "a DOT diagram on the card.",
    ],
    "examples": [
        {"yaml": """
version: \"1.0\"
name: LangGraph Minimal
type: workflow
summary: Minimal two-node LangGraph with in-memory checkpointing.
description: Agent + tools node, START → agent → tools → END. No conditional routing.

platforms:
  langgraph:
    language: python
    entry_graph: { file: app/graph.py, symbol: graph }
    nodes:
      - name: agent
        kind: agent
        llm: { provider: anthropic, model: claude-haiku-4-5-20251001 }
        tools: [web_search]
      - name: tools
        kind: tool
    edges:
      - { from: START, to: agent }
      - { from: agent, to: tools }
      - { from: tools, to: END }
    checkpoint: { store: memory }

safety:
  min_permissions: [network:outbound:api.anthropic.com]
  safe_for_auto_spawn: true

env_vars_required:
  - name: ANTHROPIC_API_KEY
    description: Anthropic API key.
    secret: true

deployment:
  targets: [langgraph]

metadata:
  license: Apache-2.0
  author: { name: Graph Co., handle: graph-co }
  source: { type: git, url: https://github.com/graph-co/langgraph-min }
  id: com.graph-co.langgraph-min
"""},
        {"yaml": """
version: \"1.0\"
name: LangGraph Human-in-Loop Approver
type: workflow
summary: Full LangGraph with Postgres checkpointing and human-before-tools interrupt.
description: >
  Approver graph: agent proposes an action, a human reviews before
  `tools` runs, reducer writes the audit log. Postgres checkpoints
  so resumption across restarts is safe.

platforms:
  langgraph:
    language: python
    entry_graph: { file: app/graph.py, symbol: graph }
    state_schema_ref: app/state.py
    nodes:
      - name: agent
        kind: agent
        llm: { provider: anthropic, model: claude-opus-4-7 }
        tools: [execute_action]
      - name: tools
        kind: tool
      - name: human
        kind: human
      - name: audit
        kind: reducer
    edges:
      - { from: START, to: agent }
      - { from: agent, to: human }
      - { from: human, to: tools }
      - { from: tools, to: audit }
      - { from: audit, to: END }
    checkpoint:
      store: postgres
      dsn_env: LANGGRAPH_CHECKPOINT_DSN
    interrupt:
      before: [tools]

safety:
  min_permissions:
    - network:outbound:api.anthropic.com
    - network:outbound:db.internal.acme.com
  rate_limit_qps: 2
  cost_limit_usd_daily: 20
  safe_for_auto_spawn: false

env_vars_required:
  - name: ANTHROPIC_API_KEY
    description: Anthropic API key.
    secret: true
  - name: LANGGRAPH_CHECKPOINT_DSN
    description: Postgres DSN.
    secret: true

deployment:
  targets: [langgraph]

metadata:
  license: proprietary
  author: { name: Ops Team, handle: ops-team, org: Acme }
  source: { type: git, url: https://github.com/acme-ops/langgraph-approver }
  id: com.acme-ops.langgraph-approver
"""},
        {"yaml": """
version: \"1.0\"
name: Plate Review Cycle
type: workflow
summary: Creative LangGraph cycle that keeps revising a plate caption until score threshold.
description: >
  Plate captioner cycle: writer → critic → router (score). Router
  loops back to writer until the critic's score clears threshold,
  then to END. Demonstrates graph cycles with conditional edges.

platforms:
  langgraph:
    language: typescript
    entry_graph: { file: src/graph.ts, symbol: reviewGraph }
    state_schema_ref: src/state.ts
    nodes:
      - name: writer
        kind: agent
        llm: { provider: anthropic, model: claude-sonnet-4-6 }
      - name: critic
        kind: agent
        llm: { provider: anthropic, model: claude-sonnet-4-6 }
      - name: router
        kind: router
    edges:
      - { from: START, to: writer }
      - { from: writer, to: critic }
      - { from: critic, to: router }
      - { from: router, conditional_ref: src/router.ts }

safety:
  min_permissions: [network:outbound:api.anthropic.com]
  cost_limit_usd_daily: 5
  safe_for_auto_spawn: true

env_vars_required:
  - name: ANTHROPIC_API_KEY
    description: Anthropic API key.
    secret: true

deployment:
  targets: [langgraph]

visuals: { palette: parchment }

metadata:
  license: CC-BY-4.0
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/langgraph-review-cycle }
  categories: [ai, writing, graphics]
  id: com.plate-studio.langgraph-review-cycle
"""},
    ],
}
