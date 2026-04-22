# Google Cloud (GCP) — universal-spawn platform extension

GCP ships three primary application hosting surfaces that fit a universal-spawn manifest: Cloud Run (managed containers), Cloud Functions (single-file serverless), and App Engine (managed platform). The extension picks one via `runtime` and models the surface-specific fields.

## What this platform cares about

The runtime (`cloud_run`, `cloud_functions`, `app_engine`), the project id, the region, and the surface-specific block.

## What platform-specific extras unlock

`cloud_run.ingress` controls the ingress policy. `cloud_functions.trigger` attaches an event source (`http`, `pubsub`, `storage`, `firestore`, `scheduler`).

## Supported runtime targets

| Runtime           | GCP service       | Typical shape                 |
|-------------------|-------------------|-------------------------------|
| `cloud_run`       | Cloud Run         | Managed container web service |
| `cloud_functions` | Cloud Functions   | Single-file serverless fn     |
| `app_engine`      | App Engine Standard / Flex | Managed platform     |


## Compatibility table

| Manifest field | Google Cloud (GCP) behavior |
|---|---|
| `version` | Required. |
| `name, description` | Service / app card. |
| `type` | `web-app`, `api-service`, `container`, `workflow`, `bot`, `site`. |
| `env_vars_required` | Secret Manager secrets. |
| `deployment.targets` | Must include `gcp`. |
| `platforms.gcp` | Strict. |

### `platforms.gcp` fields

| Field | Purpose |
|---|---|
| `platforms.gcp.runtime` | `cloud_run`, `cloud_functions`, `app_engine`. |
| `platforms.gcp.project_id` | GCP project id. |
| `platforms.gcp.region` | GCP region. |
| `platforms.gcp.service_account` | Service-account email override. |
| `platforms.gcp.cloud_run` | Cloud Run service block. |
| `platforms.gcp.cloud_functions` | Cloud Function block. |
| `platforms.gcp.app_engine` | App Engine service block. |

See [`compatibility.md`](./compatibility.md) for the side-by-side diff
against `app.yaml / cloudbuild.yaml`, [`deploy-button.md`](./deploy-button.md)
for the canonical Deploy-button recipe, and [`perks.md`](./perks.md) for
what a conformant Google Cloud (GCP) consumer SHOULD offer manifests that
declare `platforms.gcp`.
