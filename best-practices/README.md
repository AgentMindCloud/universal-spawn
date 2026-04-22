# Best practices

Builder-to-builder docs on how to author universal-spawn manifests
that hold up in production. Each doc is 600–1200 words, opinionated,
specific.

| Doc | Read this when… |
|---|---|
| [`secrets-and-permissions.md`](./secrets-and-permissions.md) | …you need to declare what your creation can touch. |
| [`rate-cost-limits.md`](./rate-cost-limits.md) | …you want sensible numbers for `rate_limit_qps` and `cost_limit_usd_daily`. |
| [`versioning.md`](./versioning.md) | …you're about to bump your manifest's `name` or restructure `platforms`. |
| [`platform-perks.md`](./platform-perks.md) | …you want to know what to ask a platform team for in exchange for honoring the spec. |
| [`trust-model.md`](./trust-model.md) | …you need to explain what universal-spawn does and does NOT guarantee. |
| [`abuse-prevention.md`](./abuse-prevention.md) | …you're a platform, and you want to know how this standard limits the blast radius of malicious manifests. |
| [`migration-strategy.md`](./migration-strategy.md) | …you have an existing repo with `vercel.json`/`fly.toml`/etc. and you're adding universal-spawn. |
| [`monetization.md`](./monetization.md) | …you want to charge for activations and need optional metadata for it. |
| [`multi-platform-strategy.md`](./multi-platform-strategy.md) | …you target two or more platforms and need to decide how to split. |
| [`naming-conventions.md`](./naming-conventions.md) | …you can't decide what to put in `name`, `metadata.id`, and `metadata.keywords`. |
| [`metadata-patterns.md`](./metadata-patterns.md) | …you want to use `x-ext` well. |
| [`i18n-and-localization.md`](./i18n-and-localization.md) | …your creation ships in multiple languages. |
| [`accessibility.md`](./accessibility.md) | …you're building anything user-facing. |
| [`observability-logging.md`](./observability-logging.md) | …you want platform consumers to surface useful telemetry. |
