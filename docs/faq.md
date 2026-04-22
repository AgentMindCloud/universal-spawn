# FAQ

Decisions, non-decisions, and common confusions.

## Why another manifest format?

Every installable thing on the internet currently has its own manifest
— `package.json` for Node, `Cargo.toml` for Rust, `pyproject.toml` for
Python, `Dockerfile` for containers, `openapi.yaml` for HTTP APIs,
`.well-known/ai-plugin.json` for GPT plugins, a dozen per-platform
`*.json` files for AI Skills and Actions. None of them describe the
**creation** as a whole — only the machinery to build or run it.

universal-spawn covers the layer above: "what is this thing, who made
it, where does it run, what does it promise." That layer is currently
invented from scratch for every platform.

## Why YAML, JSON, **and** TOML?

Because authors already commit in those formats and we didn't want to
make a religion out of it. The schema defines a data model; the
serialization is a preference. All three map losslessly to the same
JSON.

## Why no version field?

Because the creation's version is the tag on its source repo. A
manifest describes "what the repo is"; "which snapshot you looked
at" is named by `source.commit` or by the git tag you cloned. The
spec avoided an extra version field to remove one more way for the
tag and the manifest to disagree.

## Why reverse-DNS `id`?

Reverse-DNS `id`s survive renames, forks, and platform migrations.
They also make collisions extremely unlikely without a central
registry. If you own a domain, you own an `id` namespace; if you
don't, you can use your GitHub handle as a pseudo-domain. The pattern
allows both.

## Why so strict with `additionalProperties: false`?

Because forgiving validation is how platforms silently disagree.
universal-spawn wants every consumer to interpret the same manifest
the same way. If you need an experimental field, use `x-ext.<vendor>`
— consumers are told to ignore unknown `x-ext` keys.

## Why no executable code?

Because embedded scripts turn declarative files into RCE vectors and
defeat the safety model. `ref` is always a reference — a path, route,
or image tag. The platform chooses how to actually invoke it. If you
feel constrained by that, the answer is usually "declare a better
entrypoint kind" rather than "add a shell command."

## Why Apache 2.0?

Because the spec needs to be implementable without friction, including
in commercial products. Apache 2.0 is the standard permissive license
for specifications; JSON Schema, OpenAPI, and OCI all use it or an
equivalent. No CLA is required.

## How does universal-spawn relate to MCP?

