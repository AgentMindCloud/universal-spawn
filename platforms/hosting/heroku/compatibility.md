# Heroku compatibility — field-by-field

Heroku already has a native config format
(`app.json`). universal-spawn does not replace it; the two
coexist. A Heroku consumer reads both:

- `app.json` for provider-specific knobs the universal-spawn
  extension does not (yet) model.
- `universal-spawn.yaml` (with `platforms.heroku`) for the
  cross-platform manifest.

The two files **MUST NOT** disagree on fields that appear in both; a
consumer that detects a conflict MUST warn and prefer `universal-spawn.yaml`.

## Side-by-side

### `app.json` (provider-native)

```json
{
  "name": "Your App",
  "description": "Template app.",
  "stack": "heroku-24",
  "buildpacks": [{ "url": "heroku/nodejs" }],
  "formation": {
    "web":    { "quantity": 1, "size": "basic" },
    "worker": { "quantity": 0, "size": "basic" }
  },
  "addons": [{ "plan": "heroku-postgresql:essential-0", "as": "DATABASE" }],
  "env": {
    "SESSION_SECRET": { "description": "Session cookie secret", "generator": "secret" }
  },
  "scripts": { "postdeploy": "npm run migrate" }
}
```

### `universal-spawn.yaml` (platforms.heroku block)

```yaml
platforms:
  heroku:
    stack: heroku-24
    buildpacks: [{ url: heroku/nodejs }]
    formation:
      web: { quantity: 1, size: basic }
      worker: { quantity: 0, size: basic }
    addons:
      - { plan: "heroku-postgresql:essential-0", as: DATABASE }
    scripts: { postdeploy: "npm run migrate" }
    region: us
```

## Field-by-field

| universal-spawn v1.0 field | Heroku behavior |
|---|---|
| `version` | Required. |
| `metadata.id` | Suggested app name. |
| `name, description` | Card. |
| `type` | `web-app`, `api-service`, `container`, `workflow`, `bot`. |
| `safety.*` | Informational. |
| `env_vars_required` | Prompted on Heroku Button deploy. |
| `platforms.heroku.stack` | Heroku stack. |
| `platforms.heroku.buildpacks` | Ordered buildpack list. |
| `platforms.heroku.formation` | Dyno formation. |
| `platforms.heroku.addons` | Managed services. |
| `platforms.heroku.scripts` | Lifecycle scripts. |
| `platforms.heroku.region` | Heroku region. |

## What to keep where

- Use **`app.json`** for env `generator: secret`, `require: true`, `value: X` hints, review-app config, and environment overrides.
- Use **`universal-spawn.yaml`** for the top-level manifest and cross-platform parity.

