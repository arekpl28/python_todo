from aplikacja import Aplikacja


if __name__ == '__main__':
    aplikacja = Aplikacja()
    aplikacja.wypisz()
    while True:
        print('-' * 30)
        print(
            'Co chcesz zrowbić? [w-wypisz, d-dodaj, z-oznacz jako zrobione, u-usuń, q-zakończ]: ')
        polecenie = input('Napisz "w", "d", "z", "u" lub "q" : ')
        if polecenie == "w":
            aplikacja.wypisz()
        elif polecenie == "d":
            aplikacja.dodaj()
        elif polecenie == "z":
            aplikacja.oznacz_jako_zrobione()
        elif polecenie == "u":
            aplikacja.usun()
        elif polecenie == "q":
            quit()
        else:
            print("Nie rozumiem...")
