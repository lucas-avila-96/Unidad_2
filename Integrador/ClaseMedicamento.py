class Medicamento:
    __idCama = 0
    __idMedicamento = 0
    __nombre = ''
    __monodroga = ''
    __presentacion = ''
    __cant_aplicada = 0
    __precio = 0.0

    def __init__(self, idCama, idMed, nom, md, pr, ca, pc):
        self.__idCama = idCama
        self.__idMedicamento = idMed
        self.__nombre = nom
        self.__monodroga = md
        self.__presentacion = pr
        self.__cant_aplicada = ca
        self.__precio = pc
    