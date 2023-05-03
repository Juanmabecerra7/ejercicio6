from Viajeros import Viajeros
import csv

class ManejadorViajeros:
    def __init__(self):
        self.__listaviajeros = []

    def agregarviajero (self,unviajero):
        self.__listaviajeros.append(unviajero)

    def testviajeros(self):
        archivo=open("viajeros.csv")
        reader = csv.reader (archivo, delimiter= ",")
        for fila in reader:
            num = int(fila[0])
            dni = fila[1]
            nombre = fila[2]
            apellido = fila[3]
            millas_acum = fila[4]
            unviajero= Viajeros (num,dni,nombre,apellido,millas_acum)
            self.agregarviajero(unviajero)
        archivo.close()
    
    def __str__(self):
        s = ""
        for viajeros in self.__listaviajeros:
            s+=str(viajeros)+"\n"
        return s
    
    def buscarviajeros (self, numero):
        indice=0
        valorderetorno=None
        bandera=False
        while not bandera and indice < len(self.__listaviajeros):
            if self.__listaviajeros[indice].getNumeroViajero()==numero:
                bandera = True
                valorderetorno = indice
            else:
                indice= indice + 1
        return self.__listaviajeros[valorderetorno]
