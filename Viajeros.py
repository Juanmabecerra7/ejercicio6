class Viajero:
    __num = ""
    __dni = ""
    __nombre = ""
    __apellido = ""
    __millas_acum = ""
    
    def __init__(self, num, dni, nombre,apellido, millas_acum):
        self.__num = num
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__millas_acum = millas_acum
        
    def cantidadTotalMillas (Self):
        return Self.__millas_acum
    
    def getnum(self):
        return int (self.__num)
    
    def getmillas (self):
        return int (self.__millas_acum)
    
    def __ge__(self, otro):
        maximo = 0
        print("Evaluando si son mayores")
        if int(self.__millas_acum) >= int(otro):
            maximo = int(self.__millas_acum)
        else:
            maximo = int(otro)
        return maximo

    def __add__(self, otro):
        self.__millas_acum = int(self.__millas_acum) + int(otro)
        return str("{}, {}, {}, {}, {}").format(self.__num, self.__dni, self.__nombre, self.__apellido, self.__millas_acum)

    def __sub__(self, otro):
        self.__millas_acum = self.__millas_acum = int(self.__millas_acum) - int(otro)
        return str("{}, {}, {}, {}, {}").format(self.__num, self.__dni, self.__nombre, self.__apellido, self.__millas_acum)

    def __str__(self):
        return str("{},{},{},{},{}").format (self.__num, self.__dni, self.__nombre, self.__apellido, self.__millas_acum)
    
