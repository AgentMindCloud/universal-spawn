"""CrewAI — role-based multi-agent crews (Python)."""
from scripts.ai_specs._common import (
    STANDARD_PERKS, enum, str_prop, bool_prop, schema_object,
)

SPEC = {
    "id": "crewai",
    "title": "CrewAI",
    "location": "multi-agent",

    "lede": (
        "CrewAI models a multi-agent system as a crew — a set of "
        "roles, each with a goal and a backstory, working a sequence "
        "or parallel set of tasks. A universal-spawn manifest lets "
        "you declare the crew shape: who's in it, what tools each "
        "role has, and how tasks flow."
    ),
    "cares": (
        "The crew roster, per-role LLM binding, each role's tool list, "
        "and the process flow (`sequential`, `hierarchical`, "
        "`parallel`)."
    ),
    "extras": (
        "`roles[].tools[]` lists the tools a specific role can use. "
        "`tasks[].expected_output` captures the declarative success "
        "criterion CrewAI uses for the task's Pydantic validation."
    ),
    "compat_table": [
        ("version", "Required."),
        ("name, description", "Crew metadata."),
        ("type", "`ai-agent`, `workflow`."),
        ("safety.*", "Informational."),
        ("env_vars_required", "Runtime host credential store."),
        ("platforms.crewai", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("metadata.id", "Stable key."),
        ("name, description", "Crew metadata."),
        ("type", "`ai-agent`, `workflow`."),
        ("safety.*", "Informational; CrewAI delegates to the model providers."),
        ("env_vars_required", "Secret store."),
        ("platforms.crewai.process", "`sequential`, `hierarchical`, `parallel`."),
        ("platforms.crewai.roles", "Array of role definitions."),
        ("platforms.crewai.tasks", "Array of task definitions."),
        ("platforms.crewai.verbose", "Verbose logging toggle."),
    ],
    "platform_fields": {
        "process": "Crew process: `sequential`, `hierarchical`, or `parallel`.",
        "roles": "Array of role definitions (name, goal, backstory, llm, tools).",
        "tasks": "Array of task definitions (description, expected_output, role).",
        "verbose": "Enable verbose CrewAI logging.",
    },
    "schema_body": schema_object(
        required=["process", "roles", "tasks"],
        properties={
            "process": enum(["sequential", "hierarchical", "parallel"]),
            "roles": {
                "type": "array",
                "minItems": 1,
                "items": schema_object(
                    required=["name", "goal"],
                    properties={
                        "name": str_prop(pattern=r"^[a-z][a-z0-9_-]{0,63}$"),
                        "goal": str_prop(),
                        "backstory": str_prop(),
                        "llm": schema_object(
                            properties={
                                "provider": enum(["openai", "anthropic", "google", "mistral", "cohere", "together", "local"]),
                                "model": str_prop(),
                            },
                        ),
                        "tools": {"type": "array", "items": str_prop()},
                        "allow_delegation": bool_prop(False),
                    },
                ),
            },
            "tasks": {
                "type": "array",
                "minItems": 1,
                "items": schema_object(
                    required=["description", "role"],
                    properties={
                        "description": str_prop(),
                        "expected_output": str_prop(),
                        "role": str_prop(pattern=r"^[a-z][a-z0-9_-]{0,63}$"),
                        "context_from": {"type": "array", "items": str_prop()},
                    },
                ),
            },
            "verbose": bool_prop(False),
        },
    ),
    "template_yaml": """
version: \"1.0\"
name: CrewAI Template
type: workflow
description: Template for a CrewAI-targeted universal-spawn manifest.

platforms:
  crewai:
    process: sequential
    roles:
      - name: researcher
        goal: Find authoritative sources on the topic.
        backstory: Experienced archivist with a library sciences background.
        llm: { provider: anthropic, model: claude-sonnet-4-6 }
        tools: [web_search]
      - name: writer
        goal: Turn raw research into a clear brief.
        backstory: Science journalist trained in lab-notebook style.
        llm: { provider: anthropic, model: claude-opus-4-7 }
    tasks:
      - description: Research the topic provided by the user.
        expected_output: A list of five citeable sources with short summaries.
        role: researcher
      - description: Write a 300-word brief using the researcher's findings.
        expected_output: A 300-word brief with citations.
        role: writer
        context_from: [researcher]
    verbose: false

safety:
  min_permissions: [network:outbound:api.anthropic.com, network:outbound:api.duckduckgo.com]
  rate_limit_qps: 3
  cost_limit_usd_daily: 10

env_vars_required:
  - name: ANTHROPIC_API_KEY
    description: Anthropic API key used by both roles.
    secret: true

deployment:
  targets: [crewai]

metadata:
  license: Apache-2.0
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/crewai-template }
""",
    "compatibility_extras": (
        "## Declarative → programmatic\n\n"
        "CrewAI scaffolding reads this manifest and emits the equivalent "
        "`Agent`, `Task`, and `Crew` definitions in Python. Each role "
        "maps to an `Agent`; each task to a `Task`; the crew wraps "
        "them with the declared `process`. Declarative fields round-"
        "trip to programmatic symbols by name."
    ),
    "perks": STANDARD_PERKS + [
        "**Crew validator** — consoles validate that every `tasks[].role` "
        "resolves to a `roles[].name` before the first spawn.",
    ],
    "examples": [
        {"yaml": """
version: \"1.0\"
name: Crew Triage
type: workflow
summary: Minimal two-role CrewAI crew for support-ticket triage.
description: Router classifies tickets; responder drafts a reply. Sequential.

platforms:
  crewai:
    process: sequential
    roles:
      - name: router
        goal: Classify the incoming ticket into one of three priority buckets.
        llm: { provider: anthropic, model: claude-haiku-4-5-20251001 }
      - name: responder
        goal: Draft an empathetic reply matching the priority.
        llm: { provider: anthropic, model: claude-sonnet-4-6 }
    tasks:
      - description: Classify the ticket.
        expected_output: priority (high/medium/low).
        role: router
      - description: Draft a reply.
        expected_output: Two-paragraph empathetic reply.
        role: responder
        context_from: [router]

safety:
  min_permissions: [network:outbound:api.anthropic.com]
  safe_for_auto_spawn: true

env_vars_required:
  - name: ANTHROPIC_API_KEY
    description: Anthropic API key.
    secret: true

deployment:
  targets: [crewai]

metadata:
  license: Apache-2.0
  author: { name: Triage Co., handle: triage-co }
  source: { type: git, url: https://github.com/triage-co/crew-triage }
  id: com.triage-co.crew-triage
"""},
        {"yaml": """
version: \"1.0\"
name: Crew Research Lab
type: workflow
summary: Full CrewAI research lab with four roles and hierarchical process.
description: >
  Research lab: PI delegates to researcher, critic, and editor.
  Hierarchical process — the PI agent decides ordering. Verbose logs
  for LangSmith-style inspection.

platforms:
  crewai:
    process: hierarchical
    roles:
      - name: pi
        goal: Direct the research lab toward producing a peer-reviewable brief.
        backstory: Senior investigator with 20 years in the field.
        llm: { provider: anthropic, model: claude-opus-4-7 }
        allow_delegation: true
      - name: researcher
        goal: Surface citeable primary sources.
        llm: { provider: openai, model: gpt-5 }
        tools: [web_search, arxiv_search]
      - name: critic
        goal: Identify weak claims and missing counter-evidence.
        llm: { provider: anthropic, model: claude-sonnet-4-6 }
      - name: editor
        goal: Enforce lab-notebook voice and citation formatting.
        llm: { provider: anthropic, model: claude-sonnet-4-6 }
    tasks:
      - description: Produce a 500-word peer-reviewable brief on the topic.
        expected_output: A 500-word brief with >=5 citations, reviewed by critic, edited by editor.
        role: pi
    verbose: true

safety:
  min_permissions:
    - network:outbound:api.anthropic.com
    - network:outbound:api.openai.com
    - network:outbound:export.arxiv.org
  rate_limit_qps: 5
  cost_limit_usd_daily: 40
  safe_for_auto_spawn: false

env_vars_required:
  - name: ANTHROPIC_API_KEY
    description: Anthropic API key.
    secret: true
  - name: OPENAI_API_KEY
    description: OpenAI API key.
    secret: true

deployment:
  targets: [crewai]

metadata:
  license: proprietary
  author: { name: Research Lab, handle: research-lab, org: Lab }
  source: { type: git, url: https://github.com/research-lab/crew-lab }
  id: com.research-lab.crew-lab
"""},
        {"yaml": """
version: \"1.0\"
name: Plate Atelier
type: workflow
summary: Creative CrewAI atelier crew generating and critiquing plates.
description: >
  Three-role atelier: sketcher drafts a Residual Frequencies plate
  concept, painter renders it in words, critic scores it against the
  design rules. Parallel process — sketcher and critic run
  concurrently after painter.

platforms:
  crewai:
    process: parallel
    roles:
      - name: sketcher
        goal: Draft a Residual Frequencies plate concept in 3 sentences.
        llm: { provider: mistral, model: mistral-medium-latest }
      - name: painter
        goal: Expand the concept into a full lab-notebook caption.
        llm: { provider: mistral, model: mistral-large-latest }
      - name: critic
        goal: Score the caption against the visual-system rules.
        llm: { provider: mistral, model: mistral-medium-latest }
    tasks:
      - description: Sketch a plate concept.
        expected_output: 3-sentence concept.
        role: sketcher
      - description: Write the caption.
        expected_output: Caption in lab-notebook voice.
        role: painter
        context_from: [sketcher]
      - description: Score the caption.
        expected_output: 3-criterion score (frame, ticks, accent).
        role: critic
        context_from: [painter]

safety:
  min_permissions: [network:outbound:api.mistral.ai]
  safe_for_auto_spawn: true

env_vars_required:
  - name: MISTRAL_API_KEY
    description: Mistral API key.
    secret: true

deployment:
  targets: [crewai]

visuals: { palette: parchment }

metadata:
  license: CC-BY-4.0
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/plate-atelier }
  categories: [ai, graphics, writing]
  id: com.plate-studio.plate-atelier
"""},
    ],
}
