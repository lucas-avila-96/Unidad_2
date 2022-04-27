import numpy as np
import csv
from ClaseMedicamento import Medicamento

class ManejadorMedicamento:
    __cantidad = 0
    __dimension = 0
    __incremento = 1

    def __init__(self, dimension, incremento = 1):
        self.__arregloMedicamentos = np.empty(dimension, dtype = Medicamento)
        self.__cantidad = 0
        self.__dimension = dimension

    def agregarMedicamento(self, unMedicamento):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__arregloMedicamentos.resize(self.__dimension)
        self.__arregloMedicamentos[self.__cantidad] = unMedicamento
        self.__cantidad += 1

    def testMedicamentos(self):
        archivo = open('medicamentos.csv')
        reader = csv.reader(archivo, delimiter = ';')
        next(reader)

        for fila in reader:
            idCama = fila[0]
            idMedicamento = fila[1]
            nombreComercial = fila[2]
            monodroga = fila[3]
            presentacion = fila[4]
            cantidadAplicada = fila[5] 
            precioTotal = fila[6]
            self.agregarMedicamento(Medicamento(idCama, idMedicamento, nombreComercial, monodroga, presentacion, cantidadAplicada, precioTotal))
            