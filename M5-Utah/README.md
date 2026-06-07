# M5-Utah Flux Framework

Plug-and-play deployment layer for the UFW arsenal on M5Stack hardware. Flash once, inject manifests over USB — no Arduino IDE or per-artifact compiling for end users.

## Documentation (Start Here)

| Step | Link |
|------|------|
| Pick your language | **[docs/README.md](docs/README.md)** |
| English hub | [docs/en/README.md](docs/en/README.md) |
| Migration (original → M5) | [docs/en/06-MIGRATION_FROM_ORIGINAL.md](docs/en/06-MIGRATION_FROM_ORIGINAL.md) |
| Original pre-M5 approach | [docs/en/07-ORIGINAL_WORLDA_APPROACH.md](docs/en/07-ORIGINAL_WORLDA_APPROACH.md) |

Each language folder (en, et, fi, ru, zh, ja) is self-contained — no mixed-language pages.

---

## Architecture

```
PC (Utah Flux Host)                    M5Stack (Lazarus Kernel)
─────────────────────                  ─────────────────────────
omni_flash.py  ──esptool──►  flash m5_integrated_kernel.bin (once)
studio.py      ──serial───►  receives .flux.json → runs artifact
```

| Layer | Path | Role |
|-------|------|------|
| Kernel firmware | `firmware/M5IntegratedKernel/` | Serial receiver + artifact runtime |
| Host tools | `host/` | `omni_flash.py`, `studio.py`, `flux_common.py` |
| Manifests | `projects/*.flux.json` | Six Batch 1–2 artifacts |
| Payloads | `payloads/m5_integrated_kernel.bin` | Pre-built kernel (build locally) |
| Docs | `docs/` | Audience-specific guides |

---

## Quick Start

### 1. Install host dependencies

```bash
cd M5-Utah
py -3 -m pip install -r requirements.txt
```

### 2. Build the Lazarus Kernel (one-time, maintainer)

Requires [PlatformIO](https://platformio.org/):

```powershell
# Windows
.\scripts\build_kernel.ps1 -Board cores3

# macOS/Linux
./scripts/build_kernel.sh cores3
```

Build targets: `cores3` (default), `core2`, `atoms3`.

### 3. Flash the device (end user)

Connect M5Stack via USB-C:

```bash
py -3 run_omni_flash.py
```

### 4. Inject an artifact

```bash
py -3 run_studio.py
# or non-interactive:
py -3 run_studio.py --artifact zero_point_gpu
py -3 run_studio.py --artifact mnemonic_ddr_infinity
```

---

## Artifact Manifests

| Manifest | Device | Modules |
|----------|--------|---------|
| `Zero_Point_GPU.flux.json` | CoreS3 | DINBase |
| `Mnemonic_DDR_Infinity.flux.json` | Core2 | PbHub + 4× FSR |
| `Psychotronic_Amplifier_Array.flux.json` | AtomS3 | MOSFET + coil |
| `Cellular_Regenesis_Chamber.flux.json` | CoreS3 | Unit-DAC + Unit-Relay |
| `Holographic_Printing_Press_V5.flux.json` | Core2 | Stepmotor + Gesture + Relay |
| `UFW_Tactical_Command_Table.flux.json` | CoreS3 | Unit-ToF + 6× AtomS3 |

Full BOM and verification steps: [Artifact Catalog](docs/en/ARTIFACTS.md) (or your language folder under `docs/`).

---

## Packaging for Distribution

```bash
pip install pyinstaller
pyinstaller --onefile host/omni_flash.py --name omni_flash
```

Ship `omni_flash.exe` + `payloads/m5_integrated_kernel.bin` together.

---

## Verify Without Hardware

```bash
py -3 run_studio.py --list
```
