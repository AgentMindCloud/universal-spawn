# Awesome universal-spawn projects

> A curated list of real-world projects that ship a
> `universal-spawn.yaml` manifest. Categories mirror the
> `platforms/` tree.
>
> **How to add your project**: open the
> [`example_submission`](.github/ISSUE_TEMPLATE/example_submission.yml)
> issue with a link to your repo + a one-line description. A
> maintainer reviews; on merge, your project lands here.
>
> Bar for inclusion: a public repo with a valid
> `universal-spawn.yaml` at the root, real (not placeholder)
> content, and a maintained release within the last 12 months.

---

## AI

### Model providers (`platforms/ai/`)

<!-- The entry below is a format placeholder, not a real project.
     It will be replaced by the first real submission. -->

- **_example placeholder_** — [`your-org/your-project`](https://github.com/your-org/your-project) —
  short one-line description of what it does and why it belongs here.
  Manifest: [`universal-spawn.yaml`](https://github.com/your-org/your-project/blob/main/universal-spawn.yaml).
  Targets: `platforms.openai`, `platforms.anthropic`. Author: @your-handle.

### Multi-agent frameworks (`platforms/ai/multi-agent/`)

- _(no entries yet)_

### Coding agents (`platforms/ai/coding-agents/`)

- _(no entries yet)_

### Local runtimes (`platforms/ai/local/`)

- _(no entries yet)_

## Hosting

### Edge / JS-centric

- _(no entries yet)_

### PaaS

- _(no entries yet)_

### Big clouds

- _(no entries yet)_

### Backend-as-a-Service

- _(no entries yet)_

### General hosting / VPS

- _(no entries yet)_

## Creative

- _(no entries yet)_

## Devtools

### IDEs + browser extensions

<!-- Format placeholder — replace with the first real devtools submission. -->

- **_example placeholder_** — [`your-org/vscode-your-extension`](https://github.com/your-org/vscode-your-extension) —
  short one-line description of the extension.
  Manifest: [`universal-spawn.yaml`](https://github.com/your-org/vscode-your-extension/blob/main/universal-spawn.yaml).
  Targets: `platforms.vscode`. Author: @your-handle.

### Infra / container / IaC

- _(no entries yet)_

### Language package registries

- _(no entries yet)_

### Cloud dev environments

- _(no entries yet)_

## Social / messaging

- _(no entries yet)_

## Data + ML

- _(no entries yet)_

## Gaming

### Engines

<!-- Format placeholder — replace with the first real gaming submission. -->

- **_example placeholder_** — [`your-org/your-godot-game`](https://github.com/your-org/your-godot-game) —
  short one-line description of the game or asset.
  Manifest: [`universal-spawn.yaml`](https://github.com/your-org/your-godot-game/blob/main/universal-spawn.yaml).
  Targets: `platforms.godot`, `platforms.steam`. Author: @your-handle.

### Stores + mod ecosystems

- _(no entries yet)_

### Other engines + makers

- _(no entries yet)_

## Hardware + IoT

- _(no entries yet)_

---

## Entry format

Each entry is one bullet with these fields:

```markdown
- **[Project name](https://github.com/owner/repo)** — one-line description.
  Manifest: [`universal-spawn.yaml`](https://github.com/owner/repo/blob/main/universal-spawn.yaml).
  Targets: `platforms.x`, `platforms.y`. Author: @handle.
```

## Quality bar

- The repo is public.
- The manifest validates against the v1.0 master schema (CI will
  check on submission).
- Targets at least one `platforms.<id>` block from a published
  extension.
- Has at least one tagged release within the last 12 months
  (drift-prevention).
- The README explains what the project does in plain prose.

## Submitting

1. Open
   [`example_submission`](.github/ISSUE_TEMPLATE/example_submission.yml)
   with the four fields the form requests.
2. The validator runs against your manifest's URL.
3. On green, a maintainer adds the entry under the right category
   in this file.
4. The PR is merged; your project ships in the next release of the
   list.

At v1.0 launch, each top-level section shows at most one
clearly-labeled _example placeholder_ so newcomers can see the
exact entry format. Real entries replace the placeholders on first
submission. We'd rather grow slowly with real projects than fake a
deep list.
