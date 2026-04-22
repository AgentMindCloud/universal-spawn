# Observability and logging

The standard does not mandate a telemetry shape. It does include
two hooks that platforms typically rely on for telemetry, and one
extension namespace for anything more structured.

## What the spec gives you out of the box

- **Canonical manifest hash.** Conformant consumers compute and
  log SHA-256 of the canonical manifest bytes on every spawn. This
  is the single most useful telemetry primitive: every other event
  ties back to it, and you can audit "which manifest version
  spawned at 3am" with one query.
- **Permission envelope.** When a consumer denies a syscall because
  it's outside `safety.min_permissions`, the denial event ties to
  the manifest hash. Surfacing that count in your dashboard tells
  you whether your envelope is too tight or your code is doing
  things it shouldn't.

## What you should add

Most platforms will want at least:

1. Per-spawn lifecycle events (spawn started, spawn ended, spawn
   killed by cap).
2. Per-call cost accumulation (so the `cost_limit_usd_daily`
   ceiling can act).
3. Permission-denial events (counts, sample stack traces).
4. Manifest-load events (parse failures, schema failures).

None of this needs to be in the manifest itself. It happens at the
consumer.

## When you want telemetry in the manifest

A tracker (W&B, Honeycomb, Arize, Datadog, your in-house thing)
sometimes needs the manifest to point at its config. Use a
reverse-DNS extension namespace:

```yaml
x-ext:
  com.example.observability:
    tracker: wandb
    project: plate-studio
    entity: plate
    otel_endpoint: "https://otel.example.com/v1/traces"
    sample_rate: 0.1
```

A consumer that recognizes `com.example.observability` wires it.
Consumers that don't, ignore it.

We may promote a small `observability` block to first-class in
v1.1. The shape we're tracking:

```yaml
observability:
  exporters:
    - { kind: otel, endpoint_env: OTEL_EXPORTER_OTLP_ENDPOINT }
    - { kind: wandb, project: plate-studio }
  sample_rate: 0.1
```

If you ship `x-ext.com.example.observability` today, switching to
`observability:` later is a one-pass migration.

## What to log per spawn

A defensible minimum:

- Manifest canonical hash.
- Manifest `metadata.id` (when present).
- Spawn start time / duration.
- Per-call cost incremented.
- Per-call permission decisions (allowed / denied / scoped).
- Exit reason (clean / cap-hit / error / killed).

A maximum (don't ship without thought):

- Full manifest text (storage cost adds up; the hash + the schema
  registry is enough).
- Tool-call arguments (likely contain user data; mask).
- Outbound request bodies (same).

## Privacy

Logging PII is your responsibility. The standard's `env_vars_required`
secrets pattern means the manifest itself never carries PII; user
data flows through the spawn, not through the manifest. But the
spawn *does* see user data, and your logger may end up with it.

Use the `safety.data_residency[]` field to constrain where logs
themselves can land. A manifest that declares `data_residency:
[eu]` should not have its logs streamed to a US analytics endpoint.

## Sampling

For high-traffic creations, sample. A `sample_rate: 0.1` in
observability config means 10% of spawns are fully traced; the
rest emit only the manifest hash + the exit reason. The hash plus
the cost cap are enough to detect runaway spends regardless.

## Two telemetry anti-patterns

### "Let me just log the whole prompt"

Tempting; expensive; risks shipping user secrets to your logger.
Mask first, log second. If you really need the full prompt, route
it to a SOC2-hardened store, not your default logging stack.

### "Telemetry is mandatory at install time"

The spec lets consumers ignore `x-ext` blocks. If your registry
refuses to install creations whose manifests don't declare
telemetry, you're using the standard's surface for the wrong
purpose. Telemetry is the operator's choice, not the spec's mandate.

## What ops dashboards usually want

Three panels are enough for most operators:

1. **Spawn rate and exit-reason distribution** by `metadata.id`.
2. **Cost spent vs cost cap** per `metadata.id` per day.
3. **Permission-denial events** ranked by frequency. Top denials
   suggest either an over-tight envelope or active misuse.

Build those before anything fancier.

## TL;DR

The manifest is the contract; observability watches the spawn.
Use the canonical hash as your join key. Use `x-ext.com.you.observability`
for declarative wiring; expect a future `observability:` field to
formalize it. Mask PII; sample heavy traffic; respect
`data_residency`.
