'''
Napisz funkcję która dla przykładu po wywołaniu:

print(count(2,4,1,2,4,5, 10))

pokaże jako wynik:

28

czyli sumę wszystkich argumentów.
''' 
container = []

def sum_elements(*container):
    return sum(container)
    
print(sum_elements(2,4,1,2,4,5,10)) #rozwiazanie z wieloargumentowa funkcja


