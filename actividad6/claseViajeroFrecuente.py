
class ViajeroFrecuente:
    __num = 0
    __dni = ''
    __nombre = ''
    __apellido = ''
    __millas_acum = 0

    def __init__(self, num, dni, nombre, apellido, millas = 0):
        self.__num = num
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__millas_acum = millas

    def getNumero(self):
        return self.__num
    
    def get_nombre(self):
        return self.__nombre
    def cantidadTotalMillas(self):
        return self.__millas_acum
    
    def __gt__(self, otro):
        if self.__millas_acum > otro.__millas_acum :
            return True
    def __add__(self, otro):
        return ViajeroFrecuente(self.__num, self.__dni, self.__nombre, self.__apellido, self.__millas_acum + otro)

    def __sub__(self, otro):
        return ViajeroFrecuente(self.__num, self.__dni, self.__nombre, self.__apellido, self.__millas_acum - otro)
        
    def __eq__(self, otro):
        if self.__millas_acum == otro.__millas_acum:
            return True