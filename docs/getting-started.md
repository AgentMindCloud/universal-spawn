# Getting started — 5 minutes

You're either (a) a creator who wants their project to be
spawnable across many platforms, or (b) a platform engineer who
wants to honor the standard. This page gets you to the next
useful action in five minutes.

## If you're a creator

```bash
# 1) Install the validator (Python or Node — pick one).
uv pip install universal-spawn       # python
# or
npm i -g universal-spawn             # node

# 2) Generate a starter at the root of your repo.
universal-spawn init --type minimal

# 3) Edit universal-spawn.yaml — fill in the four required fields:
#    name, description, type, plus a real `platforms.<id>` block.
$EDITOR universal-spawn.yaml

# 4) Validate.
universal-spawn validate

# 5) Commit. Push. You're done.
git add universal-spawn.yaml && git commit -m "add universal-spawn manifest"
```

That's the 5-minute path. Detailed walkthrough in
[`quickstart.md`](./quickstart.md). Field-by-field reference in
[`field-reference.md`](./field-reference.md). Safety-envelope
philosophy in [`safety-model.md`](./safety-model.md).

If you're not sure where to start, drop one of the
[`templates/`](../templates/) into your repo and edit the
placeholders.

## If you're a platform engineer

```bash
# 1) Install the validator in your build pipeline.
uv pip install universal-spawn       # or npm i -g universal-spawn

# 2) In your spawn pipeline:
#      a. read universal-spawn.yaml at the repo root
#      b. validate with the master schema + your <id>-spawn.schema.json
#      c. enforce safety.{min_permissions, rate_limit_qps,
#                         cost_limit_usd_daily, safe_for_auto_spawn}
#      d. log the canonical SHA-256 of the manifest on every spawn
#
# 3) (Optional but high-leverage) render a Spawn-it button on
#    registry cards from `platforms.<your-id>`.
```

Everything beyond is gravy. The full implementer guide is
[`for-platforms.md`](./for-platforms.md). The integration
patterns for specific platforms (Grok, Claude, OpenAI, Vercel,
GitHub, Discord) live under [`../ecosystem/`](../ecosystem/).

## What "spawnable" means in one sentence

A `universal-spawn.yaml` at the root of your repo is enough for
any conformant consumer to validate, render, and (with one click
from a Spawn-it button) install your creation on the platforms
you've declared.

## Three things to read next

1. **[`quickstart.md`](./quickstart.md)** — the longer version of
   step (3) above.
2. **[`for-creators.md`](./for-creators.md)** — how to author a
   manifest that holds up in production.
3. **[`faq.md`](./faq.md)** — the questions everyone asks first.
