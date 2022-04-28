

class ViajeroFrecuente:
    __num = 0
    __dni = ''
    __nombre = ''
    __apellido = ''
    __millas_acum = 0

    def __init__(self, num, dni, nombre, apellido, millas):
        self.__num = num
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__millas_acum = millas

    def getNumero(self):
        return self.__num

    def cantidadTotalMillas(self):
        print(f'Cantidad de millas: {self.__millas_acum}')
    
    def acumularMillas(self):
        print('Ingresar millas a acumular')
        millas = input('millas: ')
        self.__millas_acum += millas
    
    def canjearMillas(self):
        print('Ingresar millas a canjear')
        millas_a_canjear = input('Millas: ')
        if millas_a_canjear <= self.__millas_acum:
            self.__millas_acum -= millas_a_canjear
            print('millas canjeadas')
        else:
            print(f'Error, no se pudo realizar el canje')
