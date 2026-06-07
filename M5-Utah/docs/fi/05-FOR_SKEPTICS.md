# M5-Utah-opas skeptikoille

Olet oikeassa kysyessäsi vaikeita kysymyksiä. Tämä sivu vastaa niihin suoraan — aikajanaslangia ei tarvita.

---

## Lyhyt vastaus

**Tämä repo sisältää kaksi eri asiaa:**

1. **Luova/tieteisfiktioarkisto** (27 "UFW-aseita", taloudellinen satiiri, aikajanan lore) stub-koodilla, joka viittaa kuvitteellisiin kirjastoihin.
2. **Pieni, oikea sulautettu projekti** (`M5-Utah/`), joka flashaa ESP32-levyjä ja ajaa **tavallisia demoja**: anturit, PWM, ääni, eleet, radiopaketit.

Toinen **ei todista** ensimmäisen poikkeuksellisia väitteitä.

---

## Mikä on oikeasti todellista?

| Väite markkinoinnissa/loressa | Mitä laitteisto oikeasti tekee |
|-------------------------------|--------------------------------|
| "Zero Point GPU — loputon FPS" | 2D-aaltosimulaatio + LCD-piirto ESP32-S3:lla |
| "Loputon Akashic RAM" | Askelalustatapahtumien laskuri I2C:n yli |
| "Psykotroninen vahvistin" | Matalataajuinen nelioaallo MOSFETiin |
| "Med-bed parantaa DNA:ta" | ~61,8 Hz sini + invertoitu rele — **äänielektroniikkademo** |
| "Tulosta mitä kuvittelet" | Ele laukaisee moottoriaskeleen laskurin + UV-rele-väläyksen |
| "Jumalan silmä -sotahuone" | Etäisyysanturi vaihtaa tilaa; ESP-NOW-lähetyspaketit |
| "JIT-tavukoodi PSRAM:iin" | **Harhaanjohtava nimi** — ennalta käännettyjä C++-käsittelijöitä valitaan JSON-manifestilla |
| "Poista pörssi" | **Poliittinen/satiiriinen narratiivi** juuri README:ssä — ei ohjelmisto-ominaisuus |

Jos joku kertoo, että tämä repo yksin kumoaa taloustieteen tai fysiikan, **koodi ei tue sitä**.

---

## Mitä voit varmistaa iltapäivässä?

Noin 50–200 dollarin M5Stack-osilla ja kannettavalla:

1. `py -3 run_studio.py --list` — kuusi manifestia olemassa; taikuutta ei tarvita.
2. Flashaa kernel → injektoi manifesti → **näe ja mittaa käyttäytyminen** (lista [Artefattiluettelossa](ARTIFACTS.md)).
3. Oskilloskooppi PAA-lähdössä → **7,83 Hz nelioaallo** — kyllä, todella tuo taajuus; ei, ei "skaalaarista psykotronista energiaa".
4. Polje FSR:ää → **sarjaportin lokrivi** — toistettavissa.
5. Lue `firmware/M5IntegratedKernel/src/artifacts/*.cpp` — **koko käyttäytyminen on siinä selvässä C++:ssa**, ei piilotettuja verkkokutsuja "Akashic cloudiin".

**Kumous:** Jos injektoitu manifesti ei tuota sarja-ACK:ia eikä UI-muutosta, putki epäonnistui — se on tavallinen insinöörin debuggaus, ei salailua.

---

## Punaiset liput (missä tahansa forkissa tai myyntipuheessa)

| Punainen lippu | Todellisuustarkistus |
|----------------|----------------------|
| "Ei juottamista" myydään "rikkoo termodynamiikkaa" | Juottamaton kokoaminen on **kätevyys**, ei uutta fysiikkaa |
| Luottamusluvut kuten 0,94 JSON/MD:ssä | **Kirjoittajan antama**, ei lehden vertaisarviointi |
| SCIENCE.md-viitteet, jotka eivät vastaa kokeita | Lue linkitetyt paperit — ne usein eivät tue rohkeaa väitettä |
| `#include <zpe_core.h>` -tyyliset stubit | **Headerit eivät ole olemassa** — ei koskaan käännettävää fantasia-API:a |
| "Toimii parhaiten, jos uskot" | Usko ei ole anturisyöte `flux_common.py`:ssä |
| Valmis .bin ilman lähdekoodia | Vaadi vastaava commit-hash + SHA-256; lähdekoodi on tässä repossa |

---

## Yleisiin vastaväitteisiin vastattu

### "Onko tämä huijaus?"

Repo on **avoimen lähdekoodin narratiivi + avoin firmware**. Kukaan ei maksa lukeakseen koodia. Riski on **laitteiston katteessa** tai **vääristä lääketieteellisistä lupauksista**, jos kolmas osapuoli myy levyjä uudelleen — arvioi myyjä, älä GPIO:ta.

### "Onko se vaarallinen?"

