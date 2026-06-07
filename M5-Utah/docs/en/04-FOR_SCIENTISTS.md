# M5-Utah Guide for Scientists & Researchers

This document separates **testable hardware behavior** from **narrative physics claims** in the UFW archive, and provides reproducible measurement protocols for the six deployable artifacts.

---

## Executive Summary

| Layer | Nature | Peer-review status |
|-------|--------|-------------------|
| M5-Utah firmware & host tools | Embedded systems + Python serial tooling | Standard engineering; reproducible given hardware |
| Parent repo `*_SCIENCE.md` files | Mixed exposition with confidence scores | Not independent validation; treat as author narrative |
| Lore terms (ZPE, Akashic memory, med-bed healing) | Speculative / fictional framing | **No evidentiary support** in this repository |

**What you can publish:** instrumented characterization of GPIO, I2C, PWM, acoustic, and ESP-NOW behaviors.  
**What you cannot claim from this repo alone:** biological regeneration, vacuum energy extraction, thought-to-matter printing, or psychotronic causation.

---

## Claim Taxonomy

### Tier A — Directly measurable (World-A)

- UART manifest injection at 115200 baud with defined framing
- FreeRTOS dual-task execution on ESP32-S3
- I2C analog reads from PbHub + FSR voltage dividers
- PWM square waves at 7.83 Hz and 40.0 Hz
- I2C DAC sine generation ~61.8 Hz with relay phase inversion
- Gesture interrupt via PAJ7620U2 I2C register reads
- VL53L0X time-of-flight distance thresholds
- ESP-NOW broadcast frames on 2.4 GHz Wi-Fi radio

### Tier B — Analogies to published physics (require your own citation chain)

- **Schumann resonance (~7.83 Hz):** Extremely low-frequency electromagnetic cavity mode of Earth–ionosphere system. A 7.83 Hz **electrical oscillator** on a bench is not equivalent to coupling to that geophysical mode without antenna, field strength, and SNR analysis.
- **40 Hz gamma entrainment:** Published neuroscience literature examines 40 Hz sensory stimulation paradigms; **this device does not demonstrate clinical outcomes**.
- **61.8 Hz acoustic interference:** Beat cancellation and phase inversion are classical acoustics; mapping to "Priore effect" or "phase-conjugate biology" is **hypothesis**, not demonstrated here.
- **Wave equation on 2D grid:** Numerical Laplacian stencil in `zero_point_gpu.cpp` — standard finite-difference demo, not vacuum computation.

### Tier C — Not empirically grounded in codebase

- Zero-point energy GPU / Casimir compute
- Akashic / vacuum memory allocation
- Cellular age regression
- Holographic matter compilation from intent
- Psychotronic scalar broadcasting
- Timeline analytics / hostility detection

---

## Reproducibility Checklist

### Software versions to record

```
Python: py --version
esptool: esptool version
PlatformIO: pio --version
Board env: cores3 | core2 | atoms3
Git commit hash of ufwwaragainstthemiddleclassandrich
m5_integrated_kernel.bin SHA-256
Manifest manifest_version + artifact_id
```

### Hardware manifest

Record M5Stack SKU, firmware chip (ESP32 vs ESP32-S3), PSRAM presence, and external module revision numbers.

---

## Per-Artifact Protocols

### 1. Zero Point GPU Emulator

**Hypothesis (testable):** Core 0 computes a 2D scalar field update while Core 1 renders without starving the UI loop.

**Apparatus:** CoreS3, USB serial, optional logic analyzer on UART TX.

**Procedure:**

1. Inject `Zero_Point_GPU.flux.json`.
2. Log serial at 115200 for 60 s.
3. Capture display refresh visually or via camera at known FPS.
4. Optionally read `parameters.grid_size`, `wave_speed`, `zpe_gain` from manifest and correlate with visual propagation speed.

**Observables:** Frame counter in serial (`ZPE GPU f=N`); stable display update; no watchdog reset.

**Not demonstrated:** Vacuum energy extraction, photon hard-light projection.

---

### 2. Mnemonic DDR Infinity

**Hypothesis (testable):** FSR pressure reduces analog count below `strike_threshold` and triggers debounced events.

**Apparatus:** Core2, PbHub, 4× FSR, multimeter optional on hub channels.

**Procedure:**

1. Inject manifest; note `strike_threshold` (default 1800).
2. Apply known masses to FSR pads; log serial `[DDR] Memory write` events.
3. Plot trigger count vs. applied force curve.

**Observables:** Monotonic increase in `write_count`; channel ID in log.

**Not demonstrated:** Non-local memory, petabyte allocation, spacetime locking.

---

### 3. Psychotronic Amplifier Array

**Hypothesis (testable):** AtomS3 outputs stable low-frequency square wave on MOSFET gate GPIO.

**Apparatus:** AtomS3, MOSFET Unit, oscilloscope on gate and coil terminals, **current-limited external PSU**.

