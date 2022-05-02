import csv
from CLasePlanAhorro import PlanAhorro


class ManejadorPlanes:
    __listaPlanes = []

    def __init__(self):
        self.__listaPlanes = []

    def testPlanes(self):
        archivo = open('planes.csv')
        reader = csv.reader(archivo, delimiter = ';')

        for fila in reader:
            cod = fila[0]
            mod = fila[1]
            ver =  fila[2]
            valor = fila[3]
            unPlan = PlanAhorro(cod,mod,ver,valor)
            self.agregarPlan(unPlan)
        archivo.close()

    def __str__(self):
        s = ""
        for plan in self.__listaPlanes:
            s += str(plan) + '\n'
        return s

    def agregarPlan(self, unPlan):
        self.__listaPlanes.append(unPlan)

    def actualizarListaPrecios(self):
        for elemento in self.__listaPlanes:
            elemento.mostrarInfo()
            nuevoPrecio = input('Ingrese nuevo valor:')
            elemento.actualizarPrecio(nuevoPrecio)

    def vehiculoMenorValorCuota(self):
        valor = int(input('Ingrese valor: '))
        for elemento in self.__listaPlanes:
            if int(elemento.getPrecioCuota()) < valor:
                elemento.mostrarInfo()
        
    
    def montoParaLicitar(self):
        for elemento in self.__listaPlanes:
            elemento.mostrarMontoParaLicitar()
        
    def modificarCuotas(self):
        PlanAhorro.modificarCuotasLicitar()
    
