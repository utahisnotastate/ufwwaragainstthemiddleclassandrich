#!/usr/bin/env python3
"""
Omni-Flash Executive (OFE) — one-time Zero-Click injection of the Lazarus Kernel.

Flashes M5IntegratedKernel.bin to any connected M5Stack device via esptool.
End users never touch Arduino IDE or PlatformIO.
"""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
import time
from pathlib import Path

from colorama import Fore, Style, init

from flux_common import (
    FLUX_BAUD_FLASH,
    M5_UTAH_ROOT,
    PAYLOADS_DIR,
    find_m5_port,
    iter_m5_ports,
)

init(autoreset=True)

KERNEL_BIN = PAYLOADS_DIR / "m5_integrated_kernel.bin"
BIN_DIR = M5_UTAH_ROOT / "bin"


class OmniFlashExecutive:
    def __init__(self, firmware_path: Path = KERNEL_BIN):
        self.baud_rate = FLUX_BAUD_FLASH
        self.firmware_path = firmware_path
        self.esptool_path = self._resolve_esptool()

    def _resolve_esptool(self) -> str:
        bundled = BIN_DIR / ("esptool.exe" if os.name == "nt" else "esptool")
        if bundled.is_file():
            return str(bundled)
        return "esptool.py"

    def scan_ports(self) -> str | None:
        print(f"{Fore.CYAN}[SCAN] Searching for M5Stack substrate...")
        ports = list(iter_m5_ports())
        if not ports:
            print(f"{Fore.RED}[FAIL] No M5Stack detected. Connect device via USB-C.")
            return None
        for entry in ports:
            print(f"{Fore.GREEN}[FOUND] {entry.description} on {entry.device}")
        return ports[0].device

    def flash_kernel(self, port: str) -> bool:
        if not self.firmware_path.is_file():
            print(f"{Fore.RED}[FAIL] Kernel binary not found: {self.firmware_path}")
            print(f"{Fore.YELLOW}[HINT] Build firmware first:")
            print("  cd M5-Utah/firmware/M5IntegratedKernel && pio run")
            print("  copy .pio/build/*/firmware.bin to M5-Utah/payloads/m5_integrated_kernel.bin")
            return False

        print(f"{Fore.YELLOW}[INJECT] Commencing Zero-Click firmware injection on {port}...")

        cmd = [
            self.esptool_path,
            "--chip",
            "auto",
            "--port",
            port,
            "--baud",
            str(self.baud_rate),
            "--before",
            "default_reset",
            "--after",
            "hard_reset",
            "write_flash",
            "-z",
            "--flash_mode",
            "dio",
            "--flash_freq",
            "80m",
            "--flash_size",
            "detect",
            "0x0",
            str(self.firmware_path),
        ]

        try:
            process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
            )
            assert process.stdout is not None
            for line in process.stdout:
                if "Writing at" in line:
                    sys.stdout.write(f"\r{Fore.MAGENTA}[UPLOADING] {line.strip()}   ")
                    sys.stdout.flush()
            process.wait()

            if process.returncode == 0:
                print(f"\n{Fore.GREEN}[SUCCESS] Lazarus Kernel injected. Device is a Sovereign Node.")
                return True

            print(f"\n{Fore.RED}[FAIL] Injection failed (exit {process.returncode}). Check USB connection.")
            return False

        except FileNotFoundError:
            print(f"\n{Fore.RED}[CRITICAL] esptool not found. Install: pip install esptool")
            return False
        except OSError as exc:
            print(f"\n{Fore.RED}[CRITICAL ERROR] {exc}")
            return False


def main() -> int:
    parser = argparse.ArgumentParser(description="Omni-Flash Executive — flash M5IntegratedKernel")
    parser.add_argument("--port", help="Serial port override (e.g. COM3, /dev/ttyUSB0)")
    parser.add_argument("--firmware", type=Path, default=KERNEL_BIN, help="Path to kernel .bin")
    args = parser.parse_args()

    print(f"{Style.BRIGHT}{Fore.WHITE}--- OMNI-FLASH EXECUTIVE V1.0 ---")

    executive = OmniFlashExecutive(firmware_path=args.firmware)
    target_port = find_m5_port(args.port) or executive.scan_ports()
    if not target_port:
        time.sleep(3)
        return 1

    success = executive.flash_kernel(target_port)
    time.sleep(3)
    return 0 if success else 1


if __name__ == "__main__":
    raise SystemExit(main())
