class Email:
    __idCuenta = ''
    __dominio =''
    __tipoDominio = ''
    __contraseña = ''

    def __init__(self, idCuenta = '', dominio = '', tipoDominio = '', contraseña = ''):
        self.__idCuenta = idCuenta
        self.__dominio = dominio
        self.__tipoDominio = tipoDominio
        self.__contraseña = contraseña

    def retornaEmail(self):
        return (f'{self.__idCuenta}@{self.__dominio}.{self.__tipoDominio}')
    
    def getId(self):
        return(self.__idCuenta) 
    
    def getTipo(self):
        return (self.__tipoDominio)

    def getDominio(self):
        return(self.__dominio) 
    
    def updateContraseña(self):
        print("Actualizar contraseña.")
        while True:
            print('Ingrese la contraseña actual')    
            contraseñaActual = input('Contraseña: ')
            if(contraseñaActual == self.__contraseña):
                print('Ingrese nueva contraseña')
                nuevaContraseña = input('Nueva contraseña: ')
                self.__contraseña = nuevaContraseña
                print('La contraseña se modifico correctamente')
                break
            else: 
                print('contraseña actual incorrecta')

    def crearCuenta(self, direccion):
        arroba = direccion.find('@')
        punto = direccion.rfind('.')
        self.__idCuenta = direccion[ : arroba]
        self.__dominio = direccion[arroba + 1 : punto]
        self.__tipoDominio = direccion[punto + 1 : ]
