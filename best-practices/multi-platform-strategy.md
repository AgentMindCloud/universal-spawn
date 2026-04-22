# Multi-platform strategy

When to keep one universal manifest and when to ship a platform-
specific manifest alongside.

## Three rules of thumb

1. **One manifest per creation, even when you target many platforms.**
   `platforms.<id>` blocks were designed for this. Add a block per
   target; the master schema validates them all in one pass.
2. **Add a sibling platform-specific manifest only when the platform
   ships its own deeply-non-universal config.** The classic case is
   `grok-install.yaml` (legacy), which encodes Grok-specific fields
   the universal schema does not (yet) model.
3. **Never ship two manifests that disagree.** A consumer that
   reads both must warn on conflicts and prefer the universal one.

## Decision tree

```
Are you targeting 2+ platforms?
├── No → one manifest. Done.
└── Yes →
    Do all targets fit the universal schema?
    ├── Yes → one manifest with multiple platforms.<id> blocks.
    └── No → one manifest + one sibling for the non-fitting one,
              with the sibling clearly marked as the legacy form.
```

## Universal-only example: Next.js on Vercel + Netlify

```yaml
platforms:
  vercel:
    framework: nextjs
    install_command: "pnpm install"
    build_command: "pnpm build"
    output: .next
    regions: [iad1]
  netlify:
    build_command: "pnpm build"
    publish: ".next"
    plugins: [{ package: "@netlify/plugin-nextjs" }]
```

One manifest, two real deploys. No sibling files needed.

## Sibling-required example: Grok-native bot

```
your-repo/
├── universal-spawn.yaml      ← cross-platform; describes everything
├── grok-install.yaml         ← legacy; same bot, Grok-specific shape
├── tools/
└── prompts/
```

`grok-install.yaml` exists because a fleet of Grok consumers reads
that file directly and won't be retrofitted overnight. The
universal manifest's `platforms.grok` block carries the same
information; the sibling is a compatibility courtesy, not a
duplication.

## Two patterns that look similar but aren't

### Pattern A: same creation, multiple deploys

A single creation deploys to two hosts (Vercel + Netlify) for
failover. One manifest. Both `platforms.vercel` and
`platforms.netlify` are populated. One repo.

### Pattern B: same brand, multiple creations

The "same brand" wraps two distinct creations — a bot and a SaaS,
say. Two repos, two manifests. The metadata.author is the same;
nothing else is. Don't try to fit both into one manifest just
because the brand is one.

## How to think about ordering

When `deployment.targets[]` is an ordered preference list, the
first entry is the canonical target. A consumer that supports
multiple targets picks the highest-ranked target it can fulfill.

```yaml
deployment:
  targets: [vercel, netlify]   # vercel preferred; netlify is fallback
```

Order by preference, not alphabetically.

## Ergonomics inside `platforms.*`

Each `platforms.<id>` block is independent. Don't try to share
fields between them via YAML anchors or anything fancier — it
breaks JSON parsers and confuses readers. If two platforms need
the same value, write it twice.

Do share *files* across platforms. The same `tools/reply.json`
can be referenced by `platforms.claude.tools[*].function_ref` and
`platforms.openai.tools[*].function_ref`. The schema is identical
between the two.

## When to split into two manifests

There's exactly one case in the v1.0 spec: when the targets have
genuinely incompatible deployment lifecycles. The example in
`platforms/hosting/aws/` is `runtime: lambda` vs `runtime: ecs` —
mixing them in one manifest would conflate a serverless-function
shape with a container shape, and ops would never forgive you.

In that case ship two manifests at sibling subdirectories:

```
your-repo/
├── api/universal-spawn.yaml      ← runtime: lambda
└── jobs/universal-spawn.yaml     ← runtime: ecs
```

Each one validates independently. The `metadata.id` differs by
suffix (`com.you.api`, `com.you.jobs`).

## Pitfalls

- **Over-splitting.** Two manifests for two platforms is strictly
  worse than one when the platforms can coexist in a single
  manifest. Avoid the temptation.
- **Under-splitting.** One manifest with a Lambda + an ECS service
  conflates lifecycles. Split.
- **Manifest sprawl.** A 700-line manifest is a smell. If yours is
  approaching that, split by `metadata.id` and have two repos.

## TL;DR

One manifest, many `platforms.<id>` blocks, by default. Sibling
files only when a legacy or genuinely-non-universal platform
forces it. Never disagree across files.
