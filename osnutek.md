# Razlike v povprečnih mesečnih plačah v Sloveniji glede na regijo, starost in spol

### Avtorji: Miha Kralj, Armen Hodža, Tone Pivk

## Opis problema in cilji analize: 

V Sloveniji obstajajo velike razlike v povprečnih mesečnih plačah med različnimi regijami, starostnimi skupinami in spoloma. Namen analize je raziskati te razlike ter ugotoviti, kateri dejavniki najbolj vplivajo na razlike v plačah. Med ključnimi vprašanji, na katera želimo odgovoriti, so:
* Kako so se povprečne mesečne plače spreminjale v obdobju 2008–2022?
* Kakšne so razlike med spoloma v posameznih regijah in starostnih skupinah?
* Kako močno starost vpliva na povprečno plačo v posamezni regiji?

## Vir in oblika podatkov

Podatke smo pridobili iz portala OPSI (Odprti podatki Slovenije). Podatki vključujejo različne kategorije, kot so povprečna plača, mediana plače, percentili.. Organizirani so v obliki .px datotek in zajemajo naslednje dimenzije:
* Regija prebivališča (12 regij Slovenije)
* Starostne skupine (npr. 15–24, 25–34, 35–44, 45–54, 55–64, 65+)
* Spol (moški, ženske)
* Leto (2008–2022)

Link: [Podatki OPSI](https://podatki.gov.si/dataset/surs0711322s)

## Vir in oblika podatkov

Podatke smo pridobili iz portala OPSI (Odprti podatki Slovenije). Podatki vključujejo različne kategorije, kot so povprečna plača, mediana plače, percentili. Organizirani so v obliki .px datotek in zajemajo naslednje dimenzije:

*   Regija prebivališča (12 regij Slovenije)
*   Starostne skupine (npr. 15–24, 25–34, 35–44, 45–54, 55–64, 65+)
*   Spol (moški, ženske)
*   Leto (2008–2022)

Link: [Podatki OPSI](https://podatki.gov.si/dataset/surs0711322s)

## Zahteve za namestitev (requirements.txt)

Za zagon tega projekta potrebujete naslednje Python pakete. Seznam paketov je shranjen v datoteki `requirements.txt`.

**Navodila za namestitev:**

1.  Prepričajte se, da imate nameščen Python in pip.
2.  Odprite ukazno vrstico ali terminal v mapi, kjer se nahaja datoteka `requirements.txt`.
3.  Za namestitev vseh potrebnih paketov zaženite naslednji ukaz:

    ```bash
    pip install -r requirements.txt
    ```

    Ta ukaz bo namestil vse pakete, navedene v datoteki `requirements.txt`.