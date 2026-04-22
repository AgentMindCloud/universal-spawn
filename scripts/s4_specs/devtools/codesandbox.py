"""CodeSandbox — sandboxes + devboxes."""
from scripts.ai_specs._common import enum, str_prop, bool_prop, schema_object


SPEC = {
    "id": "codesandbox",
    "title": "CodeSandbox",
    "lede": (
        "CodeSandbox runs sandboxes (browser-based code editors) and "
        "devboxes (microVMs). A universal-spawn manifest pins the "
        "kind, the entry template, and the optional `.codesandbox/` "
        "config directory."
    ),
    "cares": (
        "The `kind` (`sandbox`, `devbox`), the template id, and the "
        "config directory."
    ),
    "compat_table": [
        ("version", "Required."),
        ("type", "`web-app`, `container`, `workflow`."),
        ("platforms.codesandbox", "Strict."),
    ],
    "compat_table_full": [
        ("version", "Required."),
        ("platforms.codesandbox.kind", "`sandbox`, `devbox`."),
        ("platforms.codesandbox.template", "Template id."),
        ("platforms.codesandbox.config_dir", ".codesandbox directory."),
        ("platforms.codesandbox.preview_port", "Preview port."),
    ],
    "platform_fields": {
        "kind": "`sandbox` or `devbox`.",
        "template": "Template id.",
        "config_dir": ".codesandbox dir.",
        "preview_port": "Preview port.",
    },
    "schema_body": schema_object(
        required=["kind"],
        properties={
            "kind": enum(["sandbox", "devbox"]),
            "template": enum(["node", "vite-react", "vite-vue", "vite-svelte", "next", "remix", "astro", "static", "nextjs", "create-react-app", "custom"]),
            "config_dir": str_prop(),
            "preview_port": {"type": "integer", "minimum": 1, "maximum": 65535},
        },
    ),
    "template_yaml": """
version: "1.0"
name: CodeSandbox Template
type: web-app
description: Template for a CodeSandbox-targeted universal-spawn manifest.

platforms:
  codesandbox:
    kind: sandbox
    template: vite-react
    preview_port: 5173

safety:
  min_permissions: [network:inbound, network:outbound, fs:read, fs:write]

env_vars_required: []

deployment:
  targets: [codesandbox]

metadata:
  license: MIT
  author: { name: Your Name, handle: yourhandle }
  source: { type: git, url: https://github.com/yourhandle/codesandbox-template }
""",
    "native_config_name": ".codesandbox/",
    "native_config_lang": "json",
    "native_config": """
{
  "template": "vite-react",
  "tasks": { "dev": { "command": "pnpm dev", "preview": { "port": 5173 } } }
}
""",
    "universal_excerpt": """
platforms:
  codesandbox:
    kind: sandbox
    template: vite-react
    preview_port: 5173
    config_dir: .codesandbox
""",
    "compatibility_extras": "",
    "examples": {
        "example-1": """
version: "1.0"
name: Plate Sandbox
type: web-app
summary: Minimal CodeSandbox sandbox for a Vite + React demo.
description: Browser-only sandbox.

platforms:
  codesandbox:
    kind: sandbox
    template: vite-react
    preview_port: 5173

safety:
  min_permissions: [network:inbound]
  safe_for_auto_spawn: true

env_vars_required: []

deployment:
  targets: [codesandbox]

metadata:
  license: MIT
  author: { name: Plate Studio, handle: plate-studio }
  source: { type: git, url: https://github.com/plate-studio/codesandbox-plate-demo }
  id: com.plate-studio.codesandbox-plate-demo
""",
        "example-2": """
version: "1.0"
name: Plate Devbox
type: container
summary: Full CodeSandbox devbox running Next.js with custom dev tasks.
description: microVM-backed devbox; persists dependencies between sessions.

platforms:
  codesandbox:
    kind: devbox
    template: next
    config_dir: .codesandbox
    preview_port: 3000

safety:
  min_permissions: [network:inbound, network:outbound, fs:read, fs:write]
  safe_for_auto_spawn: false

env_vars_required:
  - name: DATABASE_URL
    description: Postgres URL.
    secret: true

deployment:
  targets: [codesandbox]

metadata:
  license: Apache-2.0
  author: { name: Stack Co., handle: stack-co }
  source: { type: git, url: https://github.com/stack-co/codesandbox-next-devbox }
  id: com.stack-co.codesandbox-next-devbox
""",
    },
}
