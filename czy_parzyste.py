lista = [1, 2, 3, 5, 6, 32, 9]

parzysta_lista = list(filter(lambda x: x % 2 == 0, lista))
print(parzysta_lista)
    