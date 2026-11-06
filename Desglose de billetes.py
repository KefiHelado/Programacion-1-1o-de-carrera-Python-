total = int(input("Indica una cantidad de euros para el desglose: "))
c500 = 0
c200 = 0
c100 = 0
c50 = 0
c20 = 0
c10 = 0
c5 = 0
c2 = 0
c1 = 0

while total > 500:
    c500+=1
    total = total-500
while total > 200:
    c200+=1
    total = total-200
while total > 100:
    c100+=1
    total = total-100
while total > 50:
    c50+=1
    total = total-50
while total > 20:
    c20+=1
    total = total-20
while total > 10:
    c10+=1
    total = total-10
while total > 5:
    c5+=1
    total = total-5
while total > 2:
    c2+=1
    total = total-2
while total >= 1:
    c1+=1
    total = total-1


print("El total del desglose es el siguiente", "\nBilletes de 500: ", c500, "\nBilletes de 200: ", c200, "\nBilletes de 100: ", c100, "\nBilletes de 50: ", c50, "\nBilletes de 20: ", c20, "\nBilletes de 10: ", c10, "\nBilletes de 5: ", c5, "\nMonedas de 2: ", c2, "\nMonedas de 1: ", c1)