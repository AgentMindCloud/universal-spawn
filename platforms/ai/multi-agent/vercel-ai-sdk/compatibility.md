# Vercel AI SDK compatibility — field-by-field

| universal-spawn v1.0 field | Vercel AI SDK behavior |
|---|---|
| `version` | Required. |
| `metadata.id` | Stable key. |
| `name, description` | Card. |
| `type` | `ai-agent`, `ai-skill`, `library`, `web-app`. |
| `safety.*` | Informational. |
| `env_vars_required` | Secrets. |
| `platforms.vercel-ai-sdk.provider` | Default provider id. |
| `platforms.vercel-ai-sdk.model` | Default model id. |
| `platforms.vercel-ai-sdk.tools` | Array of `{name, zod_schema_ref, handler_ref}` tools. |
| `platforms.vercel-ai-sdk.generate_object` | Schema ref for `generateObject`. |
| `platforms.vercel-ai-sdk.stream` | Streaming on/off. |
| `platforms.vercel-ai-sdk.runtime` | `node`, `edge`, `nextjs`. |


