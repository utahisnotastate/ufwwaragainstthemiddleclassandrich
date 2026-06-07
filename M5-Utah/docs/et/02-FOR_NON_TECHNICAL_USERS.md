# M5-Utah juhend mittetehnilistele kasutajatele

Sa **ei pea** koodi kirjutama, jootma ega avama Arduino IDE-d. Kui oskad ühendada USB-kaabli ja topeltklõpsata programmil (või käivitada ühe käsu, mille sõber sulle annab), saad seda süsteemi kasutada.

---

## Mida sa saad

**M5-Utah** muudab väikese M5Stacki vidina erinevateks kasulikeks seadmeteks:

- **Sammupadja juhtimine** tantsu- või treeningmängude jaoks
- **Värviline ekraanidemo** (lainesimulaator)
- **Madalsageduslik oscillator** mähise katsete jaoks
- **Helilainete demo** kahe väljundiga
- **Žestidega juhitav mootoridemo**
- **Laua armatuurlaud**, mis reageerib käeliigutustele

Ostad riistvara üks kord, kirjutad püsivara üks kord, seejärel **vahetad režiime** igal ajal, valides nime nimekirjast.

---

## Mida osta (stardikomplektid)

Vali **üks** projekt alustamiseks. Kõik kasutavad sama baastarkvara.

### Kõige lihtsam stardikomplekt: Lainemaalija (ainult CoreS3)

| Osa | Ligikaudne roll |
|-----|-----------------|
| M5Stack CoreS3 | Põhiseade ekraaniga |
| USB-C kaabel | Tavaliselt seadmega kaasas |

### Sammupadjad: Mnemonic DDR

| Osa | Kogus |
|-----|-------|
| M5Stack Core2 | 1 |
| M5Stack PbHub Unit | 1 |
| M5Stack FSR Unit | 4 |
| Grove kaablid (HY2.0-4P) | 5 |

### Täielik nimekiri

Vaata [Artefaktide kataloogi](ARTIFACTS.md) iga BOM-i jaoks.

---

## Ühekordne seadistus (küsi tehnilist sõpra VÕI järgi täpselt)

### Arvutis

