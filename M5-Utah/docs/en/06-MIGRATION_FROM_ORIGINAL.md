# Migration Guide: Original UFW → M5-Utah

This guide is for anyone who started with the **original archive layout** (27 project folders, stubs, manuals) and is moving to **M5-Utah** (M5Stack + Flux deployment).

---

## At a Glance

| Topic | Original (pre-M5) | M5-Utah |
|-------|-------------------|---------|
| **Where code lives** | `ProjectName/Reality_Engine.cpp`, `Matter_Compiler.py`, etc. | `M5-Utah/firmware/.../artifacts/*.cpp` + `projects/*.flux.json` |
| **Hardware** | Custom breadboards, soldering, Arduino, Pi, CUDA PC | M5Stack Grove modules, no soldering |
| **Build** | Not buildable (fictional `#include`) | PlatformIO + `build_kernel.ps1` |
| **Deploy** | Conceptual manuals only | `omni_flash.py` once, then `studio.py` |
| **Switch device type** | Re-wire / recompile per project | Pick new `.flux.json` manifest |
| **Dependencies** | `zpe_core.h`, `scalar_physics`, etc. (missing) | M5Unified, ArduinoJson, pyserial |

---

## Per-Artifact Migration Map

### 1. Zero Point GPU Emulator

| | Original | M5-Utah |
|---|----------|---------|
| **Blueprint** | `The_Zero_Point_GPU_Emulator/The_Zero_Point_GPU_Emulator_BLUEPRINT.json` | Same file referenced in manifest |
| **Code** | `Reality_Engine.cpp` — `#include <zpe_core.h>`, CUDA-class PC GPU | `artifacts/zero_point_gpu.cpp` — 2D wave math + LCD |
| **Hardware** | Host CPU + "Casimir Compute Gate" + HDMI | M5Stack CoreS3 + optional DINBase |
| **Manual** | `The_Zero_Point_GPU_Emulator_MANUAL.md` — NVIDIA CUDA, 16 GB RAM | [Non-Technical Users](02-FOR_NON_TECHNICAL_USERS.md) |

**What you lose in migration:** PC-scale rendering narrative.  
**What you gain:** Portable demo, dual-core ESP32, zero CUDA setup.

---

### 2. Mnemonic DDR Infinity

| | Original | M5-Utah |
|---|----------|---------|
| **Blueprint** | `Mnemonic_DDR_Infinity/Mnemonic_DDR_Infinity_BLUEPRINT.json` | Same |
| **Code** | `AKASHIC_RAM.cpp` — `MallocVacuum()`, spacetime lock | `artifacts/mnemonic_ddr.cpp` — PbHub FSR polling |
| **Hardware** | DDR5 slot form factor, quantum cache capacitors (BOM CSV) | Core2 + PbHub + 4× FSR + Grove cables |
| **Manual** | Motherboard RAM slot installation | Step plates under FSR pads |

**What you lose:** "Infinite petabyte" story.  
**What you gain:** Real stomp detection without Zener clipping on piezo discs.

---

### 3. Psychotronic Amplifier Array

| | Original | M5-Utah |
|---|----------|---------|
| **Blueprint** | `Psychotronic_Amplifier_Array/Psychotronic_Amplifier_Array_BLUEPRINT.json` | Same |
| **Science** | `Psychotronic_Amplifier_Array_SCIENCE.md` | Still valid as narrative; firmware is PWM |
| **Hardware** | Custom transistor arrays, caduceus coil, quartz — RF shielding critical | AtomS3 + MOSFET Unit + coil in screw terminals |
| **Code** | No `.cpp` in original folder | `artifacts/psychotronic_amplifier.cpp` |

**What you lose:** High-gain analog bench build.  
**What you gain:** Isolated MOSFET gate, 7.83 / 40 Hz toggle on BtnA.

---

### 4. Cellular Regenesis Chamber

| | Original | M5-Utah |
|---|----------|---------|
| **Blueprint** | `Cellular_Regenesis_Chamber/Cellular_Regenesis_Chamber_BLUEPRINT.json` | Same |
| **Code** | `CHRONO_HEAL_KERNEL.cpp` — `PhaseConjugation::invert_time()` | `artifacts/chrono_heal.cpp` — DAC sine + relay invert |
| **Hardware** | Op-amps, Tesla coils, breadboard parasitic risk | CoreS3 + Unit-DAC + Unit-Relay + transducers |
| **Manual** | `Cellular_Regenesis_Chamber_MANUAL.md` | Med-bed acoustic demo docs |

