
class ViajeroFrecuente:
    __num = 0
    __dni = ''
    __nombre = ''
    __apellido = ''
    __millas_acum = 0

    def __init__(self, num, dni, nombre, apellido):
        self.__num = num
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido

    def getNumero(self):
        return self.__num

    def cantidadTotalMillas(self):
        return (self.__millas_acum)
    
    def acumularMillas(self, millas_recorridas):
        self.__millas_acum += millas_recorridas
        return self.__millas_acum
    
    def canjearMillas(self, millas_a_canjear):
        if(millas_a_canjear <= self.__millas_acum):
            self.__millas_acum -= millas_a_canjear
            return self.__millas_acum
        else:
            print(f'Error, no se pudo realizar el canje')

