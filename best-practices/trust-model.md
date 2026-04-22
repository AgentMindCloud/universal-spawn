# Trust model

What the universal-spawn standard guarantees, and what it
deliberately delegates to platforms.

## What the standard guarantees

1. **Validation is deterministic.** Two conformant validators
   reading the same manifest reach the same verdict. The schema is
   draft-07 with strict `additionalProperties: false`; surprises are
   spec-violations.
2. **Identity is stable.** `metadata.id` (when present) is reverse-
   DNS, lower-case, dot-separated, and stable across renames and
   forks. A consumer can deduplicate on `id` without coordination.
3. **The safety envelope is declarative.** `safety.min_permissions`,
   `safety.rate_limit_qps`, `safety.cost_limit_usd_daily`, and
   `safety.safe_for_auto_spawn` are the four fields that platforms
   are obligated to enforce.
4. **Secrets are never in the manifest.** `env_vars_required`
   declares names; the platform's credential store supplies values
   at spawn time.
5. **Cross-link integrity.** Every reference inside the spec
   resolves — schema `$ref`s, platform-extension `allOf` chains,
   the canonical schema URL pattern.

## What the standard delegates

1. **The decision to spawn.** A consumer decides whether to spawn
   on its surface. The manifest is a description, not a command.
2. **Identity verification.** The standard does not ship a PKI.
   Trust in `metadata.author` derives from the source URL and the
   credentials at the source host. (We expect future signing
   extensions; they aren't here yet.)
3. **Sandbox implementation.** The platform decides how to enforce
   `min_permissions` — kernel cgroups, browser CSP, a managed VM,
   whatever fits its surface. The standard says what to enforce,
   not how.
4. **Cost tracking.** The standard says "halt before
   `cost_limit_usd_daily` is exceeded." It does not specify the
   accounting bucket (per spawn / per user / per organization). The
   platform decides.
5. **Discovery.** Where consumers find manifests is a registry
   problem; many registries are possible. The spec just says how
   the manifest looks.

## What the standard refuses to do

- **Embed executable code.** Manifests are declarative. There is no
  `script:` field, no `eval:` field, no `webhook_body:` field
  carrying executable text.
- **Trust client-supplied capabilities.** A manifest that *claims*
  it doesn't need network outbound is enforced as not-needing-net.
  If the code tries to `fetch`, the sandbox blocks it.
- **Cache through unknown intermediaries.** Schemas have stable
  `$id` URLs; the spec doesn't recommend mirroring through
  unauthenticated CDNs.

## What a consumer should do at spawn time

1. **Validate the manifest.** Refuse anything that fails master
   schema. Refuse anything that fails the platform extension schema
   for `platforms.<your-id>`.
2. **Check the secret envelope.** Refuse spawn if any
   `required: true` env var is missing.
3. **Apply the permission envelope.** Sandbox the spawn at the
   intersection of (your platform's max envelope) and
   (`safety.min_permissions`).
4. **Apply the rate + cost ceilings.** Soft-warn at 80%; hard-stop
   at 100%.
5. **Confirm with a human if `safe_for_auto_spawn` is false.** The
   default is false; this is the most-common case.
6. **Log the canonical hash.** Hash the canonical-form bytes (per
   the spec's appendix) so audits can reproduce what spawned.

## What a creator should do

1. **Declare the smallest envelope you actually use.** Reviewers
   will ask why you needed each line; you should be able to point
   at a function.
2. **Set `safe_for_auto_spawn: false` until you're sure.** Most
   creations should leave it false. The default is false on
   purpose.
3. **Pin `metadata.source.commit` for releases.** That commit is
   the canonical snapshot. Anything else is "latest."
4. **Don't ship a `--no-verify` workflow.** Skipping the hooks is
   skipping the contract. Fix the underlying issue.

## What the standard cannot tell you

- Whether a creation does what it says it does. Static schema
  validation can't read intent.
- Whether the upstream API the creation calls is itself
  trustworthy.
- Whether the user actually wants this thing on their account.

For all three, the standard expects a human in the loop — usually
gated by `safe_for_auto_spawn: false` plus a UI confirmation step
the platform owns.

## TL;DR

The standard is a contract that two parties (creator, platform)
sign for the benefit of a third (the user). Authors describe what
they need; platforms enforce what they got described; users see a
clear envelope before saying yes.
