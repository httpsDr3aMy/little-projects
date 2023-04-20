'''
Wejście: Parametry wejściowe to:

1. Słownik person z następującymi kluczami:

- name: ciąg znaków reprezentujący imię i nazwisko osoby (np. "John Doe")

- age: liczba całkowita reprezentująca wiek osoby (np. 30)

- skills: lista ciągów znaków reprezentujących umiejętności osoby (np. ['Python', 'JavaScript', 'C++'])

2. Lista ciągów znaków skills reprezentująca wymagane umiejętności do wykonania określonego zadania (np. ['Python', 'JavaScript'])

Wyjście: Funkcja musi zwrócić wartość Boolean wskazującą, czy osoba posiada wszystkie wymagane umiejętności.
'''

def czy_posiada_wymagane_umiejetnosci(osoba, umiejetnosci):
    return all(umiejetnosci in osoba['skills'] for umiejetnosci in wymagane_umiejetnosci)

John = {
    'name': 'John Doe',
    'age': 30,
    'skills': ['Python', 'JavaScript', 'C++']
}

Jane = {
    'name': 'Jane Smith',
    'age': 25,
    'skills': ['Python', 'Java']
}

wymagane_umiejetnosci = ['Python', 'JavaScript']

print(czy_posiada_wymagane_umiejetnosci(John, wymagane_umiejetnosci))


