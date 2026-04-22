# `platforms/ai/` — AI destinations

This directory is the registry of AI-flavoured platform extensions for
universal-spawn v1.0. Each subdirectory is self-contained: a developer
landing in `platforms/ai/<id>/` can use it without reading anything
else.

Extensions here all follow the same structure:

```
<id>/
├── README.md                 # 3-6 paragraphs. What the platform
│                             # cares about, what perks it offers,
│                             # how the universal manifest maps to
│                             # it, what platform-specific extras
│                             # unlock. Ends with a compatibility
│                             # table.
├── <id>-spawn.yaml           # Canonical platform-specific manifest
├── <id>-spawn.schema.json    # Draft-07 extension: allOf → [master
│                             # v1.0 schema, platform additions]
├── compatibility.md          # Field-by-field map, universal ↔ platform
├── perks.md                  # What a platform could/should offer
│                             # for manifests that target it
└── examples/
    ├── example-1.yaml        # minimal realistic
    ├── example-2.yaml        # full-featured
    └── example-3.yaml        # creative / unusual
```

All schema extensions are **draft-07** and use `allOf` against
`spec/v1.0/universal-spawn.schema.json` — they never redefine shared
fields. All examples validate against the platform schema (which in
turn validates against the master).

## Capability matrix (30+ platforms)

Enforcement key:
**E** — platform enforces the field at the sandbox/runtime boundary.
**U** — platform uses the field (UI, billing, discovery) but does not
gate spawning on it.
**—** — platform ignores the field.

### AI model providers

| Id              | Vendor       | Primary use          | `min_permissions` | `cost_limit_usd_daily` | `tool-call` | `mcp` | `streaming` |
|-----------------|--------------|----------------------|:-----------------:|:----------------------:|:-----------:|:-----:|:-----------:|
| [grok](./grok)  | xAI          | Chat + agents (hero) | E | E | E | U | E |
| [claude](./claude) | Anthropic | Messages, Skills, Agents | E | E | E | E | E |
| [openai](./openai) | OpenAI    | Responses, Custom GPTs, Agents | E | E | E | U | E |
| [gemini](./gemini) | Google    | Gemini API, Vertex, Gems | E | E | E | U | E |
| [llama](./llama) | Meta        | Llama Stack + Llama Guard | E | U | E | U | E |
| [mistral](./mistral) | Mistral | La Plateforme + agents | U | U | E | — | E |
| [groq-cloud](./groq-cloud) | Groq | Fast inference      | U | U | E | — | E |
| [perplexity](./perplexity) | Perplexity | Sonar + Pplx API | U | U | E | — | E |
| [together-ai](./together-ai) | Together | Open-model inference | U | U | E | — | E |
| [fireworks](./fireworks) | Fireworks | Inference + tool calls | U | U | E | — | E |
| [replicate](./replicate) | Replicate | Model hosting     | U | U | — | — | E |
| [huggingface](./huggingface) | HF | Inference Endpoints + Models + Spaces | U | U | — | — | E |
| [anthropic-mcp](./anthropic-mcp) | MCP | Model Context Protocol server | E | — | — | E | E |
| [cohere](./cohere) | Cohere    | Command R + Compass  | U | U | E | — | E |
| [ai21](./ai21)   | AI21       | Jamba + Maestro      | U | U | E | — | E |

### Multi-agent frameworks

| Id                                            | Language     | Run model                    |
|-----------------------------------------------|--------------|-------------------------------|
| [langchain](./multi-agent/langchain)          | Python / TS  | Chains + agents               |
| [crewai](./multi-agent/crewai)                | Python       | Role-based crews              |
| [autogen](./multi-agent/autogen)              | Python       | Multi-agent conversations     |
| [langgraph](./multi-agent/langgraph)          | Python / TS  | Graph state machines          |
| [semantic-kernel](./multi-agent/semantic-kernel) | C# / Python | Skills + planners           |
| [litellm](./multi-agent/litellm)              | Python       | Provider-agnostic router      |
| [mastra](./multi-agent/mastra)                | TypeScript   | Agent + workflow runtime      |
| [vercel-ai-sdk](./multi-agent/vercel-ai-sdk)  | TypeScript   | Streaming + generateObject    |

### Coding agents

| Id                                          | Kind             |
|---------------------------------------------|------------------|
| [cursor](./coding-agents/cursor)            | IDE (fork)       |
| [windsurf](./coding-agents/windsurf)        | IDE (fork)       |
| [aider](./coding-agents/aider)              | CLI pair-prog   |
| [continue](./coding-agents/continue)        | IDE extension    |
| [cline](./coding-agents/cline)              | IDE extension    |
| [claude-code](./coding-agents/claude-code)  | CLI              |

### Local runtimes

| Id                                   | Host shape     |
|--------------------------------------|----------------|
| [ollama](./local/ollama)             | Local daemon   |
| [lm-studio](./local/lm-studio)       | Desktop + API  |
| [llamacpp](./local/llamacpp)         | Library + CLI  |
| [vllm](./local/vllm)                 | OpenAI-compatible server |

## Special notes

- **`grok/`** is the canonical cross-platform companion to
  [`AgentMindCloud/grok-install`](https://github.com/AgentMindCloud/grok-install)
  v2.14. See `grok/README.md` for the aliasing rules.
- **`anthropic-mcp/`** is separate from `claude/` because MCP is a
  distinct interop layer that applies across Claude, any MCP host,
  and some third-party consumers.
- **`coding-agents/claude-code/`** is the CLI tool; `claude/` is the
  Claude API surface. They differ.
- **`groq-cloud/`** (Groq, the inference company) is NOT the same as
  **`grok/`** (xAI's model). The spelling is deliberate.

## Adding an AI platform

1. Open a [new-platform issue](../../.github/ISSUE_TEMPLATE/new_platform.yml).
2. Create `platforms/ai/<id>/` with all six required files plus at
   least three examples.
3. The schema **MUST** be `allOf` against
   `spec/v1.0/universal-spawn.schema.json`.
4. Update the capability matrix above.
5. Two maintainer approvals.

## Validation

Everything under `platforms/ai/**` is exercised by the session's
validation sweep — see `scripts/validate-ai.py`. A single failing
example blocks merge.
