# Examples

Every file in this directory is a complete, schema-valid
universal-spawn manifest. They are ordered from smallest to most
exhaustive.

| File                                     | Demonstrates                                |
|------------------------------------------|---------------------------------------------|
| `minimal.spawn.yaml`                     | The smallest manifest that validates.       |
| `full.spawn.yaml`                        | Every field of the schema in use.           |
| `ai-agent.spawn.yaml`                    | A tool-calling AI agent.                    |
| `web-app.spawn.yaml`                     | A Next.js app with host extensions.         |
| `creative-tool.spawn.yaml`               | A Figma plugin.                             |
| `game-mod.spawn.yaml`                    | A Unity mod with scene entrypoint.          |
| `hardware-device.spawn.yaml`             | Firmware for an embedded device.            |
| `cross-platform.spawn.yaml`              | One manifest, six spawn targets.            |

To validate any example locally:

```bash
npx ajv-cli validate \
  -s ../spec/v1.0.0/manifest.schema.json \
  -d minimal.spawn.yaml --spec=draft2020
```

CI enforces the invariant that every file here validates.
