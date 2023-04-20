'''
Stwórz menu, z którego użytkownik, może wybrać opcje, aby policzyć powierzchnie figur:

1) prostokąta

2) kwadratu

3) trójkąta

4) trapezu

5) koła
'''

import math

def pole_prostokatu():
    a = float(input('Podaj dlugosc boku a: '))
    b = float(input('Podaj dlugosc boku b: '))
    return a * b

def pole_trojkata():
    a = float(input('Podaj dlugosc podstawy: '))
    h = float(input('Podaj wysokosc: '))
    return a * h / 2

def pole_trapezu():
    a = float(input('Podaj dlugosc dluzszej podstawy: '))
    b = float(input('Podaj dlugosc dluzszej podstawy: '))
    h = float(input('Podaj wysokosc: '))
    return ((a+b)*h)/2

def pole_kola():
    r = float(input('Podaj promien kola: '))
    return math.pi * r ** 2

while True:
    print('1. Pole prostokata')
    print('2. Pole kwadratu')
    print('3. Pole trojkata')
    print('4. Pole trapezu')
    print('5. Pole kola')
    print('6. Wylacz')
    odpowiedz = int(input('Wybierz opcję: '))
    if odpowiedz == 1:
        print(pole_prostokatu())
    elif odpowiedz == 2:
        print(pole_prostokatu())
    elif odpowiedz == 3:
        print(pole_trojkata())
    elif odpowiedz == 4:
        print(pole_trapezu())
    elif odpowiedz == 5:
        print(pole_kola())
    elif odpowiedz == 6:
        break
    else:
        print('Brak takiej funkcji.')