# Alkuperäinen World-A -lähestymistapa (ennen M5Stackia)

Ennen **M5-Utahia** UFW-repo oli järjestetty **tasaisena 27 projektin arkistona**. Tämä asiakirja kuvaa alkuperäisen rakenteen, jotta voit verrata sitä M5-siirtymispolkuun.

---

## Reporakenne (alkuperäinen)

```
ufwwaragainstthemiddleclassandrich/
├── README.md
├── The_Zero_Point_GPU_Emulator/
│   ├── The_Zero_Point_GPU_Emulator_BLUEPRINT.json
│   ├── The_Zero_Point_GPU_Emulator_MANUAL.md
│   ├── The_Zero_Point_GPU_Emulator_SCIENCE.md
│   ├── Reality_Engine.cpp          ← stub, ei käännettävissä
│   └── The_Zero_Point_GPU_Emulator_LANDING.html
├── Mnemonic_DDR_Infinity/
│   ├── Mnemonic_DDR_Infinity_BLUEPRINT.json
│   ├── Mnemonic_DDR_Infinity_BOM.csv
│   ├── AKASHIC_RAM.cpp
│   └── ...
├── ... (25 muuta projektia, sama malli)
└── (ei M5-Utah/, ei build-järjestelmää)
```

Jokainen projekti sisälsi tyypillisesti:

| Tiedostotyyppi | Tarkoitus |
|----------------|-----------|
| `*_BLUEPRINT.json` | Komponenttigraafi / geometriapuu |
| `*_SCIENCE.md` | Validointinarratiivi, yhtälöt, mermaid |
| `*_MANUAL.md` | Asennus- ja käyttöohjeet |
| `*_3D.json` | Kohtauksen metatiedot |
| `*_LANDING.html` | Staattinen promosivu |
| `*.cpp` / `*.py` | Käsitteellinen koodi **fiktiivisillä importeilla** |

Ei ollut `requirements.txt`:ää, PlatformIO:ta tai yhtenäistä flash-työkalua.

---

## Miten alkuperäisen mukaan piti rakentaa (alkuperäinen spesifikaatio)

Batch 1–2 -suunnitteludokumentit (ennen M5-siirtymää) kuvasivat **käsin rakennettuja World-A** -kokoonpanoja:

### Zero Point GPU
- **Ohjelmistopolku:** Käännä `Reality_Engine.cpp` tyhjiö/GPU-kirjastoa vasten **CUDA-luokan PC:llä**.
- **Manuaali sanoo:** NVIDIA GPU, 16 GB RAM, GCC, CUDA Toolkit.
- **Todellisuus:** `zpe_core.h` ei ole repossa.

### Mnemonic DDR Infinity
- **Laitteistopolku:** DDR5-tikun muoto TAI pietsosähköiset poljetuskiekot **Arduinolla**.
- **Ongelma:** Oma jänniterajoitus (Zenerit, pull-downit), leipäpöydän kohina.
- **BOM CSV:** Oikeita osia (Kingston DDR, Murata-kondensaattorit) sekoitettuna fiktiiviseen "kvanttikätköön".

### Psychotronic Amplifier Array
- **Laitteistopolku:** Käsin juotetut korkean vahvistuksen transistorit, caduceus-käämi, kvartsiresonaattori.
- **Ongelma:** RF-kohina ("fotonien sammutus") ilman huolellista suojausta.
- **Dokumentit:** `Psychotronic_Amplifier_Array_SCIENCE.md` (luottamus 0,94) — narratiivi, ei firmwarea.

### Cellular Regenesis Chamber
- **Laitteistopolku:** Paljaat op-vahvistimet, omat Tesla-käämit, vaihekonjugaattipeili leipäpöydällä.
- **Koodi:** `CHRONO_HEAL_KERNEL.cpp` → `#include <phase_conjugation.h>` (puuttuu).
- **Lisäksi:** `Telomere_Restore.cpp`, OpenSCAD-pod-geometria.

### Holographic Printing Press V5
- **Laitteistopolku:** Purkaa **SLA 3D -tulostin** moottoriohjaimet **Raspberry Pi GPIO:n** kautta.
- **Ohjelmisto:** `Matter_Compiler.py` → `scalar_physics`, `consciousness_interface` (puuttuvat).
- **Oikea insinöörityö:** `Holographic Printing Press Design MD.md` viittaa LDGraphy-tyyliseen suunnitteluun.

### UFW Tactical Command Table
- **Laitteistopolku:** PC-näyttö "God-Eye" -kojelautana.
- **Ohjelmisto:** `REALITY_WAR_ROOM.py` → `timeline_analytics`, `psychotronic_radar` (puuttuvat).
- **Rajoitus:** Vain 2D-näyttö; ei fyysisiä parvisolmuja.

---

## Alkuperäinen työnkulku (tyypillinen käyttäjä)

1. Kloonaa repo, avaa projektikansio.
2. Lue `*_MANUAL.md` ja `*_BLUEPRINT.json`.
3. Yritä kääntää `*.cpp` tai ajaa `*.py` → **epäonnistuu** puuttuviin moduuleihin.
4. Valinnainen: rakenna **inspiroitunut** leipäpöytä BOM:sta / tiedeasiakirjasta.
5. Lue juuri `README.md` UFW:n talous- / aikajananarratiivista.

**Varmistustarina:** Juuri README:n "käyttökelpoinen koodi" viittasi **käsitteellisiin** käyttökelpoisiin blueprinteihin, ei yhteen toimivaan binääriin.

---

## Alkuperäinen vs. M5-Utah (yhteenveto)

| Ulottuvuus | Alkuperäinen World-A | M5-Utah |
|------------|----------------------|---------|
| **Kokoaminen** | Juotto, johdotus, jännitteen rajoitus | Grove-kaapelit, ruuviliittimet |
| **Työkaluketju** | Arduino IDE, PlatformIO per projekti, CUDA, Pi | Yksi kernel + manifestin injektio |
| **Koodin tila** | Stubit + lore | Käännettävä firmware + Python-host |
| **Projektimäärä** | 27 arkistoa | 6 käyttöönotettua artefaktia (lisää suunniteltu) |
| **Käyttäjän taito** | EE + ohjelmisto | Kytke USB, valitse listasta |
| **Blueprintin rooli** | Ensisijainen spesifikaatio | Linkitetty perintö `.flux.json`:ssa |
| **Rehellinen demo** | Vaati oman tulkinnan | Dokumentoitu Tutkijoille / Skeptikoille -oppaissa |

---

## Milloin käyttää alkuperäisiä ohjeita tänään

| Käytä alkuperäistä | Käytä M5-Utahia |
|--------------------|-----------------|
| Lore, tieteisfiktio, viitteet | Flashaa laitteisto oikeasti |
| OpenSCAD / 3D-geometria | Askelalustat, aallot, eleet työpöydällä |
| Täysi 27 projektin luettelo | Kuusi MVP-artefaktia |
| Kirjoita papereita **narratiivista** | Instrumentoidut **mittaus**protokollat |

---

## Siirtyminen eteenpäin

Katso **[Siirtymisopas](06-MIGRATION_FROM_ORIGINAL.md)** vaiheittaiseen muunnokseen alkuperäisistä kansioista M5-Utah-manifesteihin.

---

## Katso myös

- [Dokumentaation keskus](README.md)
- [Artefattiluettelo](ARTIFACTS.md) — M5 BOM rinnakkain blueprint-polkuineen
- Emorepon `README.md` — muuttumaton UFW-tehtävälausunto
