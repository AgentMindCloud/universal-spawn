# Netlify — Deploy-button recipe

A manifest that declares `platforms.netlify` with a
complete `netlify.toml`-equivalent block is eligible
for the canonical Netlify Deploy button. Drop this snippet
into the repository's `README.md` to surface it.

## Markdown

```markdown
[![Deploy to Netlify](https://www.netlify.com/img/deploy/button.svg)](https://app.netlify.com/start/deploy?repository=https%3A%2F%2Fgithub.com%2Fyourhandle%2Fyour-project)
```

## HTML

```html
<a href="https://app.netlify.com/start/deploy?repository=https%3A%2F%2Fgithub.com%2Fyourhandle%2Fyour-project">
  <img src="https://www.netlify.com/img/deploy/button.svg" alt="Deploy to Netlify" />
</a>
```

## Parameters

The Netlify deploy link accepts:

- `repository` (required) — URL-encoded git repo URL.
- `base` — sub-directory inside the repo.
- `branch` — branch to deploy.
- `site_name` — suggested site slug.
- `env` — env vars to prompt the user for.

Generators MAY fill `env` from `env_vars_required[*].name`.

## Badge style

The universal-spawn project ships a complementary "Spawns on
Netlify" badge you can pair with the Deploy button. The badge
verifies against the platform schema at install time; a manifest that
fails `netlify-spawn.schema.json` loses the badge.

```markdown
[![Spawns on Netlify](https://universal-spawn.dev/badge/netlify.svg)](https://universal-spawn.dev/registry/netlify)
```
