# Platforms

Each subdirectory here describes how a specific platform consumes a
universal-spawn manifest. A folder contains:

- `README.md` — narrative overview.
- `<id>-spawn.yaml` — template manifest tuned for this platform.
- `schema.extension.json` — strict JSON Schema for the
  `platforms.<id>` object, with `additionalProperties: false`.
- `compatibility.md` — which core fields the platform honors and how.
- `examples/` — at least two complete manifests that validate against
  both the master schema and this extension schema.

## Supported

| Id             | Platform        | Folder                               |
|----------------|-----------------|---------------------------------------|
| `claude`       | Anthropic Claude | [claude/](claude)                   |
| `gemini`       | Google Gemini    | [gemini/](gemini)                   |
| `openai`       | OpenAI           | [openai/](openai)                   |
| `vercel`       | Vercel           | [vercel/](vercel)                   |
| `netlify`      | Netlify          | [netlify/](netlify)                 |
| `unity`        | Unity            | [unity/](unity)                     |
| `figma`        | Figma            | [figma/](figma)                     |
| `discord`      | Discord          | [discord/](discord)                 |
| `huggingface`  | Hugging Face     | [huggingface/](huggingface)         |

## Adding a platform

See [`../CONTRIBUTING.md`](../CONTRIBUTING.md#adding-a-platform). The
short version: open a proposal issue, then submit a PR that creates a
folder with all five required files plus two validating examples.

## Extension schema conventions

- `$schema` must be `https://json-schema.org/draft/2020-12/schema`.
- `$id` must be `https://universal-spawn.org/platforms/<id>/v1.0.0/schema.extension.json`.
- `additionalProperties: false` at every level. Platform extensions are
  the precise shape the platform reads; unknown keys are an error.
- Every property has a `description`. Every enum value is documented.
