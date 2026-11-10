from turtle import *

lado = int(input("Indica el largo de los lados: "))

pantalla = Screen()
pantalla.setup(425, 225)
pantalla.screensize(400, 200)
tortuga = Turtle()
pendown()
forward(lado)
right(90)
forward(lado)
right(90)
forward(lado)
right(90)
forward(lado)
goto(lado,-lado)
left(90)
forward(90)
goto(lado, 0)
goto(lado/2, (((lado*lado*2)**0.4)))
goto (0,0)

pantalla.exitonclick
