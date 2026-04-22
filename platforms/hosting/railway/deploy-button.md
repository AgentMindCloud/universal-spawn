# Railway — Deploy-button recipe

A manifest that declares `platforms.railway` with a
complete `railway.json`-equivalent block is eligible
for the canonical Railway Deploy button. Drop this snippet
into the repository's `README.md` to surface it.

## Markdown

```markdown
[![Deploy on Railway](https://railway.com/button.svg)](https://railway.com/new/template?template=https%3A%2F%2Fgithub.com%2Fyourhandle%2Fyour-project)
```

## HTML

```html
<a href="https://railway.com/new/template?template=https%3A%2F%2Fgithub.com%2Fyourhandle%2Fyour-project">
  <img src="https://railway.com/button.svg" alt="Deploy on Railway" />
</a>
```

## Parameters

The Railway template URL accepts:

- `template` — URL-encoded git repo URL.
- `referralCode` — referral code.
- `plugins` — comma-separated plugin list (pg, redis, …).

Generators MAY fill `plugins` from `platforms.railway.plugins[*].kind`.

## Badge style

The universal-spawn project ships a complementary "Spawns on
Railway" badge you can pair with the Deploy button. The badge
verifies against the platform schema at install time; a manifest that
fails `railway-spawn.schema.json` loses the badge.

```markdown
[![Spawns on Railway](https://universal-spawn.dev/badge/railway.svg)](https://universal-spawn.dev/registry/railway)
```
