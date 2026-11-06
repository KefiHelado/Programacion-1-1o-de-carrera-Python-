n = int(input("Indica el primer número entero positivo: "))
m = int(input("Indica el segundo número entero positivo: "))
j = 0
k = 0
if (n < 0) or (m < 0):
    print("Ambos números deben de ser positivos")
else:
    for i in range (1, n):
        if n % i == 0:
            j+=i
    for i in range (1, m):
        if m % i == 0:
            k+=i
    if j == m and k == n:
        print("Los números", n, "y", m, "son amigos. ")
    else:
        print("Los números", n, "y", m, "NO son amigos. ")
        