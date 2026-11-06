def leer_datos_adn():
    M = []
    fichero = open("fasta.txt", "r")
    
    for linea in fichero:
        datos = linea.split('>')  
        identificador = datos[0]
        descripcion = datos[1]
        secuencia = datos[2]
        fila = [identificador, descripcion, secuencia]
        M.append(fila)

    fichero.close()
    return M

def son_complemento_inverso(secuencia1, secuencia2):
    secuencia2_invertida = secuencia2[::-1]
    
    if len(secuencia1) != len(secuencia2_invertida):
        return False
    
    for i in range(len(secuencia1)):
        base1 = secuencia1[i]
        base2 = secuencia2_invertida[i]
        
        if base1 == 'A' and base2 != 'T':
            return False
        elif base1 == 'T' and base2 != 'A':
            return False
        elif base1 == 'G' and base2 != 'C':
            return False
        elif base1 == 'C' and base2 != 'G':
            return False
    
    return True