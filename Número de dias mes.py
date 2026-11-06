mes = str(input("Dime un mes del año: "))
mes_minusculas = mes.lower()
año = int(input("Dime un año: "))
dias = 0

if mes_minusculas in ("enero", "marzo", "mayo", "julio", "agosto", "octubre", "diciembre" ):
    dias = 31

elif mes_minusculas in ("abril", "junio", "septiembre", "noviembre"):
    dias = 30

elif mes_minusculas == "febrero" and ((año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)):
    dias = 29

else:
    dias = 28

print (mes,"de", año, "tiene", dias, "días")