from turtle import *

lado = int(input("Indica el largo de los lados: "))
x = int(input("Indica el centro del circulo en el eje x: "))
y = int(input("Indica el centro del circulo en el eje y: "))
radio = lado/1.4

pantalla = Screen()
pantalla.setup(425, 225)
pantalla.screensize(400, 200)
tortuga = Turtle()
penup()
goto(-lado/2,lado/2)
pendown()
pencolor('red')
goto(lado/2,lado/2)
goto(lado/2,-lado/2)
goto(-lado/2,-lado/2)
goto(-lado/2,lado/2)
penup()
goto(0,-radio)
pendown()
pencolor('blue')
circle(radio)
penup()
goto(x,y)

if x < lado/2 and x > -lado/2 and y < lado/2 and y > -lado/2:
    pencolor('red')
    
elif x < radio and x > -radio and y < radio and y > -radio:
    pencolor('blue')
    
else:
    pencolor('green')

dot()
goto(0,0)
pencolor('black')
write("(0,0)")
