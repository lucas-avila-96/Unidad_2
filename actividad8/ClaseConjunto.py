from main import C


class Conjunto:
    __lista = []

    def __init__(self, objLista = []):
        self.__lista = objLista
    
    def __add__(self, otro):
        union = []
        for i in range(len(self.__lista)):
                if(self.__lista[i] <= otro.__lista[i]):
                    union.append(self.lista[i])

        return Conjunto(union)
    def __sub__(self, otro):
        resta = []

        return Conjunto(resta)

    def __eq__(self, otro):
        