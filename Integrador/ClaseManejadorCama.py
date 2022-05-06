import numpy as np
import csv
from ClaseCama import Cama


class ManejadorCama:
    __cantidad = 0
    __dimension = 0
    __incremento = 1

    def __init__(self, dimension = 1, incremento = 1):
        self.__arregloCamas = np.empty(dimension, dtype = Cama)
        self.__cantidad = 0
        self.__dimension = dimension
        self.__incremento = incremento

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
            fechaInternacion = fila[5]
            fechaAlta = fila[6]
            self.agregarCama(Cama(id, habitacion, estado, apellidoNombre, diagnostico, fechaInternacion, fechaAlta))
            
    def buscarPaciente(self, nombre):
        i = 0
        band = False
        paciente = None
        while i < self.__arregloCamas.size and not band:
            if nombre == self.__arregloCamas[i].getNombre():
                paciente = self.__arregloCamas[i]
                band = True
            else:
                i += 1
        return paciente
        
    def buscarPacienteDiagnostico(self, diagnostico):
        pacientes = []
        for i in range(self.__cantidad):
            print(self.__arregloCamas[i].getDiagnostico())
            if diagnostico == self.__arregloCamas[i].getDiagnostico():
                pacientes.append(self.__arregloCamas[i])
        return pacientes