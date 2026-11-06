def prefijo_comun_mas_largo(lista_cadenas):
    if not lista_cadenas:
        return ""

    if len(lista_cadenas) == 1:
        return lista_cadenas[0]

    cadena_mas_corta = min(lista_cadenas, key=len)

    for i in range(len(cadena_mas_corta)):
        caracter_actual = cadena_mas_corta[i]

        for cadena in lista_cadenas:
            if cadena[i] != caracter_actual:
                return cadena_mas_corta[:i]
    
    return cadena_mas_corta