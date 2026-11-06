cadena = str(input("Dime una frase o varias palabras separadas: "))
a = []
palabra = ""

for i in cadena:
    if i != " ":
        palabra +=i
    else:
        a.append(palabra)
        palabra = ""

if palabra: 
    a.append(palabra)

print (a)