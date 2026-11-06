cadena = input("Dime una cadena de números: ")
resumida = ""
cantidad = 0
yavistos = []
for i in cadena:
    if i not in yavistos:
        digito = i
        for j in cadena:
            if j == digito:
                cantidad +=1
        resumida = resumida + str(cantidad) + digito
        yavistos.append(i)
        cantidad = 0
print(resumida)