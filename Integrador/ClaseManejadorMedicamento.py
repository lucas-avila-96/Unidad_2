import numpy as np
import csv
from ClaseMedicamento import Medicamento

class ManejadorMedicamento:
    __listaMedicamentos = []

    def __init__(self):
        self.__listaMedicamentos = []

    def agregarMedicamento(self, unMedicamento):
        
        self.__listaMedicamentos.append(unMedicamento)

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
    
    def buscarMedicamento(self, id):
        medicamentosPaciente = []
        for i in self.__arregloCamas.size:
            if id == self.listaMedicamentos[i].getIdCama():
                medicamentosPaciente.append(self.listaMedicamentos[i])
        return medicamentosPaciente