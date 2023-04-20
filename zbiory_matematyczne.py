zbior_a = set()
zbior_b = set()

while True:
    zakoncz = int(input('Aby zakonczyc program wpisz 1: '))
    if zakoncz == 1:
        print('Program wylaczono.')
        break
    else:
        ile_elementow_a = int(input('Wybierz ile elementow ma byc w zbiorze a: '))
        ile_elementow_b = int(input('Wybierz ile elementow ma byc w zbiorze b: '))

        for _ in range(ile_elementow_a):
            element_a = int(input('Wprowadz element zbioru a: '))
            zbior_a.add(element_a)

        for _ in range(ile_elementow_b):
            element_b = int(input('Wprowadz element zbioru b: '))
            zbior_b.add(element_b)
        print('\n1. Koniunkcja')
        print('2. Suma')
        print('3. Zbiór elementów, które były w A, ale nie ma ich w B')
        print('4. Zbiór elementów, które były w B, ale nie ma ich w A')
        print('5. Alternatywa')
        print('6. Usunięcie podanego elementu ze zbioru A')
        print('7. Usunięcie podanego elementu ze zbioru B')
        odpowiedz = int(input('Wybierz opcję: '))
        if odpowiedz == 1:
            print(zbior_a&zbior_b)
        elif odpowiedz == 2:
            print(zbior_a|zbior_b)
        elif odpowiedz == 3:
            print(zbior_a-zbior_b)
        elif odpowiedz == 4:
            print(zbior_b-zbior_a)
        elif odpowiedz == 5:
            print(zbior_a^zbior_b)
        elif odpowiedz == 6:
            usun = int(input('Wprowadz liczbe, ktora chcesz usunac ze zbioru: '))
            zbior_a.discard(usun)
            print(f'Oto zbiór a po zmianach {zbior_a}')
        elif odpowiedz == 7:
            usun = int(input('Wprowadz liczbe, ktora chcesz usunac ze zbioru: '))
            zbior_b.discard(usun)
            print(f'Oto zbiór a po zmianach {zbior_b}')
        else:
            print('Nie ma takiej funkcji. ')         

