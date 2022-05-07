import numpy as np
import csv
from ClaseIntegrantes import Integrantes


class ManejadorIntegrantesProyecto:
    __cantidad = 0
    __dimension = 0
    __incremento = 1

    def __init__(self, dimension = 1, incremento = 1):
        self.__arregloIntegrantes = np.empty(dimension, dtype = Integrantes)
        self.__cantidad = 0
        self.__dimension = dimension
        self.__incremento = incremento

    def agregarIntegrante(self, unIntegrante):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__arregloIntegrantes.resize(self.__dimension)
        self.__arregloIntegrantes[self.__cantidad] = unIntegrante
        self.__cantidad += 1

    def testIntegrantes(self):
        archivo = open('integrantesProyecto.csv')
        reader = csv.reader(archivo, delimiter = ';')
        next(reader)
        for fila in reader:
            idProyecto, apellidoNombre, dni, categoriaInvestigacion, rol = fila[0], fila[1], fila[2], fila[3], fila[4],
            self.agregarIntegrante(Integrantes(idProyecto, apellidoNombre, dni, categoriaInvestigacion, rol))
            