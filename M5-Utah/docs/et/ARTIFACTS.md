# Artefaktide kataloog

Kuus UFW artefakti on täna M5-Utah kaudu paigutatavad. Iga rida loetleb **mida osta**, **mida seade World-A-s tegelikult teeb** ja **kus algne blueprint asub**.

## Kokkuvõtetabel

| # | Nimi | M5 plaat | Lisad | World-A käitumine |
|---|------|----------|-------|-------------------|
| 1 | Zero Point GPU Emulator | CoreS3 | DINBase (valikuline jahutus) | Animeeritud laineruut ekraanil; matemaatika ühel CPU tuumal, joonistamine teisel |
| 2 | Mnemonic DDR Infinity | Core2 | PbHub + 4× FSR + Grove kaablid | Sammupadjad käivitavad „memory write“ sündmused; loendur ekraanil |
| 3 | Psychotronic Amplifier Array | AtomS3 | MOSFET Unit + käsitsi keritud mähis | PWM oscillator 7.83 Hz või 40 Hz; väline toiteplokk juhib mähise |
| 4 | Cellular Regenesis Chamber | CoreS3 | Unit-DAC + Unit-Relay + transduktorid | 61.8 Hz siinus DAC-il; invert. faas releel akustiliste katsete jaoks |
| 5 | Holographic Printing Press V5 | Core2 | Stepmotor + Unit-Gesture + Unit-Relay | Käeliigutus tuvastatud → Z-samm loendur + UV relee impulss (demo) |
| 6 | UFW Tactical Command Table | CoreS3 | Unit-ToF + 6× AtomS3 Lite (swarm) | ESP-NOW leviedastus; ToF käeliigutus lülitab halt/execute (overlord node) |

## Artefaktipõhine detail

### 1. Zero Point GPU Emulator

- **Manifest:** `projects/Zero_Point_GPU.flux.json`
- **Blueprint:** `The_Zero_Point_GPU_Emulator/The_Zero_Point_GPU_Emulator_BLUEPRINT.json`
- **Lähtestub:** `The_Zero_Point_GPU_Emulator/Reality_Engine.cpp`
- **Kokkupanek:** Snap CoreS3 DINBase'ile; USB-C arvutisse.
- **Kontroll:** Ekraan näitab elavat värvilist ruudustikku; jadaport prindib kaadri uuendusi.

### 2. Mnemonic DDR Infinity (Step Machine)

- **Manifest:** `projects/Mnemonic_DDR_Infinity.flux.json`
- **Blueprint:** `Mnemonic_DDR_Infinity/Mnemonic_DDR_Infinity_BLUEPRINT.json`
- **Lähtestub:** `Mnemonic_DDR_Infinity/AKASHIC_RAM.cpp`
- **Kokkupanek:** PbHub Port A-s; FSR üksused CH0–CH3; paigalda sammumisplaatide alla.
- **Kontroll:** Samm padjale → jadaport logib `[DDR] Memory write`; loendur suureneb ekraanil.

### 3. Psychotronic Amplifier Array (PAA)

- **Manifest:** `projects/Psychotronic_Amplifier_Array.flux.json`
- **Blueprint:** `Psychotronic_Amplifier_Array/Psychotronic_Amplifier_Array_BLUEPRINT.json`
- **Teadusdokument:** `Psychotronic_Amplifier_Array/Psychotronic_Amplifier_Array_SCIENCE.md`
- **Kokkupanek:** MOSFET Port A-s; mähise juhtmed kruvi klemmides; **kasuta välist toiteplokki mähise voolu jaoks**.
- **Kontroll:** Ostsilloskoop MOSFET väljundil näitab ~7.83 Hz või 40 Hz ruutlaine; vajuta BtnA AtomS3-l režiimi vahetamiseks.

### 4. Cellular Regenesis Chamber (Med-Bed)

- **Manifest:** `projects/Cellular_Regenesis_Chamber.flux.json`
- **Blueprint:** `Cellular_Regenesis_Chamber/Cellular_Regenesis_Chamber_BLUEPRINT.json`
- **Lähtestub:** `Cellular_Regenesis_Chamber/CHRONO_HEAL_KERNEL.cpp`
- **Kokkupanek:** Unit-DAC Port A-s; Unit-Relay Port B-s; helitransduktorid klemmplokkidel.
- **Kontroll:** DAC väljastab siinuse; relee lülitub poole tsükli inversiooniga; jadaport logib `[CHRONO]`.

### 5. Holographic Printing Press V5

- **Manifest:** `projects/Holographic_Printing_Press_V5.flux.json`
- **Blueprint:** `Holographic_Printing_Press_V5/Holographic_Printing_Press_V5_BLUEPRINT.json`
- **Lähtestub:** `Holographic_Printing_Press_V5/Matter_Compiler.py`
- **Kokkupanek:** Stepmotor Core2 all; Gesture A-s; Relay B-s; NEMA-17 stepperi klemmidel.
- **Kontroll:** Allapoole liigutus žestianduril suurendab Z-d ja impulssib releed (UV demo).

### 6. UFW Tactical Command Table

- **Manifest:** `projects/UFW_Tactical_Command_Table.flux.json`
- **Blueprint:** `UFW_Tactical_Command_Table/UFW_Tactical_Command_Table_BLUEPRINT.json`
- **Lähtestub:** `UFW_Tactical_Command_Table/REALITY_WAR_ROOM.py`
- **Kokkupanek:** CoreS3 keskel; Unit-ToF Port A-s; valikuline 6× AtomS3 Lite worker ESP-NOW swarmi jaoks.
- **Kontroll:** Käsi ToF ulatuses lülitab HALT/ACTIVE ekraanil; ESP-NOW paketid jadapordi monitoris.

## Süstimiskäsud

```bash
py -3 run_studio.py --artifact zero_point_gpu
py -3 run_studio.py --artifact mnemonic_ddr_infinity
py -3 run_studio.py --artifact psychotronic_amplifier_array
py -3 run_studio.py --artifact cellular_regenesis_chamber
py -3 run_studio.py --artifact holographic_printing_press_v5
py -3 run_studio.py --artifact ufw_tactical_command_table
```
