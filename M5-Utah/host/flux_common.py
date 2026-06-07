"""
Utah Flux shared utilities — serial protocol, port detection, manifest I/O.
Used by studio.py (JIT injection) and omni_flash.py (kernel flash).
"""

from __future__ import annotations

import json
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Iterator, Optional

import serial.tools.list_ports

# USB VID/PID pairs for common M5Stack / ESP32 serial bridges
M5STACK_VID_PID = [
    (0x1A86, 0x55D4),  # CH9102F (AtomS3 / StampS3)
    (0x1A86, 0x7523),  # CH340 (legacy M5)
    (0x0403, 0x6001),  # FT232R (M5Stack Core)
    (0x10C4, 0xEA60),  # CP210x (Core2 / CoreS3)
    (0x303A, 0x1001),  # ESP32-S3 USB-JTAG/serial (native USB)
]

FLUX_SYNC_START = b"FLUX_SYNC_START"
FLUX_SYNC_END = b"FLUX_SYNC_END"
FLUX_BAUD_RUNTIME = 115200
FLUX_BAUD_FLASH = 460800

REPO_ROOT = Path(__file__).resolve().parents[2]
M5_UTAH_ROOT = Path(__file__).resolve().parents[1]
PROJECTS_DIR = M5_UTAH_ROOT / "projects"
PAYLOADS_DIR = M5_UTAH_ROOT / "payloads"


@dataclass
class SerialPortInfo:
    device: str
    description: str
    vid: Optional[int]
    pid: Optional[int]


def iter_m5_ports() -> Iterator[SerialPortInfo]:
    """Yield serial ports that match known M5Stack USB identifiers."""
    for port in serial.tools.list_ports.comports():
        if port.vid is None or port.pid is None:
            continue
        for vid, pid in M5STACK_VID_PID:
            if port.vid == vid and port.pid == pid:
                yield SerialPortInfo(
                    device=port.device,
                    description=port.description or "M5Stack",
                    vid=port.vid,
                    pid=port.pid,
                )
                break


def find_m5_port(preferred: Optional[str] = None) -> Optional[str]:
    """Return the first detected M5 port, or a user-specified port if valid."""
    if preferred:
        return preferred
    ports = list(iter_m5_ports())
    return ports[0].device if ports else None


def list_flux_manifests(directory: Path = PROJECTS_DIR) -> list[Path]:
    """Return sorted .flux.json manifest paths."""
    if not directory.is_dir():
        return []
    return sorted(directory.glob("*.flux.json"))


def load_manifest(path: Path | str) -> dict:
    """Load and validate a .flux.json manifest."""
    manifest_path = Path(path)
    with manifest_path.open(encoding="utf-8") as handle:
        manifest = json.load(handle)

    required = ("manifest_version", "artifact_id", "display_name", "m5_hardware")
    missing = [key for key in required if key not in manifest]
    if missing:
        raise ValueError(f"Manifest missing required keys: {', '.join(missing)}")
    return manifest


def resolve_blueprint_ref(manifest: dict) -> Optional[Path]:
    """Resolve optional source_blueprint path relative to repo root."""
    ref = manifest.get("source_blueprint")
    if not ref:
        return None
    candidate = (REPO_ROOT / ref).resolve()
    return candidate if candidate.is_file() else None


def serialize_manifest_payload(manifest: dict) -> bytes:
    """Compact JSON payload for serial transmission."""
    return json.dumps(manifest, separators=(",", ":")).encode("utf-8")


def transmit_manifest(serial_conn, manifest: dict) -> int:
    """
    Stream manifest to M5IntegratedKernel using the Flux sync protocol.
    Returns number of payload bytes sent.
    """
    payload = serialize_manifest_payload(manifest)
    serial_conn.write(FLUX_SYNC_START)
    serial_conn.write(len(payload).to_bytes(4, byteorder="little"))
    serial_conn.write(payload)
    serial_conn.write(FLUX_SYNC_END)
    return len(payload)
