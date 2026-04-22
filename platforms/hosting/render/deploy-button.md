# Render — Deploy-button recipe

A manifest that declares `platforms.render` with a
complete `render.yaml`-equivalent block is eligible
for the canonical Render Deploy button. Drop this snippet
into the repository's `README.md` to surface it.

## Markdown

```markdown
[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https%3A%2F%2Fgithub.com%2Fyourhandle%2Fyour-project)
```

## HTML

```html
<a href="https://render.com/deploy?repo=https%3A%2F%2Fgithub.com%2Fyourhandle%2Fyour-project">
  <img src="https://render.com/images/deploy-to-render-button.svg" alt="Deploy to Render" />
</a>
```

## Parameters

The Render deploy URL accepts:

- `repo` — URL-encoded git repo URL.

Everything else is read from `render.yaml` at the root of the repo.

## Badge style

The universal-spawn project ships a complementary "Spawns on
Render" badge you can pair with the Deploy button. The badge
verifies against the platform schema at install time; a manifest that
fails `render-spawn.schema.json` loses the badge.

```markdown
[![Spawns on Render](https://universal-spawn.dev/badge/render.svg)](https://universal-spawn.dev/registry/render)
```
