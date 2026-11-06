def palabras_guipon():
    fichero = open("fichero.txt", "r")
    fichero2 = open("fichero2.txt", "w")
    for linea in fichero:
        palabras = linea.split()
        for palabra in palabras:
            if "-" in palabra:
                fichero2.write(palabra + "\n")
                
    fichero.close()
    fichero2.close()
    