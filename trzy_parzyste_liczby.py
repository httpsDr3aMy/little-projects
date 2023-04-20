#Napisz program, który doda 3 parzyste liczby dodatnie podane przez użytkownika

'''
Jeśli liczba będzie niedodatnia lub nieparzysta to program ma zapytać się o liczbę jeszcze raz. Program ma pytać się o liczby parzyste dodatnie, dopóki nie doda 3 liczb.
Pamiętaj liczby mają być i parzyste i dodatnie w tym samym momencie!

Liczby spełniające warunek to np. 2, 4

Liczby niespełniające warunek to np. -2, -8, -5, 3
'''

suma = 0
i = 0

while i != 3:
    liczba = int(input('\nPodaj parzysta liczbe: '))
    if liczba % 2 == 0 and liczba > 0:
        suma += liczba
        i += 1
    elif liczba % 2 != 0 and liczba > 0:
        print('Prosze podac liczbe parzysta.')
    elif liczba % 2 == 0 and liczba < 0:
        print('Prosze podac liczbe dodatnia.')
    elif liczba % 2 != 0 and liczba < 0:
        print('Prosze podac dodatnia liczbe parzysta.')
    elif liczba == 0:
        print('Zero nie jest parzyste.')
print(f'Suma podanych liczb wynosi: {suma}.')
    