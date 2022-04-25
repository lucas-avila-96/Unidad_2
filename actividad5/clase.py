class PlanAhorro:
    __codigo = 0
    __modelo = ''
    __version = ''
    __valor_vehiculo = 0.0
    __cuotas_plan = 12
    __cuotas_lic = 8
    __valor_cuota = (__valor_vehiculo/__cuotas_plan) + __valor_vehiculo * 0.10

    def __init__(self, cod, mod, ver, val, cp, cl):
        self.__codigo = cod
        self.__modelo = mod
        self.__version = ver
        self.__valor = val
        self.__cuotas_plan = cp
        self.__cuotas_lic = cl
    def get_valor_cuota(self):
        return self.__valor_cuota
    def actualizar_valor_mensual(cls):
        pass
    def actualizar_valor(self, valor_actual):
        self.__valor_vehiculo = valor_actual
    def mostrar_info(self):
        print(f'Codigo: {self.__codigo}')
        print(f'Modelo: {self.__modelo}')
        print(f'Version: {self.__version}')

    def mostrar_monto_lic(self):
        pass
    def mod_cuotas(self):
        pass
