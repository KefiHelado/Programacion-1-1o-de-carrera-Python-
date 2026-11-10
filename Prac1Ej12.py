horas = int(input("Indica la cantidad de horas que has tenido alquilada la bicicleta: "))
dias = horas/24
pagar = 0
if horas > 720:
    print("Cantidad de horas mayor a la de 1 mes")

elif horas < 24:
    print("Debes pagar 11€")
elif horas < 120 and horas >= 48:
    pagar = dias * 6

elif horas >= 120 and horas < 336:
    pagar = dias * 5.5

elif horas <= 336:
    pagar = dias * 3.67

print("Debes pagar {0}€".format(pagar))
    
