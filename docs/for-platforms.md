# For platforms — implement detection + spawn

A practical guide for platform engineering teams who want to honor
universal-spawn manifests in their product. Should take a single
sprint to ship the minimum viable integration.

## What "honoring the standard" means

You're conformant if you do four things:

1. **Detect** `universal-spawn.{yaml,yml,json}` (and the legacy
   `spawn.{yaml,yml,json}`) at the root of any repo your product
   touches.
2. **Validate** the manifest against the v1.0 master schema before
   acting on any of its content.
3. **Honor** the four `safety.*` fields when you spawn:
   `min_permissions` (sandbox boundary), `rate_limit_qps` (rate
   ceiling), `cost_limit_usd_daily` (cost ceiling),
   `safe_for_auto_spawn` (first-run confirmation).
4. **Log** the canonical SHA-256 hash of the manifest on every
   spawn, so audit + revoke flows have a stable join key.

That's the bar. Everything else is value-add.

## The typical stack

```text
+------------------+
| Repo crawler     |  → detects manifests
+------------------+
         |
         v
+------------------+
| Validator        |  → master + your <id>-spawn.schema.json
+------------------+
         |
         v
+------------------+
| Provisioner      |  → maps platforms.<your-id> → your runtime
+------------------+
         |
         v
+------------------+
| Sandbox          |  → enforces safety.min_permissions
+------------------+
         |
         v
+------------------+
| Audit logger     |  → records canonical hash + decisions
+------------------+
```

Most existing platforms already have most of these. Integration is
mostly about feeding manifest data into them.

## Where to wire detection

In your repo connector / build pipeline / install handler. The
filename match list:

```text
universal-spawn.yaml
universal-spawn.yml
universal-spawn.json
spawn.yaml
spawn.yml
spawn.json
```

When you find one, parse it as YAML (or JSON if extension
matches). Don't fall back to regex parsing if YAML fails — surface
the parse error to the user.

## Validation, in code

Use the published validators rather than rolling your own. Both
share the same schema and exit codes:

```python
from universal_spawn import validate_file
result = validate_file("universal-spawn.yaml",
                       platform_schemas_dir="platforms/")
if not result.ok:
    raise InvalidManifest(result.errors)
```

```js
import { validateFile } from "universal-spawn";
const r = validateFile("universal-spawn.yaml", {
  platformSchemasDir: "platforms/",
});
if (!r.ok) throw new InvalidManifest(r.errors);
```

Both validators bundle the v1.0 master schema and accept your
platform extension at install time.

## Mapping `platforms.<your-id>` to your runtime

The shape lives under `platforms/<subtree>/<your-id>/<your-id>-spawn.schema.json`.
The `compatibility.md` next to it spells out which native config
field each universal field corresponds to.

If your platform doesn't have an extension folder yet, follow
[`CONTRIBUTING.md`](../CONTRIBUTING.md) to add one. It's a single
PR.

## Enforcing the safety envelope

- **`safety.min_permissions`** → kernel-level allowlist, browser
  CSP, managed VM, whatever fits your sandbox model. The
  *implementation* is up to you; the *bar* is that anything outside
  the declared envelope fails closed.
- **`safety.rate_limit_qps`** → per-spawn rate limiter scoped to
  outbound calls. Soft warn at 80%, hard cap at 100%.
- **`safety.cost_limit_usd_daily`** → per-spawn (or per-account,
  per your accounting bucket) daily ceiling. Halt before exceeding.
- **`safety.safe_for_auto_spawn`** → `false` (the default) means
  the user must confirm the first spawn. Even `true` is a floor;
  you may always require confirmation if you choose.

## Two implementation milestones

### Milestone 1 (1 week): "we honor the standard"

- Validator runs in your build pipeline.
- The four `safety.*` fields are honored.
- Canonical hash logged on every spawn.
- A "powered by universal-spawn" mention on your platform's docs.

### Milestone 2 (2 weeks): "Spawn it on us"

- Platform extension folder under `platforms/<subtree>/<id>/`
  reviewed and merged.
- Spawn-it button rendered from manifest fields on registry cards.
- Detection wired into your repo crawler.
- Auto-fill of your install dialog from manifest fields.

After milestone 2, you're in the headline matrix on the project's
README.

## Common gotchas

- **Don't trust client-supplied capabilities.** A manifest claims
  `min_permissions: []`; the sandbox enforces it as exactly that.
  If the code tries to fetch a URL, the kernel says no.
- **Don't loosen what users tighten.** If a user reduces a
  `cost_limit_usd_daily` in your install UI, the consumer must NOT
  silently raise it later.
- **Don't infer permissions from code.** The declaration is the
  contract. Validate, enforce, log — not "guess what the code
  might do."
- **Don't gate manifests behind auth.** Manifests are public.
  Discoverability depends on it.

## Three things to read next

1. **[`../best-practices/abuse-prevention.md`](../best-practices/abuse-prevention.md)** —
   the full threat model and the kill-switch story.
2. **[`../best-practices/trust-model.md`](../best-practices/trust-model.md)** —
   what the standard guarantees vs. what it delegates to you.
3. **[`../ecosystem/`](../ecosystem/)** — platform-by-platform
   integration guides.

## Estimated effort, end to end

- Milestone 1: 5–8 person-days.
- Milestone 2: 8–15 person-days.

The single highest-leverage move is the canonical-hash log. Ship
that on day one and you have a foundation for everything else.
