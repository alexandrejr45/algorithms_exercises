# Calcular o volume livre de um esfera circunscrita em um cubo
from math import pi

raio_esfera = float(input("Raio da esfera\n"))
aresta_cubo = float(input("Aresta do cubo\n"))
volume_esfera = 4 * pi * (raio_esfera ** 3)
volume_cubo = aresta_cubo ** 3


if volume_cubo < volume_esfera:
    print("Não há volume livre")
    print("O volume do cubo é menor que o volume da esfera")
else:
    volume_livre = volume_cubo - volume_esfera
    print("Volume Livre")
