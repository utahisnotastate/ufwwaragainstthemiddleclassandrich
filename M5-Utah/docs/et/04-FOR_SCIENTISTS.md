# M5-Utah juhend teadlastele ja teaduritele

See dokument eraldab **testitava riistvara käitumise** **narratiivsetest füüsikaväidetest** UFW arhiivis ja annab kuue paigutatava artefakti jaoks kordatavad mõõtmisprotokollid.

---

## Kokkuvõte

| Kiht | Olemus | Eakaaslaste ülevaatus |
|------|--------|----------------------|
| M5-Utah püsivara ja hosti tööriistad | Manussüsteemid + Python jadapordi tööriistad | Standardne inseneritöö; kordatav antud riistvaraga |
| Vanemrepo `*_SCIENCE.md` failid | Segatud esitus koos usaldusskooridega | Sõltumatu valideerimine puudub; käsitle autorinarratiivina |
| Loori terminid (ZPE, Akashic memory, med-bed healing) | Spekulatiivne / fiktiivne raamistik | **Tõendusmaterjali pole** selles repos |

**Mida saad avaldada:** instrumenteeritud karakteriseerimine GPIO, I2C, PWM, akustika ja ESP-NOW käitumise kohta.  
**Mida sa ei saa väita ainult selle repo põhjal:** bioloogiline regeneratsioon, vaakumenergia eraldamine, mõttest ainesse printimine või psühotrooniline põhjuslikkus.

---

## Väidete taksonoomia

### Kiht A — Otseselt mõõdetav (World-A)

- UART manifesti süstimine 115200 baudil määratletud raamistikuga
- FreeRTOS kahe ülesande täitmine ESP32-S3-l
- I2C analooglugemised PbHubist + FSR pingejaguritest
- PWM ruutlained 7.83 Hz ja 40.0 Hz
- I2C DAC siinusgenereerimine ~61.8 Hz relee faasiinversiooniga
- Žesti katkestus PAJ7620U2 I2C registrilugemiste kaudu
- VL53L0X time-of-flight kauguse läved
- ESP-NOW leviedastusraamid 2.4 GHz Wi-Fi raadios

### Kiht B — Analoogiad avaldatud füüsikaga (vajavad oma tsiteerimisahelat)

- **Schumanni resonants (~7.83 Hz):** Maa–ioonosfääri süsteemi väga madala sagedusega elektromagnetiline resonaatorirežiim. 7.83 Hz **elektriline oscillator** töölaual ei ole ekvivalentne geofüüsikalise režiimiga sidumisega ilma antenni, väljatugevuse ja SNR analüüsita.
- **40 Hz gamma entrainment:** Avaldatud neuroteaduse kirjandus uurib 40 Hz sensoorse stimulatsiooni paradigmasid; **see seade ei demonstreeri kliinilisi tulemusi**.
- **61.8 Hz akustiline interferents:** Põrke tühistamine ja faasiinversioon on klassikaline akustika; seostamine „Priore efektiga“ või „faasikonjugaate bioloogiaga“ on **hüpotees**, mitte siin demonstreeritud.
- **Lainevõrrand 2D ruudul:** Numbriline Laplace'i šabloon `zero_point_gpu.cpp` failis — standardne lõplike erinevuste demo, mitte vaakumarvutus.

### Kiht C — Koodibaasis empiiriliselt põhjendamata

- Zero-point energy GPU / Casimir compute
- Akashic / vaakummälu eraldamine
- Raku vanuse regressioon
- Holograafiline aine kompileerimine kavatsusest
- Psühotrooniline skalaarne levitamine
- Ajajoone analüütika / vaenulikkuse tuvastamine

---

## Kordatavuse kontrollnimekiri

### Tarkvaraversioonid, mida salvestada

```
Python: py --version
esptool: esptool version
PlatformIO: pio --version
Board env: cores3 | core2 | atoms3
Git commit hash of ufwwaragainstthemiddleclassandrich
m5_integrated_kernel.bin SHA-256
Manifest manifest_version + artifact_id
```

### Riistvara manifest

Salvesta M5Stack SKU, püsivara kiip (ESP32 vs ESP32-S3), PSRAM olemasolu ja väliste moodulite revisjoninumbrid.

