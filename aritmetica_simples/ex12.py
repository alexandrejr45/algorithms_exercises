# Calcular o volume de um cone
from math import pi

altura = float(input("Altura\n"))
raio_base = float(input("Raio da base\n"))
volume = (pi * (raio_base ** 2) * altura) / 3

print("Volume do cone: ", round(volume, 2))
