
class Integrantes:
    __idProyecto: 0
    __apellidoNombre = ''
    __dni = 0
    __categoriaInvestigacion = ''
    __rol = ''

    def __init__(self, idProyecto, apellidoNombre, dni, categoriaInvestigacion, rol):
        self.__idProyecto = idProyecto
        self.__apellidoNombre = apellidoNombre
        self.__dni = dni
        self.__categoriaInvestigacion = categoriaInvestigacion
        self.__rol = rol
