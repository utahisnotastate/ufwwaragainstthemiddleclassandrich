# Migratsioonijuhend: algne UFW → M5-Utah

See juhend on neile, kes alustasid **algse arhiivi paigutusega** (27 projektikausta, stubid, manualid) ja liiguvad **M5-Utah** peale (M5Stack + Flux paigutus).

---

## Ülevaade

| Teema | Algne (enne M5) | M5-Utah |
|-------|-----------------|---------|
| **Kus kood elab** | `ProjectName/Reality_Engine.cpp`, `Matter_Compiler.py` jne | `M5-Utah/firmware/.../artifacts/*.cpp` + `projects/*.flux.json` |
| **Riistvara** | Kohandatud prototüüpplaadid, jootmine, Arduino, Pi, CUDA PC | M5Stack Grove moodulid, jootmine pole vaja |
| **Ehitamine** | Ei kompileeru (fiktiivne `#include`) | PlatformIO + `build_kernel.ps1` |
| **Paigutus** | Ainult kontseptuaalsed manualid | `omni_flash.py` üks kord, seejärel `studio.py` |
| **Seadme tüübi vahetus** | Uuesti juhtmestik / kompileerimine projekti kohta | Vali uus `.flux.json` manifest |
| **Sõltuvused** | `zpe_core.h`, `scalar_physics` jne (puuduvad) | M5Unified, ArduinoJson, pyserial |

---

## Artefaktipõhine migratsioonikaart

### 1. Zero Point GPU Emulator

| | Algne | M5-Utah |
|---|-------|---------|
| **Blueprint** | `The_Zero_Point_GPU_Emulator/The_Zero_Point_GPU_Emulator_BLUEPRINT.json` | Sama fail viidatud manifestis |
| **Kood** | `Reality_Engine.cpp` — `#include <zpe_core.h>`, CUDA-klassi PC GPU | `artifacts/zero_point_gpu.cpp` — 2D laine matemaatika + LCD |
| **Riistvara** | Host CPU + „Casimir Compute Gate“ + HDMI | M5Stack CoreS3 + valikuline DINBase |
| **Manual** | `The_Zero_Point_GPU_Emulator_MANUAL.md` — NVIDIA CUDA, 16 GB RAM | [Mittetehnilistele kasutajatele](02-FOR_NON_TECHNICAL_USERS.md) |

**Mida migratsioonil kaotad:** PC-mastaabis renderdamise narratiiv.  
**Mida saad:** Kaasaskantav demo, kahetuumaline ESP32, null CUDA seadistust.

---

### 2. Mnemonic DDR Infinity

| | Algne | M5-Utah |
|---|-------|---------|
| **Blueprint** | `Mnemonic_DDR_Infinity/Mnemonic_DDR_Infinity_BLUEPRINT.json` | Sama |
| **Kood** | `AKASHIC_RAM.cpp` — `MallocVacuum()`, spacetime lock | `artifacts/mnemonic_ddr.cpp` — PbHub FSR polling |
| **Riistvara** | DDR5 pesade vorm, quantum cache kondensaatorid (BOM CSV) | Core2 + PbHub + 4× FSR + Grove kaablid |
| **Manual** | Emaplaadi RAM-pesa paigaldus | Sammumisplaadid FSR padjade all |

**Mida kaotad:** „Lõputu petabait“ lugu.  
**Mida saad:** Päris tammumise tuvastus ilma Zeneri piiramiseta piezo ketastel.

---

### 3. Psychotronic Amplifier Array

| | Algne | M5-Utah |
|---|-------|---------|
| **Blueprint** | `Psychotronic_Amplifier_Array/Psychotronic_Amplifier_Array_BLUEPRINT.json` | Sama |
| **Science** | `Psychotronic_Amplifier_Array_SCIENCE.md` | Kehtib narratiivina; püsivara on PWM |
| **Riistvara** | Kohandatud transistormassiivid, caduceus mähis, kvarts — RF varjestus kriitiline | AtomS3 + MOSFET Unit + mähis kruvi klemmides |
| **Kood** | Algse kaustas pole `.cpp` | `artifacts/psychotronic_amplifier.cpp` |

**Mida kaotad:** Kõrge võimendusega analoogne töölaud.  
**Mida saad:** Isoleeritud MOSFET värav, 7.83 / 40 Hz lüliti BtnA-ga.

---

### 4. Cellular Regenesis Chamber

