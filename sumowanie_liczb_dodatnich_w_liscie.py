'''
Napisz funkcję, która jako argument przyjmuje listę liczb i zwraca sumę wszystkich liczb dodatnich na liście. 
Funkcja powinna ignorować wszelkie liczby ujemne lub zera na liście.
'''

def sumowanie_liczb_dodatnich_w_liscie(lista_z_liczbami):
    return sum(liczba for liczba in lista_z_liczbami if liczba > 0)

liczby = [-1, 0, 2, 9]

    
print(sumowanie_liczb_dodatnich_w_liscie(liczby))