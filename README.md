# buduruoka

# Tavoite:
#    Sovelluksessa käyttäjät pystyvät jakamaan ruokareseptejään. Reseptissä lukee tarvittavat ainekset ja valmistusohje.
#    Käyttäjä pystyy luomaan tunnuksen ja kirjautumaan sisään sovellukseen.
#    Käyttäjä pystyy lisäämään reseptejä ja muokkaamaan ja poistamaan niitä.
#    Käyttäjä näkee sovellukseen lisätyt reseptit.
#    Käyttäjä pystyy etsimään reseptejä hakusanalla.
#    Käyttäjäsivu näyttää, montako reseptiä käyttäjä on lisännyt ja listan käyttäjän lisäämistä resepteistä.
#    Käyttäjä pystyy valitsemaan esimerkiksi seuraavia luokitteluja:
#        Ruoan tyyppi: alkuruoka, pääruoka tai jälkiruoka
#        Ruokavalio: laktoositon, gluteeniton tai vegaaninen
#        Ruoan hinta: edullinen, super edullinen tai puoli-ilmainen
#        Valmistuksen nopeus: hidas, keskiverto, nopea
#    Käyttäjä pystyy antamaan reseptille kommentin ja arvosanan. Reseptistä näytetään kommentit ja keskimääräinen arvosana.
#
# Tässä pääasiallinen tietokohde on ruokaresepti ja toissijainen tietokohde on kommentti reseptiin.
## Sovelluksen testaaminen:
#
# 1. Kloonaa repositorio ja siirry projektin kansioon.
#
# 2. Luo virtuaaliympäristö:
#
#
# python3 -m venv venv
#
#
# 3. Aktivoi virtuaaliympäristö:
#
# macOS / Linux:
#
# bash
# source venv/bin/activate
#
#
# Windows:
#
#
# venv\Scripts\activate
#
#
# 4. Asenna Flask:
#
#
# pip install flask
#
#
# 5. Luo SQLite-tietokanta `schema.sql`-tiedoston perusteella:
#
#
# sqlite3 database.db < schema.sql
#
#
# 6. Käynnistä sovellus:
#
#
# flask run
#
#
# 7. Avaa selaimessa:
#
#
# http://127.0.0.1:5000
#
#
#
# Sovelluksessa voi tällä hetkellä:
#
# rekisteröidä uuden käyttäjän
# - kirjautua sisään ja ulos
# -  lisätä uuden budjettireseptin
# - selata reseptejä etusivulla
# - hakea reseptejä nimellä, ainesosilla tai valmistusohjeen sisällöllä
# - avata reseptin omalle sivulleen
# - muokata omia reseptejä
# - poistaa omia reseptejä
#
# Reseptin lisääminen vaatii kirjautumisen. Käyttäjä voi muokata ja poistaa vain itse lisäämiään reseptejä.
#
# Tietokantatiedosto `database.db` ei kuulu repositorioon, vaan se luodaan paikallisesti `schema.sql`-tiedoston perusteella.