| | Algne | M5-Utah |
|---|-------|---------|
| **Blueprint** | `Cellular_Regenesis_Chamber/Cellular_Regenesis_Chamber_BLUEPRINT.json` | Sama |
| **Kood** | `CHRONO_HEAL_KERNEL.cpp` — `PhaseConjugation::invert_time()` | `artifacts/chrono_heal.cpp` — DAC siinus + relee invert |
| **Riistvara** | Op-ampid, Tesla mähised, prototüüpplaadi parasiitne risk | CoreS3 + Unit-DAC + Unit-Relay + transduktorid |
| **Manual** | `Cellular_Regenesis_Chamber_MANUAL.md` | Med-bed akustiline demo dokumentatsioon |

**Mida kaotad:** Faasikonjugaat peegli narratiiv bioloogiana.  
**Mida saad:** Mõõdetav 61.8 Hz akustiline katse.

---

### 5. Holographic Printing Press V5

| | Algne | M5-Utah |
|---|-------|---------|
| **Blueprint** | `Holographic_Printing_Press_V5/Holographic_Printing_Press_V5_BLUEPRINT.json` | Sama |
| **Kood** | `Matter_Compiler.py` — `scalar_physics`, `consciousness_interface` | `artifacts/holographic_press.cpp` |
| **Riistvara** | SLA printeri lahtivõtmine, Pi GPIO, stepperi häkkimine | Core2 + Stepmotor Module + Unit-Gesture + Relay |
| **Disainidokument** | `Holographic Printing Press Design MD.md` (päris LDGraphy viited) | Žesti tõmbamine → Z samm + UV impulss |

**Mida kaotad:** Täielik vaigu SLA torustik / G-code.  
**Mida saad:** Jooteta žest + stepper virn.

---

### 6. UFW Tactical Command Table

| | Algne | M5-Utah |
|---|-------|---------|
| **Blueprint** | `UFW_Tactical_Command_Table/UFW_Tactical_Command_Table_BLUEPRINT.json` | Sama |
| **Kood** | `REALITY_WAR_ROOM.py` — `timeline_analytics`, `psychotronic_radar` | `artifacts/war_room.cpp` — ESP-NOW + ToF |
| **Riistvara** | PC monitor, holo projektorid, infrasound woofer | CoreS3 overlord + 6× AtomS3 + Unit-ToF |

**Mida kaotad:** Ainult 2D PC armatuurlaud.  
**Mida saad:** Füüsilised lauasõlmed, käeliigutusega peatamine.

---

## Migratsiooni sammud (kontrollnimekiri)

### Kui kasutasid ainult algseid dokumente / blueprinte

1. Loe [Algne World-A lähenemine](07-ORIGINAL_WORLDA_APPROACH.md) — mõista, mis arhiiv oli.
2. Osta M5 riistvara **ühe** artefakti jaoks ([Artefaktide kataloog](ARTIFACTS.md)).
3. `cd M5-Utah` → paigalda `requirements.txt`.
4. Ehita või hanki `payloads/m5_integrated_kernel.bin`.
5. `py -3 run_omni_flash.py` (üks kord).
6. `py -3 run_studio.py --artifact <id>` vastavalt sinu plaadile.
7. Säilita algne `*_BLUEPRINT.json` päritoluna — manifestid viitavad neile juba.

### Kui proovisid kompileerida algseid stube

1. **Lõpeta** `zpe_core.h`, `vacuum_dynamics.h`, `scalar_physics` tagaajamine — neid repos pole.
2. Porti **ainult loogikaideed** (nt sammutuvastus, sagedusväärtused) M5 artefakti parameetritesse `.flux.json` failis.
3. Päris implementatsioon on `M5-Utah/firmware/M5IntegratedKernel/src/artifacts/` all.

### Kui jootsid juba algseid World-A prototüüpplaate

Saad **mõlemat kasutada**: algne töölaud katseteks; M5-Utah demodeks ja õpetamiseks. Need ei välista teineteist. Dokumenteeri, milline füüsiline seadistus vastab millisele dokumendikogule.

---

## Failiteede võrdlustabel

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

## KKK

**Kas kustutan 27 algset kausta?**  
Ei. Need jäävad kontseptuaalseks arhiiviks. M5-Utah on riistvara paigutuse kiht.

**Kas migratsioon muudab lugu/loori?**  
Ei. Ajajoone narratiiv jääb vanema README ja `*_SCIENCE.md` failidesse. M5-Utah dokumendid selgitavad World-A käitumist ausalt.

**Kas saan lisada 7. artefakti?**  
Laienda `artifact_runtime.cpp`, lisa `projects/NewThing.flux.json`, ehita kernel uuesti. Algne muster oli ainult uue tipptaseme kausta lisamine.

---

## Vaata ka

- [Algne World-A lähenemine](07-ORIGINAL_WORLDA_APPROACH.md)
- [Tehniline viide](03-FOR_TECHNICAL_USERS.md)
- [Artefaktide kataloog](ARTIFACTS.md)
