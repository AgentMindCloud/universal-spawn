# `minimal-safe` template

The smallest universal-spawn manifest that validates and follows the
spec's safety defaults.

## What it ships

- `universal-spawn.yaml` — four required fields plus a single empty
  `platforms` block to satisfy the master schema's anyOf clause.
- `safety.safe_for_auto_spawn: false` (the default) so the first
  spawn always asks for human confirmation.

## What to change before you ship

| Field | What to put |
|---|---|
| `name` | Your project's display name. No emoji. |
| `description` | One paragraph (10–500 chars). First sentence stands alone. |
| `type` | One of the schema enum values. `web-app` is a safe default. |
| `metadata.author` | You / your org. |
| `metadata.source.url` | The canonical git URL once you push. |
| `platforms.<id>` | Add a real platform extension when you've picked one. |

## Validate

```bash
universal-spawn validate
```
