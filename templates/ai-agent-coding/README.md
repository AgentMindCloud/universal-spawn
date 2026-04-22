# `ai-agent-coding` template

Agentic coding assistant manifest — pairs Claude Opus with the
filesystem, git, and a tight tool envelope. Designed to be invoked
from Claude Code or any subagent host.

## Change before shipping

1. Trim `safety.min_permissions` to the smallest set you actually need.
2. `metadata.author` and source URL.

## Validate

```bash
universal-spawn validate
```