[MCP (Model Context Protocol)](https://modelcontextprotocol.io) is a
wire protocol; universal-spawn is a declarative manifest. They are
complementary. A universal-spawn manifest can declare an MCP server
via `entrypoints[].kind: stdio`, `http`, or `websocket` combined with
`platforms.claude.mcp_server`, or via any other platform that
understands MCP. Nothing in the spec ties MCP to a specific platform.

## Why no registry?

Because the spec is deliberately decentralized. A registry is an
implementation choice; multiple can coexist. GitHub search already
works as a naive registry (find `filename:spawn.yaml`). Dedicated
registries can exist above the spec.

## Why these nine platforms?

Because they cover the shape of the ecosystem — AI (Claude, Gemini,
OpenAI), hosting (Vercel, Netlify), creative (Figma, Unity), social
(Discord), and models (Hugging Face). Adding a tenth is a PR. The
Editor rejects additions only when the platform has no mechanical way
to consume the manifest.

## Why not cover `<your favourite platform>`?

Because we only ship platform folders that a maintainer has signed up
to keep current. Open a proposal issue; unclaimed platforms don't ship
because stale extension schemas are worse than no schemas.

## Can I embed a universal-spawn manifest inside another file?

Yes, but not in a way defined by the spec. If your host format
already has a place for "metadata," you can put a manifest there, but
conformant consumers only read `spawn.{yaml,yml,json,toml}` at repo
root. Hosting elsewhere is an implementation detail you own.

## What about signing?

See [`safety-model.md`](./safety-model.md#threat-t5--supply-chain-swap)
and spec Appendix C. In v1.0.0 signatures are **advisory** — the spec
defines how to compute and verify them, but does not require
consumers to reject unsigned manifests. Internal deployments often
add that requirement via policy.

## How do I keep my manifest in sync with my code?

Treat it like any other committed file. Run the validator in CI on
every PR. Keep entrypoint `ref`s stable. Add a lint step that checks
that declared `env_vars_required` names appear somewhere in the code
(the inverse check — code references to undeclared vars — is a
separate lint).

## What changed in 1.0.0 from "pre-public"?

Nothing is "pre-public." 1.0.0 is the first public release of this
spec. Earlier internal drafts (none of which are published) should be
considered non-existent.

## Do I still need `vercel.json` (or `netlify.toml`, `fly.toml`, …)?

Yes. universal-spawn is **additive**, not a replacement. `vercel.json`
keeps owning Vercel-specific knobs the universal schema doesn't (yet)
model — `crons[]`, `headers[]`, `redirects[]`, `rewrites[]`, image-
optimization config. The same goes for `netlify.toml`, `fly.toml`,
`render.yaml`, `wrangler.toml`. Both files coexist in the repo;
conformant consumers read both and warn on conflicts (the universal
manifest wins). The migration playbook lives in
[`../best-practices/migration-strategy.md`](../best-practices/migration-strategy.md).

## What about `grok-install.yaml`? Do I delete it?

No. `grok-install.yaml` (AgentMindCloud/grok-install v2.14) is the
prior Grok-specific manifest and Grok consumers continue to read it
verbatim. Ship `universal-spawn.yaml` (with a `platforms.grok` block)
**alongside** it — neither file replaces the other. The discovery
order Grok consumers SHOULD follow is documented in
[`../platforms/ai/grok/`](../platforms/ai/grok/), and the
[`x-native-agent-grok-compat`](../templates/x-native-agent-grok-compat/)
flagship template ships both files side-by-side as the canonical
exercise.

## Who owns the standard?

The **canonical source** is
[`github.com/AgentMindCloud/universal-spawn`](https://github.com/AgentMindCloud/universal-spawn),
maintained by Jani Solo (`@JanSol0s`) under the AgentMindCloud
organization. The spec itself is **Apache 2.0 in perpetuity** —
mirrors are welcome, forks that re-brand the standard are not. The
roadmap to a technical steering committee, the RFC process, and the
release cadence all live in
[`../GOVERNANCE.md`](../GOVERNANCE.md). Practically: nobody can
revoke or paywall the spec; every implementation can fork the schema
and ship a derivative.

## Can I monetize a creation that ships a manifest?

Yes. The standard is licensing-neutral. Use the platform's first-class
billing surface where one exists (Unity Asset Store, GPT Store
Actions, Vercel Marketplace, Roblox DevEx). For subscription /
per-spawn / freemium patterns the platform doesn't model, declare it
under `x-ext.com.universal-spawn.monetization` — see
[`../best-practices/monetization.md`](../best-practices/monetization.md)
for the recommended shape. The spec also leaves
`metadata.license: proprietary` valid for closed creations.

## How is universal-spawn different from OpenAPI?

OpenAPI describes an HTTP API surface — the routes, parameters, and
response shapes that an HTTP client should expect. universal-spawn
describes a **creation as a whole** — what it is, who made it, where
it deploys, what permissions it needs, what platforms it spawns on.
The two complement each other: a manifest can reference an OpenAPI
document via `compat.openapi` (or under
`platforms.openai.action.openapi_ref` for GPT Store Actions and
`platforms.gemini.extension.openapi_ref` for Vertex AI Extensions).
Think of OpenAPI as the contract for *one HTTP surface* and
universal-spawn as the contract for *a spawnable thing* (which may
expose zero, one, or several HTTP surfaces, and may also be a
notebook, a bot, a game mod, or a piece of firmware).
