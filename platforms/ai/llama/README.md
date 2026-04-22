# Llama (Meta) — universal-spawn platform extension

Meta's Llama family (Llama 3.3, Llama 4) is distributed through Llama Stack — a reference set of inference APIs that any vendor can host. This extension covers a manifest that targets a Llama Stack endpoint (self-hosted, Together, Groq, Fireworks, and so on) and optionally engages Llama Guard for input/output safety classification.

## What this platform cares about

Llama Stack consumers care about three things: the model variant (`llama-3.3-70b-instruct`, `llama-4-scout`, `llama-4-maverick`), the Llama-Stack-compatible endpoint URL, and the Llama Guard policy file if content moderation is on. The declared `min_permissions` are enforced only when the consumer runs its own sandbox; many Llama Stack deployments delegate that to the hosting vendor.

## What platform-specific extras unlock

`llama_guard.policy_ref` points at a policy document that Llama Guard loads before the first turn. `endpoint_url` pins a specific Llama Stack server; omit it to let the consumer pick.

## Compatibility table

How core manifest fields map onto this platform:

| Manifest field | Llama (Meta) behavior |
|---|---|
| `version` | Required `"1.0"`. |
| `name, description` | Shown on the Llama Stack server's model card. |
| `type` | Accepts `ai-agent`, `ai-skill`, `ai-model`. |
| `safety.min_permissions` | Enforced when the consumer sandboxes its own inference host. |
| `safety.cost_limit_usd_daily` | Informational; most Llama Stack deployments bill through the hosting vendor. |
| `env_vars_required` | Staged into the consumer's credential store. |
| `platforms.llama` | Strict; see table below. |

### `platforms.llama` fields

| Field | Purpose |
|---|---|
| `platforms.llama.model` | Llama variant (`llama-3.3-70b-instruct`, `llama-4-scout`, …). |
| `platforms.llama.endpoint_url` | Pin a specific Llama Stack server. |
| `platforms.llama.tools` | OpenAI-shaped function tools. |
| `platforms.llama.llama_guard` | Policy file + enforcement level. |
| `platforms.llama.quantization` | Weight quantization hint. |

See [`compatibility.md`](./compatibility.md) for the full field-by-field
map and [`perks.md`](./perks.md) for what this platform could offer
manifests that target it.
