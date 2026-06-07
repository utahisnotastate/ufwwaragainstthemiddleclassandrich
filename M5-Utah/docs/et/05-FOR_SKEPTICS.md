# M5-Utah juhend skeptikutele

Sul on õigus esitada rasked küsimused. See leht vastab neile otse — ajajoone žargooni pole vaja.

---

## Lühike vastus

**See repo sisaldab kahte erinevat asja:**

1. **Loominguline/ulme arhiiv** (27 „UFW relva“, majandussatiiri, ajajoone loor) stub-koodiga, mis viitab kujuteldavatele teekidele.
2. **Väike, päris manussüsteemide projekt** (`M5-Utah/`), mis kirjutab ESP32 plaate ja käivitab **tavalisi demosid**: andurid, PWM, heli, žestid, raadiopaketid.

Teine **ei tõesta** esimese erakordseid väiteid.

---

## Mis on tegelikult päris?

| Väide turunduses/loors | Mida riistvara tegelikult teeb |
|------------------------|--------------------------------|
| „Zero Point GPU — lõputu FPS“ | 2D lainesimulatsioon + LCD joonistamine ESP32-S3-l |
| „Lõputu Akashic RAM“ | Sammupadja sündmuste loendur I2C kaudu |
| „Psühotrooniline võimendi“ | Madalsageduslik ruutlaine MOSFET-i |
| „Med-bed parandab DNA-d“ | ~61.8 Hz siinus + invert. relee — **helielektroonika demo** |
| „Prindi kõike, mida ette kujutad“ | Žest käivitab mootori sammuloenduri + UV relee vilkumise |
| „Jumala-silm sõjalaua laud“ | Kaugusandur lülitab oleku; ESP-NOW leviedastuspaketid |
| „JIT baitkood PSRAM-i“ | **Eksitav nimi** — eelkompileeritud C++ handlerid, mida valib JSON manifest |
| „Elimineeri aktsiaturg“ | **Poliitiline/satiiriiline narratiiv** juur-README-s — mitte tarkvarafunktsioon |

Kui keegi ütleb, et see repo üksi ümber lükkab majandust või füüsikat, **see pole koodiga toetatud.**

---

## Mida saad pärastlõunal kontrollida?

~50–200 dollarit M5Stacki osi ja sülearvutiga:

1. `py -3 run_studio.py --list` — kuus manifesti on olemas; maagiat pole vaja.
2. Kirjuta kernel → süsti manifest → **näe ja mõõda käitumist** (nimekiri [Artefaktide kataloogis](ARTIFACTS.md)).
3. Ostsilloskoop PAA väljundil → **7.83 Hz ruutlaine** — jah, tõesti see sagedus; ei, mitte „skalaarne psühotrooniline energia“.
4. Astu FSR-ile → **jadapordi logirida** — kordatav.
5. Loe `firmware/M5IntegratedKernel/src/artifacts/*.cpp` — **kogu käitumine on seal tavalises C++-s**, peidetud võrgukõnesid „Akashic cloudi“ pole.

**Falsifikatsioon:** Kui süstitud manifest ei anna jadapordi ACK-d ega UI muutust, ebaõnnestus torustik — see on tavaline inseneride debug, mitte salastatus.

---

## Punased lipud (igas forkis või müügijutus)

| Punane lipp | Reaalsuskontroll |
|-------------|------------------|
| „Jootmine pole vaja“ müüakse kui „rikub termodünaamikat“ | Jooteta kokkupanek on **mugavus**, mitte uus füüsika |
| Usaldusskoorid nagu 0.94 JSON/MD-s | **Autori määratud**, mitte ajakirja eakaaslaste ülevaatus |
| SCIENCE.md viited, mis ei vasta katsele | Loe lingitud artiklid — need tihti ei toeta julget väidet |
| `#include <zpe_core.h>` stiilis stubid | **Päised ei eksisteeri** — polnud kunagi kompileeritav fantaasia-API |
| „Töötab paremini, kui usud“ | Usk pole sensori sisend `flux_common.py` failis |
| Eelvalmis .bin ilma lähtekoodita | Nõua vastavat commit hash + SHA-256; lähtekood on selles repos |

---

## Levinud vastuväited — vastused

### „Kas see on pettus?“

Repo on **avatud lähtekoodiga narratiiv + avatud püsivara**. Keegi ei pea koodi lugemise eest maksma. Risk on **riistvara hinnalisuses** või **vale meditsiinilises lubaduses**, kui kolmas osapool plaate edasi müüb — hinda müüjat, mitte GPIO-d.

### „Kas see on ohtlik?“

