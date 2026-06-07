# M5-Utah-opas tutkijoille ja tutkimustyöntekijöille

Tämä asiakirja erottaa **testattavan laitteiston käyttäytymisen** **tarinallisista fysiikkaväitteistä** UFW-arkistossa ja tarjoaa toistettavat mittausprotokollat kuudelle käyttöönotettavalle artefaktille.

---

## Yhteenveto

| Taso | Luonne | Vertaisarvioinnin tila |
|------|--------|------------------------|
| M5-Utah-firmware ja host-työkalut | Sulautetut järjestelmät + Python-sarjatyökalut | Tavallista insinöörityötä; toistettavissa annetulla laitteistolla |
| Emorepon `*_SCIENCE.md` -tiedostot | Sekoitettu esitys luottamusluvuilla | Ei riippumatonta validointia; käsittele kirjoittajan narratiivina |
| Lore-termiä (ZPE, Akashic-muisti, med-bed-parantaminen) | Spekulatiivinen / fiktiivinen kehys | **Ei todisteaineistoa** tässä repossa |

**Mitä voit julkaista:** instrumentoitu kuvaus GPIO:sta, I2C:stä, PWM:stä, akustiikasta ja ESP-NOW-käyttäytymisestä.  
**Mitä et voi väittää pelkästään tästä reposta:** biologinen regeneraatio, tyhjiöenergian talteenotto, ajatuksesta aineeseen -tulostus tai psykotroninen kausaalisuus.

---

## Väitteiden taksonomia

### Taso A — Suoraan mitattavissa (World-A)

- UART-manifestin injektio 115200 baudilla määritellyllä kehystyksellä
- FreeRTOS-kahden tehtävän suoritus ESP32-S3:lla
- I2C-analogialukemat PbHubista + FSR-jännitejakajista
- PWM-nelioaallot 7,83 Hz:llä ja 40,0 Hz:llä
- I2C-DAC-sini ~61,8 Hz releen vaiheinversiolla
- Elekeskeytys PAJ7620U2 I2C-rekisterilukujen kautta
- VL53L0X-etäisyysmittauksen kynnysarvot
- ESP-NOW-lähetyskehykset 2,4 GHz Wi-Fi-radiolla

### Taso B — Analogiat julkaistuun fysiikkaan (vaativat oman viiteketjusi)

- **Schumann-resonanssi (~7,83 Hz):** Maan–ionosfäärijärjestelmän erittäin matalataajuinen sähkömagneettinen ontelotila. 7,83 Hz:n **sähköoskillaattori** työpöydällä ei vastaa kytkentää tuohon geofysikaaliseen tilaan ilman antennia, kenttävoimakkuutta ja SNR-analyysiä.
- **40 Hz gamma-entrainment:** Julkaistu neurotieteellinen kirjallisuus tutkii 40 Hz:n aististimulaatioparadigmoja; **tämä laite ei osoita kliinisiä tuloksia**.
- **61,8 Hz akustinen interferenssi:** Pulsan poistuminen ja vaiheinversio ovat klassista akustiikkaa; yhdistäminen "Priore-ilmiöön" tai "vaihekonjugaattiseen biologiaan" on **hypoteesi**, ei tässä osoitettu.
- **Aaltoyhtälö 2D-verkossa:** Numeerinen Laplacen malli `zero_point_gpu.cpp`:ssä — tavallinen äärellisten erotusten demo, ei tyhjiölaskentaa.

### Taso C — Ei empiirisesti perusteltu koodipohjassa

- Zero-point energy GPU / Casimir-laskenta
- Akashic / tyhjiömuistin varaus
- Solujen ikäpalautus
- Holografinen aineen kääntäminen aikomuksesta
- Psykotroninen skalaarilähetys
- Aikajana-analytiikka / uhkien tunnistus

---

## Toistettavuuden tarkistuslista

### Kirjattavat ohjelmistoversiot

```
Python: py --version
esptool: esptool version
PlatformIO: pio --version
Board env: cores3 | core2 | atoms3
Git commit hash of ufwwaragainstthemiddleclassandrich
m5_integrated_kernel.bin SHA-256
Manifest manifest_version + artifact_id
```

### Laitteiston manifesti

Kirjaa M5Stack-SKU, firmware-siru (ESP32 vs. ESP32-S3), PSRAM:n läsnäolo ja ulkoisten moduulien revisionumerot.

---

