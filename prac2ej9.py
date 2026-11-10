from turtle import *
from random import *
pantalla = Screen()
pantalla.setup(824, 425)
pantalla.screensize(800, 400)
goto(0, 0)
loop = 0
cantidad = randint(1, 50)
while (loop < cantidad):
    trazos = int(input("Indica el número de trazos aleatorios: "))
    for i in range(trazos):
        grosor = randint(1, 20)
        redvar = random()
        greenvar = random()
        bluevar = random()
        color(redvar, greenvar, bluevar)
        pensize(grosor)
        goto(randint(0, 800), randint(0, 400))
    loop +=1