#!/usr/bin/env bash
# Build M5IntegratedKernel and copy firmware.bin to payloads/
set -euo pipefail

BOARD="${1:-cores3}"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
FIRMWARE_DIR="$ROOT/firmware/M5IntegratedKernel"
PAYLOAD_DIR="$ROOT/payloads"

cd "$FIRMWARE_DIR"
pio run -e "$BOARD"
cp ".pio/build/$BOARD/firmware.bin" "$PAYLOAD_DIR/m5_integrated_kernel.bin"
echo "[OK] Kernel copied to payloads/m5_integrated_kernel.bin ($BOARD build)"
