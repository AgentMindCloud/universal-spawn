# Northflank compatibility — field-by-field

Northflank already has a native config format
(`northflank.yaml (Spec CLI)`). universal-spawn does not replace it; the two
coexist. A Northflank consumer reads both:

- `northflank.yaml (Spec CLI)` for provider-specific knobs the universal-spawn
  extension does not (yet) model.
- `universal-spawn.yaml` (with `platforms.northflank`) for the
  cross-platform manifest.

The two files **MUST NOT** disagree on fields that appear in both; a
consumer that detects a conflict MUST warn and prefer `universal-spawn.yaml`.

## Side-by-side

### `northflank.yaml (Spec CLI)` (provider-native)

```yaml
kind: Project
spec:
  name: your-app
services:
  - kind: CombinedService
    spec:
      name: web
      deployment: { instances: 1 }
      runtimeEnvironment: { DATABASE_URL: "addon:db:connectionString" }
      ports:
        - name: web
          internalPort: 8080
          protocol: HTTP
          public: true
addons:
  - kind: Addon
    spec:
      name: db
      type: postgres
      plan: nf-compute-20
```

### `universal-spawn.yaml` (platforms.northflank block)

```yaml
platforms:
  northflank:
    kind: combined
    build: { git_ref: main, dockerfile_path: Dockerfile }
    resources: { plan: nf-compute-20 }
    replicas: 1
    ports:
      - { name: web, port: 8080, protocol: HTTP, public: true }
    addons:
      - { kind: postgres, name: db, plan: nf-compute-20 }
```

## Field-by-field

| universal-spawn v1.0 field | Northflank behavior |
|---|---|
| `version` | Required. |
| `metadata.id` | Project name suggestion. |
| `name, description` | Card. |
| `type` | `web-app`, `api-service`, `container`, `workflow`. |
| `safety.*` | Informational. |
| `env_vars_required` | Secret groups. |
| `platforms.northflank.kind` | `combined`, `deployment`, `job`. |
| `platforms.northflank.build` | Git build configuration. |
| `platforms.northflank.image` | Image reference when `kind: deployment`. |
| `platforms.northflank.resources` | CPU + RAM allocation. |
| `platforms.northflank.replicas` | Replica count. |
| `platforms.northflank.ports` | HTTP ports. |
| `platforms.northflank.addons` | Managed addons. |
| `platforms.northflank.pipeline` | Pipeline id. |
| `platforms.northflank.region` | Region. |


