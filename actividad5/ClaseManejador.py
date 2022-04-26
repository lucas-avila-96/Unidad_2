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
            cantCuotasPlan = fila[4]
            cantCuotasLic = fila[5]
            unPlan = PlanAhorro(cod,mod,ver,valor, cantCuotasPlan, cantCuotasLic)
            self.agregar_plan(unPlan)
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
        valor = input('Ingrese valor: ')
        vehiculo = None
        for elemento in self.__listaPlanes:
            if(elemento.getPrecioCuota() < valor):
                elemento.mostrarInfo()
                vehiculo = elemento
        return vehiculo
    
    def montoParaLicitar(self):
        vehiculo = self.vehiculoMenorValorCuota()
        vehiculo.mostrarMontoParaLicitar()
        
    def modificarCuotas(self):
        PlanAhorro.modificarCuotasLicitar()
    
