"""Continue — IDE extension (VS Code + JetBrains)."""
from scripts.ai_specs._common import (
    STANDARD_PERKS, enum, str_prop, bool_prop, schema_object,
)

SPEC = {
    "id": "continue",
    "title": "Continue",
    "location": "coding-agents",
    "lede": (
        "Continue is an open-source IDE extension for VS Code and "
        "JetBrains. Configuration lives in `~/.continue/config.yaml`. "
        "A universal-spawn manifest targets Continue by declaring the "
        "provider list, system prompts, context providers, and rule "
        "files."
    ),
    "cares": (
        "The model list (one entry per role — chat, edit, apply, "
        "autocomplete, embed, rerank), context providers, and rule "
        "files."
    ),
    "extras": (
        "`context_providers[]` lists Continue context providers "
        "(`codebase`, `docs`, `diff`, `currentFile`, etc.)."
    ),
    "compat_table": [
        ("version", "Required."),
        ("type", "`extension`, `plugin`, `ai-skill`, `library`."),
        ("safety.*", "Informational."),
        ("env_vars_required", "User env."),
        ("platforms.continue", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("metadata.id", "Stable key."),
        ("name, description", "Shown in Continue's assistant picker."),
        ("type", "`extension`, `plugin`, `ai-skill`, `library`."),
        ("safety.*", "Informational."),
        ("env_vars_required", "User env."),
        ("platforms.continue.models", "Model list keyed by role."),
        ("platforms.continue.system_prompt_file", "Path to the system prompt."),
        ("platforms.continue.context_providers", "Context providers."),
        ("platforms.continue.rules_files", "Rule files (`.continuerules`)."),
        ("platforms.continue.ide", "Target IDEs (`vscode`, `jetbrains`)."),
    ],
    "platform_fields": {
        "models": "Model list by role.",
        "system_prompt_file": "System prompt.",
        "context_providers": "Context providers.",
        "rules_files": "Rule files.",
        "ide": "Target IDEs.",
    },
    "schema_body": schema_object(
        properties={
            "models": {
                "type": "array",
                "items": schema_object(
                    required=["role", "provider", "model"],
                    properties={
                        "role": enum(["chat", "edit", "apply", "autocomplete", "embed", "rerank"]),
                        "provider": enum(["openai", "anthropic", "google", "mistral", "cohere", "together", "fireworks", "ollama", "lmstudio", "groq"]),
                        "model": str_prop(),
                    },
                ),
            },
            "system_prompt_file": str_prop(),
            "context_providers": {
                "type": "array",
                "items": enum(["codebase", "docs", "diff", "currentFile", "open", "git", "terminal", "url", "tree"]),
            },
            "rules_files": {"type": "array", "items": str_prop()},
            "ide": {
                "type": "array",
                "items": enum(["vscode", "jetbrains"]),
            },
        },
    ),
    "template_yaml": """
version: \"1.0\"
name: Continue Template
type: extension
description: Template for a Continue-targeted universal-spawn manifest.

platforms:
  continue:
    models:
      - { role: chat, provider: anthropic, model: claude-sonnet-4-6 }
      - { role: autocomplete, provider: ollama, model: qwen2.5-coder:7b }
      - { role: embed, provider: ollama, model: nomic-embed-text }
    context_providers: [codebase, diff, currentFile, docs]
    rules_files: [.continuerules]
    ide: [vscode, jetbrains]

safety:
  min_permissions: [network:outbound:api.anthropic.com, network:outbound:localhost]
  safe_for_auto_spawn: true

env_vars_required:
  - name: ANTHROPIC_API_KEY
    description: Anthropic key.
    secret: true

deployment:
  targets: [continue]

metadata:
  license: Apache-2.0
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/continue-template }
""",
    "compatibility_extras": "",
    "perks": STANDARD_PERKS,
    "examples": [
        {"yaml": """
version: \"1.0\"
name: Continue Minimal
type: extension
summary: Minimal Continue assistant with one chat model.
description: Single assistant. Anthropic Sonnet. VS Code only.

platforms:
  continue:
    models:
      - { role: chat, provider: anthropic, model: claude-sonnet-4-6 }
    ide: [vscode]

safety:
  min_permissions: [network:outbound:api.anthropic.com]
  safe_for_auto_spawn: true

env_vars_required:
  - name: ANTHROPIC_API_KEY
    description: Anthropic key.
    secret: true

deployment:
  targets: [continue]

metadata:
  license: Apache-2.0
  author: { name: Continue Co., handle: continue-co }
  source: { type: git, url: https://github.com/continue-co/continue-minimal }
  id: com.continue-co.continue-minimal
"""},
        {"yaml": """
version: \"1.0\"
name: Continue Full Stack
type: extension
summary: Full Continue assistant with chat, edit, apply, autocomplete, embed, rerank roles.
description: >
  Full six-role assistant. Chat/edit on Claude Opus. Apply on Sonnet.
  Autocomplete + embed on Ollama. Rerank on Cohere. Works in both
  VS Code and JetBrains.

platforms:
  continue:
    models:
      - { role: chat, provider: anthropic, model: claude-opus-4-7 }
      - { role: edit, provider: anthropic, model: claude-opus-4-7 }
      - { role: apply, provider: anthropic, model: claude-sonnet-4-6 }
      - { role: autocomplete, provider: ollama, model: qwen2.5-coder:7b }
      - { role: embed, provider: ollama, model: nomic-embed-text }
      - { role: rerank, provider: cohere, model: rerank-english-v3.0 }
    system_prompt_file: .continue/system.md
    context_providers: [codebase, diff, currentFile, docs, git, terminal]
    rules_files: [.continuerules]
    ide: [vscode, jetbrains]

safety:
  min_permissions:
    - network:outbound:api.anthropic.com
    - network:outbound:api.cohere.com
    - network:outbound:localhost
  cost_limit_usd_daily: 15
  safe_for_auto_spawn: false

env_vars_required:
  - name: ANTHROPIC_API_KEY
    description: Anthropic key.
    secret: true
  - name: COHERE_API_KEY
    description: Cohere key.
    secret: true

deployment:
  targets: [continue]

metadata:
  license: Apache-2.0
  author: { name: DevEx Co., handle: devex-co, org: DevEx }
  source: { type: git, url: https://github.com/devex-co/continue-full-stack }
  id: com.devex-co.continue-full-stack
"""},
        {"yaml": """
version: \"1.0\"
name: Continue Parchment Assistant
type: extension
summary: Creative Continue assistant tuned for the Residual Frequencies design system.
description: >
  Continue assistant scoped to SVG/CSS edits. Chat on Mistral-large,
  autocomplete off. Rules file teaches parchment palette, letter-spacing,
  tick grammar.

platforms:
  continue:
    models:
      - { role: chat, provider: mistral, model: mistral-large-latest }
    system_prompt_file: .continue/parchment.md
    context_providers: [codebase, currentFile]
    rules_files: [.continuerules]
    ide: [vscode]

safety:
  min_permissions: [network:outbound:api.mistral.ai]
  safe_for_auto_spawn: true

env_vars_required:
  - name: MISTRAL_API_KEY
    description: Mistral key.
    secret: true

deployment:
  targets: [continue]

visuals: { palette: parchment }

metadata:
  license: CC-BY-4.0
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/continue-parchment }
  categories: [ai, graphics, devtools]
  id: com.plate-studio.continue-parchment
"""},
    ],
}
