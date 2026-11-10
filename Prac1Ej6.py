from turtle import *

lado = int(input("Indica el largo de los lados: "))

pantalla = Screen()
pantalla.setup(425, 225)
pantalla.screensize(400, 200)
tortuga = Turtle()
goto(0, lado)
write("(0, {0}".format(lado))
goto(lado, lado)
write("({0}, {1}".format(lado,lado))
goto(lado, 0)
write("({0},0".format(lado))
goto(0,0)
write("(0, 0)")
pantalla.exitonclick
