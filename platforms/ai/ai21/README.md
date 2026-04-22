# AI21 — universal-spawn platform extension

AI21 ships the Jamba family of long-context hybrid-Mamba models plus Maestro, their orchestration layer. The extension handles both: Jamba for inference, Maestro for plan-then-execute workflows.

## What this platform cares about

The Jamba model id, the context-window target (Jamba goes to 256k), whether Maestro orchestration is on, and the Maestro plan-level cost cap.

## What platform-specific extras unlock

`maestro.plan_file` points at a declarative plan; `maestro.max_steps` bounds the plan-execute loop.

## Compatibility table

How core manifest fields map onto this platform:

| Manifest field | AI21 behavior |
|---|---|
| `version` | Required. |
| `name, description` | Shown on the AI21 Studio card. |
| `type` | `ai-agent`, `ai-skill`, `ai-model`, `workflow`. |
| `safety.cost_limit_usd_daily` | Advisory; AI21 enforces at workspace. |
| `env_vars_required` | AI21 secret store. |
| `platforms.ai21` | Strict. |

### `platforms.ai21` fields

| Field | Purpose |
|---|---|
| `platforms.ai21.model` | Jamba variant id. |
| `platforms.ai21.tools` | Function tools. |
| `platforms.ai21.maestro` | Maestro plan registration. |
| `platforms.ai21.context_tokens` | Target context-window length. |
| `platforms.ai21.response_format` | `text` or `json_object`. |

See [`compatibility.md`](./compatibility.md) for the full field-by-field
map and [`perks.md`](./perks.md) for what this platform could offer
manifests that target it.
