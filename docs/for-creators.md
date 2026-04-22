# For creators — author a strong manifest

A "strong" manifest is one a registry can show, a platform can
spawn, and an ops team can defend in review. This page distills
the patterns that hold up in production.

## The four required fields

Every manifest has these. Get them right.

| Field | Rules |
|---|---|
| `version` | Always `"1.0"` for v1 manifests. Don't guess; the schema enforces. |
| `name` | Display name. No emoji. 1–80 chars. Reads naturally aloud. |
| `description` | One paragraph (10–500 chars). First sentence stands alone. Plain prose, no lists, no markdown. |
| `type` | One enum value. Pick the one a new user will expect. |

Plus at least one of `platforms.<id>` or `deployment.targets[]`.

A manifest with just these is technically valid. Don't ship one
this thin in production — keep going.

## What separates a "good enough" manifest from a strong one

### 1. A real safety envelope

```yaml
safety:
  min_permissions:
    - network:outbound:api.anthropic.com
    - model:call:claude-opus-4-7
  rate_limit_qps: 3
  cost_limit_usd_daily: 15
  safe_for_auto_spawn: false
```

All four fields. Concrete hosts in `min_permissions` (no
wildcards, no bare `network:outbound`). Numbers picked from real
measurement, not guessed. `safe_for_auto_spawn: false` unless
you're sure.

See [`best-practices/secrets-and-permissions.md`](../best-practices/secrets-and-permissions.md)
and [`best-practices/rate-cost-limits.md`](../best-practices/rate-cost-limits.md).

### 2. Honest `env_vars_required`

```yaml
env_vars_required:
  - name: ANTHROPIC_API_KEY
    description: Anthropic key with Opus 4.7 access.
    secret: true
  - name: GITHUB_TOKEN
    description: Optional — used only when fetching private repo metadata.
    secret: true
    required: false
```

Each entry has a useful `description`. Secrets are flagged.
Optional vars are explicit.

### 3. Stable `metadata.id`

```yaml
metadata:
  id: com.parchment-studio.inkwell
```

Reverse-DNS, lower-case. Pick once, never change. See
[`best-practices/naming-conventions.md`](../best-practices/naming-conventions.md).

### 4. Pinned `metadata.source.commit` (for releases)

```yaml
metadata:
  source:
    type: git
    url: https://github.com/parchment-studio/inkwell
    commit: a1b2c3d4e5f6
```

Pin the commit a third party should reproduce. Branch alone is
not reproducible.

### 5. Useful `metadata.keywords[]`

```yaml
metadata:
  keywords: [saas, nextjs, vercel, postgres, nextauth]
```

Lower-case, kebab-case. Words a user would actually search for.

### 6. A `metadata.author` that reads like a credit line

```yaml
metadata:
  author:
    name: Parchment Studio
    handle: parchment-studio
    org: Parchment Studio
    url: https://parchment.studio
```

If the project has multiple maintainers, add `metadata.maintainers[]`.

## Platform extension blocks

Pick the platform you actually deploy to (or want to deploy to)
and fill in its block. The shapes live under `platforms/<subtree>/<id>/`
in this repo. A few common ones:

```yaml
platforms:
  vercel:
    framework: nextjs
    install_command: "pnpm install"
    build_command: "pnpm build"
    output: .next
    regions: [iad1]

  claude:
    skill_type: subagent
    model: claude-opus-4-7
    surface: [claude-api, claude-code]

  discord:
    application_id: "111122223333444455"
    scopes: [bot, applications.commands]
    intents: [guilds]
    permissions: "2147483648"
```

Each subtree's `README.md` documents the field shape; each
folder's `compatibility.md` documents how the platform interprets
the universal manifest fields.

## Multi-platform — when

If you target two platforms, add two `platforms.<id>` blocks. One
manifest, many targets. See
[`best-practices/multi-platform-strategy.md`](../best-practices/multi-platform-strategy.md).

## Coexistence with native config

If you already have `vercel.json`, `package.json`, `pyproject.toml`,
`Cargo.toml`, etc — keep them. universal-spawn is additive, not a
replacement. See
[`best-practices/migration-strategy.md`](../best-practices/migration-strategy.md).

## Validate before you commit

```bash
# Local
universal-spawn validate

# In CI
- uses: AgentMindCloud/universal-spawn/validators/github-action@v1
```

A failing validator is the signal you'd otherwise miss until a
user reports a broken Deploy button.

## The 60-second checklist

- [ ] Four required fields filled.
- [ ] At least one `platforms.<id>` block matching where you
  actually deploy.
- [ ] `safety.min_permissions[]` lists every host with a concrete
  scope. No wildcards.
- [ ] `safety.rate_limit_qps` and `safety.cost_limit_usd_daily`
  set, picked from real measurement.
- [ ] `safety.safe_for_auto_spawn: false` unless you're sure.
- [ ] Every secret is in `env_vars_required` with `secret: true`
  and a useful `description`.
- [ ] `metadata.id` is reverse-DNS in a namespace you control.
- [ ] `metadata.source.commit` pinned for releases.
- [ ] `metadata.keywords[]` populated with real search terms.
- [ ] Validator passes locally.

If all 10 are checked, you have a strong manifest.
