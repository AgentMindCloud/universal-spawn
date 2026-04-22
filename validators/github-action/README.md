# `universal-spawn validate` — GitHub Action

Composite action that installs the Node CLI and validates the
manifest at the repo root on every push / pull request.

## Quick start

`.github/workflows/validate.yml`:

```yaml
name: validate
on: [push, pull_request]
jobs:
  manifest:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: AgentMindCloud/universal-spawn/validators/github-action@v1
```

## Inputs

| Name | Default | Description |
|---|---|---|
| `path` | auto-detect | Manifest path. Auto-detects `universal-spawn.{yaml,yml,json}` or `spawn.{yaml,yml,json}` at the repo root. |
| `node-version` | `20` | Node version installed for the validator. |
| `fail-on-warning` | `false` | Treat warnings as errors. Useful in `strict` repos. |

## Examples

### Validate a non-default path

```yaml
- uses: AgentMindCloud/universal-spawn/validators/github-action@v1
  with:
    path: subproject/universal-spawn.yaml
```

### Strict mode

```yaml
- uses: AgentMindCloud/universal-spawn/validators/github-action@v1
  with:
    fail-on-warning: 'true'
```

### Matrix: validate every monorepo child

```yaml
strategy:
  matrix:
    project: [api, web, mobile]
steps:
  - uses: actions/checkout@v4
  - uses: AgentMindCloud/universal-spawn/validators/github-action@v1
    with:
      path: ${{ matrix.project }}/universal-spawn.yaml
```

## What it actually does

1. Installs the universal-spawn Node CLI globally
   (`npm i -g universal-spawn`).
2. Resolves the manifest path (input → first match from the canonical
   filename list).
3. Runs `universal-spawn validate <path>` (or `... --strict` if
   `fail-on-warning: true`).
4. Exits non-zero on validation failure.

The action is intentionally a thin wrapper around the CLI so that
`act` reproduces it locally and so that what runs in CI is the same
binary you can run on your laptop.
