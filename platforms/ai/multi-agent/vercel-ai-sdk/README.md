# Vercel AI SDK — universal-spawn platform extension

The Vercel AI SDK is a provider-agnostic library for TypeScript apps: `streamText`, `generateObject` (typed via Zod), `tool`, and a common tool-calling loop. A manifest declares the default provider/model, the tools, the Zod schema refs for structured output, and the deployment runtime.

## What this platform cares about

The provider + model default, the array of tools with Zod schema paths, and whether `generateObject` is wired up with its own schema.

## What platform-specific extras unlock

`generate_object.schema_ref` points at a Zod schema module. `stream` defaults to true; set false for non-streaming one-shot calls.

## Compatibility table

How core manifest fields map onto this platform:

| Manifest field | Vercel AI SDK behavior |
|---|---|
| `version` | Required. |
| `type` | `ai-agent`, `ai-skill`, `library`, `web-app`. |
| `safety.*` | Informational. |
| `env_vars_required` | Host runtime (typically Vercel). |
| `platforms.vercel-ai-sdk` | Strict. |

### `platforms.vercel-ai-sdk` fields

| Field | Purpose |
|---|---|
| `platforms.vercel-ai-sdk.provider` | Default provider (`openai`, `anthropic`, `google`, `mistral`, `cohere`, `xai`, `groq`). |
| `platforms.vercel-ai-sdk.model` | Default model id. |
| `platforms.vercel-ai-sdk.tools` | Array of tools (`{name, zod_schema_ref, handler_ref}`). |
| `platforms.vercel-ai-sdk.generate_object` | Zod schema ref for `generateObject`. |
| `platforms.vercel-ai-sdk.stream` | Streaming mode. |
| `platforms.vercel-ai-sdk.runtime` | `node`, `edge`, or `nextjs`. |

See [`compatibility.md`](./compatibility.md) for the full field-by-field
map and [`perks.md`](./perks.md) for what this platform could offer
manifests that target it.
