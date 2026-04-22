# `platforms/hardware-iot/` — hardware & IoT

Extensions for devices, microcontrollers, educational hardware, and
home-automation platforms. Each folder ships a minimal sketch /
firmware example plus, where applicable, a flash-via-companion-app
example that a consumer (Arduino Lab, esptool-js in browser, the
Home Assistant config flow) can execute directly.

## Capability matrix (9 platforms)

| Id | Native config | Shape |
|---|---|---|
| [arduino](./arduino)             | `library.properties` + `.ino`     | sketches, libraries, board pinning |
| [raspberry-pi](./raspberry-pi)   | `cmdline.txt` + `config.txt`      | images, overlays, scripts |
| [esp32](./esp32)                 | `partitions.csv` + platformio.ini | firmware, OTA channels |
| [home-assistant](./home-assistant)| `manifest.json` (integration)    | integrations, blueprints |
| [platform-io](./platform-io)     | `platformio.ini`                  | build config, environments |
| [micropython](./micropython)     | `main.py` + `boot.py`             | scripts + filesystems |
| [circuitpython](./circuitpython) | `code.py` + `lib/`                | scripts + libraries |
| [microbit](./microbit)           | MakeCode JSON / Python            | snap-to-flash projects |
| [lego-spike](./lego-spike)       | SPIKE App project export          | educational projects |

## Special examples

- `arduino/` and `esp32/` ship an `flash-via-companion.yaml` example
  that a companion installer (Arduino Lab for MicroPython, `esptool-
  js`) reads to download a prebuilt binary and flash over WebUSB /
  WebSerial.
- `home-assistant/compatibility.md` shows the explicit mapping from
  `platforms.home-assistant` to the Home Assistant integration's
  `manifest.json` fields (`domain`, `dependencies`, `iot_class`,
  `requirements`).

## Cross-links

- Device firmware for a physical product commonly pairs a universal-
  spawn manifest under `hardware-iot/*` with a hosting manifest under
  `platforms/hosting/*` for its companion dashboard (e.g. Fly.io +
  ESP32 OTA channel).
