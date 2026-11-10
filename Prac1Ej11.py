peso = int(input("Indicame tu peso en kg: "))
altura = float(input("Indicame tu altura en m: "))
IMC = (peso/(altura**2))
if(IMC >= 40):
    print("Obesidad mórbida")
elif(IMC >= 30):
    print("Obesidad")
elif(IMC >= 25):
    print("Sobrepeso")
elif(IMC < 18.5):
    print("Bajo peso")
else:
    print("Peso normal")
