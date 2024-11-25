from datetime import datetime

class Jarat:
    def __init__(self, szam, celallomas, jegyar):
        self.szam = szam
        self.celallomas = celallomas
        self.jegyar = jegyar

    def __str__(self):
        return f"Járatszám: {self.szam}, Célállomás: {self.celallomas}, Jegyár: {self.jegyar} Ft"

class HelyiJarat(Jarat):
    pass

class KulfoldiJarat(Jarat):
    pass

class Legitarsasag:
    def __init__(self, nev):
        self.nev = nev
        self.jaratok = []

    def jarat_hozzadasa(self, jarat):
        self.jaratok.append(jarat)

    def jarat_kilistazasa(self):
        return self.jaratok

class Foglalas:
    def __init__(self, utas_nev, jarat, datum):
        self.utas_nev = utas_nev
        self.jarat = jarat
        self.datum = datum

    def __str__(self):
        return f"Utas neve: {self.utas_nev}, Járat: {self.jarat.szam}, Dátum: {self.datum}"

class Rendszer:
    def __init__(self):
        self.foglalasok = []

    def uj_foglalas(self, utas_nev, jarat, datum, kiir=True):
        if jarat:
            foglalas = Foglalas(utas_nev, jarat, datum)
            self.foglalasok.append(foglalas)
            if kiir:
                print(f"Sikeres foglalás: {utas_nev} számára a(z) {jarat.szam} járatra.")
        else:
            if kiir:
                print("Hibás járat!")

    def foglalas_torlese(self, utas_nev, jarat_szam):
        torolve = False
        for foglalas in self.foglalasok:
            if foglalas.utas_nev == utas_nev and foglalas.jarat.szam == jarat_szam:
                self.foglalasok.remove(foglalas)
                torolve = True
                print(f"A foglalás törölve: {utas_nev}, {jarat_szam}.")
                break
        if not torolve:
            print("Nincs ilyen foglalás.")

    def foglalasok_kiirasa(self):
        if self.foglalasok:
            print("\n--- Aktív foglalások ---")
            for foglalas in self.foglalasok:
                print(foglalas)
        else:
            print("Nincsenek aktív foglalások.")

if __name__ == "__main__":
    # Légitársaság létrehozása
    airline = Legitarsasag("SkyFly")

    # Járatok létrehozása
    belfoldi = HelyiJarat("SF001", "Debrecen", 12000)
    nemzetkozi1 = KulfoldiJarat("SF002", "Berlin", 35000)
    nemzetkozi2 = KulfoldiJarat("SF003", "New York", 85000)

    # Járatok hozzáadása
    airline.jarat_hozzadasa(belfoldi)
    airline.jarat_hozzadasa(nemzetkozi1)
    airline.jarat_hozzadasa(nemzetkozi2)

    # Foglalási rendszer létrehozása
    foglalasi_rendszer = Rendszer()

    # 10 előre betöltött foglalás (nem jelenik meg az indításkor)
    foglalasi_rendszer.uj_foglalas("Varga János", belfoldi, datetime(2024, 11, 18, 14, 0), kiir=False)
    foglalasi_rendszer.uj_foglalas("Kiss Petra", nemzetkozi1, datetime(2024, 11, 18, 18, 0), kiir=False)
    foglalasi_rendszer.uj_foglalas("Szabó Anna", nemzetkozi2, datetime(2024, 11, 19, 10, 0), kiir=False)
    foglalasi_rendszer.uj_foglalas("Nagy Péter", belfoldi, datetime(2024, 11, 20, 9, 0), kiir=False)
    foglalasi_rendszer.uj_foglalas("Molnár Gábor", nemzetkozi1, datetime(2024, 11, 20, 15, 0), kiir=False)
    foglalasi_rendszer.uj_foglalas("Horváth Zsófia", nemzetkozi2, datetime(2024, 11, 21, 12, 30), kiir=False)
    foglalasi_rendszer.uj_foglalas("Takács László", belfoldi, datetime(2024, 11, 22, 8, 0), kiir=False)
    foglalasi_rendszer.uj_foglalas("Kovács Márta", nemzetkozi1, datetime(2024, 11, 23, 17, 0), kiir=False)
    foglalasi_rendszer.uj_foglalas("Tóth Balázs", nemzetkozi2, datetime(2024, 11, 24, 11, 30), kiir=False)
    foglalasi_rendszer.uj_foglalas("Bodnár Lilla", belfoldi, datetime(2024, 11, 25, 13, 0), kiir=False)

    # Kezdő menü
    while True:
        print("\n--- Foglalási rendszer ---")
        print("1. Elérhető járatok")
        print("2. Foglalás készítése")
        print("3. Foglalás törlése")
        print("4. Aktív foglalások")
        print("5. Kilépés")

        valasztas = input("Válasszon opciót: ")

        if valasztas == "1":
            for jarat in airline.jarat_kilistazasa():
                print(jarat)

        elif valasztas == "2":
            nev = input("Adja meg az utas nevét: ")
            jarat_szam = input("Adja meg a járatszámot: ")
            jarat = next((jarat for jarat in airline.jaratok if jarat.szam == jarat_szam), None)
            if jarat:
                datum = datetime.strptime(input("Adja meg a foglalás dátumát (YYYY-MM-DD HH:MM): "), "%Y-%m-%d %H:%M")
                foglalasi_rendszer.uj_foglalas(nev, jarat, datum)
            else:
                print("Járat nem található!")

        elif valasztas == "3":
            nev = input("Adja meg az utas nevét: ")
            jarat_szam = input("Adja meg a járatszámot: ")
            foglalasi_rendszer.foglalas_torlese(nev, jarat_szam)

        elif valasztas == "4":
            foglalasi_rendszer.foglalasok_kiirasa()

        elif valasztas == "5":
            break
        else:
            print("Érvénytelen opció!")
