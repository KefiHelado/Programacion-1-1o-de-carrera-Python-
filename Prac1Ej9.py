from turtle import *

lado = int(input("Indica el largo de los lados: "))
radio = lado/2
pantalla = Screen()
pantalla.setup(425, 225)
pantalla.screensize(400, 200)
tortuga = Turtle()
penup()
goto(-lado/2,lado/2)
pendown()
goto(lado/2,lado/2)
goto(lado/2,-lado/2)
goto(-lado/2,-lado/2)
goto(-lado/2,lado/2)
penup()
goto(0,-radio)
pendown()
circle(radio)
