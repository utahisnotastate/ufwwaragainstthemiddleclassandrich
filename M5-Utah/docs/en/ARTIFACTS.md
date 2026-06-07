# Artifact Catalog

Six UFW artifacts are deployable today through M5-Utah. Each row lists **what you buy**, **what the device actually does in World-A**, and **where the original blueprint lives**.

## Summary Table

| # | Name | M5 Board | Add-ons | World-A behavior |
|---|------|----------|---------|------------------|
| 1 | Zero Point GPU Emulator | CoreS3 | DINBase (optional cooling) | Animated wave grid on screen; math on one CPU core, drawing on the other |
| 2 | Mnemonic DDR Infinity | Core2 | PbHub + 4× FSR + Grove cables | Step pads trigger "memory write" events; counts shown on display |
| 3 | Psychotronic Amplifier Array | AtomS3 | MOSFET Unit + hand-wound coil | PWM oscillator at 7.83 Hz or 40 Hz; external PSU drives coil |
| 4 | Cellular Regenesis Chamber | CoreS3 | Unit-DAC + Unit-Relay + transducers | 61.8 Hz sine on DAC; inverted phase on relay for acoustic experiments |
| 5 | Holographic Printing Press V5 | Core2 | Stepmotor + Unit-Gesture + Unit-Relay | Hand swipe detected → Z-step counter + UV relay pulse (demo) |
| 6 | UFW Tactical Command Table | CoreS3 | Unit-ToF + 6× AtomS3 Lite (swarm) | ESP-NOW broadcast; ToF hand wave toggles halt/execute (overlord node) |

## Per-Artifact Detail

### 1. Zero Point GPU Emulator

- **Manifest:** `projects/Zero_Point_GPU.flux.json`
- **Blueprint:** `The_Zero_Point_GPU_Emulator/The_Zero_Point_GPU_Emulator_BLUEPRINT.json`
- **Source stub:** `The_Zero_Point_GPU_Emulator/Reality_Engine.cpp`
- **Assembly:** Snap CoreS3 onto DINBase; USB-C to PC.
- **Verify:** Screen shows a live color grid; serial prints frame updates.

### 2. Mnemonic DDR Infinity (Step Machine)

- **Manifest:** `projects/Mnemonic_DDR_Infinity.flux.json`
- **Blueprint:** `Mnemonic_DDR_Infinity/Mnemonic_DDR_Infinity_BLUEPRINT.json`
- **Source stub:** `Mnemonic_DDR_Infinity/AKASHIC_RAM.cpp`
- **Assembly:** PbHub on Port A; FSR units on CH0–CH3; mount under stepping plates.
- **Verify:** Step on a pad → serial logs `[DDR] Memory write`; counter increments on screen.

### 3. Psychotronic Amplifier Array (PAA)

- **Manifest:** `projects/Psychotronic_Amplifier_Array.flux.json`
- **Blueprint:** `Psychotronic_Amplifier_Array/Psychotronic_Amplifier_Array_BLUEPRINT.json`
- **Science doc:** `Psychotronic_Amplifier_Array/Psychotronic_Amplifier_Array_SCIENCE.md`
- **Assembly:** MOSFET on Port A; coil leads in screw terminals; **use external PSU for coil current**.
- **Verify:** Oscilloscope on MOSFET output shows ~7.83 Hz or 40 Hz square wave; press BtnA on AtomS3 to toggle mode.

### 4. Cellular Regenesis Chamber (Med-Bed)

- **Manifest:** `projects/Cellular_Regenesis_Chamber.flux.json`
- **Blueprint:** `Cellular_Regenesis_Chamber/Cellular_Regenesis_Chamber_BLUEPRINT.json`
- **Source stub:** `Cellular_Regenesis_Chamber/CHRONO_HEAL_KERNEL.cpp`
- **Assembly:** Unit-DAC on Port A; Unit-Relay on Port B; audio transducers on terminal blocks.
- **Verify:** DAC outputs sine; relay toggles at half-cycle inversion; serial logs `[CHRONO]`.

### 5. Holographic Printing Press V5

- **Manifest:** `projects/Holographic_Printing_Press_V5.flux.json`
- **Blueprint:** `Holographic_Printing_Press_V5/Holographic_Printing_Press_V5_BLUEPRINT.json`
- **Source stub:** `Holographic_Printing_Press_V5/Matter_Compiler.py`
- **Assembly:** Stepmotor stacked under Core2; Gesture on A; Relay on B; NEMA-17 on stepper terminals.
- **Verify:** Down swipe on gesture sensor increments Z and pulses relay (UV demo).

### 6. UFW Tactical Command Table

- **Manifest:** `projects/UFW_Tactical_Command_Table.flux.json`
- **Blueprint:** `UFW_Tactical_Command_Table/UFW_Tactical_Command_Table_BLUEPRINT.json`
- **Source stub:** `UFW_Tactical_Command_Table/REALITY_WAR_ROOM.py`
- **Assembly:** CoreS3 center; Unit-ToF on Port A; optional 6× AtomS3 Lite workers for ESP-NOW swarm.
- **Verify:** Hand within ToF range toggles HALT/ACTIVE on screen; ESP-NOW packets on serial monitor.

## Inject Commands

```bash
py -3 run_studio.py --artifact zero_point_gpu
py -3 run_studio.py --artifact mnemonic_ddr_infinity
py -3 run_studio.py --artifact psychotronic_amplifier_array
py -3 run_studio.py --artifact cellular_regenesis_chamber
py -3 run_studio.py --artifact holographic_printing_press_v5
py -3 run_studio.py --artifact ufw_tactical_command_table
```
