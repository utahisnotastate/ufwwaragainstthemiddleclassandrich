# M5-Utah-opas ei-teknisille käyttäjille

Sinun **ei tarvitse** koodata, juottaa tai avata Arduino IDE:tä. Jos osaat kytkeä USB-kaapelin ja kaksoisnapsauttaa ohjelmaa (tai ajaa yhden komennon, jonka ystävä antaa sinulle), voit käyttää tätä järjestelmää.

---

## Mitä saat

**M5-Utah** muuttaa pienen M5Stack-laitteen erilaisiksi hyödyllisiksi laitteiksi:

- **Askelalustaohjain** tanssi- tai liikuntapeleihin
- **Värikäs näyttödemo** (aaltojen simulaattori)
- **Matalataajuusoskillaattori** käämikokeiluihin
- **Ääniaaltodemo** kahdella lähdöllä
- **Eleillä ohjattu moottoridemo**
- **Työpöytäkojelauta**, joka reagoi kädenheilutuksiin

Ostat laitteiston kerran, flashaat sen kerran ja **vaihdat tilaa** milloin tahansa valitsemalla nimen listasta.

---

## Mitä ostaa (aloituspaketit)

Valitse **yksi** projekti alkuun. Kaikki käyttävät samaa perusohjelmistoa.

### Helpoin aloitus: Aaltomaalari (vain CoreS3)

| Tuote | Noin rooli |
|-------|------------|
| M5Stack CoreS3 | Päälaite näytöllä |
| USB-C-kaapeli | Tulee yleensä laitteen mukana |

### Askelalustat: Mnemonic DDR

| Tuote | Määrä |
|-------|-------|
| M5Stack Core2 | 1 |
| M5Stack PbHub Unit | 1 |
| M5Stack FSR Unit | 4 |
| Grove-kaapelit (HY2.0-4P) | 5 |

### Täysi lista

Katso [Artefattiluettelo](ARTIFACTS.md) jokaisen BOM-listan osalta.

---

## Kertaluonteinen käyttöönotto (pyydä teknistä ystävää TAI seuraa tarkasti)

### Tietokoneellasi

