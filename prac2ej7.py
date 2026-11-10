from turtle import *
pantalla = Screen()
pantalla.setup(824, 425)
pantalla.screensize(800, 400)
shape("turtle")
penup()
while(xcor() < 800 and ycor() < 400):
    grados=int(input("Indica los grados que quieres que se mueva la tortuga: "))
    distancia=int(input("Indica la distancia que quieres que se mueva la tortuga: "))
    right(grados)
    forward(distancia)
    stamp()