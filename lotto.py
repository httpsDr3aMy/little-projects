import random, time 

def tworzenie_listy_uzytkownika_oraz_listy_wygrywajacej():
    lista_uzytkownika = [int(input('Podaj liczbę: ')) for _ in range(6)]
    lista_wygrywajaca = (random.sample(range(1, 49), 6))
    return lista_uzytkownika,lista_wygrywajaca

lista_uzytkownika, lista_wygrywajaca = tworzenie_listy_uzytkownika_oraz_listy_wygrywajacej()


def sprawdzanie(lista_uzytkownika, lista_wygrywajaca):
    return sum(x in lista_wygrywajaca for x in lista_uzytkownika)

licznik = sprawdzanie(lista_uzytkownika, lista_wygrywajaca)

print(f'Trafiles {licznik} liczb! Liczby wygrywajace to {lista_wygrywajaca}, a twoje typy to {lista_uzytkownika}.')

