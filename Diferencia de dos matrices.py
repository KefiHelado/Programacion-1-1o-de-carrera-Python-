m = int(input("Dime el número de filas de la matriz 1: "))
n = int(input("Dime el número de columnas de la matriz 1: "))
M = []
for i in range (m):
    M.append([0] * n )

for i in range (m):
    for j in range (n):
        M[i][j] = float(input("Dame el componente de la matriz 1 ({0}, {1}): ".format(i, j)))


m2 = int(input("Dime el número de filas de la matriz 2: "))
n2 = int(input("Dime el número de columnas de la matriz 2: "))
diferencia = 0
N = []
for i in range (m2):
    N.append([0] * n2 )

for i in range (m2):
    for j in range (n2):
        N[i][j] = float(input("Dame el componente de la matriz 2 ({0}, {1}): ".format(i, j)))

if m2 != m or n2 != n:
    print("Las matrices son de tamaño distinto.")

else: 
    for i in range (m):
        for j in range(n):
            if M[i][j] != N[i][j]:
                print("La diferencia está en la posición", i, j)
                diferencia = 1

if diferencia == 0:
    print("No hay diferencia entre las dos matrices.")
