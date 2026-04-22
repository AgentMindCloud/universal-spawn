# Secrets and permissions

Two of the most common ways to ship a broken universal-spawn
manifest: oversharing in `safety.min_permissions`, or leaking a
secret value into the manifest itself. Both are easy to avoid.

## Secrets — the rules

1. **Never put a secret value in the manifest.** Manifests are
   committed to public repos. Anything in them is read by anyone
   who can `git clone`.
2. **Declare secrets by name only.** Use `env_vars_required[]`. Mark
   secrets explicitly with `secret: true`. The platform's credential
   store supplies the actual value at spawn time.
3. **Each secret has a description.** Other humans need to know what
   key to provision. "API key" is not a description; "Anthropic API
   key with Opus 4.7 access" is.

```yaml
env_vars_required:
  - name: ANTHROPIC_API_KEY
    description: Anthropic key with Opus 4.7 access.
    secret: true
  - name: GITHUB_TOKEN
    description: GitHub token with repo + read:org scopes.
    secret: true
    required: false
```

The `required: false` flag is for keys the creation only uses on
some code paths. The platform doesn't block spawn when an optional
key is missing — it disables the feature that needed it.

## Permissions — the rules

1. **Declare the smallest set you actually use.** If you read
   `https://api.example.com/v1/x` and nothing else, declare
   `network:outbound:api.example.com`. Not `network:outbound`.
2. **Use scopes whenever the namespace allows them.** `fs:write` is
   a red flag in any review. `fs:write:/tmp/your-app` is fine.
3. **Hostnames are concrete strings.** No wildcards. The master
   schema's regex rejects `*.example.com`. If you need three
   subdomains, list three.

```yaml
safety:
  min_permissions:
    - network:outbound:api.anthropic.com
    - network:outbound:api.openalex.org
    - fs:read
    - fs:write:/tmp/your-app
    - model:call:claude-opus-4-7
```

## How the two interact

A secret without a permission to use it is useless. A permission
without a secret can be a footgun. Pair them: every outbound host
in `min_permissions` should correspond to a secret that
authenticates against it (or to a public API that doesn't need
one). If your manifest's permissions list grows beyond what your
`env_vars_required` justifies, something is wrong — usually a
copy-paste from another template.

## What the platform does with this

A conformant platform consumer:

1. Refuses to spawn if a `required: true` secret is missing.
2. Sandboxes outbound traffic to the listed hosts. Anything else
   gets denied at the kernel boundary.
3. Logs the manifest's canonical SHA-256 hash so future audits can
   tie a specific spawn to a specific declared envelope.

What it does NOT do is *infer* permissions from your code. The
declaration is the contract. If your code does something the
manifest didn't declare, the platform breaks the call — not the
other way around.

## Recipes

### A read-only research agent

```yaml
safety:
  min_permissions:
    - network:outbound:api.anthropic.com
    - network:outbound:api.openalex.org
    - model:call:claude-opus-4-7
  rate_limit_qps: 3
  cost_limit_usd_daily: 10
  safe_for_auto_spawn: false
```

### A bot that writes to a single S3 bucket

```yaml
safety:
  min_permissions:
    - network:outbound:s3.us-east-1.amazonaws.com
    - identity:assume-role:arn:aws:iam::1234:role/your-bot
  cost_limit_usd_daily: 5
  safe_for_auto_spawn: false
```

### A computer-use skill

```yaml
safety:
  min_permissions:
    - network:outbound:api.anthropic.com
    - network:outbound:legacy-portal.acme.example
    - model:call:claude-opus-4-7
  cost_limit_usd_daily: 3
  safe_for_auto_spawn: false
```

## Common review failures

- A permission no env var supports.
- A secret that no permission lets the bot use.
- `network:outbound` without a host scope.
- `fs:write` without a path scope.
- A `safe_for_auto_spawn: true` manifest that has any required
  secrets — almost always a mistake. Auto-spawn is for creations
  that need nothing; if you need a key, you need a confirmation gate.

## Threat model in one paragraph

The author publishes the smallest possible envelope. The platform
enforces it. The manifest is the contract. Capability containment
is the only real safety boundary; everything else is policy with
extra steps.
