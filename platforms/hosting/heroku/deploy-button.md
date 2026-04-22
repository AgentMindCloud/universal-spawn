# Heroku — Deploy-button recipe

A manifest that declares `platforms.heroku` with a
complete `app.json`-equivalent block is eligible
for the canonical Heroku Deploy button. Drop this snippet
into the repository's `README.md` to surface it.

## Markdown

```markdown
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https%3A%2F%2Fgithub.com%2Fyourhandle%2Fyour-project)
```

## HTML

```html
<a href="https://heroku.com/deploy?template=https%3A%2F%2Fgithub.com%2Fyourhandle%2Fyour-project">
  <img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy" />
</a>
```

## Parameters

The Heroku Button URL accepts:

- `template` (required) — URL-encoded git repo URL.

Heroku reads `app.json` at the root of the repo to build the deploy form; the env vars prompted come from `app.json`'s `env` map.

## Badge style

The universal-spawn project ships a complementary "Spawns on
Heroku" badge you can pair with the Deploy button. The badge
verifies against the platform schema at install time; a manifest that
fails `heroku-spawn.schema.json` loses the badge.

```markdown
[![Spawns on Heroku](https://universal-spawn.dev/badge/heroku.svg)](https://universal-spawn.dev/registry/heroku)
```
