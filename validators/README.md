# Validators

The universal-spawn standard ships in five validator delivery modes so
authors and platforms can pick whatever fits their workflow:

| Folder | Mode | Use when |
|---|---|---|
| [`cli/python/`](./cli/python) | Python CLI (`universal-spawn`) | You're already in a Python toolchain, you want a `pre-commit` hook, or you want to embed the validator in a Python platform consumer. |
| [`cli/node/`](./cli/node) | Node CLI (`npx universal-spawn`) | You're in a JS/TS toolchain. Same commands as the Python CLI, AJV-backed. |
| [`online/index.html`](./online/index.html) | Single-file HTML page | You want to paste a manifest and see results without installing anything. Self-contained, no build step. |
| [`schemas/`](./schemas) | IDE autocomplete | Wire `yaml.schemas` (VS Code) / JSON-schema source URLs (JetBrains, neovim) so creators get autocomplete + inline validation while writing. |
| [`pre-commit/`](./pre-commit) | git pre-commit hook | Block commits that contain an invalid manifest. |
| [`github-action/`](./github-action) | Composite GitHub Action | Validate every PR / push in CI. |

## Source of truth

All five validators consume the **same** schemas from `spec/v1.0/` and
the per-platform extensions under `platforms/<subtree>/<id>/<id>-spawn.schema.json`.
A manifest that passes one mode passes the others.

## CLI command surface (Python + Node share)

```
universal-spawn validate [PATH]      # default: ./universal-spawn.yaml
universal-spawn init [--type TYPE]   # write a starter manifest
universal-spawn migrate [PATH]       # lift legacy v1.0.0 spawn.yaml → v1.0
```

## Quality gates

- `cd validators/cli/python && uv run pytest`  — at least 10 cases, all pass.
- `cd validators/cli/node && npx vitest run`   — at least 10 cases, all pass.
- `validators/online/index.html` opens in any modern browser, paste a
  manifest, see validation results live. No network fetches required
  for the bundled v1.0 schema.
- `validators/pre-commit/hook.sh` blocks commits with an invalid manifest.
- `validators/github-action/action.yml` runs the Node CLI on every PR.
