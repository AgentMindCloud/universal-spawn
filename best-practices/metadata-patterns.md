# Metadata patterns — using `x-ext` well

Sometimes a manifest needs a field the spec doesn't have yet.
That's what `x-ext` is for.

## The rules

1. **Reverse-DNS prefix.** Every key under `x-ext` MUST start with
   a domain you own. `x-ext.com.example.foo` is fine;
   `x-ext.foo` is not. The schema enforces this.
2. **Consumers MAY ignore.** The spec explicitly says that any
   consumer can ignore any `x-ext.*` content. Don't put critical
   information here.
3. **Stable shape.** Treat your `x-ext.<your-namespace>.*` keys as
   if they were a public API. If you change the shape, version the
   namespace (`x-ext.com.example.foo.v2.*`), don't reshape v1.
4. **No secrets.** `x-ext` is part of the manifest. Manifests are
   public. Same rule as `env_vars_required`.

## Good uses

- Vendor-specific extra fields not yet in the spec.
- Experimental fields you want to test before proposing them
  upstream.
- Telemetry / analytics opt-in flags that platforms can read.
- Cross-org metadata (e.g. badges from a curation collective).

## Bad uses

- Replacing a first-class field. If `metadata.license` exists, use
  it; don't put a license under `x-ext`.
- Storing PII. `metadata.author.email` is fine; arbitrary
  `x-ext.com.example.contact` for an end-user is not.
- Smuggling executable instructions. `x-ext.com.example.script` is
  still rejected by the spec's declarative-only principle.

## Recipes

### Telemetry opt-in

```yaml
x-ext:
  org.agentmindcloud.telemetry:
    anonymous: true
    opt_in: true
    endpoint: "https://telemetry.universal-spawn.dev/v1/spawn"
```

A consumer that supports telemetry honors `opt_in: true` to enable
sending; a consumer that doesn't ignores the block.

### Org-specific monetization

```yaml
x-ext:
  com.example.monetization:
    model: subscription
    free_tier: true
    billing_url: "https://app.example.com/billing"
```

(See `monetization.md` for the full story.)

### Badges

```yaml
x-ext:
  org.curation.badges:
    awarded:
      - { name: "verified", date: "2026-01-15" }
      - { name: "audited",  date: "2026-02-03" }
```

A registry that recognizes the curation collective's namespace
renders the badges; everyone else ignores them.

### Migration breadcrumbs

```yaml
x-ext:
  org.agentmindcloud.grok-install:
    version: "2.14"
    note: "legacy grok-install.yaml ships alongside this manifest."
```

Used by the legacy lowering tool to know whether to emit a
`grok-install.yaml` companion.

## What about `x-` for non-DNS keys?

The spec's `x-ext` block intentionally requires reverse-DNS
prefixes. The bare `x-` prefix common in OpenAPI is too easy to
collide on; the standard says no.

If you see a manifest with `x-ext.foo` (no DNS prefix), the schema
is rejecting it on parse. The author needs to add a real prefix.

## Promoting an `x-ext` field to first-class

Three steps:

1. Use the `x-ext` field in your own manifests for at least one
   minor spec cycle.
2. Open a spec proposal (see `CONTRIBUTING.md`) describing the
   field, its type, who uses it, what consumers do with it.
3. If the proposal lands in v1.N, the field becomes first-class.
   Your existing `x-ext` form stays valid forever (consumers
   ignore unknown keys), and you migrate at your own pace.

## Common mistakes

- Using camelCase under `x-ext` keys that already have a snake_case
  twin. Pick one style per namespace and stick with it.
- Nesting `x-ext` six levels deep. If the structure is that
  intricate, factor it into a sibling JSON file referenced by path.
- Shipping `x-ext` fields a consumer is required to honor. The
  spec says consumers MAY ignore. If the field is required, it
  needs to be first-class — propose the change.

## TL;DR

`x-ext` is the polite escape hatch. Use a reverse-DNS namespace,
keep your fields stable, accept that consumers can ignore them,
and never use it to smuggle around the schema's invariants.
