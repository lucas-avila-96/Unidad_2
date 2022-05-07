import csv
from ClaseProyecto import Proyecto


class ManejadorProyecto:
    __listaProyectos = []

    def __init__(self):
        self.__listaProyectos = []

    def agregarProyecto(self, unProyecto):
        self.__listaProyectos.append(unProyecto)

    def testProyectos(self):
        archivo = open('proyectos.csv')
        reader = csv.reader(archivo, delimiter=';')
        next(reader)
        for fila in reader:
            idProyecto, titulo, palabrasClave = fila[0], fila[1], fila[2]
            self.agregarProyecto(Proyecto(idProyecto, titulo, palabrasClave))