**Procedure:**

1. Inject manifest; default `schumann` → 7.83 Hz.
2. Measure period T ≈ 127.7 ms ± tolerance budget (crystal, `delayMicroseconds` jitter).
3. Press BtnA; verify switch to ~40 Hz (T ≈ 25 ms).
4. Document duty cycle vs. `duty_percent` parameter.

**Safety:** Do not run high coil current through GPIO; MOSFET isolates MCU.

**Not demonstrated:** Psychotronic signal detection, mind–matter coupling, cited arXiv/MDPI links in parent SCIENCE.md are **not reproduced** by this firmware.

---

### 4. Cellular Regenesis Chamber

**Hypothesis (testable):** DAC outputs sinusoid at carrier_hz; relay output is logically inverted half-cycle.

**Apparatus:** CoreS3, Unit-DAC, Unit-Relay, two transducers or high-Z scope probes, SPL meter optional.

**Procedure:**

1. Inject manifest (`carrier_hz`: 61.8).
2. Capture DAC analog output — expect sine with f ≈ 61.8 Hz.
3. Capture relay digital output — expect 180° phase relationship to sine zero-crossings (within relay latency).
4. If acoustic path installed, measure SPL; **use hearing-safe levels**.

**Not demonstrated:** DNA resequencing, telomere restoration, entropy reduction in biological tissue.

---

### 5. Holographic Printing Press V5

**Hypothesis (testable):** PAJ7620 gesture code `0x04` triggers Z increment and relay pulse of `uv_pulse_ms`.

**Apparatus:** Core2, Unit-Gesture, Unit-Relay, scope on relay contacts.

**Procedure:**

1. Inject manifest.
2. Perform controlled down-swipe at fixed distance; count relay pulses.
3. Verify `z_position_steps` increments by 800 per trigger (firmware constant).

**Not demonstrated:** SLA resin curing pipeline, vacuum stress materialization, intent clarity metrics.

---

### 6. UFW Tactical Command Table

**Hypothesis (testable):** VL53L0X ranging below `wave_threshold_mm` toggles system state and emits ESP-NOW packets.

**Apparatus:** CoreS3, Unit-ToF, second ESP32 as ESP-NOW sniffer (optional), Wi-Fi spectrum analyzer optional.

**Procedure:**

1. Inject manifest.
2. Approach hand at measured distances; log HALT/ACTIVE transitions.
3. Capture ESP-NOW frames with sniffer; document MAC broadcast `FF:FF:FF:FF:FF:FF` and payload struct `WorkerPacket` (see `war_room.cpp`).

**Not demonstrated:** Threat intent classification, timeline simulation, FinOps profitability sensing.

---

## Data Schema for Publication

Suggested open dataset fields per run:

```yaml
run_id: UUID
artifact_id: string
board: string
manifest_sha256: string
firmware_sha256: string
environment:
  temperature_c: float
  humidity_pct: float
instruments:
  - model: string
    calibration_date: date
results:
  - observable: string
    value: float
    unit: string
    uncertainty: float
```

---

## Relationship to Parent `*_SCIENCE.md` Files

Example: `Psychotronic_Amplifier_Array_SCIENCE.md` reports confidence 0.94 with Schrödinger-form equations and external citations. **That score is internal to the archive schema**, not the output of blinded replication.

Recommended interpretation:

1. Use SCIENCE.md as **conceptual bibliography and hypothesis notes**.
2. Use M5-Utah firmware as **apparatus definition** for Tier A measurements only.
3. Do not merge Tier C claims into Tier A results without separate preregistered studies.

---

## Ethical & Safety Notes for Human Subjects

- **No medical claims** — med-bed artifact is an audio/electronics testbed.
- **Hearing protection** for sustained 61.8 Hz or 40 Hz exposure at high SPL.
- **Coil experiments** — limit current; fire risk with continuous MOSFET switching into inductive load.
- **ESP-NOW / Wi-Fi** — RF exposure within consumer device limits; document locale regulations.

---

## Suggested Citations (Methods, Not UFW Claims)

When describing apparatus, cite primary sources for components:

- Espressif ESP32-S3 Technical Reference Manual
- M5Stack product wiki for I2C addresses and Grove pinout
- Espressif ESP-NOW API documentation
- PAJ7620U2 gesture sensor datasheet
- VL53L0X ranging sensor datasheet

For biological or ZPE claims, **do not cite this GitHub repo as evidence** — cite peer-reviewed literature independently.

---

## Contact & Collaboration

Repository author context: Utah-1 / General 23 narrative framing. For instrumented replication studies, document your fork, manifest hashes, and raw captures; issue reproducibility reports against specific git commits.

Further reading: [For Skeptics](05-FOR_SKEPTICS.md) | [Technical Reference](03-FOR_TECHNICAL_USERS.md)
