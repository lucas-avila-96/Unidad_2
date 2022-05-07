class Proyecto:
    __idProyecto = 0
    __titulo = ''
    __palabraClave = ''
    
    def __init__(self, idProyecto, titulo, palabrasClave):
        self.__idProyecto = idProyecto
        self.__titulo = titulo
        self.__palabraClave = palabrasClave

    def __gt__(self, otro):
        pass
    