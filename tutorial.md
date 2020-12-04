# Django tutorial
Ez most windows-t feltételez, a virtualenves részeket kihagyjuk, de akit érdekel, annak nagyon is ajánljuk a következő oktatóvideót:
https://www.youtube.com/watch?v=F5mRW0jo-U4&ab_channel=freeCodeCamp.org

## Download Python 3
Itt tudod letölteni a python 3-at: https://www.python.org/downloads/

**Figyelj arra, hogy az Add to PATH be legyen kattintva!**

Másoknál probléma volt, hogy nem a C:-re rakták a pythont. Szerintem ez azért van, mert a fentit elmulasztották, de ha nem menne valami, számolj ezzel is.

Itt tudod megnézni, hogy sikerült-e, illetve hogy milyen verziót használ
``` py -V ```

Így tudsz elindítani egy python interpretert:
``` py ```

Mielőtt továbbmegyünk, érdemes frissíteni a pip-et, a python package managert
``` python -m pip install --upgrade pip ```

## Install django
```  pip install django ```
## Django Project
Ez létrehoz egy django projectet:
``` django-admin startproject EZAPROJEKTNEVE ```

Ez egy új könyvtárat hozott létre, amiben le van már pakolva mindenféle fájl. 
A ``` tree /f ```
paranccsal körbe is tudunk nézni.

A legfontosabb fájl a **manage.py**. Nem kell nézegetni, úgy sincsen benne semmi érthető, elirányít máshova, de a lényeg az, hogy **minden** ehhez a projekthez kapcsolódó parancssoros machinációt (pl. a development szerver elindítása) ezen keresztül kell végrehajtani. 

### runserver
Ha elindítanánk a szervert, akkor az már eldöcög:
``` py manage.py runserver```
De rögtön sikít is, hogy 
```You have [...] unapplied migration(s).```
De azért elfut. Ha ki akarod kapcsolni, akkor CTRL+C.

> Lehetséges probléma: volt, akinél gondot okozott, hogy a számítógép (tehát nem a windows user name) ékezetet tartalmazott, és bár ő tudott projektet csinálni és pythont futtatni, a szerver nem indult el. Nincs jobb ötletem, mint átírni a számítógép nevét ékezetmentesre. Amúgy sem tartom jó ötletnek az ékezetek használatát ilyen helyeken.

Nézzük meg a böngészőben a ``` 127.0.0.1:8000```-en vagy a ``` localhost:8000 ```-on a dev. szervert. 

Sőt, meg lehet nézni, hogy a django-t admin site-tal együtt shippelik: ``` localhost:8000/admin ```

Belépni persze nem tudunk, mert nincs is még admin felhasználó. Elővigyázatosságból még default admin sincs.

### migrate
Na most mivel a parancssorunkon épp a szerver fut, indítsunk új parancssort/powershell

Hozzunk létre egy admint és migráljunk.

1. Hozzunk létre egy admin-t. A Django beépített admin-site-tal rendelkezik, és oda azért jó, ha van belépő is.
	``` py manage.py createsuperuser ```
2. az előbbi műveletünk miatt (és mert újszülött projektről van szó) megváltozott az adatbázis, amit át kéne vezetni a rendszeren. Ehhez egy migrációs fájlt kell létrehozni:
	``` py manage.py makemigration ```
3. Ezt pedig le kell futtatni.
	``` py manage.py migrate ```
	Általában is mindig ez lesz, hogy ha *alapvető szerkezeti* változtatásokat eszközölnénk az adatbázison, pl új mezőt szúrunk be egy táblába vagy új táblákat hozunk létre, akkor mindig kell egy makemigrations + migrate kombó. Új rekordok esetén persze nincs erre szükség, hiszen ilyen változtatásokat a felhasználók is csinálhatnak.
4. Ha esetleg leállt volna, újraindítjuk egy parancssorban/powershellben a **development** szervert.
	```py manage.py runserver```
	Innentől ez itt fut, és amíg a szerver fut, ebben a parancssorban már nemigen csinálunk semmit. Nyissunk egy új parancssort.
A szervert egyébként nem kell minden változtatás után újra elindítani, a kisebb, kezelhető változtatásokkor (pl. más fájlok mentésekor) automatikusan újraindítja magát. Van persze, hogy úgy rontunk el valamit, hogy újra kell indítani a szervert. Ilyenkor **CTRL+C**, és újra 
	```py manage.py runserver```



A nekünk fontos fájlok: 
- **urls.py**: itt tudod megmondani, hogy szerver mit kezdjen a hozzá beérkező url-ekkel. Itt lesznek kiosztva a feladatok, hogy melyik url-t melyik applikációnak melyik view-ja szolgálja ki.
- **settings.py**: itt van minden más alapvető beállítás.

A többihez nem kell nyúlnunk (asgi, wsgi: asynchronous/web server gateway interface)

### Apps

``` py manage.py startapp tanapp```

Ez létrehozza az első appot.

Ez még kevés, hogy a szerver tudjon róla, ezt regisztrálni is kell:
```py


