# Google Cloud (GCP) compatibility — field-by-field

Google Cloud (GCP) already has a native config format
(`app.yaml / cloudbuild.yaml`). universal-spawn does not replace it; the two
coexist. A Google Cloud (GCP) consumer reads both:

- `app.yaml / cloudbuild.yaml` for provider-specific knobs the universal-spawn
  extension does not (yet) model.
- `universal-spawn.yaml` (with `platforms.gcp`) for the
  cross-platform manifest.

The two files **MUST NOT** disagree on fields that appear in both; a
consumer that detects a conflict MUST warn and prefer `universal-spawn.yaml`.

## Side-by-side

### `app.yaml / cloudbuild.yaml` (provider-native)

```yaml
runtime: nodejs22
instance_class: F2
automatic_scaling:
  target_cpu_utilization: 0.65
  max_instances: 10
```

### `universal-spawn.yaml` (platforms.gcp block)

```yaml
platforms:
  gcp:
    runtime: app_engine
    project_id: your-project
    region: us-central
    app_engine:
      service: default
      runtime_id: nodejs22
      instance_class: F2
      scaling: automatic
```

## Field-by-field

| universal-spawn v1.0 field | Google Cloud (GCP) behavior |
|---|---|
| `version` | Required. |
| `metadata.id` | Resource name suggestion. |
| `name, description` | Card. |
| `type` | See above. |
| `safety.min_permissions` | Mapped onto the service-account IAM role. |
| `safety.cost_limit_usd_daily` | Advisory; Budget alerts honor it. |
| `env_vars_required` | Secret Manager. |
| `platforms.gcp.runtime` | `cloud_run`, `cloud_functions`, `app_engine`. |
| `platforms.gcp.project_id` | GCP project id. |
| `platforms.gcp.region` | GCP region. |
| `platforms.gcp.service_account` | Service account email override. |
| `platforms.gcp.cloud_run` | Cloud Run service block. |
| `platforms.gcp.cloud_functions` | Cloud Function block. |
| `platforms.gcp.app_engine` | App Engine block. |

## Relation to existing GCP configs

- **Cloud Run** normally uses `gcloud run deploy` flags; this extension models those flags declaratively so a universal-spawn consumer can emit the equivalent command.
- **Cloud Functions** traditionally uses `gcloud functions deploy` flags or a `functions-framework` entry — again, declaratively captured here.
- **App Engine** uses `app.yaml`; the side-by-side above shows how App Engine content maps to the extension.
