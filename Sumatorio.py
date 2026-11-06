n = int(input("Indica el primer valor de n: "))
m = int(input("Indica el último valor de n: "))
k = 0
for i in range(n, m+1):
    k+=i
print("El valor final del sumatorio es:", k)