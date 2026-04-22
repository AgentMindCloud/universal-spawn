# AutoGen (Microsoft) — universal-spawn platform extension

AutoGen runs multi-agent conversations — typed agents that exchange messages until a termination condition fires. A manifest declares the agent roster, the group-chat pattern, the termination condition, and whether user-proxy agents require human input.

## What this platform cares about

The pattern (`round-robin`, `selector`, `swarm`, `nested-chat`), per-agent LLM binding, tool bindings, and termination condition.

## What platform-specific extras unlock

`termination.max_messages` and `termination.text` compose — the chat ends when either triggers. `user_proxy.human_input_mode` controls the interactive gate.

## Compatibility table

How core manifest fields map onto this platform:

| Manifest field | AutoGen (Microsoft) behavior |
|---|---|
| `version` | Required. |
| `type` | `ai-agent`, `workflow`. |
| `safety.*` | Informational. |
| `env_vars_required` | Runtime host. |
| `platforms.autogen` | Strict. |

### `platforms.autogen` fields

| Field | Purpose |
|---|---|
| `platforms.autogen.pattern` | Group-chat pattern. |
| `platforms.autogen.agents` | Typed agent roster (assistants + user proxies). |
| `platforms.autogen.user_proxy` | User-proxy agent settings. |
| `platforms.autogen.termination` | Termination condition (max messages / text trigger). |

See [`compatibility.md`](./compatibility.md) for the full field-by-field
map and [`perks.md`](./perks.md) for what this platform could offer
manifests that target it.
