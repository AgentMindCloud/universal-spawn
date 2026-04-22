# Platform Compatibility Matrix (v1.0.0)

This matrix shows which core manifest fields each supported platform
honors when it spawns a creation. A cell is one of:

- **R** — required by the platform before it will spawn.
- **U** — used by the platform.
- **—** — ignored by the platform.

Platform extensions (under `platforms.<id>`) may tighten, relax, or
extend these rules; see each platform folder for details.

| Field                  | claude | gemini | openai | vercel | netlify | unity | figma | discord | huggingface |
|------------------------|:------:|:------:|:------:|:------:|:-------:|:-----:|:-----:|:-------:|:-----------:|
| `spawn_version`        |   R    |   R    |   R    |   R    |    R    |   R   |   R   |    R    |      R      |
| `id`                   |   R    |   R    |   R    |   R    |    R    |   R   |   R   |    R    |      R      |
| `name`                 |   R    |   R    |   R    |   R    |    R    |   R   |   R   |    R    |      R      |
| `kind`                 |   R    |   R    |   R    |   R    |    R    |   R   |   R   |    R    |      R      |
| `description`          |   R    |   R    |   R    |   U    |    U    |   U   |   U   |    U    |      U      |
| `summary`              |   U    |   U    |   U    |   U    |    U    |   U   |   U   |    U    |      U      |
| `license`              |   R    |   R    |   R    |   U    |    U    |   U   |   U   |    U    |      R      |
| `author`               |   R    |   R    |   R    |   U    |    U    |   U   |   U   |    U    |      R      |
| `source`               |   R    |   R    |   R    |   R    |    R    |   U   |   U   |    U    |      R      |
| `homepage`             |   U    |   U    |   U    |   U    |    U    |   U   |   U   |    U    |      U      |
| `icon`                 |   U    |   U    |   U    |   U    |    U    |   U   |   U   |    U    |      U      |
| `hero_plate`           |   U    |   U    |   U    |   U    |    U    |   —   |   U   |    U    |      U      |
| `keywords`             |   U    |   U    |   U    |   U    |    U    |   U   |   U   |    U    |      U      |
| `categories`           |   U    |   U    |   U    |   —    |    —    |   U   |   U   |    U    |      U      |
| `runtime`              |   U    |   U    |   U    |   U    |    U    |   R   |   U   |    U    |      U      |
| `dependencies`         |   U    |   U    |   U    |   U    |    U    |   U   |   U   |    U    |      U      |
| `entrypoints`          |   R    |   R    |   R    |   R    |    R    |   R   |   R   |    R    |      U      |
| `env_vars_required`    |   U    |   U    |   U    |   R    |    R    |   U   |   U   |    U    |      U      |
| `min_permissions`      |   R    |   R    |   R    |   U    |    U    |   U   |   R   |    R    |      U      |
| `rate_limit_qps`       |   U    |   U    |   U    |   U    |    U    |   —   |   —   |    U    |      —      |
| `cost_limit_usd_daily` |   U    |   U    |   U    |   U    |    U    |   —   |   —   |    —    |      U      |
| `safe_for_auto_spawn`  |   U    |   U    |   U    |   U    |    U    |   U   |   U   |    U    |      U      |
| `data_residency`       |   U    |   U    |   U    |   U    |    U    |   —   |   —   |    —    |      U      |
| `compat.grok_install`  |   U    |   U    |   U    |   —    |    —    |   —   |   —   |    —    |      U      |
| `compat.openapi`       |   U    |   U    |   U    |   U    |    U    |   —   |   —   |    —    |      U      |
| `compat.dockerfile`    |   U    |   U    |   U    |   U    |    U    |   —   |   —   |    —    |      U      |
| `signatures`           |   U    |   U    |   U    |   —    |    —    |   —   |   —   |    U    |      U      |

## Entrypoint-kind coverage

| Entrypoint `kind`  | claude | gemini | openai | vercel | netlify | unity | figma | discord | huggingface |
|--------------------|:------:|:------:|:------:|:------:|:-------:|:-----:|:-----:|:-------:|:-----------:|
| `http`             |   ✓    |   ✓    |   ✓    |   ✓    |    ✓    |   —   |   —   |    ✓    |      ✓      |
| `cli`              |   ✓    |   ✓    |   ✓    |   —    |    —    |   —   |   —   |    —    |      ✓      |
| `websocket`        |   ✓    |   ✓    |   ✓    |   ✓    |    ✓    |   —   |   —   |    ✓    |      —      |
| `stdio`            |   ✓    |   —    |   —    |   —    |    —    |   —   |   —   |    —    |      —      |
| `script`           |   —    |   —    |   —    |   ✓    |    ✓    |   ✓   |   ✓   |    —    |      ✓      |
| `container`        |   —    |   —    |   —    |   ✓    |    ✓    |   —   |   —   |    —    |      ✓      |
| `webhook`          |   —    |   —    |   —    |   ✓    |    ✓    |   —   |   —   |    ✓    |      ✓      |
| `scene`            |   —    |   —    |   —    |   —    |    —    |   ✓   |   —   |    —    |      —      |
| `slash-command`    |   ✓    |   —    |   —    |   —    |    —    |   —   |   —   |    ✓    |      —      |
| `tool-call`        |   ✓    |   ✓    |   ✓    |   —    |    —    |   —   |   —   |    —    |      —      |
| `ui-panel`         |   —    |   —    |   —    |   —    |    —    |   —   |   ✓   |    —    |      —      |

## Notes on enforcement

- **claude**, **gemini**, **openai** all enforce `min_permissions` against
  their tool-calling / code-execution sandboxes.
- **vercel** and **netlify** ignore `min_permissions` because their build
  pipelines grant a fixed permission envelope; they use
  `env_vars_required` instead to block builds missing secrets.
- **unity** and **figma** enforce `min_permissions` only for the runtime
  portion (plugin sandboxes, scene scripts). Editor-time operations run
  outside the spawn envelope.
- **discord** enforces `min_permissions` by mapping them to bot intents
  and scopes.
- **huggingface** stages creations as repositories; the `license` field
  determines visibility tier.
