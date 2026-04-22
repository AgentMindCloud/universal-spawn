# Showcase · `nightly-rollups` — a data pipeline on Modal

**Use case.** A daily data-rollup pipeline that aggregates the
previous day's events into Postgres. Runs on Modal's serverless
Python runtime.

## The manifest

```yaml
version: "1.0"
name: Nightly Rollups
description: >
  Daily data-rollup pipeline. Reads events from a Postgres source,
  aggregates them into nightly summaries, writes back to Postgres.
  Runs on Modal at 03:00 UTC.
type: workflow
platforms:
  modal:
    entry_file: rollups.py
    app_name: nightly-rollups
    gpu: none
    image_kind: debian-slim
    secrets: [pg-secret]
safety:
  min_permissions:
    - network:outbound:api.modal.com
    - network:outbound:db.internal.example
  cost_limit_usd_daily: 5
  safe_for_auto_spawn: false
env_vars_required:
  - { name: MODAL_TOKEN_ID,     secret: true, description: Modal token id }
  - { name: MODAL_TOKEN_SECRET, secret: true, description: Modal token secret }
deployment: { targets: [modal] }
metadata:
  license: Apache-2.0
  id: com.example.nightly-rollups
  author: { name: Data Team, handle: data-team, org: Example }
  source: { type: git, url: https://github.com/example/nightly-rollups }
```

## Platforms targeted, and why

- **`modal`** — serverless cron + cheap CPU; no need to babysit a
  worker queue.

## How discovery happens

Internal: discovered through the company's universal-spawn registry,
which crawls every internal repo and surfaces what runs where. The
manifest's safety envelope is what makes the pipeline auditable.
