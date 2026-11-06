def intercambio(lista1, lista2):
    lista3 = []
    if len(lista1) != len(lista2):
        return ""
    else:
        for i in range(len(lista1)):
            lista3.append (lista1[i])
        for i in range(len(lista2)):
            lista1[i] = lista2[i]
        for i in range(len(lista2)):
            lista2[i] = lista3[i]
    return (lista1, lista2)