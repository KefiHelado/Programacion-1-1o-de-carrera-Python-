from turtle import *

r = int(input("Indica la longitud del radio: "))
n = int(input("Indica el valor de n: "))
penup()
goto(0, -r)
pendown()
circle(r)
penup()
color('red')
for i in range(n):
    x=0
    y=0
    x=int(input("Dime las coordenadas de un punto x dentro del circulo: "))
    y=int(input("Dime las coordenadas de un punto y dentro del circulo: "))
    goto(x,y)
    dot(4)

print("Se han dibujado {0} puntos".format(n))