## Artefaktikohtaiset protokollat

### 1. Zero Point GPU Emulator

**Hypoteesi (testattavissa):** Ydin 0 laskee 2D-skaalarikentän päivityksen, kun ydin 1 renderöi ilman UI-silmukan nälkää.

**Laitteisto:** CoreS3, USB-sarja, valinnainen logiikka-analysaattori UART TX:ään.

**Menetelmä:**

1. Injektoi `Zero_Point_GPU.flux.json`.
2. Lokita sarjaportti 115200 baudilla 60 s.
3. Tallenna näytön päivitys visuaalisesti tai kameralla tunnetulla FPS:llä.
4. Valinnainen: lue `parameters.grid_size`, `wave_speed`, `zpe_gain` manifestista ja korreloi visuaalisen etenemisnopeuden kanssa.

**Havainnot:** Kehyslaskuri sarjassa (`ZPE GPU f=N`); vakaa näytön päivitys; ei watchdog-resetiä.

**Ei osoitettu:** Tyhjiöenergian talteenotto, fotonien kovavaloprojektio.

---

### 2. Mnemonic DDR Infinity

**Hypoteesi (testattavissa):** FSR-paine vähentää analogialukemaa alle `strike_threshold`:n ja laukaisee debouncetut tapahtumat.

**Laitteisto:** Core2, PbHub, 4× FSR, monimetri valinnainen hubin kanavilla.

**Menetelmä:**

1. Injektoi manifesti; huomioi `strike_threshold` (oletus 1800).
2. Aseta tunnettuja massoja FSR-alustoille; lokita sarja `[DDR] Memory write` -tapahtumat.
3. Piirrä laukaisumäärä vs. sovellettu voima.

**Havainnot:** Monotoninen `write_count`:n kasvu; kanava-ID lokissa.

**Ei osoitettu:** Ei-lokaalinen muisti, petatavaravaraus, avaruusaika-lukitus.

---

### 3. Psychotronic Amplifier Array

**Hypoteesi (testattavissa):** AtomS3 tuottaa vakaan matalataajuisen nelioaallon MOSFET-portin GPIO:lla.

**Laitteisto:** AtomS3, MOSFET Unit, oskilloskooppi portissa ja käämin liittimissä, **virranrajoitettu ulkoinen PSU**.

**Menetelmä:**

1. Injektoi manifesti; oletus `schumann` → 7,83 Hz.
2. Mittaa jakso T ≈ 127,7 ms ± toleranssibudjetti (kide, `delayMicroseconds`-vaihtelu).
3. Paina BtnA; varmista siirtyminen ~40 Hz:ään (T ≈ 25 ms).
4. Dokumentoi työsykli vs. `duty_percent`-parametri.

**Turvallisuus:** Älä aja suurta käämivirtaa GPIO:n kautta; MOSFET eristää MCU:n.

**Ei osoitettu:** Psykotronisen signaalin tunnistus, mielen–aineen kytkentä; emon SCIENCE.md:n arXiv/MDPI-viitteitä **ei toisteta** tämän firmwaren toimesta.

---

### 4. Cellular Regenesis Chamber

**Hypoteesi (testattavissa):** DAC tuottaa siniaallon `carrier_hz`:llä; releen lähtö on loogisesti invertoitu puolijakson.

**Laitteisto:** CoreS3, Unit-DAC, Unit-Relay, kaksi transduktoria tai korkean Z:n oskilloskooppikoetta, SPL-mittari valinnainen.

**Menetelmä:**

1. Injektoi manifesti (`carrier_hz`: 61,8).
2. Tallenna DAC-analogilähtö — odota siniä f ≈ 61,8 Hz.
3. Tallenna releen digitaalilähtö — odota 180° vaihesuhdetta sinin nollanylityksiin (releen viiveen sisällä).
4. Jos akustinen polku asennettu, mittaa SPL; **käytä kuulon turvallisia tasoja**.

**Ei osoitettu:** DNA:n uudelleenjärjestely, telomeerien palautus, entropian väheneminen biologisessa kudoksessa.

---

### 5. Holographic Printing Press V5

**Hypoteesi (testattavissa):** PAJ7620-elekoodi `0x04` laukaisee Z-incrementin ja relepulssin `uv_pulse_ms`:n ajaksi.

**Laitteisto:** Core2, Unit-Gesture, Unit-Relay, oskilloskooppi releen kontakteissa.

