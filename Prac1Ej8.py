from turtle import *
radio = int(input("Indica el radio del circulo: "))
x = int(input("Indica el centro del circulo en el eje x: "))
y = int(input("Indica el centro del circulo en el eje y: "))
penup()
goto(x, y)
write("({1},{1})".format(x, y))
goto (x, y-radio)
pendown()
write("Radio = {0}".format(radio))
circle(radio)
    
