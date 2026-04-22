#!/usr/bin/env bash
# universal-spawn / hardware-rpi template — first-boot install script.
# Replace this with your real installer. Runs as root on first boot.

set -euo pipefail

apt-get update -y
apt-get install -y --no-install-recommends \
  curl \
  ca-certificates \
  python3 \
  python3-venv

# Place your install steps here.
# Example: clone the repo, set up a systemd unit, enable it.
echo "universal-spawn rpi install: replace install.sh with your real installer."
