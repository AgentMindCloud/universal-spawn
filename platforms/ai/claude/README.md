# Claude (Anthropic) — universal-spawn platform extension

Claude is Anthropic's family of models: Opus 4.7 (`claude-opus-4-7`),
Sonnet 4.6 (`claude-sonnet-4-6`), and Haiku 4.5
(`claude-haiku-4-5-20251001`). This extension maps a universal-spawn
v1.0 manifest onto the surfaces Anthropic ships: the Messages API,
Claude Code (the CLI), Claude.ai (web / mobile, including Skills,
Projects, and the Chrome extension), and any MCP-compatible host.

The extension covers five shapes a creation can take on Claude:

1. **Tool** — a callable function exposed via the Messages API
   `tools` parameter.
2. **Skill** — a Claude.ai / Claude Code skill stored under
   `.claude/skills/` with its own YAML header.
3. **Subagent** — an agent launched via the Claude Agent SDK or
   Claude Code's Agent tool.
4. **MCP server** — an MCP server the host connects to. See also
   [`../anthropic-mcp/`](../anthropic-mcp/) for the standalone MCP
   extension.
5. **Computer-use** — a skill that operates a browser or desktop
   sandbox via the Computer-Use API, including the Claude-in-Chrome
   integration.

The extension schema is strict (`additionalProperties: false`). It
composes with the master v1.0 schema via `allOf`; it never redefines
`version`, `name`, `description`, or `type`.

## Perks Claude honors

- `safety.min_permissions` — mapped 1-to-1 onto the tool and code-
  execution sandboxes. A permission not declared is a permission not
  granted.
- `safety.cost_limit_usd_daily` — enforced as a hard ceiling at the
  API key / organisation scope.
- `safety.rate_limit_qps` — advisory for outbound tool calls; hard
  for the Messages API itself.
- `env_vars_required` — staged into the credential store; missing
  required, non-optional secrets block the first spawn.
- `metadata.source.commit` — pinned for audit when the creation is
  installed from git.

## Claude-in-Chrome and Computer Use

The `claude.computer_use` block turns a manifest into a
computer-using agent. It declares the `viewport`, `allowed_urls`,
and `max_actions_per_turn`. Claude-in-Chrome reads the same block
when it imports the creation as a managed extension.

## MCP

An MCP server is declared with `claude.mcp_server`:

```yaml
platforms:
  claude:
    mcp_server:
      transport: stdio
      ref: bin/mcp-server
```

See [`../anthropic-mcp/`](../anthropic-mcp/) for the full MCP
extension when a creation wants to advertise itself to *any* MCP
host (not just Claude).

## Compatibility table

| Manifest field                 | Claude behavior                                                     |
|--------------------------------|----------------------------------------------------------------------|
| `version`                      | Required, literal `"1.0"`.                                          |
| `name`, `description`, `summary` | Shown on the skill / agent card and in Claude Code's `/` picker.  |
| `type`                         | Accepts `ai-agent`, `ai-skill`, `ai-model`, `cli-tool`, `workflow`.  |
| `safety.min_permissions`       | Enforced on the tool-calling and code-execution sandboxes.           |
| `safety.rate_limit_qps`        | Best-effort on outbound tool calls.                                  |
| `safety.cost_limit_usd_daily`  | Hard ceiling at org / key scope.                                     |
| `safety.safe_for_auto_spawn`   | Controls the first-run confirmation gate.                            |
| `env_vars_required`            | Staged into the credential store.                                    |
| `platforms.claude.surface[*]`  | Restricts which Anthropic surfaces may spawn the creation.           |
| `platforms.claude.tools[*]`    | Registered via the Messages API `tools` parameter.                   |
| `platforms.claude.mcp_server`  | Registered as an MCP server on the host.                             |
| `platforms.claude.computer_use`| Sandbox envelope for computer-using agents.                          |
| `platforms.claude.thinking`    | Extended-thinking budget recommendation.                             |
| `platforms.claude.prompt_cache`| Enables prompt caching for recurring context.                        |
| Other `platforms.*`            | Ignored.                                                             |
