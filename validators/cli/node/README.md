# `universal-spawn` — Node CLI

AJV-backed JS implementation of the universal-spawn validator + CLI.
Same surface and exit codes as the Python CLI.

## Install + use

```bash
# One-shot via npx (no install)
npx universal-spawn validate

# Global install
npm i -g universal-spawn
universal-spawn validate

# Validate a specific file
universal-spawn validate apps/api/universal-spawn.yaml

# Validate including platform extensions
universal-spawn validate --platform-schemas-dir platforms/

# Treat warnings as failures
universal-spawn validate --strict

# Write a starter manifest
universal-spawn init --type minimal           # → universal-spawn.yaml
universal-spawn init --type ai-agent --force

# Lift legacy v1.0.0 spawn.yaml → v1.0
universal-spawn migrate spawn.yaml --out universal-spawn.yaml
```

## API

```js
import { validate, validateFile } from "universal-spawn";

const result = validate({ version: "1.0", /* ... */ });
if (!result.ok) {
  for (const e of result.errors) console.error(e);
}
```

## Tests

```bash
cd validators/cli/node
npm install
npx vitest run
```

12 cases cover the master schema, platform-extension validation, the
CLI surface, and the platforms-or-deployment requirement.

## What it bundles

The package ships the v1.0 master schema as a sibling JSON file
(`v1.0.schema.json`). Platform extension schemas are not bundled —
pass `--platform-schemas-dir` to the CLI or `platformSchemasDir` to
`validateFile()`.
