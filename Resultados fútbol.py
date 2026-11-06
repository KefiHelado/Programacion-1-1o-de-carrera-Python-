def leer_datos_partido():
    M = []
    fichero = open("fichero.txt", "r")
    
    for linea in fichero:
        datos = linea.split('#')  
        nombre1 = datos[0]
        goles1 = datos[1]
        nombre2 = datos[2]
        goles2 = datos[3]
        fila = [nombre1, goles1, nombre2, goles2]
        M.append(fila)

    fichero.close()
    return M

def resumen_datos_equipos(nombre, M):
    goles_totales= 0
    goles_recibidos = 0
    puntos_totales = 0
    for linea in M:
        if linea[0] == nombre:
            goles_totales += linea[1]
            goles_recibidos += linea[3]
            if linea[1] > linea[3]:
                puntos_totales += 3
            elif linea[1] == linea[3]:
                puntos_totales += 1

        elif linea[2] == nombre:
            goles_totales += linea[3]
            goles_recibidos += linea[1]
            if linea[1] < linea[3]:
                puntos_totales += 3
            elif linea[1] == linea[3]:
                puntos_totales += 1
        
    
    return(goles_totales, goles_recibidos, puntos_totales)

def mejor_clasificado(lista, M):
    mejor_equipo = ""
    max_puntos = -1
    max_diferencia = -1
    
    for equipo in lista:
        goles, recibidos, puntos = resumen_datos_equipos(equipo, M)
        diferencia = goles - recibidos

        if puntos > max_puntos:
            max_puntos = puntos
            max_diferencia = diferencia
            mejor_equipo = equipo
        
        elif puntos == max_puntos:
            if diferencia > max_diferencia:
                max_diferencia = diferencia
                mejor_equipo = equipo
    
    return mejor_equipo