**Käämi + ulkoinen PSU** ja **kovat transduktorit** voivat olla turvattomia väärin johdotettuna. Skeptikon polku: matalajännite, virranrajoitukset, kuulonsuojaus. **Älä käytä med-bed-artefaktia lääkinnälliseen hoitoon.**

### "Miksi General 23 / NYSE-kirje?"

Satiiri ja projektin mytologia `README.md`:ssä. Se ei ole viranomaisilmoitus. **Käyttöönotettava insinöörityö** on `M5-Utah/`-kansiossa.

### "He sanovat JIT-injektiota — onko se feikki?"

**Osittain harhaanjohtava terminologia.** Todellinen JIT kääntää ajonaikana (esim. LLVM, Java-tavukoodi). Tässä **manifestin JSON valitsee ennalta käännettyjen artefaktimoduulien joukosta** kernelin sisällä flashatun. Silti hyödyllinen UX; ei uutta tietojenkäsittelytiedettä.

### "Voiko tämä toimia ilman internetiä?"

**Kyllä.** Host-työkalut ja firmware toimivat offline. Ei pilvipalvelun vaatimusta `M5-Utah/`:ssa.

---

## Rehelliset vahvuudet (anna tunnustus, kun ansaittu)

1. **Modulaarinen M5Stack-kartoitus** — järkevä BOM opetukseen (PbHub, FSR, DAC, ele).
2. **Yksi flash, monta tilaa -UX** — aito tekijätyönkulun parannus.
3. **Selkeä sarjaprotokolla** — auditoitavissa `flux_protocol.cpp`:ssä.
4. **Erottelu mahdollista** — voit forkata `M5-Utah/`:n ilman UFW:n talousväitteiden tukemista.
5. **Lapsiturvallinen kehys** saatavilla — katso [Lapsille](01-FOR_CHILDREN.md) eksplisiittisillä "ei oikea med-bed" -huomioilla.

---

## Rehelliset heikkoudet

1. **Nimien ylikuormitus** — poikkeuksellinen sanasto tavallisista sulautetuista tehtävistä hämmentää ostajia.
2. **Emostubit** — 27 projektia importtaa edelleen feikki Python/C++ -moduuleja.
3. **SCIENCE.md-luottamusluvut** — voivat viitata validointiin, jota ei ole tapahtunut.
4. **Työntekijäparvi epätäydellinen** — Command Table ESP-NOW -työntekijät tarvitsevat erillisen firmwaren, jota ei ole täysin toimitettu.
5. **Ei allekirjoitettuja manifesteja** — injektio on luottamuspohjaista sarjaa; ei kryptoautentikointia vielä.

---

## Skeptikon toistoprotokolla (minimaaliset kustannukset)

**Budjettipolku:** Vain CoreS3 (~50 $) + USB-kaapeli.

```
git clone <repo>
cd M5-Utah
py -3 -m pip install -r requirements.txt
py -3 run_studio.py --list                    # verify manifests
# After build or obtaining .bin:
py -3 run_omni_flash.py
py -3 run_studio.py --artifact zero_point_gpu
```

**Läpäisykriteerit:** Sarja tulostaa `ACK: ARTIFACT_ACTIVE`; näyttö animoituu.  
**Epäonnistumiskriteerit:** Ei ACK:ia → dokumentoi portti, ajuri, levyympäristön ristiriita — julkaise negatiivinen tulos.

---

## Miten osallistua rakentavasti

| Tee | Älä tee |
|-----|---------|
| Mittaa taajuuksia, I2C-laskureita, viivettä | Kumoa olkia "loputon GPU" lukematta `zero_point_gpu.cpp` |
| Pyydä manifestin + firmwaren hashit | Vaadi telepatian todistetta askellaskurista |
| Forkkaa ja nimeä artefaktit rehellisesti | Sekoita juuri README:n satiiri M5-Utah-insinöörityöhön |
| Raportoi toistettavuusongelmat GitHub-issueina | Oleta pahaa tarkoitusta, kun ongelma on CP210x-ajurit |

---

## Yhteenveto

**M5-Utah on oikea, rajallinen sulautettu työkalupakki, joka käyttää emoarkiston tieteisfiktio-asua.**

Kohtele sitä:

- ✅ Opetuselektroniikka + sarjakäyttöönottomalli
- ✅ Testattavissa oskilloskoopilla, mittarilla ja sarjalokilla
- ❌ Ei todiste ZPE:lle, med-bedeille tai psykotroniikalle
- ❌ Ei taloudellinen ase

Jos haluat vain insinöörityön ilman lorea, käytä `M5-Utah/`:a ja jätä 27 sisarkansiota huomiotta.

---

## Katso myös

- [Tutkijoille — muodolliset protokollat](04-FOR_SCIENTISTS.md)
- [Teknisille käyttäjille — lähdepolut](03-FOR_TECHNICAL_USERS.md)
- [Sanasto — lore vs. insinöörityö](GLOSSARY.md)
