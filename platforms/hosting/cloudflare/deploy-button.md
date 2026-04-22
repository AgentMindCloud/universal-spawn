# Cloudflare — Deploy-button recipe

A manifest that declares `platforms.cloudflare` with a
complete `wrangler.toml`-equivalent block is eligible
for the canonical Cloudflare Deploy button. Drop this snippet
into the repository's `README.md` to surface it.

## Markdown

```markdown
[![Deploy to Cloudflare](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=https%3A%2F%2Fgithub.com%2Fyourhandle%2Fyour-worker)
```

## HTML

```html
<a href="https://deploy.workers.cloudflare.com/?url=https%3A%2F%2Fgithub.com%2Fyourhandle%2Fyour-worker">
  <img src="https://deploy.workers.cloudflare.com/button" alt="Deploy to Cloudflare Workers" />
</a>
```

## Parameters

The `deploy.workers.cloudflare.com` endpoint accepts:

- `url` (required) — URL-encoded git repo URL.

Pages deployments use a different button: see the Cloudflare Pages docs. The button above targets Workers.

## Badge style

The universal-spawn project ships a complementary "Spawns on
Cloudflare" badge you can pair with the Deploy button. The badge
verifies against the platform schema at install time; a manifest that
fails `cloudflare-spawn.schema.json` loses the badge.

```markdown
[![Spawns on Cloudflare](https://universal-spawn.dev/badge/cloudflare.svg)](https://universal-spawn.dev/registry/cloudflare)
```
