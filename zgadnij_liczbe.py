szukana_liczba = 20
zgadywana_liczba = 0

while szukana_liczba!=zgadywana_liczba:
    zgadywana_liczba = int(input('Wprowadz liczbe: '))
    if szukana_liczba == zgadywana_liczba:
        print('Zgadles liczbe!')
        break
    elif szukana_liczba > zgadywana_liczba:
        print('Szukana liczba jest większa!')
    elif szukana_liczba < zgadywana_liczba:
        print('Szukana liczba jest mniejsza!')