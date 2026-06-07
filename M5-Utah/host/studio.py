#!/usr/bin/env python3
"""
Utah Flux Host (studio.py) — JIT manifest injection for M5 Sovereign Nodes.

Connects to a device running M5IntegratedKernel, lists available .flux.json
artifacts, and streams the selected manifest for instant on-device execution.
"""

from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

import serial
from colorama import Fore, init

from flux_common import (
    FLUX_BAUD_RUNTIME,
    PROJECTS_DIR,
    find_m5_port,
    list_flux_manifests,
    load_manifest,
    resolve_blueprint_ref,
    transmit_manifest,
)

init(autoreset=True)


class UtahFluxDaemon:
    def __init__(self, port: str | None = None, baud: int = FLUX_BAUD_RUNTIME):
        self.port = port
        self.baud = baud
        self.serial_conn: serial.Serial | None = None
        self.manifest_dir = PROJECTS_DIR

    def connect(self) -> bool:
        target = find_m5_port(self.port)
        if not target:
            print(f"{Fore.RED}[FLUX ERROR] No M5Stack port detected. Plug in device or pass --port.")
            return False

        try:
            self.serial_conn = serial.Serial(target, self.baud, timeout=2)
            print(f"{Fore.GREEN}[FLUX LINK] Connected to Sovereign Node on {target}")
            time.sleep(2)
            return True
        except serial.SerialException as exc:
            print(f"{Fore.RED}[FLUX ERROR] Cannot connect: {exc}")
            return False

    def list_artifacts(self) -> list[Path]:
        manifests = list_flux_manifests(self.manifest_dir)
        print(f"\n{Fore.CYAN}--- AVAILABLE ARTIFACT MANIFESTS ---")
        if not manifests:
            print(f"{Fore.YELLOW}No manifests in {self.manifest_dir}")
            return []

        for index, path in enumerate(manifests):
            try:
                manifest = load_manifest(path)
                device = manifest["m5_hardware"].get("device", "unknown")
                print(f"[{index}] {path.name}  ({manifest['display_name']} / {device})")
            except (OSError, ValueError, KeyError):
                print(f"[{index}] {path.name}  (invalid manifest)")
        return manifests

    def inject_manifest(self, filepath: Path) -> bool:
        if self.serial_conn is None:
            print(f"{Fore.RED}[ERROR] Not connected.")
            return False

        print(f"\n{Fore.YELLOW}[INJECTING] Parsing {filepath.name}...")
        try:
            manifest = load_manifest(filepath)
            blueprint = resolve_blueprint_ref(manifest)
            if blueprint:
                print(f"{Fore.CYAN}[BLUEPRINT] Linked: {blueprint.relative_to(blueprint.parents[2])}")

            byte_count = transmit_manifest(self.serial_conn, manifest)
            print(f"{Fore.MAGENTA}[TRANSMITTING] Streamed {byte_count} bytes to node...")
            print(f"{Fore.GREEN}[SUCCESS] Manifest injected. Node rebooting into {manifest['artifact_id']}.")

            # Read acknowledgement lines from kernel
            deadline = time.time() + 5
            while time.time() < deadline:
                if self.serial_conn.in_waiting:
                    line = self.serial_conn.readline().decode("utf-8", errors="replace").strip()
                    if line:
                        print(f"{Fore.WHITE}  << {line}")
                else:
                    time.sleep(0.1)
            return True

        except (OSError, ValueError, serial.SerialException) as exc:
            print(f"{Fore.RED}[ERROR] Injection failed: {exc}")
            return False

    def close(self) -> None:
        if self.serial_conn and self.serial_conn.is_open:
            self.serial_conn.close()


def main() -> int:
    parser = argparse.ArgumentParser(description="Utah Flux Host — manifest injection")
    parser.add_argument("--port", help="Serial port override")
    parser.add_argument("--list", action="store_true", help="List manifests and exit")
    parser.add_argument("--inject", type=Path, help="Inject a specific .flux.json path")
    parser.add_argument("--artifact", help="Inject by artifact_id (e.g. zero_point_gpu)")
    args = parser.parse_args()

    print(f"{Fore.CYAN}--- UTAH FLUX HOST V1.0 ---")

    daemon = UtahFluxDaemon(port=args.port)

    if args.list:
        manifests = daemon.list_artifacts()
        return 0 if manifests else 1

    if not daemon.connect():
        return 1

    try:
        manifests = daemon.list_artifacts()
        if not manifests:
            return 1

        selected: Path | None = None

        if args.inject:
            selected = args.inject if args.inject.is_absolute() else PROJECTS_DIR / args.inject
        elif args.artifact:
            for path in manifests:
                manifest = load_manifest(path)
                if manifest["artifact_id"] == args.artifact:
                    selected = path
                    break
            if not selected:
                print(f"{Fore.RED}No manifest with artifact_id={args.artifact!r}")
                return 1
        else:
            choice = input(f"\n{Fore.WHITE}Select artifact to manifest (0-{len(manifests) - 1}): ")
            try:
                selected = manifests[int(choice)]
            except (ValueError, IndexError):
                print(f"{Fore.RED}Invalid selection.")
                return 1

        return 0 if daemon.inject_manifest(selected) else 1
    finally:
        daemon.close()


if __name__ == "__main__":
    raise SystemExit(main())
