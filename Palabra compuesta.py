def palabra_compuesta(cadena, lista_cadenas):

    for i in range(len(lista_cadenas)):
        palabra1 = lista_cadenas[i]

        for j in range(len(lista_cadenas)):
            palabra2 = lista_cadenas[j]
            compuesta = palabra1 + palabra2

            if compuesta == cadena:
                return True
            
    return False            