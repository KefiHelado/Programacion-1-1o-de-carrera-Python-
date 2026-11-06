total = int(input("Indica una cantidad de euros para el desglose: "))

c500 = total // 500
total %= 500

c200 = total // 200
total %= 200

c100 = total // 100
total %= 100

c50 = total // 50
total %= 50

c20 = total // 20
total %= 20

c10 = total // 10
total %= 10

c5 = total // 5
total %= 5

c2 = total // 2
total %= 2

c1 = total

print(
    "El total del desglose es el siguiente",
    "\nBilletes de 500:", c500,
    "\nBilletes de 200:", c200,
    "\nBilletes de 100:", c100,
    "\nBilletes de 50:", c50,
    "\nBilletes de 20:", c20,
    "\nBilletes de 10:", c10,
    "\nBilletes de 5:", c5,
    "\nMonedas de 2:", c2,
    "\nMonedas de 1:", c1
)
