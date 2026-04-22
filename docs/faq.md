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
