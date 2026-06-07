# Sanasto

Selkeät määritelmät M5-Utahissa ja laajemmassa UFW-arkistossa käytetyille termeille.

| Termi | Merkitys |
|-------|----------|
| **Artifact** | Laitetila — esim. askelalustaohjain, aaltonäyttö, ele-tulostin. Valitse yksi `studio.py`:ssä. |
| **Blueprint** | JSON-tiedosto emorepossa, joka kuvaa artefaktin käsitteelliset komponentit (`*_BLUEPRINT.json`). |
| **ESP32** | Mikrokontrolleri M5Stack-laitteiden sisällä. Ajaa kernel-firmwarea. |
| **Flux manifest** | `.flux.json`-tiedosto, joka kertoo laitteelle, mitä artefaktia ajaa ja millä asetuksilla. |
| **FSR** | Force Sensitive Resistor — alusta, joka tunnistaa, kun poljet sitä. |
| **Grove cable** | Värikoodattu liitinjohto M5Stack-yksiköille (ei juottamista). |
| **I2C** | Kaksijohtoinen väylä lisämoduuleille (PbHub, DAC, anturit). |
| **JIT injection** | Manifestin lähetys USB:n yli, jotta laite vaihtaa tilaa ilman uudelleenflashausta. |
| **Kernel / Lazarus Kernel** | `M5IntegratedKernel` — perusfirmware flashataan kerran; vastaanottaa manifestit sen jälkeen. |
| **Manifest** | Sama kuin Flux manifest. |
| **M5Stack** | Modulaaristen ESP32-laitteiden brändi (näytöt, anturit, pinottavat yksiköt). |
| **Omni-Flash** | `omni_flash.py` — työkalu, joka flashaa kernelin tyhjälle M5Stackille. |
| **PbHub** | M5Stack-yksikkö, joka lukee jopa 6 analogista anturia I2C:n yli. |
| **PSRAM** | Lisä-RAM joillakin ESP32-levyillä suurempiin puskureihin. |
| **Sovereign Node** | Projektissa käytetty nimi M5Stackille, joka ajaa Lazarus Kerneliä. |
| **Studio / Utah Flux Host** | `studio.py` — työkalu, joka listaa ja injektoi manifestit. |
| **UFW** | Utah Future Weapons — tämän repon projektiperheen nimi. |
| **World-A** | Repossa käytetty termi nykyajan, fyysisesti rakennettavalle käyttöönotolle (vs. aikajanan lore). |
| **Zero-click** | Loppukäyttäjä ei avaa Arduino IDE:tä eikä käänä koodia. |

## Lore-termiä (narratiivi — ei insinöörispesifikaatioita)

Nämä esiintyvät blueprinteissa ja tarinatekstissä. Ne ovat **projektin sanastoa**, ei varmennettua fysiikkaa:

- Akashic Record / Cloud
- Phase-conjugate / Priore Effect (med-bed-väitteenä)
- Psychotronic / scalar waves
- Zero Point Energy (ZPE) loputtomana energialähteenä
- Vacuum memory / spacetime locking

Katso [Tutkijoille](04-FOR_SCIENTISTS.md) ja [Skeptikoille](05-FOR_SKEPTICS.md), miten nämä kartoituvat oikeaan laitteiston käyttäytymiseen.
