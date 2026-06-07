# Algne World-A lähenemine (enne M5Stacki)

Enne **M5-Utah** oli UFW repo korraldatud **tasase arhiivina 27 projektist**. See dokument kirjeldab seda algset paigutust, et saaksid võrrelda M5 migratsiooniteega.

---

## Repo kuju (algne)

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

Iga projekt sisaldas tavaliselt:

| Failitüüp | Eesmärk |
|-----------|---------|
| `*_BLUEPRINT.json` | Komponentide graaf / geomeetriapuu |
| `*_SCIENCE.md` | Valideerimise narratiiv, võrrandid, mermaid |
| `*_MANUAL.md` | Paigaldus- ja kasutusjuhend |
| `*_3D.json` | Stseeni metaandmed |
| `*_LANDING.html` | Staatiline tutvustusleht |
| `*.cpp` / `*.py` | Kontseptuaalne kood **fiktiivsete importidega** |

**Pole** `requirements.txt`, PlatformIO ega ühtset flash-tööriista.

---

## Kuidas pidid ehitama (algne spetsifikatsioon)

Partii 1–2 disainibriifid (enne M5 migratsiooni) kirjeldasid **käsitsi ehitatud World-A** seadmeid:

### Zero Point GPU
- **Tarkvaratee:** Kompileeri `Reality_Engine.cpp` vaakum/GPU teegi vastu **CUDA-klassi PC-l**.
- **Manual ütleb:** NVIDIA GPU, 16 GB RAM, GCC, CUDA Toolkit.
- **Reaalsus:** `zpe_core.h` repos ei eksisteeri.

### Mnemonic DDR Infinity
- **Riistvaratee:** DDR5 pulga vorm või piezoelektrilised tammukettad **Arduinol**.
- **Probleem:** Kohandatud pinge piiramine (Zenerid, pull-downid), prototüüpplaadi müra.
- **BOM CSV:** Päris osad (Kingston DDR, Murata kondensaatorid) segatud fiktiivse „quantum cache“-iga.

### Psychotronic Amplifier Array
- **Riistvaratee:** Käsitsi jootatud kõrge võimendusega transistorid, caduceus mähis, kvartsresonaator.
- **Probleem:** RF müra („photon quenching“) ilma hoolika varjestuseta.
- **Dokumendid:** `Psychotronic_Amplifier_Array_SCIENCE.md` (usaldusskoor 0.94) — narratiiv, mitte püsivara.

### Cellular Regenesis Chamber
- **Riistvaratee:** Avatud op-ampid, kohandatud Tesla mähised, faasikonjugaat peegel prototüüpplaadil.
- **Kood:** `CHRONO_HEAL_KERNEL.cpp` → `#include <phase_conjugation.h>` (puudub).
- **Samuti:** `Telomere_Restore.cpp`, OpenSCAD podi geomeetria.

### Holographic Printing Press V5
- **Riistvaratee:** Pöördprojekteeri **SLA 3D-printeri** mootorijuhtimised **Raspberry Pi GPIO** kaudu.
- **Tarkvara:** `Matter_Compiler.py` → `scalar_physics`, `consciousness_interface` (puuduvad).
- **Päris inseneritöö:** `Holographic Printing Press Design MD.md` viitab LDGraphy-stiilis disainile.

### UFW Tactical Command Table
- **Riistvaratee:** PC monitor „God-Eye“ armatuurlaud.
- **Tarkvara:** `REALITY_WAR_ROOM.py` → `timeline_analytics`, `psychotronic_radar` (puuduvad).
- **Piirang:** Ainult 2D ekraan; füüsilised swarm-sõlmed puuduvad.

---

## Algne töövoog (tüüpiline kasutaja)

1. Klooni repo, ava projektikaust.
2. Loe `*_MANUAL.md` ja `*_BLUEPRINT.json`.
3. Proovi kompileerida `*.cpp` või käivitada `*.py` → **ebaõnnestub** puuduvate moodulite tõttu.
4. Valikuliselt ehita **inspireeritud** prototüüpplaat BOM / science dokumendi järgi.
5. Loe juur-README UFW majandus-/ajajoone narratiivi jaoks.

**Verifikatsiooni lugu:** „Kasutatav kood“ juur-README-s viitas **kontseptuaalselt** kasutatavatele blueprintidele, mitte ühele töötavale binaarile.

---

## Algne vs M5-Utah (kokkuvõte)

| Dimensioon | Algne World-A | M5-Utah |
|------------|---------------|---------|
| **Kokkupanek** | Jootmine, juhtmestik, pinge klambrid | Grove kaablid, kruvi klemmid |
| **Tööriistaahel** | Arduino IDE, PlatformIO projekti kohta, CUDA, Pi | Üks kernel + manifesti süstimine |
| **Koodi olek** | Stubid + loor | Kompileeritav püsivara + Python host |
| **Projektide arv** | 27 arhiivi | 6 paigutatud artefakti (rohkem planeeritud) |
| **Kasutaja oskus** | EE + tarkvara | Ühenda USB, vali nimekirjast |
| **Blueprinti roll** | Peamine spetsifikatsioon | Lingitud päritolu `.flux.json` failis |
| **Aus demo** | Nõudis iseinterpretatsiooni | Dokumenteeritud Teadlaste / Skeptikute juhendites |

---

## Millal kasutada algseid dokumente täna

| Kasuta algset | Kasuta M5-Utah |
|---------------|----------------|
| Loor, ulme, tsitaadid | Tõesti kirjuta riistvara |
| OpenSCAD / 3D geomeetria | Sammupadjad, lained, žestid laual |
| Täielik 27-projekti kataloog | Kuus MVP artefakti |
| Artiklite kirjutamine **narratiivist** | Instrumenteeritud **mõõtmis**protokollid |

---

## Edasi liikumine

Vaata **[Migratsioonijuhendit](06-MIGRATION_FROM_ORIGINAL.md)** samm-sammult üleminekuks algsetest kaustadest M5-Utah manifestidele.

---

## Vaata ka

- [Dokumentatsiooni keskus](README.md)
- [Artefaktide kataloog](ARTIFACTS.md) — M5 BOM kõrvuti blueprint teedega
- Vanemrepo `README.md` — muutmata UFW missioonideklaratsioon
