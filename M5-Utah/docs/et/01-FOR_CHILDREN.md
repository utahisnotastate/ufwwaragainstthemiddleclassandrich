# M5 maagilised kastid — juhend lastele (täiskasvanuga)

**Vanus:** umbes 8–14 aastat  
**Vajad:** täiskasvanut USB-kaablite, ühendamise ja osade ostmise jaoks.

---

## Mis see on?

Kujuta ette **väikest arvutit ekraaniga**, mis saab vahetada tööd nagu videomängu tegelane uue võime valib.

- Ühenda see sülearvutiga USB-kaabli abil.
- Vali **režiim** (me nimetame seda *artefaktiks*).
- Kast **muutub** — võib saada tantsusammude loenduriks, värviliseks lainemaalijaks või käeliigutuste juhtimiseks.

Kasti nimetatakse **M5Stack**. Sülearvuti programm, mis sellega suhtleb, on **Utah Flux**.

---

## Kuus superrežiimi

| Režiim | Tunne | Mida teed |
|--------|-------|-----------|
| **Lainemaalija** (Zero Point GPU) | Elavad vikerkaare ruudud ekraanil | Vaata, kuidas värvid liiguvad |
| **Sammumälu** (Mnemonic DDR) | Põrandapadjad, mis mäletavad su samme | Tammu padjadel |
| **Sumisev kast** (Psychotronic Amplifier) | Väike kast, mis sumiseb mähise väga aeglaselt | Kuula/tunne mähise lähedal (täiskasvan jälgib) |
| **Heliravi demo** (Med-Bed) | Kaks kõlarit teevad erilisi vastassuunalisi helisid | Istu kõlarite vahel (vaikne helitugevus!) |
| **Käeprinter** (Holographic Press) | Tõmba nähtamatu objekt ülespoole käega | Liiguta kätt allapoole õhus anduri kohal |
| **Sõjalaua laud** (Command Table) | Kapteni laud — liiguta kätt, et kõik peatada | Liiguta kätt keskmise ekraani kohal |

---

## Turvareeglid (oluline!)

1. **Alati ole täiskasvanu juures**, kui ühendad USB-d või juhtmeid.
2. **Ära kunagi** ühenda mähiseid ega kõlareid seinapistikust ilma elektroonikat tundva täiskasvanuta.
3. **Hoia joogid eemal** seadmetest.
4. Kui midagi muutub **kuumaks** või lõhnab **põlenud**, eemalda kohe vool ja ütle täiskasvanule.
5. Need on **demod ja mänguasjad õppimiseks** — need **ei ole** päris meditsiiniseadmed ega maagilised printerid.

---

## Proovi 4 sammuga (täiskasvan kirjutab)

1. **Ühenda** M5Stack arvutiga USB-C kaabli abil.
2. **Kirjuta kord** (ainult esimest korda): täiskasvan käivitab `run_omni_flash.py`.
3. **Vali režiim**: täiskasvan käivitab `run_studio.py` ja valib numbri.
4. **Mängi!** Vaata ekraani ja proovi andureid.

---

## Lõbusad katsed

### Lainemaalija
Loenda, mitu sekundit kulub enne mustri muutumist. Kas oskad ette arvata, kuhu hele koht liigub?

### Sammumälu
Tee rütm: vasak — parem — vasak — vasak. Kas loendur suureneb iga kord?

### Käeprinter
Kui lähedal peab käsi olema, enne kui see reageerib? Mõõda joonlauaga!

### Sõjalaua laud
Kas suudad laua peatada käeliigutusega ja siis uue liigutusega jälle käivitada?

---

## Lugu vs päriselu

Repo kasutab **lahedaid ulme-nimesid** kindral 23 ajajoontest. Päriselus:

- **„lõputu mälu“** on **sammude loendur ja logija**, mitte maagiline salvestus.
- **„med-bed“** teeb **helilaineid**, mida saad mõõta — see **ei ravi inimesi**.
- **„3D-printer“** liigutab mootorit ja vilgutab UV-tuld **demona** — see **ei prindi objekte mõtetest**.

See on okei! Päris andurite ja arvutite töö õppimine on ikka äge.

---

## Sõnad, mida teada

- **USB-kaabel** — juhe, mis räägib arvutiga.
- **Andur** — osa, mis tunneb samme, käeliigutusi või kaugust.
- **Ekraan** — näitab, mis toimub.
- **Režiim / artefakt** — millist tööd kast parasjagu teeb.

Rohkem sõnu: [Sõnastik](GLOSSARY.md)

---

## Mida edasi lugeda

- Täiskasvanu seadistus: [Mittetehnilistele kasutajatele](02-FOR_NON_TECHNICAL_USERS.md)
- Osade pildid: [Artefaktide kataloog](ARTIFACTS.md)
