from zadanie import Zadanie


class Aplikacja:
    def __init__(self):
        self.zadania = [
            Zadanie('Posprzątaj pokój'),
            Zadanie('Umyj auto')
        ]

    def wypisz(self):
        for indeks, zadanie in enumerate(self.zadania):
            print(f'[{indeks}].', zadanie.wypisz())

    def dodaj(self):
        nazwa = self.pobierz_nazwe_przypomnienia()
        zadanie = Zadanie(nazwa)
        self.zadania.append(zadanie)
        self.wypisz()

    def usun(self):
        indeks = self.pobierz_indeks()
        del self.zadania[indeks]
        self.wypisz()

    def oznacz_jako_zrobione(self):
        indeks = self.pobierz_indeks()
        self.zadania[indeks].ustaw_jako_zrobione()
        self.wypisz()

    def pobierz_indeks(self) -> int:
        jest_ok = False
        while not jest_ok:
            indeks = int(
                input("Którego wydarzenia dotyczy działanie? : "))
            if indeks < len(self.zadania):
                jest_ok = True
        return indeks

    def pobierz_nazwe_przypomnienia(self) -> str:
        jest_ok = False
        while not jest_ok:
            nazwa = input('Powiedz, co masz do zrobienia? ')
            if len(nazwa) > 3:
                jest_ok = True
        return nazwa
