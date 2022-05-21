from datetime import *

def login(select, resultado):
    hoy = datetime.today()

    access = open("log.txt",'a')

    if (select == 1):
        access.write(str(hoy) + " Suma: " + str(resultado) + "\n")
        access.close()

    elif (select == 2):
        access.write(str(hoy) + " Resta: " + str(resultado) + "\n")
        access.close()

    elif (select == 3):
        access.write(str(hoy) + " Multiplicación: " + str(resultado) + "\n")
        access.close()

    elif (select == 4):
        access.write(str(hoy) + " División: " + str(resultado) + "\n")
        access.close()
    
    elif (select == 5):
        access.write(str(hoy) + " Seno: " + str(resultado) + "\n")
        access.close()

    elif (select == 6):
        access.write(str(hoy) + " Coseno: " + str(resultado) + "\n")
        access.close()

    elif (select == 7):
        access.write(str(hoy) + " Tangente: " + str(resultado) + "\n")
        access.close()

    elif (select == 8):
        access.write(str(hoy) + " Numeros pares: " + str(resultado) + "\n")
        access.close()