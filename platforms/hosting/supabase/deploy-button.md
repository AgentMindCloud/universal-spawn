# Supabase — Deploy-button recipe

A manifest that declares `platforms.supabase` with a
complete `supabase/config.toml`-equivalent block is eligible
for the canonical Supabase Deploy button. Drop this snippet
into the repository's `README.md` to surface it.

## Markdown

```markdown
[![Deploy to Supabase](https://supabase.com/docs/img/deploy-to-supabase.svg)](https://supabase.com/dashboard/new?templateUrl=https%3A%2F%2Fgithub.com%2Fyourhandle%2Fyour-project)
```

## HTML

```html
<a href="https://supabase.com/dashboard/new?templateUrl=https%3A%2F%2Fgithub.com%2Fyourhandle%2Fyour-project">
  <img src="https://supabase.com/docs/img/deploy-to-supabase.svg" alt="Deploy to Supabase" />
</a>
```

## Parameters

The Supabase dashboard new-project URL accepts:

- `templateUrl` — URL-encoded git repo URL.
- `orgId` — target organization id.
- `region` — region slug.

The template repo's `supabase/config.toml` and `universal-spawn.yaml` jointly drive provisioning.

## Badge style

The universal-spawn project ships a complementary "Spawns on
Supabase" badge you can pair with the Deploy button. The badge
verifies against the platform schema at install time; a manifest that
fails `supabase-spawn.schema.json` loses the badge.

```markdown
[![Spawns on Supabase](https://universal-spawn.dev/badge/supabase.svg)](https://universal-spawn.dev/registry/supabase)
```
