# Vercel — Deploy-button recipe

A manifest that declares `platforms.vercel` with a
complete `vercel.json`-equivalent block is eligible
for the canonical Vercel Deploy button. Drop this snippet
into the repository's `README.md` to surface it.

## Markdown

```markdown
[![Deploy to Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fyourhandle%2Fyour-project)
```

## HTML

```html
<a href="https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fyourhandle%2Fyour-project">
  <img src="https://vercel.com/button" alt="Deploy to Vercel" />
</a>
```

## Parameters

The Vercel clone URL accepts the following params:

- `repository-url` (required) — URL-encoded git repo URL.
- `project-name` — suggested project name.
- `repository-name` — suggested repo name at destination.
- `env` — comma-separated env var names to prompt for.
- `envDescription` — blurb shown above the env form.
- `envLink` — link to docs explaining the env vars.

Generators MAY fill `env` from `env_vars_required[*].name`.

## Badge style

The universal-spawn project ships a complementary "Spawns on
Vercel" badge you can pair with the Deploy button. The badge
verifies against the platform schema at install time; a manifest that
fails `vercel-spawn.schema.json` loses the badge.

```markdown
[![Spawns on Vercel](https://universal-spawn.dev/badge/vercel.svg)](https://universal-spawn.dev/registry/vercel)
```