---

## Artefaktipõhised protokollid

### 1. Zero Point GPU Emulator

**Hüpotees (testitav):** Tuum 0 arvutab 2D skalaarvälja uuendust, samal ajal kui tuum 1 renderdab ilma UI tsüklit näljutamata.

**Apaaraat:** CoreS3, USB jadaport, valikuline loogikaanalüsaator UART TX-l.

**Protseduur:**

1. Süsti `Zero_Point_GPU.flux.json`.
2. Logi jadaporti 115200 60 s.
3. Jäädvusta ekraani värskendus visuaalselt või kaameraga teadaoleva FPS-iga.
4. Valikuliselt loe manifestist `parameters.grid_size`, `wave_speed`, `zpe_gain` ja korreleeri visuaalse levikiirusega.

**Observables:** Kaadrite loendur jadapordis (`ZPE GPU f=N`); stabiilne ekraani uuendus; watchdog reset puudub.

**Ei demonstreeritud:** Vaakumenergia eraldamine, fotonite kõval-valguse projektsioon.

---

### 2. Mnemonic DDR Infinity

**Hüpotees (testitav):** FSR surve vähendab analoogloendit alla `strike_threshold` ja käivitab debounced sündmused.

**Apaaraat:** Core2, PbHub, 4× FSR, multimeeter valikuliselt hubi kanalitel.

**Protseduur:**

1. Süsti manifest; märgi `strike_threshold` (vaikimisi 1800).
2. Rakenda teadaolevaid masse FSR padjadele; logi jadapordi `[DDR] Memory write` sündmused.
3. Joonista käivituste arv vs rakendatud jõu kõver.

**Observables:** Monotoonne `write_count` kasv; kanali ID logis.

**Ei demonstreeritud:** Mittelokaalne mälu, petabaitide eraldamine, ajaruumi lukustamine.

---

### 3. Psychotronic Amplifier Array

**Hüpotees (testitav):** AtomS3 väljastab stabiilse madalsagedusliku ruutlaine MOSFETi värava GPIO-l.

**Apaaraat:** AtomS3, MOSFET Unit, ostsilloskoop väraval ja mähise klemmidel, **voolupiiranguga väline toiteplokk**.

**Protseduur:**

1. Süsti manifest; vaikimisi `schumann` → 7.83 Hz.
2. Mõõda periood T ≈ 127.7 ms ± tolerants (kristall, `delayMicroseconds` jitter).
3. Vajuta BtnA; kontrolli üleminekut ~40 Hz-le (T ≈ 25 ms).
4. Dokumenteeri töötsükkel vs `duty_percent` parameeter.

**Turvalisus:** Ära lase suurt mähisevoolu GPIO kaudu; MOSFET isoleerib MCU.

**Ei demonstreeritud:** Psühotrooniline signaalide tuvastamine, meele–aine sidumine; vanemas SCIENCE.md viidatud arXiv/MDPI lingid **ei ole selle püsivaraga reprodutseeritud**.

---

### 4. Cellular Regenesis Chamber

**Hüpotees (testitav):** DAC väljastab siinuse `carrier_hz` juures; relee väljund on loogiliselt inverteeritud poole tsükli.

**Apaaraat:** CoreS3, Unit-DAC, Unit-Relay, kaks transduktorit või kõrge-Z ostsilloskoobi sondid, SPL-mõõtur valikuliselt.

**Protseduur:**

1. Süsti manifest (`carrier_hz`: 61.8).
2. Jäädvusta DAC analoogväljund — oodata siinus f ≈ 61.8 Hz.
3. Jäädvusta relee digitaalväljund — oodata 180° faasiseos siinuse nullületustega (relee latentsuse piires).
4. Kui akustiline tee on paigaldatud, mõõda SPL; **kasuta kuulmiskaitse tasemeid**.

**Ei demonstreeritud:** DNA resekventseerimine, telomeeride taastamine, entropia vähenemine bioloogilises koekes.

---

### 5. Holographic Printing Press V5

**Hüpotees (testitav):** PAJ7620 žestikood `0x04` käivitab Z suurenemise ja relee impulsi `uv_pulse_ms`.

