# CrewAI — universal-spawn platform extension

CrewAI models a multi-agent system as a crew — a set of roles, each with a goal and a backstory, working a sequence or parallel set of tasks. A universal-spawn manifest lets you declare the crew shape: who's in it, what tools each role has, and how tasks flow.

## What this platform cares about

The crew roster, per-role LLM binding, each role's tool list, and the process flow (`sequential`, `hierarchical`, `parallel`).

## What platform-specific extras unlock

`roles[].tools[]` lists the tools a specific role can use. `tasks[].expected_output` captures the declarative success criterion CrewAI uses for the task's Pydantic validation.

## Compatibility table

How core manifest fields map onto this platform:

| Manifest field | CrewAI behavior |
|---|---|
| `version` | Required. |
| `name, description` | Crew metadata. |
| `type` | `ai-agent`, `workflow`. |
| `safety.*` | Informational. |
| `env_vars_required` | Runtime host credential store. |
| `platforms.crewai` | Strict. |

### `platforms.crewai` fields

| Field | Purpose |
|---|---|
| `platforms.crewai.process` | Crew process: `sequential`, `hierarchical`, or `parallel`. |
| `platforms.crewai.roles` | Array of role definitions (name, goal, backstory, llm, tools). |
| `platforms.crewai.tasks` | Array of task definitions (description, expected_output, role). |
| `platforms.crewai.verbose` | Enable verbose CrewAI logging. |

See [`compatibility.md`](./compatibility.md) for the full field-by-field
map and [`perks.md`](./perks.md) for what this platform could offer
manifests that target it.
