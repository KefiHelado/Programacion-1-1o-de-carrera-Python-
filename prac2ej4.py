from turtle import *

peldaños = int(input("Indica la cantidad de peldaños para la escalera: "))
longitud = int(input("Indica la longitud de los peldaños: "))
forward (longitud*peldaños)
for i in range(peldaños):
    left(90)
    forward(longitud)
    left(90)
    forward(longitud)
    right(180)

left(270)
forward(longitud*peldaños)
    
