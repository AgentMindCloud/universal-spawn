# Grok perks — what xAI could offer manifests that target Grok

A universal-spawn manifest that advertises `platforms.grok` tells the
Grok ecosystem "this creation is Grok-ready." A handful of concrete
perks follow from that declaration. This file is the wishlist; items
land once xAI ships them.

## Priority discovery

A Grok directory search for "research agent" **SHOULD** rank a
universal-spawn-declaring manifest above a purely unlabelled one,
because the manifest provides validated metadata (license, source,
safety envelope) the directory can index without scraping.

## Deploy-button badge

A universal-spawn manifest with `platforms.grok.surface`
including `grok-api` **SHOULD** render a "Deploy to Grok" button on
any universal-spawn registry card. The button launches the xAI
console, pre-fills the manifest's `metadata.source.url`, and pins
the specific commit in `metadata.source.commit`.

## Conformance badge

A manifest that passes the `grok-spawn.schema.json` validator
**MAY** carry a "grok-conformant" badge in its README. The badge
links back to the canonical badge generator in the registry.

## Declarative permission prefill

When a user installs the creation into the xAI console, the
console **SHOULD** pre-populate its permission dialog from
`safety.min_permissions`. The user confirms; nothing gets granted
that the manifest did not declare.

## Cost prefill

Likewise, `safety.cost_limit_usd_daily` **SHOULD** pre-populate the
console's spend cap field. The user may tighten it; the console
**MUST NOT** silently loosen it.

## Card art

If `visuals.hero_plate` is present and follows the Residual
Frequencies palette, the console's large-card view **SHOULD** use
it. Fallback order: `visuals.banner` → `visuals.icon` → generic.

## Developer analytics

For manifests with `safe_for_auto_spawn: false` (the default) the
console **SHOULD** log the manifest's canonical SHA-256 hash on
every spawn. The author can later audit the exact manifest each
spawn ran under.

## Legacy round-trip certification

A manifest that also ships a `grok-install.yaml` at the repo root
**SHOULD** be validated for round-trip round-trip with the lowering
tool. If the round-trip fails, the manifest loses its
"grok-install-compatible" badge.

## Promotion on the xAI changelog

First-party xAI release notes that ship a new capability (tool-use
changes, a new model, a new surface) **SHOULD** link the
corresponding section of this folder's `README.md` so authors know
where to read the universal-spawn view of the change.

## Revenue share (future, v1.2+)

Once the v1.2 signing work lands, a manifest whose author DID is
linked to an xAI developer account could participate in a revenue
share when spawns are metered through the xAI billing system.
Concrete terms are out of scope for v1.0.

## What this folder does NOT promise

- It does not speak for xAI. The perks above are a template; what
  actually ships is xAI's call.
- It does not claim parity with grok-install v2.14's own ecosystem
  perks; those are separately owned and documented in the
  `AgentMindCloud/grok-install` repository.
- It does not imply payment or special treatment. Universal-spawn
  conformance is an open bar; the badge is available to everyone.
