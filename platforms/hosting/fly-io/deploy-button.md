# Fly.io — Deploy-button recipe

A manifest that declares `platforms.fly-io` with a
complete `fly.toml`-equivalent block is eligible
for the canonical Fly.io Deploy button. Drop this snippet
into the repository's `README.md` to surface it.

## Markdown

```markdown
[![Deploy on Fly.io](https://fly.io/static/images/launch/deploy.svg)](https://fly.io/launch?repo=https%3A%2F%2Fgithub.com%2Fyourhandle%2Fyour-project)
```

## HTML

```html
<a href="https://fly.io/launch?repo=https%3A%2F%2Fgithub.com%2Fyourhandle%2Fyour-project">
  <img src="https://fly.io/static/images/launch/deploy.svg" alt="Deploy on Fly.io" />
</a>
```

## Parameters

The Fly launch URL accepts:

- `repo` — URL-encoded git repo URL.
- `name` — suggested app name.
- `region` — primary region (e.g. `iad`, `cdg`, `syd`).

Generators MAY fill `name` from `platforms.fly-io.app` and `region` from `platforms.fly-io.primary_region`.

## Badge style

The universal-spawn project ships a complementary "Spawns on
Fly.io" badge you can pair with the Deploy button. The badge
verifies against the platform schema at install time; a manifest that
fails `fly-io-spawn.schema.json` loses the badge.

```markdown
[![Spawns on Fly.io](https://universal-spawn.dev/badge/fly-io.svg)](https://universal-spawn.dev/registry/fly-io)
```
