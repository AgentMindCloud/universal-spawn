# Showcase · `lab-crew` — a research agent using CrewAI

**Use case.** A four-role research crew (PI, researcher, critic,
editor) that produces peer-reviewable briefs on a topic. Uses Opus
for the PI, Sonnet for the rest.

## The manifest

```yaml
version: "1.0"
name: Lab Crew
description: >
  CrewAI research crew. PI delegates to researcher, critic, and
  editor. Hierarchical process. Produces a 500-word peer-reviewable
  brief on the topic.
type: workflow
platforms:
  crewai:
    process: hierarchical
    roles:
      - { name: pi,         goal: Direct the lab to a peer-reviewable brief, llm: { provider: anthropic, model: claude-opus-4-7 }, allow_delegation: true }
      - { name: researcher, goal: Surface citeable primary sources,         llm: { provider: anthropic, model: claude-sonnet-4-6 }, tools: [web_search, arxiv_search] }
      - { name: critic,     goal: Identify weak claims,                     llm: { provider: anthropic, model: claude-sonnet-4-6 } }
      - { name: editor,     goal: Enforce lab-notebook voice + citations,  llm: { provider: anthropic, model: claude-sonnet-4-6 } }
    tasks:
      - { description: Produce a 500-word brief with >=5 citations, expected_output: 500-word brief, role: pi }
    verbose: true
safety:
  min_permissions:
    - network:outbound:api.anthropic.com
    - network:outbound:export.arxiv.org
    - model:call:claude-opus-4-7
  rate_limit_qps: 5
  cost_limit_usd_daily: 40
  safe_for_auto_spawn: false
env_vars_required:
  - { name: ANTHROPIC_API_KEY, secret: true, description: Anthropic key }
deployment: { targets: [crewai] }
metadata:
  license: Apache-2.0
  id: com.lab-crew.research
  author: { name: Research Lab, handle: research-lab }
  source: { type: git, url: https://github.com/research-lab/crewai-lab }
  categories: [ai, research]
```

## Platforms targeted, and why

- **`crewai`** — the runtime. The role-based crew model maps
  cleanly onto how the team actually works.

## How discovery happens

Internal: the lab's repo registry surfaces this manifest and renders
a "Run Lab Crew" panel that sets `topic`, kicks the workflow off,
and shows W&B traces.
