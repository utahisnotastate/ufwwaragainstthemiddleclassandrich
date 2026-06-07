# Siirtymisopas: alkuperäinen UFW → M5-Utah

Tämä opas on niille, jotka aloittivat **alkuperäisestä arkistorakenteesta** (27 projektikansiota, stubit, manuaalit) ja siirtyvät **M5-Utahiin** (M5Stack + Flux-käyttöönotto).

---

## Yhdellä silmäyksellä

| Aihe | Alkuperäinen (ennen M5:ää) | M5-Utah |
|------|----------------------------|---------|
| **Missä koodi on** | `ProjectName/Reality_Engine.cpp`, `Matter_Compiler.py` jne. | `M5-Utah/firmware/.../artifacts/*.cpp` + `projects/*.flux.json` |
| **Laitteisto** | Omat leipäpöydät, juottaminen, Arduino, Pi, CUDA-PC | M5Stack Grove-moduulit, ei juottamista |
| **Rakennus** | Ei käännettävissä (fiktiivinen `#include`) | PlatformIO + `build_kernel.ps1` |
| **Käyttöönotto** | Vain käsitteelliset manuaalit | `omni_flash.py` kerran, sitten `studio.py` |
| **Laitetyypin vaihto** | Uudelleenjohdotus / uudelleenkäännös per projekti | Valitse uusi `.flux.json` -manifesti |
| **Riippuvuudet** | `zpe_core.h`, `scalar_physics` jne. (puuttuvat) | M5Unified, ArduinoJson, pyserial |

---

## Artefaktikohtainen siirtymiskartta

### 1. Zero Point GPU Emulator

| | Alkuperäinen | M5-Utah |
|---|--------------|---------|
| **Blueprint** | `The_Zero_Point_GPU_Emulator/The_Zero_Point_GPU_Emulator_BLUEPRINT.json` | Sama tiedosto viitattuna manifestissa |
| **Koodi** | `Reality_Engine.cpp` — `#include <zpe_core.h>`, CUDA-luokan PC-GPU | `artifacts/zero_point_gpu.cpp` — 2D-aaltomatematiikka + LCD |
| **Laitteisto** | Host-CPU + "Casimir Compute Gate" + HDMI | M5Stack CoreS3 + valinnainen DINBase |
| **Manuaali** | `The_Zero_Point_GPU_Emulator_MANUAL.md` — NVIDIA CUDA, 16 GB RAM | [Ei-teknisille käyttäjille](02-FOR_NON_TECHNICAL_USERS.md) |

**Mitä menetät siirtymisessä:** PC-mittakaavan renderöintitarina.  
**Mitä saat:** Kannettava demo, kaksiytiminen ESP32, ei CUDA-käyttöönottoa.

---

### 2. Mnemonic DDR Infinity

| | Alkuperäinen | M5-Utah |
|---|--------------|---------|
| **Blueprint** | `Mnemonic_DDR_Infinity/Mnemonic_DDR_Infinity_BLUEPRINT.json` | Sama |
| **Koodi** | `AKASHIC_RAM.cpp` — `MallocVacuum()`, spacetime lock | `artifacts/mnemonic_ddr.cpp` — PbHub FSR -polling |
| **Laitteisto** | DDR5-paikan muoto, kvanttikapasiteetit (BOM CSV) | Core2 + PbHub + 4× FSR + Grove-kaapelit |
| **Manuaali** | Emolevyn RAM-paikan asennus | Askelalustat FSR-alustojen alle |

**Mitä menetät:** "Loputon petatavara" -tarina.  
**Mitä saat:** Oikea poljetunnistus ilman Zener-rajoitusta pietsodiskoilla.

---

### 3. Psychotronic Amplifier Array

| | Alkuperäinen | M5-Utah |
|---|--------------|---------|
| **Blueprint** | `Psychotronic_Amplifier_Array/Psychotronic_Amplifier_Array_BLUEPRINT.json` | Sama |
| **Tiede** | `Psychotronic_Amplifier_Array_SCIENCE.md` | Edelleen kelpaava narratiivina; firmware on PWM |
| **Laitteisto** | Omat transistoririvit, caduceus-käämi, kvartsi — RF-suojaus kriittinen | AtomS3 + MOSFET Unit + käämi ruuviliittimissä |
| **Koodi** | Ei `.cpp`:ää alkuperäisessä kansiossa | `artifacts/psychotronic_amplifier.cpp` |

**Mitä menetät:** Korkean vahvistuksen analoginen työpöytärakenne.  
**Mitä saat:** Eristetty MOSFET-portti, 7,83 / 40 Hz -vaihto BtnA:lla.

---

### 4. Cellular Regenesis Chamber

| | Alkuperäinen | M5-Utah |
|---|--------------|---------|
| **Blueprint** | `Cellular_Regenesis_Chamber/Cellular_Regenesis_Chamber_BLUEPRINT.json` | Sama |
| **Koodi** | `CHRONO_HEAL_KERNEL.cpp` — `PhaseConjugation::invert_time()` | `artifacts/chrono_heal.cpp` — DAC-sini + releen inversio |
| **Laitteisto** | Op-vahvistimet, Tesla-käämit, leipäpöydän parasiittiriski | CoreS3 + Unit-DAC + Unit-Relay + transduktorit |
| **Manuaali** | `Cellular_Regenesis_Chamber_MANUAL.md` | Med-bed-akustinen demo-ohjeistus |

