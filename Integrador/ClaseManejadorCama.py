import numpy as np
import csv
from ClaseCama import Cama


class ManejadorCama:
    __cantidad = 0
    __dimension = 0
    __incremento = 1

    def __init__(self, dimension, incremento = 1):
        self.__arregloCamas = np.empty(dimension, dtype = Cama)
        self.__cantidad = 0
        self.__dimension = dimension

    def agregarCama(self, unaCama):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__arregloCamas.resize(self.__dimension)
        self.__arregloCamas[self.__cantidad] = unaCama
        self.__cantidad += 1

    def testCamas(self):
        archivo = open('camas.csv')
        reader = csv.reader(archivo, delimiter = ';')
        next(reader)

        for fila in reader:
            id = fila[0]
            habitacion = fila[1]
            estado = fila[2]
            apellidoNombre = fila[3]
            diagnostico = fila[4]
            fechaInternacion = fila[4]
            fechaAlta = fila[4]
            self.agregarCama(Cama(id, habitacion, estado, apellidoNombre, diagnostico, fechaInternacion, fechaAlta))
            
