# Raspberry Pi compatibility — field-by-field

| universal-spawn v1.0 field | Raspberry Pi behavior |
|---|---|
| `version` | Required. |
| `platforms.raspberry-pi.model` | `pi-1`, `pi-2`, ..., `pi-5`, `compute-module-4`, `pico`, `pico-2`, `pico-w`. |
| `platforms.raspberry-pi.os` | `raspberry-pi-os`, `raspberry-pi-os-lite`, `ubuntu`, `dietpi`, `none`. |
| `platforms.raspberry-pi.install_method` | `image-flash`, `overlay`, `script`. |
| `platforms.raspberry-pi.image_url` | Image URL for image-flash installs. |
| `platforms.raspberry-pi.entry_file` | Entry file for overlay / script installs. |

## Coexistence with `config.txt + cmdline.txt + cloud-init`

universal-spawn does NOT replace config.txt + cmdline.txt + cloud-init. Both files coexist; consumers read both and warn on conflicts.

### `config.txt + cmdline.txt + cloud-init` (provider-native)

```ini
[all]
gpu_mem=128
dtparam=audio=on
```

### `universal-spawn.yaml` (platforms.raspberry-pi block)

```yaml
platforms:
  raspberry-pi:
    model: pi-5
    os: raspberry-pi-os
    install_method: script
    entry_file: install.sh
```
