# Jupyter compatibility — field-by-field

| universal-spawn v1.0 field | Jupyter behavior |
|---|---|
| `version` | Required. |
| `platforms.jupyter.kind` | `notebook-project` or `lab-extension`. |
| `platforms.jupyter.entry_notebook` | Entry .ipynb path. |
| `platforms.jupyter.requirements` | Requirements file. |
| `platforms.jupyter.kernel` | Kernel name. |
| `platforms.jupyter.lab_extension_id` | JupyterLab extension id. |

## Coexistence with `*.ipynb + requirements.txt / pyproject.toml`

universal-spawn does NOT replace *.ipynb + requirements.txt / pyproject.toml. Both files coexist; consumers read both and warn on conflicts.

### `*.ipynb + requirements.txt / pyproject.toml` (provider-native)

```text
# A Jupyter project's source of truth is the .ipynb files plus the package config used to install the kernel.
```

### `universal-spawn.yaml` (platforms.jupyter block)

```yaml
platforms:
  jupyter:
    kind: notebook-project
    entry_notebook: notebooks/index.ipynb
    requirements: requirements.txt
    kernel: python3
```
