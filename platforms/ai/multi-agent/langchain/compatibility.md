# LangChain compatibility — field-by-field

| universal-spawn v1.0 field | LangChain behavior |
|---|---|
| `version` | Required. |
| `metadata.id` | Stable key. |
| `name, description` | LangSmith project metadata. |
| `type` | `ai-agent`, `ai-skill`, `workflow`. |
| `safety.*` | Informational. |
| `env_vars_required` | Staged in LangSmith / runtime host. |
| `platforms.langchain.language` | `python` or `typescript`. |
| `platforms.langchain.provider` | `openai`, `anthropic`, `google`, `mistral`, `cohere`, `together`, `local`. |
| `platforms.langchain.model` | Provider-specific model id. |
| `platforms.langchain.entry_chain` | Entry chain module + symbol. |
| `platforms.langchain.retriever` | Retriever configuration. |
| `platforms.langchain.langsmith_tracing` | Enable LangSmith tracing. |

## Declarative → programmatic

A scaffolding tool reads this manifest and emits LangChain bindings: a `ChatModel` for `provider`+`model`, a retriever for `retriever.*`, and imports `entry_chain.file`'s `entry_chain.symbol` as the graph entrypoint. The manifest is declarative; the generated code is programmatic. The round-trip is not two-way — code changes that stray from the manifest require regenerating the manifest.
