
class Conjunto:
    __lista = []

    def __init__(self, objLista = []):
        self.__lista = objLista
    
    def __str__(self):
        return (f'{self.__lista}')

    def __add__(self, otro):
        result = list(self.__lista)
        for n in otro.__lista:
            if not n in result:
                result.append(n)
        return Conjunto(result)

    def __sub__(self, otro):
        result = list(self.__lista)
        i = 0
        while i <len(result):
            if result[i] in otro.__lista:
                result.pop(i)
            else:
                i += 1
        return Conjunto(result)

    def __eq__(self, otro):
        esIgual = True
        if len(self.__lista) == len(otro.__lista):
            i = 0
            while i < len(self.__lista) and esIgual:
                if self.__lista[i] in otro.__lista:
                    i += 1
                else:
                    esIgual = False
        else: esIgual = False
        return esIgual
                
                