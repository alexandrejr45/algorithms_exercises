# Calcular o volume de uma esfera
import math

diametro = float(input("Diâmetro \n"))
raio = diametro / 2
volume = (4 * math.pi * (raio ** 3)) / 3

print(volume)