1. Asenna **Python 3** osoitteesta [python.org](https://www.python.org/downloads/) (valitse Windowsissa "Add to PATH").
2. Avaa terminaali `M5-Utah`-kansiossa.
3. Aja:
   ```
   py -3 -m pip install -r requirements.txt
   ```
4. Jos sait valmiin `m5_integrated_kernel.bin`-tiedoston, sen pitäisi olla jo `M5-Utah/payloads/`-kansiossa. Jos ei, teknisen ystävän täytyy rakentaa se (katso [Tekninen opas](03-FOR_TECHNICAL_USERS.md)).

### M5Stackilla (vain ensimmäisellä kerralla)

1. Yhdistä M5Stack tietokoneeseen USB-C:llä.
2. Aja:
   ```
   py -3 run_omni_flash.py
   ```
3. Odota **SUCCESS**. Laite on nyt tyhjä "vastaanotin".

**Flashaat vain kerran**, ellei sinulla ole uutta levyä tai suurta firmware-päivitystä.

---

## Päivittäinen käyttö (joka kerta, kun haluat uuden laitetilan)

1. Kytke USB-C.
2. Aja:
   ```
   py -3 run_studio.py
   ```
3. Näet numeroidun listan, esimerkiksi:
   ```
   [0] Cellular_Regenesis_Chamber.flux.json  (Med-Bed / cores3)
   [1] Holographic_Printing_Press_V5.flux.json  ...
   ...
   ```
4. Kirjoita numero ja paina Enter.
5. M5Stack käynnistyy uudelleen kyseiseen tilaan. Valmis.

### Pikakuvake (jos joku antoi sinulle nimen)

```
py -3 run_studio.py --artifact mnemonic_ddr_infinity
```

### Listaa tilat ilman kytkentää

```
py -3 run_studio.py --list
```

---

## Fyysinen kokoaminen (ei juottamista)

Kaikki M5Stack-yksiköt käyttävät **Grove-kaapeleita** — värikkäitä liittimiä, jotka napsahtavat paikalleen.

**Esimerkki — askelalustat:**

1. Kytke **PbHub** **Port A**an (punainen) Core2:ssa.
2. Kytke jokainen **FSR** PbHubin kanaviin **CH0, CH1, CH2, CH3**.
3. Aseta jokainen FSR lattialaudan tai pahvilaatan "askelalueen" alle.

**Esimerkki — Med-Bed-äänidemo:**

1. Kytke **Unit-DAC** Port Aan CoreS3:ssa.
2. Kytke **Unit-Relay** Port B:hen.
3. Liitä pienet kaiuttimet tai exciterit ruuviliittimiin (aikuisen apu).

Kaaviot ja porttien nimet: [Artefattiluettelo](ARTIFACTS.md).

---

## Miten tiedät, että se toimii

| Laitetila | Sinun pitäisi nähdä… |
|-----------|----------------------|
| Aaltomaalari | Värit liikkuvat näytöllä |
| Askelmuisti | Numero kasvaa, kun poljet laatoilla |
| Hum-laatikko | Tila AtomS3-näytöllä; käämi ohjataan MOSFETin kautta (käytä oskilloskooppia tai LEDiä käämissä, jos epäilet) |
| Med-Bed-demo | Sarjaportin viestit; ääni transduktoreista, jos johdotettu |
| Käsi-tulostin | Z-korkeus kasvaa, kun pyyhkäiset alas eleanturin edessä |
| Sotapöytä | Näyttö sanoo ACTIVE tai HALT, kun heilutat kättä ToF-anturin yläpuolella |

Jos mitään ei tapahdu: katso **Vianmääritys** alla.

---

## Vianmääritys

| Ongelma | Kokeile tätä |
|---------|--------------|
| "No M5Stack detected" | Toinen USB-kaapeli; kokeile toista USB-porttia; asenna CP210x- tai CH340-ajuri (googlaa levyn nimi + "USB driver") |
| Flash epäonnistuu | Pidä **BOOT**-painiketta pohjassa kytkettäessä USB, yritä sitten `run_omni_flash.py` uudelleen |
| Väärä tila injektion jälkeen | Irrota virta, kytke uudelleen, aja `run_studio.py` uudelleen oikealla numerolla |
| Askelalustat eivät toimi | Tarkista, että Grove-kaapeli on napsahtanut kunnolla; PbHub Port A:ssa |
| Näyttö tyhjä | Flashaa kernel uudelleen; varmista, että rakensit/flashasit oikealle levylle (Core2 vs. CoreS3 vs. AtomS3) |

---

## Mitä tämä EI ole

Selkeys auttaa kaikkia:

- **Ei** lääkinnällinen laite. "Med-Bed" on **äänitaajuusdemo**.
- **Ei** oikea holografinen tulostin. Se on **ele + moottori + rele -demo**.
- **Ei** loputon tietokonemuisti. Askeltila **kirjaa poljetapahtumat**.
- **Ei** todistettu "psykotroninen" teknologia. Se tuottaa **tunnettuja taajuuksia** (7,83 Hz, 40 Hz) GPIO-napilla.

**Tarina ja nimet** tulevat UFW:n luovasta arkistosta. **Laitteiston käyttäytyminen** on tavallista elektroniikkaa, jonka voit testata silmillä ja korvilla.

Lisätietoa: [Skeptikoille](05-FOR_SKEPTICS.md)

---

## Alkuperäinen UFW vs. M5 (mitkä ohjeet?)

| Tilanne | Lue |
|---------|-----|
| Sinulla on **vanha 27-kansion** repo-rakenne | [Alkuperäinen World-A -lähestymistapa](07-ORIGINAL_WORLDA_APPROACH.md) |
| **Siirryt** leipäpöydästä/Arduinosta M5:een | [Siirtymisopas](06-MIGRATION_FROM_ORIGINAL.md) |

## Apua tarvittaessa

| Tarve | Lue |
|-------|-----|
| Lapsille sopiva selitys | [Lapsille](01-FOR_CHILDREN.md) |
| Rakenna firmware itse | [Teknisille käyttäjille](03-FOR_TECHNICAL_USERS.md) |
| Mittaa ja viittaa kokeisiin | [Tutkijoille](04-FOR_SCIENTISTS.md) |
| Kaikki osien nimet | [Sanasto](GLOSSARY.md) |
