"""AutoGen (Microsoft) — multi-agent conversation framework."""
from scripts.ai_specs._common import (
    STANDARD_PERKS, enum, str_prop, bool_prop, schema_object,
)

SPEC = {
    "id": "autogen",
    "title": "AutoGen (Microsoft)",
    "location": "multi-agent",

    "lede": (
        "AutoGen runs multi-agent conversations — typed agents that "
        "exchange messages until a termination condition fires. A "
        "manifest declares the agent roster, the group-chat pattern, "
        "the termination condition, and whether user-proxy agents "
        "require human input."
    ),
    "cares": (
        "The pattern (`round-robin`, `selector`, `swarm`, "
        "`nested-chat`), per-agent LLM binding, tool bindings, and "
        "termination condition."
    ),
    "extras": (
        "`termination.max_messages` and `termination.text` compose — "
        "the chat ends when either triggers. `user_proxy.human_input_mode` "
        "controls the interactive gate."
    ),
    "compat_table": [
        ("version", "Required."),
        ("type", "`ai-agent`, `workflow`."),
        ("safety.*", "Informational."),
        ("env_vars_required", "Runtime host."),
        ("platforms.autogen", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("metadata.id", "Stable key."),
        ("name, description", "Chat metadata."),
        ("type", "`ai-agent`, `workflow`."),
        ("safety.*", "Informational."),
        ("env_vars_required", "Secret store."),
        ("platforms.autogen.pattern", "`round-robin`, `selector`, `swarm`, `nested-chat`."),
        ("platforms.autogen.agents", "Typed agent roster."),
        ("platforms.autogen.user_proxy", "User-proxy agent config."),
        ("platforms.autogen.termination", "Termination condition."),
    ],
    "platform_fields": {
        "pattern": "Group-chat pattern.",
        "agents": "Typed agent roster (assistants + user proxies).",
        "user_proxy": "User-proxy agent settings.",
        "termination": "Termination condition (max messages / text trigger).",
    },
    "schema_body": schema_object(
        required=["pattern", "agents"],
        properties={
            "pattern": enum(["round-robin", "selector", "swarm", "nested-chat"]),
            "agents": {
                "type": "array",
                "minItems": 1,
                "items": schema_object(
                    required=["name", "type"],
                    properties={
                        "name": str_prop(pattern=r"^[a-z][a-z0-9_]{0,63}$"),
                        "type": enum(["assistant", "user_proxy", "retrieve_assistant", "conversable"]),
                        "system_message_file": str_prop(),
                        "llm": schema_object(
                            properties={
                                "provider": enum(["openai", "anthropic", "azure-openai", "google", "mistral", "local"]),
                                "model": str_prop(),
                            },
                        ),
                        "tools": {"type": "array", "items": str_prop()},
                    },
                ),
            },
            "user_proxy": schema_object(
                properties={
                    "name": str_prop(),
                    "human_input_mode": enum(["NEVER", "ALWAYS", "TERMINATE"]),
                    "code_execution": bool_prop(False),
                },
            ),
            "termination": schema_object(
                properties={
                    "max_messages": {"type": "integer", "minimum": 1},
                    "text": str_prop(desc="Message substring that terminates the chat when produced."),
                },
            ),
        },
    ),
    "template_yaml": """
version: \"1.0\"
name: AutoGen Template
type: ai-agent
description: Template for an AutoGen-targeted universal-spawn manifest.

platforms:
  autogen:
    pattern: selector
    agents:
      - name: planner
        type: assistant
        llm: { provider: openai, model: gpt-5 }
      - name: coder
        type: assistant
        llm: { provider: openai, model: gpt-5 }
      - name: user
        type: user_proxy
    user_proxy:
      name: user
      human_input_mode: TERMINATE
      code_execution: true
    termination:
      max_messages: 20
      text: \"TERMINATE\"

safety:
  min_permissions: [network:outbound:api.openai.com]
  rate_limit_qps: 3
  cost_limit_usd_daily: 8

env_vars_required:
  - name: OPENAI_API_KEY
    description: OpenAI API key.
    secret: true

deployment:
  targets: [autogen]

metadata:
  license: MIT
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/autogen-template }
""",
    "compatibility_extras": "",
    "perks": STANDARD_PERKS,
    "examples": [
        {"yaml": """
version: \"1.0\"
name: AutoGen Debate
type: workflow
summary: Minimal round-robin two-agent debate.
description: Two assistants debate a claim; terminates at 10 messages.

platforms:
  autogen:
    pattern: round-robin
    agents:
      - name: pro
        type: assistant
        llm: { provider: openai, model: gpt-4o-mini }
      - name: con
        type: assistant
        llm: { provider: openai, model: gpt-4o-mini }
    termination:
      max_messages: 10

safety:
  min_permissions: [network:outbound:api.openai.com]
  safe_for_auto_spawn: true

env_vars_required:
  - name: OPENAI_API_KEY
    description: OpenAI API key.
    secret: true

deployment:
  targets: [autogen]

metadata:
  license: MIT
  author: { name: Debate Co., handle: debate-co }
  source: { type: git, url: https://github.com/debate-co/autogen-debate }
  id: com.debate-co.autogen-debate
"""},
        {"yaml": """
version: \"1.0\"
name: AutoGen Coder Swarm
type: workflow
summary: Full swarm-pattern AutoGen team with planner, coder, tester, reviewer.
description: >
  Coder swarm with a planner, three coders, and a reviewer. Code
  execution enabled for the user-proxy. Terminates on "DONE".

platforms:
  autogen:
    pattern: swarm
    agents:
      - name: planner
        type: assistant
        llm: { provider: anthropic, model: claude-opus-4-7 }
      - name: coder_a
        type: assistant
        llm: { provider: openai, model: gpt-5 }
        tools: [python_repl]
      - name: coder_b
        type: assistant
        llm: { provider: openai, model: gpt-5 }
        tools: [python_repl]
      - name: coder_c
        type: assistant
        llm: { provider: openai, model: gpt-5 }
        tools: [python_repl]
      - name: reviewer
        type: assistant
        llm: { provider: anthropic, model: claude-sonnet-4-6 }
      - name: user
        type: user_proxy
    user_proxy:
      name: user
      human_input_mode: TERMINATE
      code_execution: true
    termination:
      max_messages: 50
      text: \"DONE\"

safety:
  min_permissions:
    - network:outbound:api.openai.com
    - network:outbound:api.anthropic.com
    - fs:read
    - fs:write:/tmp/autogen
  rate_limit_qps: 5
  cost_limit_usd_daily: 40
  safe_for_auto_spawn: false

env_vars_required:
  - name: OPENAI_API_KEY
    description: OpenAI API key.
    secret: true
  - name: ANTHROPIC_API_KEY
    description: Anthropic API key.
    secret: true

deployment:
  targets: [autogen]

metadata:
  license: proprietary
  author: { name: Code Lab, handle: code-lab, org: Lab }
  source: { type: git, url: https://github.com/code-lab/autogen-coder-swarm }
  id: com.code-lab.autogen-coder-swarm
"""},
        {"yaml": """
version: \"1.0\"
name: Parchment Nested Chat
type: ai-agent
summary: Creative nested-chat pattern for a plate-writing salon.
description: >
  Nested-chat: an outer salon director talks with two inner specialist
  chats (typographer, pigment critic). Creative exploration of how
  to structure multi-topic agent conversations.

platforms:
  autogen:
    pattern: nested-chat
    agents:
      - name: director
        type: assistant
        llm: { provider: mistral, model: mistral-large-latest }
      - name: typographer
        type: assistant
        llm: { provider: mistral, model: mistral-medium-latest }
      - name: pigment_critic
        type: assistant
        llm: { provider: mistral, model: mistral-medium-latest }
      - name: user
        type: user_proxy
    user_proxy:
      name: user
      human_input_mode: TERMINATE
    termination: { max_messages: 30, text: \"CURTAIN\" }

safety:
  min_permissions: [network:outbound:api.mistral.ai]
  safe_for_auto_spawn: false

env_vars_required:
  - name: MISTRAL_API_KEY
    description: Mistral API key.
    secret: true

deployment:
  targets: [autogen]

visuals: { palette: parchment }

metadata:
  license: CC-BY-4.0
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/autogen-salon }
  categories: [ai, graphics, writing]
  id: com.plate-studio.autogen-salon
"""},
    ],
}
