def tworz_liste(max):
    lista = []
    for i in range(max+1):
        lista.append(i)
    return lista
        

def czy_nalezy(lista, odpowiedz):
    if odpowiedz in lista:
        return True
    else:
        return False
        
max = int(input('Podaj maxa: '))
odpowiedz = int(input('Jakiej liczby szukasz? '))
print(tworz_liste(max))
print(czy_nalezy(tworz_liste(max), odpowiedz))
