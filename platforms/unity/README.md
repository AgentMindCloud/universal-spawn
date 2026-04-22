# Unity platform extension

**Id**: `unity`
**Vendor**: Unity Technologies
**Surfaces**: Unity Editor (via a custom package importer), Unity
Package Manager, Unity Asset Store (where policy allows).

A conformant Unity consumer:

1. Validates core + extension.
2. Imports the creation as a Unity package (or project), selecting the
   entry scene named by `entry_scene`.
3. Chooses the render pipeline (`built-in`, `urp`, or `hdrp`) indicated
   in the extension; refuses to import if the project's pipeline
   differs and the creation hasn't declared fallback variants.
4. Applies `min_permissions` to the runtime-side scripts. Editor-time
   scripts are out of the spawn envelope.

## Notable fields

- `target_version` — required minimum Unity editor version.
- `render_pipeline` — `built-in`, `urp`, `hdrp`.
- `scripting_backend` — `mono` or `il2cpp`.
- `entry_scene` — path to the scene to open on spawn.
- `packages[]` — required UPM packages.
- `defines[]` — scripting defines to set.
- `target_platforms[]` — build targets to enable.

See [`unity-spawn.yaml`](./unity-spawn.yaml) and
[`examples/`](./examples).
