estudiantes = []
nombre = input("Indica el nombre del estudiante: ")
media = 0
maxima = 0
bucle = 0
minima = 11
while nombre != "":
    nota = float(input("Indica la nota del estudiante: "))
    estudiantes.append([nombre, nota])
    nombre = input("Indica el nombre del estudiante: ")
    if nota < minima:
        minima = nota
    
    if nota > maxima:
        maxima = nota
    bucle +=1
    media += nota

print("Lista de estudiantes: ")
for i in range(len(estudiantes)):
    print ({estudiantes[i][0]}, ":", {estudiantes[i][1]})

print("Nota media: ", media/bucle)
print("Nota minima: ", minima)
print("Nota maxima: ", maxima)

averiguar = input("Quieres saber la nota de un estudiante en concreto?: ")
if averiguar != "":
    for i in range(len(estudiantes)):
        if estudiantes[i][0] == averiguar:
            print({estudiantes[i][1]})