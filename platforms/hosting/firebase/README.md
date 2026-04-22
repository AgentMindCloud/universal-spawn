# Firebase — universal-spawn platform extension

Firebase bundles Hosting (static + SSR), Cloud Functions for Firebase, Firestore / Realtime Database, Auth, Storage, and App Check under one manifest. DB provisioning is first-class: the manifest lists Firestore indexes, security rules, and seed data alongside the rest of the deployment.

## What this platform cares about

The project id, which services are enabled (`hosting`, `functions`, `firestore`, `realtime_db`, `storage`, `auth`, `extensions`), and per-service configuration.

## What platform-specific extras unlock

`firestore.rules_file` and `firestore.indexes_file` drive security + indexes. `extensions[]` installs official Firebase Extensions (e.g. `delete-user-data`, `resize-images`).

## Compatibility table

| Manifest field | Firebase behavior |
|---|---|
| `version` | Required. |
| `name, description` | Firebase project metadata. |
| `type` | `web-app`, `api-service`, `workflow`, `bot`, `site`. |
| `env_vars_required` | Firebase secrets manager (Functions config). |
| `deployment.targets` | Must include `firebase`. |
| `platforms.firebase` | Strict. |

### `platforms.firebase` fields

| Field | Purpose |
|---|---|
| `platforms.firebase.project_id` | Firebase project id. |
| `platforms.firebase.region` | Primary region (for Functions). |
| `platforms.firebase.hosting` | Hosting block. |
| `platforms.firebase.functions` | Cloud Functions block. |
| `platforms.firebase.firestore` | Firestore block (rules + indexes). |
| `platforms.firebase.realtime_db` | Realtime Database rules. |
| `platforms.firebase.storage` | Storage rules + buckets. |
| `platforms.firebase.auth` | Auth providers. |
| `platforms.firebase.extensions` | Firebase Extensions. |

See [`compatibility.md`](./compatibility.md) for the side-by-side diff
against `firebase.json`, [`deploy-button.md`](./deploy-button.md)
for the canonical Deploy-button recipe, and [`perks.md`](./perks.md) for
what a conformant Firebase consumer SHOULD offer manifests that
declare `platforms.firebase`.
