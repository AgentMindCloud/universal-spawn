# Showcase · `parchment-weather` — an Arduino weather station

**Use case.** A DIY weather station built on an ESP32. Reads
temperature, humidity, and barometric pressure; reports over MQTT
to a dashboard. Ships a flash-via-companion path so non-developers
can flash it from a browser.

## The manifest

```yaml
version: "1.0"
name: Parchment Weather Station
description: >
  ESP32 weather-station firmware. Reads temperature, humidity, and
  pressure; publishes over MQTT. Ships a flash-via-companion variant
  for browser-based flashing.
type: firmware
platforms:
  esp32:
    kind: flash-via-companion
    chip: esp32-s3
    prebuilt_binary_url: "https://releases.parchment.example/weather-station-esp32s3.bin"
safety:
  min_permissions: [usb:claim:vid=0x303a]
  safe_for_auto_spawn: false
env_vars_required:
  - { name: MQTT_BROKER_URL, description: Public MQTT broker }
  - { name: DEVICE_AUTH_TOKEN, secret: true, description: Per-device auth token }
deployment: { targets: [esp32] }
visuals: { palette: parchment }
metadata:
  license: BSD-3-Clause
  id: com.parchment-studio.weather-station
  author: { name: Parchment Studio, handle: parchment-studio }
  source: { type: git, url: https://github.com/parchment-studio/esp32-weather-station }
  categories: [hardware, science]
```

## Platforms targeted, and why

- **`esp32`** with `kind: flash-via-companion` — keeps the install
  story to "click here, plug in your ESP32, click flash". No
  toolchain needed.

## How discovery happens

The repo's README renders a flash button. A web flasher (esptool-js)
reads the manifest's `prebuilt_binary_url` and flashes the device
over WebSerial.
