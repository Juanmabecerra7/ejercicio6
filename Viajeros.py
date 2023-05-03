class Viajeros:
    __num = ""
    __dni = ""
    __nombre = ""
    __apellido = ""
    __millas_acum = ""
    def __init__ (self, num, dni, nombre, apellido, millas_acum):
        self.__num = num
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__millas_acum = millas_acum

    def cantidadtotalmillas (self):
        return self.__millas_acum

    def __ad__(self, millas):
        self.millas_acum = int(self.__millas_acum) + millas
        return self.millas_acum

    def __sub__(self, canjear):
        if canjear <= int(self.__millas_acum):
             self.__millas_acum = int(self.__millas_acum) - canjear
        return self.__millas_acum

     
    def getNumeroViajero (self):
        return self.__num

    def __str__(self):
        return str(self.__num)+" "+self.__dni+" "+self.__nombre+" "+self.__apellido+" "+self.__millas_acum+" "
    
