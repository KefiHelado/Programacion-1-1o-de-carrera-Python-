cadena = input("Dime una cadena: ")
for i in cadena:
    if 48 <= ord(i) <= 57:
        print("La cadena contiene un dígito")
        break
    elif 97 <= ord(i) <= 122:
        print("La cadena contiene una letra mínuscula")
        break
else:
    print("La cadena no contiene ningún dígito ni mínuscula")