m = int(input("Dime el número de filas de la matriz 1: "))
n = int(input("Dime el número de columnas de la matriz 1: "))
M = []
triangular = True

for i in range (m):
    M.append([0] * n )

for i in range (m):
    for j in range (n):
        M[i][j] = float(input("Dame el componente de la matriz 1 ({0}, {1}): ".format(i, j)))

if (m != n):
    print("Para que la matriz sea triangular superior debe de ser cuadrada.")
else:
    for i in range (m):
        for j in range(n):
            if i > j and M[i][j] != 0:
                triangular = False

                
if triangular == True:
    print ("Es triangular superior.")
else:
    print ("NO es trianglular superior.") 