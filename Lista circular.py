cadena = str(input("Dime una frase o varias palabras separadas: "))
lista = []
palabra = ""

for i in cadena: 
    if i != " ":
        palabra +=i
    else:
        lista.append(palabra)
        palabra = ""

if palabra: 
    lista.append(palabra)

check = True

for i in range(len(lista)):
    ultima = lista[i][-1]
    primera = lista [(i+1) % len(lista)][0]
    if ultima == primera:
        check = True
    else:
        check = False

print(check)