# Original World-A Approach (Pre-M5Stack)

Before **M5-Utah**, the UFW repository was organized as a **flat archive of 27 projects**. This document describes that original layout so you can compare it to the M5 migration path.

---

## Repository Shape (Original)

```
ufwwaragainstthemiddleclassandrich/
├── README.md
├── The_Zero_Point_GPU_Emulator/
│   ├── The_Zero_Point_GPU_Emulator_BLUEPRINT.json
│   ├── The_Zero_Point_GPU_Emulator_MANUAL.md
│   ├── The_Zero_Point_GPU_Emulator_SCIENCE.md
│   ├── Reality_Engine.cpp          ← stub, not compilable
│   └── The_Zero_Point_GPU_Emulator_LANDING.html
├── Mnemonic_DDR_Infinity/
│   ├── Mnemonic_DDR_Infinity_BLUEPRINT.json
│   ├── Mnemonic_DDR_Infinity_BOM.csv
│   ├── AKASHIC_RAM.cpp
│   └── ...
├── ... (25 more projects, same pattern)
└── (no M5-Utah/, no build system)
```

Each project typically included:

| File type | Purpose |
|-----------|---------|
| `*_BLUEPRINT.json` | Component graph / geometry tree |
| `*_SCIENCE.md` | Validation narrative, equations, mermaid |
| `*_MANUAL.md` | Install and operate instructions |
| `*_3D.json` | Scene metadata |
| `*_LANDING.html` | Static promo page |
| `*.cpp` / `*.py` | Conceptual code with **fictional imports** |

There was **no** `requirements.txt`, PlatformIO, or unified flash tool.

---

## How You Were Supposed to Build (Original Spec)

The Batch 1–2 design briefs (pre-M5 migration) described **hand-built World-A** rigs:

### Zero Point GPU
- **Software path:** Compile `Reality_Engine.cpp` against a vacuum/GPU library on a **CUDA-class PC**.
- **Manual says:** NVIDIA GPU, 16 GB RAM, GCC, CUDA Toolkit.
- **Reality:** `zpe_core.h` does not exist in the repo.

### Mnemonic DDR Infinity
- **Hardware path:** DDR5 stick form factor OR piezoelectric stomp discs on **Arduino**.
- **Problem:** Custom voltage clipping (Zeners, pull-downs), breadboard noise.
- **BOM CSV:** Real parts (Kingston DDR, Murata caps) mixed with fictional "quantum cache."

### Psychotronic Amplifier Array
- **Hardware path:** Hand-soldered high-gain transistors, caduceus coil, quartz resonator.
- **Problem:** RF noise ("photon quenching") without careful shielding.
- **Docs:** `Psychotronic_Amplifier_Array_SCIENCE.md` (confidence 0.94) — narrative, not firmware.

### Cellular Regenesis Chamber
- **Hardware path:** Exposed op-amps, custom Tesla coils, phase-conjugate mirror on breadboard.
- **Code:** `CHRONO_HEAL_KERNEL.cpp` → `#include <phase_conjugation.h>` (missing).
- **Also:** `Telomere_Restore.cpp`, OpenSCAD pod geometry.

### Holographic Printing Press V5
- **Hardware path:** Reverse-engineer **SLA 3D printer** motor drivers via **Raspberry Pi GPIO**.
- **Software:** `Matter_Compiler.py` → `scalar_physics`, `consciousness_interface` (missing).
- **Real engineering:** `Holographic Printing Press Design MD.md` references LDGraphy-style design.

### UFW Tactical Command Table
- **Hardware path:** PC monitor "God-Eye" dashboard.
- **Software:** `REALITY_WAR_ROOM.py` → `timeline_analytics`, `psychotronic_radar` (missing).
- **Limitation:** 2D screen only; no physical swarm nodes.

---

## Original Workflow (Typical User)

1. Clone repo, open a project folder.
2. Read `*_MANUAL.md` and `*_BLUEPRINT.json`.
3. Attempt to compile `*.cpp` or run `*.py` → **fail** on missing modules.
4. Optionally build **inspired** breadboard from BOM / science doc.
5. Read root `README.md` for UFW economic / timeline narrative.

**Verification story:** "Usable code" in root README referred to **conceptual** usable blueprints, not a single working binary.

---

## Original vs M5-Utah (Summary)

| Dimension | Original World-A | M5-Utah |
|-----------|------------------|---------|
| **Assembly** | Solder, wire, clip voltage | Grove cables, screw terminals |
| **Toolchain** | Arduino IDE, PlatformIO per project, CUDA, Pi | One kernel + manifest injection |
| **Code status** | Stubs + lore | Compilable firmware + Python host |
| **Project count** | 27 archives | 6 deployed artifacts (more planned) |
| **User skill** | EE + software | Plug USB, pick list |
| **Blueprint role** | Primary spec | Linked lineage in `.flux.json` |
| **Honest demo** | Required self-interpretation | Documented in Scientists / Skeptics guides |

---

## When to Use Original Docs Today

| Use original | Use M5-Utah |
|--------------|-------------|
| Lore, science fiction, citations | Actually flash hardware |
| OpenSCAD / 3D geometry | Step pads, waves, gestures on desk |
| Full 27-project catalog | Six MVP artifacts |
| Writing papers about **narrative** | Instrumented **measurement** protocols |

---

## Migrating Forward

See **[Migration Guide](06-MIGRATION_FROM_ORIGINAL.md)** for step-by-step conversion from original folders to M5-Utah manifests.

---

## See Also

- [Documentation Hub](README.md)
- [Artifact Catalog](ARTIFACTS.md) — M5 BOM side-by-side with blueprint paths
- Parent repo `README.md` — unchanged UFW mission statement
