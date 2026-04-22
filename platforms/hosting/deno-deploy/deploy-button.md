# Deno Deploy — Deploy-button recipe

A manifest that declares `platforms.deno-deploy` with a
complete `deno.json`-equivalent block is eligible
for the canonical Deno Deploy Deploy button. Drop this snippet
into the repository's `README.md` to surface it.

## Markdown

```markdown
[![Deploy to Deno](https://deno.com/button)](https://dash.deno.com/new?url=https%3A%2F%2Fgithub.com%2Fyourhandle%2Fyour-project)
```

## HTML

```html
<a href="https://dash.deno.com/new?url=https%3A%2F%2Fgithub.com%2Fyourhandle%2Fyour-project">
  <img src="https://deno.com/button" alt="Deploy to Deno" />
</a>
```

## Parameters

The `dash.deno.com/new` endpoint accepts:

- `url` — URL-encoded git repo URL.
- `entrypoint` — pre-fill the entry module path.


## Badge style

The universal-spawn project ships a complementary "Spawns on
Deno Deploy" badge you can pair with the Deploy button. The badge
verifies against the platform schema at install time; a manifest that
fails `deno-deploy-spawn.schema.json` loses the badge.

```markdown
[![Spawns on Deno Deploy](https://universal-spawn.dev/badge/deno-deploy.svg)](https://universal-spawn.dev/registry/deno-deploy)
```
