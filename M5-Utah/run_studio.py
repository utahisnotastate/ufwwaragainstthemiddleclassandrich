#!/usr/bin/env python3
"""Launcher for Utah Flux Host — run from M5-Utah root."""

import runpy
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "host"))
runpy.run_path(str(Path(__file__).resolve().parent / "host" / "studio.py"), run_name="__main__")
