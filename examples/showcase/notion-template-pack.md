# Showcase · `clinical-notes` — a Notion template pack

**Use case.** A Notion template pack for clinical research notes —
study log, hypothesis tracker, citation database. Distributed for
free. The author wants one URL anyone can click to duplicate the
pack into their own workspace.

## The manifest

```yaml
version: "1.0"
name: Clinical Notes Pack
description: >
  A Notion template pack for clinical research notes — study log,
  hypothesis tracker, citation database. Free; one URL duplicates
  the entire pack into the viewer's workspace.
type: design-template
platforms:
  notion:
    page_url: "https://notion.so/clinical-notes/abcdef0123456789abcdef0123456789"
    page_id: "abcdef0123456789abcdef0123456789"
    kind: workspace-pack
safety: { safe_for_auto_spawn: true }
env_vars_required: []
deployment: { targets: [notion] }
visuals: { palette: parchment }
metadata:
  license: CC-BY-4.0
  id: com.clinical-notes.pack
  author: { name: Clinical Notes, handle: clinical-notes }
  source: { type: git, url: https://github.com/clinical-notes/template-pack }
  categories: [productivity, research]
```

## Platforms targeted, and why

- **`notion`** — the only place the pack actually lives; the URL is
  what enables one-click duplication. There's no code surface here.

## How discovery happens

A consumer crawling `*.spawn.yaml` files surfaces this pack. The
universal-spawn registry card renders a "Duplicate to your Notion"
button using `platforms.notion.page_url`; the button takes the user
straight to Notion's own duplicate flow.
