# Monetization

The standard does not require monetization metadata. It does
include optional fields and an `x-ext` escape hatch you can use
if you charge for activations or subscriptions.

## Three patterns we've seen

### 1) Pay-once for the asset

The creation is something you buy once (a Unity asset pack, a
Notion template, a Figma design system). Use the platform's own
pricing surface — `platforms.unity.asset_store_category`,
`platforms.canva.kind: template`, `platforms.figma.kind: template`
— and let the platform's store handle billing.

The universal-spawn manifest doesn't need a `price` field for this
case. The store does.

### 2) Pay-per-spawn

The creation is something a user activates and pays for per spawn
(a paid Action, a per-call AI tool). Use `safety.cost_limit_usd_daily`
to declare the maximum spend a single user could incur, and use
the platform's billing API to actually meter calls.

The standard's only role here is to make the cap visible up front,
so users know what they're agreeing to. Platforms that surface the
cap as a "max ask" in the install dialog reduce support load
dramatically.

### 3) Subscription / seat-based

The creation gates features behind a paid subscription. Three
fields cover this declaratively:

```yaml
metadata:
  license: proprietary
  x-ext:
    com.universal-spawn.monetization:
      model: subscription
      billing_url: "https://app.example.com/billing"
      free_tier: true
```

The reverse-DNS prefix marks this as a vendor-extension key, not
a spec field. Consumers MAY ignore it; consumers that understand
it can render a "Subscribe" button alongside the install button.

We may promote `x-ext.com.universal-spawn.monetization` to a
first-class field in v1.1. The shape we're tracking is:

```yaml
monetization:
  model: <one-time | subscription | per-spawn | freemium>
  free_tier: <bool>
  billing_url: <uri>
  trial_days: <int, optional>
```

## What you should NOT do

### Don't gate the manifest itself

A manifest that returns 404 unless a paid token is in the
referrer header breaks discoverability. Manifests are public; the
gating belongs at the spawn step, not at the read step.

### Don't put a price in `description`

`description` is a one-paragraph summary, indexed for search.
Putting "$9/month" there is a hack. If you need a price,
declare it under `x-ext.com.universal-spawn.monetization.price_usd`
(or whatever first-class field the future spec lands on).

### Don't use `safety.cost_limit_usd_daily` as a "starting price"

That field is the user's ceiling, not your floor. Conflating the
two leads to billing surprises and angry support tickets.

## Working with platform stores

Most platforms with a store (Unity Asset Store, Vercel
Marketplace, Cloudflare Apps, Roblox DevEx) handle pricing in
their own UI. universal-spawn's job is to declare the platform
target; the platform's job is to charge.

Two cooperative patterns work well:

1. **The platform reads the manifest's free-tier flag.** If you
   declare `x-ext.com.universal-spawn.monetization.free_tier:
   true`, a Vercel-style listing renders a "Free tier available"
   ribbon. Without that signal, the listing assumes paid-only.
2. **The platform writes back the price.** When you publish to a
   store, the store may inject its own price field into a
   build-time copy of the manifest. Don't fight this; treat the
   stored copy as the source of truth for that platform.

## What about open-source SaaS?

A growing pattern: the manifest is open, the code is open, the
hosted version is paid. Three fields tell the story:

```yaml
metadata:
  license: AGPL-3.0-only           # signal: it's open
  homepage: "https://app.you.com"   # the hosted version
  x-ext:
    com.universal-spawn.monetization:
      model: freemium
      free_tier: true
      billing_url: "https://app.you.com/billing"
```

The manifest still validates. Platforms that don't understand the
`x-ext` block ignore it; platforms that do can surface the hosted
option alongside the self-hosted one.

## Bottom line

The standard does not police your business model. It just gives
you stable places to declare the model so platforms can render a
sensible UI around it. Use the platform's first-class billing
surface where one exists; use `x-ext.com.universal-spawn.monetization`
otherwise.
