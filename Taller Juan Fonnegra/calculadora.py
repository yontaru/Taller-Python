from funciones import *

from access import *


user = input('Bienvenido a la calculadora, ¿cuál es su nombre?: ')

def main():

    print('\nBienvenido', user, 'seleccione la operación que quiere usar\n\n')
    print('1. Suma')
    print('2. Resta')
    print('3. Multiplicación')
    print('4. División')
    print('5. Seno')
    print('6. Coseno')
    print('7. Tangente')
    print('8. Numeros Páres')
    print('0. Salir')

    select = int(input('¿Qué operación desea realizar?: '))

    if(select==0):
        print('Muchas gracias', user, 'por usar la calculadora')
        quit()

    elif (select > 8):
        print('Por favor seleccione las opciones indicadas')
        return main()

    else:
        a = int(input('Escriba el primer número: '))

        if (select < 5):
            b = int(input('\nEscriba el segundo número: '))

        if(select == 1):
            resultado=sumar(a, b)
            print("\nEl resultado de ", a , "+", b, "es igual a", resultado)
            login(select,resultado)
            return main()

        elif(select == 2):
            resultado=restar(a, b)
            print("\nEl resultado de ", a , "-", b, "es igual a", resultado)
            login(select,resultado)
            return main()


        elif(select == 3):
            resultado=multiplicar(a, b)
            print("\nEl resultado de ", a , "*", b, "es igual a", resultado)
            login(select,resultado)
            return main()

        
        elif(select == 4):
            if(b == 0):
                print("\nEl número que ingresó es 0 y no se puede dividir por cero")
                return main()
            

            else:
                resultado=dividir(a, b)
                print("\nEl resultado de ", a , "/", b, "es igual a", resultado)
                login(select,resultado)
                return main()
 

        elif(select == 5):
            resultado=seno(a)
            print("\nEl seno de", a , "es igual a", resultado)
            login(select,resultado)
            return main()
  

        elif(select == 6):
            resultado=coseno(a)
            print("\nEl coseno de", a , "es igual a", resultado)
            login(select,resultado)
            return main()


        elif(select == 7):
            resultado=tangente(a)
            print("\nLa tangente de", a , "es igual a", resultado)
            login(select,resultado)
            return main()

        
        elif(select == 8):
            print("\nLos números pares que hay antes del", a , "son:")
            resultado=numerospares(a)
            login(select,resultado)
            return main()

main()