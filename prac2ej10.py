from turtle import *

lados = int(input("Indica la cantidad de lados de la que quieres tu figura: "))
longitud = int(input("Indica la longitud de los lados: "))
radio = int(input("Indica el radio de los círculos: "))
color("blue")

for i in range(lados):
    circle(radio)
    forward(longitud)
    left(360/lados)
