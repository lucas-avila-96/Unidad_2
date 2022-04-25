
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

    def __str__(self):
        return (f'Nombre: {self.__nombre}\nMillas acumuladas: {self.__millas_acum}')
        
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
        return ViajeroFrecuente(self.__num, self.__dni, self.__nombre, self.__apellido,
            self.__millas_acum + otro)

    __radd__ = __add__

    def __sub__(self, otro):
        if self.__millas_acum >= otro:
            print(f'Canjeaste {otro} millas')
            return ViajeroFrecuente(self.__num, self.__dni, self.__nombre, self.__apellido,
                self.__millas_acum - otro)
        else: print('No se realizo el canje. Millas insuficientes')

    __rsub__ = __sub__

    def __eq__(self, otro):
        return self.__millas_acum == otro
    __req__ = __eq__