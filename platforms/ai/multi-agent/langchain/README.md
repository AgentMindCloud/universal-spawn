# LangChain — universal-spawn platform extension

LangChain is a framework, not a runtime — a manifest that targets LangChain describes how declarative data maps onto a programmatic graph of `Runnable`s. This extension captures entry chains, retriever components, and the provider/model pair LangChain should bind by default.

## What this platform cares about

The language (`python` or `typescript`), the entry chain module path, the provider/model pair, and the retriever spec. The manifest is read by scaffolding tools that emit LangChain code; LangChain itself does not enforce anything at runtime.

## What platform-specific extras unlock

`entry_chain.file` + `entry_chain.symbol` point at the entry `Runnable`. `retriever.kind` names the retriever family (`vector`, `web`, `parent-document`).

## Compatibility table

How core manifest fields map onto this platform:

| Manifest field | LangChain behavior |
|---|---|
| `version` | Required. |
| `name, description` | Used in LangSmith project metadata. |
| `type` | `ai-agent`, `ai-skill`, `workflow`. |
| `safety.cost_limit_usd_daily` | Informational; LangChain delegates cost to the model provider. |
| `env_vars_required` | Staged in LangSmith or the runtime host. |
| `platforms.langchain` | Strict; drives scaffolding. |

### `platforms.langchain` fields

| Field | Purpose |
|---|---|
| `platforms.langchain.language` | `python` or `typescript`. |
| `platforms.langchain.provider` | Model-provider id. |
| `platforms.langchain.model` | Provider-specific model id. |
| `platforms.langchain.entry_chain` | `{file, symbol}` locating the entry Runnable. |
| `platforms.langchain.retriever` | Retriever family + parameters. |
| `platforms.langchain.langsmith_tracing` | Enable LangSmith tracing. |

See [`compatibility.md`](./compatibility.md) for the full field-by-field
map and [`perks.md`](./perks.md) for what this platform could offer
manifests that target it.
