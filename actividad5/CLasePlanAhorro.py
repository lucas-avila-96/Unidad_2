class PlanAhorro:
    __codigo = 0
    __modelo = ''
    __version = ''
    __valorVehiculo = 0.0
    __cuotasPlan = 60
    __cuotasLic = 10
    __valorCuota = 0

    def __init__(self, cod, mod, ver, val):
        self.__codigo = cod
        self.__modelo = mod
        self.__version = ver
        self.__valorVehiculo = val
        self.__valorCuota = (int(val)/int(self.getCuotasPlan())) + int(val) * 0.10

    def getCuotasPlan(cls):
        return cls.__cuotasPlan

    def getPrecioCuota(self):
        return self.__valorCuota
        
    def actualizarPrecio(self, valorActual):
        self.__valorVehiculo = valorActual

    def mostrarInfo(self):
        print(f'Codigo: {self.__codigo}')
        print(f'Modelo: {self.__modelo}')
        print(f'Version: {self.__version}')

    def mostrarMontoParaLicitar(self):
        print(f'Monto para licitar: {self.__valorCuota * self.__cuotasLic}')
    @classmethod
    def modificarCuotasLicitar(cls):
        print('Modificar cantidad de cuotas')
        cls.__cuotasLic = int(input('Cuotas para licitar:'))
    
    def __str__(self):
        return (f'Codigo:{self.__codigo}\nModelo:{self.__modelo}\nVersion:{self.__version}\nValor:{self.__valorVehiculo}\nCuotas del plan:{self.__cuotasPlan}\nCuotas p/Licitar:{self.__cuotasLic}\n')
