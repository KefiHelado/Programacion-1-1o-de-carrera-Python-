cadena = input("Dime una cadena: ")
cadena1 = ""
cadena2 = ""

for i in cadena:
    if i != " ":
        cadena1 += i

for j in cadena:
    if j != " ":
        cadena2 = j + cadena2
    

if cadena1 == cadena2:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")
