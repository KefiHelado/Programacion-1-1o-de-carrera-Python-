peso = float(input("Indica el peso de la persona en kg: "))
estatura = float(input("Indica la estatura: "))
IMC = peso/(estatura**2)
IMC = round (IMC, 2)
if IMC >= 40:
    print("Usted tiene un IMC de", IMC, "esto indica obseidad mórbida.")
elif IMC >= 30:
    print("Usted tiene un IMC de", IMC, "esto indica obseidad")
elif IMC >= 25:
    print("Usted tiene un IMC de", IMC, "esto indica sobrepeso.")
elif IMC < 24.99 and IMC > 18.5:
    print("Usted tiene un IMC de", IMC, "esto indica peso normal.")
elif IMC < 18.5:
    print("Usted tiene un IMC de", IMC, "esto indica bajo peso.")
