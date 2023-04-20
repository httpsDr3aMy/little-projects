from PIL import Image

nazwaPliku = input('Wprowadz nazwe pliku (oraz jego lokalizacje): ')

image = Image.open(nazwaPliku)

width, height = image.size 

print("Szerokość obrazka:", width)
print("Wysokość obrazka:", height)