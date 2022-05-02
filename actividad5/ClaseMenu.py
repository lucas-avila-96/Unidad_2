from ClaseManejador import ManejadorPlanes
class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { '1':self.opcion1,
                            '2':self.opcion2,
                            '3':self.opcion3,
                            '4':self.opcion4
                            }
    def opcion(self,op, mp):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        if op == '1' or op == '2' or op == '3' or op == '4':
            func(mp)
        else:
            func()
    
    def opcion1(self, mp):
        mp.actualizarListaPrecios()
    def opcion2(self, mp):
        mp.vehiculoMenorValorCuota()
    def opcion3(self, mp):
        mp.montoParaLicitar()
    def opcion4(self, mp):
        mp.modificarCuotas()