# Mastra — universal-spawn platform extension

Mastra is a TypeScript framework combining an agent runtime, a workflow engine, and first-class integrations with the Vercel AI SDK. A manifest declares the agents, the workflows, and the memory backend. Typed state, streaming by default.

## What this platform cares about

The agents array (each with model + tools + memory), the workflows array (each a typed state machine), and the memory backend (`libsql`, `pg`, `upstash-redis`).

## What platform-specific extras unlock

`telemetry.otlp_endpoint_env` sends OpenTelemetry traces to the named endpoint. `deploy.runtime` picks `nextjs`, `vercel-edge`, `cloudflare`, or `node`.

## Compatibility table

How core manifest fields map onto this platform:

| Manifest field | Mastra behavior |
|---|---|
| `version` | Required. |
| `type` | `ai-agent`, `workflow`. |
| `safety.*` | Informational. |
| `env_vars_required` | Runtime host secrets. |
| `platforms.mastra` | Strict. |

### `platforms.mastra` fields

| Field | Purpose |
|---|---|
| `platforms.mastra.agents` | Agents array (name, model, tools, memory). |
| `platforms.mastra.workflows` | Workflows array (name, entry step). |
| `platforms.mastra.memory` | Memory backend. |
| `platforms.mastra.telemetry` | OpenTelemetry endpoint. |
| `platforms.mastra.deploy` | Deployment runtime (`nextjs`, `vercel-edge`, `cloudflare`, `node`). |

See [`compatibility.md`](./compatibility.md) for the full field-by-field
map and [`perks.md`](./perks.md) for what this platform could offer
manifests that target it.
