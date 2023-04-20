slownik = []

while True:
    print('1. Dodaj nowe pojecie')
    print('2. Znajdz pojecie')
    print('3. Usun pojecie')
    print('4. Wylacz program')
    odpowiedz = int(input('Wybierz opcje: '))
    if odpowiedz == 1:
        pojecie = input('Podaj pojecie: ')
        definicja = input('Podaj definicje: ')
        slownik.append({'pojecie': pojecie, 'definicja': definicja})
    elif odpowiedz == 2:
        odpowiedz2 = input('Szukasz definicji, czy pojecia? ')
        odpowiedz2 = odpowiedz2.lower()
        if odpowiedz2 == 'pojecie':
            szukane_pojecie = input('Wpisz jakiego pojecia szukasz: ')   
            for i in slownik:
                if szukane_pojecie == i.get('pojecie'):
                    print('Znajduje sie takie pojecie i jego definicja jest '+str(i.get('definicja'))+'.')
                    break
                else:
                    continue
        if odpowiedz2 == 'definicja':
            szukana_definicja = input('Wpisz jakiej definicji szukasz: ')        
            for i in slownik:
                if szukana_definicja == i.get('definicja'):
                    print('Znajduje sie taka definicja i jej pojecie to '+str(i.get('pojecie'))+'.')
                    break
                else:
                    continue                
    elif odpowiedz == 3:
        usun_pojecie = input('Jakie chcesz usunac pojecie? ')
        for i in slownik:
            if usun_pojecie == i.get('pojecie'):
                del(i)
                print('Pomyślnie usunięto definicje')
            else:
                continue
    elif odpowiedz == 4:
        break        
    else:
        print('Brak takiej opcji.')    