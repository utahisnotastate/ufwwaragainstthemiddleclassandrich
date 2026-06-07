#!/usr/bin/env python3
"""Launcher for Omni-Flash Executive — run from M5-Utah root."""

import runpy
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "host"))
runpy.run_path(str(Path(__file__).resolve().parent / "host" / "omni_flash.py"), run_name="__main__")
