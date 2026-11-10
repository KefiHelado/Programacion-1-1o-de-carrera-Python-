i = 0
for i in range(1,111):

    if (i%3!=0 and i%5!=0 and i%7!=0 and i%11!=0):
        print(i, end=" ")

    else:
        
        if i%3 == 0:
            print("Cosa", end="")

        if i%5 == 0:
            print("Losa", end="")

        if i%7 == 0:
            print("Wosa", end="")

        if i%11 == 0:
            print("", i, "\n", end="")

        else:
            print(" ", end="")
