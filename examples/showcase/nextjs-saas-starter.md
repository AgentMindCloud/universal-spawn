# Showcase · `inkwell` — a NextJS SaaS starter

**Use case.** A minimal SaaS starter built on Next.js 15, Postgres,
NextAuth, and Stripe. Deploys to Vercel; sibling Netlify deploy
available for failover.

## The manifest

```yaml
version: "1.0"
name: Inkwell
description: >
  A minimal SaaS starter — Next.js 15 + Postgres + NextAuth +
  Stripe. Deploys to Vercel (primary) and Netlify (failover) from
  the same manifest.
type: web-app
platforms:
  vercel:
    framework: nextjs
    install_command: "pnpm install"
    build_command: "pnpm build"
    output: .next
    node_version: "20"
    regions: [iad1, cdg1]
    env_promotion: [production, preview]
  netlify:
    build_command: "pnpm build"
    publish: ".next"
    node_version: "20"
    env_contexts: [production]
    plugins: [{ package: "@netlify/plugin-nextjs" }]
safety:
  min_permissions: [network:inbound, network:outbound]
  cost_limit_usd_daily: 30
  safe_for_auto_spawn: false
env_vars_required:
  - { name: DATABASE_URL,       secret: true, description: Postgres connection string }
  - { name: NEXTAUTH_SECRET,    secret: true, description: NextAuth signing secret }
  - { name: STRIPE_SECRET_KEY,  secret: true, description: Stripe key }
deployment: { targets: [vercel, netlify] }
metadata:
  license: MIT
  id: com.inkwell.saas-starter
  author: { name: Inkwell, handle: inkwell }
  source: { type: git, url: https://github.com/inkwell/saas-starter }
  categories: [web]
```

## Platforms targeted, and why

- **`vercel`** — primary host; the framework's home turf.
- **`netlify`** — failover. One manifest, two deploys.

## How discovery happens

The README renders both Deploy buttons (Vercel + Netlify). The
universal-spawn registry shows whichever target a viewer's account
is configured for.
