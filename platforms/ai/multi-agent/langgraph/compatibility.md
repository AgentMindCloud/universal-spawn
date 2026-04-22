# LangGraph compatibility — field-by-field

| universal-spawn v1.0 field | LangGraph behavior |
|---|---|
| `version` | Required. |
| `metadata.id` | Stable key. |
| `name, description` | LangSmith metadata. |
| `type` | `ai-agent`, `workflow`. |
| `safety.*` | Informational. |
| `env_vars_required` | Secret store. |
| `platforms.langgraph.language` | `python`, `typescript`. |
| `platforms.langgraph.entry_graph` | `{file, symbol}` locating the compiled graph. |
| `platforms.langgraph.state_schema_ref` | Path to the state Pydantic / zod schema source. |
| `platforms.langgraph.nodes` | Declared node list. |
| `platforms.langgraph.edges` | Declared edges (static + conditional). |
| `platforms.langgraph.checkpoint` | Checkpoint store settings. |
| `platforms.langgraph.interrupt` | Human-in-the-loop interrupts. |


