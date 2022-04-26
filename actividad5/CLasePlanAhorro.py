class PlanAhorro:
    __codigo = 0
    __modelo = ''
    __version = ''
    __valorVehiculo = 0.0
    __cuotasPlan = 60
    __cuotasLic = 10
    __valorCuota = (__valorVehiculo/__cuotasPlan) + __valorVehiculo * 0.10

    def __init__(self, cod, mod, ver, val, cp, cl):
        self.__codigo = cod
        self.__modelo = mod
        self.__version = ver
        self.__valorVehiculo = val
        self.__cuotasPlan = cp
        self.__cuotasLic= cl

    def getPrecioCuota(self):
        return self.__valor_cuota

    def actualizarValorMensual(cls):
        pass

    def actualizarPrecio(self, valor_actual):
        self.__valorVehiculo = valor_actual

    def mostrarInfo(self):
        print(f'Codigo: {self.__codigo}')
        print(f'Modelo: {self.__modelo}')
        print(f'Version: {self.__version}')

    def mostrarMontoParaLic(self):
        print(f'Monto para licitar: {self.__valorCuota * self.__cuotasLic}')

    def modificarCuotasLicitar(cls):
        print('Modificar cantidad de cuotas')
        cls.__cuotasLic = input('Cuotas para licitar:')
    
    def __str__(self):
        return (f'Codigo:{self.__codigo}\nModelo:{self.__modelo}\nVersion:{self.__version}\nValor:{self.__valorVehiculo}\nCuotas del plan:{self.__cuotasPlan}\nCuotas p/Licitar:{self.__cuotasLic}\n')
