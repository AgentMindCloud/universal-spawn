# Migration strategy

You have an existing repo with `vercel.json`, `fly.toml`,
`pyproject.toml`, or some other native config. You want to add
universal-spawn without breaking anything. Here's the playbook.

## Principle: additive, not replacement

Universal-spawn does not replace `vercel.json`. It does not replace
`pyproject.toml`. It does not replace `fly.toml`. The two files
coexist; consumers read what they understand. A repo with both is
strictly better than a repo with one.

## Three phases

### Phase 1: ship a manifest alongside (1 hour)

1. Run `universal-spawn init --type <closest-type>` at the repo
   root. You get a starter `universal-spawn.yaml`.
2. Fill in the four required fields (`name`, `description`,
   `type`, plus a `platforms.<id>` block matching where you
   already deploy).
3. Pull values **from** your existing config — don't duplicate
   them by hand. If `vercel.json` says `framework: nextjs`, your
   manifest's `platforms.vercel.framework` says the same.
4. Run `universal-spawn validate`. It passes? Commit.

You now have a valid manifest. Nothing else changed.

### Phase 2: wire the validator into CI (30 minutes)

Add the GitHub Action:

```yaml
- uses: AgentMindCloud/universal-spawn/validators/github-action@v1
```

…or the pre-commit hook:

```yaml
- repo: local
  hooks:
    - id: universal-spawn
      name: universal-spawn validate
      entry: validators/pre-commit/hook.sh
      language: script
```

CI now blocks PRs that break the manifest. This is the bar that
matters; everything below is optional.

### Phase 3: graduate the safety envelope (a week)

This is where most of the value lands. Walk through:

- `safety.min_permissions` — write down every host your code
  reaches and every filesystem path it writes to. Declare them.
  Run the deploy. Watch for sandbox failures; tighten the list
  until they stop.
- `safety.rate_limit_qps` — measure real traffic for a week. Set
  the limit to 1.5× the p99 rate.
- `safety.cost_limit_usd_daily` — measure real cost for a week.
  Set the limit to 2× the p95 daily.
- `safety.safe_for_auto_spawn` — false by default; flip true only
  if the manifest has zero `required: true` env vars and you've
  audited every code path.

By the end of the week, you have a real safety envelope, not a
placeholder one.

## Coexistence rules per common config

### `vercel.json`

- Keep it for: `headers[]`, `redirects[]`, `rewrites[]`,
  `crons[]`, per-project image-optimization config.
- Move into `universal-spawn.yaml`: framework, build command,
  output dir, regions, per-route function memory + duration, env
  promotion scopes.
- A consumer that reads both must warn on conflicts.

### `fly.toml`

- Keep it for: `[build]` args, `[env]` (non-secret), `[metrics]`,
  `[statics]`, kernel/swap settings.
- Move into `universal-spawn.yaml`: app name, primary region,
  VM size, HTTP service, mounts, processes, healthcheck.

### `pyproject.toml`

- Keep it for: `[build-system]`, `[project]`, `dependencies`,
  optional extras, `[tool.*]`.
- Move into `universal-spawn.yaml`: distribution name, Python
  range, console_scripts entries, repository (pypi/testpypi),
  build backend.
- The two files cannot disagree on `name` or `requires-python`.

### `package.json`

- Keep it for: `dependencies`, `devDependencies`, `scripts`,
  `exports`, `types`, npm-specific knobs.
- Move into `universal-spawn.yaml`: package name, shape (library /
  cli / workspace), access (public/restricted), bin map.

### `Cargo.toml`

- Keep it for: `dependencies`, `[[bin]]`, `[lib]`, workspace
  config, Cargo-specific metadata.
- Move into `universal-spawn.yaml`: crate name, edition, MSRV,
  shape (library / bin / both), named features.

### `Dockerfile`

- Keep it for: the actual build steps.
- Move into `universal-spawn.yaml`: image reference, build
  platforms, build args (the values, not the steps), registry.

### `wrangler.toml`

- Keep it for: per-environment overrides (`[env.preview]`,
  `[env.production]`), `triggers.crons[]`, custom domains, tail
  logs config.
- Move into `universal-spawn.yaml`: surface (`workers`/`pages`),
  main script, compatibility date, bindings (R2/D1/KV/Queues/DO).

## When NOT to migrate

- The creation lives entirely behind a custom CI/CD pipeline you
  control end-to-end and no third party will ever consume the
  manifest. (You're missing out, but the spec doesn't oblige you.)
- The creation is the platform itself. Internal Vercel-builds-of-
  Vercel don't need a universal-spawn manifest.

## When to delete the native config

Almost never. The native config is what the platform's first-party
toolchain reads; the universal manifest is the cross-platform
metadata layer. Both stay.

The exception is when you also adopt a wrapper tool that translates
the universal manifest *into* the native config at build time. In
that case, the native config becomes a generated artifact (don't
check it in). This is rare; default to keeping both committed.
