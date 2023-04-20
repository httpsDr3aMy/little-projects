'''
Wykonaj poniższe kroki, aby ukończyć ćwiczenie:

1. Utwórz listę o nazwie „zadania”, która zawiera kilka elementów łańcuchowych, z których każdy reprezentuje zadanie do wykonania.

2. Użyj pętli for i funkcji `enumerate`, aby przeglądać listę zadań. Dla każdej iteracji wydrukuj indeks i zadanie.

3.  Wyszukaj w Internecie, jak zmienić punkt początkowy funkcji wyliczającej. Zmodyfikuj pętlę for, aby używała indeksu początkowego 1 zamiast 0 dla wyliczenia.

4. Ponownie zmodyfikuj pętlę, aby pierwsza litera każdego zadania na liście była pisana wielką literą i wydrukuj je.
'''

zadania = ['Kup', 'sprzedaj', 'wynajmij']

for i, zadanie in enumerate(zadania):
    if zadanie[0].islower():
        print(f'{i+1}. {zadanie.capitalize()}')
    else:
        print(f'{i+1}. {zadanie}')