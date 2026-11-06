suspensos = int(input("Indica el número de suspensos "))
aprobados = int(input("Indica el número de aprobados "))
notables = int(input("Indica el número de notables "))
sobresalientes = int(input("Indica el número de sobresalientes "))
total = suspensos +  aprobados + notables + sobresalientes
print ("El porcentaje de suspensos es: ", (suspensos/total)*100)
print ("El porcentaje de aprobados es: ", (aprobados/total)*100)
print ("El porcentaje de notables es: ", (notables/total)*100)
print ("El porcentaje de sobresalientes es: ", (sobresalientes/total)*100)