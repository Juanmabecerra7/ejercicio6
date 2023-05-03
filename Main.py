from Viajeros import Viajeros
from ManejadorViajeros import ManejadorViajeros

if __name__=="__main__":
    mv = ManejadorViajeros()
    mv.testviajeros()
    print(str(mv))
    numero = int (input("ingrese el numero de un viajero:"))
    while numero != 0:
       unviajero = mv.buscarviajeros(numero)
       if unviajero==None:
            print ('---El viajero ingresado no exite---')
       else:
          while numero != 0:
            print("1: Consutar Cantidad de Millas del Viajero")
            print("2: Acumular Millas")
            print("3: Canjear Millas")
            print("4: Elegir un nuevo viajero")
            print("5: Acumular Todas las Millas")
            print("6: Salir")
            opcion= int (input())
            if opcion == 1:
               print (Viajeros.cantidadtotalmillas(unviajero))
            elif opcion == 2:
                millas= int(input("ingrese la cantidad de millas acumuladas: "))
                print (Viajeros.acumularmillas(unviajero,millas))
            elif opcion == 3:
                canjear= int(input("ingrese la cantidad de millas a canjear: "))
                print (Viajeros.canjearmillas(unviajero, canjear))
            elif opcion==4:
                numero = 0
            elif opcion==5:
                print (Viajeros.__add__(unviajero))
            elif opcion ==6:
                print(Viajeros.__sub__(unviajero))
            elif opcion==6:
                exit()
            else:
                print ("---Opcion Incorrecta---")
    numero = int(input("ingrese el numero de un viajero"))
       
