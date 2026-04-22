# Showcase · `mcp-github-pro` — an MCP server

**Use case.** A Model Context Protocol server that exposes GitHub
repositories, PRs, and issues as MCP resources, plus a small set of
mutating tools (open PR, add comment, merge PR, close issue).

## The manifest

```yaml
version: "1.0"
name: MCP GitHub Pro
description: >
  An MCP server exposing GitHub repos / PRs / issues as resources,
  plus mutating tools for opening PRs, commenting, merging, and
  closing issues. Compatible with every major MCP host.
type: extension
platforms:
  anthropic-mcp:
    transport: http
    url: "http://localhost:7811/mcp"
    resources:
      - { uri_template: "github://{owner}/{repo}",         description: GitHub repository }
      - { uri_template: "github://{owner}/{repo}/pull/{n}", description: Pull request }
      - { uri_template: "github://{owner}/{repo}/issue/{n}", description: Issue }
    tools:
      - { name: open_pr,     description: Open a pull request }
      - { name: merge_pr,    description: Merge a pull request }
      - { name: add_comment, description: Add a comment to a PR or issue }
      - { name: close_issue, description: Close an issue }
    hosts: [claude-desktop, claude-code, cursor, windsurf, zed]
safety:
  min_permissions: [network:outbound:api.github.com, network:inbound]
  safe_for_auto_spawn: false
env_vars_required:
  - { name: GITHUB_TOKEN, secret: true, description: GitHub token with repo scope }
deployment: { targets: [mcp] }
metadata:
  license: Apache-2.0
  id: com.mcp-tooling.github-pro
  author: { name: MCP Tooling, handle: mcp-tooling }
  source: { type: git, url: https://github.com/mcp-tooling/mcp-github-pro }
  categories: [devtools]
```

## Platforms targeted, and why

- **`anthropic-mcp`** — host-neutral. The same manifest works for
  Claude Desktop, Cursor, Windsurf, and Zed.

## How discovery happens

Listed on the MCP registry. Hosts read the `hosts[]` array to
determine compatibility before offering install.
