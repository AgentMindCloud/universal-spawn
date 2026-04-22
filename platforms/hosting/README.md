# `platforms/hosting/` — hosting & cloud destinations

Registry of hosting-flavoured platform extensions. Each subdirectory
is self-contained: drop a developer into `platforms/hosting/<id>/`
and they can use it without reading anything else.

Every folder follows the same seven-file layout:

```text
<id>/
├── README.md                      # 3-6 paragraphs + compat table
├── <id>-spawn.yaml                # canonical platform manifest
├── <id>-spawn.schema.json         # draft-07, allOf against master v1.0
├── compatibility.md               # side-by-side diff vs native config
├── deploy-button.md               # Deploy-button markdown/html
├── perks.md                       # what the platform could offer
└── examples/
    ├── static-site.yaml           # minimal static site
    ├── serverless-api.yaml        # serverless function / API
    └── full-stack-app.yaml        # full-stack app with DB + secrets
```

All schema extensions are **draft-07** and use `allOf` against
`spec/v1.0/universal-spawn.schema.json`. They never redefine shared
fields. All examples validate against the platform schema (which in
turn validates against the master).

## Coexistence with native config

Every hosting provider already has a native config file: `vercel.json`,
`netlify.toml`, `railway.json`, `fly.toml`, `render.yaml`,
`wrangler.toml`, `app.json`, `app.yaml`, and so on. **universal-spawn
does not replace those files.** Instead:

1. A manifest sets `platforms.<provider>` to describe the creation
   from the provider's perspective.
2. The native config (if present) carries provider-specific knobs the
   universal schema does not (yet) model.
3. A conformant consumer reads both; conflicts must trigger a warning
   and prefer `universal-spawn.yaml`.

Each provider folder's `compatibility.md` has the side-by-side diff
showing how a real native config co-lives with the universal manifest.

## Capability matrix (20 providers)

Enforcement key: **E** = enforced, **U** = used (advisory), **—** = ignored.

### Edge / JS-centric

| Id | Native config | Static sites | Serverless fns | Full-stack | Deploy button |
|---|---|:---:|:---:|:---:|:---:|
| [vercel](./vercel)             | `vercel.json`          | E | E | E | E |
| [netlify](./netlify)           | `netlify.toml`         | E | E | E | E |
| [cloudflare](./cloudflare)     | `wrangler.toml`        | E | E | E | E |
| [deno-deploy](./deno-deploy)   | `deno.json`            | U | E | U | U |

### PaaS (containers + buildpacks)

| Id | Native config | Docker? | Long-running | Deploy button |
|---|---|:---:|:---:|:---:|
| [railway](./railway)           | `railway.json`         | E | E | E |
| [fly-io](./fly-io)             | `fly.toml`             | E | E | E |
| [render](./render)             | `render.yaml`          | E | E | E |
| [heroku](./heroku)             | `app.json`             | E | E | E |
| [koyeb](./koyeb)               | `koyeb.yaml`           | E | E | U |
| [northflank](./northflank)     | `northflank.yaml`      | E | E | U |

### Big clouds (AWS / GCP / Azure)

| Id | Native config | Runtime targets | Deploy button |
|---|---|---|:---:|
| [aws](./aws)                   | `samconfig.toml`, AWS CDK | Lambda, ECS, App Runner, Amplify | U |
| [gcp](./gcp)                   | `app.yaml`, `cloudbuild.yaml` | Cloud Run, Cloud Functions, App Engine | U |
| [azure](./azure)               | `azure.yaml` (azd)     | Static Web Apps, Functions, Container Apps | U |

### Backend-as-a-Service

| Id | Native config | DB provisioning | Deploy button |
|---|---|:---:|:---:|
| [supabase](./supabase)         | `supabase/config.toml` | E (Postgres + Auth + Storage) | U |
| [firebase](./firebase)         | `firebase.json`        | E (Firestore + Auth + Storage) | U |

### General hosting / VPS

| Id | Native config | Shape |
|---|---|---|
| [digitalocean](./digitalocean) | `app.yaml` (App Platform) | App Platform + Functions |
| [pythonanywhere](./pythonanywhere) | `wsgi.py` pattern | Python-only hosting |
| [hetzner](./hetzner)           | `cloud-init` snippets  | Cloud VM + image recipes |
| [linode](./linode)             | StackScript            | Akamai Cloud VMs |
| [vultr](./vultr)               | `cloud-init` + API     | VPS + managed services |

## Adding a hosting provider

1. Open a [new-platform issue](../../.github/ISSUE_TEMPLATE/new_platform.yml)
   with category `hosting`.
2. Create `platforms/hosting/<id>/` with all six top-level files plus
   three `examples/{static-site,serverless-api,full-stack-app}.yaml`.
3. The schema **MUST** be `allOf` against
   `spec/v1.0/universal-spawn.schema.json`.
4. Update this matrix.
5. Two maintainer approvals.

## Validation

Everything under `platforms/hosting/**` is exercised by
`scripts/validate_hosting_platforms.py`. A single failing example
blocks merge.
