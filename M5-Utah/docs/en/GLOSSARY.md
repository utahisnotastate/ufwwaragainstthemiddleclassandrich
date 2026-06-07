# Glossary

Plain definitions for terms used in M5-Utah and the wider UFW archive.

| Term | Meaning |
|------|---------|
| **Artifact** | A device mode — e.g. step pad controller, wave display, gesture printer. Pick one in `studio.py`. |
| **Blueprint** | JSON file in the parent repo describing an artifact's conceptual components (`*_BLUEPRINT.json`). |
| **ESP32** | The microcontroller inside M5Stack devices. Runs the kernel firmware. |
| **Flux manifest** | A `.flux.json` file telling the device which artifact to run and with what settings. |
| **FSR** | Force Sensitive Resistor — a pad that senses when you step on it. |
| **Grove cable** | Color-coded plug cable used by M5Stack units (no soldering). |
| **I2C** | A two-wire bus for talking to add-on modules (PbHub, DAC, sensors). |
| **JIT injection** | Sending a manifest over USB so the device switches mode without re-flashing. |
| **Kernel / Lazarus Kernel** | `M5IntegratedKernel` — base firmware flashed once; receives manifests after. |
| **Manifest** | Same as Flux manifest. |
| **M5Stack** | Brand of modular ESP32 gadgets (screens, sensors, stackable units). |
| **Omni-Flash** | `omni_flash.py` — tool that flashes the kernel onto a blank M5Stack. |
| **PbHub** | M5Stack unit that reads up to 6 analog sensors over I2C. |
| **PSRAM** | Extra RAM on some ESP32 boards used for larger buffers. |
| **Sovereign Node** | Name used in-project for an M5Stack running the Lazarus Kernel. |
| **Studio / Utah Flux Host** | `studio.py` — tool that lists and injects manifests. |
| **UFW** | Utah Future Weapons — this repository's project family name. |
| **World-A** | In-repo term for present-day, physically buildable deployment (vs. timeline lore). |
| **Zero-click** | End user does not open Arduino IDE or compile code. |

## Lore Terms (Narrative — Not Engineering Specs)

These appear in blueprints and story text. They are **project vocabulary**, not verified physics:

- Akashic Record / Cloud
- Phase-conjugate / Priore Effect (as med-bed claim)
- Psychotronic / scalar waves
- Zero Point Energy (ZPE) as infinite power source
- Vacuum memory / spacetime locking

See [For Scientists](04-FOR_SCIENTISTS.md) and [For Skeptics](05-FOR_SKEPTICS.md) for how these map to real hardware behavior.
