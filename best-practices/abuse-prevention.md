# Abuse prevention

The standard's abuse-prevention story rests on three pillars:
manifests are declarative, validation happens before any code runs,
and platforms wire kill switches that a single hash query can
trigger.

## Pillar 1: declarative-only

Manifests cannot ship executable code. There is no `script:` field
that takes a shell snippet, no `eval:` that takes JS, no
`webhook_body:` that takes a templated request body. Every field
that *references* code references it by path or by URL. The
platform decides how to invoke the referenced thing.

This means a malicious manifest cannot, by itself, run anything.
The worst it can do is reference a malicious binary at a URL — and
the spawn host has full control over whether to fetch and run that
binary. Compare this to a `package.json` with an `install` hook,
which runs `npm install`'s scripts on any machine that touches it.

## Pillar 2: pre-scan

Conformant platforms run validation *before* any spawn-time code
executes. The validation chain is:

1. Parse YAML/JSON. If parse fails: refuse.
2. Validate against the v1.0 master schema. If fails: refuse.
3. Validate `platforms.<your-id>` against your extension schema.
   If fails: refuse.
4. Resolve `metadata.source.url` and `metadata.source.commit`
   against your fetch policy. If you don't trust the source, refuse.
5. Apply policy filters specific to your platform (banned authors,
   blocked permission sets, regions you don't serve). If filtered:
   refuse.

Only after all five steps does any spawn-time code touch a CPU.

## Pillar 3: kill switches

A platform that honors universal-spawn computes the canonical
SHA-256 of the manifest at spawn time and logs it. Reverse this:
when you discover an abusive manifest, you can revoke it with one
hash query.

```text
revoke <hash>
  → all currently-running spawns of this manifest are halted
  → no new spawns of this manifest are allowed
```

Critically, the revocation key is the manifest hash, not the
author's username or the source URL. Authors can re-publish under
new identities; their fingerprint can't dodge a hash revocation.

## Concrete attack categories the standard pre-emptively closes

### "Capability sneak"

The author declares `network:outbound` (broad) hoping the platform
won't notice. Mitigation: the master schema forbids unscoped
network permissions in any reviewer-quality template. Example
specs and templates uniformly use scoped hosts; reviewers are
trained to flag the unscoped form.

### "Cost runaway"

The creation makes more LLM calls than expected; the user wakes up
to a $5,000 bill. Mitigation: `cost_limit_usd_daily` is a hard
ceiling. The platform halts at the cap, regardless of code intent.

### "Secret exfiltration"

The creation reads `ANTHROPIC_API_KEY` from env, posts it to
attacker-controlled host. Mitigation: outbound network is locked to
`min_permissions`. A POST to `evil.example` from a manifest that
declared only `api.anthropic.com` fails at the syscall boundary.

### "Drive-by spawn"

The user clicks a link; a creation spawns and starts doing things.
Mitigation: `safe_for_auto_spawn: false` by default. The first
spawn is gated by an explicit human confirmation.

### "Supply-chain swap"

The author signs a benign manifest; later swaps the binary at the
source URL for malware. Mitigation: `metadata.source.commit`
exists for pinning. The standard's planned signature extension
(see `spec/v1.0.0/spec.md` Appendix C) ships canonical-bytes
signing for this case.

### "Permission elevation via deps"

A creation has `min_permissions: []` but depends on another
manifest with `network:outbound:*`. Mitigation: the standard
requires a spawn host to **union** the transitive dependency
envelope and present that union to the user for consent.

## What's still on the author's shoulders

The standard cannot:

- Tell whether your code is correct. Validation is structural.
- Stop you from publishing an under-declared manifest. Reviewers
  catch this; the spec can only catch obvious violations.
- Stop a determined human attacker from social-engineering past a
  confirmation gate. Sandboxes shrink blast radius; they don't
  abolish trust decisions.

## How a platform wires this in 30 minutes

1. Add the universal-spawn validator to your spawn pipeline.
2. Compute and log the canonical hash on every spawn.
3. Implement `revoke <hash>` as a single SQL update.
4. Block new spawns whose hash is in the revoked set.
5. Surface the user-confirmation gate when
   `safe_for_auto_spawn: false`.

That's the whole story.
