

class Cama:
    __idCama = 0
    __habitacion = ''
    __estado = False
    __nomAp = None
    __diagnostico = ''
    __fecha_inter = ''
    __fecha_alta = ''
    
    def __init__(self, id, hab, est, na, diag, fi, fa):
        self.__idCama = id
        self.__habitacion = hab
        self.__estado = est
        self.__nomAp = na
        self.__diagnostico = diag
        self.__fecha_inter = fi
        self.__fecha_alta = fa
    
    def setFechaAlta(self, fecha):
        self.__fecha_alta = fecha
    
    def setEstado(self):
        self.__estado = False

    def getIdCama(self):
        return self.__idCama

    def getHabitacion(self):
        return self.__habitacion

    def getEstado(self):
        return self.__estado

    def getNombre(self):
        return self.__nomAp

    def getDiagnostico(self):
        return self.__diagnostico

    def getFechaInternacion(self):
        return self.__fecha_inter
    
    def getFechaAlta(self):
        return self.__fecha_alta

    def __str__(self):
        return(f'ID:{self.__idCama}\nHabitacion: {self.__habitacion}\nNombre: {self.__nomAp}\nEstado: {self.__estado}\n Diagnostico: {self.__diagnostico}\nFecha Internacion: {self.__fecha_inter}\nFecha Alta: {self.__fecha_alta}\t')