# `universal/` — creator-facing reference files

This directory holds the single files a creator is most likely to copy
into their own repository.

| File                           | For                                                  |
|--------------------------------|-------------------------------------------------------|
| [`universal-spawn.yaml`](./universal-spawn.yaml) | Annotated reference. Start here.      |
| [`universal-spawn.json`](./universal-spawn.json) | Same content, JSON form.              |
| [`universal-spawn.toml`](./universal-spawn.toml) | Same content, TOML form.              |
| [`aliases.md`](./aliases.md)   | Accepted filenames in discovery order.                |
| [`cheatsheet.md`](./cheatsheet.md) | One-page creator reference.                      |

All three manifest files describe the **same** data model. If they
disagree, the YAML form is the source of truth in this directory;
`universal-spawn.json` and `universal-spawn.toml` are generated from
it so they stay in lockstep. Tooling should accept whichever form the
author commits.

## Copy-paste workflow

1. Copy [`universal-spawn.yaml`](./universal-spawn.yaml) to the root
   of your repository.
2. Fill in `name`, `description`, `type`, `metadata`, and remove any
   fields that don't apply.
3. If you target specific platforms (Claude, Vercel, etc.), add the
   corresponding `platforms.<id>` block. See
   [`../platforms/`](../platforms/) for each one's extension schema
   and worked examples.
4. Validate:

   ```bash
   npx ajv-cli validate --all-errors --spec=draft7 -c ajv-formats \
     -s https://universal-spawn.dev/spec/v1.0/universal-spawn.schema.json \
     -d universal-spawn.yaml
   ```

5. Commit.

## Discovery

A consumer scanning your repository looks for the manifest in a
fixed order. See [`aliases.md`](./aliases.md) for the full list.
In 95% of cases the file should be named `universal-spawn.yaml` and
live at the root.

## How universal + platform-specific combine

You can ship both a universal manifest and a platform-specific one in
the same repository (for example, `universal-spawn.yaml` plus
`vercel.json` or `.claude/skill.yaml`). In that case:

- The universal manifest carries cross-platform fields (description,
  safety envelope, metadata, env var declarations).
- The platform-specific file carries platform-exclusive options
  (Vercel's `headers`, `rewrites`, `crons`; Claude's skill body;
  etc.).
- The platform reads its own file first; the universal-spawn
  consumer fills in the rest.

Do not duplicate overlapping fields in both. When overlap is
unavoidable, the platform-specific file wins for that platform.
