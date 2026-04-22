# X (Twitter) — universal-spawn platform extension

X bots are built on the X Developer Platform v2 API and increasingly on Grok-for-X surfaces. A universal-spawn manifest declares the OAuth scopes, the bot account, and (when applicable) cross-links to the Grok extension that powers the AI side.

## What this platform cares about

The OAuth 2.0 scopes the bot needs, the X account handle, the API tier, and the optional Grok cross-link for AI-driven bots.

## Compatibility table

| Manifest field | X (Twitter) behavior |
|---|---|
| `version` | Required. |
| `type` | `bot`, `ai-agent`, `workflow`. |
| `platforms.x-twitter` | Strict. |

### `platforms.x-twitter` fields

| Field | Purpose |
|---|---|
| `platforms.x-twitter.account` | Bot @-handle. |
| `platforms.x-twitter.scopes` | OAuth 2.0 scopes. |
| `platforms.x-twitter.tier` | API tier. |
| `platforms.x-twitter.streams` | Filtered-stream rule files. |
| `platforms.x-twitter.uses_grok` | Routes inference through Grok. |

See [`compatibility.md`](./compatibility.md) for more.

## See also

AI-driven X bots typically pair `platforms.x-twitter` with `platforms.grok` from the AI subtree. See [`../../ai/grok/`](../../ai/grok/) for the model-side surface.
