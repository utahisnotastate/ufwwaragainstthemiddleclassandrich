# M5-Utah Guide for Non-Technical Users

You do **not** need to code, solder, or open the Arduino IDE. If you can plug in a USB cable and double-click a program (or run one command a friend gives you), you can use this system.

---

## What You Are Getting

**M5-Utah** turns a small M5Stack gadget into different useful devices:

- A **step-pad controller** for dance or exercise games
- A **colorful display demo** (wave simulator)
- A **low-frequency oscillator** for coil experiments
- A **sound-wave demo** with two outputs
- A **gesture-controlled motor demo**
- A **desk dashboard** that responds to hand waves

You buy the hardware once, flash it once, then **switch modes** anytime by picking a name from a list.

---

## What to Buy (Starter Kits)

Pick **one** project to start. All use the same base software.

### Easiest starter: Wave Painter (CoreS3 only)

| Item | Approx. role |
|------|----------------|
| M5Stack CoreS3 | Main device with screen |
| USB-C cable | Comes with device usually |

### Step pads: Mnemonic DDR

| Item | Qty |
|------|-----|
| M5Stack Core2 | 1 |
| M5Stack PbHub Unit | 1 |
| M5Stack FSR Unit | 4 |
| Grove cables (HY2.0-4P) | 5 |

### Full list

See [Artifact Catalog](ARTIFACTS.md) for every BOM.

---

## One-Time Setup (Ask a Technical Friend OR Follow Exactly)

### On your computer

1. Install **Python 3** from [python.org](https://www.python.org/downloads/) (check "Add to PATH" on Windows).
2. Open a terminal in the `M5-Utah` folder.
3. Run:
   ```
   py -3 -m pip install -r requirements.txt
   ```
4. If you received a pre-built `m5_integrated_kernel.bin`, it should already be in `M5-Utah/payloads/`. If not, a technical friend must build it (see [Technical Guide](03-FOR_TECHNICAL_USERS.md)).

### On the M5Stack (first time only)

1. Connect the M5Stack to your PC with USB-C.
2. Run:
   ```
   py -3 run_omni_flash.py
   ```
3. Wait for **SUCCESS**. The device is now a blank "receiver."

**You only flash once** unless you get a new board or a major firmware update.

---

## Daily Use (Every Time You Want a New Device Mode)

1. Plug in USB-C.
2. Run:
   ```
   py -3 run_studio.py
   ```
3. You will see a numbered list, for example:
   ```
   [0] Cellular_Regenesis_Chamber.flux.json  (Med-Bed / cores3)
   [1] Holographic_Printing_Press_V5.flux.json  ...
   ...
   ```
4. Type the number and press Enter.
5. The M5Stack reboots into that mode. Done.

### Shortcut (if someone gave you the name)

```
py -3 run_studio.py --artifact mnemonic_ddr_infinity
```

### List modes without plugging in

```
py -3 run_studio.py --list
```

---

## Physical Assembly (No Soldering)

All M5Stack units use **Grove cables** — colored plugs that click in.

**Example — Step pads:**

1. Plug **PbHub** into **Port A** (red) on the Core2.
2. Plug each **FSR** into PbHub channels **CH0, CH1, CH2, CH3**.
3. Put each FSR under a floor plate or cardboard "step zone."

**Example — Med-Bed sound demo:**

1. Plug **Unit-DAC** into Port A on CoreS3.
2. Plug **Unit-Relay** into Port B.
3. Connect small speakers or exciters to the screw terminals (grown-up help).

Diagrams and port names: [Artifact Catalog](ARTIFACTS.md).

---

## How You Know It Works

| Device mode | You should see… |
|-------------|----------------|
| Wave Painter | Colors moving on the screen |
| Step Memory | Number increases when you step on pads |
| Hum Box | Status on AtomS3 screen; coil driven via MOSFET (use scope or LED on coil if unsure) |
| Med-Bed demo | Serial messages; sound from transducers if wired |
| Hand Printer | Z height number increases when you swipe down in front of gesture sensor |
| War Table | Screen says ACTIVE or HALT when you wave over ToF sensor |

If nothing happens: see **Troubleshooting** below.

---

## Troubleshooting

| Problem | Try this |
|---------|----------|
| "No M5Stack detected" | Different USB cable; try another USB port; install CP210x or CH340 driver (Google your board name + "USB driver") |
| Flash fails | Hold **BOOT** button while plugging in USB, then retry `run_omni_flash.py` |
| Wrong mode after inject | Unplug, replug, run `run_studio.py` again with correct number |
| Step pads dead | Check Grove cable clicked fully; PbHub on Port A |
| Screen blank | Re-flash kernel; confirm you built/flashed for the correct board (Core2 vs CoreS3 vs AtomS3) |

---

## What This Is NOT

Being clear helps everyone:

- **Not** a medical device. The "Med-Bed" is an **audio-frequency demo**.
- **Not** a real holographic printer. It is a **gesture + motor + relay demo**.
- **Not** infinite computer memory. Step mode **logs stomp events**.
- **Not** proven "psychotronic" technology. It outputs **known frequencies** (7.83 Hz, 40 Hz) on a GPIO pin.

The **story and names** come from the UFW creative archive. The **hardware behavior** is ordinary electronics you can test with your eyes and ears.

More detail: [For Skeptics](05-FOR_SKEPTICS.md)

---

## Original UFW vs M5 (Which Docs?)

| Situation | Read |
|-----------|------|
| You have the **old 27-folder** repo layout | [Original World-A Approach](07-ORIGINAL_WORLDA_APPROACH.md) |
| You are **switching** from breadboard/Arduino to M5 | [Migration Guide](06-MIGRATION_FROM_ORIGINAL.md) |

## Getting Help

| Need | Read |
|------|------|
| Kid-friendly explanation | [For Children](01-FOR_CHILDREN.md) |
| Build firmware yourself | [For Technical Users](03-FOR_TECHNICAL_USERS.md) |
| Measure and cite experiments | [For Scientists](04-FOR_SCIENTISTS.md) |
| All part names | [Glossary](GLOSSARY.md) |
