entero = int(input("Indicame un numero entero para convertirlo en una lista: "))
lista = []
while entero > 0:
    i = entero%10
    lista.append(i)
    entero = entero // 10

print(lista[::-1])