# LangGraph — universal-spawn platform extension

LangGraph is a graph runtime on top of LangChain. Agents and tools are nodes; edges are routing decisions; the run replays a typed state dictionary. A manifest captures the graph topology so scaffolding can emit the bindings.

## What this platform cares about

The nodes, the edges (typed conditionals), the state schema reference, and the checkpoint store so the graph survives restarts.

## What platform-specific extras unlock

`checkpoint.store` picks the checkpoint backend (`memory`, `sqlite`, `postgres`, `redis`). `interrupt.before[]` and `interrupt.after[]` mark nodes where the graph pauses for a human.

## Compatibility table

How core manifest fields map onto this platform:

| Manifest field | LangGraph behavior |
|---|---|
| `version` | Required. |
| `type` | `ai-agent`, `workflow`. |
| `safety.*` | Informational. |
| `env_vars_required` | Runtime host + checkpoint store. |
| `platforms.langgraph` | Strict. |

### `platforms.langgraph` fields

| Field | Purpose |
|---|---|
| `platforms.langgraph.language` | `python` or `typescript`. |
| `platforms.langgraph.entry_graph` | `{file, symbol}` locating the compiled graph. |
| `platforms.langgraph.state_schema_ref` | Path to the state schema module. |
| `platforms.langgraph.nodes` | Declared node list. |
| `platforms.langgraph.edges` | Static + conditional edges. |
| `platforms.langgraph.checkpoint` | Checkpoint store (`memory`, `sqlite`, `postgres`, `redis`). |
| `platforms.langgraph.interrupt` | `{before[], after[]}` human-in-the-loop interrupts. |

See [`compatibility.md`](./compatibility.md) for the full field-by-field
map and [`perks.md`](./perks.md) for what this platform could offer
manifests that target it.
