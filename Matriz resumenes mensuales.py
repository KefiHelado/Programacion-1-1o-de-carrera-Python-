def media_historica_datos_mes(matriz, mes):

    media_temperaturas_maximas = 0
    media_temperaturas_minimas = 0
    numero_dias_helado = 0
    total_precipitaciones = 0
    total_horas_de_sol = 0
    contador = 0

    for i in range(len(matriz)):
        if matriz[i][1] == mes:
            media_temperaturas_maximas += matriz[i][2]
            media_temperaturas_minimas += matriz[i][3]
            numero_dias_helado += matriz[i][4]
            total_precipitaciones += matriz[i][5]
            total_horas_de_sol += matriz[i][6]
            contador += 1
    
    if contador == 0:
        return []
    
    return [mes, 
            media_temperaturas_maximas / contador,
            media_temperaturas_minimas / contador,
            numero_dias_helado / contador,
            total_precipitaciones / contador,
            total_horas_de_sol / contador]

def año_mas_caluroso_que_la_media(matriz, año):
    for i in range(len(matriz)):
        if matriz[i][0] == año:
            mes_actual = matriz[i][1]
            temp_max_actual = matriz[i][2]
            resultado_media = media_historica_datos_mes(matriz, mes_actual)
            temp_max_media = resultado_media[1]
            
            if temp_max_actual >= temp_max_media:
                return True
            else:
                return False
        else:
            return ""
