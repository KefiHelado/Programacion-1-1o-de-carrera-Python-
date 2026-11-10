i = int(input("Indicame el número del cual quieres calcular la raíz cuadrada entera: "))
j=0
while(j < i):
    if j**2 <= i and (j+1)**2 > i:
        print("La raíz cuadrada entera es: ", j)
        j+=1
    else:
        j+=1
