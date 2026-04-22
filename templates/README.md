# Templates

Drop-in starting points. Each subfolder is a self-contained template:
copy it into a new repo, edit the placeholder fields, validate, ship.

| When you want to ship… | Template |
|---|---|
| The smallest valid manifest | [`minimal-safe/`](./minimal-safe) |
| An X reply bot powered by Grok | [`ai-agent-x-reply-bot/`](./ai-agent-x-reply-bot) |
| A Discord bot built on an LLM | [`ai-agent-discord-bot/`](./ai-agent-discord-bot) |
| A multi-source research agent | [`ai-agent-research/`](./ai-agent-research) |
| An agentic coding assistant | [`ai-agent-coding/`](./ai-agent-coding) |
| A Next.js / SvelteKit / Astro SaaS | [`saas-web-app-{nextjs,sveltekit,astro}/`](./) |
| A Unity asset, Godot project, Roblox experience, itch.io web build | [`game-…/`](./) |
| A Jupyter / Colab / HF Space notebook | [`notebook-…/`](./) |
| A 3D asset pack, Figma kit, Notion template, Obsidian vault | [`creative-…/`](./) |
| A Chrome / Firefox extension | [`browser-extension-…/`](./) |
| A Discord / Telegram / Slack bot | [`bot-…/`](./) |
| A Python / Node / Rust / Go CLI | [`cli-tool-…/`](./) |
| An npm package or PyPI package | [`{npm,pypi}-package/`](./) |
| A Figma plugin, VS Code extension, or MCP server | [`figma-plugin/`](./figma-plugin), [`vscode-extension/`](./vscode-extension), [`mcp-server/`](./mcp-server) |
| A course lesson | [`course-lesson/`](./course-lesson) |
| Arduino / Raspberry Pi firmware | [`hardware-…/`](./) |
| **The grok-install compat showcase** | [`x-native-agent-grok-compat/`](./x-native-agent-grok-compat) |

## How to use a template

```bash
# 1) Copy the folder you want into your new repo's root.
cp -r templates/ai-agent-x-reply-bot/* my-new-repo/

# 2) Edit universal-spawn.yaml — every field marked "Replace…".
# 3) Validate.
universal-spawn validate

# 4) Commit and ship.
```

## Quality gate

Every template's `universal-spawn.yaml` validates against the v1.0
master schema. CI runs `universal-spawn validate` over each one.
