from turtle import *
pantalla = Screen()
pantalla.setup(824, 425)
pantalla.screensize(800, 400)
from random import randint
while(xcor() < 800 and ycor() < 400):
    pasos = int(input("Indica la cantidad de pasos del borracho: "))
    for i in range(pasos):
        right(randint(0, 360))
        forward(20)