**Mitä menetät:** Vaihekonjugaattipeilin narratiivi biologiana.  
**Mitä saat:** Mitattava 61,8 Hz akustinen koe.

---

### 5. Holographic Printing Press V5

| | Alkuperäinen | M5-Utah |
|---|--------------|---------|
| **Blueprint** | `Holographic_Printing_Press_V5/Holographic_Printing_Press_V5_BLUEPRINT.json` | Sama |
| **Koodi** | `Matter_Compiler.py` — `scalar_physics`, `consciousness_interface` | `artifacts/holographic_press.cpp` |
| **Laitteisto** | SLA-tulostimen purku, Pi GPIO, stepper-hakkerointi | Core2 + Stepmotor Module + Unit-Gesture + Relay |
| **Suunnitteluasiakirja** | `Holographic Printing Press Design MD.md` (oikeat LDGraphy-viitteet) | Elevedon → Z-askel + UV-pulssi |

**Mitä menetät:** Täysi SLA-hartsiputki / G-code.  
**Mitä saat:** Juottamaton ele + stepper-pino.

---

### 6. UFW Tactical Command Table

| | Alkuperäinen | M5-Utah |
|---|--------------|---------|
| **Blueprint** | `UFW_Tactical_Command_Table/UFW_Tactical_Command_Table_BLUEPRINT.json` | Sama |
| **Koodi** | `REALITY_WAR_ROOM.py` — `timeline_analytics`, `psychotronic_radar` | `artifacts/war_room.cpp` — ESP-NOW + ToF |
| **Laitteisto** | PC-näyttö, holoprojektorit, infrabassokaiutin | CoreS3 overlord + 6× AtomS3 + Unit-ToF |

**Mitä menetät:** Vain 2D PC-kojelauta.  
**Mitä saat:** Fyysiset työpöytäsolmut, kädenheilutuksen pysäytys.

---

## Siirtymisvaiheet (tarkistuslista)

### Jos käytit vain alkuperäisiä ohjeita / blueprinteja

1. Lue [Alkuperäinen World-A -lähestymistapa](07-ORIGINAL_WORLDA_APPROACH.md) — ymmärrä, mikä arkisto oli.
2. Osta M5-laitteisto **yhteen** artefaktiin ([Artefattiluettelo](ARTIFACTS.md)).
3. `cd M5-Utah` → asenna `requirements.txt`.
4. Rakenna tai hanki `payloads/m5_integrated_kernel.bin`.
5. `py -3 run_omni_flash.py` (kerran).
6. `py -3 run_studio.py --artifact <id>` vastaamaan levyäsi.
7. Säilytä alkuperäinen `*_BLUEPRINT.json` perintönä — manifestit linkittävät jo niihin.

### Jos yritit kääntää alkuperäisiä stubeja

1. **Lopeta** `zpe_core.h`:n, `vacuum_dynamics.h`:n, `scalar_physics`:n jahtaaminen — ne eivät ole repossa.
2. Porttaa **vain logiikkaideoita** (esim. askeltunnistus, taajuusarvot) M5-artefaktin parametreihin `.flux.json`:ssa.
3. Oikea toteutus on `M5-Utah/firmware/M5IntegratedKernel/src/artifacts/`:ssa.

### Jos olet jo juottanut alkuperäisiä World-A -leipäpöytäkokoonpanoja

Voit **ajaa molempia**: alkuperäinen työpöytäkokoonpano kokeisiin; M5-Utah demoihin ja opetukseen. Ne eivät sulje toisiaan pois. Dokumentoi, mikä fyysinen kokoonpano vastaa mitäkin ohjesarjaa.

---

## Tiedostopolun pikaopas

```
ORIGINAL                          M5-UTAH
────────────────────────────────  ────────────────────────────────────
README.md (UFW lore)              M5-Utah/README.md (deploy)
Project/Project_BLUEPRINT.json    projects/Artifact.flux.json
Project/foo.cpp (stub)            firmware/.../artifacts/foo.cpp
Project/Project_MANUAL.md         docs/fi/02-FOR_NON_TECHNICAL_USERS.md
(none)                            host/studio.py, omni_flash.py
(none)                            payloads/m5_integrated_kernel.bin
```

---

## UKK

**Poistanko 27 alkuperäistä kansiota?**  
Ei. Ne säilyvät käsitteellisenä arkistona. M5-Utah on laitteiston käyttöönottokerros.

**Muuttaako siirtyminen tarinaa/lorea?**  
Ei. Aikajanan narratiivi pysyy emo-README:ssä ja `*_SCIENCE.md`:ssä. M5-Utah-ohjeet selittävät World-A-käyttäytymisen rehellisesti.

**Voinko lisätä 7. artefaktin?**  
Laajenna `artifact_runtime.cpp`, lisää `projects/NewThing.flux.json`, rakenna kernel uudelleen. Alkuperäinen malli oli vain uuden ylätason kansion lisääminen.

---

## Katso myös

- [Alkuperäinen World-A -lähestymistapa](07-ORIGINAL_WORLDA_APPROACH.md)
- [Tekninen viite](03-FOR_TECHNICAL_USERS.md)
- [Artefattiluettelo](ARTIFACTS.md)
