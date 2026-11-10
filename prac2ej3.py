from turtle import *

lados = int(input("Indica la cantidad de lados de la que quieres tu figura (máximo 6): "))
longitud = int(input("Indica la longitud de los lados: "))

for i in range(lados):
    if lados == 3:
        forward(longitud)
        left(120)

    if lados == 4:
        forward(longitud)
        left(90)

    if lados == 5:
        forward(longitud)
        left(72)

    if lados == 6:
        forward(longitud)
        left(60)
