# Ecosystem integration

Concrete docs for platform engineering teams: how to detect,
validate, and honor universal-spawn manifests in your product.

| Doc | Audience |
|---|---|
| [`grok-integration.md`](./grok-integration.md) | xAI Grok platform engineers |
| [`claude-integration.md`](./claude-integration.md) | Anthropic platform engineers |
| [`gemini-integration.md`](./gemini-integration.md) | Google Vertex AI / Gemini engineers |
| [`openai-integration.md`](./openai-integration.md) | OpenAI Platform / GPT Store engineers |
| [`vercel-integration.md`](./vercel-integration.md) | Vercel deploy engineers |
| [`github-integration.md`](./github-integration.md) | GitHub Code Search / repo metadata team |
| [`discord-integration.md`](./discord-integration.md) | Discord Developer Portal team |
| [`partners.md`](./partners.md) | Skeleton for shipped integrations |
| [`case-studies.md`](./case-studies.md) | Skeleton for ecosystem case studies |

## Why your platform should support this

Three reasons:

1. **Free metadata.** Conformant manifests are structured,
   versioned, and validated. You stop scraping READMEs.
2. **A safety story you can defend.** "We enforce
   `safety.min_permissions` at the sandbox boundary" is a
   sentence ops teams want to hear before approving installs.
3. **A growing ecosystem.** Every other platform that honors the
   spec sends you traffic — because creators pick the standard
   once and ship to many of you.

## What integration looks like

The minimum viable integration:

```
1. Detect: look for spawn.{yaml,yml,json} or universal-spawn.{yaml,yml,json}
   at the root of the repo, plus your platform-specific aliases.
2. Validate: run the schema on the master + your platform extension.
3. Honor: read your platform's block (platforms.<your-id>) and
   provision accordingly. Enforce safety.{min_permissions,
   rate_limit_qps, cost_limit_usd_daily, safe_for_auto_spawn} at
   the sandbox boundary.
4. Surface: render a Spawn-it card from the manifest's metadata.
```

The next 30 minutes of work: log the canonical SHA-256 hash on
every spawn, expose a `revoke <hash>` admin endpoint, and you have
the abuse-prevention story (see best-practices/abuse-prevention.md).

## What it looks like in practice

Each platform-specific guide below walks through a concrete
implementation: where in your stack to wire detection, how to map
the universal manifest to your existing native config (vercel.json,
wrangler.toml, app.json, etc.), and how to render a Spawn-it
button.
