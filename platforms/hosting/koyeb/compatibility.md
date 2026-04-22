# Koyeb compatibility — field-by-field

Koyeb already has a native config format
(`koyeb.yaml`). universal-spawn does not replace it; the two
coexist. A Koyeb consumer reads both:

- `koyeb.yaml` for provider-specific knobs the universal-spawn
  extension does not (yet) model.
- `universal-spawn.yaml` (with `platforms.koyeb`) for the
  cross-platform manifest.

The two files **MUST NOT** disagree on fields that appear in both; a
consumer that detects a conflict MUST warn and prefer `universal-spawn.yaml`.

## Side-by-side

### `koyeb.yaml` (provider-native)

```yaml
name: your-app
service:
  type: web
  regions: [fra, was]
  instance_type: nano
  ports:
    - port: 8080
      protocol: http
      path: /
  autoscaling:
    min: 1
    max: 5
    targets:
      cpu: { value: 80 }
```

### `universal-spawn.yaml` (platforms.koyeb block)

```yaml
platforms:
  koyeb:
    service_kind: web
    build: { kind: git, build_command: "pnpm build", run_command: "pnpm start" }
    regions: [fra, was]
    instance_type: nano
    ports:
      - { port: 8080, protocol: http, path: / }
    autoscaling: { min: 1, max: 5, targets: { cpu_percent: 80 } }
```

## Field-by-field

| universal-spawn v1.0 field | Koyeb behavior |
|---|---|
| `version` | Required. |
| `metadata.id` | App-name suggestion. |
| `name, description` | Card. |
| `type` | `web-app`, `api-service`, `container`, `workflow`. |
| `safety.*` | Informational. |
| `env_vars_required` | Koyeb secrets. |
| `platforms.koyeb.service_kind` | `web`, `worker`. |
| `platforms.koyeb.build` | `git` or `docker`. |
| `platforms.koyeb.regions` | Regions list. |
| `platforms.koyeb.instance_type` | Instance type. |
| `platforms.koyeb.ports` | HTTP port routing. |
| `platforms.koyeb.autoscaling` | Autoscaling bounds + targets. |


