"""StackBlitz — WebContainer-powered in-browser dev."""
from scripts.ai_specs._common import enum, str_prop, bool_prop, schema_object


SPEC = {
    "id": "stackblitz",
    "title": "StackBlitz",
    "lede": (
        "StackBlitz runs Node.js in the browser via WebContainers. A "
        "universal-spawn manifest pins the project starter, the "
        "WebContainer node version, and the auto-open file."
    ),
    "cares": (
        "The starter id, the entry file, the auto-open file, and the "
        "Node.js version that should boot."
    ),
    "compat_table": [
        ("version", "Required."),
        ("type", "`web-app`, `library`, `cli-tool`."),
        ("platforms.stackblitz", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("platforms.stackblitz.starter", "StackBlitz starter id."),
        ("platforms.stackblitz.node_version", "Node version to boot."),
        ("platforms.stackblitz.open_file", "File to open at first load."),
        ("platforms.stackblitz.terminal_command", "Initial terminal command."),
        ("platforms.stackblitz.embed_view", "Embed view (`editor`, `preview`, `both`)."),
    ],
    "platform_fields": {
        "starter": "Starter id.",
        "node_version": "Node version.",
        "open_file": "Auto-open file.",
        "terminal_command": "Initial terminal command.",
        "embed_view": "Embed view mode.",
    },
    "schema_body": schema_object(
        properties={
            "starter": enum(["node", "vite", "angular", "react", "vue", "svelte", "nextjs", "remix", "astro", "static"]),
            "node_version": str_prop(pattern=r"^[0-9]+(\.[0-9]+)*$"),
            "open_file": str_prop(),
            "terminal_command": str_prop(),
            "embed_view": enum(["editor", "preview", "both"]),
        },
    ),
    "template_yaml": """
version: "1.0"
name: StackBlitz Template
type: web-app
description: Template for a StackBlitz-targeted universal-spawn manifest.

platforms:
  stackblitz:
    starter: vite
    node_version: "20"
    open_file: src/main.ts
    terminal_command: "pnpm dev"
    embed_view: both

safety:
  min_permissions: [network:inbound, network:outbound]

env_vars_required: []

deployment:
  targets: [stackblitz]

metadata:
  license: MIT
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/stackblitz-template }
""",
    "native_config_name": ".stackblitzrc",
    "native_config_lang": "json",
    "native_config": """
{
  "installDependencies": true,
  "startCommand": "pnpm dev",
  "env": { "NODE_VERSION": "20" }
}
""",
    "universal_excerpt": """
platforms:
  stackblitz:
    starter: vite
    node_version: "20"
    open_file: src/main.ts
    terminal_command: "pnpm dev"
""",
    "compatibility_extras": "",
    "examples": {
        "example-1": """
version: "1.0"
name: Plate Vite Sandbox
type: web-app
summary: Minimal StackBlitz Vite project.
description: Browser-only Vite sandbox.

platforms:
  stackblitz:
    starter: vite
    node_version: "20"
    open_file: index.html
    terminal_command: "pnpm dev"
    embed_view: both

safety:
  min_permissions: [network:inbound]
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [stackblitz]

metadata:
  license: MIT
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/stackblitz-vite-plate }
  id: com.plate-studio.stackblitz-vite-plate
""",
        "example-2": """
version: "1.0"
name: Tutorial Workspace
type: web-app
summary: Full StackBlitz tutorial workspace with auto-opened README.
description: Astro starter; auto-opens the lesson README; embeds preview-only mode.

platforms:
  stackblitz:
    starter: astro
    node_version: "20"
    open_file: src/pages/lesson-01.md
    terminal_command: "pnpm dev"
    embed_view: preview

safety:
  min_permissions: [network:inbound]
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [stackblitz]

metadata:
  license: CC-BY-4.0
  author: { name: Tutorial Co., handle: tutorial-co }
  source: { type: git, url: https://github.com/tutorial-co/stackblitz-astro-tutorial }
  id: com.tutorial-co.stackblitz-astro-tutorial
""",
    },
}
