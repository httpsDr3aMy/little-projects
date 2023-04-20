def suma_kolejnych_liczb(min, max):
    return sum(range(min, max+1))

min = int(input('Wprowadz najmniejsza liczbe ktora ma byc sumowana: '))
max = int(input('Wprowadz najwieksza liczbe ktora ma byc sumowana: '))
print(suma_kolejnych_liczb(min, max))