1. Paigalda **Python 3** aadressilt [python.org](https://www.python.org/downloads/) (Windowsis märgi „Add to PATH“).
2. Ava terminal kaustas `M5-Utah`.
3. Käivita:
   ```
   py -3 -m pip install -r requirements.txt
   ```
4. Kui said eelvalmis `m5_integrated_kernel.bin`, peaks see juba olema kaustas `M5-Utah/payloads/`. Kui mitte, peab tehniline sõber selle ehitama (vaata [Tehnilist juhendit](03-FOR_TECHNICAL_USERS.md)).

### M5Stackil (ainult esimest korda)

1. Ühenda M5Stack arvutiga USB-C kaabli abil.
2. Käivita:
   ```
   py -3 run_omni_flash.py
   ```
3. Oota **SUCCESS**. Seade on nüüd tühi „vastuvõtja“.

**Kirjutad püsivara ainult üks kord**, välja arvatud uue plaadi või suure püsivara uuenduse korral.

---

## Igapäevane kasutamine (iga kord, kui tahad uut seadme režiimi)

1. Ühenda USB-C.
2. Käivita:
   ```
   py -3 run_studio.py
   ```
3. Näed nummerdatud nimekirja, näiteks:
   ```
   [0] Cellular_Regenesis_Chamber.flux.json  (Med-Bed / cores3)
   [1] Holographic_Printing_Press_V5.flux.json  ...
   ...
   ```
4. Sisesta number ja vajuta Enter.
5. M5Stack taaskäivitub selles režiimis. Valmis.

### Otsetee (kui keegi andis sulle nime)

```
py -3 run_studio.py --artifact mnemonic_ddr_infinity
```

### Loetle režiime ilma ühendamiseta

```
py -3 run_studio.py --list
```

---

## Füüsiline kokkupanek (jootmine pole vaja)

Kõik M5Stacki üksused kasutavad **Grove kaableid** — värvilised pistikud, mis klõpsavad sisse.

**Näide — sammupadjad:**

1. Ühenda **PbHub** Core2 **Port A** (punane).
2. Ühenda iga **FSR** PbHubi kanalitesse **CH0, CH1, CH2, CH3**.
3. Aseta iga FSR põrandplaadi või pappkastist „sammutsooni“ alla.

**Näide — Med-Bed helidemo:**

1. Ühenda **Unit-DAC** CoreS3 Port A-sse.
2. Ühenda **Unit-Relay** Port B-sse.
3. Ühenda väikesed kõlarid või eksiteerid kruvi klemmidele (täiskasvanu abi).

Skeemid ja pordi nimed: [Artefaktide kataloog](ARTIFACTS.md).

---

## Kuidas tead, et see töötab

| Seadme režiim | Peaksid nägema… |
|---------------|-----------------|
| Lainemaalija | Värvid liiguvad ekraanil |
| Sammumälu | Number suureneb, kui astud padjadele |
| Sumisev kast | Olek AtomS3 ekraanil; mähis juhitakse MOSFETi kaudu (kasuta ostsilloskoopi või LEDi mähisel, kui pole kindel) |
| Med-Bed demo | Jadapordi sõnumid; heli transduktoritest, kui juhtmestik on tehtud |
| Käeprinter | Z-kõrguse number suureneb, kui liigutad kätt allapoole žestianduri ees |
| Sõjalaua laud | Ekraan ütleb ACTIVE või HALT, kui liigutad kätt ToF-anduri kohal |

Kui midagi ei juhtu: vaata allpool **Veaotsing**.

---

## Veaotsing

| Probleem | Proovi seda |
|----------|-------------|
| „No M5Stack detected“ | Teine USB-kaabel; proovi teist USB-porti; paigalda CP210x või CH340 draiver (otsi Google'ist oma plaadi nimi + „USB driver“) |
| Kirjutamine ebaõnnestub | Hoia **BOOT** nuppu all USB ühendamise ajal, seejärel proovi uuesti `run_omni_flash.py` |
| Vale režiim pärast süstimist | Eemalda vool, ühenda uuesti, käivita `run_studio.py` uuesti õige numbriga |
| Sammupadjad ei reageeri | Kontrolli, et Grove kaabel on täielikult kinni; PbHub Port A-s |
| Ekraan tühi | Kirjuta kernel uuesti; veendu, et ehitasid/kirjutasid õige plaadi jaoks (Core2 vs CoreS3 vs AtomS3) |

---

## Mida see EI OLE

Selgus aitab kõiki:

- **Ei ole** meditsiiniseade. „Med-Bed“ on **helisageduse demo**.
- **Ei ole** päris holograafiline printer. See on **žest + mootor + relee demo**.
- **Ei ole** lõputu arvutimälu. Sammurežiim **logib tammumissündmusi**.
- **Ei ole** tõestatud „psühotrooniline“ tehnoloogia. See väljastab **teadaolevaid sagedusi** (7.83 Hz, 40 Hz) GPIO-pinnil.

**Lugu ja nimed** pärinevad UFW loomingulise arhiivi. **Riistvara käitumine** on tavaline elektroonika, mida saad silmade ja kõrvadega testida.

Rohkem detaili: [Skeptikutele](05-FOR_SKEPTICS.md)

---

## Algne UFW vs M5 (milliseid dokumente lugeda?)

| Olukord | Loe |
|---------|-----|
| Sul on **vana 27-kaustaline** repo paigutus | [Algne World-A lähenemine](07-ORIGINAL_WORLDA_APPROACH.md) |
| **Üleminek** prototüüpplaadilt/Arduinost M5-le | [Migratsioonijuhend](06-MIGRATION_FROM_ORIGINAL.md) |

## Abi saamine

| Vajad | Loe |
|-------|-----|
| Lapsele sobiv selgitus | [Lastele](01-FOR_CHILDREN.md) |
| Ehita püsivara ise | [Tehnilistele kasutajatele](03-FOR_TECHNICAL_USERS.md) |
| Mõõda ja tsiteeri katseid | [Teadlastele](04-FOR_SCIENTISTS.md) |
| Kõik osade nimed | [Sõnastik](GLOSSARY.md) |
