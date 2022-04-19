
class Registro:
    __temperatura: 0
    __humedad: 0
    __presion_atmosferica: 0

    def __init__(self, temperatura, humedad, presion):
        __temperatura = temperatura
        __humedad = humedad
        __presion = presion

    def get_temperatura(self):
        return self.__temperatura
    
    def get_humedad(self):
        return self.__humedad
    
    def get_presion(self):
        return self.__presion_atmosferica
    