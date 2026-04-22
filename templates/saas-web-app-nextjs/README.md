# `saas-web-app-nextjs` template

Next.js SaaS starter manifest. Targets Vercel by default; add a
`platforms.netlify` block for parallel hosting.

## What ships

- `universal-spawn.yaml`
- `vercel.json` — minimal Vercel config alongside the manifest.

## Change before shipping

1. `metadata.author` and `metadata.source.url`.
2. `env_vars_required` — match what your app actually reads.
3. `platforms.vercel.regions` — pick what's right for you.
