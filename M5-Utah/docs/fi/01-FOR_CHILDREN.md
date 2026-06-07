# M5-magiat laatikot — opas lapsille (aikuisen kanssa)

**Ikä:** noin 8–14 vuotta  
**Tarvitset:** aikuisen USB-kaapeleihin, kytkentään ja osien ostoon.

---

## Mikä tämä on?

Kuvittele **pieni tietokone näytöllä**, joka voi vaihtaa tehtävää kuin videopelihahmo valitsee uuden voiman.

- Kytket sen kannettavaan tietokoneeseen USB-kaapelilla.
- Valitset **tilan** (kutsumme sitä *artefaktiksi*).
- Laatikko **muuttuu** — se voi muuttua tanssiaskelelaskuriksi, värikkääksi aaltojen maalariksi tai kädenheilutusohjaimiksi.

Laatikkoa kutsutaan **M5Stackiksi**. Kannettavan ohjelmaa, joka puhuu sen kanssa, kutsutaan **Utah Fluxiksi**.

---

## Kuusi supertilaa

| Tila | Miltä se tuntuu | Mitä teet |
|------|-----------------|-----------|
| **Aaltomaalari** (Zero Point GPU) | Elävät sateenkaarineliöt näytöllä | Katsot värien liikkumista |
| **Askelmuisti** (Mnemonic DDR) | Lattialaatat, jotka muistavat askeleesi | Poljet laatoilla |
| **Hum-laatikko** (Psychotronic Amplifier) | Pieni laatikko, joka värähtelee käämiä hyvin hitaasti | Kuuntelet/tunnet lähellä käämiä (aikuinen valvoo) |
| **Ääniparantaja-demo** (Med-Bed) | Kaksi kaiutinta tekee erityisiä vastakkaisia ääniä | Istut kaiuttimien välissä (hiljainen äänenvoimakkuus!) |
| **Käsi-tulostin** (Holographic Press) | Vedät näkymätöntä esinettä ylöspäin kädelläsi | Pyyhkäiset ilmassa anturin yläpuolella |
| **Sotapöytä** (Command Table) | Kapteenin työpöytä — heilauta kättä pysäyttääksesi kaiken | Heilautat keskellä olevaa näyttöä |

---

## Turvallisuussäännöt (tärkeää!)

1. **Aikuinen aina mukana**, kun kytket USB:ää tai liität johtoja.
2. **Älä koskaan** kytke käämiä tai kaiuttimia seinävirtaan ilman aikuista, joka osaa elektroniikkaa.
3. **Pidä juomat kaukana** laitteista.
4. Jos jokin **kuumentuu** tai haisee **palaneelta**, irrota virta heti ja kerro aikuiselle.
5. Nämä ovat **demoja ja oppimisleluja** — ne **eivät** ole oikeita lääkinnällisiä koneita tai taikaprintereitä.

---

## Kokeile neljässä vaiheessa (aikuinen kirjoittaa komennot)

1. **Yhdistä** M5Stack tietokoneeseen USB-C:llä.
2. **Flashaa kerran** (vain ensimmäisellä kerralla): aikuinen ajaa `run_omni_flash.py`.
3. **Valitse tila**: aikuinen ajaa `run_studio.py` ja valitsee numeron.
4. **Leiki!** Katso näyttöä ja kokeile antureita.

---

## Hauskoja kokeita

### Aaltomaalari
Laske, montako sekuntia kestää ennen kuin kuvio muuttuu. Voitko arvata, minne kirkas piste siirtyy?

### Askelmuisti
Tee rytmi: vasen — oikea — vasen — vasen. Nouseeko laskuri joka kerta?

### Käsi-tulostin
Kuinka lähelle kätesi pitää olla, ennen kuin se reagoi? Mittaa viivaimella!

### Sotapöytä
Voitko jäädyttää pöydän heilautuksella ja sitten vapauttaa sen toisella?

---

## Tarina vs. todellisuus

Repo käyttää **siistejä tieteisfiktionimiä** General 23:n aikajanalta. Todellisuudessa:

- **"Loputon muisti"** on **askellaskuri ja lokikirja**, ei taikamuisti.
- **"Med-bed"** tekee **ääniaaltoja**, joita voit mitata — se **ei paranna** ihmisiä.
- **"3D-tulostin"** liikuttaa moottoria ja väläyttää UV-valoa **demona** — se **ei tulosta** esineitä ajatuksista.

Se on ihan ok! Oppia siitä, miten oikeat anturit ja tietokoneet toimivat, on silti mahtavaa.

---

## Sanoja, jotka kannattaa tietää

- **USB-kaapeli** — johto, joka puhuu tietokoneen kanssa.
- **Anturi** — osa, joka tunnistaa askeleet, käden liikkeet tai etäisyyden.
- **Näyttö** — näyttää, mitä tapahtuu.
- **Tila / artefakti** — mitä tehtävää laatikko tekee juuri nyt.

Lisää sanoja: [Sanasto](GLOSSARY.md)

---

## Mitä lukea seuraavaksi

- Aikuisen käyttöönotto: [Ei-teknisille käyttäjille](02-FOR_NON_TECHNICAL_USERS.md)
- Osien kuvaukset: [Artefattiluettelo](ARTIFACTS.md)
