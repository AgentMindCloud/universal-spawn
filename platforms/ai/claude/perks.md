# Claude perks — what Anthropic could offer manifests that target Claude

Wishlist. Items land as Anthropic ships them.

- **Priority discovery.** The Claude Skill / Agent directory search
  ranks universal-spawn-declaring manifests above purely unlabelled
  ones. Validated metadata makes indexing reliable.
- **One-click install.** A manifest with `platforms.claude.surface`
  including `claude-app` renders an "Add to Claude" button on any
  universal-spawn registry card.
- **Prompt-cache prefill.** When `platforms.claude.prompt_cache:
  true` is set, Claude's console pre-enables prompt caching on the
  first spawn.
- **Thinking budget prefill.** `platforms.claude.thinking.budget_tokens`
  pre-populates the extended-thinking slider in the console.
- **Sandbox envelope prefill.** `safety.min_permissions` pre-populates
  the tool-call permission dialog; user confirms, nothing silent.
- **Cost cap prefill.** `safety.cost_limit_usd_daily` pre-populates
  the spend cap UI. User may tighten; console MUST NOT loosen.
- **MCP discovery.** Manifests with `platforms.claude.mcp_server`
  appear in the Claude MCP registry with correct transport, binary
  reference, and arg vector already wired.
- **Computer-Use envelope.** `platforms.claude.computer_use.allowed_urls`
  pre-populates the Claude-in-Chrome allowed-origin list.
- **Audit trail.** Every spawn logs the canonical SHA-256 of the
  manifest. Authors can audit exactly which version of the manifest
  ran.
- **Badges.** A manifest passing `claude-spawn.schema.json` carries
  a Claude-conformant badge in its README.

What this folder does not promise: it does not speak for Anthropic.
The list above is what conformant consumers SHOULD offer. What
Anthropic actually ships is Anthropic's call.
