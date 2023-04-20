dostep = ['Alan', 'Adam', 'Arkadiusz']

while True:
    print('1. Sprawdz dostep')
    print('2. Zatrzymaj program')
    odpowiedz_uzytkownika = int(input('Wybierz funkcje: '))
    
    if odpowiedz_uzytkownika == 1:
        sprawdz_dostep = str(input('Wprowadz nazwe uzytkownika ktoremu chcesz sprawdzic czy ma dostep: '))
        if sprawdz_dostep in dostep:
            print(f'Uzytkownik {sprawdz_dostep} posiada dostep.')
        else:
            print(f'Uzytkownik {sprawdz_dostep} nie posiada dostepu.')
    elif odpowiedz_uzytkownika == 2:
        break
    else:
        print('Brak takiej funkcji.')

    