**Apaaraat:** Core2, Unit-Gesture, Unit-Relay, ostsilloskoop relee kontaktidel.

**Protseduur:**

1. Süsti manifest.
2. Tee kontrollitud allapoole liigutus fikseeritud kaugusel; loe relee impulsse.
3. Kontrolli, et `z_position_steps` suureneb 800 võrra käivituse kohta (püsivara konstant).

**Ei demonstreeritud:** SLA vaigu kõvastumise torustik, vaakumistressi materialiseerimine, kavatsuse selguse mõõdikud.

---

### 6. UFW Tactical Command Table

**Hüpotees (testitav):** VL53L0X kaugusmõõtmine alla `wave_threshold_mm` lülitab süsteemi oleku ja saadab ESP-NOW pakette.

**Apaaraat:** CoreS3, Unit-ToF, teine ESP32 ESP-NOW nuuskurina (valikuline), Wi-Fi spektraalanalüsaator valikuline.

**Protseduur:**

1. Süsti manifest.
2. Liiguta kätt mõõdetud kaugustel; logi HALT/ACTIVE üleminekuid.
3. Jäädvusta ESP-NOW raamid nuuskuriga; dokumenteeri MAC leviedastus `FF:FF:FF:FF:FF:FF` ja payload struct `WorkerPacket` (vaata `war_room.cpp`).

**Ei demonstreeritud:** Ohu kavatsuse klassifikatsioon, ajajoone simulatsioon, FinOps kasumlikkuse tajumine.

---

## Andmeskeem avaldamiseks

Soovitatud avatud andmestiku väljad käigu kohta:

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

## Seos vanema `*_SCIENCE.md` failidega

Näide: `Psychotronic_Amplifier_Array_SCIENCE.md` teatab usaldusskoori 0.94 koos Schrödingeri-vormi võrrandite ja väliste viidetega. **See skoor on arhiivi skeemi sisemine**, mitte pimestatud replikatsiooni tulemus.

Soovitatud tõlgendus:

1. Kasuta SCIENCE.md **kontseptuaalse bibliograafia ja hüpoteesimärkmetena**.
2. Kasuta M5-Utah püsivara **apaaraadi definitsioonina** ainult kihi A mõõtmiste jaoks.
3. Ära liida kihi C väiteid kihi A tulemustesse ilma eraldi eelregistreeritud uuringuteta.

---

## Eetilised ja turvalisuse märkused inimsubjektide jaoks

- **Meditsiinilisi väiteid pole** — med-bed artefakt on audio/elektroonika testplatvorm.
- **Kuulmiskaitse** püsiva 61.8 Hz või 40 Hz kokkupuute korral kõrge SPL-i juures.
- **Mähise katsed** — piira voolu; tuleoht pideva MOSFETi lülitamisega induktiivkoormusse.
- **ESP-NOW / Wi-Fi** — RF-kokkupuude tarbijaseadme piirides; dokumenteeri kohalikud regulatsioonid.

---

## Soovitatud tsitaadid (meetodid, mitte UFW väited)

Apaaraati kirjeldades tsiteeri komponentide esmaste allikate kaudu:

- Espressif ESP32-S3 Technical Reference Manual
- M5Stack toote wiki I2C aadresside ja Grove pinouti jaoks
- Espressif ESP-NOW API dokumentatsioon
- PAJ7620U2 žestianduri andmeleht
- VL53L0X kaugusanduri andmeleht

Bioloogiliste või ZPE väidete puhul **ära tsiteeri seda GitHub repot tõendina** — tsiteeri iseseisvalt eakaaslaste ülevaatuses olevat kirjandust.

---

## Kontakt ja koostöö

Repo autori kontekst: Utah-1 / General 23 narratiivne raamistik. Instrumenteeritud replikatsiooniuuringute jaoks dokumenteeri oma fork, manifesti räsid ja toorandmed; esita kordatavuse aruanded konkreetsete git commitide vastu.

Edasine lugemine: [Skeptikutele](05-FOR_SKEPTICS.md) | [Tehniline viide](03-FOR_TECHNICAL_USERS.md)