**Menetelmä:**

1. Injektoi manifesti.
2. Tee kontrolloitu alaspyyhkäisy kiinteällä etäisyydellä; laske relepulssit.
3. Varmista, että `z_position_steps` kasvaa 800:lla per laukaisu (firmware-vakio).

**Ei osoitettu:** SLA-hartsin kovettumisputki, tyhjiöstressin materialisointi, aikomuksen selkeyden mittarit.

---

### 6. UFW Tactical Command Table

**Hypoteesi (testattavissa):** VL53L0X-etäisyys alle `wave_threshold_mm`:n vaihtaa järjestelmän tilaa ja lähettää ESP-NOW-paketteja.

**Laitteisto:** CoreS3, Unit-ToF, toinen ESP32 ESP-NOW-snifferinä (valinnainen), Wi-Fi-spektrianalysaattori valinnainen.

**Menetelmä:**

1. Injektoi manifesti.
2. Lähesty kättä mitatuilla etäisyyksillä; lokita HALT/ACTIVE-siirtymät.
3. Tallenna ESP-NOW-kehykset snifferillä; dokumentoi MAC-lähetys `FF:FF:FF:FF:FF:FF` ja payload-rakenne `WorkerPacket` (katso `war_room.cpp`).

**Ei osoitettu:** Uhkien aikomuksen luokittelu, aikajanasimulaatio, FinOps-kannattavuuden tunnistus.

---

## Julkaisun datan skeema

Ehdotetut avoimen aineiston kentät per ajo:

```yaml
run_id: UUID
artifact_id: string
board: string
manifest_sha256: string
firmware_sha256: string
environment:
  temperature_c: float
  humidity_pct: float
instruments:
  - model: string
    calibration_date: date
results:
  - observable: string
    value: float
    unit: string
    uncertainty: float
```

---

## Suhde emon `*_SCIENCE.md` -tiedostoihin

Esimerkki: `Psychotronic_Amplifier_Array_SCIENCE.md` raportoi luottamusluvun 0,94 Schrödinger-muotoisilla yhtälöillä ja ulkoisilla viitteillä. **Tuo luku on arkiston skeeman sisäinen**, ei sokko-toiston tulos.

Suositeltu tulkinta:

1. Käytä SCIENCE.md:ää **käsitteellisenä bibliografiana ja hypoteesimuistiinpanoina**.
2. Käytä M5-Utah-firmwarea **laitteiston määrittelynä** vain tason A mittauksille.
3. Älä yhdistä tason C väitteitä tason A tuloksiin ilman erillisiä ennalta rekisteröityjä tutkimuksia.

---

## Eettiset ja turvallisuushuomiot ihmiskoehenkilöille

- **Ei lääketieteellisiä väitteitä** — med-bed-artefakti on ääni-/elektroniikkatestialusta.
- **Kuulonsuojaus** jatkuvalle 61,8 Hz:n tai 40 Hz:n altistukselle korkealla SPL:llä.
- **Käämikokeet** — rajoita virtaa; palovaara jatkuvalla MOSFET-kytkennällä induktiiviseen kuormaan.
- **ESP-NOW / Wi-Fi** — RF-altistus kuluttajalaitteen rajoissa; dokumentoi paikalliset säännökset.

---

## Ehdotetut viitteet (menetelmät, ei UFW-väitteitä)

Kuvaessasi laitteistoa viittaa komponenttien ensisijaisiin lähteisiin:

- Espressif ESP32-S3 Technical Reference Manual
- M5Stack-tuotewiki I2C-osoitteille ja Grove-pinoutille
- Espressif ESP-NOW API -dokumentaatio
- PAJ7620U2-eleanturin datasheet
- VL53L0X-etäisyysanturin datasheet

Biologisiin tai ZPE-väitteisiin **älä viittaa tähän GitHub-repoon todisteena** — viittaa vertaisarvioituun kirjallisuuteen itsenäisesti.

---

## Yhteystiedot ja yhteistyö

Repon kirjoittajakonteksti: Utah-1 / General 23 -tarinakehys. Instrumentoiduissa toistotutkimuksissa dokumentoi forkisi, manifestien hashit ja raakatallenteet; julkaise toistettavuusraportteja tiettyjä git-commiteja vasten.

Lisälukemaa: [Skeptikoille](05-FOR_SKEPTICS.md) | [Tekninen viite](03-FOR_TECHNICAL_USERS.md)