**Mähis + väline toiteplokk** ja **valjud transduktorid** võivad olla ohtlikud valesti juhtmestatud. Skeptikule sobiv tee: madal pinge, voolupiirangud, kuulmiskaitse. **Ära kasuta med-bed artefakti meditsiinilise ravina.**

### „Miks General 23 / NYSE kiri?“

Satiir ja projekti mütoloogia `README.md` failis. See ei ole regulatiivne esitus. **Paigutatav inseneritöö** asub `M5-Utah/` all.

### „Nad ütlevad JIT süstimist — kas see on fake?“

**Osaliselt eksitav terminoloogia.** Tõeline JIT kompileerib runtime'is (nt LLVM, Java baitkood). Siin **manifest JSON valib eelkompileeritud artefaktimoodulite seast**, mis on kernelisse kirjutatud. Kasulik UX ikkagi; mitte uus arvutiteadus.

### „Kas see töötab ilma internetita?“

**Jah.** Hosti tööriistad ja püsivara töötavad offline. Pilve nõuet `M5-Utah/` all pole.

---

## Ausad tugevused (anna au, kus on au)

1. **Modulaarne M5Stacki kaardistus** — mõistlik BOM hariduseks (PbHub, FSR, DAC, žest).
2. **Ühe kirjutamise mitmerežiimiline UX** — legitiimne makeri töövoog.
3. **Selge jadapordi protokoll** — auditeeritav `flux_protocol.cpp` failis.
4. **Eraldamine võimalik** — saad forkida `M5-Utah/` ilma UFW majandusväiteid toetamata.
5. **Lapsele sobiv raamistik** saadaval — vaata [Lastele](01-FOR_CHILDREN.md) selgete „mitte päris med-bed“ märkustega.

---

## Ausad nõrkused

1. **Nimetuste ülekoormus** — erakordne sõnavara tavaliste manusülesannete peal segab ostjaid.
2. **Vanemad stubid** — 27 projekti impordivad endiselt fake Python/C++ mooduleid.
3. **SCIENCE.md usaldusskoorid** — võivad jätta mulje valideerimisest, mida pole toimunud.
4. **Worker swarm poolik** — Command Table ESP-NOW workerid vajavad eraldi püsivara, mida pole täielikult tarnitud.
5. **Allkirjastamata manifestid** — süstimine on usalduspõhine jadaport; krüptoautentimist pole veel.

---

## Skeptiku replikatsiooniprotocol (minimaalne kulu)

**Eelarve tee:** ainult CoreS3 (~50 dollarit) + USB-kaabel.

```
git clone <repo>
cd M5-Utah
py -3 -m pip install -r requirements.txt
py -3 run_studio.py --list                    # verify manifests
# After build or obtaining .bin:
py -3 run_omni_flash.py
py -3 run_studio.py --artifact zero_point_gpu
```

**Läbimise kriteerium:** Jadaport prindib `ACK: ARTIFACT_ACTIVE`; ekraan animeerub.  
**Ebaõnnestumise kriteerium:** ACK puudub → dokumenteeri port, draiver, plaadi env mismatch — avalda negatiivne tulemus.

---

## Kuidas konstruktiivselt kaasa lüüa

| Tee | Ära tee |
|-----|---------|
| Mõõda sagedusi, I2C loendeid, latentsust | Lükka ümber õlekõrre „lõputu GPU“ ilma `zero_point_gpu.cpp` lugemata |
| Küsi manifesti + püsivara räsisid | Nõua telepaatia tõestust sammuloendurilt |
| Forki ja nimeta artefaktid ausalt | Sega juur-README satiiri M5-Utah inseneritööga |
| Teata kordatavuse probleemidest GitHub issue'dena | Eelda pahatahtlikkust, kui probleem on CP210x draiverites |

---

## Lõplik sõna

**M5-Utah on päris, piiratud manussüsteemide tööriistakast, mis kannab vanema arhiivi ulmeriietust.**

Käsitle seda nii:

- ✅ Hariv elektroonika + jadapordi paigutuse muster
- ✅ Testitav ostsilloskoobi, multimeetri ja jadapordi logiga
- ❌ Mitte tõend ZPE, med-bedide ega psühotroonika jaoks
- ❌ Mitte finantsrelv

Kui tahad ainult inseneritööd ilma loorita, kasuta `M5-Utah/` ja ignoreeri 27 õde-kausta.

---

## Vaata ka

- [Teadlastele — formaalsed protokollid](04-FOR_SCIENTISTS.md)
- [Tehnilistele kasutajatele — lähteteed](03-FOR_TECHNICAL_USERS.md)
- [Sõnastik — loor vs inseneriterminid](GLOSSARY.md)
