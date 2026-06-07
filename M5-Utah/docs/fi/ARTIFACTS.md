# Artefattiluettelo

Kuusi UFW-artefaktia on käyttöönotettavissa tänään M5-Utahin kautta. Jokaisella rivillä on **mitä ostat**, **mitä laite oikeasti tekee World-A:ssa** ja **missä alkuperäinen blueprint sijaitsee**.

## Yhteenvetotaulukko

| # | Nimi | M5-levy | Lisäosat | World-A-käyttäytyminen |
|---|------|---------|----------|------------------------|
| 1 | Zero Point GPU Emulator | CoreS3 | DINBase (valinnainen jäähdytys) | Animoitu aaltoverkko näytöllä; matematiikka yhdellä CPU-ytimellä, piirto toisella |
| 2 | Mnemonic DDR Infinity | Core2 | PbHub + 4× FSR + Grove-kaapelit | Askelalustat laukaisevat "memory write" -tapahtumat; laskurit näytöllä |
| 3 | Psychotronic Amplifier Array | AtomS3 | MOSFET Unit + käsin käämitty käämi | PWM-oskillaattori 7,83 Hz tai 40 Hz; ulkoinen PSU ohjaa käämiä |
| 4 | Cellular Regenesis Chamber | CoreS3 | Unit-DAC + Unit-Relay + transduktorit | 61,8 Hz sini DAC:lla; invertoitu vaihe releellä akustisiin kokeisiin |
| 5 | Holographic Printing Press V5 | Core2 | Stepmotor + Unit-Gesture + Unit-Relay | Käden pyyhkäisy tunnistetaan → Z-askelaskuri + UV-relepulssi (demo) |
| 6 | UFW Tactical Command Table | CoreS3 | Unit-ToF + 6× AtomS3 Lite (parvi) | ESP-NOW-lähetys; ToF-kädenheilutus vaihtaa halt/execute (overlord-solmu) |

## Artefaktikohtaiset tiedot

### 1. Zero Point GPU Emulator

- **Manifest:** `projects/Zero_Point_GPU.flux.json`
- **Blueprint:** `The_Zero_Point_GPU_Emulator/The_Zero_Point_GPU_Emulator_BLUEPRINT.json`
- **Lähdestub:** `The_Zero_Point_GPU_Emulator/Reality_Engine.cpp`
- **Kokoaminen:** Napsauta CoreS3 DINBaseen; USB-C tietokoneeseen.
- **Varmistus:** Näyttö näyttää elävän väriverkon; sarja tulostaa kehys-päivityksiä.

### 2. Mnemonic DDR Infinity (Step Machine)

- **Manifest:** `projects/Mnemonic_DDR_Infinity.flux.json`
- **Blueprint:** `Mnemonic_DDR_Infinity/Mnemonic_DDR_Infinity_BLUEPRINT.json`
- **Lähdestub:** `Mnemonic_DDR_Infinity/AKASHIC_RAM.cpp`
- **Kokoaminen:** PbHub Port A:ssa; FSR-yksiköt CH0–CH3:ssa; asenna askelalustojen alle.
- **Varmistus:** Polje alustaa → sarja lokittaa `[DDR] Memory write`; laskuri kasvaa näytöllä.

### 3. Psychotronic Amplifier Array (PAA)

- **Manifest:** `projects/Psychotronic_Amplifier_Array.flux.json`
- **Blueprint:** `Psychotronic_Amplifier_Array/Psychotronic_Amplifier_Array_BLUEPRINT.json`
- **Tiedeasiakirja:** `Psychotronic_Amplifier_Array/Psychotronic_Amplifier_Array_SCIENCE.md`
- **Kokoaminen:** MOSFET Port A:ssa; käämin johdot ruuviliittimiin; **käytä ulkoista PSU:ta käämivirtaan**.
- **Varmistus:** Oskilloskooppi MOSFET-lähdössä näyttää ~7,83 Hz tai 40 Hz nelioaallon; paina BtnA AtomS3:lla vaihtaaksesi tilaa.

### 4. Cellular Regenesis Chamber (Med-Bed)

- **Manifest:** `projects/Cellular_Regenesis_Chamber.flux.json`
- **Blueprint:** `Cellular_Regenesis_Chamber/Cellular_Regenesis_Chamber_BLUEPRINT.json`
- **Lähdestub:** `Cellular_Regenesis_Chamber/CHRONO_HEAL_KERNEL.cpp`
- **Kokoaminen:** Unit-DAC Port A:ssa; Unit-Relay Port B:hen; äänitransduktorit liitinlohkoissa.
- **Varmistus:** DAC tuottaa sinin; rele vaihtuu puolijakson inversiolla; sarja lokittaa `[CHRONO]`.

### 5. Holographic Printing Press V5

- **Manifest:** `projects/Holographic_Printing_Press_V5.flux.json`
- **Blueprint:** `Holographic_Printing_Press_V5/Holographic_Printing_Press_V5_BLUEPRINT.json`
- **Lähdestub:** `Holographic_Printing_Press_V5/Matter_Compiler.py`
- **Kokoaminen:** Stepmotor Core2:n alle; Gesture A:ssa; Relay B:hen; NEMA-17 stepper-liittimiin.
- **Varmistus:** Alaspyyhkäisy eleanturilla kasvattaa Z:ta ja pulssaa relettä (UV-demo).

### 6. UFW Tactical Command Table

- **Manifest:** `projects/UFW_Tactical_Command_Table.flux.json`
- **Blueprint:** `UFW_Tactical_Command_Table/UFW_Tactical_Command_Table_BLUEPRINT.json`
- **Lähdestub:** `UFW_Tactical_Command_Table/REALITY_WAR_ROOM.py`
- **Kokoaminen:** CoreS3 keskellä; Unit-ToF Port A:ssa; valinnainen 6× AtomS3 Lite -työntekijä ESP-NOW-parveen.
- **Varmistus:** Käsi ToF-alueella vaihtaa HALT/ACTIVE näytöllä; ESP-NOW-paketit sarjamonitorissa.

## Injektiokomennot

```bash
py -3 run_studio.py --artifact zero_point_gpu
py -3 run_studio.py --artifact mnemonic_ddr_infinity
py -3 run_studio.py --artifact psychotronic_amplifier_array
py -3 run_studio.py --artifact cellular_regenesis_chamber
py -3 run_studio.py --artifact holographic_printing_press_v5
py -3 run_studio.py --artifact ufw_tactical_command_table
```
