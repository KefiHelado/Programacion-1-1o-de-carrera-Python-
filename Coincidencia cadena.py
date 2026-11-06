cadena1 = input("Dime una cadena: ")
cadena2 = input("Dime otra cadena: ")
cantidad = 0

if len(cadena1) < len(cadena2):
    longitud_minima = len(cadena1)
    
else:
    longitud_minima = len(cadena2)

for longitud in range(1, longitud_minima + 1):
    coincide = True

    for i in range(longitud):
        indice_cadena1 = len(cadena1) - longitud + i
        indice_cadena2 = i
        
        if cadena1[indice_cadena1] != cadena2[indice_cadena2]:
            coincide = False
    
    if coincide:
        cantidad = longitud

print("Coinciden", cantidad, "letras")