**What you lose:** Phase-conjugate mirror narrative as biology.  
**What you gain:** Measurable 61.8 Hz acoustic experiment.

---

### 5. Holographic Printing Press V5

| | Original | M5-Utah |
|---|----------|---------|
| **Blueprint** | `Holographic_Printing_Press_V5/Holographic_Printing_Press_V5_BLUEPRINT.json` | Same |
| **Code** | `Matter_Compiler.py` — `scalar_physics`, `consciousness_interface` | `artifacts/holographic_press.cpp` |
| **Hardware** | SLA printer tear-down, Pi GPIO, stepper hacking | Core2 + Stepmotor Module + Unit-Gesture + Relay |
| **Design doc** | `Holographic Printing Press Design MD.md` (real LDGraphy refs) | Gesture pull → Z step + UV pulse |

**What you lose:** Full resin SLA pipeline / G-code.  
**What you gain:** Solderless gesture + stepper stack.

---

### 6. UFW Tactical Command Table

| | Original | M5-Utah |
|---|----------|---------|
| **Blueprint** | `UFW_Tactical_Command_Table/UFW_Tactical_Command_Table_BLUEPRINT.json` | Same |
| **Code** | `REALITY_WAR_ROOM.py` — `timeline_analytics`, `psychotronic_radar` | `artifacts/war_room.cpp` — ESP-NOW + ToF |
| **Hardware** | PC monitor, holo projectors, infrasound woofer | CoreS3 overlord + 6× AtomS3 + Unit-ToF |

**What you lose:** 2D-only PC dashboard.  
**What you gain:** Physical desk nodes, hand-wave halt.

---

## Migration Steps (Checklist)

### If you only used original docs / blueprints

1. Read [Original World-A Approach](07-ORIGINAL_WORLDA_APPROACH.md) — understand what the archive was.
2. Buy M5 hardware for **one** artifact ([Artifact Catalog](ARTIFACTS.md)).
3. `cd M5-Utah` → install `requirements.txt`.
4. Build or obtain `payloads/m5_integrated_kernel.bin`.
5. `py -3 run_omni_flash.py` (once).
6. `py -3 run_studio.py --artifact <id>` matching your board.
7. Keep original `*_BLUEPRINT.json` as lineage — manifests already link to them.

### If you tried to compile original stubs

1. **Stop** chasing `zpe_core.h`, `vacuum_dynamics.h`, `scalar_physics` — they are not in the repo.
2. Port **logic ideas** only (e.g. step detection, frequency values) into M5 artifact parameters in `.flux.json`.
3. Real implementation is in `M5-Utah/firmware/M5IntegratedKernel/src/artifacts/`.

### If you already soldered original World-A breadboards

You can **run both**: original bench rig for experiments; M5-Utah for demos and teaching. They are not mutually exclusive. Document which physical setup matches which doc set.

---

## File Path Cheat Sheet

```
ORIGINAL                          M5-UTAH
────────────────────────────────  ────────────────────────────────────
README.md (UFW lore)              M5-Utah/README.md (deploy)
Project/Project_BLUEPRINT.json    projects/Artifact.flux.json
Project/foo.cpp (stub)            firmware/.../artifacts/foo.cpp
Project/Project_MANUAL.md         docs/en/02-FOR_NON_TECHNICAL_USERS.md
(none)                            host/studio.py, omni_flash.py
(none)                            payloads/m5_integrated_kernel.bin
```

---

## FAQ

**Do I delete the 27 original folders?**  
No. They remain the conceptual archive. M5-Utah is the hardware deployment layer.

**Does migration change the story/lore?**  
No. Timeline narrative stays in parent README and `*_SCIENCE.md`. M5-Utah docs explain World-A behavior honestly.

**Can I add a 7th artifact?**  
Extend `artifact_runtime.cpp`, add `projects/NewThing.flux.json`, rebuild kernel. Original pattern was add a new top-level folder only.

---

## See Also

- [Original World-A Approach](07-ORIGINAL_WORLDA_APPROACH.md)
- [Technical Reference](03-FOR_TECHNICAL_USERS.md)
- [Artifact Catalog](ARTIFACTS.md)
