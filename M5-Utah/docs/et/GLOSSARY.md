# Sõnastik

Lihtsad definitsioonid M5-Utah ja laiemas UFW arhiivis kasutatavate terminite jaoks.

| Termin | Tähendus |
|--------|----------|
| **Artifact** | Seadme režiim — nt sammupadja juhtimine, laineekraan, žestiprinter. Vali üks `studio.py` abil. |
| **Blueprint** | JSON-fail vanemrepos, mis kirjeldab artefakti kontseptuaalseid komponente (`*_BLUEPRINT.json`). |
| **ESP32** | Mikrokontroller M5Stack seadmete sees. Käivitab kerneli püsivara. |
| **Flux manifest** | `.flux.json` fail, mis ütleb seadmele, millist artefakti käivitada ja milliste seadetega. |
| **FSR** | Force Sensitive Resistor — padi, mis tunneb, kui sa sellele astud. |
| **Grove cable** | Värviline pistikkaabel M5Stack üksuste jaoks (jootmine pole vaja). |
| **I2C** | Kahejuhtmeline siin lisamoodulitega suhtlemiseks (PbHub, DAC, andurid). |
| **JIT injection** | Manifesti saatmine USB kaudu, et seade vahetaks režiimi ilma uuesti kirjutamata. |
| **Kernel / Lazarus Kernel** | `M5IntegratedKernel` — baaspüsivara, mida kirjutatakse üks kord; võtab manifeste pärast. |
| **Manifest** | Sama mis Flux manifest. |
| **M5Stack** | Modulaarsete ESP32 vidinate bränd (ekraanid, andurid, virndatavad üksused). |
| **Omni-Flash** | `omni_flash.py` — tööriist, mis kirjutab kerneli tühjale M5Stackile. |
| **PbHub** | M5Stack üksus, mis loeb kuni 6 analoogandurit I2C kaudu. |
| **PSRAM** | Lisamälu mõnel ESP32 plaadil suuremate puhverite jaoks. |
| **Sovereign Node** | Projekti nimetus M5Stacki jaoks, mis käivitab Lazarus Kerneli. |
| **Studio / Utah Flux Host** | `studio.py` — tööriist manifestide loetlemiseks ja süstimiseks. |
| **UFW** | Utah Future Weapons — selle repo projektipere nimi. |
| **World-A** | Repo termin tänapäevase, füüsiliselt ehitatava paigutuse jaoks (vs ajajoone loor). |
| **Zero-click** | Lõppkasutaja ei ava Arduino IDE-d ega kompileeri koodi. |

## Loori terminid (narratiiv — mitte insenerispetsifikatsioonid)

Need ilmuvad blueprintides ja loos. Need on **projekti sõnavara**, mitte kontrollitud füüsika:

- Akashic Record / Cloud
- Phase-conjugate / Priore Effect (med-bed väitena)
- Psychotronic / scalar waves
- Zero Point Energy (ZPE) lõputu energiaallikana
- Vacuum memory / spacetime locking

Vaata [Teadlastele](04-FOR_SCIENTISTS.md) ja [Skeptikutele](05-FOR_SKEPTICS.md), kuidas need kaardistuvad päris riistvara käitumisele.
